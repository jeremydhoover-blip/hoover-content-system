---
name: defining-guardrails-and-constraints
description: Defines behavioral limits and safety constraints for AI agents. Use when specifying what an agent must not do, setting scope boundaries, or implementing safety policies.
---

# Defining Guardrails and Constraints

## Quick start
Collect or infer:
- Agent purpose and capability scope
- Risk domains (data access, actions, external calls)
- Organizational safety policies
- User trust level and context sensitivity

Then produce output using [TEMPLATES.md](TEMPLATES.md). Validate with [RUBRIC.md](RUBRIC.md).

## Workflow
1. Identify the agent's intended action space
2. Map risk categories: data exposure, irreversible actions, scope creep, hallucination-sensitive domains
3. Define hard boundaries (absolute prohibitions)
4. Define soft boundaries (conditional restrictions with escalation paths)
5. Specify detection and enforcement mechanisms
6. Write constraint language using imperative, unambiguous phrasing
7. Run the rubric check. Revise until it passes.

## Degrees of freedom
- **Low**: Constraint language must use imperative mood and explicit scope
- Allowed variation: Ordering of constraint categories; specific escalation mechanisms may vary by deployment context

## Failure modes to avoid
- Vague prohibitions ("be careful with sensitive data")
- Constraints that conflict with core functionality
- Missing enforcement mechanisms
- Overly broad restrictions that block valid use cases

## References
- Templates: [TEMPLATES.md](TEMPLATES.md)
- Rubric: [RUBRIC.md](RUBRIC.md)
- Examples: [EXAMPLES.md](EXAMPLES.md)
- Constraint taxonomy: [reference/constraint-taxonomy.md](reference/constraint-taxonomy.md)
- Enforcement patterns: [reference/enforcement-patterns.md](reference/enforcement-patterns.md)
