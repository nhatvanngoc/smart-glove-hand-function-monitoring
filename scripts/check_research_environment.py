#!/usr/bin/env python3
"""Report reproducible research-tooling readiness."""
from __future__ import annotations

import argparse
import importlib.util
import json
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOCK = ROOT / "tools" / "research_sources.lock.json"


def command_version(name: str, args: list[str]) -> tuple[bool, str]:
    path = shutil.which(name)
    if not path:
        return False, "not found"
    try:
        proc = subprocess.run([path, *args], text=True, capture_output=True, timeout=20, check=False)
        text = (proc.stdout or proc.stderr).strip().splitlines()
        return proc.returncode == 0, text[0] if text else path
    except (OSError, subprocess.TimeoutExpired) as exc:
        return False, str(exc)


def git_value(path: Path, *args: str) -> str:
    try:
        return subprocess.check_output(
            ["git", "-C", str(path), *args], text=True, stderr=subprocess.DEVNULL, timeout=20
        ).strip()
    except (OSError, subprocess.SubprocessError):
        return ""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--strict", action="store_true", help="exit nonzero when any required/target check fails")
    parser.add_argument("--json", action="store_true", help="emit JSON")
    args = parser.parse_args()

    results: list[dict[str, object]] = []

    def add(category: str, name: str, ok: bool, detail: str, required: bool = True) -> None:
        results.append({"category": category, "name": name, "ok": ok, "required": required, "detail": detail})

    for command, version_args, required in (
        ("git", ["--version"], True),
        ("python3", ["--version"], True),
        ("pdflatex", ["--version"], True),
        ("miktexsetup", ["--version"], False),
    ):
        ok, detail = command_version(command, version_args)
        add("command", command, ok, detail, required)

    for module, package in (
        ("numpy", "numpy"),
        ("matplotlib", "matplotlib"),
        ("sklearn", "scikit-learn"),
    ):
        ok = importlib.util.find_spec(module) is not None
        detail = "importable" if ok else f"not importable; install {package} via requirements.txt"
        add("python", package, ok, detail)

    try:
        lock = json.loads(LOCK.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        add("source", "lock file", False, str(exc))
        lock = {"repositories": []}

    for item in lock["repositories"]:
        path = ROOT / ".tools" / "sources" / item["name"]
        commit = git_value(path, "rev-parse", "HEAD")
        origin = git_value(path, "remote", "get-url", "origin")
        dirty = git_value(path, "status", "--porcelain")
        ok = commit == item["commit"] and origin == item["url"] and not dirty
        state = "clean" if not dirty else "LOCAL CHANGES"
        detail = f"{commit[:12] or 'missing'}; {state}; origin={origin or 'missing'}"
        add("source", item["name"], ok, detail)

    for skill in ("deep-research", "academic-paper", "academic-paper-reviewer", "academic-pipeline"):
        link = ROOT / ".claude" / "skills" / skill
        skill_md = link / "SKILL.md"
        add("skill", skill, skill_md.is_file(), str(link.relative_to(ROOT)), required=False)

    if args.json:
        print(json.dumps({"schema_version": 1, "checks": results}, ensure_ascii=False, indent=2))
    else:
        for row in results:
            label = "PASS" if row["ok"] else ("FAIL" if row["required"] else "WARN")
            print(f"{label:4}  {row['category']:<8} {row['name']:<28} {row['detail']}")
        required_ok = sum(bool(r["ok"]) for r in results if r["required"])
        required_total = sum(1 for r in results if r["required"])
        print(f"\nRequired/target readiness: {required_ok}/{required_total}")
        print("Caffe/PGF/MiKTeX source builds are intentionally not part of this check.")

    failed = any(r["required"] and not r["ok"] for r in results)
    return 1 if args.strict and failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
