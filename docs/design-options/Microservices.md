# Agents as Microservices

In the microservices design, each component—such as the orchestrator and every
specialized agent—is encapsulated as an independent service running within its
own process, potentially on separate machines or cloud services. These agents
interact exclusively via well-defined APIs or messaging protocols. This
distributed approach is a natural fit for complex multi-agent systems where the
demands for scalability, maintainability, flexible technology stacks, and
deployment autonomy outweigh the operational overhead of distributed systems.

## Key Characteristics

- **Service Independence**: Each agent is developed, deployed, and scaled
  independently. Teams may choose distinct languages, frameworks, or even cloud
  platforms for each service.
- **Technology Flexibility**: Microservices enable teams to choose the most
  appropriate technologies for each service, rather than being constrained to a
  single tech stack. This allows agents developed by different teams—or even
  entirely separate organizations—to interoperate seamlessly. The architecture
  enables rapid innovation and the integration of specialized solutions tailored
  to the specific needs of each service.
- **Distributed Infrastructure**: Each service manages its own infrastructure
  resources (memory, storage, replicas), yet they collaborate through network
  communication (e.g. REST, gRPC, message queues).
- **Decentralized Governance**: Policy enforcement, agent governance, and
  versioning are implemented via inter-service contracts and registration
  protocols rather than assumed by process boundaries alone.
- **Observability across services**: Logs, traces, and metrics must be
  correlated across process and service boundaries for effective troubleshooting
  and monitoring.
