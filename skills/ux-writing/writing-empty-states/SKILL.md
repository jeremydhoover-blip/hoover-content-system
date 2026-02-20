---
name: writing-empty-states
description: Write helpful, actionable empty state messages for UI. Use when displaying screens with no data, first-run experiences, zero results, or cleared content states.
---

# Writing Empty States

## Quick start
Collect or infer:
- Empty state type (first-run, no-results, user-cleared, error-caused)
- What content would normally appear here
- User's likely goal or task
- Available actions to populate the state

Then produce output using [TEMPLATES.md](TEMPLATES.md). Validate with [RUBRIC.md](RUBRIC.md).

## Workflow
1. Identify empty state type using [reference/empty-state-types.md](reference/empty-state-types.md)
2. Determine what the user expects to see
3. Write the headline (acknowledge the state)
4. Write supporting text (explain or guide)
5. Provide primary action (if applicable)
6. Run the rubric check. Revise until it passes.

## Degrees of freedom
- **Low**: Structure (headline + support + action) is fixed
- **Medium**: Tone can be warmer for first-run, neutral for no-results
- **Allowed variation**: Support text optional if action is self-explanatory

## Constraints
- Headline: max 50 characters
- Support text: max 120 characters
- Action label: max 25 characters
- Never leave users without guidance
- First-run states should motivate, not just describe absence

## References
- Templates: [TEMPLATES.md](TEMPLATES.md)
- Rubric: [RUBRIC.md](RUBRIC.md)
- Examples: [EXAMPLES.md](EXAMPLES.md)
- Empty state types: [reference/empty-state-types.md](reference/empty-state-types.md)
