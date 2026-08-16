#!/usr/bin/env python3
"""Append an auditable query record without third-party dependencies."""
from __future__ import annotations

import argparse
import json
import secrets
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
PUBLIC_LOG = ROOT / "research" / "queries" / "QUERY_LOG.jsonl"
PRIVATE_LOG = ROOT / "research" / "queries" / "private" / "QUERY_LOG.jsonl"


def append_record(
    *,
    kind: str,
    query: str,
    purpose: str,
    status: str = "complete",
    summary: str = "",
    sources: Iterable[str] = (),
    engine: str = "manual",
    output: Path | None = None,
) -> tuple[dict[str, object], Path]:
    """Append one JSONL record and return the record and resolved output path."""
    if not query.strip():
        raise ValueError("Refusing to log an empty query.")
    now = datetime.now(timezone.utc)
    record: dict[str, object] = {
        "id": f"Q-{now:%Y%m%dT%H%M%SZ}-{secrets.token_hex(3)}",
        "timestamp_utc": now.isoformat(timespec="seconds").replace("+00:00", "Z"),
        "timestamp_precision": "second",
        "reconstructed": False,
        "kind": kind,
        "engine": engine,
        "query": query.strip(),
        "purpose": purpose,
        "status": status,
        "result_summary": summary,
        "selected_source_ids": list(sources),
    }
    resolved = output or PUBLIC_LOG
    if not resolved.is_absolute():
        resolved = ROOT / resolved
    resolved.parent.mkdir(parents=True, exist_ok=True)
    with resolved.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write(json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n")
    return record, resolved


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Append a user/search/tool query to the research JSONL ledger."
    )
    parser.add_argument("--kind", choices=("user", "search", "tool", "decision"), required=True)
    query = parser.add_mutually_exclusive_group(required=True)
    query.add_argument("--query", help="Query text. Do not pass credentials or participant data.")
    query.add_argument("--query-file", type=Path, help="UTF-8 file containing a long query.")
    parser.add_argument("--purpose", required=True)
    parser.add_argument(
        "--status", choices=("planned", "running", "complete", "blocked", "failed"), default="complete"
    )
    parser.add_argument("--summary", default="")
    parser.add_argument("--sources", nargs="*", default=[], help="Source IDs from SOURCE_LEDGER.csv")
    parser.add_argument("--engine", default="manual")
    parser.add_argument("--private", action="store_true", help="Write under ignored research/queries/private/")
    parser.add_argument("--output", type=Path, help=argparse.SUPPRESS)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    text = args.query if args.query is not None else args.query_file.read_text(encoding="utf-8")
    try:
        record, output = append_record(
            kind=args.kind,
            query=text,
            purpose=args.purpose,
            status=args.status,
            summary=args.summary,
            sources=args.sources,
            engine=args.engine,
            output=args.output or (PRIVATE_LOG if args.private else PUBLIC_LOG),
        )
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 2
    display = output.relative_to(ROOT) if output.is_relative_to(ROOT) else output
    print(f"Logged {record['id']} -> {display}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
