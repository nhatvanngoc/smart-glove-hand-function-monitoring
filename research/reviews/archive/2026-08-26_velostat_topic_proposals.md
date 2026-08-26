# Velostat-exploiting topic proposals (2026-08-26)

Owner directive: exploit Velostat (rare at ViSEF), find NEW high-potential topics, judge by the **ISEF rubric** (Research Problem 10 / Design 15 / Execution 20 / Creativity 20 / Presentation 35), not by the earlier PhD-level "≥80 novelty" bar. Prefer bench-feasible (no human/IRB/force-plate) so Execution can score high.

## Insight that generates the topics

Every existing Velostat project **hides** the material's weakness. The literature documents large, varied failure modes — accuracy 16–48% FSO, static drift ~1.17%/min, cyclic drift, hysteresis ~7.25% FSO, thermal swing up to 67%, crosstalk/"ghost", non-repeatability, and per-sensor calibration is "impractical for large arrays" (`SRC-HOPKINS-2020-VELOSTAT-SOCKET`, `SRC-MARTINEZ-2021-VELOSTAT-PSM`, `Polymers 2020`). Velostat also has one unique asset: it is **cheap** (≈$5/sheet), so redundancy is affordable.

**Nobody turns the weakness + cheapness into a capability.** That is the open intersection.

## Ranked proposals (ISEF-rubric estimates, conservative)

### #1 — Self-honest Velostat sensing skin (TOP)
- **One-liner:** a low-cost large-area pressure skin that **diagnoses its own failure modes** (thermal vs creep vs hysteresis vs crosstalk vs contact-loss), **corrects** them using the redundancy that cheap Velostat affords, and **flags** a reading instead of outputting a false pressure map.
- **Mechanism (new vs prior art):** existing arrays correct globally (creep/hysteresis compensation models, CoP algorithms) or just recalibrate; none identify *which* failure mode is active per cell using a few sacrificial reference cells + injected known perturbations. Velostat's cheapness is exactly what makes built-in redundancy feasible — a design no expensive-sensor system needs.
- **Why it fits ISEF:** Creativity = reframing weakness→capability (the "different perspective" ISEF names). Execution = fully bench-testable (inject heat / sustained load / partial contact / known weights; ground truth = weights + thermistor), no human, no force plate. Presentation = strong demo: "raw Velostat lies under heat/creep; the skin catches itself and corrects."
- **Est. ISEF:** Research 9 + Design 13 + Execution 18 + Creativity 17 + Presentation 30 ≈ **87/100**.
- **Nearest prior art to kill-test before commit:** self-calibrating/redundancy sensor arrays; temperature-compensated tactile arrays; the multi-frequency material+temperature retrieval idea seen in EIT-skin literature.

### #2 — Passive creep "dosimeter" (bolder, riskier)
- **One-liner:** a **battery-free** Velostat patch whose viscoelastic creep **records** sustained/peak pressure-exposure history, read out later — "a pressure memory with no power."
- **Mechanism:** exploit creep/settling as a cumulative record rather than fighting it.
- **Fit:** very high Creativity/legibility; Execution riskier (creep is noisy, hard to make repeatable). Best as a *sub-feature* of #1, or a standalone if bench calibration proves repeatable.
- **Est. ISEF:** ≈ 80/100 (Creativity high, Execution uncertain).

### #3 — Relative-change monitor (safer fallback)
- **One-liner:** because Velostat cannot give absolute force, use it only for what it is good at — **within-user relative change and asymmetry** (left/right, over-time) — and never claim absolute values.
- **Fit:** bench-feasible, honest about the material. But this drifts back toward the longitudinal-monitoring framing the owner found less legible, so it is the weakest hook.
- **Est. ISEF:** ≈ 82/100.

## Recommendation

**#1** is the best intersection of the two things that define Velostat (cheap + unreliable) and maps onto a single, demo-able mechanism that scores on Execution + Presentation (70% of ISEF) while being bench-feasible. **Next step before adopting: a focused kill-test of #1** (self-calibrating / redundancy-based / temperature-compensated tactile arrays) to confirm the cause-diagnosis mechanism is unoccupied.
