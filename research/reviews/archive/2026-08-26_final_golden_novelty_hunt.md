# Final golden-novelty hunt — terminal result (2026-08-26)

- **Mandate (owner):** FINAL bounded hunt, not infinite brainstorm. Problem-first (a human problem with a specific failure mode no embedded system solves), then check the platform. Keep Edge-AI + hardware (Velostat + Mega + RK3588). Swap the topic. Novelty must be a NEW MECHANISM stated in one sentence ("No system X can do Y under condition Z"), not "combine A+B+C". Target ViSEF → ISEF: novelty must be obvious in 1–2 minutes.
- **Rubric (owner):** 5 questions × 20 (1-sentence novelty / new mechanism / direct experiment / clear baseline / judge-understands-in-1-2-min). **< 80/100 → drop.**
- **Anti-hallucination:** every prior-art claim below is from a search-read source in `research/evidence/SOURCE_LEDGER.csv`; none are full-text verified yet, so "occupied" means "strong prior art found in bounded search", not "proven closed".

## Method

Problem-first scan of human-urgent failure modes reachable by a pressure-sensing platform, then a kill-test (nearest prior art) for each. Five spaces were attacked.

## Kill-test results

| # | Problem (human-urgent) | Failure mode | Nearest prior art found | Verdict |
|---|---|---|---|---|
| 1 | Prosthetic socket fit | Pistoning / high interface pressure → skin breakdown | `SRC-KWAK-2020-SOCKET` (pressure+temp at skin-socket), `SRC-SCIADV-2026-SOCKET-SHEAR` (normal+shear, closed-loop), closed-loop motorized socket (Wiley 2025), pistoning-alert patent | OCCUPIED |
| 2 | Pressure ulcer / wheelchair | Sustained pressure+shear → ischemia, no sensation | Smart Seat Cushion + ASSAM (closed-loop), multimodal pad + electro-therapy (MDPI 2021), `SRC-GAO-2015-IMPEDANCE-PU`, `npj 2025` skin-integrated, Orpyx (commercial) | OCCUPIED |
| 3 | Diabetic foot ulcer | Loss of protective sensation → harmful load unnoticed | TRIPS pressure+shear insole, LOMIS (shear+compression, 3-month), IDC smart footwear, ESP32 multimodal insole | OCCUPIED |
| 4 | Scoliosis brace | Corrective pressure drift / unknown optimal dose | `Cor-Esc-25`, FBG body-pressure knitwear, smart soft brace (textile), IEEE multimodal brace | OCCUPIED |
| 5 | Cast / compartment syndrome | Swelling under rigid cast → ischemia | `SRC-SENSEI-CAST` (8-sensor sleeve, real-time ACS alert) | OCCUPIED |

## The two genuine gaps that survive (and why they don't fit)

Independent sources converge on **two** real unmet needs. Neither is reachable as a clean swap under the current constraints:

1. **Surface pressure cannot see deep-tissue / internal state.** `SRC-GAO-2015-IMPEDANCE-PU` (surface pressure is an insufficient proxy; early damage needs impedance), `SRC-DTI-STRAIN-2026` (surface pressure misses deep-tissue strain; needs deformation-based assessment), `SRC-BONEFORCE-2020` (wearables do not estimate internal bone/tissue load). — A **Velostat pressure array cannot measure impedance, SpO2, or internal strain**, and the internal-load route needs force-plate/instrumented-treadmill ground truth. Not reachable with the current hardware and no-reference constraint.
2. **False alarms from measurement artifacts.** Documented across continuous wearable monitoring (vital-sign and gait reviews note artifact/contact-driven false alarms). — This is exactly the **measurement-integrity** candidate the owner judged not legible enough for ISEF.

## Rubric scoring (honest)

| Candidate | 1-sentence | New mechanism | Direct experiment | Baseline | Judge 1–2 min | Total | Pass (≥80)? |
|---|---:|---:|---:|---:|---:|---:|---|
| Measurement-integrity (current) | 12 | 14 | 16 | 15 | 10 | **67** | No |
| Socket pistoning alert | 18 | 8 | 16 | 16 | 18 | 76 | No (mechanism done) |
| Pressure-ulcer alert | 18 | 6 | 14 | 16 | 18 | 72 | No |
| Deep-tissue injury from pressure | 18 | 18 | 8 | 10 | 16 | 70 | No (unreachable + no ground truth) |
| Cast / compartment syndrome | 18 | 8 | 12 | 14 | 18 | 70 | No (occupied + clinical) |

Scores are provisional/conservative estimates, not measurements. **No candidate clears 80/100 under the full constraint set.**

## Terminal conclusion

Under the constraints **{human-urgent problem + reachable by pressure sensing + new mechanism + no force plate + ISEF-legible ≥80/100}**, this bounded hunt found **no problem-space swap that clears the bar.** The reason is structural: with a pressure array + Edge-AI fixed, every urgent human pressure-sensing application is already occupied, so novelty cannot come from the *problem* — it can only come from the *mechanism*, and the one defensible mechanism found across C21–C40 and this hunt is measurement-integrity (which fails only the legibility criterion).

**Therefore one constraint must give. Owner decision required (DEC-INSOLE-013):**

- **(A) Relax "no reference":** secure a force-plate / instrumented-treadmill / multi-axis load-cell collaborator. This unlocks the internal-load gap (`SRC-BONEFORCE-2020`) — a legible mechanism with novelty — and also revives the kinetic RQ. Highest-leverage if a collaborator exists.
- **(B) Relax the hardware platform:** allow non-pressure sensing (e.g., impedance/PPG). Opens the deep-tissue / cuffless-vitals unmet needs, but abandons the Velostat platform.
- **(C) Keep platform + accept the strongest surviving novelty (measurement-integrity) and engineer its legibility** into an obvious, demo-able mechanism (e.g., a self-test/"phantom" that injects a known failure and shows the device catching itself before it reports a false change). This is the only mechanism that survived every kill-test; the work is making a judge see it in 1 minute.

No topic was swapped in this turn; the decision is left to the owner.
