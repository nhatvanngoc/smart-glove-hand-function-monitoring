"""
EXP-01: Hybrid Calibration — Velostat vs Hybrid comparison
==========================================================
So sánh sai số và drift giữa Velostat thuần vs Hybrid (Velostat + Piezocap).

Acceptance: Hybrid RMSE < Velostat RMSE × 0.8 (i.e., giảm ≥ 20%).
"""
from __future__ import annotations
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import numpy as np

from src.pressure_model.cross_calibration import HybridCalibrator


def velostat_only(v_raw, _):
    """Naive Velostat → pressure without calibration."""
    return v_raw * 0.4  # placeholder scale (ADC → mmHg)


def run_experiment(seed: int = 7, T: int = 300):
    rng = np.random.RandomState(seed)
    cal = HybridCalibrator()

    err_vel = []
    err_hyb = []
    drift_over_time = {k: [] for k in ["vel", "hyb"]}

    for t in range(T):
        # True pressure with sacrum hotspot
        true_p = 25 + rng.rand(64) * 10
        true_p[27:36] += 12  # sacrum zone in flat index
        # Velostat drift grows over time
        drift = 0.08 * t
        v_raw = (2.0 * true_p + drift + rng.randn(64) * 1.5).clip(0, 255)
        v_raw = v_raw.astype(np.float32)

        # Piezocapacitive at anchors (no drift)
        p_pz = np.array([true_p[c] for c in cal.anchor_cells]) + rng.randn(8) * 0.3

        # Velostat only
        p_vel = velostat_only(v_raw, None).reshape(8, 8)

        # Hybrid (cross-calibrated)
        p_hyb = cal.calibrate(v_raw, p_pz)

        err_vel.append(np.sqrt(((p_vel - true_p.reshape(8, 8))**2).mean()))
        err_hyb.append(np.sqrt(((p_hyb - true_p.reshape(8, 8))**2).mean()))

        drift_over_time["vel"].append(drift)
        drift_over_time["hyb"].append(float(cal.a * drift + cal.b))

    rmse_vel = float(np.sqrt(np.mean(np.array(err_vel)**2)))
    rmse_hyb = float(np.sqrt(np.mean(np.array(err_hyb)**2)))
    drift_final_vel = float(np.mean(np.abs(drift_over_time["vel"][-50:])))
    drift_final_hyb = float(np.mean(np.abs(drift_over_time["hyb"][-50:])))

    print("=" * 60)
    print("EXP-01: Hybrid Calibration")
    print("=" * 60)
    print(f"Velostat-only  RMSE:  {rmse_vel:.3f} mmHg")
    print(f"Hybrid         RMSE:  {rmse_hyb:.3f} mmHg")
    print(f"Reduction:            {(1 - rmse_hyb / rmse_vel) * 100:.1f}%")
    print(f"Velostat drift (last 50 ticks): {drift_final_vel:.2f} mmHg")
    print(f"Hybrid drift    (last 50 ticks): {drift_final_hyb:.2f} mmHg")
    print()
    print(f"Acceptance (Hybrid < Velostat × 0.8): {'✓ PASS' if rmse_hyb < rmse_vel * 0.8 else '✗ FAIL'}")
    return {"rmse_vel": rmse_vel, "rmse_hyb": rmse_hyb,
            "drift_vel": drift_final_vel, "drift_hyb": drift_final_hyb}


if __name__ == "__main__":
    run_experiment()
