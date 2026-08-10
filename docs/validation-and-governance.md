# Validation and Governance

The private vault uses metadata and validation checks so agents can distinguish evidence, synthesis, routing, and live-state authority.

## Maturity fields

Each mature page includes fields such as:

```yaml
validation_status: reviewed
fidelity_status: source-checked
retrieval_priority: high
symbolic_role: evidence
evidence_lane: engineering
requires_review: false
approved_use: ["coding-agent-guidance"]
prohibited_use: ["substituting-for-live-repo-inspection"]
```

## Why this matters

Agents are bad at noticing when they have moved from “this note says X” to “X is currently true.” The governance layer makes that boundary explicit.

## Decision-grade use

A note can support a decision-grade answer only when:

- metadata is present
- source fidelity is known
- uncertainty is stated
- the answer stays inside approved use
- live sources are inspected when live state matters

## Validation examples

The private validation pass checks:

- required frontmatter fields
- unresolved wikilinks
- raw-source links
- index drift
- missing maturity metadata
- stale project manifests
- notes that should not be promoted into retrieval packs

The public showcase validation is narrower because it intentionally excludes private content.

