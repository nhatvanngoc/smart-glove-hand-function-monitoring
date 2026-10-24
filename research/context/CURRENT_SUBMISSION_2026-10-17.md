# Current school-submission source and active revision status

## Final owner proposal — 2026-10-23

**The owner has closed proposal drafting and supplied `LV1_11A2_12A1 ky.signed.pdf` as final.** Use this attachment as the current proposal source; the older Drive DOCX and agent exports below are historical, not mirrors. The current work is component/material selection and prototype packaging. Do not rewrite or re-export the final PDF without a new request.

- Cover title: **Găng tay hỗ trợ phục hồi chức năng vận động tinh bàn tay sau đột quỵ**.
- Source attachment: `/tmp/arena-coding-uploads/LV1_11A2_12A1 ky.signed.pdf`.
- Byte-identical workspace copy (Git-ignored): `research/downloads/2026-10-23/LV1_11A2_12A1_final_68546f5a1078.pdf`.
- **1,467,835 bytes; 17 PDF pages; SHA-256 `68546f5a1078b64875fd786a28ae8a3cb3f53b74b0ef34752c1a12102a501815`**. PDF metadata records creation on 2026-10-22. The filename contains “signed”; cryptographic signature validity has not been assessed.
- The final text specifies **16 on-finger Velostat cells + 2 unloaded references + 3 Flex = 21 sensor channels**, 2 CD74HC4067 and ADS1115; 3 independent servos/spools, Bowden routing and a dorsal elastic-return splint are now described. These are the final document's design statements, not evidence of complete construction or passing tests. Older “11-channel” and blanket “no elastic return” notes do not describe this final text.
- Owner's current procurement statement: **Flex sensors and the camera module are the two remaining main purchases**. ADS1115 was already confirmed available in the conversation. Exact servo/battery/power-board models, cable routing and camera mounting are still needed for packaging decisions.
- A battery/electronics box on a waist belt, with sensors and servos on the arm/hand, is a **new proposal for discussion**, not an adopted placement. Keeping a small MUX/ADC/MCU module near the sensors is an agent alternative, also unadopted.
- The signed/final proposal is not authorization for powered human tests. Existing safety review and approval requirements remain applicable.
- Recorded as `DEC-PROP-020` and `SRC-OWNER-FINAL-2026-10-23`. No firmware or vision implementation starts automatically from this intake.

## Previous owner working source — 2026-10-21 (historical)


**Historical working copy: [DE_CUONG_NOP_TRUONG.docx](https://docs.google.com/document/d/1VgzlaKYlQj55yCP45YoJ2KSRm10LV9m3/edit) was the proposal and primary writing-style sample before the final PDF above.** The owner explicitly identified this as the latest file after personally revising its wording. This supersedes the agent's core v3 (`1jd22OBFOiyv2Fvd3au_cWn2HT8wl4WfQ`) as the starting point for future edits; it does not establish that the document was formally submitted.

- Drive file ID: `1VgzlaKYlQj55yCP45YoJ2KSRm10LV9m3`; parent `102Ua4MQn-zwVSscCZIdRWvJaeFZh6YaL`.
- MIME: stored DOCX; size **1,654,271 bytes**; modified **2026-10-21T09:31:56.509Z** (16:31:56, UTC+7); Drive MD5 **c8ade1c15d9a5d9f7cbc2cd53fc25ba7**. Metadata unchanged on a second read.
- Text read through the Drive connector. Layout/images/page count have not been verified and no byte-identical local mirror was created.
- Structure observed: A has 5 sections, including biomedical theory at A.2; B uses I–III and mechanisms 3.2.1–3.2.6; C is **Kế hoạch chế tạo và thử nghiệm**, 7 sections. Preserve this owner structure instead of restoring v3's C.8/C.9, cross-reference table or image-request appendix.
- Read-only intake. No Drive edits/comments/uploads authorized by this handoff; do not overwrite the owner's file or silently treat a local Markdown as its mirror. Do not replace the historical `docs/DE_CUONG_NOP_TRUONG.md` merely because its basename resembles this file.
- The new draft contains a separate Flex/Velostat DSP design, a single-segment Velostat construction statement and renumbered references. Record these as content differences; do not promote thresholds or claims of validation solely because the prose has changed.
- Decision `DEC-PROP-019`; source `SRC-OWNER-PROPOSAL-2026-10-21`; intake/style observations: [`2026-10-21_owner_draft_intake.md`](../reviews/2026-10-21_owner_draft_intake.md).

## Historical provenance and directions through 2026-10-20

The following notes are retained for history. They are not the latest working-copy pointer; use the owner file above. Technical evidence and unresolved safety/design questions remain governed by their dated records.

### Earlier source provenance

- The user-designated 12-page Drive PDF [`11A2.pdf`](https://drive.google.com/file/d/1uJDGpTx_sR1P1VCsHM1fv6hrnCzMgDaJ/view?usp=sharing), file ID `1uJDGpTx_sR1P1VCsHM1fv6hrnCzMgDaJ`, is the latest supplied proposal as of 2026-10-19. It was reviewed read-only and has not been edited or replaced.
- The earlier source `11A2.docx` (Drive ID `1VbI9CRPWsx7q0o54h7lAQ4bWq9nz50PO`) was read-only intake on 2026-10-17. The local extraction is generated/ignored and not a faithful layout copy.
- The separate Drive review copy `11A2_CAP_NHAT_DU_THAO_2026-10-19.docx` (ID `1YXvVbi53CPcrzXaJQAPZTQ3ugnsjhErd`) was typeset from an earlier Markdown draft. It is **stale relative to the latest active direction and must not be presented as current or final**. Do not edit/replace the Drive source without explicit approval.
- Submitted PDFs and prior school-submission files remain historical; do not silently rewrite them.

### Owner direction recorded on 2026-10-19 (historical)

Use `research/context/CURRENT_DESIGN_BASELINE.md` and `DEC-REHAB-001` as current authority:

- Working topic: a glove to support fine-motor rehabilitation after stroke, targeting middle-aged users and intended home practice. Home usability and clinical benefit are not established.
- Functional progression: machine-assisted finger flexion/extension when the user cannot complete the motion; **automatic threshold-based transition to AAN** once predefined movement criteria are met; then coordinated thumb/index/middle grasp, lift, transfer and placement of a spoon at a defined target. No KTV/therapist action is required for mode switching.
- Flex sensor supplies bend/posture information; Velostat supplies local pressure/contact-related relative evidence, not semantic intention, angle or absolute Newton force. Camera tracks spoon/target and task completion and provides immediate visual feedback. Orange Pi 5 Pro is the proposed vision-compute platform; no model, metric depth, speed or accuracy has been benchmarked. RL is not adopted.
- Owner has confirmed three Flex sensors, one per thumb/index/middle finger. The 16-channel/one-CD74HC4067 target must be remapped to include three Flex inputs and Velostat; if all share the MUX, at most 13 channels remain for Velostat/reference inputs. Exact positions, number of Velostat elements and acquisition timing remain open.
- Exact automatic thresholds, observation window, number of repetitions, hysteresis, fallback, task protocol, vision pipeline, independent force reference, spool return/release and mechanical ability to flex/extend remain open. Do not invent numerical values.
- Keep A/B/C + References format. No novelty/“first” claim, no patient testing, no clinical-effectiveness claim, and no validated home-use or safety claim. Bench/phantom first; any powered healthy-volunteer study remains conditional on safety review and required approvals.

### Repository drafts recorded before the owner handoff

- [`docs/DE_CUONG_A_B_C_DRAFT_2026-10-19.md`](../../docs/DE_CUONG_A_B_C_DRAFT_2026-10-19.md) has been revised to the new owner direction. It is an active review draft, not approved, submitted, or asserted to match the Drive PDF.
- The local Word review copy and its Drive counterpart were not edited in this update because they are historical review artifacts and the source remains under owner control. Build a fresh review DOCX only after the Markdown draft is reviewed and approved.
- **2026-10-19 (lượt tài liệu thứ hai, theo chỉ đạo "hoàn thiện đề cương rồi mới code"):** bản A/B/C được bổ sung §C.4 (bảng đăng ký trước chỉ số/ngưỡng — mọi ô ngưỡng để `OPEN`) và §C.5 (thứ tự triển khai công cụ), cùng liên kết tới bộ artifact Gate 0 mới: `research/protocols/10_gate0_task_state_sheet.md`, `10a_gate0_channel_map_and_acquisition_budget.md`, `10b_channel_map_proposed.csv`, `docs/07_Vision_TaskState_Architecture.md`, `docs/08_Software_Firmware_Roadmap.md`. Bản Markdown vẫn **chưa được duyệt**, nên **chưa dựng lại DOCX review** và **không** chỉnh sửa `11A2.pdf`/`11A2.docx`/`11A2_CAP_NHAT_DU_THAO_2026-10-19.docx` trên Drive. Sổ tay nhật ký nghiên cứu trên Drive được bổ sung bằng một tệp nhật ký mới có ngày 2026-10-19 (không ghi đè tệp sổ tay cũ); chủ dự án yêu cầu **chưa commit GitHub** trong lượt này.

### Evidence and open checks recorded on 2026-10-19

- No hardware, threshold-transition, camera, depth, end-to-end latency, task-success or human study was run as part of this scope update.
- The latest PDF's older force-in-Newton/5 N content, targets phrased as achieved results, and unverified RL/NPU claims do not carry forward.
- Current claim status and open work are in `research/claims/CLAIM_LEDGER.csv`, `research/context/CURRENT_DESIGN_BASELINE.md`, and protocol 09.