# Agents Communication

_Last updated: 2025-06-30_

This chapter introduces two foundational paradigms for agent interaction:
request-based and message-driven communication. These models shape how agents
coordinate, scale, and recover in distributed systems.

- [Request-Based Communication](./Request-Based.md): Agents communicate by
  sending direct requests to one another—through synchronous or asynchronous
  interactions— offering predictability and simplicity, making it well-suited
  for tightly coupled or latency-sensitive scenarios.
- [Message-Driven Communication](./Message-Driven.md): Agents communicate
  asynchronously via a broker or event bus, exchanging commands, events, or
  responses. This promotes loose coupling, scalability, and
  resilience—especially in distributed or dynamic environments.

Many systems adopt **hybrid models**, combining request-based communication with
asynchronous messaging to balance control, flexibility, and fault tolerance
(e.g. agents emitting events to be consumed by external systems).

This chapter outlines the strengths, trade-offs, and design considerations of
each approach to help you align communication strategies with your agents’ roles
and system goals.

---

{{ #include ../../components/discuss-button.hbs }}
