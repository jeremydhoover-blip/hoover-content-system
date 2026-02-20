---
name: generating-state-maps
description: Creates visual and structured representations of all possible states a feature can exist in, including transitions, triggers, and content requirements per state. Use when documenting a new feature, auditing existing state handling, or preparing context for UI copy.
---

# Generating State Maps

## Quick start
Collect or infer:
- Feature name and scope
- User actions that trigger state changes
- System events that trigger state changes
- Error conditions and edge cases
- Content touchpoints per state (messages, labels, CTAs)

Then produce output using [TEMPLATES.md](TEMPLATES.md). Validate with [RUBRIC.md](RUBRIC.md).

## Workflow
1. Identify the feature's entry state (first state a user encounters).
2. List all possible states using the [state taxonomy](reference/state-taxonomy.md).
3. Document transitions: what triggers movement from one state to another.
4. Identify dead ends (terminal states with no outbound transitions).
5. Map content requirements per state (what copy appears, what actions are available).
6. Validate completeness: every state must have at least one inbound transition (except entry).
7. Identify missing states by checking for unhandled edge cases.
8. Run the rubric check. Revise until it passes.

## Degrees of freedom
- **Default:** Low. State maps must be complete and accurate.
- **Allowed variation:** Visual format (Mermaid, table, ASCII) may vary by team preference. Content requirement detail level may flex based on scope.

## Failure modes to avoid
- Omitting error states
- Forgetting permission-gated states
- Missing loading/pending states
- Creating orphan states (no inbound transition)
- Conflating user-facing states with technical backend states
- Assuming happy path only

## References
- Templates: [TEMPLATES.md](TEMPLATES.md)
- Rubric: [RUBRIC.md](RUBRIC.md)
- Examples: [EXAMPLES.md](EXAMPLES.md)
- State taxonomy: [reference/state-taxonomy.md](reference/state-taxonomy.md)
- Transition patterns: [reference/transition-patterns.md](reference/transition-patterns.md)
