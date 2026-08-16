#!/usr/bin/env bash
# Reproducibly prepare third-party research/tooling checkouts.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LOCK="$ROOT/tools/research_sources.lock.json"
SOURCES="$ROOT/.tools/sources"
MODE="sync"
LINK_SKILLS=1

usage() {
  cat <<'EOF'
Usage: scripts/bootstrap_research_tooling.sh [--check] [--no-skill-links]

  --check           verify local checkouts without using the network
  --no-skill-links  do not create local .claude/skills links

Checkouts are pinned by tools/research_sources.lock.json and treated as
read-only third-party material. Caffe, PGF, and MiKTeX are not built here.
EOF
}

while (($#)); do
  case "$1" in
    --check) MODE="check" ;;
    --no-skill-links) LINK_SKILLS=0 ;;
    -h|--help) usage; exit 0 ;;
    *) echo "Unknown option: $1" >&2; usage >&2; exit 2 ;;
  esac
  shift
done

for cmd in git python3; do
  command -v "$cmd" >/dev/null || { echo "Missing required command: $cmd" >&2; exit 1; }
done
[[ -f "$LOCK" ]] || { echo "Missing lock file: $LOCK" >&2; exit 1; }
mkdir -p "$SOURCES"

mapfile -t REPOS < <(python3 - "$LOCK" <<'PY'
import json, sys
with open(sys.argv[1], encoding="utf-8") as f:
    data = json.load(f)
for item in data["repositories"]:
    print("\t".join(item[k] for k in ("name", "url", "ref", "commit")))
PY
)

failed=0
for row in "${REPOS[@]}"; do
  IFS=$'\t' read -r name url ref commit <<<"$row"
  dest="$SOURCES/$name"

  if [[ "$MODE" == "check" ]]; then
    if [[ ! -d "$dest/.git" ]]; then
      printf 'MISSING  %s\n' "$name"
      failed=1
      continue
    fi
    actual_url="$(git -C "$dest" remote get-url origin 2>/dev/null || true)"
    actual_commit="$(git -C "$dest" rev-parse HEAD 2>/dev/null || true)"
    dirty="$(git -C "$dest" status --porcelain 2>/dev/null || true)"
    if [[ "$actual_url" == "$url" && "$actual_commit" == "$commit" && -z "$dirty" ]]; then
      printf 'OK       %-28s %s\n' "$name" "${commit:0:12}"
    else
      printf 'MISMATCH %-28s expected=%s actual=%s\n' "$name" "${commit:0:12}" "${actual_commit:0:12}"
      [[ "$actual_url" != "$url" ]] && printf '         origin expected=%s actual=%s\n' "$url" "$actual_url"
      [[ -n "$dirty" ]] && printf '         checkout has local changes\n'
      failed=1
    fi
    continue
  fi

  if [[ -e "$dest" && ! -d "$dest/.git" ]]; then
    echo "Refusing to overwrite non-Git path: $dest" >&2
    exit 1
  fi

  if [[ ! -d "$dest/.git" ]]; then
    echo "Cloning $name ($ref)..."
    git clone --depth 1 --filter=blob:none --single-branch --branch "$ref" "$url" "$dest"
  fi

  actual_url="$(git -C "$dest" remote get-url origin)"
  [[ "$actual_url" == "$url" ]] || {
    echo "Origin mismatch for $name: $actual_url" >&2
    exit 1
  }
  if [[ -n "$(git -C "$dest" status --porcelain)" ]]; then
    echo "Refusing to alter modified third-party checkout: $dest" >&2
    exit 1
  fi
  if ! git -C "$dest" cat-file -e "${commit}^{commit}" 2>/dev/null; then
    echo "Fetching pinned commit for $name..."
    git -C "$dest" fetch --depth 1 origin "$commit"
  fi
  git -C "$dest" checkout --quiet --detach "$commit"
  printf 'READY    %-28s %s\n' "$name" "${commit:0:12}"
done

if ((LINK_SKILLS)); then
  ars="$SOURCES/academic-research-skills"
  skills_dir="$ROOT/.claude/skills"
  if [[ -d "$ars" ]]; then
    mkdir -p "$skills_dir"
    for skill in deep-research academic-paper academic-paper-reviewer academic-pipeline; do
      link="$skills_dir/$skill"
      target="../../.tools/sources/academic-research-skills/$skill"
      if [[ -L "$link" && "$(readlink "$link")" == "$target" ]]; then
        :
      elif [[ -e "$link" || -L "$link" ]]; then
        echo "Refusing to replace existing skill path: $link" >&2
        exit 1
      else
        ln -s "$target" "$link"
      fi
    done
    echo "Local Academic Research Skills links are ready in .claude/skills/."
  elif [[ "$MODE" != "check" ]]; then
    echo "Academic Research Skills checkout missing; cannot link skills." >&2
    failed=1
  fi
fi

if [[ "$MODE" == "check" && $failed -ne 0 ]]; then
  exit 1
fi

cat <<'EOF'
Source setup complete. This intentionally does not:
  - build legacy Caffe;
  - install PGF from source (use the TeX distribution package);
  - turn the MiKTeX source checkout into a TeX runtime.
Run scripts/install_miktex_debian.sh where applicable, then run
python scripts/check_research_environment.py --strict.
EOF
