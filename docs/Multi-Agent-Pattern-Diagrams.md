# Architecture Patterns Companion

This companion document provides diagrammatic representations of core patterns
described in the Multi-Agent Reference Architecture. Each sequence or component
diagram illustrates how patterns operate in practice.

---

## 1. Semantic Router with LLM Fallback

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

---

## 2. RAG Pipeline with Vector DB

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

---

## 3. Agent Registry and Discovery

```mermaid
sequenceDiagram
    participant Agent
    participant Registry
    participant Orchestrator

    Agent->>Registry: Register(metadata, capabilities)
    Orchestrator->>Registry: Discover agents by capability
    Registry-->>Orchestrator: Matching agent endpoints
```

---

## 4. Agent-to-Agent Communication

```mermaid
sequenceDiagram
    participant Agent A
    participant Orchestrator
    participant Agent B

    Agent A->>Orchestrator: Request delegation
    Orchestrator->>Agent B: Forward task
    Agent B-->>Orchestrator: Result
    Orchestrator-->>Agent A: Return result
```

---

## 5. Orchestration with Skill Chaining

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

More diagrams will be added as additional patterns are implemented or refined. For feedback or contributions, visit the project repo or contact the maintainers.
