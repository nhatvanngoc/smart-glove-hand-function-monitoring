"""
Cross-Calibration — Velostat ↔ Piezocapacitive Hybrid
=====================================================
Online Kalman-filter style calibration để giảm drift của Velostat và sai số
tích lũy khi đo liên tục.

Piezocapacitive (8 anchors) cung cấp reference chính xác; Velostat (64 cells)
phủ rộng nhưng drift → cần hiệu chuẩn liên tục.

Theo ARS Stage 2 — design + design patent on hybrid cross-cal.
"""
from __future__ import annotations
import numpy as np
from dataclasses import dataclass, field
from typing import Tuple


@dataclass
class HybridCalibrator:
    """State-space model:
        State:      true pressure P_true (8x8)
        Obs_vel:    V = a·P + b + noise_vel  (drift)
        Obs_pz:     P = P_true + noise_pz     (anchor)

        Online update mỗi N steps using piezocapacitive anchors as truth.
    """
    n_cells: int = 64
    n_anchors: int = 8
    # Anchor positions: which 8 cells overlap with piezocap nodes
    anchor_cells: Tuple[int, ...] = (27, 28, 35, 36,  # sacrum center
                                     10, 53,          # upper/lower
                                     13, 50)          # lateral
    a: float = 1.0   # Velostat scale (online fit)
    b: float = 0.0   # Velostat offset
    p_var: float = 1.0      # state variance (prior)
    r_vel_var: float = 0.5  # Velostat obs noise
    r_pz_var: float = 0.1   # Piezocap obs noise (more accurate)

    # Online accumulators for Velostat linear fit
    n_samples: int = 0
    sum_v: float = 0.0
    sum_p: float = 0.0
    sum_vp: float = 0.0
    sum_vv: float = 0.0

    def fit_velostat(self, v_anchor: np.ndarray, p_anchor: np.ndarray) -> None:
        """Update Velostat linear coefficients using anchor measurements.

        v_anchor, p_anchor: shape (n_anchors,) — Velostat reading + Piezocap truth.
        """
        self.n_samples += len(v_anchor)
        self.sum_v  += float(v_anchor.sum())
        self.sum_p  += float(p_anchor.sum())
        self.sum_vp += float((v_anchor * p_anchor).sum())
        self.sum_vv += float((v_anchor * v_anchor).sum())
        if self.n_samples >= 10:
            denom = self.n_samples * self.sum_vv - self.sum_v ** 2
            if abs(denom) > 1e-6:
                self.a = (self.n_samples * self.sum_vp - self.sum_v * self.sum_p) / denom
                self.b = (self.sum_p - self.a * self.sum_v) / self.n_samples

    def vel_to_pressure(self, v_raw: np.ndarray) -> np.ndarray:
        """Convert Velostat raw ADC to mmHg using current (a, b)."""
        return self.a * v_raw + self.b

    def kalman_update(self, p_pred: np.ndarray, v_obs: np.ndarray, p_pz: np.ndarray) -> np.ndarray:
        """Online Kalman step to refine pressure map.

        p_pred: (8,8) prior estimate
        v_obs:  (8,8) Velostat-derived (using a, b)
        p_pz:   (n_anchors,) Piezocap truth at anchor positions
        """
        # Innovation from Velostat
        innov_v = v_obs - p_pred
        k_v = self.p_var / (self.p_var + self.r_vel_var)
        p_post = p_pred + k_v * innov_v

        # Anchor correction
        for i, cell in enumerate(self.anchor_cells):
            if i >= len(p_pz):
                break
            k_pz = self.p_var / (self.p_var + self.r_pz_var)
            p_post.flat[cell] = p_post.flat[cell] + k_pz * (p_pz[i] - p_post.flat[cell])

        # Decay prior variance (assumes some model trust)
        self.p_var = max(0.05, self.p_var * 0.95)
        return p_post

    def calibrate(self, v_raw: np.ndarray, p_pz: np.ndarray) -> np.ndarray:
        """Full pipeline: Velostat → linear → Kalman with anchors.

        v_raw: (64,) raw Velostat ADC values (8-bit per STM32)
        p_pz:  (8,)  Piezocap mmHg at anchor positions
        returns: (8, 8) calibrated pressure map in mmHg
        """
        v_flat = np.asarray(v_raw, dtype=np.float32)
        p_pz   = np.asarray(p_pz, dtype=np.float32)

        # Reshape to 8x8
        v_map = v_flat.reshape(8, 8)

        # Online fit using anchor readings
        v_anchor = np.array([v_map.flat[c] for c in self.anchor_cells], dtype=np.float32)
        self.fit_velostat(v_anchor, p_pz)

        # Convert Velostat to pressure via current (a, b)
        p_pred = self.vel_to_pressure(v_map)

        # Kalman refine
        p_cal = self.kalman_update(p_pred, v_pred:=p_pred, p_pz)

        return p_cal


# Synthetic smoke test
if __name__ == "__main__":
    rng = np.random.RandomState(7)

    cal = HybridCalibrator()

    # Simulate 100 frames
    for t in range(100):
        # True pressure with slow drift in Velostat
        drift = 0.05 * t
        p_true = 20 + rng.randn(64) * 2 + (rng.rand(64) > 0.95) * 30
        v_raw  = (p_true + drift + rng.randn(64) * 1.5) * 0.4  # Velostat ADC
        v_raw  = np.clip(v_raw, 0, 255).astype(np.float32)

        # Piezocap (only at anchors)
        anchors = list(cal.anchor_cells)
        p_pz = p_true[anchors] + rng.randn(len(anchors)) * 0.5

        p_cal = cal.calibrate(v_raw, p_pz)

        if t % 20 == 0:
            print(f"t={t:3d}  drift={drift:5.1f}  a={cal.a:.3f}  b={cal.b:.3f}  "
                  f"max_err={(p_cal - p_true.reshape(8,8)).max():.2f}")
