# Gate 1 → 4 execution status

- **Date:** 2026-08-25
- **Rule:** this report separates completed literature/template work from unavailable physical evidence. It does not report a bench result, a force-plate result, or a human result.

## Step 1 — Gate 1 prior-art kill test: **completed for C21–C30; disposition OPEN (candidate not killed, novelty narrowed)**

The 30-paper attack matrix is at `research/reviews/01_prior_art_matrix.md`. It includes 20 read-scope rows and the 10 candidates C21–C30. As of 2026-08-26 all nine C21–C29 candidates were identity-verified (title/authors/venue/year/DOI) and read to abstract/selected full text; C30 is a citation-chasing map. The bounded screen found close *partial* neighbours but no source with the full combination of controlled perturbations + integrity estimate/quality gate + session-held-out longitudinal decision + false-alert endpoint + abstention/coverage in a plantar-sensing setting.

Three additional adversarial searches attacked the exact mechanism. They found the *general* pattern "monitor integrity → suppress data-driven false alerts" already established in industrial sensor-health monitoring/APM (`SRC-INDUS-SHM-ALERT-PATTERN`), structural health monitoring (`SRC-SHM-REVIEW-2025`), and longitudinal gait attribution (`SRC-SKDH-2025-GAIT-ATTRIB`), with abstention/coverage as mature ML machinery. None is a plantar insole with perturbation injection + longitudinal-false-alert + coverage endpoint.

| Candidate | What it occupies | Why it does not kill the candidate in declared scope |
|---|---|---|
| C21 `SRC-CARTER-2024-GRF` | 16-FSR+IMU LSTM GRF, LOSO | Subject/condition generalization, not longitudinal sessions or integrity state |
| C23 `SRC-HARON-2024-SHEAR-CALIB` | Calibration area/location change readings up to 80%/90% | Calibration/feasibility study; no runtime integrity estimate, no longitudinal alert/abstention |
| C25 `SRC-CHOCKALINGAM-2026-DEVICE-THRESH` | Device-dependent thresholds misclassify (5.4% agreement) | Recommends device-specific thresholds; no integrity estimator, no longitudinal-change or abstention endpoint |
| C27 `SRC-LATSCH-2026-INSOLE-REVIEW` | "Measurement disturbance"; calibration/verification gap; 9/41 use reference for sensor+gait | Motivates the gap; builds no operational integrity/alert system |
| C28 `SRC-PILLONI-2025-GAITHUB` | 3 weekly home sessions + clinic baseline; ICC/Bland-Altman | Longitudinal reliability only; no integrity state or false biological-change endpoint |
| C29 `SRC-KLUGE-2024-WRIST-GAIT` | Wrist IMU gait-event TP/FP/FN | Different device/task; transfer decision-metric logic only |
| Pattern `SRC-INDUS-SHM-ALERT-PATTERN` / `SRC-SHM-REVIEW-2025` | Integrity→false-alert suppression in machinery/structures | Different domain, residual/analytic-redundancy not perturbation injection; constrains novelty wording (see `CLM-NOV-003`) |

**Gate 1 disposition:** `OPEN`. The candidate is not killed, but this is a bounded screen, not a systematic review, so no GAP CONFIRMED (proof of absence) is permitted. Novelty must be framed narrowly per `CLM-NOV-003`: the plantar perturbation-injection integrity estimator + longitudinal-false-alert + coverage combination, explicitly citing the industrial-SHM and conformal-abstention prior patterns.

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
