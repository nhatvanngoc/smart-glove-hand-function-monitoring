"""
Test: Supine scenario — 70 kg mannequin nằm ngửa trên cushion.

Mục tiêu: verify pressure distribution + cushion có duy trì sacrum < 32 mmHg.
"""
from __future__ import annotations
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import numpy as np

from simulation.plugins.cushion_dynamics_simulator import simulate_supine


def run_test(duration_s: float = 60.0):
    print("=" * 70)
    print(" TEST SCENARIO — Supine Mannequin (70 kg)")
    print("=" * 70)
    results = simulate_supine(duration_s=duration_s, render=True)

    # Print final state
    print("\nFinal pressure map:")
    print(np.round(results["final_pressure"], 1))

    print("\nFinal risk map (0=low, 1=mod, 2=high, 3=crit):")
    print(results["final_risk"])

    return results


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--duration", type=float, default=60.0)
    args = parser.parse_args()
    run_test(args.duration)
