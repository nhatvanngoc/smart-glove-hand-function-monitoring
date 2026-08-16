#!/usr/bin/env python3
"""
TinyFish search helper without storing API keys.

Usage in WSL/Linux:
    export TINYFISH_API_KEY='YOUR_KEY_HERE'
    python scripts/tinyfish_search.py "velostat" outputs/reports/tinyfish_velostat.json

Security:
    - API key is read from environment variable only.
    - API key is not written to output files.
    - Do not commit or paste the key into Markdown/code.
"""
from __future__ import annotations

import json
import os
import sys
import urllib.parse
import urllib.request
from pathlib import Path


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: python scripts/tinyfish_search.py <query> [output_json]", file=sys.stderr)
        return 2

    query = sys.argv[1]
    out_path = Path(sys.argv[2]) if len(sys.argv) >= 3 else Path("outputs/reports/tinyfish_search.json")

    api_key = os.environ.get("TINYFISH_API_KEY")
    if not api_key:
        print("ERROR: TINYFISH_API_KEY is not set.", file=sys.stderr)
        print("Set it in the shell, e.g.: export TINYFISH_API_KEY='...'; do not write it into files.", file=sys.stderr)
        return 1

    url = "https://api.search.tinyfish.ai?" + urllib.parse.urlencode({"query": query})
    req = urllib.request.Request(url, headers={"X-API-Key": api_key})

    with urllib.request.urlopen(req, timeout=30) as resp:
        body = resp.read().decode("utf-8", errors="replace")
        status = resp.status

    try:
        data = json.loads(body)
    except json.JSONDecodeError:
        data = {"raw_text": body}

    out_path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "query": query,
        "endpoint": "https://api.search.tinyfish.ai",
        "http_status": status,
        "data": data,
    }
    out_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Saved TinyFish result to: {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
