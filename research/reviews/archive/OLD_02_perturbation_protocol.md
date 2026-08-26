# 02 — Controlled measurement-perturbation protocol

- **Status:** preregistration-style draft. No human-participant data collection is authorized by this document. Bench/phantom/reference-load work is the initial phase. Any wearable testing involving other people requires applicable ISEF/affiliated-fair IRB/SRC pre-approval first.
- **Research question:** Can controlled measurement perturbations be used to estimate measurement integrity in a low-cost plantar sensing system, thereby reducing false longitudinal gait-change alerts without substantially increasing missed true changes?

## 1. Operational definitions

### 1.1 Measurement integrity (MI)

`MI` is not a self-reported neural-network confidence and is not a clinical state. It is an externally evaluated quality label/score describing agreement of a measurement under a stated protocol with its traceable reference.

For a target `z` (e.g., reference-load force, force-plate Fz/COP only after approval/equipment), define normalized error components on a locked reference set:

`e_force = normalized absolute target-force error`

`e_COP = normalized COP distance error`

`e_repeat = normalized repeatability deviation`

A provisional *reference-derived* integrity score may be specified before analysis as:

`MI_ref = clip(1 - (wF*e_force + wC*e_COP + wR*e_repeat), 0, 1)`

Weights, denominators, and pass threshold must be frozen from pilot/reference requirements before testing. If force plate/COP is unavailable, do **not** invent MI for 3D-GRF/COP; restrict `MI_ref` to the traceable bench target.

### 1.2 Decisions

| Ground condition | Integrity class | Correct decision |
|---|---|---|
| No induced gait change | acceptable | `NO_CHANGE` |
| No induced gait change | degraded | `ABSTAIN / SENSOR_CONTEXT_SUSPECT` |
| Controlled gait/task change | acceptable | `ALERT` |
| Controlled gait/task change | degraded | `ABSTAIN / cautious alert`, pre-specified before test |

“Biological unchanged” is a protocol label, not proof that a person’s biomechanics are identical. In the pre-approval bench phase it means **same reference loading program**.

## 2. Perturbation library

Run one factor at a time in the initial screening. Every test logs timestamp, hardware revision, cell layout, ADC configuration, sensor ID, operator, reference device, ambient temperature/humidity if available, and raw files.

| ID | Perturbation | Nominal / altered levels | Initial reference | Primary output |
|---|---|---|---|---|
| P1 | Placement / registration | nominal; ±5 mm AP/ML shift; defined rotation | fixed mechanical fixture + reference load; force plate only later | force/COP or pressure-map error vs reference |
| P2 | Loading history / creep | no preload; fixed repeated-cycle blocks; defined recovery intervals | load cell/test rig | error immediately and after recovery; drift slope |
| P3 | Calibration mismatch | static calibration → dynamic evaluation; low-load → high-load evaluation; task-matched control | load rig; force plate only later | calibration-transfer error |
| P4 | Footwear / interface | one nominal shoe/insole interface, then one altered stiffness/thickness condition | fixture/phantom first | change in reference agreement |
| P5 | Context / task | bench waveform rate/amplitude first; later controlled walk/stand only after approval | programmed loading waveform | condition-transfer error |
| P6 | Acquisition | locked sampling/scan setting, then one reduced rate or multiplexing configuration | synchronized load waveform | temporal alignment/peak error |

Do not add temperature, humidity, participant gait, multiple shoe types, and all perturbations at once. Add a factor only after the preceding factor has a reproducible effect or has been documented as null.

## 3. Phase A — bench metrology (first permitted phase)

1. **Sensor identity and baseline:** assign immutable sensor/cell IDs; photograph layout; record electrode materials, dimensions, conditioning circuit, ADC reference, scan order, and firmware hash.
2. **Reference load program:** use a traceable/characterized load cell or materials-test fixture. Run ascending/descending loads, repeats, constant holds, and cycle blocks. Preserve raw reference and ADC timestamps.
3. **Crosstalk and spatial registration:** load a known region; quantify response of non-target cells. Repeat at P1 placements with a fixture.
4. **History experiment:** run P2 with predeclared cycle count, load, rate, rest and recovery times. Compare a common check-load response before/after each block.
5. **Calibration-transfer experiment:** fit calibration only on the declared calibration condition. Evaluate it without refitting on P3 conditions.
6. **Screening rule:** a perturbation advances only if its reference-derived degradation has a confidence interval excluding the nominal repeatability/noise bound. Otherwise document it as a null/insufficient perturbation.

## 4. Phase B — force-plate validation (only when reference access and participant approvals exist)

- Synchronize insole, force plate and any IMU with a documented common trigger or measurable synchronization procedure.
- Reference target scope must be explicit: Fz/COP first unless the force plate and coordinate conventions support Fx/Fy claims.
- Use session IDs and predeclare session separation. Do not split windows randomly across train/test.
- For a no-change control, retain task, footwear, participant, pace and setup as stable as practicable while altering **only** the authorized measurement perturbation.

## 5. Dataset schema

```text
record_id, sensor_unit_id, firmware_hash, session_id, participant_id_or_bench_id,
reference_device_id, reference_timestamp, raw_pressure_sequence, raw_imu_sequence,
reference_force, reference_COP, task_label, nominal_or_controlled_gait_change,
placement_condition, loading_history_condition, calibration_condition,
footwear_interface_condition, acquisition_condition, environment_log,
MI_reference_label_or_score, leakage_partition
```

Participant identifiers must never enter tracked files. Use coded IDs, maintain any mapping privately and only after required approval.

## 6. Data split and baseline lock

- **Test partition:** leave-session-out is mandatory. If feasible, use leave-person-and-session-out as an external generalization test.
- **Model order:** threshold/statistical → linear/logistic → MLP → 1D-CNN → LSTM/GRU → proposed model. ST-GNN is only considered after these baselines.
- **Required comparisons:** raw calibrated pressure; ordinary recalibration; contact/IMU baseline when IMU exists; proposed MI-aware decision layer.

## 7. Primary/secondary endpoints

- **Primary:** false longitudinal gait-change alert rate in no-change + degraded-MI conditions.
- **Secondary:** missed controlled-change rate, sensitivity, specificity, cross-session target error, MI score/label performance, abstention rate, coverage, selective risk, calibration time and (if claimed) measured edge latency/power.

`coverage = non-abstained decisions / all eligible cases`

`selective risk = errors among non-abstained decisions / non-abstained decisions`

Report coverage–risk curves. An abstaining system does not pass merely by lowering alerts at trivial coverage.
