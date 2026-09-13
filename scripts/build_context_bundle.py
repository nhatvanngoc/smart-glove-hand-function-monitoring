#!/usr/bin/env python3
"""Build a deterministic, bounded context packet from curated project artifacts.

This packs human-curated summaries and deterministic document outlines. It does not
claim to perform semantic/LLM summarization and does not turn the packet into evidence.
"""
from __future__ import annotations

import argparse
import hashlib
import math
import os
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "research" / "generated" / "context_bundle.md"

FULL_SOURCES = [
    "research/context/PROJECT_SNAPSHOT.md",
    "research/context/DECISION_LOG.md",
    "research/claims/CLAIM_LEDGER.csv",
    "research/evidence/SOURCE_LEDGER.csv",
    "research/reviews/00_EXPLORATION_SUMMARY.md",
    "research/context/CONVERSATION_2026-09-13.md",
    "research/protocols/ISEF_REVIEW_ORCHESTRATION.md",
    "research/protocols/06_glove_hand_GATE_experiment.md",
    "docs/01_Topic_Definition.md",
    "docs/02_Theoretical_Foundation.md",
]
OUTLINE_SOURCES = [
    "docs/03_Literature_Gap_Analysis_Plan.md",
    "docs/04_Hardware_Architecture.md",
    "research/tooling/SETUP_STATUS.md",
]
RISK_PATTERN = re.compile(
    r"(?i)(synthetic|simulation|mô phỏng|chưa|không được|warning|cảnh báo|risk|rủi ro|"
    r"limitation|giới hạn|32\s*mmhg|irb|src|volunteer|claim|evidence|5\s*[x×]\s*9|"
    r"8\s*[x×]\s*8|orange pi|jetson|robot arm|gate|drift|unreliable|phantom|"
    r"esp32|cd74hc4067|mdc|icc)"
)


def digest(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def generated_utc() -> str:
    """Honor SOURCE_DATE_EPOCH when byte-for-byte reproducibility is needed."""
    epoch = os.environ.get("SOURCE_DATE_EPOCH")
    if epoch is not None:
        try:
            value = datetime.fromtimestamp(int(epoch), tz=timezone.utc)
        except (ValueError, OverflowError) as exc:
            raise ValueError("SOURCE_DATE_EPOCH must be an integer Unix timestamp") from exc
    else:
        value = datetime.now(timezone.utc)
    return value.isoformat(timespec="seconds").replace("+00:00", "Z")


def git_head() -> str:
    try:
        return subprocess.check_output(
            ["git", "-C", str(ROOT), "rev-parse", "HEAD"], text=True, timeout=10
        ).strip()
    except (OSError, subprocess.SubprocessError):
        return "unavailable"


def outline(text: str, max_lines: int = 90) -> str:
    """Keep headings plus high-risk/status lines, preserving source line numbers."""
    selected: list[str] = []
    seen: set[int] = set()
    lines = text.splitlines()
    for index, line in enumerate(lines, 1):
        if line.startswith("#") or RISK_PATTERN.search(line):
            if index not in seen:
                selected.append(f"L{index}: {line}")
                seen.add(index)
            if len(selected) >= max_lines:
                selected.append(f"… outline capped at {max_lines} selected lines …")
                break
    return "\n".join(selected) if selected else "(no matching outline lines)"


def section(path_text: str, mode: str) -> str:
    path = ROOT / path_text
    if not path.is_file():
        return f"## {path_text}\n\nMISSING SOURCE\n"
    raw = path.read_text(encoding="utf-8", errors="replace")
    body = raw.rstrip() if mode == "full" else outline(raw)
    return (
        f"## {path_text}\n\n"
        f"- mode: `{mode}`\n- sha256: `{digest(raw)}`\n- source_chars: `{len(raw)}`\n\n"
        f"{body}\n"
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--budget-chars", type=int, default=40000)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    if args.budget_chars < 8000:
        parser.error("--budget-chars must be at least 8000")

    try:
        generated = generated_utc()
    except ValueError as exc:
        parser.error(str(exc))
    header = f"""# Generated bounded context bundle

- generated_utc: `{generated}`
- repository_head: `{git_head()}`
- character_budget: `{args.budget_chars}`
- token_estimate_rule: `ceil(characters / 4)` (rough navigation estimate only)

> This packet is a deterministic navigation aid assembled from curated summaries and document outlines. It is not a source of evidence. Resolve every consequential statement against the named artifact and its SHA-256 digest.

"""
    chunks = [header]
    omissions: list[str] = []
    used = len(header)

    for mode, paths in (("full", FULL_SOURCES), ("outline", OUTLINE_SOURCES)):
        for path in paths:
            chunk = section(path, mode)
            if used + len(chunk) <= args.budget_chars:
                chunks.append(chunk + "\n")
                used += len(chunk) + 1
            else:
                omissions.append(f"- `{path}` ({mode}; would exceed budget)")

    footer = "\n# Omitted by budget\n\n" + ("\n".join(omissions) if omissions else "None.") + "\n"
    remaining = args.budget_chars - used
    if len(footer) <= remaining:
        chunks.append(footer)
    else:
        marker = "\n# Omitted by budget\n\nOmission list exceeded the remaining budget.\n"
        chunks.append(marker[: max(remaining, 0)])

    output = args.output if args.output.is_absolute() else ROOT / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    content = "".join(chunks)
    assert len(content) <= args.budget_chars, "context packet exceeded its hard character budget"
    output.write_text(content, encoding="utf-8", newline="\n")
    print(f"Wrote {output.relative_to(ROOT) if output.is_relative_to(ROOT) else output}")
    print(f"Characters: {len(content)}; rough tokens: {math.ceil(len(content) / 4)}; omitted: {len(omissions)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
