---
name: writing-confirmation-dialogs
description: Write clear confirmation dialogs for user actions. Use when users trigger irreversible actions, destructive operations, or significant state changes that require explicit consent.
---

# Writing Confirmation Dialogs

## Quick start
Collect or infer:
- Action being confirmed
- Reversibility (reversible, hard to reverse, irreversible)
- Impact scope (single item, multiple items, account-wide)
- Consequences of proceeding

Then produce output using [TEMPLATES.md](TEMPLATES.md). Validate with [RUBRIC.md](RUBRIC.md).

## Workflow
1. Classify the action's severity and reversibility
2. Write the headline (what will happen)
3. Write the body (consequences, if not obvious)
4. Write confirm button (specific verb matching action)
5. Write cancel button (safe exit)
6. Run the rubric check. Revise until it passes.

## Degrees of freedom
- **Low**: Structure (headline + body + confirm + cancel) is fixed
- **Medium**: Body length varies by complexity of consequences
- **Allowed variation**: Body can be omitted for simple reversible actions

## Constraints
- Headline: max 60 characters
- Body: max 200 characters
- Confirm button: max 20 characters, must be specific verb
- Cancel button: max 15 characters
- Confirm button must NOT be generic "Yes" or "OK"
- Destructive actions use red/warning button styling (note in output)

## References
- Templates: [TEMPLATES.md](TEMPLATES.md)
- Rubric: [RUBRIC.md](RUBRIC.md)
- Examples: [EXAMPLES.md](EXAMPLES.md)
