---
name: writing-error-messages
description: Write clear, actionable error messages for UI. Use when users encounter validation failures, system errors, connection problems, or any state where something went wrong.
---

# Writing Error Messages

## Quick start
Collect or infer:
- Error type (validation, system, network, permission, not-found)
- Severity (blocking, degraded, informational)
- User action that triggered error
- Available recovery actions

Then produce output using [TEMPLATES.md](TEMPLATES.md). Validate with [RUBRIC.md](RUBRIC.md).

## Workflow
1. Classify error using [reference/error-categories.md](reference/error-categories.md)
2. Identify what the user was trying to do
3. Write the error title (what happened)
4. Write the body (why it happened, if helpful)
5. Write the action (how to fix it)
6. Run the rubric check. Revise until it passes.

## Degrees of freedom
- **Low**: Error structure (title + body + action) is fixed
- **Medium**: Tone adjusts by severity per [reference/error-categories.md](reference/error-categories.md)
- **Allowed variation**: Body can be omitted if cause is obvious and action is clear

## Constraints
- Title: max 60 characters
- Body: max 150 characters
- Action label: max 25 characters
- Never blame the user
- Never expose technical details (stack traces, error codes) in user-facing copy

## References
- Templates: [TEMPLATES.md](TEMPLATES.md)
- Rubric: [RUBRIC.md](RUBRIC.md)
- Examples: [EXAMPLES.md](EXAMPLES.md)
- Error categories: [reference/error-categories.md](reference/error-categories.md)
