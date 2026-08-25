# Golden-novelty hunt — reverse-engineering failure mechanisms

- **Status:** working protocol + verified seed cards; **not** a final novelty claim or systematic review.
- **Rule:** every card distinguishes direct source observation, inference, and project hypothesis. A search miss is never evidence that a method does not exist.
- **Target question:** can a low-cost plantar-sensing insole retain *measurement fidelity* across time and changing measurement conditions sufficiently to distinguish a repeatable gait deviation from sensor/environment-induced change?

## 1. Correction that changes the landscape

The supplied “2021” vGRF lead is verified as **Olugbon et al., arXiv:2501.07748 (2025), a preprint**, not a 2021 peer-reviewed paper (`SRC-OLUGBON-2025-VGRF`). It directly states that wearable vGRF methods suffer from pressure-sensor drift and poor generalization, then avoids raw pressure magnitude by treating pressure cells as pressed/not-pressed to compute a center-of-pressed-sensors feature and fusing it with IMU data.

This is important close prior art. It means “use IMU + spatial pressure/contact features + ML to mitigate drift for vGRF” is **not** a golden novelty. Its demonstrated scope, from the read artifact, is vGRF intra-/inter-participant testing; it does not itself establish a multi-session causal separation of biological change from sensor/environment state.

## 2. Technology landscape fields (mandatory for 20–30-paper matrix)

| Field to extract | Required question |
|---|---|
| Measurement target | pressure / Fz / 3D-GRF / COP / gait metric / clinical endpoint? |
| Sensor & configuration | modality, cell count/layout, IMU, shoe/insole construction, sensor placement? |
| Reference & synchronization | force plate, motion capture, load rig; sample rate and trigger/clock alignment? |
| Calibration | factory, static/dynamic, task-matched, person-specific, per-session, none? |
| Dataset & split | participant/session/task/footwear/environment coverage; leakage-safe split? |
| Failure mechanism reported | drift, creep, hysteresis, fit, bending, migration, temperature, task/domain shift, model uncertainty? |
| Limitation / future work | exact author-stated limitation, with section/page anchor where available |
| Remaining gap | a falsifiable question, never “no one did it” |
| Hardware fit | which hypothesis component can Velostat/Mega/RK3588/IMU/reference rig actually implement? |

## 3. Verified seed Gap Cards

### GN-01 — Contact geometry as a drift-avoidance feature, not sensor-state separation

- **Literature says:** Olugbon et al. identify drift/generalization limitations and use binary pressure contacts plus IMU to estimate **vGRF** (`SRC-OLUGBON-2025-VGRF`, Abstract, Introduction, Discussion).
- **Existing mechanism:** discard raw pressure magnitude for the center-of-pressed-sensors feature; fuse with IMU; compare ANN/RF/LSTM.
- **What remains unshown in the read scope:** whether a detected change on day 30 is gait biology, shoe fit, sensor wear, thermal state, loading history, or a combination.
- **Candidate gap, not confirmed:** multi-session **attribution**, not merely vGRF regression.
- **Killer discriminator:** fixed reference-load checks and no-biological-change repeated sessions; perturb sensor/environment state separately from gait task; compare raw pressure, contact-geometry/IMU baseline, ordinary recalibration, and a proposed sensor-state-aware method on held-out sessions.

### GN-02 — Task-matched calibration is an exposed hidden variable

- **Literature says:** CoP accuracy is best when calibration motion matches the evaluated motion and changes with vertical force and number of active cells (`SRC-BLIN-2022-COP`, Abstract).
- **Contradiction to mine:** a system can be accurate in a matched calibration/task condition yet inaccurate after a condition shift.
- **Hidden state candidate:** sensor-to-foot/shoe coordinate and loading-state mismatch, represented initially as `S_t` rather than assumed fixed.
- **Candidate gap, not confirmed:** can `S_t` be estimated or flagged online well enough that the system **abstains** from biological-change claims when measurement conditions have shifted?
- **Killer discriminator:** calibrate on walk and evaluate run/cut or deliberately modify fit/footwear; force-plate CoP gives the reference; measure error, calibration burden, and false gait-change alerts.

### GN-03 — Sensor count/layout is not merely a hardware detail

- **Literature says:** CoP concordance/RMSE varies by reduced layout and gait in simulated layouts (`SRC-FUCHS-2024-REDUCED-COP`, Abstract).
- **Implication:** layout can interact with gait condition; “16 ADC inputs” cannot be justified by convenience alone.
- **Candidate gap, not confirmed:** choose a layout by *longitudinal change-detection reliability*, not just same-session CoP RMSE.
- **Killer discriminator:** pre-register 8/12/16-cell candidate layouts (or multiplexed alternatives) under the same reference, changes in fit, and multiple sessions; evaluate minimum detectable change and false-change rate.

### GN-04 — Mechanical placement/configuration perturbs the measurement system

- **Literature says:** relative insole position affected accuracy in a smart-insole/Pedar/force-plate benchmark (`SRC-WEIZMAN-2019-BENCHMARK`, Highlights); the article also notes in-shoe systems cannot directly measure horizontal GRF.
- **Implication:** fitting/stacking/placement is a measurable nuisance variable, not laboratory noise to ignore.
- **Candidate gap, not confirmed:** a measurement-integrity model that detects/compensates a placement-state change without miscalling it a gait change.
- **Killer discriminator:** randomize/measure controlled placement states while holding the gait task as stable as practicable; validate that a proposed quality/state signal tracks the placement perturbation and reduces false alerts.

## 4. Candidate golden novelty — current conservative formulation

> **Hypothesis candidate, not a novelty claim:** A longitudinal low-cost plantar-sensing system can improve the *validity of gait-change alerts* by explicitly estimating or detecting measurement-system state `S_t` (calibration/fit/loading-history/environment), separating it from the observed gait/force state, and abstaining when attribution is insufficient.

A suitable model begins as an accounting identity, not an asserted causal discovery:

`Y_observed(t) = h(G_t, S_t, E_t) + ε_t`

where `G_t` is gait/loading state, `S_t` is sensor/fit/history state, and `E_t` is environment/task context. The research burden is to make some parts identifiable with controlled interventions and reference measurements.

**Novelty fails** if a close paper already performs the same multi-session intervention design, sensor-state inference/quality control, held-out-session validation, and false-change outcome for comparable pressure insoles. The 20–30-paper matrix must test this explicitly.

## 5. Non-negotiable killer-experiment acceptance criteria

1. **Reference trace:** Force plate or traceable multi-axis/load reference for the claimed target; no substitution by model output.
2. **No-change control:** repeated standardized sessions where biological change is not expected; report false positive rate and confidence intervals.
3. **One-factor perturbations:** at minimum loading history/creep, temperature if plausible, fit/placement, footwear or task condition; log them rather than calling all variation drift.
4. **Session-held-out evaluation:** no shared session windows between train/tuning/test; use leave-session-out and, where possible, leave-person-out.
5. **Ablation:** raw pressure baseline; contact/IMU or simple calibration baseline; proposed state-aware method. ST-GNN is only a later comparator after linear/CNN/LSTM baselines.
6. **Decision outcome:** error alone is insufficient. Report false gait-change alerts, missed controlled changes, residual drift, calibration frequency/burden, uncertainty/abstention rate, and energy/latency if edge deployment is claimed.

## 6. Matrix execution plan

- Populate **20–30 papers** in four passes: (A) sensor/metrology + calibration, (B) GRF/COP estimation, (C) domain/cross-session/personal adaptation, (D) longitudinal and clinical endpoint validity.
- Read **Limitations/Discussion/Future Work/Methods/Dataset** before ranking a card; abstracts only mark a candidate as `PARTIAL`.
- For each paper, record one direct quote or faithful anchored observation, its failure mechanism, who addresses it next, and what exact experiment remains.
- Rank only cards with traceable sources using the owner’s eight axes: importance, novelty, depth, measurability, ground truth, feasibility, ISEF impact, ceiling. A score is a decision aid, not evidence.

## 7. First 20-paper gap matrix checkpoint

The first matrix is now stored as `research/reviews/2026-08-25_golden_novelty_gap_matrix.csv`.

- **16 cards** have a source already read to the declared scope in `SOURCE_LEDGER.csv`; some are full-text primary sources, one is a preprint, and one is a review. They are evidence for their stated scope only.
- **4 cards** are explicitly `ABSTRACT_ONLY`/`SEARCH_EXCERPT` candidates. They cannot support a novelty conclusion until their bibliographic identity and relevant full text are verified.
- The matrix already defeats several weak framings: generic 3D-GRF regression, contact/IMU fusion to reduce raw-pressure dependence, generic sensor correction, and generic longitudinal monitoring.
- The strongest surviving *question* is not yet a confirmed gap: **whether a pressure-insole system can estimate or flag measurement-system state and thereby reduce false longitudinal gait-change alerts under controlled fit/calibration/loading-history/context shifts.**

## 8. Immediate search set

`"smart insole" drift`; `"plantar pressure" hysteresis`; `"pressure sensor" long-term drift`; `"smart insole" recalibration`; `"GRF estimation" cross-session`; `"GRF estimation" inter-subject`; `"plantar pressure" domain adaptation`; `"COP" calibration`; `"COP" longitudinal`; `"wearable biomechanics" reliability`; `"wearable GRF" generalization`; `"smart insole" real-world validation`.
