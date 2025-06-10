# Memory

_Last updated: 2025-05-18_

Memory is a foundational aspect of multi-agent systems, shaping how agents
understand context, make decisions, and collaborate effectively. This chapter
introduces two core memory types in multi-agent systems:

- **Short-term Memory (STM):** Enables agents to maintain recent context within
  an active session (also known as conversation history), supporting coherent
  interaction and task coordination across agents.
- **Long-term Memory (LTM):** Provides persistence of information across
  sessions, allowing agents to recall knowledge, preferences, and outcomes over
  time to provide personalized experiences.

Designing STM and LTM in multi-agent systems brings unique challenges around
synchronization, ownership, privacy, and data consistency. The following
sections outline key patterns and trade-offs for integrating effective memory
into your architecture.

---

<a class="github-button" href="https://github.com/microsoft/multi-agent-reference-architecture/discussions/new?category=q-a&body=Source: [Memory](https://github.com/microsoft/multi-agent-reference-architecture/blob/main/docs/memory/Memory.md)" data-icon="octicon-comment-discussion" target="_blank" data-size="large" aria-label="Discuss buttons/github-buttons on GitHub">Discuss this page</a>

<script async defer src="https://buttons.github.io/buttons.js"></script>
