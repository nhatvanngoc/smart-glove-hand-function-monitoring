# 01 — Prior-art kill matrix: measurement integrity → longitudinal change detection → abstention

- **Status:** active attack matrix, not a systematic-review conclusion.
- **Question under attack:** Does a close prior-art pressure-insole system already combine controlled measurement perturbations, explicit measurement-integrity estimation, longitudinal change detection, false-alert evaluation, and abstention/coverage evaluation?
- **Rule:** `—` means not verified in the declared read scope; it never means the feature does not exist. `CANDIDATE` rows cannot support a gap claim until identity/full text is verified.
- **Primary source ledger:** `research/evidence/SOURCE_LEDGER.csv`.

## Feature matrix — verified/read-scope rows

| ID | Source | Calibration / perturbation observed | Longitudinal / repeated session | Explicit measurement state / quality gate | False gait-change endpoint | Abstention / coverage | Verdict for close-prior-art test |
|---|---|---|---|---|---|---|---|
| P01 | `SRC-OLUGBON-2025-VGRF` | Contact-geometry feature intended to reduce raw pressure drift effects | intra/inter-participant; multi-session protocol not verified | No explicit integrity state verified | — | — | Close vGRF mitigation neighbor, not full combination |
| P02 | `SRC-ZHANG-2025-3DGRF` | Multimodal pressure+IMU | Longitudinal design not verified | — | — | — | Close 3D-GRF regression neighbor |
| P03 | `SRC-YAMAGUCHI-2023-3DGRF` | Four direct triaxial sole sensors; task models | Longitudinal design not verified | — | — | — | Closes generic 3D-GRF claim, different sensor physics |
| P04 | `SRC-DEFAZIO-2021-VELOSTAT` | Velostat characterization and history/time correction | — | No explicit integrity state verified | — | — | Close sensor-characterization/correction neighbor |
| P05 | `SRC-HU-2023-VELOSTAT` | Velostat matrix; crosstalk handling/cell heterogeneity | — | — | — | — | Low-cost Velostat architecture neighbor, phase-only |
| P06 | `SRC-JUNG-2026-PIEZO-SHEAR` | Cyclic drift/stabilization characterization | — | — | — | — | Demonstrates drift is measurable, no attribution protocol |
| P07 | `SRC-PARKER-2023-XSENSOR` | Two-day bench loading; duration/load/contact-area effects | two days | — | — | — | Reference for pressure metrology, not gait alerting |
| P08 | `SRC-BLIN-2022-COP` | Calibration-task match; load and active-cell effects | — | Reference-frame calibration, not integrity estimate | — | — | Strong calibration-mismatch neighbor |
| P09 | `SRC-FUCHS-2024-REDUCED-COP` | Sensor number/layout × gait type | — | — | — | — | Strong layout/context neighbor |
| P10 | `SRC-WEIZMAN-2019-BENCHMARK` | Insole relative position affects accuracy | — | — | — | — | Strong placement perturbation neighbor |
| P11 | `SRC-ROUSE-2023-INSOLE-RETEST` | Multiple activities; force-plate agreement | same-day two sessions | — | — | — | Separates repeatability from agreement, no alert endpoint |
| P12 | `SRC-LIU-2025-RELIABILITY` | Linear/curved conditions, MDC and step-distance need | 4–7-day retest | No integrity gate verified | — | — | Strong MDC/reliability neighbor |
| P13 | `SRC-SCHELTINGA-2025-IMU-DAYS` | Session effects; placement/natural variability confounded | 3 outdoor days | No explicit state separation | — | — | Closest conceptual day-to-day attribution neighbor; IMU-only |
| P14 | `SRC-ELSTUB-2022-SAMPLING` | Sampling rate as controlled measurement perturbation | — | — | — | — | Embedded acquisition boundary, not integrity protocol |
| P15 | `SRC-SCIREP-2025-INDIVIDUALITY` | Intra- vs inter-individual pressure variation | repeated trials | — | — | — | Personal-baseline/statistical neighbor |
| P16 | `SRC-NPJPD-2026-LONGITUDINAL` | Reliability and disease specificity selection | months/years | Metric selection, not sensor-state gate | no device-error alert endpoint verified | — | Longitudinal endpoint framework, wrong device/disease |
| P17 | `SRC-SANTOS-2024-REVIEW` | Review identifies calibration/real-world/longitudinal limitations | review | — | — | — | Map only; cannot prove absence |
| P18 | `SRC-ISEF-2026-HUMAN` | N/A; rule reference | N/A | N/A | N/A | N/A | Human tests require pre-approval; bench work remains allowed |
| P19 | `SRC-OWNER-2026-08-25B` | Owner-selected intended perturbation direction | proposed only | proposed only | proposed only | proposed only | Project provenance, not prior art |
| P20 | `SRC-DOC-THEORY-02` | Project theory labels uncertainty | proposed only | proposed only | proposed only | proposed only | Internal navigation only |

## Candidate papers to complete the 30-paper attack set

| ID | Candidate / locator | Why it was selected | Required verification before it enters a conclusion |
|---|---|---|---|
| C21 | Carter et al., *Consumer-priced wearable sensors … predict GRF*, PeerJ 2024, `peerj.com/articles/17896` | 16 resistive sensors + IMU; LOSO GRF | Confirm authors, full methods, any session split/quality logic |
| C22 | Jlassi et al., *Outdoor Walking Classification … IMU and Foot Pressure*, Sensors 2026, DOI `10.3390/s26010232` | Context state observable with IMU/pressure | Check whether context is used for longitudinal validity or only classification |
| C23 | *In-shoe plantar shear stress sensor design, calibration and evaluation*, PLOS ONE 2024, DOI `10.1371/journal.pone.0309514` | Calibration area/location perturbation | Read full methods; extract authors and any integrity/alert endpoint |
| C24 | *Testing protocols and measurement techniques when using pressure sensors …*, J Biomech 2024, PII `S0958259224000270` | Calibration/drift protocol review | Verify bibliographic identity and review scope |
| C25 | *Device-dependent variability of plantar pressure thresholds*, 2026, PII `S0966636226000366` | Device/protocol state changes clinical classification | Verify authors, study design, whether alert misclassification is measured |
| C26 | *A wireless, self-powered smart insole … nonlinear synergistic pressure sensing*, Sci Adv 2025 | Long-cycle sensor stability claim | Verify full test conditions; not equate 180k cycles with longitudinal gait validity |
| C27 | *A Review of Sensor Insoles*, arXiv 2025 | Explicit “measurement disturbance” framing | Treat as preprint/review; chase its primary citations |
| C28 | GAIT-HUB, *Monitoring Mobility at Home*, 2025, PMCID `PMC12310191` | Home longitudinal reliability/placement/calibration protocol | Verify whether error alerts/abstention occur |
| C29 | *Real-World Gait Detection Using a Wrist-Worn Inertial Sensor*, 2024, PMCID `PMC11097052` | Explicit TP/FP/FN and specificity trade-off | Transfer only decision-metric logic, not device claims |
| C30 | *Device-dependent variability …* companion citations and calibration standards | Citation chasing from C25 | Locate primary pressure-insole measurement-state studies |

## C21–C30 — verification result (2026-08-26)

All nine primary/review candidates were identity-verified (title/authors/venue/year/DOI) and read to abstract or selected full-text. Full records are in `research/evidence/SOURCE_LEDGER.csv`. `—` still means "not verified in declared scope", never "absent".

| ID | Verified source | Controlled perturbation | Longitudinal / repeated session | Integrity state / quality gate | False gait-change endpoint | Abstention / coverage | Kills candidate? |
|---|---|---|---|---|---|---|---|
| C21 | `SRC-CARTER-2024-GRF` (PeerJ 12:e17896) | Subject/condition variation, not injected measurement perturbation | LOSO across subjects, not sessions | — | — | — | No |
| C22 | `SRC-JLASSI-2026-OUTDOOR` (Sensors 26(1):232) | — | — | — | — | — | No (classification task) |
| C23 | `SRC-HARON-2024-SHEAR-CALIB` (PLOS ONE 19(9):e0309514) | Yes — indenter area/location, up to 80%/90% reading change | Two 15-min sessions, 1 diabetic + 1 healthy | Calibration procedure, not a runtime integrity estimate | — | — | No (closest calibration-perturbation neighbour) |
| C24 | `SRC-BURNIE-2024-PRESSURE-REVIEW` (Foot 59:102094) | Review of calibration suitability | Review | Review recommends, does not build | — | — | No (map only; venue corrected from J Biomech) |
| C25 | `SRC-CHOCKALINGAM-2026-DEVICE-THRESH` (Gait Posture 126:110128) | Device/system differences | Cross-device, single condition | No integrity estimator; recommends device-specific thresholds | Threshold misclassification (5.4% agreement), not longitudinal change | — | No (closest clinical-decision neighbour) |
| C26 | `SRC-WANG-2025-SELFPOWERED` (Sci Adv 11:eadu1598) | 180k-cycle durability ≠ measurement perturbation | — | — | — | — | No |
| C27 | `SRC-LATSCH-2026-INSOLE-REVIEW` (IEEE Sensors J 26(3):3577-3596) | Frames "measurement disturbance" | Review | Recommends calibration/verification discipline | — | — | No (motivates the gap) |
| C28 | `SRC-PILLONI-2025-GAITHUB` (Digit Biomark 9(1):140-154) | Placement/supervision protocol | 3 weekly home sessions + clinic baseline | Cross-device agreement, not integrity state | — | — | No (longitudinal reliability only) |
| C29 | `SRC-KLUGE-2024-WRIST-GAIT` (JMIR Form Res 8:e50035) | — | — | — | Gait-event TP/FP/FN (different task) | Implicit in detection metrics | No (wrist IMU; transfer metrics only) |
| C30 | Citation chasing from C25/C27 | — | — | — | — | — | Map only; `SRC-LATSCH-2026-INSOLE-REVIEW` reports 9/41 insoles use a reference for both sensor test and gait |

**C21–C30 disposition: none kills the candidate.** No verified source combines all six criteria.

## Adversarial pattern check — the danger is over-claiming, not a single kill paper

Direct attacks on the exact combination surfaced **no** plantar-insole system with the full set, but surfaced a strong *general* pattern that constrains how novelty may be worded:

| Pattern source | What it establishes | Domain |
|---|---|---|
| `SRC-INDUS-SHM-ALERT-PATTERN` (GE Vernova APM SmartSignal, non-academic vendor page) | "Monitor sensor health → suppress alerts driven by unhealthy data → reduce false-positive alerts" is an already-deployed engineering pattern (via analytic redundancy/residuals, not injected perturbations) | Rotating machinery / industrial asset performance |
| `SRC-SHM-REVIEW-2025` (PMC11902730) | Quantifying operational/environmental conditions to normalize data "preventing benign changes from being misinterpreted as damage … reducing false alarms (Type I)" is a standard performance criterion | Structural health monitoring |
| `SRC-SKDH-2025-GAIT-ATTRIB` (JMIR 27:e72831) | Longitudinal changes "must be confidently attributed to underlying clinical status rather than algorithmic error" — the exact problem framing, in IMU gait | Wearable IMU gait |
| Selective Conformal Risk Control (arXiv:2512.12844); conformal abstention; ICCM (arXiv:2608.18397) | Abstention/coverage (selective risk vs coverage) is mature ML machinery already applied to wearable signal-quality gating | General ML / wearables |

**Consequence:** the novelty may **not** be framed as "monitor integrity to suppress false alerts" or "abstain under uncertainty" — both are established. It must be framed as the **specific transfer**: a *perturbation-injection* measurement-integrity estimator for a low-cost plantar insole, evaluated against a *longitudinal biological-change false-alert* endpoint with an explicit coverage/selective-risk trade-off.

## Kill-test conclusion as of this checkpoint (2026-08-26)

**No PRIOR ART FOUND (kill), and no GAP CONFIRMED (proof of absence).** All 20 read-scope rows and all 9 C21–C29 candidates plus the C30 map were verified; none carries the full six-criterion combination. Three direct adversarial searches on the exact mechanism found the *general* integrity→alert-suppression pattern in other domains but not in a plantar insole with perturbation injection and a coverage endpoint.

This is a **bounded screen, not a systematic review**: it establishes that no kill paper was found in the declared scope, not that none exists. Per `AGENTS.md`, "not found" ≠ "does not exist".

A near-neighbour kills this candidate if it has all of: controlled sensor/system perturbations; explicit integrity/state estimate or quality gate; longitudinal/held-out-session evaluation; false biological-change or equivalent decision endpoint; abstention/coverage (or an equivalent selective-decision evaluation); and a comparable plantar-sensing setting. None verified so far does.

**Gate 1 disposition: OPEN — candidate not killed, novelty framing narrowed.** The candidate may proceed to bench/falsification work, but any novelty statement must cite the industrial-SHM and conformal-abstention prior patterns and claim only the plantar perturbation-injection + longitudinal-false-alert + coverage combination.
