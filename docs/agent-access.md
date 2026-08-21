# Agent Access Model

This showcase documents the access pattern used by coding agents and research agents against the private vault.

## Default route

```text
START HERE
→ wiki/agent-entry
→ wiki/question-router
→ wiki/index-short, unless a narrower route is already known
→ relevant retrieval pack
→ relevant playbook/source/concept
```

## Coding-agent route

Before changing code under a project root:

1. Identify the exact repository.
2. Read the project manifest for that repository.
3. Read the coding-agent operating card.
4. Read the relevant retrieval pack and task playbook.
5. Inspect the live repository files named by the manifest.
6. Make the smallest safe change.
7. Validate with repo-native checks.
8. Report what passed, what was not run, and what remains uncertain.

## Important guardrail

The agent should not modify anything until the exact repository is named.

A project root is not a repo. A manifest is not proof of current repo state. The live repo wins.

## Fast retrieval strategy

The private vault keeps a compact `index-short` as a tier-0 retrieval cache. Agents should use it for routing, not as a substitute for opening source notes when claims require evidence.

Escalation ladder:

```text
index-short hook is enough → answer
need fuller summary → open index
need evidence/caveats → open page
need exact source fidelity → inspect raw/private source, if available and permitted
```

## Unsafe answer patterns

A vault-backed answer fails the bar when it:

- treats vault notes as proof of live repo or API state
- skips live repository inspection before code advice
- silently relies on stale or low-confidence material
- treats missing maturity metadata as reviewed
- invents citations
- cites a file that was not actually opened

