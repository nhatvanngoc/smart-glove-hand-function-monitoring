# Gap scan: groups 2, 4, 5, 7 + Devil's Advocate review

- **Date:** 2026-08-25
- **Status:** initial, non-exhaustive evidence scan; not a systematic-review conclusion.
- **Review mode:** **sequential role review; not independent multi-agent verification.** This environment did not dispatch isolated reviewers/models.
- **Scope:** prior art relevant to (2) 3D-GRF, (4) pressure-sensor drift/hysteresis, (5) cross-session generalization/calibration, and (7) longitudinal gait monitoring.
- **Out of scope:** a claim that any cited system diagnoses knee OA; any hardware or clinical result for this project; a final novelty decision.

## Frozen packet manifest

| Artifact | SHA-256 |
|---|---|
| `AGENTS.md` | `125c0531fd655f8c1f5d38623562c2c0553a4d2dbaf6345ec9d76468d98978fa` |
| `docs/01_Topic_Definition.md` | `8814ce83976e2bc7495e6e5eab5419abb95b50ef548416bc6cc7037315d6a78a` |
| `docs/03_Literature_Gap_Analysis_Plan.md` | `ebbb08a012226f53a6e10cf2d9e822873ec0ae05b9bcb692173f0f4ee246f074` |
| `research/claims/CLAIM_LEDGER.csv` | `a12cfd4b672c17adb95f6fbc4fd1133935052f652ce3f815f02f1bfb019c04d5` |
| `research/evidence/SOURCE_LEDGER.csv` | `fdd1d02ad15a6eb3dfb803fd55a20921fdd4d94ae8875de9055d84bb4f5c07bd` |
| `research/protocols/SMART_INSOLE_CRITIQUE_5_SEATS.md` | `6e08abe38ae9d7083b4c24ee58481bcdffc03d87941ec14ffd66f956960c5d9c` |

Search provenance is in `research/queries/QUERY_LOG.jsonl` (five records beginning `Q-20260825T054212Z`). Source identities, URLs/DOIs, access date, and exact read scope are in `research/evidence/SOURCE_LEDGER.csv`.

## 1. Evidence observations by group

### Group 2 — 3D-GRF estimation: **OVERLAP for generic premise**

- Zhang et al. (2025) describe a low-cost smart insole using CapSense plus IMU and a dual-stream attention model, trained with synchronized force-plate reference data, for 3D-GRF estimation; the paper reports a lowest NRMSE of 4.1% within its protocol (`SRC-ZHANG-2025-3DGRF`, abstract and Methods/Introduction).
- This is direct, close prior art against presenting “low-cost smart insole + ML/attention → 3D-GRF” as the central novelty.
- It does **not** establish equivalence to a Velostat-only matrix, nor longitudinal drift robustness, biology-vs-sensor separation, or a 30-day false-change endpoint.

**Implication:** novelty candidate “plain 3D-GRF regression” is already overlapped. The project must not claim it as new.

### Group 4 — drift/hysteresis: **OVERLAP for sensor limitation; method gap unresolved**

- de Fazio et al. use a Velostat piezoresistive sensing matrix and explicitly characterize response under loading/unloading and time behavior; their insole firmware includes a correction depending on the preceding pressure and elapsed time (`SRC-DEFAZIO-2021-VELOSTAT`, §3.1, §4.1, §4.4).
- Jung et al. (2026) report a piezoresistive insole module with initial drift and gradual stabilization under cyclic testing; this is a direct warning that drift-like behavior is not hypothetical (`SRC-JUNG-2026-PIEZO-SHEAR`, §4.2).
- Neither source, based on the read scope, validates a method that identifies whether a longitudinal change originates from biology, sensor behavior, or the environment.

**Implication:** “Velostat/piezoresistive sensors need characterization/correction” is not new. A defensible contribution must be a **measured residual-drift bound plus an identified separation protocol**, not merely applying a derivative or a generic correction.

### Group 5 — cross-session generalization/calibration: **UNRESOLVED**

- Rouse et al. compare wireless pressure insoles with force plates and assess test–retest reliability in two same-day sessions. Their abstract reports systematic differences: lower vGRF and shorter ML COP trajectories from insoles, even where repeatability was fair to excellent (`SRC-ROUSE-2023-INSOLE-RETEST`, abstract and test–retest methods).
- This establishes that reliability and agreement are distinct. It is not evidence of a multi-day drift correction, train-day-1/test-day-30 generalization, or a biology-vs-sensor causal separation.
- The targeted scans did not verify a close primary paper that jointly reports: pressure-insole 3D-GRF/COP, multi-session sensor/environment perturbations, and a false biological-change endpoint. **“Not verified in this scan” is not “does not exist.”**

**Implication:** E (biology-vs-sensor separation) remains a plausible **hypothesis**, not a confirmed gap. The protocol must deliberately create identifiable controls: repeated reference loading, temperature/footwear records, sensor replacement/repositioning conditions, and sessions designed with no expected biological change.

### Group 7 — longitudinal monitoring: **OVERLAP for high-level objective; device-specific contribution unresolved**

- A 2026 wearable study in Parkinson’s disease evaluates within-participant longitudinal changes, test–retest reliability, and comparison against a non-PD group over extended follow-up (`SRC-NPJPD-2026-LONGITUDINAL`, abstract). It shows the general idea “wearables can track longitudinal change” is established, though with wrist sensing and PD rather than pressure insoles and OA.
- A 2025 plantar-pressure study explicitly distinguishes intra- from inter-individual variation and discusses sensitivity to subsequent-session changes (`SRC-SCIREP-2025-INDIVIDUALITY`, abstract). It is not a sensor-drift decomposition study.

**Implication:** do not claim invention of longitudinal wearable gait monitoring or personal baselines. A contribution must be narrowed to the testable combination: low-cost plantar sensing + controlled sensor/environment characterization + validated false-change reduction against a kinetic reference.

## 2. Working novelty disposition (conservative)

| Candidate | Disposition | Why | Required before advancing |
|---|---|---|---|
| Generic smart-insole ML 3D-GRF | **OVERLAP** | Close 2025 force-plate-validated prior art exists (`SRC-ZHANG-2025-3DGRF`). | Reframe as baseline/benchmark, not novelty. |
| Generic drift compensation | **OVERLAP / insufficient alone** | Velostat history-based correction and piezoresistive drift characterization exist (`SRC-DEFAZIO-2021-VELOSTAT`; `SRC-JUNG-2026-PIEZO-SHEAR`). | Quantify residual drift on the project sensor and compare defined ablations. |
| Cross-session 3D-GRF/COP robustness | **UNRESOLVED** | Reliability work exists but is not the requested multi-session experiment. | Read a broader set of primary articles; preregister/define leave-session-out evaluation. |
| Longitudinal gait-change monitoring | **OVERLAP at high level** | Longitudinal wearable endpoints exist (`SRC-NPJPD-2026-LONGITUDINAL`). | Avoid broad claim; establish a device-specific, measurable contribution. |
| E: biology-vs-sensor/environment separation | **UNRESOLVED (candidate only)** | No source in the current bounded scan verified this exact combination. | Demonstrate identifiability with controls and force-plate/repeated-reference evidence. |

## 3. G5 — Devil's Advocate

```text
review_id: REV-2026-08-25-G5-INITIAL
role: G5 Devil's Advocate / frame challenger
reviewer/model/session identifier: Arena sequential role review
packet_manifest_sha256: generated from file hashes below
read_scope: named project artifacts + named full/partial primary texts recorded in SOURCE_LEDGER
verdict: BLOCK
confidence: high for current blockers; medium for literature-completeness conclusions
```

### Findings

| ID | Severity | Exact claim/location | Attack or failure mode | Evidence path | Evidence that would resolve it / required action | Gate |
|---|---|---|---|---|---|---|
| DA-01 | **BLOCKER** | `CLM-GT-001`; `DEC-INSOLE-006` | Without a force plate or a traceable multi-axis reference, Fx/Fy/Fz and COP cannot be validated. A pressure map does not make Fx/Fy ground truth appear. | Owner decision `SRC-OWNER-2026-08-25B`; close 3D-GRF prior art uses synchronized force plates (`SRC-ZHANG-2025-3DGRF`). | Secure access and synchronization plan for force plate/multi-axis reference; otherwise formally narrow project to quantities that can be supported. | G0/G2 |
| DA-02 | **BLOCKER** | `CLM-NOV-002`; topic novelty wording | The preferred E+D novelty is not demonstrated merely by observing a changed insole signal. Biology, fit, footwear, temperature, electrode wear, and sensor hysteresis are confounded; the current scan has **not** verified an identifying method. | `SRC-DEFAZIO-2021-VELOSTAT`; `SRC-JUNG-2026-PIEZO-SHEAR`; Group 5 disposition above. | Pre-specify perturbation/control design: fixed reference load before/after each session; repeated unchanged-condition sessions; deliberate sensor/environment perturbations; a biological-change proxy only after approvals; causal/measurement model and decision rule. | G1/G2 |
| DA-03 | **MAJOR** | Killer experiment in `docs/01`; `CLM-DRIFT-001` | “Corrected error stays constant” can be an artifact of recalibration, leakage, selective sessions, or changing task conditions. dP/dt can suppress slow offset yet amplify high-frequency noise and cannot by itself remove gain drift/hysteresis/creep. | `AGENTS.md`; `SRC-DEFAZIO-2021-VELOSTAT` records hysteresis/time correction. | Compare raw, dP/dt-only, calibration-only, and proposed full method using the same held-out **session**; report residual drift, uncertainty and false positives in a no-biological-change control. | G1/G2 |
| DA-04 | **MAJOR** | Generic 3D-GRF novelty in `CLM-NOV-001` | A 2025 low-cost insole + IMU + attention model with force-plate validation is a direct neighbor. Changing the sensor material or calling the model GNN is likely integration, not a scientific contribution. | `SRC-ZHANG-2025-3DGRF`. | Remove generic 3D-GRF novelty language; compare against simple linear/CNN/LSTM baselines and articulate a quantitatively distinct longitudinal endpoint. | G1/G2 |
| DA-05 | **MAJOR** | RQ 2 and knee-OA framing in `docs/01` | Longitudinal wearables in other conditions support feasibility, not OA inference. A pressure/GRF change is not an OA diagnosis or validated rehabilitation-response measure. | `SRC-NPJPD-2026-LONGITUDINAL` has PD/wrist scope; `CLM-BIO-002`; `CLM-ETH-001`. | Keep clinical language as “research measurement prototype/supports monitoring”; do not recruit/test people before IRB/SRC; make OA work conditional and out of current validation claim. | G3 |
| DA-06 | **MAJOR** | `DEC-INSOLE-001`; `CLM-HW-001` | The architecture is not locked: 16 ADC inputs versus desired cells/layout/multiplexing, sampling synchronization, NPU latency/power, and durability remain unmeasured. 6 TOPS is a vendor specification, not project evidence. | `DECISION_LOG.md`; `CLM-HW-001`. | Owner lock for layout/acquisition; bench timing/noise and power measurements; INT8 latency measurement on actual board; permit a smaller baseline model to win. | G0/G4 |
| DA-07 | **MINOR** | Group 5/7 literature conclusion | The scan is bounded and search-based. The absence of a verified exact paper is not proof of a gap. | Query log entries dated 2026-08-25; source limitations in ledger. | Continue groups 1/3/6/8/9/10 and database/full-text citation chasing before final novelty decision. | G1 |

### Unresolved questions

1. Which exact gold standard, axes, sampling rate, synchronization trigger and availability date will be used?
2. What single *identification experiment* distinguishes biological change from sensor/environment change rather than merely detecting a difference?
3. What change magnitude and false-positive definition constitute success, and how will the no-biological-change control be constructed?
4. Is a multi-session force-plate study feasible before the competition deadline? If not, what exact claim is removed?
5. What is the owner-approved cell layout and ADC/multiplexing strategy?

### Dissent / alternative frame

- **Alternative frame:** Treat the first publishable/science-fair contribution as an auditable **Velostat longitudinal metrology study**, not 3D-GRF AI: characterize each cell’s calibration, hysteresis, creep, temperature, placement, and session effects against a reference load; then test whether a correction reduces a pre-specified false-change outcome. Add 3D-GRF only after force-plate access.
- This is not a recommendation to abandon 3D-GRF; it is a risk-control route that can produce valid evidence even if force-plate access is delayed.

## 4. Adjudication (authoring-agent, not independent)

| Finding | Disposition | Rationale | Owner | Due gate | Residual risk |
|---|---|---|---|---|---|
| DA-01 | ACCEPT | Project itself designates this a hard validation blocker. | Project owner | G0 | No equipment commitment yet. |
| DA-02 | ACCEPT | Current evidence supports confounding risk; exact gap remains unresolved. | Research team + owner | G1/G2 | Requires experimental, not prose, resolution. |
| DA-03 | ACCEPT | Consistent with repository evidence rule and Velostat history dependence. | Research team | G2 | No residual-drift data yet. |
| DA-04 | ACCEPT | Close 2025 prior art defeats broad novelty framing. | Project owner | G1 | Exact model/sensor differentiation still needs full comparison table. |
| DA-05 | ACCEPT | Mandatory scope/safety guard. | Project owner + qualified IRB/SRC | G3 | OA work remains conditional. |
| DA-06 | ACCEPT | Unmeasured architecture facts cannot be assumed. | Project owner + engineering team | G0/G4 | Hardware design open. |
| DA-07 | ACCEPT | Prevents an absence-of-evidence claim. | Research team | G1 | Search remains incomplete. |

## 5. Immediate roadmap after this review

1. Owner answers the gold-standard and acquisition-layout decisions in `DECISION_LOG.md`.
2. Convert DA-02/03 into a preregisterable bench protocol with reference loading, temperature, cycle count, session schedule, residual-drift metric, and false-change endpoint.
3. Continue the remaining six literature groups and create the required prior-art comparison table before a final novelty decision.
4. Keep `CLM-NOV-002` **UNVERIFIED** and do not describe the system as drift-free, clinically validated, real-time, or ISEF-ready.
