# Observability

_Last updated: 2025-07-01_

Observability is the capability to understand the internal state of a system
based solely on its external outputs. This is not just about identifying when
something breaks, but understanding why.

Traditional observability relies on three foundational pillars:

- **Logs**: Discrete events and contextual information about system operations
- **Metrics**: Numerical data points indicating system health and usage
- **Traces**: End-to-end visibility into request flows across services or agents

As AI solutions evolve into complex distributed systems, especially multi-agent
architectures, they introduce unique challenges that require extending the
observability practices. How do you validate non-deterministic outputs? How do
you prevent AI-generated problems?

This new context require a fourth pillar: **evaluators**. Evaluators complement
traditional telemetry by providing systematic assessment of AI behavior, output
quality, and decision-making processes. They enable engineering teams to apply
fundamental principles such as:

- **Reliability Engineering**: Ensuring consistent, predictable AI behavior
  across different scenarios and workloads
- **Quality Assurance**: Systematic validation of AI outputs against expected
  standards and business requirements
- **Safety by Design**: Proactive identification and mitigation of harmful or
  inappropriate AI responses
- **Continuous Improvement**: Data-driven feedback loops for model and system
  optimization

Together, traditional observability pillars and evaluators form a comprehensive
framework that enables real-time assessment of both system behavior and AI
output quality. This holistic approach is critical for AI systems, enabling
proactive monitoring, faster incident response, and continuous validation of AI
reliability and safety.

For reference:

- [Monitoring Generative AI applications](https://learn.microsoft.com/en-us/ai/playbook/technology-guidance/generative-ai/mlops-in-openai/monitoring/monitoring)
- [Observability in Semantic Kernel](https://learn.microsoft.com/en-us/semantic-kernel/concepts/enterprise-readiness/observability/)
- [Observability defined by CNCF](https://www.cncf.io/blog/2024/06/25/your-guide-to-observability-engineering-in-2024/)
- [Open Telemetry Signals Concepts](https://opentelemetry.io/docs/concepts/signals/)
- [What is OpenTelemetry?](https://opentelemetry.io/docs/what-is-opentelemetry/)
- [OpenTelemetry – an open standard for collecting telemetry data.](https://opentelemetry.io/)
- [What are evaluators? - Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/observability#what-are-evaluators)

---

{{ #include ../../components/discuss-button.hbs }}
