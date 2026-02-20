---
name: designing-context-injection-patterns
description: Designs patterns for injecting contextual information into agent prompts. Use when structuring system context, managing context windows, or optimizing information retrieval for agents.
---

# Designing Context Injection Patterns

## Quick start
Collect or infer:
- Agent's task domain and required knowledge
- Context sources (docs, user history, real-time data)
- Context window limits and token budget
- Freshness and accuracy requirements

Then produce output using [TEMPLATES.md](TEMPLATES.md). Validate with [RUBRIC.md](RUBRIC.md).

## Workflow
1. Inventory available context sources and their update frequencies
2. Classify context by type: static, session, query-dependent, real-time
3. Define retrieval triggers and selection criteria
4. Design context structure and ordering within the prompt
5. Specify compression and truncation strategies
6. Define fallback behavior for missing or stale context
7. Run the rubric check. Revise until it passes.

## Degrees of freedom
- **Medium**: Context ordering and formatting may vary based on agent type
- Allowed variation: Specific retrieval mechanisms; chunking strategies for different content types

## Failure modes to avoid
- Context exceeds token limits, causing truncation of critical information
- Stale context presented as current
- Irrelevant context diluting signal
- Missing attribution for injected content

## References
- Templates: [TEMPLATES.md](TEMPLATES.md)
- Rubric: [RUBRIC.md](RUBRIC.md)
- Examples: [EXAMPLES.md](EXAMPLES.md)
- Context types: [reference/context-types.md](reference/context-types.md)
- Retrieval strategies: [reference/retrieval-strategies.md](reference/retrieval-strategies.md)
