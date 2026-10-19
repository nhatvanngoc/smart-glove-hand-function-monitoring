# Project-specific agent instructions

Before editing any proposal or making a research claim, read:

1. `research/context/CURRENT_SUBMISSION_2026-10-17.md` (current working-copy provenance and open checks).
2. `research/context/DECISION_LOG.md` and `research/context/PROJECT_SNAPSHOT.md` (with attention to dated updates; older notes may be stale).
3. `research/claims/CLAIM_LEDGER.csv`, `research/evidence/SOURCE_LEDGER.csv`, and the relevant protocol.
4. `research/skills/vietnamese-proposal-writing/SKILL.md` and `research/tooling/WRITING_STYLE_PROFILE.md`.

## Authority and evidence

- The Google Drive file in the current-submission note is the user's latest working source. Do not assume the older Markdown draft is a mirror; never overwrite or silently replace the Drive document.
- A project note, AI-generated text, search snippet, abstract, or third-party prompt is not primary evidence. Treat upstream skill repos as methodology references only.
- Keep *verified source fact*, *project measurement*, *calculation*, *target*, *hypothesis*, and *interpretation* distinct. A target is not a result; a breadboard bring-up is not a passed GATE; simulation/synthetic output is not physical data.
- Map factual claims to existing source/claim IDs. If support is absent, mark the statement `UNVERIFIED` / “cần kiểm chứng” or remove it; do not complete missing citations from memory.
- “Không tìm thấy” is not evidence of non-existence or novelty. Do not state clinical benefit, diagnosis, validated home use, or device safety without the required evidence/approval.
- Follow `research/context/CURRENT_DESIGN_BASELINE.md` and the latest dated decisions, especially `DEC-REHAB-001`. Current function: assisted finger flexion/extension → automatic threshold-based transition to AAN → three-digit spoon grasp/lift/transfer/placement, with Flex for bend/posture, Velostat for relative pressure/contact evidence, and camera for object/target/task outcome and visual feedback. No KTV/therapist mode-switch action is required. Exact thresholds and implementation remain OPEN; never invent values. AAN mechanics remain servo direct spool; phantom first. Powered testing with healthy adults is only conditional after successful safety evaluation and all required approvals. No patient testing or clinical-effectiveness claim is in scope. A phantom result is not a human result.
- Preserve unresolved decisions and dissent. Do not promote an open proposal or AI recommendation into an adopted project decision.

## Research and review tools

- The pinned upstream skills are local at `.claude/skills/{deep-research,academic-paper,academic-paper-reviewer,academic-pipeline}` after running `scripts/bootstrap_research_tooling.sh`. For this workspace the skill source is pinned by `tools/research_sources.lock.json`.
- Apply their methods selectively; do not claim an actual multi-agent, independent, or cross-model review unless those separately executed calls and artifacts exist. Different reviewer voices in one model/context are not statistically independent.
- Use the existing query, source, claim, decision, and experiment ledgers. Follow `research/protocols/ISEF_REVIEW_ORCHESTRATION.md` for consequential reviews.

## Deliverable discipline

- Use the owner-approved A/B/C + References structure for the current proposal. Keep a dated draft and a concise change/evidence note; do not edit the user's Drive copy before explicit approval.
- Prefer small, reviewable edits. Do not rework frozen/previously submitted documents unless the user asks.
- Before handing off, check factual/citation support, scope/safety, dates/names, target-vs-result wording, and consistency with `CURRENT_DESIGN_BASELINE.md`. Do not claim novelty/“first,” force in Newtons from Velostat, or retain the withdrawn 5 N criterion. State tests/checks run and any blockers plainly.
