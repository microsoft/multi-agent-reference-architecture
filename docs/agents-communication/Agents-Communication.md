# Agents Communication
_Last updated: 2025-05-15_

As the ecosystem of AI agents rapidly evolves, new protocols are emerging to
support diverse communication needs, security models, and integration patterns.
These protocols—ranging from centralized to fully decentralized approaches—are
designed to enhance agent interoperability, task delegation, and tool
integration.

Rather than prescribing a single standard, we recommend adopting the protocol
that best aligns with your intended usage scenario. Whether you're building
tool-augmented agents, enabling peer-to-peer collaboration, or orchestrating
enterprise workflows, choosing the right protocol ensures both scalability and
operational efficiency. See the
[Agent-to-Agent Communication pattern](../reference-architecture/Patterns.md#9-agent-to-agent-communication)
for more details on agent communication.

## Model Context Protocol (MCP)

[Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) is
an open protocol that standardizes how applications provide context to LLMs it
follows a client-server model using JSON-RPC for structured communication.

_Functionality_: Enables LLMs to interact with external tools, APIs, and
datasets.

_Features_: Supports predefined prompts and toolset.

_Security_: Primarily token-based, with optional support for Decentralized
Identifiers (DIDs) for authentication.

_State_: Stateless by default, but can maintain persistent tool context when
needed.

_Use Case_: Seamlessly connect AI agents to various tools through lightweight
server integration.

If you want to explore it in more detail check
[unleash the power of model context protocol](https://techcommunity.microsoft.com/blog/educatordeveloperblog/unleashing-the-power-of-model-context-protocol-mcp-a-game-changer-in-ai-integrat/4397564)

## Agent-to-Agent Protocol (A2A)

[Agent-to-Agent Protocol (A2A)](https://a2aprotocol.ai/) is an open standard
that enables AI agents to communicate and collaborate across different platforms
and frameworks, regardless of their underlying technologies

Enables direct communication between clients and remote agents.

_Discovery_: Uses Agent Cards (JSON metadata) for exposing capabilities.

_Security_: Employs DIDs for trusted, secure authentication.

_Communication_: Supports Server-Sent Events (SSE) and push notifications for
real-time, asynchronous interactions.

_Use Case_: Dynamically delegate tasks across specialized agents to build
expert-driven, distributed workflows.

Usage example with Semantic Kernel -
[Semantic Kernel A2A integration](https://devblogs.microsoft.com/foundry/semantic-kernel-a2a-integration/)

## Other emerging protocols

- [Agent Network Protocol (ANP)](https://agent-network-protocol.com/)

- [Agent Communication Protocol (ACP)](https://agentcommunicationprotocol.dev/introduction/welcome)
