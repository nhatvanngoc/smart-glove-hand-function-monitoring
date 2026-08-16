"""
Stage 4 EVALUATION — Run all experiments + end-to-end pipeline test
==================================================================
Output: Experiment results JSON + summary report.
"""
from __future__ import annotations
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))


def run_stage_4() -> dict:
    print("\n" + "=" * 60)
    print(" STAGE 4 — EVALUATION")
    print("=" * 60)

    # Run all experiments via runner
    from pipeline.runner import run_all_experiments
    results = run_all_experiments()

    # Run end-to-end orchestrator smoke test
    print("\n  Running end-to-end orchestrator smoke test...")
    from src.integration.orchestrator import Orchestrator
    import numpy as np
    rng = np.random.RandomState(0)
    orch = Orchestrator(use_llm=False, use_lstm=True, seed=42)
    n_ok = 0
    for t in range(60):
        true_p = np.clip(20 + rng.rand(64) * 20, 0, 80)
        v_raw = (2.0 * true_p + 20 + rng.randn(64) * 1.0).clip(0, 255).astype(np.float32)
        p_pz = np.array([true_p[c] for c in orch.calibrator.anchor_cells]) + rng.randn(8) * 0.5
        gaze = (50 + 0 * 100, 50 + 2 * 100) if (t % 30 == 10) else None
        out = orch.step(v_raw, p_pz, gaze_xy=gaze, comfort=4.0)
        if out["safety_ok"] or out["aac_sentence"]:
            n_ok += 1
    print(f"  ✓ Orchestrator: {n_ok}/60 ticks produced valid output")

    print("  ✓ Stage 4 complete — ready for Stage 5 (Submission)")
    return {"ok": True, "results": results, "orchestrator_valid_ticks": n_ok}


if __name__ == "__main__":
    run_stage_4()
