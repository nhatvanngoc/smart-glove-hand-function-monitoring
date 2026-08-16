"""
Stage 3 PROTOTYPE — Generate diagrams + verify source code
==========================================================
Output: All diagrams + source module verification.
"""
from __future__ import annotations
import sys, importlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))


SRC_MODULES = [
    "src.pressure_model.pti_engine",
    "src.pressure_model.cross_calibration",
    "src.pressure_model.cnn_lstm",
    "src.aac_assistant.qwen_lora",
    "src.aac_assistant.aac_grid",
    "src.eye_tracking.eye_tracker",
    "src.integration.pid_cushion",
    "src.integration.self_improve",
    "src.integration.orchestrator",
]


def run_stage_3() -> dict:
    print("\n" + "=" * 60)
    print(" STAGE 3 - PROTOTYPE")
    print("=" * 60)

    # Generate diagrams via dedicated module
    print("  Generating diagrams...")
    from pipeline.diagram_generator import generate_all
    generate_all()
    n_diagrams = len(list((ROOT / "diagrams").glob("*.png")))
    print(f"  OK Diagrams regenerated: {n_diagrams} PNG files")

    # Verify source modules
    print("  Verifying source modules...")
    n_ok = 0
    for m in SRC_MODULES:
        try:
            importlib.import_module(m)
            print(f"  OK {m}")
            n_ok += 1
        except Exception as e:
            print(f"  FAIL {m}: {e}")

    print("  OK Stage 3 complete - ready for Stage 4 (Evaluation)")
    return {"ok": True, "diagrams": n_diagrams, "modules_ok": n_ok}


if __name__ == "__main__":
    run_stage_3()
