# Preliminary baseline intake review

**Date:** 2026-08-16  
**Scope:** full read of the 7-page baseline PDF and the 9 extracted notebook entries, plus a targeted consistency review of core repository documents.  
**Review type:** internal intake/red-team review, not an independent fair, clinical, IRB, or peer-review decision.

## Executive verdict

The project has a socially meaningful direction and several testable engineering components, but it is not yet possible to identify one authoritative system baseline. The documents represent at least three designs and mix proposal language, synthetic outputs and result-like PASS language. Before scientific refinement, the team must lock a feasible architecture and rebuild claim/source provenance.

**Current gate:** `BLOCKED FOR BASELINE LOCK`; `HUMAN TESTING PAUSED`.

## What the baseline artifacts actually establish

### Baseline PDF

The PDF is a seven-page proposal. It describes an 8×8/64-cell cushion, Jetson Orin Nano, stereo camera and 3-DOF robot arm. Its methodology/design sections are high-level. The “fabricated successfully”/results, conclusion and references sections are empty. Therefore it does not establish fabrication, measured performance, or literature support.

### Science notebook

The notebook is later on several points but sparse: initial 8×4 concept; a 2026-05-01 decision to remove the robot arm; a 2026-05-05 choice of Orange Pi 5 + STM32F4; and a 2026-05-10 note about a 1×1 cell simulation. It provides a change history, not enough implementation evidence to show that those changes were built or validated.

### Repository documents

Older documents (`docs/00`–`13`) substantially retain 8×8/64, Jetson and robot arm. Later documents (`docs/15`–`29`) use a 5×9/45-cell geometry and shift simulation attention to SOFA. `docs/19_Final_Matrix_Lock_5x9_50mm.md` is the clearest later design record, but an owner must still decide whether it supersedes the PDF, notebook, source code and older docs.

## Blocking findings

### B1 — Three incompatible architecture baselines (`BLOCKER`)

- Matrix: 8×4 vs 8×8/64 vs 5×9/45.
- Compute: Jetson Orin Nano vs Orange Pi 5.
- Eye tracking: robot arm retained vs explicitly removed.
- Simulation: Gazebo/ROS2 vs SOFA and reduced-order models.

A paper, BOM, architecture diagram, protocol and novelty claim cannot be internally consistent until these are resolved. Do not patch all documents by majority vote; obtain an explicit owner decision.

### B2 — Synthetic results are presented too close to empirical validation (`BLOCKER`)

All seven current experiment scripts use generated/reference data. `docs/11_Academic_Review.md` acknowledges no hardware validation, but also displays values such as 97.5%, 22.05 ± 2.94 mmHg and +839.6% with PASS symbols, then issues “Accept with minor revisions.” This framing can mislead a reader into treating code smoke tests as physical outcomes.

Required correction: use separate columns for `simulation`, `bench`, `integrated hardware`, `human participant`, and `clinical` evidence. Only the first currently has data. Never call the internal verdict external acceptance.

### B3 — Citation-verification claim fails an internal consistency check (`BLOCKER`)

`docs/10_References.md` states that all sources passed Tier-0 verification, while its own verification table labels Saadeh 2018 as Tier-1 and “need DOI.” No complete DOI/URL/anchor provenance is supplied for all 26 entries. Initial exact-title searches did not retrieve these stated records:

- Saadeh et al. 2018, “A high-resolution, hybrid pressure sensor for wheelchair cushions”;
- Khan et al. 2021, “Cross-calibration of flexible pressure sensors for medical applications,” *Sensors* 21(12):4102;
- Mahmood et al. 2023, “Self-improving medical AI agents: a survey,” *npj Digital Medicine*.

They are `UNVERIFIED`, not declared nonexistent. Each must be resolved via publisher/Crossref/full text or replaced with a real source that supports the exact claim. The broader novelty/gap claims must be re-run only after this bibliography cleanup.

### B4 — Human participant plan lacks demonstrated pre-approval (`SAFETY BLOCKER`)

`docs/08_Experimental_Protocol.md` proposes 10–20 volunteers depending on experiment and up to four hours lying on the device. A notice to a school science committee or mentor approval is not automatically a properly constituted IRB. Official ISEF human-participant rules require IRB review and approval before recruitment or interaction for non-exempt testing by others, plus the applicable consent and documentation process (`SRC-ISEF-2026-HUMAN`, `SRC-ISEF-2026-GUIDE`).

Required correction: no recruitment, pilot interaction or prototype testing with others until the affiliated fair/IRB confirms the route. Use mannequin, calibrated loads and bench rigs meanwhile. The four-hour exposure requires a qualified risk assessment; “healthy volunteer” does not eliminate device, pressure, discomfort or privacy risk.

### B5 — `32 mmHg` cannot be the universal safety/pass criterion (`MAJOR`)

Several older documents use sacral pressure `<32 mmHg` as a hard PASS. Biomechanical evidence explains that interface pressure does not directly represent deep-tissue stress and that the historical capillary value varies by tissue/site/person; avoiding values above 32 mmHg is not necessarily “pressure relief” (`SRC-GEFEN-SAPU-REVIEW`). Later docs correctly soften it to a reference value.

Required correction: treat pressure magnitude jointly with time, spatial distribution, unloading/reperfusion behavior, peak/gradient stability and uncertainty. Keep any threshold framed as an engineering reference unless a qualified protocol supports a specific use.

### B6 — Full-stack scope obscures a feasible ISEF contribution (`MAJOR`)

A 45/64-cell pneumatic system, custom sensing, per-cell control, CNN-LSTM, stereo gaze, an active camera arm, on-device LLM/AAC, contextual-bandit self-improvement, ROS2 and edge deployment are too many coupled validation problems for one defensible school-year result. Integration alone can be a contribution, but “four gaps at once” is not established novelty.

Recommended MVP: at most three measured contributions, for example:

1. calibrated low-cost pressure sensing under realistic cyclic/curved loading;
2. mannequin-based closed-loop pressure redistribution on a small safe cell array;
3. reproducible comparison against static/alternating baselines with uncertainty and ablations.

AAC can remain a separately evaluated accessibility module only if resources and a coherent RQ justify it. Defer the robot arm, online self-improvement and untrained LLM unless they are central and safely testable.

## Important non-blocking corrections

- The PDF uses “ALS” where American Sign Language is normally “ASL”; context must clarify whether the target users are people with amyotrophic lateral sclerosis (ALS), users of sign language (ASL), or a different population.
- “Clinical-grade,” “real-time,” latency, accuracy, cost and epidemiology numbers need primary-source or measured anchors.
- Caffe is not a runtime dependency of PlotNeuralNet and does not match the current NumPy/reference model path; keep it reference-only unless an experiment requires it.
- PGF upstream source is not needed for normal MiKTeX use; use the distribution package to avoid untested version combinations.
- Raw-data schemas, calibration weights/instruments, environment, sensor serial/position, code commit and exclusion logs are needed before claims become reproducible.

## Questions that must be answered before editing the project baseline

```text
1. Final matrix: 8×4, 8×8/64, or 5×9/45?
2. Final compute board: Jetson Orin Nano or Orange Pi 5?
3. Is the robot arm definitely removed?
4. Is SOFA the primary simulator, and what remains of Gazebo/ROS2?
5. What are the maximum three measured ISEF contributions?
6. Has any hardware actually been built? If yes, where are dated photos, BOM/serials, raw data and test logs?
7. Is human testing intended in this competition cycle? If yes, has a valid IRB/SRC approved it before recruitment/data collection?
```

## Review confidence and limits

High confidence: document conflicts, blank PDF result sections, synthetic experiment status, missing demonstrated human-participant pre-approval, and internal contradiction in the Tier-0 claim.  
Moderate confidence: recommended MVP and feasibility assessment; this depends on actual resources/timeline not yet provided.  
Not established: whether the three suspect citations truly do not exist; only exact-title search misses have been recorded.
