# Decision log

Only an explicit project-owner or authorized review decision may close an architecture/safety item. Agents may propose but must not self-approve project-scope decisions.

| ID | Date | Decision | Authority | Status | Evidence / consequence |
|---|---|---|---|---|---|
| DEC-PROC-001 | 2026-08-16 | Pin third-party research/tooling by commit under `.tools/sources/`; do not vendor or source-build heavy dependencies by default. | repository setup task | IMPLEMENTED | `tools/research_sources.lock.json`; reproducible bootstrap |
| DEC-PROC-002 | 2026-08-16 | Store durable context, searches, claims and review dissent in tracked ledgers; keep private/raw/download/generated data ignored. | repository setup task | IMPLEMENTED | `research/`; `.gitignore`; `AGENTS.md` |
| DEC-PROC-003 | 2026-08-16 | Treat synthetic outputs as simulation only and require independent evidence before hardware/clinical language. | safety/evidence protocol | IMPLEMENTED | `AGENTS.md`; claim ledger |
| DEC-TOPIC-001 | 2026-08-25 | **Abandon "adaptive air cushion + AAC"; redirect to Smart Insole Edge-AI (3D-GRF & COP).** | project owner | IMPLEMENTED | `docs/30_TOPIC_PIVOT_Smart_Insole.md`; supersedes DEC-ARCH-001..004 and DEC-SCOPE-001 |
| DEC-INSOLE-001 | 2026-08-25 | Hardware baseline: Arduino Mega (16-channel ADC) for acquisition + Orange Pi 5 Pro (RK3588S, NPU ~6 TOPS) for edge inference. | project owner | IMPLEMENTED (specs to verify) | "6 TOPS" is manufacturer spec; must benchmark real latency/throughput/power |
| DEC-INSOLE-002 | 2026-08-25 | Research hypothesis: dP/dt drift mitigation + ST-GNN over an anatomical foot graph to infer Fx/Fy from Fz. | project owner | PROPOSED (hypothesis) | Must be validated vs. baselines and against a gold-standard reference before any claim |
| DEC-INSOLE-003 | 2026-08-25 | Defer AAC/eye-tracking/pneumatic modules; keep all air-cushion docs/CAD/simulation as historical archive, not merged. | project owner | IMPLEMENTED | `AGENTS.md` rule 2 |
| DEC-ARCH-001 | 2026-08-16 | Select final cell geometry: 8×4, 8×8/64, or 5×9/45. | project owner | SUPERSEDED | obsolete after DEC-TOPIC-001 |
| DEC-ARCH-002 | 2026-08-16 | Select edge computer: Jetson Orin Nano or Orange Pi 5. | project owner | SUPERSEDED | obsolete after DEC-TOPIC-001; Orange Pi 5 Pro chosen in DEC-INSOLE-001 |
| DEC-ARCH-003 | 2026-08-16 | Confirm robot arm is removed or retained. | project owner | SUPERSEDED | obsolete after DEC-TOPIC-001 |
| DEC-ARCH-004 | 2026-08-16 | Confirm primary simulator and role of Gazebo versus SOFA. | project owner | SUPERSEDED | obsolete after DEC-TOPIC-001 |
| DEC-SCOPE-001 | 2026-08-16 | Lock a feasible ISEF MVP and explicitly defer nonessential modules. | project owner + mentor | SUPERSEDED | re-opened as insole MVP below |
| DEC-ETHICS-001 | OPEN | Determine human-participant route with affiliated fair/IRB before any recruitment or interaction. | qualified IRB/SRC | PENDING | human protocol must remain paused; applies to the new insole topic too |

## Open decisions for the Smart Insole (owner response required)

```text
Gold-standard reference (force plate / multi-axis load cell):
Sensor cell count + electrode layout:
ADC/multiplexing strategy (>16 cells?):
ST-GNN only after baselines (linear/CNN/LSTM)? yes/no
Final novelty scope (after systematic review):
Human testing planned now? yes/no
```

## Required owner response format (legacy air-cushion items — now superseded)

```text
Matrix:
Compute board:
Robot arm:
Primary simulator:
ISEF MVP (maximum 3 measured contributions):
Modules explicitly deferred:
Human testing planned now? yes/no
```
