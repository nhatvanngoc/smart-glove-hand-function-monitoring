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

## Kill-test conclusion as of this checkpoint

**No GAP CONFIRMED.** No read/verified row above has established the full proposed combination; this is not evidence that no such work exists. Candidate C21–C30 must be read before Gate 1 can pass.

A near-neighbor kills this candidate if it has all of: controlled sensor/system perturbations; explicit integrity/state estimate or quality gate; longitudinal/held-out-session evaluation; false biological-change or equivalent decision endpoint; abstention/coverage (or an equivalent selective-decision evaluation); and a comparable plantar-sensing setting.
