---
name: vietnamese-proposal-writing
description: Evidence-first Vietnamese school research proposal drafting and review, using the project author's observed register while avoiding generic AI prose and unsupported claims.
---

# Vietnamese proposal writing (project skill)

> **Project-specific current ruling (2026-10-19):** defer to `research/context/CURRENT_DESIGN_BASELINE.md`. AAN is primary; servo winds fishing line directly on a spool (no spring/four-bar); Velostat/EI is relative, not absolute force; no Newton-based assistance formula or current 5 N limit. Phantom first; any powered healthy-volunteer test only after successful safety evaluation and required approvals. Treat proposal values as targets absent traceable logs; GAP is open pending a valid angle method; do not claim “first” or novelty.

Use this skill for the school's current six-part KHKT proposal, reviewer notes, and text prepared for the team. The current Drive source and its provenance are listed in `research/context/CURRENT_SUBMISSION_2026-10-17.md`.

## 1. Intake before drafting

- Read `AGENTS.md`, the current proposal source, relevant adopted decisions, and the applicable protocol before proposing edits.
- Identify the document's purpose, school template, audience, length and deadline. The current school template has six sections: project title; reason for choosing the topic; objectives; idea/content; expected products/results; feasibility.
- Do not assume the local Markdown file is the latest version. Keep an explicit source/version/date for every draft.
- Build a short claim map first: statement → evidence/source ID → evidence status → how it may be worded. Resolve conflicts before polishing sentences.

## 2. Evidence ledger: mandatory labels

For each quantitative or consequential statement, label internally as one of:

- **Source fact** — tied to a source ID and the exact supporting passage/table/page.
- **Project measurement** — tied to a dated raw log, protocol, calibration and units.
- **Calculation** — show inputs, formula and rounding; label as the team's estimate, not a published statistic.
- **Target/acceptance threshold** — use future/conditional wording (“mục tiêu”, “ngưỡng đặt trước”, “sẽ kiểm tra”).
- **Hypothesis/rationale** — say it is a proposed explanation, not an established outcome.
- **Interpretation** — bounded to the tested sample, setup and period.

If the source is a title, abstract, search result, cached snippet, or secondary summary, say so in the ledger and do not write as if the full text was checked. Verify citation metadata and claim support separately. Never invent a DOI, author, page, quotation, measurement, participant, expert endorsement, or reference number. Preserve `UNVERIFIED`, `PARTIAL`, `CONFLICTED`, and negative results until primary evidence resolves them.

## 3. Project-specific scope and safety guardrails

- Use the latest adopted wording in `DECISION_LOG.md`, not stale titles or old GATE names copied from prior submissions.
- Keep “đo lực/đáp ứng”, “suy luận hướng”, “góc đo trực tiếp”, and “diễn giải chức năng” distinct. A sensor proxy is not a clinical outcome.
- Do not say the system diagnoses stroke, replaces FMA/ARAT/BBT, proves recovery, or is clinically validated.
- State that the AAN mechanism is currently checked only on a mechanical rig and hand phantom, unless an approved decision and evidence explicitly change that boundary. Do not imply it assists a patient.
- Do not describe a proposed RL/edge-AI capability, latency, sampling rate, NPU performance, or GATE as implemented or passed unless dated test artifacts demonstrate it.
- Never recruit or test a human participant before the relevant ethics/SRC/IRB determination and approval documented for this project.

## 4. Voice profile: use the author's strengths, not the old topic's content

The supplied style sample is an earlier, unrelated agriculture/robotics proposal. It is useful only as a sample of structure and register. A newer, topic-relevant proposal was also read in the user's Drive folder. Do not reuse the sample's facts, citations, technical claims, or errors.

Preserve these observed preferences:

- Vietnamese academic register with direct section headings and numbered subsections.
- A practical chain from problem → why it matters → what the team will do → how it will be checked.
- Concrete quantities and technical nouns where the evidence supports them.
- Brief lists/tables for requirements, steps and comparison; explanatory prose for the reasoning.
- A clear author/team point of view when genuinely supplied by the student (for example, why this topic was chosen).

Do not manufacture a personal anecdote or pretend the student wrote or performed something. Retain first person only where it is authentic and consistent with the submission's voice.

## 5. Anti-slop editing: natural, clear, not detector evasion

The goal is readable, specific writing in the student's real voice—not to disguise AI use or game AI detectors. Follow any school disclosure rules.

- Start paragraphs with the actual problem, evidence, decision, or action; remove throat-clearing.
- Give each paragraph one job. Prefer one supported claim per sentence; explain what the evidence does and does not establish.
- Vary sentence length and section structure naturally. Avoid making every paragraph the same size, every section a three-item list, or repeatedly using the same “không phải X mà là Y” contrast.
- Use dashes, semicolons and colon-led lists only when they clarify the sentence; do not impose arbitrary counts or add punctuation variation for its own sake.
- Prefer concrete verbs (“đo”, “so sánh”, “ghi”, “kiểm tra”, “ước tính”) over padded nouns and promotional adjectives.
- Cut repeated summaries, duplicated “điểm mới” claims, and empty transitions that do not advance the argument.
- Treat formulaic openers such as “Trong bối cảnh…”, “Từ những vấn đề trên…”, “Có thể thấy rằng…”, “Đóng vai trò quan trọng…”, “mở ra tiềm năng…”, and “mang tính đột phá/toàn diện” as edit flags, not banned words. Keep one only if it adds precise, necessary meaning.
- Avoid unsupported certainty (“chứng minh”, “triệt tiêu”, “đầu tiên”, “đảm bảo”, “hiệu quả lâm sàng”). Choose a verb matching the evidence: “đề xuất”, “dự kiến”, “thử nghiệm”, “quan sát”, “ghi nhận”, “cho thấy trong điều kiện…”.
- Do not add deliberate typos, random colloquialisms, or awkward phrasing to seem human. Authenticity comes from the student's real choices and accurately reported work.

## 6. Draft → challenge → revise

1. **Outline:** map each required school section to its purpose and evidence; move content only, don't silently change scope.
2. **Draft:** write plainly in the author's register and mark unresolved facts as `[CẦN XÁC MINH: ...]` in the working copy, never in a submission-ready copy.
3. **Evidence challenge:** for every number, superlative, causal statement, novelty statement and safety statement, ask “what exact source/log licenses these words?”
4. **Adversarial review:** check for contradictory decisions, citation-number mismatch, planned-as-completed claims, missing controls, inflated benefits, and unsupported claims about patients.
5. **Human pass:** ask the student/team to confirm personal rationale, actual work performed, names, deadline and institutional template. Do not invent the answers.
6. **Final pass:** remove working markers, retain the change log, and list any unresolved items separately instead of laundering them into polished prose.

## 7. Review integrity

Use `research/protocols/ISEF_REVIEW_ORCHESTRATION.md` for substantial review. Reviewer roles are a way to organize questions, not proof of independent reasoning. Do not claim “independent multi-agent review” unless the underlying separate executions and artifacts exist. Majority vote does not replace evidence or project-owner decisions.
