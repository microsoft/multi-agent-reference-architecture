# Tool Call Evaluation

_Last updated: 2025-10-21_

This document outlines the importance of evaluating tool usage. It defines the
characteristics of successful tool invocations, and strategies to assess
their correctness and alignment with intended behavior.

## Overview

In agent-based architectures, **tool calls** represent the bridge between
reasoning and action.

Evaluate this steps is essential for understanding how well the agent
translates intent into action, whether it invokes the appropriate tool, and if
the execution contributes meaningfully to solving the user's request.

## Core Aspects to Evaluate

Tool call evaluation should consider multiple dimensions beyond traditional
accuracy metrics:

### 1. **Correctness of Invocation**

* Did the agent choose the expected tool/function/module?
* Were the arguments valid, complete, and well-formed?
* Was the call executed without runtime failure?

### 2. **Intent Alignment**

* Does the selected tool match the user's request or goal?
* Could another tool have fulfilled the intent more effectively?
* Does the call reflect appropriate use of system capabilities?

### 3. **Context Awareness**

* Did the agent account for the conversation history or prior tool outputs?
* Were dependencies between multi-step calls respected?

### 4. **Robustness and Fallibility**

* How does the agent behave when a tool is unavailable or fails?
* Does it recover gracefully, retry, or escalate?

### 5. **Reasoning Traceability**

* Is the rationale behind the tool choice observable from logs or metadata?
* Can the evaluation system distinguish between strategic use vs random invocation?

## Example Scenarios

Tool call evaluation can be applied in various operational contexts:

* **Simple invocation**: Agent correctly calls a REST API with the expected
endpoint and parameters.
* **Multi-turn planning**: Agent chooses a sequence of tools that contribute
cumulatively to task resolution.
* **Fallback detection**: Agent attempts a backup tool when the preferred one is
unavailable.
* **Hallucinated call prevention**: Agent avoids fabricating tools that were not
part of the registered capabilities.
* **Policy enforcement**: Certain tools may be restricted by role or
context, evaluators can verify compliance.

## Methods and Tools

| Approach            | Use Case                                   |
| ------------------- | ------------------------------------------ |
| Static rules        | Validate schema, tool name, required args  |
| Golden dataset      | Compare to labeled ground truth            |
| Behavior heuristics | Infer consistency, fallback, retries       |
| Semantic evaluation | LLM-based matching of tool intent vs input |
| Human review        | For gray areas or disputed calls           |

Frameworks like **Azure AI Evaluation**, and custom telemetry services can
provide instrumentation, log export, and evaluation pipelines that support tool
call introspection at scale.

## Best Practices

* **Log consistently**: Include tool name, arguments, results, timestamps,
and agent metadata.
_(Always ensure sensitive or personally identifiable information (PII) is
protected or redacted according to data governance policies)_.
* **Decouple evaluation logic**: Allow swapping evaluation strategies without
modifying agent logic.
* **Define tool policies**: Make tool usage contracts explicit to simplify
validation.
* **Correlate with task completion**: Understand how tool behavior affects
broader goals.

For reference:

* [ToolCallAccuracyEvaluator (Microsoft / .NET)](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.ai.evaluation.quality.toolcallaccuracyevaluator?view=net-9.0-pp)
* [Agent evaluators](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-evaluators/agent-evaluators)

---

{{ #include ../../components/discuss-button.hbs }}