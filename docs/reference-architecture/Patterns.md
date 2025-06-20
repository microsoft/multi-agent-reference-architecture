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

```mermaid
sequenceDiagram
    title Semantic Kernel Orchestration with Skills

    participant User
    participant Orch as SK-Orchestrator
    participant Memory
    participant Planner
    participant Goal
    participant SkillA as Skill: Search
    participant SkillB as Skill: Summarize
    participant SkillC as Skill: Recommend

    User->>Orch: Submit query / task
    Orch->>Memory: Retrieve context
    Memory-->>Orch: Return relevant memory

    Orch->>Planner: Analyze task and context
    Planner-->>Orch: Return skill execution plan

    Orch->>Goal: Evaluate intent and goal alignment
    Goal-->>Orch: Confirm objective

    Orch->>SkillA: Execute Skill: Search
    SkillA-->>Orch: Return search results

    Orch->>SkillB: Execute Skill: Summarize
    SkillB-->>Orch: Return summary

    Orch->>SkillC: Execute Skill: Recommend
    SkillC-->>Orch: Return recommendation

    Orch-->>User: Deliver final result
```

## 4. Local & Remote Agent Execution

**Federated agent model with supervisor coordination.**

- Local supervisor delegates tasks to local or remote agents.
- Secure channels maintain observability and traceability.
- Benefit: Enables scalability across networks or geographies.

```mermaid
sequenceDiagram
    title Local & Remote Agent Execution
    participant User
    participant UserApp as User Application
    participant Orch as SK-Orchestrator
    participant Class as Classifier
    participant Super as Supervisor Agent
    participant AgReg as Agent Registry
    participant Agent1 as Agent 1 (Local)
    participant Agent2 as Agent 2 (Remote)
    participant KnowL as Knowledge Layer
    participant StorL as Storage Layer
    
    User->>UserApp: 1. Submit complex query
    UserApp->>Orch: 2. Forward request
    Orch->>StorL: 3. Load conversation history
    StorL-->>Orch: 4. Return context
    Orch->>Class: 5. Classify query
    Class->>Class: 6. Determine multi-agent needed
    Class->>AgReg: 7. Get matching agents
    AgReg-->>Class: 8. Return Agents 1 & 2
    Class-->>Orch: 9. Return classification
    
    Orch->>Orch: 10. Allocate context window
    Orch->>Super: 11. Coordinate multi-agent task
    Super->>Super: 12. Decompose task
    Super->>Agent1: 13. Process part 1
    Super->>Agent2: 14. Process part 2
    
    Agent1->>KnowL: 15. Query knowledge
    KnowL-->>Agent1: 16. Return information
    Agent2->>KnowL: 17. Query knowledge
    KnowL-->>Agent2: 18. Return information
    
    Agent1->>Agent1: 19. Generate response 1
    Agent2->>Agent2: 20. Generate response 2
    Agent1-->>Super: 21. Return part 1
    Agent2-->>Super: 22. Return part 2
    
    Super->>Super: 23. Merge responses
    Super->>Super: 24. Synthesize final response
    Super-->>Orch: 25. Return unified response
    
    Orch->>StorL: 26. Store interaction
    StorL-->>Orch: 27. Acknowledge
    Orch-->>UserApp: 28. Return response
    UserApp-->>User: 29. Display answer
```

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

```mermaid
sequenceDiagram
    title MCP Integration Layer – Decoupled Agent-to-Investment Tool Invocation

    participant Agent as Agent (e.g. Investment Advisor)
    participant MCP as MCP Server
    participant Policy as Policy Engine
    participant Tool as Tool API (e.g. StockQuotes, RiskAnalysis)
    participant Audit as Audit Log

    Agent->>MCP: Request to invoke "GetStockQuote" tool (e.g. for AAPL)
    MCP->>Policy: Evaluate access rules and validate parameters
    Policy-->>MCP: Access granted with constraints

    MCP->>Tool: Call StockQuotes API with validated input
    Tool-->>MCP: Return quote data (price, volume, trend)

    MCP->>Audit: Log tool invocation and response
    MCP-->>Agent: Return investment data result
```

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

{{ #include ../../components/discuss-button.hbs }}
