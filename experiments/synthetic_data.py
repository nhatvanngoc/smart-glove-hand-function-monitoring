"""
Synthetic Data Generator — for testing without hardware.
========================================================
Generates realistic pressure sequences, eye-tracking frames, AAC interactions.
All reproducible with seed.

Note: Designed to reflect realistic clinical scenarios where the algorithms
have meaningful signal to detect (gradual pressure buildup, varied risk levels).
"""
from __future__ import annotations
import numpy as np
from typing import Tuple


def synthetic_pressure_sequence(T: int = 2400, n_volunteers: int = 5,
                                 seed: int = 42) -> Tuple[np.ndarray, np.ndarray]:
    """Generate (n_volunteers, T, 8, 8) pressure maps in mmHg + posture labels.

    T=2400 frames @ 10 Hz = 4 minutes — long enough for gradual risk buildup.
    """
    rng = np.random.RandomState(seed)
    data   = np.zeros((n_volunteers, T, 8, 8), dtype=np.float32)
    posture = rng.randint(0, 3, size=(n_volunteers, T))

    for v in range(n_volunteers):
        # Each volunteer has a different body weight / distribution
        base = 18 + rng.rand() * 10
        # Build a gradual pressure buildup: starts low, slowly rises
        buildup = np.linspace(0, 25, T)
        # Posture-dependent hotspot
        for t in range(T):
            p = np.full((8, 8), base + buildup[t] * 0.3, dtype=np.float32)
            p += rng.randn(8, 8) * 1.0
            ph = posture[v, t]
            if ph == 0:    # supine — sacrum
                p[3:6, 3:6] += 8 + buildup[t] * 0.4
            elif ph == 1:  # lateral — trochanter
                p[4:5, 2:3] += 12 + buildup[t] * 0.3
            else:          # prone — scapula, knees
                p[0:1, :] += 6 + buildup[t] * 0.2
                p[6:7, :] += 6 + buildup[t] * 0.2
            data[v, t] = np.clip(p, 0, 100)
    return data, posture


def synthetic_eye_tracking(n_samples: int = 200, seed: int = 0):
    """Generate synthetic (gaze_x, gaze_y, target_x, target_y) tuples."""
    rng = np.random.RandomState(seed)
    targets_x = (rng.randint(5, size=n_samples).astype(np.float32) + 0.5) * 100
    targets_y = (rng.randint(3, size=n_samples).astype(np.float32) + 0.5) * 100
    gaze_x = targets_x + rng.randn(n_samples) * 15
    gaze_y = targets_y + rng.randn(n_samples) * 15
    return gaze_x, gaze_y, targets_x, targets_y


def synthetic_aac_pairs(n: int = 50, seed: int = 0):
    """Generate test (keywords, ground_truth) pairs from SEED_DATASET."""
    from src.aac_assistant.qwen_lora import SEED_DATASET
    rng = np.random.RandomState(seed)
    pairs = []
    for _ in range(n):
        idx = rng.randint(len(SEED_DATASET))
        kws, gt = SEED_DATASET[idx]
        if rng.rand() > 0.7:
            kws = list(kws)
            rng.shuffle(kws)
        pairs.append((kws, gt))
    return pairs


if __name__ == "__main__":
    data, posture = synthetic_pressure_sequence()
    print(f"Pressure data: shape={data.shape}, range=[{data.min():.1f}, {data.max():.1f}]")
    print(f"Posture: shape={posture.shape}, distribution={np.bincount(posture.flatten())}")
    print(f"Sacrum zone pressure (volunteer 0, last 100 frames):")
    print(f"  mean = {data[0, -100:, 3:6, 3:6].mean():.1f} mmHg")
    print(f"  max  = {data[0, -100:, 3:6, 3:6].max():.1f} mmHg")
    gx, gy, tx, ty = synthetic_eye_tracking()
    print(f"Eye-tracking: n={len(gx)}, mean pixel error={np.sqrt(((gx-tx)**2 + (gy-ty)**2).mean()):.1f}")
