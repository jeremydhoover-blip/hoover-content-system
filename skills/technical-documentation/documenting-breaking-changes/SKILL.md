---
name: documenting-breaking-changes
description: Create clear documentation for breaking changes that helps users understand impact and migrate successfully. Use when releasing changes that require user action to maintain functionality.
---

# Documenting Breaking Changes

## Quick start
Collect or infer:
- What specifically changed (API, behavior, configuration)
- Who is affected (all users, specific integrations, specific versions)
- What breaks if users don't act
- How to migrate (step-by-step)
- Timeline (grace period, deprecation date, removal date)

Then produce output using [TEMPLATES.md](TEMPLATES.md). Validate with [RUBRIC.md](RUBRIC.md).

## Workflow
1. Identify the change type and scope precisely.
2. Document what worked before and what works now.
3. Explain who is affected and how to detect if impacted.
4. Provide step-by-step migration instructions.
5. Include before/after code examples.
6. Set clear timelines with specific dates.
7. Link to related documentation and support.
8. Run the rubric check. Revise until it passes.

## Degrees of freedom
- **Low**: Migration documentation structure must be followed strictly.
- Allowed variation: Level of technical detail based on audience, as long as rubric passes.

## State awareness
- If change affects security, prioritize and expedite communication.
- If change has workarounds, document temporary and permanent solutions.
- If change affects subset of users, help users self-identify.
- If migration is complex, consider migration tooling.

## Failure modes to avoid
- Describing what changed without explaining impact
- Missing migration steps
- Vague timelines ("soon", "in a future release")
- Not helping users identify if they're affected
- Assuming technical knowledge without stating prerequisites

## References
- Templates: [TEMPLATES.md](TEMPLATES.md)
- Rubric: [RUBRIC.md](RUBRIC.md)
- Examples: [EXAMPLES.md](EXAMPLES.md)
- Breaking change categories: [reference/breaking-change-types.md](reference/breaking-change-types.md)
