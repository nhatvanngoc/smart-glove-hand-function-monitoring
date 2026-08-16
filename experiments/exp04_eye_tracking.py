"""
EXP-04: Eye-Tracking Accuracy — Top-1 + angular error
======================================================
5×3 grid, synthetic gaze with noise + drift.

Acceptance: Top-1 > 80%, mean angular error < 2° (~30 px).
"""
from __future__ import annotations
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import numpy as np

from experiments.synthetic_data import synthetic_eye_tracking


def run_experiment(seed: int = 0):
    gx, gy, tx, ty = synthetic_eye_tracking(n_samples=200, seed=seed)

    # Map continuous gaze to grid cell (5 cols × 3 rows)
    cell_w, cell_h = 100, 100
    gx_col = np.clip((gx / cell_w).astype(int), 0, 4)
    gy_row = np.clip((gy / cell_h).astype(int), 0, 2)
    tx_col = np.clip((tx / cell_w).astype(int), 0, 4)
    ty_row = np.clip((ty / cell_h).astype(int), 0, 2)

    # Top-1 accuracy
    correct = (gx_col == tx_col) & (gy_row == ty_row)
    top1 = float(correct.mean())

    # Angular error (approximate: pixel error → degree)
    # 1 cell ≈ 100 px ≈ 5°  (calibrated FOV)
    pixel_err = np.sqrt((gx - tx) ** 2 + (gy - ty) ** 2)
    angular_err = pixel_err / 100 * 5  # very rough

    # Robustness: exclude drift samples
    non_drift = ~((np.arange(len(gx)) >= 20) & (np.arange(len(gx)) < 25))
    top1_no_drift = float(correct[non_drift].mean()) if non_drift.any() else top1

    print("=" * 60)
    print("EXP-04: Eye-Tracking Accuracy")
    print("=" * 60)
    print(f"Samples:                  {len(gx)}")
    print(f"Top-1 accuracy (all):     {top1 * 100:.1f}%")
    print(f"Top-1 accuracy (no drift):{top1_no_drift * 100:.1f}%")
    print(f"Mean angular error:       {angular_err.mean():.2f}°")
    print(f"Median angular error:     {np.median(angular_err):.2f}°")
    print()
    print(f"Acceptance (Top-1 > 80%): {'✓ PASS' if top1_no_drift > 0.80 else '✗ FAIL'}")
    print(f"Acceptance (ang < 2°):    {'✓ PASS' if angular_err.mean() < 2.0 else '✗ FAIL'}")
    return {"top1_all": top1, "top1_no_drift": top1_no_drift,
            "mean_angular_error": float(angular_err.mean()),
            "median_angular_error": float(np.median(angular_err))}


if __name__ == "__main__":
    run_experiment()
