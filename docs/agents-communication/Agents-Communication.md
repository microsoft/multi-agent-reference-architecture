# Agents Communication

_Last updated: 2025-05-31_

This chapter introduces foundational communication paradigms central to
designing robust multi-agent systems: **request-based** and **event-driven**
architectures. The communication choices have significant implications for
system behavior and scalability.

- **Request-Based Communication**: In this model, client and agents interact
  through explicit, synchronous or asynchronous message exchanges—much like a
  client making an API request and waiting for a response. Typical protocols
  include HTTP, RPC (unary), or direct function calls within a process. This
  paradigm emphasizes predictable, traceable workflows and fine-grained control
  over interactions, often resulting in lower operational complexity for
  straightforward use cases.
- **Event-Driven Communication**: Here, client and agents respond to
  asynchronous events published to a message broker or event bus. One agent’s
  action emits an event (e.g., task completed, new message created), which
  interested agents and external systems consume and act upon. This approach
  enables loose coupling, reactive processing, high scalability, and
  extensibility—at the cost of increased system complexity, eventual
  consistency, and challenging debugging flows.

Hybrid approaches, where requests and events are combined, are common in
production-ready architectures, allowing development teams to balance control,
scalability, and extensibility according to use case and maturity.

This chapter will unpack the strengths, trade-offs, and practical considerations
of each model, and help you select or combine approaches aligned with your
agents’ roles, your SLA needs, and your team's operational capabilities.
