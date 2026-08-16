"""
Stage 2 DESIGN — System architecture, hardware, software, ML design
====================================================================
Output: Stage 2 status, architecture docs loaded.
"""
from __future__ import annotations
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))


DESIGN_DOCS = [
    "04_System_Architecture.md",
    "05_Hardware_Design.md",
    "06_Software_Design.md",
    "07_ML_Models.md",
]


def run_stage_2() -> dict:
    print("\n" + "=" * 60)
    print(" STAGE 2 — DESIGN")
    print("=" * 60)
    docs = ROOT / "docs"
    n_loaded = 0
    for d in DESIGN_DOCS:
        p = docs / d
        if p.exists():
            print(f"  ✓ {d}: {p.stat().st_size} bytes")
            n_loaded += 1
        else:
            print(f"  ! {d}: missing")
    diagrams = ROOT / "diagrams"
    n_diagrams = len(list(diagrams.glob("*.png")))
    print(f"  ✓ Diagrams available: {n_diagrams} PNG files")
    print("  ✓ Stage 2 complete — ready for Stage 3 (Prototype)")
    return {"ok": True, "docs_loaded": n_loaded, "diagrams": n_diagrams}


if __name__ == "__main__":
    run_stage_2()
