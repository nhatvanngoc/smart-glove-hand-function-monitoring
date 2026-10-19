# Repo-wide scope synchronization — 2026-10-19

> **Historical sync with owner-update addendum:** Sections before “Owner update — rehabilitation function and automatic mode transition” record the prior camera-free candidate as it stood earlier on 2026-10-19. That candidate is superseded by `DEC-REHAB-001`; follow the addendum and current baseline for today's scope.

## Follow-up from latest Drive proposal

On 2026-10-19, the user designated a 12-page PDF, Drive ID `1uJDGpTx_sR1P1VCsHM1fv6hrnCzMgDaJ` ([link](https://drive.google.com/file/d/1uJDGpTx_sR1P1VCsHM1fv6hrnCzMgDaJ/view?usp=sharing)), as the latest proposal. It was read-only reviewed and not modified. New owner direction: three fingers (thumb/index/middle) on 16 channels; separate hand-worn mass (80–120 g target) from remote electronics/battery/servo; separate wearable consumables estimate (1.0–1.3M VND) from the ~5.5M VND E2E estimate using lab equipment; remove whole-system <1.5M and <150g thresholds. SEA was clarified as **not** selected: keep direct servo-to-spool winding without spring/SEA.

Orange Pi 5 Pro/RL remains unresolved. The generic fixed-vs-threshold-vs-RL phantom comparison was withdrawn as too incremental after owner feedback; the current candidate is a camera-free task-level three-finger grasp assistant, pending sensor-observability checks and prior-art review. The earlier review DOCX uploaded on 2026-10-19 is an older separate copy based on the prior Markdown draft, not the latest Drive PDF. The PDF still contains force-in-Newton/5 N content and unverified RL/NPU performance wording; these are not carried forward.

## Applied decisions

The current authority is `research/context/CURRENT_DESIGN_BASELINE.md`, recorded in `DECISION_LOG.md` as `DEC-SCOPE-007`, `DEC-AAN-002`, `DEC-METRIC-003`, `DEC-DEF-002`, `DEC-PROP-004`, `DEC-SCOPE-008`, `DEC-COST-002`, and `DEC-MASS-001`:

- AAN is the primary target; direct servo winding of fishing line onto a spool; no spring or four-bar linkage.
- Velostat/EI is relative effort signaling only; no Newton-valued `F_assist` formula and the prior 5 N criterion is withdrawn.
- Phantom first. Powered actuation on healthy volunteers is only a conditional future option after successful safety evaluation and all required approvals. No patient testing or clinical-effectiveness claim.
- Proposal values are targets unless traceable measurement artifacts support a result. GAP is open pending a valid angle method.
- A/B/C + References; no novelty/“first” claim; submitted and historical files remain unchanged.
- Three-finger scope (thumb/index/middle), 16-channel target, separate wearable/remote mass and cost. The cited mass/cost amounts are targets/estimates, not measurements.
- Orange Pi/RL is still a proposed direction requiring scope and protocol approval, not a result or deployed capability.

## Synchronized files

- `README.md`, `INDEX.md`, `AGENTS.md`, `research/context/PROJECT_SNAPSHOT.md`, `research/context/CURRENT_SUBMISSION_2026-10-17.md` — current operating state and precedence.
- `docs/01_Topic_Definition.md` — rewritten as current scope/design definition.
- `docs/02_Theoretical_Foundation.md`, `docs/04_Hardware_Architecture.md`, `docs/06_Co_Cau_Co_Khi_Exoskeleton.md` — supersession notices and corrections to force/signal interpretation.
- `docs/DE_CUONG_A_B_C_DRAFT_2026-10-19.md` — updated Markdown working draft reflecting the latest scope and estimates; its RL subsection is explicitly proposed/pending owner adoption. `docs/11A2_CAP_NHAT_DU_THAO_2026-10-19.docx` and its Drive copy are older review copies and do not include these latest Markdown changes.
- `docs/DE_CUONG_NOP_BAN_KHKT_2026-10-18.md`, `docs/DE_CUONG_NGAN_5-7_TRANG_DRAFT.md`, `docs/05_De_Cuong_Dang_Ky_DRAFT.md`, `docs/OUTLINE_BAOCAO_VISEFD.md`, and `docs/bao_cao/A1–A7` — marked superseded, retained for traceability.
- `docs/bao_cao/GLOSSARY.md`, `docs/03_Literature_Gap_Analysis_Plan.md`, `research/README.md`, `research/context/EQUIPMENT_AND_ACCESS.md`, and `research/claims/CLAIM_LEDGER.csv` — updated terminology, project-specific restrictions, supersession statuses, and next actions.
- `research/protocols/06_glove_hand_GATE_experiment.md` and `07_ral_phantom_and_ktv_interview.md` — old AAN methods/limits marked superseded; `09_AAN_spool_phantom_and_conditional_volunteer.md` provides the new staged planning scaffold without inventing thresholds.
- `research/reviews/2026-10-17_11A2_docx_audit.md` — addendum records the new decisions and points to the draft.

## Preserved / not changed

- Submitted `docs/DE_CUONG.pdf`, `docs/DE_CUONG_NOP_TRUONG.md`, dated notebooks, source records, and other historical logs were not rewritten.
- The source `11A2.docx` was downloaded read-only for drafting and then the temporary local intake copy was removed. The source file was not edited or replaced.
- Per the user's follow-up request, a **separate** review copy was uploaded to the same Drive folder: [`11A2_CAP_NHAT_DU_THAO_2026-10-19.docx`](https://docs.google.com/document/d/1YXvVbi53CPcrzXaJQAPZTQ3ugnsjhErd/edit?usp=drivesdk&ouid=106741378656708745689&rtpof=true&sd=true), ID `1YXvVbi53CPcrzXaJQAPZTQ3ugnsjhErd`. It was not converted to or substituted for the source.
- The new DOCX is a re-typeset text draft from the Markdown; old figures/graphics were not copied because their accuracy and relevance need owner review. It is a review draft, not a final submission.

## Open before any actuator test

The spool dimensions, fishing-line type/routing/anchors/return behavior, servo command mapping, independent tension measurement and calibration, mechanical release, hazard review, and predeclared stop/acceptance criteria remain undecided. There is no replacement force threshold in this sync. A separate approved protocol is needed before any powered test on a person. The GAP angle method and any updated RAL definition also remain open.

## Checks

- The initial 2026-10-19 sync passed `git diff --check`, the earlier 37-row claim-ledger validation, and DOCX ZIP integrity/extraction checks. Those DOCX checks applied to the previous Markdown version only.
- After the latest-PDF follow-up, the claim ledger contains 41 rows with unique IDs, including four additional records for three-digit scope, cost estimate, mass target, and proposed RL direction. `git diff --check` was rerun after this follow-up.
- No firmware/code behavior changed; no hardware tests or RL/Orange Pi benchmarks were run.

## Owner update — rehabilitation function and automatic mode transition (2026-10-19)

The camera-free task-level grasp candidate described above is superseded by the owner-approved functional direction `DEC-REHAB-001`. The new current direction is a progressive home-oriented fine-motor training glove for middle-aged people after stroke (home use remains an intended context, not validated): assisted finger flexion/extension when the user cannot complete the motion; automatic threshold-based transition to AAN when predeclared movement criteria are met; then coordinated thumb/index/middle grasp, lift, transfer and placement of a spoon at a defined target. A KTV/therapist is not required to operate the mode switch.

Functional sensor allocation: Flex sensor tracks finger bend/posture; Velostat records local pressure/contact-related relative changes and does not semantically identify intent, measure angle or give absolute Newton force; camera tracks spoon/target/task completion and provides visible feedback. Orange Pi 5 Pro is the planned computer-vision host, not a benchmarked capability. RL is not in adopted scope. The 16-channel CD74HC4067 target must be reallocated across both Flex and Velostat. Exact threshold features/values/windows/hysteresis/fallback, camera pipeline, spoon protocol, actuation return/extension and task outcomes remain open.

The active documents updated to this direction are `CURRENT_DESIGN_BASELINE.md`, `docs/01_Topic_Definition.md`, `README.md`, `INDEX.md`, the A/B/C working draft, and protocol 09. Source Drive files and historical/submitted proposal snapshots remain unchanged. No hardware, computer-vision, threshold-transition, phantom, volunteer, patient, or clinical-outcome test was run for this update. The prior review DOCX is stale and was not rebuilt or uploaded.

## Owner clarification — Flex sensor count (2026-10-19)

The owner confirmed **three Flex sensors, one per thumb/index/middle finger** (`DEC-SENSE-001`). If these share the 16:1 CD74HC4067, reserve three mux inputs and at most 13 remain for Velostat and/or reference channels. This does not set the number or placement of Velostat elements; exact channel allocation, mounting, calibration and scan timing remain open. The implementation pipeline and current baseline now reflect this count.
