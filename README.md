# Multi-Agent Reference Architecture

This reference architecture is shaped by a combination of proven internal and external patterns. Internally, 
we draw from resources such as the [Azure Architecture Center](https://learn.microsoft.com/en-us/azure/architecture/), 
the [Azure Architecture Blog](https://techcommunity.microsoft.com/category/azure/blog/azurearchitectureblog), 
and the [Microsoft Developers Blog](https://devblogs.microsoft.com/). Externally, we
take inspiration from thought leaders like [Martin Fowler](https://martinfowler.com/architecture/)
and other influential sources.

We aim to contribute back to the community by sharing insights gained from implementing a
variety of [Agentic AI Systems](https://techcommunity.microsoft.com/blog/machinelearningblog/baseline-agentic-ai-systems-architecture/4207137)
and, more recently, Multi-Agent Systems (MAS). The architecture documented here
is grounded in real-world implementations across multiple Microsoft teams.

> Generative AI is evolving rapidly—new models, tools, and paradigms emerge weekly. One
> of our primary goals was to design a flexible architecture that can adapt to these
> changes. While the current structure is intentionally generic, we expect to revise
> and evolve it over time as the ecosystem matures.

## Architecture

The architecture below illustrates a modular and governed multi-agent system, supporting
both local and remote agents through a central orchestration layer. At its core, 
the Orchestrator (e.g., Semantic Kernel) coordinates agent interactions, consults a classifier
for intent routing, and uses a registry for agent discovery and lifecycle management.
The system integrates with knowledge bases and vector databases, and maintains context
and state through a persistent storage layer. Integration with external tools is supported
through an MCP (multi-channel protocol) server. This design ensures flexibility, extensibility, 
and strong control boundaries between components, allowing seamless onboarding
of new models, tools, and communication patterns.

![Architecture Diagram](./docs/Multi-Agent-Architecture.drawio.svg)

## Sequence diagram

To support a clearer understanding of the architecture, the following
sequence diagram illustrate key interactions:

* [Conversational Sequence Diagram](./docs/Multi-Agent-Conversational-SequenceDiagram.md)

## Patterns

Below are the most foundational patterns that shaped this architecture.
For a complete catalog of design patterns used across scenarios, 
visit the [Full Pattern Reference](./docs/Multi-Agent-Patterns.md).

List of patterns that guided the proposed architecture.

1. Semantic Router + LLM Fallback
2. Dynamic Agent Registry (Service Mesh for Agents)
3. Semantic Kernel Orchestrator with Skills
4. Local & Remote Agent Execution
5. Separation of Concerns Across Layers (Onion Architecture for Agent Systems)
6. MCP Integration for Agent-Tool Communication
7. RAG (Retrieval-Augmented Generation) Pipeline
8. Conversation-Aware Agent Orchestration (Contextual state + history memory)
9. Agent to Agent communication
    [Agent to Agent Communication Patterns](./docs/Multi-Agent-Agent-to-Agent-Patterns-SequenceDiagram.md)

## Security Principles

Security is embedded into the architecture at every layer—from identity enforcement
and data protection to policy-controlled agent execution. A detailed breakdown
is provided in the [Security Architecture Guide](./docs/Multi-Agent-Security.md).

Key considerations include:
* Identity-bound orchestration and agent execution.
* Registry authorization and capability scoping.
* Data retention policies tied to storage layers.
* Tool execution mediated through policy-controlled MCP integration.
