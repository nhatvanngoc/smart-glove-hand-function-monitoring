# Decision log

Only an explicit project-owner or authorized review decision may close an architecture/safety item. Agents may propose but must not self-approve project-scope decisions.

| ID | Date | Decision | Authority | Status | Evidence / consequence |
|---|---|---|---|---|---|
| DEC-PROC-001 | 2026-08-16 | Pin third-party research/tooling by commit under `.tools/sources/`; do not vendor or source-build heavy dependencies by default. | repository setup task | IMPLEMENTED | `tools/research_sources.lock.json`; reproducible bootstrap |
| DEC-PROC-002 | 2026-08-16 | Store durable context, searches, claims and review dissent in tracked ledgers; keep private/raw/download/generated data ignored. | repository setup task | IMPLEMENTED | `research/`; `.gitignore`; `AGENTS.md` |
| DEC-PROC-003 | 2026-08-16 | Treat synthetic outputs as simulation only and require independent evidence before hardware/clinical language. | safety/evidence protocol | IMPLEMENTED | `AGENTS.md`; claim ledger |
| DEC-ARCH-001 | OPEN | Select final cell geometry: 8×4, 8×8/64, or 5×9/45. | project owner | PENDING | blocks architecture-wide edits and BOM claims |
| DEC-ARCH-002 | OPEN | Select edge computer: Jetson Orin Nano or Orange Pi 5 (and define software/runtime implications). | project owner | PENDING | blocks deployment and latency claims |
| DEC-ARCH-003 | OPEN | Confirm robot arm is removed or retained. | project owner | PENDING | blocks novelty, hardware, safety and eye-tracking protocol |
| DEC-ARCH-004 | OPEN | Confirm primary simulator and role of Gazebo versus SOFA. | project owner | PENDING | blocks reproducible simulation baseline |
| DEC-SCOPE-001 | OPEN | Lock a feasible ISEF MVP and explicitly defer nonessential modules. | project owner + mentor | PENDING | current full stack is over-scoped and lacks hardware validation |
| DEC-ETHICS-001 | OPEN | Determine human-participant route with affiliated fair/IRB before any recruitment or interaction. | qualified IRB/SRC | PENDING | human protocol must remain paused |

## Required owner response format

```text
Matrix:
Compute board:
Robot arm:
Primary simulator:
ISEF MVP (maximum 3 measured contributions):
Modules explicitly deferred:
Human testing planned now? yes/no
```
