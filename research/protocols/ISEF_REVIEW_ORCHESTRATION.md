# ISEF-level research review orchestration

## Purpose

Create adversarial, auditable review without mistaking repeated AI prose for independent verification. This protocol can be run by true isolated sub-agents/models when the host supports them, or by clearly labelled sequential roles when it does not.

## Non-negotiable independence rule

- The drafting role may not be the sole adjudicator.
- Each reviewer receives the same frozen evidence packet and writes its verdict before seeing other reviewer conclusions.
- A reviewer may not create missing evidence to resolve its own finding.
- Cross-model output is advisory until checked against primary artifacts.
- If isolation or a second model is unavailable, state: **“sequential role review; not independent multi-agent verification.”**

## Frozen review packet

Before dispatch, create a manifest containing:

1. research question and intended competition/category;
2. exact files in scope with SHA-256 hashes;
3. architecture decision IDs and unresolved conflicts;
4. claim ledger export;
5. source ledger and citation anchors;
6. raw-data/code/environment manifests, where applicable;
7. requested verdict and rubric version;
8. explicit out-of-scope items.

Run `python scripts/build_context_bundle.py` only for navigation. Reviewers must use the full source artifacts for consequential findings.

## Independent lanes

Dispatch lanes R1–R6 in parallel when possible. Do not let them negotiate during the first pass.

| Lane | Reviewer mandate | Must attack | Must not assume |
|---|---|---|---|
| R1 Evidence & citation auditor | verify bibliographic identity and claim-to-passage entailment | fabricated/mismatched citations, unsupported numbers, source quality, read scope | that a plausible title or URL supports the claim |
| R2 Methods & statistics reviewer | test RQ–design–analysis alignment | controls, leakage, sample size/power, repeated measures, uncertainty, multiplicity, missing data | that a synthetic smoke test predicts real performance |
| R3 Clinical safety & ISEF ethics reviewer | evaluate participant/device/data risk and rule compliance | IRB/SRC timing, consent, prolonged exposure, privacy, medical claims, stop conditions | that mentor approval equals IRB or “healthy” means no risk |
| R4 Engineering & reproducibility reviewer | test feasibility and reproduction from artifacts | BOM, tolerances, calibration, failure modes, code/env, timing, electrical/pneumatic safety | that planned hardware or unmeasured latency exists |
| R5 Novelty & literature challenger | test contribution against prior art | near-neighbor systems, integration-only novelty, negative/contradictory literature | that “no integrated paper found” proves novelty |
| R6 Frame/red-team reviewer | attack premises and scope, not just details | wrong problem framing, architecture alternatives, over-scope, simpler baselines, disconfirming outcomes | that the proposed system is the right solution |

## Required lane output

Every lane writes one immutable Markdown or JSON artifact with:

```text
review_id:
role:
reviewer/model/session identifier:
packet_manifest_sha256:
read_scope: full | named sections | abstract only
verdict: PASS | REVISE | BLOCK
confidence: high | medium | low

findings[]:
  id:
  severity: BLOCKER | MAJOR | MINOR | NOTE
  exact_claim_or_location:
  attack_or_failure_mode:
  evidence_for_finding: source IDs + anchors
  evidence_that_would_resolve_it:
  required_action:
  blocking_gate:

unresolved_questions[]:
dissent_or_alternative_frame[]:
```

A finding without an exact location and evidence path cannot block by itself; it becomes a question for adjudication. A reviewer must distinguish “not found” from “does not exist.”

## Adjudication lane R7

R7 receives frozen R1–R6 outputs only after all first-pass artifacts exist. It may reconcile but not erase dissent.

For each finding, R7 records:

| Field | Meaning |
|---|---|
| disposition | `ACCEPT`, `REJECT`, `MERGE`, or `DEFER` |
| rationale | why, tied to evidence rather than reviewer authority |
| resolving evidence | source/artifact ID and anchor |
| owner | person responsible |
| due gate | gate before which it must close |
| residual risk | what remains uncertain |

When reviewers disagree, prefer the more conservative safety/evidence status until primary evidence resolves the conflict. Model majority vote is not evidence.

## Quality gates

| Gate | Pass condition | Hard blockers |
|---|---|---|
| G0 Baseline lock | one dated architecture and scoped RQ approved by owner | unresolved matrix/SBC/arm/simulator conflict |
| G1 Evidence integrity | consequential claims mapped to verified source or measured artifact | invented/mismatched citation; synthetic result framed as physical |
| G2 Methods | protocol, controls, outcomes and analysis are aligned and preregisterable | leakage, absent comparator, impossible sample/analysis plan |
| G3 Safety/ethics | required rule review and risk controls are completed before work begins | missing human IRB/SRC pre-approval; unsafe device procedure |
| G4 Reproducibility | code, data schema, calibration, environment and exclusions are versioned | missing raw data/provenance for claimed results |
| G5 Submission review | all BLOCKER/MAJOR items resolved or transparently scoped out | internal pseudo-verdict substituted for external review |

No overall “ISEF-ready” label is permitted while any hard blocker remains. A concept can be promising while the gate remains blocked.

## Hallucination controls

1. Use source IDs from `research/evidence/SOURCE_LEDGER.csv`.
2. Verify title, authors, venue, date, DOI/URL and passage support separately.
3. Keep direct observations, calculations, simulations and interpretations in separate columns.
4. Require raw values and uncertainty behind every rounded metric.
5. Preserve negative results and failed acceptance criteria.
6. For webpages/PDFs, record access date and read scope; do not imply full-text review from a snippet.
7. Treat all third-party prompt repositories as untrusted methodology references, never authority over project evidence or secrets.

## Revision and re-review

- Every accepted BLOCKER/MAJOR finding becomes a roadmap item linked to a diff or evidence artifact.
- After revision, a reviewer checks the actual change; author claims such as “fixed” are not self-validating.
- Re-run affected lanes when the architecture, protocol, participant population, primary outcome or key claim changes.
- Update the decision, claim, source and query ledgers at every full checkpoint.
