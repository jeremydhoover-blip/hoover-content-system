---
name: updating-feature-context-from-feedback
description: Updates existing feature content context based on user feedback, research findings, or product changes. Use when feedback reveals gaps, inaccuracies, or shifts in user mental models within an existing context pack.
---

# Updating Feature Context from Feedback

## Quick start
Collect or infer:
- Existing context pack (or path to it)
- Feedback source (user research, support tickets, analytics, PM input)
- Feedback type (gap, correction, expansion, deprecation)
- Change scope (additive, modifying, removing)

Then produce output using [TEMPLATES.md](TEMPLATES.md). Validate with [RUBRIC.md](RUBRIC.md).

## Workflow
1. Load the existing context pack and identify its current version.
2. Categorize incoming feedback using the [feedback taxonomy](reference/feedback-taxonomy.md).
3. Map each feedback item to affected context sections (vocabulary, states, actions, constraints).
4. Draft proposed changes with explicit before/after deltas.
5. Flag conflicts where feedback contradicts existing context or other feedback.
6. Generate a change summary with rationale for each modification.
7. Update version metadata and changelog.
8. Run the rubric check. Revise until it passes.

## Degrees of freedom
- **Default:** Low. Context changes must be traceable and justified.
- **Allowed variation:** Rationale phrasing and changelog format may adapt to team conventions, as long as traceability is preserved and rubric passes.

## Failure modes to avoid
- Applying feedback without validating source credibility
- Overwriting context without preserving change history
- Conflating user requests with validated needs
- Introducing terminology conflicts with existing vocabulary
- Removing states without confirming deprecation across all touchpoints

## References
- Templates: [TEMPLATES.md](TEMPLATES.md)
- Rubric: [RUBRIC.md](RUBRIC.md)
- Examples: [EXAMPLES.md](EXAMPLES.md)
- Feedback taxonomy: [reference/feedback-taxonomy.md](reference/feedback-taxonomy.md)
- Change record schema: [reference/change-record-schema.md](reference/change-record-schema.md)
