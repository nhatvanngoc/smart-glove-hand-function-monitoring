"""
Test: Step pressure response of single cell (verification of dynamics).

Acceptance: rise time < 2s, fall time < 3s, overshoot < 10%.
"""
from __future__ import annotations
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import numpy as np

from simulation.plugins.cushion_dynamics_simulator import CushionDynamics


def test_step_response(target_pressure: float = 80.0, duration_s: float = 6.0) -> dict:
    """Apply step from 0 to target on one cell, measure response."""
    cushion = CushionDynamics(tau=0.3, dt=0.05)

    # Single cell step (cell 27 = sacrum)
    target_cell = (3, 4)

    history = []
    cmd_history = []
    t_history = []
    t = 0.0
    while t < duration_s:
        # Step at t = 0.5s
        if t < 0.5:
            cmd = np.zeros((8, 8), dtype=np.float32)
        elif t < 3.5:
            cmd = np.zeros((8, 8), dtype=np.float32)
            cmd[target_cell] = target_pressure
        else:
            # Deflate step at t = 3.5s
            cmd = np.zeros((8, 8), dtype=np.float32)
        cushion.step(cmd)
        history.append(cushion.get_pressure()[target_cell])
        cmd_history.append(cmd[target_cell])
        t_history.append(t)
        t += cushion.dt

    history = np.array(history)
    cmd_history = np.array(cmd_history)
    t_history = np.array(t_history)

    # Compute rise time (10% → 90%)
    p_target = target_pressure
    t_10 = t_history[np.argmax(history > 0.1 * p_target)]
    t_90 = t_history[np.argmax(history > 0.9 * p_target)]
    rise_time = t_90 - t_10

    # Fall time (90% → 10%) after deflate at t=3.5
    fall_start = np.argmax(t_history >= 3.5)
    fall_history = history[fall_start:]
    fall_t_history = t_history[fall_start:]
    if (fall_history > 0.9 * p_target).any() and (fall_history < 0.1 * p_target).any():
        t_90_fall = fall_t_history[np.argmax(fall_history > 0.9 * p_target)]
        t_10_fall = fall_t_history[np.argmax(fall_history < 0.1 * p_target)]
        fall_time = t_10_fall - t_90_fall
    else:
        fall_time = 0.0

    # Overshoot
    overshoot = max(0.0, history.max() - p_target)

    print("=" * 60)
    print(f"STEP RESPONSE TEST — Target: {target_pressure} mmHg")
    print("=" * 60)
    print(f"Rise time (10% -> 90%): {rise_time:.3f} s")
    print(f"Fall time (90% -> 10%): {fall_time:.3f} s")
    print(f"Overshoot:              {overshoot:.2f} mmHg ({overshoot/p_target*100:.1f}%)")
    print(f"Steady-state (after 2s): {history[40:].mean():.2f} mmHg")
    print(f"Steady-state (after 4s): {history[80:].mean():.2f} mmHg")
    print()
    print(f"Acceptance (rise < 2s):   {'PASS' if rise_time < 2.0 else 'FAIL'}")
    print(f"Acceptance (fall < 3s):   {'PASS' if fall_time < 3.0 else 'FAIL'}")
    print(f"Acceptance (overshoot<10%):{'PASS' if overshoot < 0.1 * p_target else 'FAIL'}")

    return {
        "rise_time": rise_time,
        "fall_time": fall_time,
        "overshoot": overshoot,
        "history": history.tolist(),
        "t_history": t_history.tolist(),
        "cmd_history": cmd_history.tolist(),
    }


def plot_step_response(results: dict, save_path: str = None) -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(results["t_history"], results["history"], label="Cell pressure",
             color="#1976D2", lw=2)
    ax.plot(results["t_history"], results["cmd_history"], label="Setpoint",
             color="#AD1457", lw=1.5, linestyle="--")
    ax.axvline(0.5, color="gray", lw=0.8, linestyle=":")
    ax.axvline(3.5, color="gray", lw=0.8, linestyle=":")
    ax.axhline(80, color="#B71C1C", lw=0.8, linestyle=":",
                label="Safety max (80 mmHg)")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Pressure (mmHg)")
    ax.set_title("Step Response — Single Cell Pressure Dynamics")
    ax.legend(loc="best")
    ax.grid(True, alpha=0.3)

    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches="tight")
        print(f"Figure saved: {save_path}")
    else:
        plt.show()
    plt.close()


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", type=float, default=80.0)
    parser.add_argument("--duration", type=float, default=6.0)
    parser.add_argument("--save", type=str, default=None)
    args = parser.parse_args()

    res = test_step_response(args.target, args.duration)
    if args.save:
        plot_step_response(res, save_path=args.save)
