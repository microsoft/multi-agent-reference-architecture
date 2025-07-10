# Tools Context for Agents

The ability to perform tasks and interact with external systems is what
transforms language models from passive responders into active problem solvers.
The design of those tools directly determines how effectively specialized agents
can reason about them and coordinate their use in multi-agent workflows.

This section provides recommended practices for designing tools that are
AI-friendly (descriptive and concise purposes and input/output formats),
avoiding common pitfalls such as over-granularity or hidden side effects that
can significantly influence reliable outcomes. These recommendations are crucial
for both orchestrator agents and specialized agents.

## Recommended practices

### 1. Handling Deterministic Logic

Contextual data that is static or deterministic (i.e. doesn't rely on the user
prompt), should be handled outside of language model interactions. For example:

- **Preloading user data and preferences**: Ensures context consistency and
  eliminates redundant queries.
- **Data validation, sorting, or filtering**: Simplifies downstream processing
  and ensures reliable data.
- **Computing results for business rules or domain-specific calculations**:
  Optimizes execution by reducing repetitive reasoning within the language
  model.

> Data can be dynamically injected into the language model instructions, or
> injected in the tool(s) within the lifecycle of the request. <br/><br/>Some
> models operations such as OpenAI Chat Completions offers a `metadata` field
> only used for conversation history storage, useful for evaluation and
> distillation (technique for tranining models with the outcomes of another
> model).

This approach provides the following benefits:

- **Enhanced Performance**: By preloading static and dynamic data, agents avoid
  unnecessary computation during runtime, ensuring faster execution.
- **Simplified Tool Design**: Tools become simpler and more focused on handling
  dynamic interactions.
- **Operational Cost Reduction**: Minimizes resource usage by avoiding redundant
  operations.
- **Scalability and Flexibility**: Both static and dynamic data can be
  efficiently managed across multiple agents or systems, enabling dynamic data
  updates without embedding them into language model interactions.

---

{{ #include ../../components/discuss-button.hbs }}
