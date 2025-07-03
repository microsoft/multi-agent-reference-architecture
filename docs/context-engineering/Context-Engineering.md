# Context Engineering

_Last updated: 2025-07-03_

In Generative AI, `context` is the information a language model uses to guide
its outputs, such as instructions, memory, and external data. Context
engineering is the practice of designing, preparing, and managing this
information to shape model behavior and results.

Context engineering is especially critical in multi-agent systems, where
multiple agents collaborate to solve complex tasks. In these environments, every
improvement in context quality and data volume is amplified: even small gains
from an agent can have a significant impact as the number of agents increases.
Well-optimized context not only enhances individual agent effectiveness but also
drives overall system efficiency and scalability.

Crafting and delivering the most relevant context to each agent is essential for
achieving high-quality, efficient, and cost-effective results. This chapter
introduces strategies for optimizing context, focusing on two main objectives:

- **Minimizing irrelevant content:** Filter out outdated, redundant, or noisy
  information to reduce misleading results, token usage, costs, and latency.

- **Maximizing usefulness for each agent:** Curate and structure context to
  prioritize relevant, actionable, and timely information—such as recent or
  high-confidence data, summaries, or dynamically adapted content—empowering
  agents to make better decisions.

> In some cases, further optimization can be achieved by delegating tasks to
> simpler or more efficient components instead of language models.

Effective context optimization improves response quality, reduces computational
overhead, and enables scalable, collaborative multi-agent systems. This chapter
provides practical techniques to help engineering teams balance context richness
with efficiency:

- [Iteractive Optimization Loop](./Iteractive-Optimization-Loop.md)
- [Agents orchestration](./Agents-Orchestration.md)
- [Tools](./Tools.md)

---

{{ #include ../../components/discuss-button.hbs }}
