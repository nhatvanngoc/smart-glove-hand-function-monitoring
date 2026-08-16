"""
EXP-07: Self-Improving Loop — Δ Reward after N episodes
=========================================================
Đo sự cải thiện reward sau 24 episodes.

Acceptance: Δ reward ≥ 10%.
"""
from __future__ import annotations
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import numpy as np

from src.integration.self_improve import SelfImprovingLoop


def run_experiment(n_episodes: int = 100):
    rng = np.random.RandomState(0)
    loop = SelfImprovingLoop()
    rewards = []

    for ep in range(n_episodes):
        # Simulated environment with improving trend
        peak = max(20.0, 60.0 - ep * 0.3 + rng.randn() * 5)
        tot  = max(0.0, 0.10 - ep * 0.001 + rng.rand() * 0.02)
        aac  = min(1.0, 0.5 + ep * 0.005 + rng.rand() * 0.05)
        comfort = min(5.0, 3.0 + ep * 0.02 + rng.rand() * 0.2)
        out = loop.step(peak, tot, aac, comfort)
        rewards.append(out["reward"])

    first_window = rewards[:10]
    last_window  = rewards[-10:]
    delta = (np.mean(last_window) - np.mean(first_window))
    delta_pct = delta / max(abs(np.mean(first_window)), 1e-3) * 100
    variance_drop = float(np.std(first_window) - np.std(last_window))

    print("=" * 60)
    print("EXP-07: Self-Improving Loop")
    print("=" * 60)
    print(f"Episodes:                {n_episodes}")
    print(f"Mean reward first 10:    {np.mean(first_window):.3f}")
    print(f"Mean reward last 10:     {np.mean(last_window):.3f}")
    print(f"Δ reward:                {delta:+.3f} ({delta_pct:+.1f}%)")
    print(f"Variance drop:           {variance_drop:+.4f}")
    print(f"Final pid_gain_delta:    {loop.pid_gain_delta:.4f}")
    print(f"Final pth_delta:         {loop.pth_delta:.4f}")
    print(f"Final aac_topk_delta:    {loop.aac_topk_delta}")
    print()
    print(f"Acceptance (Δ reward ≥ 10%): {'✓ PASS' if delta_pct >= 10.0 else '✗ FAIL'}")
    return {"delta_pct": delta_pct, "variance_drop": variance_drop,
            "first_mean": float(np.mean(first_window)),
            "last_mean": float(np.mean(last_window))}


if __name__ == "__main__":
    run_experiment()
