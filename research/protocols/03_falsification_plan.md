# 03 — Falsification plan for measurement-integrity-aware longitudinal gait monitoring

- **Status:** pre-experiment decision rule. The plan exists to make negative results actionable, not to guarantee project success.

## Hypothesis

Controlled measurement perturbations can support a measurement-integrity decision layer that reduces false longitudinal gait-change alerts compared with specified simpler baselines **without an unacceptable loss of true-change detection or coverage**.

## GO / NO-GO gates

### Gate 1 — Literature kill test

**GO only if:** completion of `01_prior_art_matrix.md` finds no close source with the full equivalent combination: perturbations + explicit state/quality estimate + longitudinal held-out-session evaluation + false-change decision endpoint + abstention/coverage, in a comparable plantar-sensing setting.

**NO-GO / REFRAME if:** a close source already demonstrates it. Record source, state exactly which contribution is occupied, and return to the remaining Gap Cards; do not differentiate by hardware branding or model name alone.

### Gate 2 — Bench perturbation viability

**GO only if:** at least two pre-specified perturbation families generate reproducible reference-derived degradation larger than nominal repeatability/noise, while the bench reference program is stable.

**NO-GO / NARROW if:** perturbations are smaller than noise, effects are irreproducible, or the reference is not reliable enough. Narrow to sensor-metrology characterization or change the perturbation library; do not train an attribution model on unidentifiable labels.

### Gate 3 — Baseline problem existence

**GO only if:** on held-out sessions, at least one simple baseline produces nonzero false-change alerts under a no-gait-change/degraded-measurement condition, and the test labels are auditable.

**NO-GO / REFRAME if:** raw pressure or ordinary recalibration already controls false alerts at the required coverage. The proposed framework has no demonstrated problem to solve.

### Gate 4 — Proposed method benefit

**GO only if:** the proposed method improves the primary endpoint against locked baselines at comparable coverage, with confidence intervals; it must not simply abstain nearly everywhere.

**NO-GO if any occur:**

1. False alerts do not decrease relative to a simple baseline.
2. False alerts decrease only because missed true changes rise beyond the pre-specified acceptable bound.
3. False alerts decrease only at unusably low coverage.
4. MI labels/predictions do not generalize to held-out sessions or unseen perturbation instances.
5. Benefit exists only when samples from the same session leaked into training/tuning.
6. Claimed 3D-GRF/COP benefit lacks appropriate force-plate/reference validation.

## Pre-specified anti-gaming checks

| Risk | Required check |
|---|---|
| Abstain-all solution | coverage–risk curve; report all eligible cases and an owner-approved minimum coverage before evaluation |
| Threshold fishing | freeze all decision thresholds using development sessions only |
| Leakage | partition by session before feature normalization/tuning; audit IDs in every fold |
| Reference contamination | reference targets never used as deployment inputs; MI reference score may label training/evaluation only |
| Post-hoc perturbation selection | retain all screened perturbations and report null effects |
| Metric substitution | report primary false-alert rate even if a secondary metric looks better |
| Clinical overclaim | label results as measurement/protocol validation, not OA diagnosis/treatment evidence |

## Required result table

| Method | Session-held-out false-alert rate | Missed true-change rate | Coverage | Selective risk | Cross-session error | Notes |
|---|---:|---:|---:|---:|---:|---|
| Raw pressure | | | | | | |
| Ordinary recalibration | | | | | | |
| Contact/IMU baseline | | | | | | N/A if no IMU |
| Proposed MI-aware system | | | | | | |

## Decision language after testing

- **Supported within tested conditions:** only if Gates 1–4 pass.
- **Not supported:** if any NO-GO condition triggers; preserve the result and update the claim ledger.
- **Unresolved:** if force-plate/reference, approvals, or adequate data are unavailable. Do not replace missing evidence with simulation or a model architecture claim.
