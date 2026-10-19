# Current school-submission source and active revision status

## Source provenance

- The user-designated 12-page Drive PDF [`11A2.pdf`](https://drive.google.com/file/d/1uJDGpTx_sR1P1VCsHM1fv6hrnCzMgDaJ/view?usp=sharing), file ID `1uJDGpTx_sR1P1VCsHM1fv6hrnCzMgDaJ`, is the latest supplied proposal as of 2026-10-19. It was reviewed read-only and has not been edited or replaced.
- The earlier source `11A2.docx` (Drive ID `1VbI9CRPWsx7q0o54h7lAQ4bWq9nz50PO`) was read-only intake on 2026-10-17. The local extraction is generated/ignored and not a faithful layout copy.
- The separate Drive review copy `11A2_CAP_NHAT_DU_THAO_2026-10-19.docx` (ID `1YXvVbi53CPcrzXaJQAPZTQ3ugnsjhErd`) was typeset from an earlier Markdown draft. It is **stale relative to the latest active direction and must not be presented as current or final**. Do not edit/replace the Drive source without explicit approval.
- Submitted PDFs and prior school-submission files remain historical; do not silently rewrite them.

## Current owner direction for the next proposal revision (2026-10-19)

Use `research/context/CURRENT_DESIGN_BASELINE.md` and `DEC-REHAB-001` as current authority:

- Working topic: a glove to support fine-motor rehabilitation after stroke, targeting middle-aged users and intended home practice. Home usability and clinical benefit are not established.
- Functional progression: machine-assisted finger flexion/extension when the user cannot complete the motion; **automatic threshold-based transition to AAN** once predefined movement criteria are met; then coordinated thumb/index/middle grasp, lift, transfer and placement of a spoon at a defined target. No KTV/therapist action is required for mode switching.
- Flex sensor supplies bend/posture information; Velostat supplies local pressure/contact-related relative evidence, not semantic intention, angle or absolute Newton force. Camera tracks spoon/target and task completion and provides immediate visual feedback. Orange Pi 5 Pro is the proposed vision-compute platform; no model, metric depth, speed or accuracy has been benchmarked. RL is not adopted.
- Owner has confirmed three Flex sensors, one per thumb/index/middle finger. The 16-channel/one-CD74HC4067 target must be remapped to include three Flex inputs and Velostat; if all share the MUX, at most 13 channels remain for Velostat/reference inputs. Exact positions, number of Velostat elements and acquisition timing remain open.
- Exact automatic thresholds, observation window, number of repetitions, hysteresis, fallback, task protocol, vision pipeline, independent force reference, spool return/release and mechanical ability to flex/extend remain open. Do not invent numerical values.
- Keep A/B/C + References format. No novelty/“first” claim, no patient testing, no clinical-effectiveness claim, and no validated home-use or safety claim. Bench/phantom first; any powered healthy-volunteer study remains conditional on safety review and required approvals.

## Active repository draft

- [`docs/DE_CUONG_A_B_C_DRAFT_2026-10-19.md`](../../docs/DE_CUONG_A_B_C_DRAFT_2026-10-19.md) has been revised to the new owner direction. It is an active review draft, not approved, submitted, or asserted to match the Drive PDF.
- The local Word review copy and its Drive counterpart were not edited in this update because they are historical review artifacts and the source remains under owner control. Build a fresh review DOCX only after the Markdown draft is reviewed and approved.

## Evidence and open checks

- No hardware, threshold-transition, camera, depth, end-to-end latency, task-success or human study was run as part of this scope update.
- The latest PDF's older force-in-Newton/5 N content, targets phrased as achieved results, and unverified RL/NPU claims do not carry forward.
- Current claim status and open work are in `research/claims/CLAIM_LEDGER.csv`, `research/context/CURRENT_DESIGN_BASELINE.md`, and protocol 09.