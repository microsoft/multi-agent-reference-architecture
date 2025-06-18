# Multi-Agent Reference Architecture

{{ #include components/stars-badge.hbs }}

[![GitHub stars](https://img.shields.io/github/stars/microsoft/multi-agent-reference-architecture?style=social)](https://github.com/microsoft/multi-agent-reference-architecture/stargazers)

This repository presents a conceptual guide, complemented by practical
resources, for architecting robust multi-agent systems. The focus is not on
building an individual agent, but on the unique challenges and effectiveness of
orchestrating, governing, and scaling systems where multiple specialized agents
interact to solve complex problems. You will find actionable guidance for
_designing for change_, balancing long-term extensibility with pragmatic,
shipping-first engineering.

The recommendations are grounded in production-scale, real-world solutions built
in collaboration with Microsoft customers. As such, the approaches offered in
this reference are both opinionated (benefiting from field experience) and
agnostic (applicable across enterprises, technology stacks, and frameworks).

This guide is intended for software architects, software engineers and data
scientists familiar with
[agentic services](https://www.anthropic.com/engineering/building-effective-agents)
design and development. It is aimed at those with experience in building and
deploying agents, whether they aim to extend existing systems to multi-agent
architectures or build them from the ground up.

> **Note:**  
> Generative AI is advancing rapidly, with new models, patterns, protocols and
> paradigms constantly emerging. While the current design is intentionally
> agnostic and broad, we expect to refine and improve it as the ecosystem
> matures.

If you want to jump straight to the architecture reference, check out the
[Reference Architecture](/docs/reference-architecture/Reference-Architecture.md)
chapter. Otherwise, if you'd like to explore the concepts and recommendations in
more detail, just keep reading the next chapters.

## Table of Content

- [Introduction](docs/Introduction.md)
- [Building blocks](docs/building-blocks/Building-Blocks.md)
- [Design options](./docs/design-options/Design-Options.md)
- [Agents registry](./docs/agent-registry/Agent-Registry.md)
- [Memory](./docs/memory/Memory.md)
- [Agents communication](docs/agents-communication/Agents-Communication.md)
- [Observability](docs/observability/Observability.md)
- [Security](docs/security/Security.md)
- [Governance](docs/governance/Governance.md)
- [Reference Architecture](/docs/reference-architecture/Reference-Architecture.md)
