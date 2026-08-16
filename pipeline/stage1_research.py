"""
Stage 1 RESEARCH — Literature review + research gap identification
====================================================================
Output: Stage 1 status, key references count, RGI summary.
"""
from __future__ import annotations
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))


def run_stage_1() -> dict:
    print("\n" + "=" * 60)
    print(" STAGE 1 — RESEARCH")
    print("=" * 60)

    refs_path = ROOT / "docs" / "10_References.md"
    if refs_path.exists():
        text = refs_path.read_text(encoding="utf-8")
        # Count references (lines starting with digit.)
        n_refs = sum(1 for ln in text.split("\n") if ln.strip() and ln.strip()[0].isdigit() and "." in ln[:4])
        print(f"  ✓ References file loaded: {n_refs} references")
    else:
        print("  ! References file missing")
        return {"ok": False}

    lit_path = ROOT / "docs" / "02_Literature_Review.md"
    if lit_path.exists():
        text = lit_path.read_text(encoding="utf-8")
        # Count research gaps
        n_gaps = text.count("Gap-")
        n_3layer = sum(text.count(f"Layer {i} —") for i in [1, 2, 3])
        print(f"  ✓ Literature review loaded: {n_gaps} research gaps identified")
        print(f"  ✓ 3-Layer citation: {n_3layer} layers")
    else:
        print("  ! Literature review missing")
        return {"ok": False}

    print("  ✓ Stage 1 complete — ready for Stage 2 (Design)")
    return {"ok": True, "n_refs": n_refs, "n_gaps": n_gaps}


if __name__ == "__main__":
    run_stage_1()
