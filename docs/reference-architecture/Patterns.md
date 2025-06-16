# Multi-Agent Patterns Reference

_Last updated: 2025-05-14_

This document catalogs key design patterns used in the Multi-Agent Reference
Architecture. Each pattern contributes to the system's modularity, scalability,
governance, or performance.

## 1. Semantic Router with LLM Fallback

**Intent-based routing optimized for cost and performance.**

- Use a lightweight NLU or SLM classifier for initial routing.
- If classifier confidence is low, escalate to a more expensive LLM.
- Benefit: Reduces LLM usage while maintaining accuracy.

```mermaid
sequenceDiagram
    participant User
    participant Orchestrator
    participant NLU
    participant LLM

    User->>Orchestrator: Send query
    Orchestrator->>NLU: Classify intent
    alt Confident match
        NLU-->>Orchestrator: Intent Label
        Orchestrator-->>Agent: Route to matched agent
    else Low confidence
        Orchestrator->>LLM: Generate best-match intent
        LLM-->>Orchestrator: Intent Label
        Orchestrator-->>Agent: Route to matched agent
    end
```

## 2. Dynamic Agent Registry (Service Mesh for Agents)

**Agent discovery based on capabilities and metadata.**

- Agents register with descriptors (capabilities, tags, embeddings).
- Registry supports runtime resolution by orchestrator.
- Benefit: Supports plug-and-play extensibility and self-healing behavior.

```mermaid
sequenceDiagram
    participant Admin as Admin
    participant AdminApp as Admin Interface
    participant Orch as Orchestrator
    participant AgReg as Agent Registry
    participant ValM as Evaluation
    participant Agent3 as Agent
    participant StorL as Storage Layer

    Admin->>AdminApp: Request to register new agent
    AdminApp->>Orch: Send registration request
    Orch->>+AgReg: Forward registration request
    AgReg->>AgReg: Generate agent ID and credentials
    AgReg->>Agent3: Probe agent endpoint
    Agent3-->>AgReg: Return capability manifest
    AgReg->>AgReg: Validate schema compliance
    AgReg->>AgReg: Check security requirements
    AgReg->>StorL: Store agent metadata
    StorL-->>AgReg: Confirm storage
    AgReg->>+ValM: Evaluate new configuration
    ValM->>StorL: Request Evaluation Data Set
    StorL-->>ValM: Evaluation Data Set
    loop Orchestration Evaluation
        ValM->>Agent3: Submit prompt
        Agent3-->>ValM: Response
    end
    ValM-->>-AgReg: Evaluation response

    alt Evaluation Passed
        AgReg->>Agent3: Send registration confirmation
        Agent3-->>AgReg: Acknowledge registration
        AgReg->>StorL: Update registry storage
        StorL-->>AgReg: Confirm update
    else Evaluation Not Passed
        AgReg->>Agent3: Send registration Denied
        Agent3-->>AgReg: Acknowledge registration Denied
        AgReg->>StorL: Update storage
        StorL-->>AgReg: Confirm update
    end
    AgReg-->>-Orch: Return registration status
    Orch-->>AdminApp: Report registration status
    AdminApp-->>Admin: Display confirmation and agent details
```

## 3. Semantic Kernel Orchestration with Skills

**Composable orchestration using reusable agent capabilities.**

- Each "skill" encapsulates an agent function.
- Orchestrator chains skills with memory, planning, and goals.
- Benefit: Encourages modular and context-aware execution.

## 4. Local & Remote Agent Execution

**Federated agent model with supervisor coordination.**

- Local supervisor delegates tasks to local or remote agents.
- Secure channels maintain observability and traceability.
- Benefit: Enables scalability across networks or geographies.

## 5. Layered (Onion) Architecture

**Separation of concerns by functional domain.**

- Layers include Orchestration, Agent, Knowledge, Storage, Integration.
- Each layer has bounded responsibilities and APIs.
- Benefit: Improves maintainability, scalability, and testability.

## 6. MCP Integration Layer

**Decoupled agent-to-tool invocation with governance.**

- MCP server abstracts tool APIs from agents.
- Policies control access, parameters, and invocation flow.
- Benefit: Adds auditability, policy enforcement, and centralized logic.

## 7. RAG (Retrieval-Augmented Generation)

**Enhancing responses with contextual data from vector stores.**

- Pre-indexed content stored in vector DBs.
- Orchestrator and agents query for grounding facts.
- Benefit: Improves factual accuracy and reduces hallucination.

```mermaid
sequenceDiagram
    participant Agent
    participant VectorDB
    participant Knowledge Store
    participant LLM

    Agent->>VectorDB: Query embeddings
    VectorDB-->>Agent: Top-k docs
    Agent->>LLM: Compose prompt with documents
    LLM-->>Agent: Factual response
```

## 8. Conversation-Aware Orchestration

**Adaptive behavior based on memory and context.**

- Conversation history is stored and retrieved by orchestrator.
- Agents can use long-term and short-term memory cues.
- Benefit: Supports personalization, continuity, and context-awareness.

## 9. Agent-to-Agent Communication

**Cooperative task delegation between agents.**

- Agents interact via orchestrator or directly through scoped protocols.
- Registry tracks active agents and routing preferences.
- Benefit: Supports delegation, specialization, and parallelization.

```mermaid
sequenceDiagram
    participant Orch as Orchestrator
    participant Agent1
    participant Agent2
    participant Agent3
    participant Stor as Storage
    participant MQ as Message Queue

    %% --- Pattern 1: Orchestrator Mediated Communication ---
    Note over Agent1,Agent2: Pattern 1: Orchestrator Mediated
    Agent1->>Orch: Request info from Agent 2
    Orch->>Agent2: Forward request to Agent 2
    Agent2-->>Orch: Send response
    Orch->>Stor: Log inter-agent communication
    Orch-->>Agent1: Forward response to Agent 1

    %% --- Pattern 2: Direct via Stdin/out or A2A with Notification to Orchestrator ---
    Note over Agent1,Agent3: Pattern 2: Direct (Stdin/Stdout or A2A) with Orchestrator Notification
    Agent1->>Orch: Notify intent to contact Agent 3 (Remote)
    Orch->>Agent1: Approve direct communication
    Agent1->>Agent3: Direct request (via stdin/out or A2A)
    Agent3-->>Agent1: Direct response
    Agent1->>Orch: Report interaction completion
    Orch->>Stor: Log interaction

    %% --- Pattern 3: Pub/Sub Communication ---
    Note over Agent1,MQ: Pattern 3: Pub/Sub Messaging
    Agent1->>MQ: Publish message (topic: data_request)
    MQ->>Agent2: Subscribed agent receives message
    Agent2->>MQ: Publish response
    MQ->>Agent1: Deliver response
    MQ->>Stor: Log all communications
```

## 10. Skill Chaining with Planning Support

**Goal-oriented execution via automatic chaining of capabilities.**

- Planner creates execution path from available skills.
- Each skill is stateless, composable, and memory-aware.
- Benefit: Unlocks complex multi-step interactions.

```mermaid
sequenceDiagram
    participant Orchestrator
    participant Skill 1
    participant Skill 2
    participant Memory

    Orchestrator->>Memory: Load context
    Orchestrator->>Skill 1: Execute
    Skill 1-->>Orchestrator: Output 1
    Orchestrator->>Skill 2: Execute
    Skill 2-->>Orchestrator: Output 2
    Orchestrator->>Memory: Save updated context
```

---

<a class="github-button" href="https://github.com/microsoft/multi-agent-reference-architecture/discussions/new?category=q-a&body=Source: [Patterns](https://github.com/microsoft/multi-agent-reference-architecture/blob/main/{{selfpath}})" data-icon="octicon-comment-discussion" target="_blank" data-size="large" aria-label="Discuss buttons/github-buttons on GitHub">Discuss this page</a>

<script async defer src="https://buttons.github.io/buttons.js"></script>
