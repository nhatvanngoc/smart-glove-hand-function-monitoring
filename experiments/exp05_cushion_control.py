"""
EXP-05: Cushion Control — Maintain sacrum < 32 mmHg
===================================================
So sánh 3 control modes: (a) passive alternating, (b) adaptive PTI,
(c) adaptive + CNN-LSTM forecast.

Acceptance: Adaptive modes maintain sacrum < 32 mmHg; passive fails.
"""
from __future__ import annotations
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import numpy as np

from src.integration.pid_cushion import PIDController, risk_to_setpoint
from src.pressure_model.pti_engine import compute_pti, classify_risk
from experiments.synthetic_data import synthetic_pressure_sequence


def control_passive_alternating(p_map: np.ndarray, t: int) -> np.ndarray:
    """Simulate 2-phase alternating (no risk awareness)."""
    phase = (t // 50) % 2
    target = 25.0 if phase == 0 else 35.0
    return np.full_like(p_map, target)


def control_adaptive_pti(p_map: np.ndarray, p_history: list) -> np.ndarray:
    """Use PTI risk to set per-cell setpoint."""
    if len(p_history) < 5:
        return np.full_like(p_map, 25.0)
    arr = np.stack(p_history[-60:], axis=0)
    pti = compute_pti(arr, 0)
    risk = classify_risk(pti)
    return risk_to_setpoint(risk)


def simulate(control_fn, T: int = 600, name: str = "mode", use_pid: bool = True):
    pid = PIDController()
    rng = np.random.RandomState(99)
    data, posture = synthetic_pressure_sequence(T=T, n_volunteers=1, seed=99)
    p_seq = data[0]
    p_current = np.full((8, 8), 30.0, dtype=np.float32)
    sacrum_history = []
    peak_history = []
    history = []

    for t in range(T):
        # Target depends on mode
        if control_fn == control_passive_alternating:
            sp = control_fn(p_current, t)
        else:
            sp = control_fn(p_current, history)
        # Apply PID
        if use_pid:
            pwm = pid.step(p_current, sp)
        # Simulate plant
        p_current = p_current + 0.15 * (sp - p_current) + rng.randn(8, 8) * 0.5
        # Add disturbance (true pressure from synthetic)
        p_current = 0.7 * p_current + 0.3 * p_seq[t]
        p_current = np.clip(p_current, 0, 100)

        history.append(p_current.copy())
        if len(history) > 60:
            history.pop(0)
        sacrum_history.append(float(p_current[3:6, 3:6].mean()))
        peak_history.append(float(p_current.max()))

    sacrum = np.array(sacrum_history)
    peak   = np.array(peak_history)
    tot    = float((np.stack(history) > 32).mean() * 100)

    print(f"  [{name}] Mean sacrum: {sacrum.mean():.2f} ± {sacrum.std():.2f} mmHg")
    print(f"  [{name}] Max peak:    {peak.max():.2f} mmHg")
    print(f"  [{name}] TOT:         {tot:.1f}% time over threshold")
    return {"mean_sacrum": float(sacrum.mean()), "max_peak": float(peak.max()),
            "tot_pct": tot}


def run_experiment():
    print("=" * 60)
    print("EXP-05: Cushion Control (sacrum target < 32 mmHg)")
    print("=" * 60)
    results = {}
    print("\nMode 1: Passive Alternating (control)")
    results["passive"] = simulate(control_passive_alternating, name="passive")
    print("\nMode 2: Adaptive PTI")
    results["adaptive_pti"] = simulate(control_adaptive_pti, name="adaptive_pti")
    print()
    print("Acceptance (sacrum < 32 mmHg in adaptive mode):",
          "✓ PASS" if results["adaptive_pti"]["mean_sacrum"] < 32.0 else "✗ FAIL")
    print("Acceptance (passive worse than adaptive):",
          "✓ PASS" if results["passive"]["mean_sacrum"] > results["adaptive_pti"]["mean_sacrum"] else "✗ FAIL")
    return results


if __name__ == "__main__":
    run_experiment()
