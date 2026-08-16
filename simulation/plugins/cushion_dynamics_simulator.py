"""
Cushion Dynamics Simulator (Python-based, no Gazebo dependency)
================================================================
Mô phỏng dynamics 64 ô khí với first-order ODE:
    dp/dt = (cmd_p - p) / tau

Mục đích: test thuật toán PID control + cross-calibration trên PC
trước khi deploy lên Jetson/Gazebo.

Không cần ROS2 hay Gazebo — chạy được standalone.
"""
from __future__ import annotations
import sys
import os
import time
import numpy as np
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT))


class CushionDynamics:
    """First-order pressure dynamics for 64 cells.

    dp/dt = (cmd_p - p) / tau
    p(t+dt) = p(t) + dt * (cmd_p - p(t)) / tau
    """

    def __init__(self,
                 n_cells: int = 64,
                 rows: int = 8,
                 cols: int = 8,
                 tau: float = 0.3,
                 max_p: float = 80.0,
                 dt: float = 0.1,
                 seed: int = 42):
        assert n_cells == rows * cols
        self.rows = rows
        self.cols = cols
        self.n_cells = n_cells
        self.tau = tau
        self.max_p = max_p
        self.dt = dt
        self.rng = np.random.RandomState(seed)

        # State: pressure per cell
        self.p = np.zeros((rows, cols), dtype=np.float32)
        # Command setpoint per cell
        self.cmd = np.zeros((rows, cols), dtype=np.float32)

    def step(self, cmd_setpoint: np.ndarray) -> np.ndarray:
        """Step dynamics."""
        cmd_setpoint = np.clip(cmd_setpoint, 0.0, self.max_p)
        self.cmd = cmd_setpoint.astype(np.float32)
        # First-order ODE with small noise
        noise = self.rng.randn(self.rows, self.cols) * 0.05
        self.p = self.p + self.dt * (self.cmd - self.p) / self.tau + noise
        self.p = np.clip(self.p, 0.0, self.max_p)
        return self.p.copy()

    def get_pressure(self) -> np.ndarray:
        return self.p.copy()

    def add_disturbance(self, sacrum_pressure: float = 30.0) -> None:
        """Simulate body weight pressing on sacrum cells (rows 3..5, cols 3..5)."""
        self.p[3:6, 3:6] += sacrum_pressure * self.dt / 5.0
        self.p = np.clip(self.p, 0.0, self.max_p)


def simulate_supine(duration_s: float = 60.0, render: bool = True) -> dict:
    """Run simulation: 70 kg mannequin supine on cushion."""
    cushion = CushionDynamics(tau=0.3, max_p=80.0, dt=0.1)

    history_p = []
    history_cmd = []
    history_risk = []
    t_history = []

    print(f"\nSimulating {duration_s:.0f}s supine on 70 kg mannequin...")
    t = 0.0
    while t < duration_s:
        buildup = t / duration_s

        sp = np.full((8, 8), 28.0, dtype=np.float32)
        sp[3:6, 3:6] = 15.0 - buildup * 5
        sp[7, :] = 18.0
        sp[0, :] = 22.0

        cushion.step(sp)
        if t > 5.0:
            cushion.add_disturbance(sacrum_pressure=40.0 + buildup * 20)

        current_p = cushion.get_pressure()
        risk = np.zeros((8, 8), dtype=np.int32)
        risk[(current_p > 32) & (current_p < 50)] = 1
        risk[(current_p >= 50) & (current_p < 65)] = 2
        risk[current_p >= 65] = 3

        history_p.append(current_p.copy())
        history_cmd.append(sp.copy())
        history_risk.append(risk.copy())
        t_history.append(t)

        if render and (int(t) % 10 == 0):
            print(f"t={t:5.1f}s | peak={current_p.max():.1f} mmHg | "
                  f"sacrum mean={current_p[3:6, 3:6].mean():.1f} mmHg | "
                  f"TOT={float((current_p > 32).mean() * 100):.1f}%")

        t += cushion.dt

    history_p = np.stack(history_p, axis=0)
    history_cmd = np.stack(history_cmd, axis=0)
    history_risk = np.stack(history_risk, axis=0)

    sacrum = history_p[:, 3:6, 3:6].mean(axis=(1, 2))
    peak = history_p.max(axis=(1, 2))
    tot = (history_p > 32).mean(axis=(1, 2))

    steady = slice(int(10 / cushion.dt), None)
    sacrum_steady = sacrum[steady].mean()
    peak_steady = peak[steady].mean()

    results = {
        "duration_s": duration_s,
        "sacrum_mean_mmHg": float(sacrum.mean()),
        "sacrum_steady_mmHg": float(sacrum_steady),
        "peak_mean_mmHg": float(peak.mean()),
        "peak_steady_mmHg": float(peak_steady),
        "tot_pct_steady": float(tot[steady].mean() * 100),
        "final_pressure": history_p[-1],
        "final_cmd": history_cmd[-1],
        "final_risk": history_risk[-1],
    }

    print("\n" + "=" * 60)
    print("SIMULATION RESULTS - Supine 70kg")
    print("=" * 60)
    print(f"Duration:               {duration_s:.0f}s")
    print(f"Sacrum mean:            {results['sacrum_mean_mmHg']:.2f} mmHg")
    print(f"Sacrum steady (after 10s): {results['sacrum_steady_mmHg']:.2f} mmHg")
    print(f"Peak mean:              {results['peak_mean_mmHg']:.2f} mmHg")
    print(f"Peak steady:            {results['peak_steady_mmHg']:.2f} mmHg")
    print(f"TOT % (steady):         {results['tot_pct_steady']:.1f}%")
    print()
    print(f"Acceptance (sacrum < 32): {'PASS' if sacrum_steady < 32 else 'FAIL'}")
    print(f"Acceptance (peak < 80):   {'PASS' if peak_steady < 80 else 'FAIL'}")
    print(f"Acceptance (TOT < 10%):   {'PASS' if results['tot_pct_steady'] < 10 else 'FAIL'}")

    return results


def plot_simulation_results(results: dict, save_path: str = None) -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    fig.suptitle("Cushion Simulation Results - Supine 70kg",
                  fontsize=12, fontweight="bold")

    im = axes[0].imshow(results["final_pressure"], cmap="hot", vmin=0, vmax=80)
    axes[0].set_title("Final pressure (mmHg)")
    for r in range(8):
        for c in range(8):
            axes[0].text(c, r, f"{results['final_pressure'][r, c]:.0f}",
                          ha="center", va="center",
                          color="black" if results['final_pressure'][r, c] < 50 else "white",
                          fontsize=7)
    plt.colorbar(im, ax=axes[0])

    im = axes[1].imshow(results["final_cmd"], cmap="cool", vmin=0, vmax=30)
    axes[1].set_title("Final setpoint (mmHg)")
    for r in range(8):
        for c in range(8):
            axes[1].text(c, r, f"{results['final_cmd'][r, c]:.0f}",
                          ha="center", va="center",
                          color="white" if results['final_cmd'][r, c] > 15 else "black",
                          fontsize=7)
    plt.colorbar(im, ax=axes[1])

    risk_labels = {0: "low", 1: "mod", 2: "high", 3: "crit"}
    im = axes[2].imshow(results["final_risk"], cmap="RdYlGn_r", vmin=0, vmax=3)
    axes[2].set_title("Risk classification")
    for r in range(8):
        for c in range(8):
            axes[2].text(c, r, risk_labels[results["final_risk"][r, c]],
                          ha="center", va="center", fontsize=8)
    plt.colorbar(im, ax=axes[2], ticks=[0, 1, 2, 3])

    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches="tight")
        print(f"\nFigure saved: {save_path}")
    else:
        plt.show()
    plt.close()


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--duration", type=float, default=60.0)
    parser.add_argument("--save", type=str, default=None)
    args = parser.parse_args()

    results = simulate_supine(duration_s=args.duration)
    if args.save:
        plot_simulation_results(results, save_path=args.save)
