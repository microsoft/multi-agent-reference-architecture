# Tools Context for Agents

_Last updated: 2025-07-14_

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

### 2. Balancing Tool Granularity and Responsibility

Developers tend to adopt the Single Responsibility Principle (SRP), a common
practice in traditional software development, to design tools that perform one
specific task. While this approach promotes clarity and reusability, it can
introduce processing overhead for language models, including increased reasoning
complexity, higher token consumption, and additional network latency due to
multiple tool invocations.

On the other side of the spectrum, designing a single tool to handle multiple
responsibilities can reduce overhead but often leads to decreased reusability,
increased implementation complexity, and a higher risk of parameter mismatches
or incorrect assumptions by the model.

### Recommendations

- **Group closely related responsibilities:** Combine tasks that are frequently
  used together or share similar input/output structures into a single tool to
  minimize overhead.
- **Avoid excessive generalization:** Do not overload tools with unrelated
  responsibilities, as this can make them harder to maintain and use correctly.
- **Optimize for model reasoning:** Consider how the language model selects and
  uses tools. Overly granular tools may increase reasoning steps, while overly
  broad or generic tools may confuse parameter mapping.
- **Monitor usage patterns:** Analyze tool invocation logs to identify
  bottlenecks or frequent multi-tool workflows that could be streamlined.
- **Iterate and test:** Continuously refine tool boundaries based on real-world
  usage and model performance, aiming for a balance between efficiency and
  clarity. The previous
  [Iterative Optimization Loop](./Iteractive-Optimization-Loop.md) section
  offers a plan to do this in a structured way.

> The
> [Semantic Kernel: Make plugins AI-friendly](https://learn.microsoft.com/en-us/semantic-kernel/concepts/plugins/?pivots=programming-language-python#make-plugins-ai-friendly)
> documentation gives an agnostic view of recommendations to design clear and
> concise tool schemas for language models.

---

{{ #include ../../components/discuss-button.hbs }}
