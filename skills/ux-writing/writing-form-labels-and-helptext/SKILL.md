---
name: writing-form-labels-and-helptext
description: Write clear form field labels, placeholders, and help text. Use when designing forms, input fields, registration flows, data entry screens, or any UI requiring user input.
---

# Writing Form Labels and Help Text

## Quick start
Collect or infer:
- Field purpose (what data is being collected)
- Input type (text, email, password, select, etc.)
- Required vs. optional status
- Validation rules or format requirements

Then produce output using [TEMPLATES.md](TEMPLATES.md). Validate with [RUBRIC.md](RUBRIC.md).

## Workflow
1. Identify the data being collected and its purpose
2. Write the label (what to enter)
3. Decide if placeholder is needed (format hint only)
4. Write help text if format or constraints exist
5. Write validation error messages
6. Run the rubric check. Revise until it passes.

## Degrees of freedom
- **Low**: Labels must be present and visible (not placeholder-only)
- **Medium**: Help text optional if field is self-explanatory
- **Allowed variation**: Placeholder can be omitted if help text covers format

## Constraints
- Label: max 40 characters
- Placeholder: max 40 characters
- Help text: max 100 characters
- Validation error: max 80 characters
- Labels must always be visible (never placeholder-only forms)
- Placeholders are hints, not labels

## References
- Templates: [TEMPLATES.md](TEMPLATES.md)
- Rubric: [RUBRIC.md](RUBRIC.md)
- Examples: [EXAMPLES.md](EXAMPLES.md)
