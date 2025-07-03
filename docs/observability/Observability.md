# Observability

_Last updated: 2025-07-03_

Observability is the capability to understand the internal state of a system
based solely on its external outputs. This is not just about identifying when
something breaks, but understanding why.

Traditional observability relies on three foundational pillars:

- **Logs**: Discrete events and contextual information about system operations
- **Metrics**: Numerical data points indicating system health and usage
- **Traces**: End-to-end visibility into request flows across services or agents

## Multi-agent observability challenges

Building observable multi-agent systems requires extending this pillars to
address unique AI challenges capturing signals across the following core areas:

- **[Agent Communication](./agent-communication.md)**: Tracking inter-agent
  message flows, coordination patterns, and communication bottlenecks
- **[Performance Monitoring](./performance-monitoring.md)**: Measuring response
  times, resource utilization, and throughput across distributed agents
- **[Error Handling](./error-handling.md)**: Detecting failures, cascading
  errors, and recovery mechanisms in agent workflows
- **[Security & Compliance](./security-compliance.md)**: Monitoring for
  unauthorized access, data leaks, and regulatory compliance across agent
  interactions

### Evaluation-Driven Observability

**Evaluators** are a systematic approach to assessing agent behavior across
controlled inputs, edge cases, and expected outcomes. They provide quantitative
metrics such as relevance, factual accuracy, and tool call precision, supporting
validation during development and regression testing.

When integrated into production, **evaluators** enable observability-driven
assessments, extending traditional telemetry with runtime quality signals. This
allows for detection of behavior drift, degraded output quality, and performance
regressions that are not captured by logs or infrastructure metrics alone.

For AI evaluation strategies, see the **[Evaluation](../evaluation/)** section.

For reference:

- [Monitoring Generative AI applications](https://learn.microsoft.com/en-us/ai/playbook/technology-guidance/generative-ai/mlops-in-openai/monitoring/monitoring)
- [Observability in Semantic Kernel](https://learn.microsoft.com/en-us/semantic-kernel/concepts/enterprise-readiness/observability/)
- [Observability defined by CNCF](https://www.cncf.io/blog/2024/06/25/your-guide-to-observability-engineering-in-2024/)
- [Open Telemetry Signals Concepts](https://opentelemetry.io/docs/concepts/signals/)
- [What is OpenTelemetry?](https://opentelemetry.io/docs/what-is-opentelemetry/)
- [OpenTelemetry – an open standard for collecting telemetry data.](https://opentelemetry.io/)
- [What are evaluators? - Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/observability#what-are-evaluators)
- [Agent Evaluation in 2025: Complete Guide](https://orq.ai/blog/agent-evaluation)

---

{{ #include ../../components/discuss-button.hbs }}
