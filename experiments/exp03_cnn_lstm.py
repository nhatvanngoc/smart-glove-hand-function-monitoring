"""
EXP-03: CNN-LSTM Forecaster — AUC + MAE
========================================
Đo MAE, AUC-ROC cho high-risk detection (PTI ≥ 2.0 trong 1-5 phút tới).

Acceptance: MAE < 0.15, AUC > 0.85.
"""
from __future__ import annotations
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import numpy as np

from src.pressure_model.cnn_lstm import CNNLSTM
from src.pressure_model.pti_engine import compute_pti, classify_risk
from experiments.synthetic_data import synthetic_pressure_sequence


def build_input(frames: np.ndarray, posture: int) -> np.ndarray:
    """Build 60-frame × 8×8 × 3 input from raw pressure sequence."""
    ch0 = frames / 80.0
    pti = compute_pti(frames, posture)
    ch1 = np.broadcast_to((pti >= 2.0).astype(np.float32)[None], frames.shape).copy()
    ch2 = np.full_like(frames, posture / 2.0)
    return np.stack([ch0, ch1, ch2], axis=-1)


def run_experiment(seed: int = 42, n_test: int = 20):
    data, posture = synthetic_pressure_sequence(T=600, n_volunteers=5, seed=seed)
    rng = np.random.RandomState(seed + 1)

    model = CNNLSTM(seed=seed)

    y_true = []
    y_pred = []

    for v in range(min(n_test, data.shape[0])):
        p_seq = data[v]
        post_v = int(posture[v, 0])
        for start in range(0, p_seq.shape[0] - 60 - 30, 60):
            window = p_seq[start:start + 60]
            future = p_seq[start + 60:start + 90]   # next 30 frames (3 min @ 10 Hz)

            # Target: max PTI in next 3 min
            future_pti = compute_pti(future, post_v)
            target = float((future_pti >= 2.0).any())

            # Build input + predict
            inp = build_input(window, post_v)
            pred = model.forward(inp)

            y_true.append(target)
            y_pred.append(pred)

    y_true = np.array(y_true)
    y_pred = np.array(y_pred)

    mae = float(np.mean(np.abs(y_pred - y_true)))
    rmse = float(np.sqrt(((y_pred - y_true) ** 2).mean()))

    # AUC-ROC
    from sklearn.metrics import roc_auc_score
    try:
        auc = float(roc_auc_score(y_true, y_pred))
    except ValueError:
        auc = float("nan")

    print("=" * 60)
    print("EXP-03: CNN-LSTM Forecaster")
    print("=" * 60)
    print(f"Test samples:        {len(y_true)}")
    print(f"MAE:                 {mae:.4f}")
    print(f"RMSE:                {rmse:.4f}")
    print(f"AUC-ROC:             {auc:.4f}")
    print(f"Mean predicted risk: {y_pred.mean():.4f}")
    print(f"Mean true risk:      {y_true.mean():.4f}")
    print()
    print(f"Acceptance (MAE < 0.15):  {'✓ PASS' if mae < 0.15 else '✗ FAIL'}")
    print(f"Acceptance (AUC > 0.85):  {'✓ PASS' if auc > 0.85 else '✗ FAIL'}")
    return {"mae": mae, "rmse": rmse, "auc": auc, "n_samples": len(y_true)}


if __name__ == "__main__":
    run_experiment()
