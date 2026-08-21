---
type: concept
title: "Unit Economics: Cost per Outcome"
summary: "Dividing spend by a business-meaningful denominator so cost becomes interpretable — cost per inference, per transaction, per active user, per resolved ticket. For AI systems the denominator problem is acute, because token spend is easy to measure and the outcome it purchases usually is not."
tags: [finops, unit-economics, cloud-cost, metrics, ai-cost, measurement, decision-science]
sources: []
created: 2026-08-19
updated: 2026-08-19
status: active
aliases: ["unit economics", "cost per inference", "cost per transaction", "cost per token", "is my AI spend reasonable", "AI cost metrics", "accuracy per dollar"]
related: ["[[finops-capability-model]]", "[[focus-billing-schema]]", "[[test-time-compute-scaling]]", "[[retrieval-pack-finops-cost-engineering]]"]
confidence: high
domains: [finops, decision-science, ai-engineering]
source_kind: synthesis
authority_level: synthetic
evidence_level: indirect
validation_status: reviewed
fidelity_status: source-checked
index_eligible: true
retrieval_priority: high
---

# Unit Economics: Cost per Outcome

## Summary

A total spend figure is uninterpretable on its own. "$40,000 last month" is neither good nor bad until it is divided by something the business cares about — inferences served, transactions processed, active users, tickets resolved. **Unit Economics** is a named capability in [[finops-capability-model]], and for AI systems the FinOps for AI category supplies the specific denominators: **Cost per Inference**, **Cost per API Call**, **Token Consumption Metrics**, **Training Cost Efficiency**, **Time to First Prompt**.

## How It Works

Three parts, and the middle one is where the work is.

**The numerator** should be Effective Cost, not Billed Cost ([[focus-billing-schema]]) — you want what the workload consumed, amortized, not what happened to be invoiced that month.

**The denominator** is the hard part. It must be something the business actually values, and there is usually a tempting proxy that is easier to count. Cost per API call is easy; cost per *successfully resolved request* is what matters. The gap between them is exactly **proxy-metric-validity**, and optimizing the easy one is a textbook **goodharts-law** setup — an agent that fails fast and cheaply looks excellent on cost per call.

**The decomposition** turns the ratio into something actionable. Cost per resolved request factors into tokens per attempt × attempts per resolution × price per token. Those three have different owners and different fixes, and the aggregate ratio hides which one moved — see **measurement-decomposition**.

## Why It Matters for AI

**Token spend is trivially measurable; the outcome purchased is not.** This asymmetry is why AI cost discussions default to token counts, and why they so often fail to answer whether the spend was worthwhile.

**Reasoning models change the cost object.** [[test-time-compute-scaling]] establishes that accuracy is purchasable with inference tokens, so the honest presentation of a model decision is an **accuracy-versus-tokens curve**, not a single price. A smaller model with a good inference strategy can dominate a larger one at equal cost — invisible under a naive cost-per-call metric, obvious under cost per correct outcome.

**Emergent thinking length is a cost multiplier nobody budgeted for.** **deepseek-2025-r1-reasoning-rl** documents response length growing on its own through RL training. Reasoning models are a different cost object from chat models, and a per-request cost estimate built on chat-model behavior will be wrong by a multiple.

## Perspectives

Denominators are political. Which outcome counts determines whose team looks efficient, so the choice gets litigated — which is a reason to fix definitions early, publish them, and version them like any other contract.

Not everything worth doing has a clean unit. Exploratory work, research spikes and reliability investments resist per-unit framing, and forcing one produces a number that is precise and meaningless. **decision-oriented-measurement** is the check: measure the thing that would change a decision, and be willing to conclude that no unit metric would.

## Related Concepts

- [[finops-capability-model]] — where this sits as a named capability
- **proxy-metric-validity** · **goodharts-law** · **measurement-decomposition**
- [[test-time-compute-scaling]] — why the AI denominator keeps moving

## See Also

- **finops-2026-framework-domains-capabilities**
- **koenigstein-2026-ch11-agent-cost-efficiency**
- [[retrieval-pack-finops-cost-engineering]]
