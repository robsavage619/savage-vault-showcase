---
type: overview
title: "Retrieval Pack: AI Engineering"
summary: "Curated routing pack for RAG, retrieval, agents, LLM evaluation, and production LLM application questions. Prioritizes overview pages, canonical papers, engineering patterns, and evaluation notes."
tags: [meta, retrieval, ai-engineering, agent]
sources: []
created: 2026-08-08
updated: 2026-08-19
status: active
aliases: ["AI engineering retrieval pack", "RAG retrieval pack", "agent engineering pack"]
related: ["[[question-router]]", "[[coding-agent-operating-card]]", "[[agent-access-coding-corpus]]", "[[template-catalog]]", "[[corpus-weekly-review-protocol]]", "[[coding-agent-review-checklist]]", "[[coding-agent-context-retrieval-playbook]]", "[[coding-agent-validation-playbook]]", "[[coding-agent-safe-change-playbook]]", "[[coding-agent-python-architecture-playbook]]", "[[coding-agent-data-system-playbook]]", "[[coding-agent-production-readiness-playbook]]"]
confidence: high
domains: [ai-engineering, rag, agents, evals]
source_kind: meta
authority_level: administrative
evidence_level: administrative
validation_status: validated
fidelity_status: not-applicable
index_eligible: true
retrieval_priority: critical
symbolic_role: retrieval-pack
evidence_lane: admin
requires_review: false
---

# Retrieval Pack: AI Engineering

## Summary

Use this pack for questions about RAG, retrieval systems, LLM agents, tool use, and LLM evaluation. Start with the overviews, then move to canonical source notes for methods and tradeoffs. For implementation choices, distinguish benchmark evidence from engineering pattern notes.

## Task Paths

- Bug fix or safe change in `~/Projects`: read **project-context-manifests** for the target repo, then [[coding-agent-safe-change-playbook]], [[coding-agent-validation-playbook]], and [[coding-agent-review-checklist]].
- New agent, eval, or orchestration design: read [[coding-agent-operating-card]], [[coding-agent-context-retrieval-playbook]], [[coding-agent-validation-playbook]], then the benchmark/source notes below.
- Data-system, RAG-store, cache, or pipeline change: read the project manifest, [[coding-agent-data-system-playbook]], **kleppmann-riccomini-2024-data-system-boundaries**, and [[coding-agent-validation-playbook]].
- Data-contract, ML pipeline, model-serving, or MLOps change: read the project manifest, [[coding-agent-data-ml-contracts-playbook]], [[coding-agent-data-system-playbook]], and [[coding-agent-validation-playbook]].
- Production-readiness or deployment question: read the project manifest, [[coding-agent-production-readiness-playbook]], **nygard-2007-coding-agent-extraction**, and **forsgren-humble-kim-2018-coding-agent-extraction**.
- Measurement, causality, or system-behavior question: read **decision-oriented-measurement**, **value-of-information**, **causal-question-type-gate**, and **systems-leverage-points** before making metric, benchmark, root-cause, or intervention claims.
- Vault, corpus, or agent-docs work: read **project-context-manifests**, [[template-catalog]], and [[corpus-weekly-review-protocol]] before adding new surfaces.
- Agent handling untrusted data (web content, email, retrieved documents, third-party tool output): read [[agent-isolation-design-patterns]] first, then [[control-flow-integrity-for-agents]] and [[capability-based-tool-policy]]. Pick the least general pattern that does the job.
- Reasoning-model selection, thinking budgets, or "bigger model vs more thinking": read [[test-time-compute-scaling]], then **snell-2024-scaling-test-time-compute** and **llm-selection-framework**. Price the decision as an accuracy-versus-tokens curve, not a per-call rate.
- Cost of an agent, model, or pipeline: read [[retrieval-pack-finops-cost-engineering]] and [[unit-economics-cost-per-outcome]].
- Building or interpreting an eval: read [[eval-power-analysis]] **before** building it and [[eval-statistical-inference]] before reporting a result.

## Reading Order

1. **overview-rag-retrieval**
2. **overview-agentic-llms**
3. **retrieval-augmented-generation**
4. **rag-for-knowledge-intensive-nlp**
5. **self-rag**
6. **ragas-automated-rag-evaluation**
7. **llm-agent-patterns**
8. **react-synergizing-reasoning-and-acting**
9. **toolformer**
10. **agentbench-evaluating-llm-agents**
11. **debenedetti-2024-agentdojo**
12. **zhan-2024-injecagent**
13. **owasp-2025-llm-top-10**
14. **owasp-2025-agentic-ai-threats-mitigations**
15. **owasp-2025-securing-agentic-applications**
16. **opentelemetry-2026-genai-semantic-conventions**
17. **cemri-2025-mast-multi-agent-failure-taxonomy**
18. **yao-2024-tau-bench-tool-agent-user**
19. **maharana-2024-locomo-long-term-memory**
20. **hu-2025-memoryagentbench**

## Coding-Agent Reading Order

1. **anthropic-2024-building-effective-agents**
2. **anthropic-2025-context-engineering-agents**
3. **jimenez-2023-swe-bench**
4. **openai-2024-swe-bench-verified**
5. **yang-2024-swe-agent**
6. **xia-2024-agentless**
7. **yang-2024-swe-bench-multimodal**
8. **badertdinov-2025-swe-rebench**
9. **deng-2025-swe-bench-pro**
10. **garg-2026-swe-bench-mutation**
11. **pan-2025-swe-gym**
12. **wang-2025-swe-dev**
13. **liu-2023-repobench**
14. **ding-2023-crosscodeeval**
15. **zhang-2023-repocoder**
16. **liu-2024-graphcoder**
17. **zhang-2024-autocoderover**
18. **ruan-2024-specrover**
19. **bouzenia-2024-repairagent**
20. **wang-2023-rap-gen**
21. **rafi-2024-llm4fl**
22. **wang-2024-openhands**
23. **anthropic-2025-writing-tools-for-agents**
24. **anthropic-2025-demystifying-evals-for-ai-agents**
25. **mcp-2026-server-tools-resources-prompts**
26. **zhang-2025-wasp-web-agent-security**
27. **cao-2025-vpi-bench**
28. **shi-2025-promptarmor**
29. **kang-2025-memoryos**
30. **owasp-2025-llm-top-10**
31. **owasp-2025-agentic-ai-threats-mitigations**
32. **owasp-2025-securing-agentic-applications**
33. **opentelemetry-2026-genai-semantic-conventions**

## Coding-Agent Book Layer

1. **coding-agent-book-ingest-manifest**
2. [[coding-agent-operating-card]]
3. [[agent-access-coding-corpus]]
4. [[coding-agent-review-checklist]]
5. [[coding-agent-context-retrieval-playbook]]
6. [[coding-agent-validation-playbook]]
7. [[coding-agent-safe-change-playbook]]
8. [[coding-agent-python-architecture-playbook]]
9. [[coding-agent-data-system-playbook]]
10. [[coding-agent-production-readiness-playbook]]
11. **huyen-2024-coding-agent-extraction**
12. **huyen-2024-ch3-evaluation-methodology**
13. **huyen-2024-ch6-rag-agents**
14. **huyen-2024-ch10-ai-architecture-feedback**
15. **ousterhout-2024-coding-agent-extraction**
16. **ousterhout-2024-ch2-5-complexity-deep-modules**
17. **ousterhout-2024-ch10-18-errors-comments-obvious-code**
18. **winters-2020-coding-agent-extraction**
19. **winters-2020-ch9-14-review-testing**
20. **winters-2020-ch17-24-tools-ci-delivery**
21. **percival-gregory-2020-coding-agent-extraction**
22. **percival-gregory-2020-ch1-3-domain-repository**
23. **percival-gregory-2020-ch6-13-uow-events-di**
24. **feathers-2004-coding-agent-extraction**
25. **feathers-2004-ch2-4-feedback-seams**
26. **feathers-2004-ch13-characterization-tests**
27. **fowler-2018-coding-agent-extraction**
28. **okken-2017-coding-agent-extraction**
29. **nygard-2007-coding-agent-extraction**
30. **forsgren-humble-kim-2018-coding-agent-extraction**
31. **kleppmann-riccomini-2024-coding-agent-extraction**
32. **kleppmann-riccomini-2024-data-system-boundaries**
33. **slatkin-2024-coding-agent-extraction**
34. **viafore-2022-coding-agent-extraction**
35. **percival-2025-coding-agent-extraction**
36. **evans-2003-coding-agent-extraction**
37. **richards-ford-2020-coding-agent-extraction**
38. **ford-2021-coding-agent-extraction**
39. **newman-2021-coding-agent-extraction**
40. **newman-2021-ch12-resiliency**
41. **skelton-pais-2025-coding-agent-extraction**
42. **beyer-2016-coding-agent-extraction**
43. **beyer-2018-coding-agent-extraction**
44. **fournier-nowland-2024-coding-agent-extraction**
45. **kim-humble-debois-willis-forsgren-2021-coding-agent-extraction**
46. **reis-housley-2022-coding-agent-extraction**
47. **ford-parsons-kua-sadalage-2022-coding-agent-extraction**
48. **reinertsen-2009-coding-agent-extraction**
49. **humble-molesky-oreilly-2015-coding-agent-extraction**
50. **kersten-2018-coding-agent-extraction**
51. **storment-fuller-2020-coding-agent-extraction**
52. **sanchez-garcia-2024-coding-agent-extraction**
53. **chung-2022-coding-agent-extraction**
54. **vanderkam-2024-coding-agent-extraction**
55. **flanagan-2020-coding-agent-extraction**
56. **mcdonald-2020-coding-agent-extraction**
57. **grigorik-2013-coding-agent-extraction**
58. **albada-2025-coding-agent-extraction**
59. **koenigstein-2025-coding-agent-extraction**
60. **koenigstein-2026-ai-agents-companion-repo**
61. **koenigstein-2026-ch2-planning-reactivity-multiagent**
62. **koenigstein-2026-ch5-contracts-tools-reliable-execution**
63. **koenigstein-2026-ch6-secure-execution-tool-governance**
64. **koenigstein-2026-ch7-deploying-agents-products**
65. **koenigstein-2026-ch8-9-agent-evaluation-observation**
66. **koenigstein-2026-ch10-agent-memory**
67. **koenigstein-2026-ch11-agent-cost-efficiency**
68. **koenigstein-2026-ch12-agent-threat-modeling**
69. **velasquez-song-ravikumar-2026-coding-agent-extraction**
70. **davis-2019-coding-agent-extraction**
71. **banks-porcello-2017-coding-agent-extraction**
72. **makarevich-2023-coding-agent-extraction**
73. **roldan-2023-coding-agent-extraction**
74. **cooper-reimann-cronin-2007-coding-agent-extraction**
75. **kholmatova-2017-coding-agent-extraction**
76. **krug-2013-coding-agent-extraction**
77. **norman-2013-coding-agent-extraction**
78. **pickering-2019-coding-agent-extraction**
79. **wathan-schoger-2018-coding-agent-extraction**
80. **jones-2023-coding-agent-extraction**
81. **jones-2023-ch2-data-contract-interface**
82. **jones-2023-ch6-7-schema-contract-architecture**
83. **jones-2023-ch9-10-contract-adoption-practice**
84. **gift-deza-2021-coding-agent-extraction**
85. **gift-deza-2021-ch1-4-mlops-lifecycle-delivery**
86. **gift-deza-2021-ch6-monitoring-logging-drift**
87. **gift-deza-2021-ch10-11-interoperability-cli-services**
88. **data-contract-boundary**
89. **schema-evolution-contracts**
90. **mlops-production-readiness**
91. **model-drift-monitoring**
92. **model-artifact-contract**
93. [[coding-agent-data-ml-contracts-playbook]]
94. **decision-oriented-measurement**
95. **value-of-information**
96. **calibrated-estimation**
97. **causal-question-type-gate**
98. **ladder-of-causation**
99. **confounding-control-gate**
100. **counterfactual-reasoning**
101. **stock-flow-feedback-model**
102. **systems-leverage-points**
103. **system-boundary-and-side-effects**

## Agent Implementation Playbooks

- [[coding-agent-operating-card]] — compact default behavior card: classify the work, retrieve the right playbook, inspect the repo, validate honestly.
- [[agent-access-coding-corpus]] — read order and access contract for Claude Code, Codex, ChatGPT-style agents, and REST clients.
- [[coding-agent-review-checklist]] — acceptance checklist for code changes, architecture proposals, eval designs, data changes, and production-readiness claims.
- [[coding-agent-context-retrieval-playbook]] — context budget, vault-route, repo-route, and anti-sludge rules.
- [[coding-agent-validation-playbook]] — eval/test/review route before claiming a code change works.
- [[coding-agent-safe-change-playbook]] — existing-code patch sequence grounded in complexity, seams, characterization tests, and refactoring.
- [[coding-agent-python-architecture-playbook]] — Rob's Python architecture route across domain model, services, typing, tests, and dependency boundaries.
- [[coding-agent-data-system-playbook]] — source-of-truth, derived-data, workload, cache, and rebuild-path rules.
- [[coding-agent-data-ml-contracts-playbook]] — fast data/ML route: producer-consumer contracts, schemas, model artifacts, drift, validation, rollback, and production-readiness checks.
- [[coding-agent-production-readiness-playbook]] — reliability, observability, delivery, and handoff checklist.
- **beyer-2016-coding-agent-extraction** and **beyer-2018-coding-agent-extraction** — SLO/error-budget/toil/alerting reliability rules.
- **fournier-nowland-2024-coding-agent-extraction** — internal tools as platform products with paved roads and developer-experience measures.
- **kim-humble-debois-willis-forsgren-2021-coding-agent-extraction**, **reinertsen-2009-coding-agent-extraction**, **humble-molesky-oreilly-2015-coding-agent-extraction**, and **kersten-2018-coding-agent-extraction** — flow, feedback, value-stream, and product-operating-model rules.
- **reis-housley-2022-coding-agent-extraction** — data-engineering lifecycle rules for pipelines, sync jobs, and derived data.
- **ford-parsons-kua-sadalage-2022-coding-agent-extraction** — architectural fitness-function and automated-governance rules.
- **storment-fuller-2020-coding-agent-extraction**, **sanchez-garcia-2024-coding-agent-extraction**, and **chung-2022-coding-agent-extraction** — cloud-cost, FinOps, tagging, ownership, anomaly, budget, and AWS governance rules.
- **vanderkam-2024-coding-agent-extraction** and **flanagan-2020-coding-agent-extraction** — TypeScript and JavaScript runtime-correctness rules for frontend work.
- **mcdonald-2020-coding-agent-extraction** and **grigorik-2013-coding-agent-extraction** — web-security and browser-network performance rules.
- **albada-2025-coding-agent-extraction**, **koenigstein-2025-coding-agent-extraction**, **koenigstein-2026-ai-agents-companion-repo**, **koenigstein-2026-ch2-planning-reactivity-multiagent**, **koenigstein-2026-ch5-contracts-tools-reliable-execution**, **koenigstein-2026-ch6-secure-execution-tool-governance**, **koenigstein-2026-ch7-deploying-agents-products**, **koenigstein-2026-ch8-9-agent-evaluation-observation**, **koenigstein-2026-ch10-agent-memory**, **koenigstein-2026-ch11-agent-cost-efficiency**, **koenigstein-2026-ch12-agent-threat-modeling**, and **velasquez-song-ravikumar-2026-coding-agent-extraction** — practical agent architecture, companion implementation notebooks, planning/ReAct/multiagent tradeoffs, MCP/tool contracts, sandboxing, deployment, evals, memory, cost, threat modeling, early-release/prose caution, and neurosymbolic constraint/reasoning rules.
- **debenedetti-2024-agentdojo**, **zhan-2024-injecagent**, **zhang-2025-wasp-web-agent-security**, **cao-2025-vpi-bench**, and **shi-2025-promptarmor** — prompt-injection, web-agent, visual-prompt, and defense-evaluation sources for tool-using and browser/computer-use agents.
- **owasp-2025-llm-top-10**, **owasp-2025-agentic-ai-threats-mitigations**, and **owasp-2025-securing-agentic-applications** — official OWASP LLM/agentic-app security standards for prompt injection, excessive agency, tool misuse, memory poisoning, privilege, HITL, identity, code execution, and supply-chain risks.
- **opentelemetry-2026-genai-semantic-conventions** — current OpenTelemetry GenAI/MCP semantic conventions for portable traces, metrics, events, tool spans, agent spans, and model-operation attributes.
- **deng-2025-swe-bench-pro**, **garg-2026-swe-bench-mutation**, **pan-2025-swe-gym**, and **wang-2025-swe-dev** — coding-agent benchmark realism, long-horizon tasks, executable training environments, synthetic test generation, trajectory scaling, verifier/inference-time-scaling evidence.
- **hubbard-2010-how-to-measure-anything**, **pearl-mackenzie-2018-the-book-of-why**, and **meadows-2008-thinking-in-systems** — decision-measurement, causal-claim, counterfactual, feedback-loop, and leverage-point gates for agents that need to make better metric, root-cause, intervention, or validation judgments.
- **maharana-2024-locomo-long-term-memory**, **hu-2025-memoryagentbench**, and **kang-2025-memoryos** — long-term memory benchmarks and typed-memory architecture references for vault-backed agents.
- **davis-2019-coding-agent-extraction** — cloud-native change, failure, configuration, routing, lifecycle, data, and observability rules.
- **jones-2023-coding-agent-extraction** — data-contract rules: producer/consumer boundaries, schema expectations, governance controls, contract evolution, and enforcement before data-pipeline changes.
- **jones-2023-ch2-data-contract-interface**, **jones-2023-ch6-7-schema-contract-architecture**, and **jones-2023-ch9-10-contract-adoption-practice** — deeper data-contract notes for boundary discovery, schema/governance architecture, and rollout/compatibility practice.
- **gift-deza-2021-coding-agent-extraction** — MLOps rules: CI/CD, model packaging, deployment contracts, drift monitoring, logs, rollback, and production ML ownership.
- **gift-deza-2021-ch1-4-mlops-lifecycle-delivery**, **gift-deza-2021-ch6-monitoring-logging-drift**, and **gift-deza-2021-ch10-11-interoperability-cli-services** — deeper MLOps notes for delivery lifecycle, model observability/drift, and artifact/service contracts.
- **data-contract-boundary**, **schema-evolution-contracts**, **mlops-production-readiness**, **model-drift-monitoring**, and **model-artifact-contract** — fast concept cards for agent decisions under tight context.
- **banks-porcello-2017-coding-agent-extraction**, **makarevich-2023-coding-agent-extraction**, and **roldan-2023-coding-agent-extraction** — React fundamentals, re-render/performance diagnosis, and production React patterns.
- **cooper-reimann-cronin-2007-coding-agent-extraction**, **kholmatova-2017-coding-agent-extraction**, **krug-2013-coding-agent-extraction**, **norman-2013-coding-agent-extraction**, **pickering-2019-coding-agent-extraction**, and **wathan-schoger-2018-coding-agent-extraction** — goal-directed UX, design systems, usability, human-centered design, accessibility, and visual hierarchy rules.

## Use Rules

- For architecture answers, cite at least one overview and one source-summary.
- For evaluation answers, open the evaluation page rather than relying only on index hooks.
- **Never report a benchmark delta as a result without an interval.** Per **miller-2024-adding-error-bars-to-evals**, pair the comparison at question level, cluster when questions share a stem, and power-check before building. Most small domain evals cannot resolve what they are used to decide.
- **Never recommend a general-purpose agent over untrusted data without naming the isolation pattern.** **beurer-kellner-2025-design-patterns-securing-llm-agents** holds that such agents cannot currently be made safe; if the pattern cannot be constrained, say the use case is unsafe rather than suggesting a better prompt.
- **Distinguish reasoning models from chat models as cost objects.** Thinking length grows on its own (**deepseek-2025-r1-reasoning-rl**); a per-request estimate built on chat behavior will be wrong by a multiple.
- For current OpenAI product behavior, use official current docs, not the vault.
- For coding-agent recommendations, distinguish benchmark design, agent interface design, repository-context retrieval, repair workflow, and eval methodology.
- For coding-agent implementation guidance, prefer the book extraction notes over raw book hubs; the hubs are navigation surfaces, while extraction notes carry operational rules.
- For non-trivial coding-agent answers or patches, use [[coding-agent-operating-card]] before acting and [[coding-agent-review-checklist]] before acceptance.
- For local project work, treat **project-context-manifests** as a routing hint, not evidence that the live repo still matches. Inspect the repo before claims.

## See Also

- [[question-router]]
- [[retrieval-pack-finops-cost-engineering]]
- **project-context-manifests**
- [[corpus-agent-evaluation-suite]]
