"""
Stage 5 SUBMISSION — Final integrity check + submission package
==================================================================
Output: Submission manifest + final report.
"""
from __future__ import annotations
import sys, json
from pathlib import Path
import time

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))


def run_stage_5() -> dict:
    print("\n" + "=" * 60)
    print(" STAGE 5 — SUBMISSION (final integrity check)")
    print("=" * 60)

    checks = {}

    # 1. Required docs
    required_docs = [
        "docs/01_RQ_Brief.md",
        "docs/02_Literature_Review.md",
        "docs/03_Methodology_Blueprint.md",
        "docs/04_System_Architecture.md",
        "docs/05_Hardware_Design.md",
        "docs/06_Software_Design.md",
        "docs/07_ML_Models.md",
        "docs/08_Experimental_Protocol.md",
        "docs/09_Risk_Register.md",
        "docs/10_References.md",
    ]
    docs_ok = 0
    for d in required_docs:
        p = ROOT / d
        ok = p.exists() and p.stat().st_size > 500
        checks[d] = ok
        docs_ok += int(ok)
    print(f"  ✓ Docs: {docs_ok}/{len(required_docs)} present and > 500 bytes")

    # 2. Diagrams
    diagrams_dir = ROOT / "diagrams"
    diagrams = list(diagrams_dir.glob("*.png"))
    checks["diagrams_count"] = len(diagrams)
    print(f"  ✓ Diagrams: {len(diagrams)} PNG files")

    # 3. Source modules
    src_files = list((ROOT / "src").rglob("*.py"))
    checks["src_py_files"] = len(src_files)
    print(f"  ✓ Source: {len(src_files)} Python files")

    # 4. Experiments
    exp_files = list((ROOT / "experiments").glob("*.py"))
    checks["experiment_files"] = len(exp_files)
    print(f"  ✓ Experiments: {len(exp_files)} scripts")

    # 5. Pipeline stages
    stage_files = list((ROOT / "pipeline").glob("stage*.py"))
    checks["pipeline_stages"] = len(stage_files)
    print(f"  ✓ Pipeline stages: {len(stage_files)} scripts")

    # 6. Experiment results exist
    results_path = ROOT / "outputs" / "reports" / "experiment_results.json"
    if results_path.exists():
        with open(results_path) as f:
            exp_results = json.load(f)
        n_pass = sum(1 for v in exp_results.values() if v.get("ok"))
        checks["experiments_passed"] = n_pass
        print(f"  ✓ Experiments passed: {n_pass}/{len(exp_results)}")
    else:
        checks["experiments_passed"] = 0
        print("  ! experiment_results.json not found — run stage 4 first")

    # 7. Write submission manifest
    manifest = {
        "project": "Adaptive Air Cushion + Eye-Tracking AAC",
        "student": "Văn Ngọc Nhật Anh — Lớp 11A2 — THPT Quảng Trị",
        "year": "2026-2027",
        "field": "Hệ thống nhúng (Embedded Systems)",
        "ars_pipeline_version": "academic-research-suite v3.12.0",
        "generated_at": time.strftime("%Y-%m-%d %H:%M:%S"),
        "checks": checks,
    }
    manifest_path = ROOT / "outputs" / "reports" / "submission_manifest.json"
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
    print(f"\n  ✓ Submission manifest saved → {manifest_path.relative_to(ROOT)}")

    # Final summary
    total = sum(1 for v in checks.values() if isinstance(v, bool) and v)
    print(f"\n  === FINAL INTEGRITY: {total}/{len(required_docs)} docs OK ===")

    return {"ok": True, "manifest": manifest}


if __name__ == "__main__":
    run_stage_5()
