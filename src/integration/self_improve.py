"""
Self-Improving Loop — Contextual Bandit (LinUCB)
================================================
Online update các tham số vận hành (PID gain, ngưỡng PTI, top-k AAC) dựa trên
reward composite. Bounded action space (±10%) + human override để an toàn.

Theo ARS M6/M7 mitigation: bounded updates, conservative reward shaping.
"""
from __future__ import annotations
import numpy as np
from dataclasses import dataclass, field
from typing import Tuple


@dataclass
class LinUCB:
    """Contextual bandit with linear payoff.

    d: feature dimension
    alpha: exploration parameter
    """
    d: int = 8
    alpha: float = 1.0
    A: np.ndarray = field(default_factory=lambda: np.eye(8))
    b: np.ndarray = field(default_factory=lambda: np.zeros(8))
    action_bounds: Tuple[float, float] = (-0.10, 0.10)  # ±10% per step

    def select(self, x: np.ndarray) -> float:
        """Return action ∈ [-0.10, +0.10]."""
        A_inv = np.linalg.inv(self.A)
        theta = A_inv @ self.b
        p = theta @ x + self.alpha * np.sqrt(x @ A_inv @ x)
        return float(np.clip(p, *self.action_bounds))

    def update(self, x: np.ndarray, r: float) -> None:
        self.A += np.outer(x, x)
        self.b += r * x


@dataclass
class SelfImprovingLoop:
    """State → Action → Reward update for cushion + AAC params."""
    pid_gain_delta: float = 0.0
    pth_delta:       float = 0.0
    aac_topk_delta:  int = 0
    bandit: LinUCB = field(default_factory=LinUCB)

    def state_features(self, peak_pressure: float, tot_pct: float,
                        aac_success_rate: float, comfort_score: float) -> np.ndarray:
        """8-dim state vector."""
        return np.array([
            peak_pressure / 80.0,
            tot_pct,
            1.0 - aac_success_rate,
            1.0 - (comfort_score / 5.0),
            self.pid_gain_delta,
            self.pth_delta,
            float(self.aac_topk_delta) / 5.0,
            1.0,  # bias
        ], dtype=np.float32)

    def reward(self, peak_pressure: float, tot_pct: float,
               aac_success_rate: float, comfort_score: float) -> float:
        """Composite reward ∈ [-1, +1]."""
        norm_peak  = max(0.0, 1.0 - peak_pressure / 80.0)
        r = (0.4 * norm_peak + 0.3 * (1.0 - tot_pct)
             + 0.2 * aac_success_rate + 0.1 * (comfort_score / 5.0))
        return float(np.clip(r * 2.0 - 1.0, -1.0, 1.0))

    def step(self, peak_pressure: float, tot_pct: float,
             aac_success_rate: float, comfort_score: float) -> dict:
        """One update tick."""
        x = self.state_features(peak_pressure, tot_pct, aac_success_rate, comfort_score)
        action = self.bandit.select(x)
        r = self.reward(peak_pressure, tot_pct, aac_success_rate, comfort_score)
        self.bandit.update(x, r)

        # Apply bounded actions
        self.pid_gain_delta = float(np.clip(action, *self.bandit.action_bounds))
        self.pth_delta      = float(np.clip(action * 0.5, *self.bandit.action_bounds))
        self.aac_topk_delta = int(round(np.clip(action * 2, -2, 2)))

        return {
            "action": action,
            "reward": r,
            "pid_gain_delta": self.pid_gain_delta,
            "pth_delta": self.pth_delta,
            "aac_topk_delta": self.aac_topk_delta,
        }


if __name__ == "__main__":
    rng = np.random.RandomState(0)
    loop = SelfImprovingLoop()
    rewards = []
    # Simulate 100 episodes
    for ep in range(100):
        peak = max(20.0, 60.0 - ep * 0.3 + rng.randn() * 5)
        tot  = max(0.0, 0.10 - ep * 0.001 + rng.rand() * 0.02)
        aac  = min(1.0, 0.5 + ep * 0.005)
        comfort = min(5.0, 3.0 + ep * 0.02)
        out = loop.step(peak, tot, aac, comfort)
        rewards.append(out["reward"])

    print(f"Mean reward first 10 eps: {np.mean(rewards[:10]):.3f}")
    print(f"Mean reward last 10 eps:  {np.mean(rewards[-10:]):.3f}")
    print(f"Δ reward: {(np.mean(rewards[-10:]) - np.mean(rewards[:10])) / max(abs(np.mean(rewards[:10])), 1e-6) * 100:.1f}%")
    print(f"Final pid_gain_delta: {loop.pid_gain_delta:.4f}")
    print(f"Final pth_delta: {loop.pth_delta:.4f}")
    print(f"Final aac_topk_delta: {loop.aac_topk_delta}")
