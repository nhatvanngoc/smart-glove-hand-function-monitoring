# Research tooling setup status — 2026-08-16

## Pinned source checkouts

| Tool/source | Commit | Local role | Build/runtime state |
|---|---|---|---|
| Academic Research Skills | `6837b4dfeaab` | research/reviewer/pipeline methodology | cloned; four local skill links created and verified |
| PlotNeuralNet | `e96bc852189` | Python → TikZ diagrams | cloned; Python → TeX generation passed; PDF rendering blocked by missing TeX |
| BVLC Caffe | `9b891540183d` | legacy architecture/reference source | cloned; intentionally not built |
| PGF/TikZ | `0a859c80b47a` | upstream source/reference | cloned; intentionally not installed from source |
| MiKTeX | `76d1b3bd2b69` | upstream source/reference | cloned; **not** a TeX runtime |

Authoritative full hashes and URLs: `tools/research_sources.lock.json`.

## Runtime status

- Debian 12 Bookworm detected.
- Official MiKTeX Debian path and signing-key fingerprint check are implemented in `scripts/install_miktex_debian.sh`.
- Runtime installation in the current sandbox is **blocked**: both HTTP and HTTPS Debian APT endpoints failed (connection/TLS termination), so `gnupg` and `miktex` could not be installed. No successful `apt-get install` occurred.
- Consequently `pdflatex` is not yet available and PlotNeuralNet PDF rendering is not yet validated here. Its upstream Python architecture generation was validated separately.
- The ignored `.venv` is ready with NumPy, Matplotlib and scikit-learn; all seven existing synthetic experiment scripts execute. Several scientific acceptance checks fail or are non-informative; see `research/tooling/SMOKE_TESTS.md`.
- Environment check result: 10/11 required/target checks pass; only `pdflatex` fails. `miktexsetup` remains an optional warning.
- This is an environment/network blocker, not evidence that the prepared installer or MiKTeX is invalid.

## Commands

```bash
# Reproduce/check source trees and local ARS links
bash scripts/bootstrap_research_tooling.sh
bash scripts/bootstrap_research_tooling.sh --check

# Python core
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt

# Debian 12 MiKTeX runtime (requires working APT/HTTPS)
bash scripts/install_miktex_debian.sh

# Report readiness
python scripts/check_research_environment.py
python scripts/check_research_environment.py --strict
```

## Deliberate non-actions

- Do not build Caffe simply because PlotNeuralNet has Caffe-era examples; the current project reference models use NumPy-style code and no Caffe runtime import.
- Do not install PGF master into a user TeX tree by default. Use MiKTeX's tested PGF/TikZ package; use upstream PGF only for a documented compatibility investigation.
- Do not source-build MiKTeX unless package-manager installation is impossible on the actual workstation and the cost is explicitly accepted.
