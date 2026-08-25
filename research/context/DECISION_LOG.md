# Decision log

Only an explicit project-owner or authorized review decision may close an architecture/safety item. Agents may propose but must not self-approve project-scope decisions.

| ID | Date | Decision | Authority | Status | Evidence / consequence |
|---|---|---|---|---|---|
| DEC-PROC-001 | 2026-08-16 | Pin third-party research/tooling by commit under `.tools/sources/`; do not vendor or source-build heavy dependencies by default. | repository setup task | IMPLEMENTED | `tools/research_sources.lock.json`; reproducible bootstrap |
| DEC-PROC-002 | 2026-08-16 | Store durable context, searches, claims and review dissent in tracked ledgers; keep private/raw/download/generated data ignored. | repository setup task | IMPLEMENTED | `research/`; `.gitignore`; `AGENTS.md` |
| DEC-PROC-003 | 2026-08-16 | Treat synthetic outputs as simulation only and require independent evidence before hardware/clinical language. | safety/evidence protocol | IMPLEMENTED | `AGENTS.md`; claim ledger |
| DEC-TOPIC-001 | 2026-08-25 | **Abandon "adaptive air cushion + AAC"; redirect to Smart Insole Edge-AI (3D-GRF & COP).** | project owner | IMPLEMENTED | supersedes old air-cushion decisions |
| DEC-TOPIC-002 | 2026-08-25 | **Refine topic:** novelty = longitudinal drift-robust kinetic monitoring (not GRF regression); no diagnosis/treatment claims; two-layer RQ; killer experiment (drift-correction ablation + false-change rate). | project owner | IMPLEMENTED | `docs/01_Topic_Definition.md`; `docs/02_Theoretical_Foundation.md` |
| DEC-TOPIC-003 | 2026-08-25 | **Delete all air-cushion/AAC old-topic files** (docs, cad, diagrams, simulation, pipeline, experiments, outputs, src, input baseline report). History retained in git. | project owner | IMPLEMENTED | commit deleting old-topic artifacts |
| DEC-INSOLE-001 | 2026-08-25 | Hardware baseline: Velostat sensing matrix + Arduino Mega (acquisition/scanning/sampling) + Orange Pi 5 Pro / RK3588 (edge GNN inference, INT8). | project owner | IMPLEMENTED (specs to verify) | NPU ~6 TOPS is manufacturer spec; must benchmark |
| DEC-INSOLE-002 | 2026-08-25 | Research hypothesis: dP/dt drift mitigation + ST-GNN anatomical foot graph to infer Fx/Fy from Fz. | project owner | PROPOSED (hypothesis) | Validate vs. baselines and force-plate gold standard first |
| DEC-INSOLE-003 | 2026-08-25 | Defer AAC/eye-tracking/pneumatic modules permanently for this topic. | project owner | IMPLEMENTED | old artifacts deleted per DEC-TOPIC-003 |
| DEC-INSOLE-004 | 2026-08-25 | Novelty candidates A–E; prioritize **E (biology-vs-sensor separation) + D (longitudinal change detection)**. GRF regression alone is insufficient. | project owner | PROPOSED | requires literature gap analysis before any novelty claim |
| DEC-INSOLE-005 | 2026-08-25 | Biomedical framing: support monitoring of motor-function change and rehab response only. Prohibited: diagnosis, treatment, replacing physician/X-ray/MRI/force plate, "GRF ⇒ OA". | project owner | IMPLEMENTED | `docs/01` section 2; `AGENTS.md` |
| DEC-INSOLE-006 | 2026-08-25 | Force plate (or multi-axis load cell) is the required gold standard for 3D-GRF/COP validation. | project owner | IMPLEMENTED (hard blocker if absent) | acquire/borrow force plate; else narrow scope to Fz+COP |
| DEC-INSOLE-007 | 2026-08-25 | Staged human research: (1) healthy/phantom/controlled loading → (2) force-plate validation → (3) gait patterns → (4) knee-OA cohort only with ethics + partners. | project owner | PROPOSED | reduces IRB risk vs. recruiting patients immediately |
| DEC-INSOLE-008 | 2026-08-25 | Do not rush hardware; run literature gap analysis 2025–2026 first (10 topic groups). | project owner | IMPLEMENTED | `docs/03_Literature_Gap_Analysis_Plan.md` |
| DEC-INSOLE-009 | 2026-08-25 | Lock the next-phase scientific hypothesis/RQ: whether controlled measurement perturbations can estimate measurement integrity in a low-cost plantar system and reduce false longitudinal gait-change alerts without substantial missed true changes. Require prior-art kill test, perturbation protocol, and falsification criteria before full model/system work. | project owner | IMPLEMENTED (candidate still unconfirmed) | `research/reviews/01_prior_art_matrix.md`; `research/protocols/02_perturbation_protocol.md`; `research/protocols/03_falsification_plan.md` |
| DEC-ETHICS-001 | OPEN | Determine human-participant route with affiliated fair/IRB before any recruitment or interaction. | qualified IRB/SRC | PENDING | human protocol must remain paused |

## Open decisions for the Smart Insole (owner response required)

```text
Gold-standard reference (force plate / multi-axis load cell):
Sensor cell count + electrode layout:
ADC/multiplexing strategy (>16 cells?):
ST-GNN only after baselines (linear/CNN/LSTM)? yes/no
Final novelty scope (after systematic gap analysis):
Human testing planned now? yes/no
```

## Superseded (kept for audit trail)

- DEC-ARCH-001..004, DEC-SCOPE-001 (2026-08-16, air-cushion architecture) — SUPERSEDED by DEC-TOPIC-001.
- DEC-INSOLE-002's original wording "triệt tiêu drift" — corrected: dP/dt only **attenuates** offset drift (see CLAIM-LEDGER CLM-DRIFT-001).
