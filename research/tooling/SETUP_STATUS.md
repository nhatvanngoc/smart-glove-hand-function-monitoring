# Research tooling setup status — 2026-08-25

## Pinned source checkouts

| Tool/source | Commit | Local role | Build/runtime state |
|---|---|---|---|
| Academic Research Skills | `6837b4dfeaab` | research/reviewer/pipeline methodology | cloned; four local skill links created and verified |
| PlotNeuralNet | `e96bc852189` | Python → TikZ diagrams | cloned; PDF rendering requires a TeX runtime |
| BVLC Caffe | `9b891540183d` | legacy architecture/reference source | cloned; intentionally not built |
| PGF/TikZ | `0a859c80b47` | upstream source/reference | cloned; intentionally not installed from source |
| MiKTeX | `76d1b3bd2b69` | upstream source/reference | cloned; **not** a TeX runtime |

Authoritative full hashes and URLs: `tools/research_sources.lock.json`.

## Runtime status

- Debian 12 Bookworm detected.
- Official MiKTeX Debian path and signing-key fingerprint check are implemented in `scripts/install_miktex_debian.sh`.
- Runtime MiKTeX installation in this sandbox remains **blocked** (APT/HTTPS endpoints) — `pdflatex` not available here. This is an environment/network blocker, not evidence that the installer or MiKTeX is invalid. Install the official MiKTeX installer on the real workstation.
- The ignored `.venv` has NumPy, Matplotlib and scikit-learn (installed 2026-08-25).
- Environment check result: **10/11** required/target checks pass; only `pdflatex` fails. `miktexsetup` remains an optional warning.

## Topic-related note (2026-08-25)

- All air-cushion/AAC artifacts (docs, cad, diagrams, simulation, pipeline, experiments, outputs, src, input baseline report, SOFA scripts) were **deleted** per DEC-TOPIC-003. No old smoke experiments remain; new experiment scripts will be added when the hardware/bench work begins.
- The five pinned third-party sources remain useful for the **new topic**: Academic Research Skills (methodology/review), PlotNeuralNet + PGF + MiKTeX (TikZ architecture diagrams), Caffe (legacy reference only).

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

- Do not build Caffe simply because PlotNeuralNet has Caffe-era examples.
- Do not install PGF master into a user TeX tree by default. Use the TeX distribution's PGF/TikZ package.
- Do not source-build MiKTeX unless package-manager installation is impossible on the actual workstation and the cost is explicitly accepted.
