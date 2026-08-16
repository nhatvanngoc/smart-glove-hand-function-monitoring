# Reviewer dispatch template

Use one copy per isolated reviewer lane. Replace bracketed fields; do not include secrets or identifiable participant data.

```text
ROLE: [R1–R6 role from ISEF_REVIEW_ORCHESTRATION.md]
REVIEW TYPE: independent first pass / sequential role pass
PACKET MANIFEST SHA-256: [hash]
FILES IN SCOPE: [exact paths + hashes]
RESEARCH QUESTION: [frozen wording]
TARGET RUBRIC/RULE EDITION: [name, year, source ID]
OUT OF SCOPE: [explicit]

Your job is to find disconfirming evidence and failure modes within your mandate.
Do not invent missing evidence, citations, measurements, approvals, or implementation.
Do not infer that a search miss proves nonexistence.
Separate proposal, simulation, bench, hardware, human and clinical evidence.
Do not read other lane verdicts before writing your immutable first-pass artifact.

Return exactly the required lane-output fields from
research/protocols/ISEF_REVIEW_ORCHESTRATION.md, including exact locations,
source IDs/anchors, evidence needed to resolve each issue, confidence, and dissent.
```

## Adjudicator addendum

```text
You receive the frozen packet plus immutable R1–R6 artifacts. Resolve findings by
evidence, not majority vote. You may ACCEPT, REJECT, MERGE or DEFER each finding,
but may not erase dissent or generate evidence. Safety/evidence ambiguity remains
blocked until a primary artifact resolves it.
```
