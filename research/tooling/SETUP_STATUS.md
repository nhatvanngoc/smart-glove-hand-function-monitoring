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
- Runtime MiKTeX installation in this local test environment remains **blocked** (APT/HTTPS endpoints) — `pdflatex` not available here. This is an environment/network blocker, not evidence that the installer or MiKTeX is invalid. Install the official MiKTeX installer on the real workstation.
- The ignored `.venv` has NumPy, Matplotlib and scikit-learn (**reinstalled 2026-09-27**; + `pypdf` for local PDF text extraction — not a runtime dependency).
- Environment check result (re-run 2026-09-27): **10/11** required/target checks pass; only `pdflatex` fails. `miktexsetup` remains an optional warning.
- Third-party checkouts + 4 skill links re-verified 2026-09-27 via `bootstrap_research_tooling.sh` (all `READY`, pinned commits match lock file).

## Current workspace verification (2026-10-17)

Re-run in the Arena workspace for the proposal-writing session:

- `bash scripts/bootstrap_research_tooling.sh` — completed; the five repositories match the full commit pins in `tools/research_sources.lock.json`; all four local skill links resolve.
- `python3 -m venv .venv` and `.venv/bin/python -m pip install -r requirements.txt` — completed; NumPy, Matplotlib and scikit-learn import successfully. `.venv/` and `.tools/` are local/ignored, not committed dependencies.
- `.venv/bin/python scripts/check_research_environment.py` — **10/11** checks pass. The sole required/target failure is `pdflatex` not installed; optional `miktexsetup` is also absent. No TeX distribution was installed in this run. PDF/LaTeX rendering therefore remains unavailable here; this does not block research ledger, Markdown or Python analysis work.
- `bash scripts/bootstrap_research_tooling.sh --check` — all pinned checkouts passed.
- Current Drive intake was read, not modified: see `research/context/CURRENT_SUBMISSION_2026-10-17.md`.

Reproduce the setup with the commands above. Do not claim `--strict` passes until a TeX runtime is installed and the check is rerun.

## Documentation-only pass (2026-10-19)

- No runtime, dependency or tooling change was made in this pass: nothing was installed, no venv was created, no script was executed against hardware, and no PDF/LaTeX rendering was attempted (`pdflatex` remains unavailable here).
- Work produced was documentation only: Gate 0 artifacts (`research/protocols/10`, `10a`, `10b`), `docs/07_Vision_TaskState_Architecture.md`, `docs/08_Software_Firmware_Roadmap.md`, the §C.4/§C.5 additions to the A/B/C draft, and ledger/context updates.
- Sandbox network note for the future coding phase: this environment reaches only `github.com`, `codeload.github.com`, `api.github.com`, `registry.npmjs.org`, `pypi.org` and `files.pythonhosted.org`. An ESP32 toolchain (PlatformIO/esptool downloads from `dl.espressif.com` / `registry.platformio.org`) therefore **cannot** be installed here; firmware must be built and flashed on the team's own machine. Host-side Python and unit tests of mirrored control logic are possible here.
- Structural checks run in this pass: `scripts/check_bench_templates.py` (bench templates untouched) and a CSV integrity check of `research/claims/CLAIM_LEDGER.csv` (11 columns per row, unique claim IDs).

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

## DOCX review build (2026-10-20)

- `scripts/build_abc_review_docx.py` converts `docs/DE_CUONG_A_B_C_DRAFT_2026-10-19.md` into `exports/11A2_CAP_NHAT_DU_THAO_2026-10-20.docx`.
- Requires **`python-docx`** (`pip install python-docx`). It is deliberately **not** added to `requirements.txt`, which covers the simulation/plotting stack only.
- Verified with `python3 scripts/build_abc_review_docx.py --check` → PASS (no leftover Markdown syntax, no truncated link paths, pre-registration table 15×6, build date valid, all `##` headings present).
- The build date is computed in **Asia/Saigon (UTC+7)** because the build machine may sit in another timezone; a first attempt stamped the previous day.
- Output is a **review copy**, not an approved or submitted document. No numbers are generated by the script; every `OPEN` slot stays empty.

## Deliberate non-actions

- Do not build Caffe simply because PlotNeuralNet has Caffe-era examples.
- Do not install PGF master into a user TeX tree by default. Use the TeX distribution's PGF/TikZ package.
- Do not source-build MiKTeX unless package-manager installation is impossible on the actual workstation and the cost is explicitly accepted.
