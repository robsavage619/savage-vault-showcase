# Sample Routing Transcript

This is a synthetic example showing how an agent should use the vault. It is not copied from the private vault.

## User request

> Can you fix the data pipeline in my project?

## Correct agent behavior

```text
1. Ask for or identify the exact repository.
2. Read the vault entry route.
3. Open the project manifest for that repository.
4. Open the coding-agent operating card.
5. Open the data-system and data-contract playbooks.
6. Inspect the live repo README, agent docs, schemas, config, tests, and pipeline entry point.
7. Identify source-of-truth vs. derived artifacts.
8. Make the smallest compatible change.
9. Validate with targeted tests and repo-native checks.
10. Report what passed and what remains uncertain.
```

## Incorrect agent behavior

```text
1. Search the vault broadly for "pipeline."
2. Assume the manifest reflects current repo state.
3. Edit a derived table or report as if it were source data.
4. Claim success without checking consumers, schemas, or tests.
```

## Core rule

Vault context guides the agent. Live files decide the implementation.

