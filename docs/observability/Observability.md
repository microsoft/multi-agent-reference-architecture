# Observability

_Last updated: 2025-07-03_

## Multi-agent observability challenges

Building observable multi-agent systems requires expanding the traditional 
pillars of logs, metrics, and traces to address the unique challenges of AI. 
This involves capturing specialized signals such as agent actions, tool usage,
model invocations, and response patterns, to effectively debug, monitor, and 
optimize agent performance across key areas:

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

Observability gives us metrics, but **evaluation** is the process of analyzing
that data (and performing tests) to determine how well an AI agent is performing
and how it can be improved. In other words, once we have traces and metrics, how
we can use them to judge the agent and make decisions?

For AI evaluation strategies, see the
**[Evaluation](../evaluation/Evaluation.md)** section.

For reference:

- [Monitoring Generative AI applications](https://learn.microsoft.com/en-us/ai/playbook/technology-guidance/generative-ai/mlops-in-openai/monitoring/monitoring)
- [Observability in Semantic Kernel](https://learn.microsoft.com/en-us/semantic-kernel/concepts/enterprise-readiness/observability/)
- [Observability defined by CNCF](https://www.cncf.io/blog/2024/06/25/your-guide-to-observability-engineering-in-2024/)
- [Open Telemetry Signals Concepts](https://opentelemetry.io/docs/concepts/signals/)
- [What is OpenTelemetry?](https://opentelemetry.io/docs/what-is-opentelemetry/)
- [OpenTelemetry – an open standard for collecting telemetry data.](https://opentelemetry.io/)
- [What are evaluators? - Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/observability#what-are-evaluators)
- [Agent Evaluation in 2025: Complete Guide](https://orq.ai/blog/agent-evaluation)
- [AI Agent Observability and Evaluation](https://huggingface.co/learn/agents-course/bonus-unit2/what-is-agent-observability-and-evaluation)

---

{{ #include ../../components/discuss-button.hbs }}
