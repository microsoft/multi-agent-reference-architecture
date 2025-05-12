# Multi-Agent Reference Architecture

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

## Table of Content

- [Introduction](./src/docs/Introduction.md)
- [Building blocks](./src/docs/building-blocks/README.md)
- [Agents communication](./src/docs/agents-communication/README.md)
- [Observability](./src/docs/observability/README.md)
- [Security](./src/docs/security/README.md)
- [Governance](./src/docs/governance/README.md)
