# Proposed implementation pipeline — rehabilitation glove (2026-10-19)

> **Status:** proposed execution plan, not a passed GATE or owner-approved numerical protocol. It translates `DEC-REHAB-001` into build/test order. No threshold, acceptance value or hardware result is invented here. Current scope authority remains `CURRENT_DESIGN_BASELINE.md`.

## 1. Functional endpoint

The system is intended to support fine-motor practice for a middle-aged person after stroke, with home practice as the design context (not validated home use). The concrete first task is: the user coordinates thumb, index and middle finger to grasp a spoon, lift it, move it, place it at a defined target, and release it.

Intended progression:

`assisted finger flexion/extension → automatically qualified AAN → three-digit spoon task → visible task feedback + traceable session record`

No therapist/KTV action is required for mode switching. The project must not claim patient recovery or clinical effectiveness from bench/phantom task performance.

## 2. Runtime signal-and-control pipeline (proposed)

```text
Three Flex sensors (one/digit) ─> bend/posture features ─┐
                                                ├─> synchronized state estimate
Velostat array ──> relative pressure/contact ───┤
                                                │
Camera ─> spoon/target location + task state ───┘
                         │
                         ├─> automatic mode supervisor
                         │     assisted flex/extend → threshold-qualified AAN
                         │
                         ├─> bounded AAN command to servo/spool
                         │
                         └─> task result → visual feedback + event log
```

- Flex measures bend/posture change; it does not measure finger force.
- Velostat measures local pressure/contact-related change; it does not directly identify semantic intent, angle or Newton force. The controller must infer an attempt/state from patterns and context.
- Camera estimates task/object state; it does not measure grip force. Its first role is to locate spoon and target, track visible progress and verify placement/release for immediate feedback.
- Vision/task state may authorize a task phase or flag uncertainty, but it must not directly command an unbounded cable pull. Low-level actuator limits, stop and release must be independent of camera inference.
- The automatic mode transition must not mistake machine-produced motion for voluntary movement. Establish a method to distinguish user-initiated participation from actuator-driven flexion before choosing thresholds. The method is OPEN; test the state logic on bench/phantom before any human consideration.
- A monocular depth model (e.g., Depth Anything) is an optional candidate only if the task needs depth. Metric coordinates require camera calibration and scene scale; first check whether a calibrated fixed-camera 2D task is sufficient.

## 3. Development and verification gates

### Gate 0 — freeze the first task and requirements

**Work:** Specify spoon dimensions/handle, grasp form, start/target zones, how the spoon is released, camera view, task success/failure/unknown labels, intended user interaction and home setup assumptions. Separate must-have functions from future expansion.

**Owner decision:** use three Flex sensors, one on each of the thumb, index and middle fingers. Draw the exact mounting/calibration points and the Velostat/Flex channel map. If all three Flex sensors use the same 16-channel CD74HC4067, reserve three channels, leaving at most 13 for Velostat and any reference inputs. The Velostat element count and any separate ADC inputs remain open; if the total does not fit, revise acquisition before building the full glove.

**Exit artifact:** one-page requirements/task-state sheet; channel map; diagram showing which finger each actuator and sensor affects. Values not yet measured are marked OPEN.

**Drafted 2026-10-19 (PROPOSED, awaiting owner approval — Gate 0 is NOT passed):** [`research/protocols/10_gate0_task_state_sheet.md`](../protocols/10_gate0_task_state_sheet.md) (task/spoon parameters, task-state labels `T_*`, mode supervisor states, five candidate methods to distinguish voluntary movement from actuator-produced movement, must-have vs future scope, digit↔sensor↔actuator diagram, OPEN register), [`10a_gate0_channel_map_and_acquisition_budget.md`](../protocols/10a_gate0_channel_map_and_acquisition_budget.md) (four channel-allocation options PA-1/PA-2/PA-3a/PA-3b, proposed CH0–CH15 map, mounting/calibration methods, scan-time budget labelled `[CALCULATION]`, sync/time base, eight pre-power hardware checks) and [`10b_channel_map_proposed.csv`](../protocols/10b_channel_map_proposed.csv). No numerical threshold, task parameter or channel count was filled in; every open slot names the evidence required to close it.

**Owner decisions 2026-10-20 (recorded, Gate 0 still NOT passed):** `DEC-CHMAP-001` ADOPTED = **PA-2** (3 Flex through the MUX + 6 Velostat palmar/dorsal + 2 reference cells = 11 scanned channels, 5 spare); `DEC-TASK-002` ADOPTED = **M3** (short assist-pause probe window) as the working method to separate voluntary movement from actuator-produced movement. Still OPEN: every task parameter (needs measuring the real spoon/zones → `DEC-TASK-001`), mounting positions, the Flex resistance range and divider resistor, the real frame rate/SPS/N (`DEC-ACQ-001`), the M3 window length and stop criteria plus its safety review, and the eight pre-power hardware checks. M3 is a method selection, not a validated rule.

### Gate 1 — sensor observability on a single finger / fixture

**Work:** Calibrate each of the three Flex sensors against an appropriate motion/angle reference on its actual mounted geometry and finger. Test each Velostat placement to determine whether it responds to finger-object interaction, finger-to-splint pressure, or both. Record repeatability, baseline drift, placement sensitivity and channel settling/scan timing.

**Exit criterion:** demonstrate that each signal is interpretable for its assigned job, or revise placement/role. Do not infer intent from a single Velostat channel or convert it to Newtons.

### Gate 2 — actuator and finger-mechanics feasibility

**Work:** On bench and hand phantom only, verify the direct servo-to-spool tendon route, flexion, slack take-up, release/return and extension. Determine whether the thumb, index and middle fingers can be driven together or independently enough for the selected spoon grasp. Use an independent tension/force reference for mechanical characterization and a reviewed stop/release procedure.

**Critical dependency:** a servo winding a cable in one direction does not establish active extension. If the selected mechanism cannot reliably release/extend or the three digits cannot form the intended grasp, revise the mechanical task/mechanism before vision-model work is allowed to define success.

**Owner decision 2026-10-20 (`DEC-MECH-007`):** **three separate spools** (one per thumb/index/middle) with **active servo cable release** for extension; no return spring/SEA and no four-bar linkage, consistent with the Giai đoạn 7 change. Rationale: the digits need independent travel to form the tripod grasp on a spoon handle. Still OPEN: one motor on a common shaft versus three motors; spool diameter, travel and safety limits; **unpowered release behaviour** (a mechanical question, not solvable in software); re-weighing the 80–120 g wearable cluster (`DEC-MASS-001`); updating the cost estimate (`DEC-COST-002`); and an independent force/tension reference. Nothing has been built, tested or safety-reviewed.

### Gate 3 — camera pipeline, prototype in parallel after Gate 0

**Work:** With a fixed camera, known spoon and target, detect/localize the spoon and target, identify visible task states (approach/contact if observable, lift, transfer, place/release, drop/unknown), and show immediate success/retry feedback. Implement the vision prototype on Orange Pi 5 Pro and measure end-to-end latency/accuracy on the actual camera and compute setup.

**Depth decision:** start with calibrated image-plane/object-target coordinates. Add depth estimation only if the chosen task needs it; calibrate scale before calling output metric 3D coordinates. Include occlusion and unknown-confidence handling.

**Drafted 2026-10-19 (PROPOSED — no code written, no benchmark run):** [`docs/07_Vision_TaskState_Architecture.md`](../../docs/07_Vision_TaskState_Architecture.md) specifies a pluggable-detector architecture (classic OpenCV adapter first, so it runs on Orange Pi 5 Pro without an NPU model; MediaPipe/YOLO/Depth-Anything as unadopted candidates), the detector output schema, the mapping from detector output to the `T_*` task-state labels, hysteresis and `UNKNOWN` rules, camera/scale calibration records, the Orange Pi ↔ ESP32-S3 message schema with the invariant that vision never commands an unbounded pull, and a benchmark sheet in which every accuracy/latency/frame-rate cell is `OPEN`.

**Exit artifact:** labeled test set and confusion/error table for the declared task states, latency measurement, camera calibration record, and fallback behavior. This is task recognition, not clinical assessment.

### Gate 4 — automatic progression and AAN state machine

**Work:** Define explicit states, valid transitions, signals, calibration procedure, mode-transition threshold(s), time/repetition window, hysteresis, confidence/invalid-signal handling, stop and return-to-safe-state behavior. Use Flex for movement progression and Velostat for relative pressure/effort/contact evidence; use vision for the task phase. Separate data used to tune thresholds from held-out evaluation data. Freeze rule/version before the comparison.

**Exit criterion:** on bench/phantom the system makes the intended transition reproducibly, rejects invalid/ambiguous signals, never treats machine-driven movement alone as voluntary progress, and safely stops/releases on faults under the predefined protocol. Numerical values must be justified and set before evaluation; none are assigned in this plan.

**Drafted 2026-10-19 (PROPOSED):** the state set (`SAFE_STOP/ASSIST/EVAL/AAN/TASK/INVALID/FAULT`), transition table and invariants are in [`research/protocols/10_gate0_task_state_sheet.md`](../protocols/10_gate0_task_state_sheet.md) §4; the five candidate methods (M1–M5) for separating voluntary effort from actuator-produced motion are in §5 — one must be selected and bench-verified before any feature/threshold is chosen. Implementation order, pre-registration and configuration-freeze rules are in [`docs/08_Software_Firmware_Roadmap.md`](../../docs/08_Software_Firmware_Roadmap.md) §1, §4 (F4) and §7. No threshold value exists yet and no code has been written.

### Gate 5 — integrated spoon-task verification

**Work:** Run the progression from assisted motion to automatic AAN, then spoon grasp/lift/transfer/place. Log raw sensor data, camera state/confidence, mode, threshold status, servo command, independent mechanical reference, task outcome and timestamps on a common clock.

**Task measures:** placement success, completion time, drops/retries, camera state errors, false/missed mode transitions, assistance events and stop/release events. These are engineering/task measures, not clinical recovery outcomes.

**Comparison:** use a fair baseline such as fixed assistance versus automatic AAN; test component contribution by removing one input only if the task can remain comparable and safe. Do not dress an untested sensor ablation up as a novelty claim.

### Gate 6 — conditional human pathway, not in this implementation pass

Bench/phantom testing comes first. A powered test with healthy adults may only be considered after a documented safety review and all permissions/approvals required by the responsible authorities, under a separate protocol. No patient testing or clinical-effectiveness inference is authorized by this plan. A later longitudinal study with stroke survivors would require a distinct approved design and appropriate clinical outcomes.

## 4. Recommended immediate work order

> **Trạng thái lượt tài liệu 2026-10-19:** mục 1 đã có bản đề xuất (`protocols/10`, `10a`, `10b` — chờ `DEC-TASK-001`, `DEC-CHMAP-001`, `DEC-ACQ-001`); mục 3 đã có đặc tả thiết kế (`docs/07`, chưa viết code); thứ tự code cho mục 4–5 nằm ở `docs/08` (F0–F6). Mục 2 là việc cơ khí phải làm trên fixture/phantom thật. **Trong lượt này không chạy code, firmware, benchmark hay phép thử phần cứng nào.** **2026-10-20:** chủ dự án duyệt `DEC-CHMAP-001` (PA-2), `DEC-TASK-002` (M3) và `DEC-MECH-007` (ba tang + servo nhả dây chủ động); chỉ đạo dựng lại DOCX review (`exports/11A2_CAP_NHAT_DU_THAO_2026-10-20.docx`). `DEC-TASK-001`, `DEC-VIS-001`, `DEC-IMPL-001/002`, `DEC-ACQ-001` **vẫn chờ**; **chưa viết code**.

1. Produce the Gate 0 task/state sheet and exact sensor/actuator map. The number of Flex sensors is now set at three, one per target digit; resolve their mounting points and the 16-channel budget.
2. Review the mechanical ability to flex, return/extend, release and coordinate the three fingers on a phantom. This is the highest-risk dependency for the spoon function.
3. In parallel, prototype fixed-camera spoon/target detection and visible task feedback on Orange Pi 5 Pro using the known scene; do not start with a broad object-recognition or RL project.
4. Characterize the mounted Flex/Velostat channels and determine how voluntary effort can be distinguished from actuator-produced movement.
5. Only after these three tracks are understood, freeze the deterministic automatic transition/AAN logic and run integrated bench/phantom comparisons.

## 5. Reporting rules

- This pipeline is a plan, not evidence that any gate passed.
- Do not invent a numerical threshold, safe force, model accuracy, depth error, latency or success rate.
- Do not claim improved recovery/neuroplasticity, validated home use, clinical benefit, safety certification, or novelty/“first” from a spoon-task prototype.
- Keep all raw logs, model/config versions, threshold versions and failed trials; report targets separately from measured results.
