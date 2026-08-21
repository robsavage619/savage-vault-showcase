---
type: analysis
title: "Coding-Agent Safe Change Playbook"
summary: "Safe-change playbook for coding agents modifying existing repositories. It combines Ousterhout's complexity model, Feathers's legacy-code protocol, Fowler's refactoring discipline, and Google's review habits into a practical patch sequence."
tags: [coding-agents, refactoring, legacy-code, software-engineering]
sources: []
created: 2026-08-08
updated: 2026-08-08
status: active
aliases: ["agent safe change playbook", "coding agent refactoring route"]
related: []
confidence: high
domains: [software-engineering, ai-engineering]
source_kind: synthesis
authority_level: synthetic
evidence_level: indirect
validation_status: validated
fidelity_status: source-checked
index_eligible: true
retrieval_priority: critical
approved_use: ["coding-agent-guidance", "refactoring-rubric", "legacy-code-change"]
prohibited_use: ["silent-broad-refactor"]
---

# Coding-Agent Safe Change Playbook

## Summary

Safe-change playbook for coding agents modifying existing repositories. It combines Ousterhout's complexity model, Feathers's legacy-code protocol, Fowler's refactoring discipline, and Google's review habits into a practical patch sequence.

## Patch Sequence

1. **Map the current behavior.** Read the smallest set of files/tests that explain the change.
2. **Find the seam.** Identify where behavior can be observed or varied safely.
3. **Characterize if needed.** If behavior is untested, add a characterization test before changing it.
4. **Make the behavioral change.** Keep it small and scoped.
5. **Refactor only after safety exists.** Use named refactoring moves; preserve behavior.
6. **Reduce complexity.** Check change amplification, cognitive load, and unknown unknowns.
7. **Validate and report.** Say what passed and what remains uncertain.

## Red Flags

- Broad rewrite before a test exists.
- New abstraction that only forwards calls.
- Mixed behavior change plus unrelated cleanup.
- Hidden global/config/time/network dependency.
- Catch-all exception hiding an unknown failure.
- “Looks cleaner” without a named design problem.

## Source Grounding

- **ousterhout-2024-ch2-5-complexity-deep-modules** — complexity symptoms and deep modules.
- **feathers-2004-ch2-4-feedback-seams** — create feedback before change.
- **feathers-2004-ch13-characterization-tests** — record actual behavior first.
- **fowler-2018-coding-agent-extraction** — behavior-preserving transformations.
- **winters-2020-ch9-14-review-testing** — review code as liability.

## See Also

- [[coding-agent-validation-playbook]]
- [[coding-agent-python-architecture-playbook]]
