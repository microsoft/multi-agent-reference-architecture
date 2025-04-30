# multi-agent-reference-architecture
Enterprise-ready reference architecture for building scalable multi-agent systems. 

## Architecture

The architecture is embodying actual project implementations
being executed by different teams at Microsoft.

![Architecture Diagram](./docs/Multi-Agent-Architecture.drawio.svg)

## Sequence diagrams

For better understanding there are a set of sequence diagrams that covers:

[Agent Registration Sequence Diagram](./docs/Multi-Agent-AgentRegistration-SequenceDiagram.md)

[Conversational Sequence Diagram](./docs/Multi-Agent-Conversational-SequenceDiagram.md)

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
    