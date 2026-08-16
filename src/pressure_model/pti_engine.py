"""
PTI Engine — Pressure-Time-Intensity
=====================================
Tính chỉ số tích lũy nguy cơ loét tì đè cho mỗi ô của ma trận cảm biến 8x8.

PTI(t) = ∫₀ᵗ w_posture(τ) · (P(τ) / P_th(τ)) dτ

Input:
    p_history: ndarray (T, 8, 8) — áp suất mmHg theo thời gian
    posture_class: int ∈ {0=supine, 1=lateral, 2=prone}
Output:
    pti: ndarray (8, 8) — chỉ số PTI cho mỗi ô
    risk: ndarray (8, 8) ∈ {0=low, 1=mod, 2=high, 3=critical}

Theo ARS Stage 2 — design phase.
"""
from __future__ import annotations
import numpy as np


# Threshold map (mmHg) per cell — clinical baseline
# Index: [posture_class, cell_i, cell_j]
THRESHOLD_MAP = {
    0: np.array([  # supine — sacrum, heels, trochanter, scapula, ...
        [40, 40, 40, 40, 40, 40, 40, 40],
        [40, 40, 40, 40, 40, 40, 40, 40],
        [35, 35, 35, 32, 32, 35, 35, 35],   # sacrum zone (rows 2..3)
        [35, 35, 32, 32, 32, 32, 35, 35],
        [35, 35, 32, 32, 32, 32, 35, 35],
        [35, 35, 35, 32, 32, 35, 35, 35],
        [40, 40, 40, 40, 40, 40, 40, 40],
        [30, 30, 30, 30, 30, 30, 30, 30],   # heels row
    ], dtype=np.float32),
    1: np.array([  # lateral — trochanter high
        [40, 40, 40, 40, 40, 40, 40, 40],
        [40, 40, 40, 40, 40, 40, 40, 40],
        [35, 35, 35, 35, 35, 35, 35, 35],
        [35, 35, 35, 35, 35, 35, 35, 35],
        [30, 30, 30, 30, 30, 30, 30, 30],   # trochanter row
        [35, 35, 35, 35, 35, 35, 35, 35],
        [40, 40, 40, 40, 40, 40, 40, 40],
        [40, 40, 40, 40, 40, 40, 40, 40],
    ], dtype=np.float32),
    2: np.array([  # prone — scapula, knees
        [35, 35, 35, 35, 35, 35, 35, 35],   # scapula
        [40, 40, 40, 40, 40, 40, 40, 40],
        [40, 40, 40, 40, 40, 40, 40, 40],
        [40, 40, 40, 40, 40, 40, 40, 40],
        [40, 40, 40, 40, 40, 40, 40, 40],
        [40, 40, 40, 40, 40, 40, 40, 40],
        [35, 35, 35, 35, 35, 35, 35, 35],   # knees
        [40, 40, 40, 40, 40, 40, 40, 40],
    ], dtype=np.float32),
}

POSTURE_WEIGHT = {0: 1.0, 1: 1.2, 2: 1.1}


def compute_pti(p_history: np.ndarray, posture_class: int = 0) -> np.ndarray:
    """Compute Pressure-Time-Intensity per cell.

    Parameters
    ----------
    p_history : (T, 8, 8) array of mmHg values over time
    posture_class : int ∈ {0, 1, 2}

    Returns
    -------
    pti : (8, 8) array, dimensionless cumulative risk
    """
    p_history = np.asarray(p_history, dtype=np.float32)
    assert p_history.ndim == 3 and p_history.shape[1:] == (8, 8), \
        f"Expected (T, 8, 8), got {p_history.shape}"

    p_th = THRESHOLD_MAP[posture_class]
    w = POSTURE_WEIGHT[posture_class]

    # Pressure ratio, clipped to [0, 5]
    ratio = p_history / p_th[None, :, :]    # (T, 8, 8)
    weighted = np.clip(ratio * w, 0, 5)

    # Cumulative sum over time → PTI per cell
    pti = weighted.sum(axis=0)              # (8, 8)
    return pti


def classify_risk(pti: np.ndarray) -> np.ndarray:
    """Map PTI values to risk levels.

    Returns
    -------
    risk : (8, 8) int ∈ {0=low, 1=mod, 2=high, 3=critical}
    """
    risk = np.zeros_like(pti, dtype=np.int32)
    risk[(pti >= 1.0) & (pti < 2.0)] = 1
    risk[(pti >= 2.0) & (pti < 3.0)] = 2
    risk[pti >= 3.0] = 3
    return risk


def risk_map_for_dashboard(p_history: np.ndarray, posture_class: int = 0) -> dict:
    """Convenience for dashboard."""
    pti = compute_pti(p_history, posture_class)
    risk = classify_risk(pti)
    peak = float(p_history.max())
    mean_sacrum = float(p_history[:, 3:6, 3:6].mean())  # sacrum zone
    tot = float((p_history > 32).mean())
    return {
        "pti": pti,
        "risk": risk,
        "peak_mmHg": peak,
        "mean_sacrum_mmHg": mean_sacrum,
        "time_over_threshold_pct": tot * 100.0,
    }


if __name__ == "__main__":
    # Smoke test
    rng = np.random.RandomState(42)
    T = 600  # 60 seconds @ 10 Hz
    p_history = rng.rand(T, 8, 8) * 30 + 10  # 10–40 mmHg
    p_history[:, 3:6, 3:6] += 20  # sacrum hotspot
    out = risk_map_for_dashboard(p_history, posture_class=0)
    print("Peak:", out["peak_mmHg"])
    print("Mean sacrum:", out["mean_sacrum_mmHg"])
    print("TOT %:", out["time_over_threshold_pct"])
    print("PTI map:")
    print(out["pti"].round(2))
    print("Risk map:")
    print(out["risk"])
