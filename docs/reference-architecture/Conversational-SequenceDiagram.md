# A Conversational Sequence Diagram

_Last updated: 2025-05-16_

```mermaid
sequenceDiagram
    participant User
    participant UserApp as User Application
    participant Orch as Orchestrator
    participant Class as Classifier
    participant AgReg as Agent Registry
    participant Super as Supervisor Agent
    participant Agent1 as Agent 1 (Local)
    participant Agent2 as Agent 2 (Local)
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
    Orch->>Super: 11. Send user's request & agents info to be invoked
    Super->>Super: 12. Decompose request based on agents' domains
    Super->>Agent1: 13. Request within agent 1 domain
    Super->>Agent2: 14. Request within agent 2 domain

    Agent1->>KnowL: 15. Query knowledge
    KnowL-->>Agent1: 16. Return information
    Agent2->>KnowL: 17. Query knowledge
    KnowL-->>Agent2: 18. Return information

    Agent1->>Agent1: 19. Generate response Agent 1
    Agent2->>Agent2: 20. Generate response Agent 2
    Agent1-->>Super: 21. Return response Agent 1
    Agent2-->>Super: 22. Return response Agent 2

    Super->>Super: 23. Merge responses
    Super->>Super: 24. Synthesize final response
    Super-->>Orch: 25. Return unified response

    Orch->>StorL: 26. Store interaction
    StorL-->>Orch: 27. Acknowledge
    Orch-->>UserApp: 28. Return response
    UserApp-->>User: 29. Display answer
```

---

<a class="github-button" href="https://github.com/microsoft/multi-agent-reference-architecture/discussions/new?category=q-a&body=Source: [Conversational Sequencediagram](https://github.com/microsoft/multi-agent-reference-architecture/blob/main/docs/reference-architecture/Conversational-SequenceDiagram.md)" data-icon="octicon-comment-discussion" target="_blank" data-size="large" aria-label="Discuss buttons/github-buttons on GitHub">Discuss this page</a>

<script async defer src="https://buttons.github.io/buttons.js"></script>
