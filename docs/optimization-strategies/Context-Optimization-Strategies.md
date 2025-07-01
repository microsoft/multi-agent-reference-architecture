# Context Optimization Strategies

_Last updated: 2025-07-01_

In multi-agent systems powered by language models, the way context is crafted
and delivered to each agent is critical for achieving high-quality, efficient,
and cost-effective outcomes. This chapter explores a set of strategies for
optimizing the external context passed to language models, with two primary
objectives:

- **Minimizing irrelevant content** by filtering out outdated, redundant, or
  noisy information to reduce misleading results, token usage, costs, and
  latency.

- **Maximizing usefulness for each agent** by curating and structuring context
  to prioritize relevant, actionable, and timely information—such as recent or
  high-confidence data, summaries, or dynamically adapted content—empowers
  agents to make better decisions and contribute more effectively.

In some scenarios, further optimization is possible by delegating tasks to
simpler or more efficient components instead of language models.

Effective context optimization improves response quality, reduces computational
overhead, and enables architects to design scalable, collaborative, and
efficient multi-agent workflows. Through practical techniques and real-world
examples, this chapter shows how engineering teams can balance context richness
with efficiency to deliver timely, and cost-effective results.
