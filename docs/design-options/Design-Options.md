# Multi-agent Design Options

_Last updated: 2025-05-15_

This chapter explores architectural strategies for building multi-agent systems.
Here we break down two primary design approaches:

- **Modular Monolith**: A standalone application where orchestrator and
  specialized agents are organized as well-defined modules. This approach
  emphasizes simplicity, shared memory, and low-latency communication.
- **Microservices**: A distributed system where each agent (or group of agents)
  is encapsulated as a service. This model enables independent deployment,
  granular scalability and flexibility to use different tools, frameworks, or
  programming languages for each service.

Each approach has trade-offs in terms of performance, scalability,
maintainability, team coordination, and operational complexity. This
documentation explores those trade-offs and offers guidance to help you choose
and implement the right architecture for your multi-agent system—based not only
on technical goals, but also on your organization's structure and team dynamics.

---

<a class="github-button" href="https://github.com/microsoft/multi-agent-reference-architecture/discussions/new?category=q-a&body=Source: [{{selftitle}}](https://github.com/microsoft/multi-agent-reference-architecture/blob/main/{{selfpath}})" data-icon="octicon-comment-discussion" target="_blank" data-size="large" aria-label="Discuss buttons/github-buttons on GitHub">Discuss this page</a>

<script async defer src="https://buttons.github.io/buttons.js"></script>
