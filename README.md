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

## Sequence diagrams

To support a clearer understanding of the architecture, the following
sequence diagrams illustrate key interactions:

* [Agent Registration Sequence Diagram](./docs/Multi-Agent-AgentRegistration-SequenceDiagram.md)
* [Conversational Sequence Diagram](./docs/Multi-Agent-Conversational-SequenceDiagram.md)
* [Agent to Agent Communication Patterns](./docs/Multi-Agent-Agent-to-Agent-Patterns-SequenceDiagram.md)

## Patterns

List of patterns that guided the proposed architecture.

1. Semantic Router + LLM Fallback
    Use a lightweight classifier for routing, escalate to LLM when uncertain

    -  lightweight model (NLU/SLM) as a first-pass classifier.
    -  If no confident match is found, it escalates to a full LLM.
    -  Reduces latency and cost while preserving accuracy.

2. Dynamic Agent Registry (Service Mesh for Agents)
    Register and resolve agents dynamically by capability, metadata, or embedding.

    - Allows plug-and-play agents and auto-scalable systems.

3. Semantic Kernel Orchestrator with Skills
    - The orchestrator (e.g., Semantic Kernel) enables chaining multiple “skills”/agents/functions with memory, planning, and context.

4. Local & Remote Agent Execution
    - Supervisor agent coordinates both local and remote agents.
    - Why it’s powerful: Scales execution beyond a single host or VNet, supporting federated deployments.

5. Separation of Concerns Across Layers (Onion Architecture for Agent Systems)
    Orchestration, Knowledge, Agent, Integration, and Storage are cleanly separated.

    - Improves maintainability, traceability, and testing.

6. MCP Integration for Agent-Tool Communication
    MCP server abstracts tool invocation from agents — giving a central, policy-controlled layer for agent-to-tool interactions.

    - Decouples logic from execution, adds governance.

7. RAG (Retrieval-Augmented Generation) Pipeline
    Vector DBs feed agents and orchestrators with contextual grounding data.

    - Keeps LLMs factual, grounded, and up-to-date.

8. Conversation-Aware Agent Orchestration (Contextual state + history memory)
    Conversation history and state influence routing decisions and agent behavior.

    - Enables continuity, personalization, and adaptive behaviors.
    - Long-Term | Short-Term Conversational Memory

9. Agent to Agent communication
    [Agent to Agent Communication Patterns](./docs/Multi-Agent-Agent-to-Agent-Patterns-SequenceDiagram.md)
