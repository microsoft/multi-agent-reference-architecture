# Multi-Agent Threat Model Worksheet

_Last updated: 2025-05-12_

This worksheet outlines potential threats and mitigation strategies for
multi-agent systems in enterprise environments. It follows the STRIDE
methodology (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of
Service, Elevation of Privilege).

---

## 1. Spoofing

**Threat:** Unauthorized agents impersonating trusted agents or orchestrators.
**Mitigation:**

- Use mutual TLS authentication.
- Enforce Azure AD or federated identity providers for agent registration.
- Sign agent registration payloads.

## 2. Tampering

**Threat:** Manipulation of agent messages, stored memory, or knowledge base
content. **Mitigation:**

- Use signed and encrypted communication channels.
- Enable integrity checks on state and registry storage.
- Log all message hashes for traceability.

## 3. Repudiation

**Threat:** Agents or orchestrators denying previous actions or interactions.
**Mitigation:**

- Enable end-to-end request logging with input/output hashes.
- Use distributed tracing with identity correlation.
- Store logs in write-once or append-only mediums.

## 4. Information Disclosure

**Threat:** Unintended access to sensitive information in memory, logs, or
vector data. **Mitigation:**

- Apply PII/PHI redaction pipelines.
- Scope memory persistence by session and user consent.
- Encrypt all data-at-rest and in-transit.

## 5. Denial of Service (DoS)

**Threat:** Overwhelming the orchestrator or agent with excessive requests.
**Mitigation:**

- Apply rate limiting per user/session.
- Use circuit breakers for agent services.
- Auto-scale orchestration layer with load protection.

## 6. Elevation of Privilege

**Threat:** An agent or user gaining access to unauthorized functions or tools.
**Mitigation:**

- Enforce RBAC on registry lookups and MCP tool invocations.
- Validate agent capability metadata before routing.
- Apply policy evaluation before task execution.

---

## Threat Prioritization Matrix

| Threat Category        | Likelihood | Impact | Priority |
| ---------------------- | ---------- | ------ | -------- |
| Spoofing               | Medium     | High   | High     |
| Tampering              | Medium     | Medium | Medium   |
| Repudiation            | Low        | Medium | Medium   |
| Information Disclosure | High       | High   | Critical |
| Denial of Service      | Medium     | High   | High     |
| Elevation of Privilege | High       | High   | Critical |

---

For implementation guidance and control validation, refer to the
[Security Architecture Guide](./Multi-agent-security.md).

---
<a class="github-button" href="https://github.com/microsoft/multi-agent-reference-architecture/discussions/new?category=q-a&body=Source: [Threat Model](https://github.com/microsoft/multi-agent-reference-architecture/blob/main/docs/security/Threat-Model.md)" data-icon="octicon-comment-discussion" target="_blank" data-size="large" aria-label="Discuss buttons/github-buttons on GitHub">Discuss this page</a>  <script async defer src="https://buttons.github.io/buttons.js"></script>