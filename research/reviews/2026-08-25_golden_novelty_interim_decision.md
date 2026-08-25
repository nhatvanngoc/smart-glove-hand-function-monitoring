# Golden-novelty interim decision — after the first 20-paper matrix

- **Date:** 2026-08-25
- **Status:** evidence-informed project hypothesis; **not a final novelty claim** and not evidence of prototype performance.
- **Evidence base:** `research/reviews/2026-08-25_golden_novelty_gap_matrix.csv`; source-level read scope is in `research/evidence/SOURCE_LEDGER.csv`.

## Decision logic

### What literature has already occupied

1. **GRF/vGRF regression:** low-cost pressure, pressure+IMU, and even direct triaxial shoe sensors have been paired with ML and force-plate references (`SRC-ZHANG-2025-3DGRF`, `SRC-OLUGBON-2025-VGRF`, `SRC-YAMAGUCHI-2023-3DGRF`).
2. **Drift/calibration acknowledgment and local correction:** Velostat/piezoresistive characterization, contact-geometry features, calibration rules, and drift-compensation ideas all exist (`SRC-DEFAZIO-2021-VELOSTAT`, `SRC-OLUGBON-2025-VGRF`, `SRC-PARKER-2023-XSENSOR`).
3. **Repeatability/longitudinal feasibility:** same-day, two-session, multi-day and longer wearable monitoring studies exist (`SRC-ROUSE-2023-INSOLE-RETEST`, `SRC-LIU-2025-RELIABILITY`, `SRC-SCHELTINGA-2025-IMU-DAYS`, `SRC-NPJPD-2026-LONGITUDINAL`).
4. **Known measurement-system perturbations:** calibration-task mismatch, vertical load/active-cell count, sensor arrangement, shoe/insole placement or migration, loading history/creep, and sampling settings alter outputs (`SRC-BLIN-2022-COP`, `SRC-FUCHS-2024-REDUCED-COP`, `SRC-WEIZMAN-2019-BENCHMARK`, `SRC-ELSTUB-2022-SAMPLING`).

Therefore, none of the following can be presented as a central discovery: “estimate 3D-GRF,” “use GNN,” “correct drift,” “monitor longitudinally,” or “use a personal baseline.”

### Remaining bottleneck

The literature repeatedly measures *repeatability*, *agreement*, or a single error source, but the current matrix has not verified a close pressure-insole study that simultaneously:

1. creates **controlled and labeled measurement-system perturbations** (e.g., fit/placement, calibration-task mismatch, loading history; no asserted biological change);
2. uses a **reference trace** to quantify kinetic/COP error;
3. evaluates **held-out sessions**, not only within-session or participant-held-out windows;
4. evaluates a decision outcome: **false biological gait-change alerts**, missed controlled changes, and abstention/uncertainty;
5. compares against raw-pressure, ordinary recalibration, and contact/IMU baselines.

This is an **unresolved finding**, not proof of absence. The candidate survives because it targets a measurement-validity decision, not another regression architecture.

## Candidate golden novelty (narrow form)

> **Intervention-calibrated measurement-integrity monitoring for low-cost plantar sensing:** a system identifies when a longitudinal change is more consistent with a measurement-system state shift than with a repeatable gait change, and suppresses or labels low-confidence gait-change alerts.

The claim must remain conditional until full near-neighbor screening and an actual experiment. It must **not** say that the system discovers biology, diagnoses OA, or eliminates drift.

## Plausible mechanism (testable, not assumed)

Maintain an explicit quality/state channel alongside kinetic estimates:

`observed signal = gait/loading component + measurement-system/context component + residual`

Rather than claim complete latent disentanglement, use experimentally manipulated state variables and reference-load/force-plate errors to train or define a **quality gate**. A gate may return `valid`, `sensor/context-shift suspected`, or `abstain`; it is wrong if it silently relabels every change as biological.

## Golden filter score — provisional and deliberately conservative

| Criterion | Score / 10 | Reason and condition |
|---|---:|---|
| Importance | 9 | A false change alert invalidates longitudinal monitoring. |
| Novelty | 6 | Exact close prior art has not been verified yet; generic calibration/drift work is crowded. |
| Depth | 9 | Formal measurement-system state versus gait-state problem. |
| Measurability | 9 | Cross-session error, residual drift, false-alert/missed-alert, MDC and abstention are measurable. |
| Ground truth | 8 | Feasible only with force plate/reference loads and synchronization. |
| Feasibility | 6 | Requires controlled rigs/protocols and a force-plate route; hardware layout is not locked. |
| ISEF impact | 9 | A judge can understand “do not confuse a faulty measurement with a real gait change.” |
| Ceiling | 8 | Generalizable metrology contribution if results replicate across perturbations. |
| **Mean** | **8.0** | **Candidate passes triage, not confirmation.** |

## Falsification conditions

Reject or narrow this candidate if any occurs:

- a close paper already demonstrates the same intervention/held-out-session/false-alert protocol for comparable pressure insoles;
- force-plate or traceable reference access cannot be secured, making kinetic/COP claims impossible;
- controlled perturbations do not produce a state signal separable enough to improve a pre-registered decision metric;
- simple fixed calibration or contact/IMU baseline achieves equal false-alert control;
- the calibration/quality protocol is too burdensome to be credible for the asserted use case.

## Required experiment before claiming novelty

A locked protocol must contain:

1. **Bench metrology:** per-cell calibration, hysteresis, creep/loading history, repeated cycles, temperature if relevant, crosstalk and bending; reference-load record retained.
2. **No-change sessions:** standardized repeated sessions with predeclared no expected biological change.
3. **One-factor perturbations:** separate placement/fit, calibration-task mismatch, footwear/context, and loading-history interventions—one at a time where practicable.
4. **Reference validation:** synchronized force plate for the claimed GRF/COP components; do not infer Fx/Fy validity from pressure alone.
5. **Leakage-safe test:** leave-session-out; if data volume permits, leave-person-and-session-out.
6. **Baselines:** raw calibrated pressure; ordinary session calibration; contact/IMU baseline; linear/CNN/LSTM before ST-GNN.
7. **Endpoints:** error by session; residual drift; false and missed change-alert rates; confidence/abstention calibration; MDC; calibration time; latency/power only when measured.

## Current project positioning

The defensible title-level framing remains **longitudinal drift-robust kinetic monitoring**, but the candidate contribution is narrowed to **measurement integrity and false-change control**, conditional on the above validation. Knee OA remains an eventual application context only; it is not the ground truth, diagnostic target, or evidence source for this phase.

## Addendum 2026-08-26 — C21–C30 completed + adversarial pattern check

The 30-paper attack set is now complete (see `research/reviews/01_prior_art_matrix.md`). All nine C21–C29 candidates were identity-verified and read to abstract/selected full text; C30 is a citation-chasing map.

**Kill-test result: no prior art kills the candidate, and no GAP CONFIRMED (proof of absence) is claimed.** No verified source combines controlled perturbations + integrity state + held-out-session longitudinal evaluation + false biological-change endpoint + abstention/coverage in a plantar-sensing setting.

**Important novelty constraint discovered (see `CLM-NOV-003`).** The adversarial searches showed that the *general* pattern "monitor measurement integrity → suppress data-driven false alerts" is already established outside plantar sensing:

- industrial sensor-health monitoring / APM (e.g. GE Vernova SmartSignal) suppresses alerts driven by unhealthy sensors to cut false positives;
- structural health monitoring treats operational/environmental normalization as a criterion to avoid misreading benign change as damage (`SRC-SHM-REVIEW-2025`);
- longitudinal gait work explicitly frames attributing change to clinical status rather than algorithmic error (`SRC-SKDH-2025-GAIT-ATTRIB`);
- abstention/coverage is mature ML machinery (selective conformal risk control, conformal abstention, wearable signal-quality gates).

Therefore the novelty **must not** be stated as "monitor integrity to suppress false alerts" or "abstain under uncertainty". It must be stated as the specific transfer: a **perturbation-injection** measurement-integrity estimator for a low-cost plantar insole, evaluated against a **longitudinal biological-change false-alert** endpoint with an explicit coverage/selective-risk trade-off, versus raw-pressure / recalibration / contact-IMU baselines.

**Revised golden-filter scores (conservative):** Novelty 6 → 6 (unchanged: no kill found, but the conceptual neighbourhood is now known to be crowded, so the ceiling on novelty rests on the specific plantar perturbation-injection + longitudinal-false-alert combination, not on the abstract idea). Mean remains **8.0 — candidate passes triage, still not confirmed**. Gate 1 stays **OPEN**.
