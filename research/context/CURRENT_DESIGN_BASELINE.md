# Current design baseline — 2026-10-19 (owner update)

> **Authority:** owner direction recorded as `DEC-REHAB-001` and prior technical decisions in `DECISION_LOG.md`. This is the current project direction, not evidence that the prototype, threshold logic, vision model, home use, safety, or clinical benefit has been validated. The working title remains provisional; submitted/history files are unchanged.

## Project purpose and intended function

- The project is directed toward a hand rehabilitation glove for **fine-motor practice for middle-aged people after stroke**, with **home practice** as the intended use context. The user population and home setting are design targets; no patient testing or validated home-use claim is in scope yet.
- The intended training progression is: **(1) machine-assisted finger flexion/extension when the user cannot initiate the motion; (2) automatic transition to assist-as-needed (AAN) when predeclared sensor/performance thresholds indicate sufficiently stable voluntary movement; (3) task-oriented coordinated three-digit grasp practice.** No therapist/KTV action is required as the operating switch. Threshold features, values, observation window, repetitions, hysteresis and safe fallback remain OPEN and must be derived and fixed before testing, not invented after seeing outcomes.
- The first concrete functional task is to **grasp a spoon with the thumb, index and middle fingers, lift it, move it, and place it at a defined target**. The exact target, spoon geometry, grasp form and task protocol remain to be fixed. Additional objects/tasks are future expansion, not current acceptance criteria.
- The camera's primary function is to localize the spoon and target, track task progress and determine visible completion/placement, then provide immediate visual feedback to the user. It is not a clinical assessor and must not be treated as a force sensor. A fixed camera and known task scene are the initial design assumption; depth estimation is optional unless the task requires metric 3D coordinates.
- Orange Pi 5 Pro is intended to host computer vision for spoon/target localization and task-state tracking; a monocular depth model such as Depth Anything may be evaluated if depth is useful. Metric coordinates require camera/scene calibration and a scale reference. The ESP32-S3/MUX acquisition and low-level bounded actuation/state-machine split is a proposed architecture to verify, not a confirmed implementation. Benchmark the complete pipeline; hardware capability alone does not establish model accuracy, frame rate, metric depth, latency or reliability. RL is not part of the adopted scope.

## Sensor roles and signal interpretation

- **Flex sensor:** estimate finger bend/posture and movement progression. It does not measure contact force.
- **Velostat:** measure local pressure/contact-related changes at designed dorsal/palmar sensing locations; use the resulting signal as a relative indicator of contact/effort in the task. It does not directly identify semantic intent, joint angle, or absolute force in Newtons. Intent/action state is inferred by the controller from signal patterns and context, not read directly from Velostat.
- **Camera:** provide object/target position and task outcome context. It cannot establish finger force or clinical recovery.
- The sensing/brace scope remains thumb, index and middle finger. Owner clarification: use **three Flex sensors, one per digit** (thumb, index and middle). The current electronics target is one CD74HC4067 / 16 analog channels. If all three Flex sensors share this mux, reserve three channels and at most 13 remain for Velostat and any reference channels. The final map, Velostat count and whether any sensor uses a separate ADC/input remain OPEN; do not treat 13 as a confirmed number of Velostat elements.
- Test Velostat on the assembled glove to verify the signal is caused by the intended finger/object interaction rather than mainly finger-to-splint pressure. Do not convert its output to Newtons or use it as an independent safety-force reference.

## Automatic progression and AAN controller

- Operating state progression is intended to be automatic: assisted flexion/extension → threshold-qualified transition → AAN → task-oriented grasp practice. An explicit KTV/therapist mode switch is not a required function.
- The transition and AAN trigger must use deterministic, predeclared rules based on calibrated signal features (likely flexion movement/consistency plus Velostat activity/contact evidence). Exact features and thresholds are **OPEN**. Establish them on bench/phantom and pre-register them before any evaluation; include hysteresis, invalid-signal handling, stop/release behavior and a safe fallback state.
- AAN means the user initiates or attempts movement and the mechanism supplies bounded assistance when the movement is insufficient. Camera may gate task phase and confirm outcome; it must not directly command an unbounded pull. Any physical force limits require an independent calibrated measurement method and responsible safety review.
- **Mechanism:** servo winds fishing line directly onto a spool/drum. No spring/SEA or four-bar linkage. Spool, line routing/anchor, return/release path, actuator mapping, independent tension measurement and safe flexion/extension behavior remain open. A pull-only spool does not by itself establish powered extension; the return mechanism must be designed and verified.
- Prior Newton-valued `F_assist=max(0,F_target−F_active)` and 5 N criterion remain withdrawn.

## Scope, mass and cost

- Active hand-worn scope is three digits: thumb, index and middle. The exact Velostat/flex channel map and scan timing remain open.
- Hand-worn brace/sensor mass target: 80–120 g, excluding remote controller, battery and servo; weigh the finished assembly before reporting a result.
- Planning estimates remain separate: 1.0–1.3 million VND for wearable consumables; about 5.5 million VND end-to-end using reused lab equipment. These are estimates pending dated BOM/quotes, not audited actual costs. The former whole-system <1.5M VND and <150 g claims remain withdrawn.

## Evaluation, evidence and claim boundaries

- The immediate engineering outcomes are successful spoon pick-up/transfer/placement, task completion rate, time, drops/retries, finger-motion trace and assistance events/level, plus vision-state errors and automatic-transition behavior. These are task/system measures, not clinical scales.
- Visual success feedback can act as immediate task feedback/reward. It is not by itself evidence of neuroplasticity or improved recovery.
- The long-term goal is to support rehabilitation and improve functional recovery, but this project may not claim clinically meaningful recovery without an appropriately designed, approved longitudinal patient study. Coordinated three-finger practice as superior for neural recovery remains a hypothesis requiring evidence.
- Keep the project ambitious in intended function while distinguishing intended outcome from what bench/phantom or conditional healthy-volunteer testing can establish. No patient testing, validated home-use claim, clinical-effectiveness claim, novelty/“first” claim, or safety certification is currently in scope.
- Test bench/phantom first. A powered test on healthy adults is only a conditional future option after successful safety evaluation and all required approvals; no such test is authorized by this baseline.
- All numerical values in current proposal sections and technical goals are targets unless supported by traceable dated logs/artifacts. GAP is not a committed product metric until an independent angle method is selected and validated.

## Documents and precedence

- Current working proposal: `docs/DE_CUONG_A_B_C_DRAFT_2026-10-19.md` (review draft, not submitted or final).
- Current operating scope: `docs/01_Topic_Definition.md`, this baseline, `DECISION_LOG.md`, and `research/protocols/09_AAN_spool_phantom_and_conditional_volunteer.md`.
- Proposed build/test order (thresholds and pass criteria still open): `research/context/IMPLEMENTATION_PIPELINE.md`.
- Preserve submitted/history documents unchanged. The local/Drive DOCX review copy remains stale relative to the current Markdown draft; do not silently replace the Drive source.