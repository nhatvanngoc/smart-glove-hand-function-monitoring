# Novelty hunt — assistive-control directions (2026-08-26)

Owner supplied 5 "very worth hunting" directions (A–E) and 3 "worth digging" (F–H), plus a forbidden list (generic smart prosthesis / insole / fall / tremor / AAC / rehab monitoring / pressure-ulcer prediction). This file records the kill-test of A–E. F–H were not yet attacked.

## Kill-test (nearest prior art found)

| Dir | Direction | Nearest prior art | Verdict |
|---|---|---|---|
| A | Adaptive residual-control interface | `SRC-EDAN-2025-ASSISTIVE` (sEMG 3-DoF for amyotrophia), residual-movement classifier for tetraplegia (PMID 35235517), `SRC-ADAPTDECODER-2021-PROSTH` (adaptive decoder, no recalibration), myokinetic/IMES interfaces | OCCUPIED |
| B | Fatigue before control failure | `SRC-EMGEEG-2025-FATIGUE` (fatigue-adaptive fusion), `SRC-EMGNMES-2025-FATIGUE` (SVM fatigue + NMES on embedded), EMG-degradation reviews | OCCUPIED |
| C | Intent vs involuntary movement | `SRC-TREMOR-ORTHOSIS-2019` (tremor-band rejection), `SRC-MULTIMODAL-2014-INTENT` (RP+EMG AND-gate), intention-tremor review (still an open challenge but worked on) | OCCUPIED (open challenge) |
| D | Inability-to-execute detection | `SRC-MULTIMODAL-2014-INTENT` detects intention to trigger assist; not found as a standalone "intended-but-failed" detector | LEAST occupied — but needs EEG/EMG; risks becoming generic AAC |
| E | Minimum-assistance control | `SRC-MISC-2025-SHAREDCTRL` (minimal-intervention shared control), `SRC-LOSEY-2018-ARBITRATION` (minimal assist-as-needed, mAAN) | OCCUPIED (named paradigm) |

## Meta-finding (the important result)

Across **two** independent hunts (pressure-sensing applications; assistive-control directions) every **application-level** direction is occupied. The reason is structural: these are mature fields, so application-level "no system does X" almost never holds.

The one gap that recurs in *every* direction is **measurement/signal integrity under degradation**:
- assistive-control papers all report that EMG degrades (fatigue, electrode shift, sweat, involuntary contractions) and that this causes control failure, and they mitigate it with **adaptive decoders / online re-calibration / transfer learning** (`SRC-ADAPTDECODER-2021-PROSTH`, `SRC-EMGEEG-2025-FATIGUE`);
- the pressure-sensing papers all report drift / placement / calibration sensitivity.

None of them **diagnose the CAUSE** of the degradation (fatigue vs electrode shift vs involuntary movement vs loss of voluntary drive) and act differently per cause. That is the same measurement-integrity mechanism as the current candidate, now confirmed as the recurring cross-domain gap.

## The bind, stated plainly

- **Legible application-level novelty** ⇒ crowded (every application direction is occupied).
- **Uncrowded novelty** ⇒ mechanism-level (metrology / integrity), which the owner judged not ISEF-legible.

So no *application* swap clears the ≥80/100 bar under the constraints. The only surviving mechanism is cause-level signal-integrity diagnosis.

## Candidate that survives (for owner decision — not adopted)

> **An assistive control interface that diagnoses WHY the user's control signal degraded — fatigue vs electrode shift vs involuntary movement vs loss of voluntary drive — and adapts per cause, instead of blindly re-calibrating.**

- One sentence: yes. New mechanism: cause-level failure-mode diagnosis (existing systems only re-calibrate/adapt blindly). Legible hook: "the interface knows *why* you lost control."
- Needs a biosignal (EMG) to separate those causes → keeps the RK3588 Edge-AI, but **not** the Velostat pressure insole.
- Must still be kill-tested (the nearest prior art is `SRC-ADAPTDECODER-2021-PROSTH`, which adapts but does not diagnose cause).

## Decision required (DEC-INSOLE-013)

Either (1) adopt the cause-level signal-integrity direction and accept it moves from pressure-insole to EMG/biosignal + RK3588; or (2) relax a constraint (sensor type / no-reference / legibility bar). Directions F–H can still be attacked if the owner wants, but A–E show the application space is saturated.
