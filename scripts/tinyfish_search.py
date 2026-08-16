#!/usr/bin/env python3
"""TinyFish search helper with automatic auditable query logging.

The API key is read only from ``TINYFISH_API_KEY``. Search results are untrusted
candidate material; add selected sources to SOURCE_LEDGER.csv only after review.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

from research_log import PRIVATE_LOG, PUBLIC_LOG, append_record

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "research" / "cache" / "tinyfish_search.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", help="Search text; never include credentials or participant identifiers")
    parser.add_argument(
        "output_json",
        nargs="?",
        type=Path,
        default=DEFAULT_OUTPUT,
        help="result file (default: ignored research/cache/tinyfish_search.json)",
    )
    parser.add_argument("--purpose", default="Candidate-source discovery")
    parser.add_argument(
        "--private-log",
        action="store_true",
        help="write query provenance to ignored private log instead of tracked public log",
    )
    return parser.parse_args()


def log_attempt(args: argparse.Namespace, status: str, summary: str) -> None:
    append_record(
        kind="search",
        query=args.query,
        purpose=args.purpose,
        status=status,
        summary=summary,
        engine="tinyfish",
        output=PRIVATE_LOG if args.private_log else PUBLIC_LOG,
    )


def main() -> int:
    args = parse_args()
    api_key = os.environ.get("TINYFISH_API_KEY")
    if not api_key:
        log_attempt(args, "blocked", "TINYFISH_API_KEY was not set; no request was sent.")
        print("ERROR: TINYFISH_API_KEY is not set.", file=sys.stderr)
        print("Set it in the shell only; do not write it into files.", file=sys.stderr)
        return 1

    url = "https://api.search.tinyfish.ai?" + urllib.parse.urlencode({"query": args.query})
    request = urllib.request.Request(url, headers={"X-API-Key": api_key})
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            body = response.read().decode("utf-8", errors="replace")
            http_status = response.status
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        log_attempt(args, "failed", f"Request failed before a result artifact was created: {type(exc).__name__}.")
        print(f"TinyFish request failed: {exc}", file=sys.stderr)
        return 1

    try:
        data = json.loads(body)
    except json.JSONDecodeError:
        data = {"raw_text": body}

    output = args.output_json
    if not output.is_absolute():
        output = ROOT / output
    output.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "query": args.query,
        "endpoint": "https://api.search.tinyfish.ai",
        "http_status": http_status,
        "data": data,
    }
    output.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8", newline="\n")
    log_attempt(
        args,
        "complete",
        f"HTTP {http_status}; raw candidate results saved to {output.relative_to(ROOT) if output.is_relative_to(ROOT) else output}. No source was selected automatically.",
    )
    print(f"Saved TinyFish candidate results to: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
