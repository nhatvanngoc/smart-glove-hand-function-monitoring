# Gate 1 → 4 execution status

- **Date:** 2026-08-25
- **Rule:** this report separates completed literature/template work from unavailable physical evidence. It does not report a bench result, a force-plate result, or a human result.

## Step 1 — Gate 1 prior-art kill test: executed, **not yet passed**

The 30-paper attack matrix is at `research/reviews/01_prior_art_matrix.md`. It includes 20 read-scope rows and 10 explicit candidates. The current bounded screen found close *partial* neighbors but did not verify a system with the full combination of controlled perturbations + integrity estimate/quality gate + session-held-out longitudinal decision + false-alert endpoint + abstention/coverage.

| Candidate | What it occupies | Why it does not yet kill the candidate in declared scope |
|---|---|---|
| Olugbon 2025 (`SRC-OLUGBON-2025-VGRF`) | Drift/generalization-aware vGRF with contact-geometry+IMU | No verified multi-session measurement-state attribution, false gait-change endpoint or abstention |
| Blin 2022 (`SRC-BLIN-2022-COP`) | Calibration-task match and condition-dependent COP accuracy | No verified longitudinal integrity decision |
| Weizman 2019 (`SRC-WEIZMAN-2019-BENCHMARK`) | Placement/stacking affects accuracy | No integrity estimator or decision endpoint |
| Parker 2023 (`SRC-PARKER-2023-XSENSOR`) | Two-day metrology, creep/protocol suitability | No gait-change attribution |
| Scheltinga 2025 (`SRC-SCHELTINGA-2025-IMU-DAYS`) | Multi-day repeatability and session-effect confounding | IMU-only; does not resolve source attribution with a pressure-insole integrity gate |
| Candidate C23 | Calibration area/location can dominate in-shoe shear readings | Must complete full identity/method read; no full-combination endpoint verified |
| Candidate C25 | Device-dependent thresholds can alter classification | Must complete identity/method read; no abstention/longitudinal protocol verified |
| Candidate C28 | Home longitudinal reliability with calibration/placement supervision | No measurement-integrity state or false biological-change endpoint verified |
| Candidate C29 | TP/FP/FN gait detection decision metrics | Different wrist-sensor task; no pressure-insole measurement-state protocol |

**Gate 1 disposition:** `OPEN`. The candidate is not killed, but no GAP CONFIRMED claim is permitted until C21–C30 and their strongest cited primary neighbors are fully verified.

## Step 2 — reference readiness: **BLOCKED by owner/open infrastructure decision**

No actual force plate, multi-axis load-cell, traceable load reference, availability date, sampling specification, synchronization trigger, or calibration record exists in this repository. Therefore no 3D-GRF/COP validation plan can be considered operational.

Required lock record before Gate 2:

```text
reference type/model:
axes available:
calibration certificate or traceability locator:
sampling rate and clock/trigger plan:
availability/access owner and date:
coordinate-system convention:
permitted reference-load fixture for bench phase:
```

If this cannot be locked, scope must remain bench pressure/metrology; it may not claim 3D-GRF/COP validation.

## Step 3 — Phase-A bench metrology: **prepared; physical execution blocked**

Created and structurally validated templates/tooling:

- `research/bench/templates/session_manifest.csv`
- `research/bench/templates/perturbation_log.csv`
- `research/bench/templates/reference_check.csv`
- `scripts/check_bench_templates.py` (PASS)

No data rows were created. The templates are not measurements. Bench execution is blocked until a traceable/characterized reference-load fixture and actual sensor/DAQ configuration are available.

## Step 4 — Gate-2 perturbation viability: **not evaluable yet**

Gate 2 requires at least two perturbation families with reference-derived degradation reproducibly greater than the nominal noise/repeatability bound. No such measurements exist. Therefore:

```text
perturbation viability: NOT MEASURED
measurement-integrity labels: NOT MEASURED
false-alert baseline: NOT MEASURED
GO/NO-GO: BLOCKED, not failed
```

## Next executable action after hardware/reference access

1. Freeze sensor/layout/firmware manifest.
2. Run nominal reference-load repeatability before perturbations.
3. Screen P1 placement and P2 loading history first; retain raw records and null results.
4. Advance only reproducible perturbations to P3 calibration-mismatch testing.
5. Compute Gate-2 decision strictly from the pre-specified noise/repeatability criterion; do not build a model first.
