---
name: writing-settings-and-preferences
description: Write clear labels and descriptions for settings and preferences UI. Use when creating settings screens, preference panels, toggles, configuration options, or feature flags exposed to users.
---

# Writing Settings and Preferences

## Quick start
Collect or infer:
- Setting category (account, notifications, privacy, appearance, etc.)
- Setting type (toggle, select, input, action)
- Default state
- Impact of changing the setting

Then produce output using [TEMPLATES.md](TEMPLATES.md). Validate with [RUBRIC.md](RUBRIC.md).

## Workflow
1. Identify the setting category and type
2. Write the label (what the setting controls)
3. Write the description (what happens when enabled/changed)
4. Specify the default value
5. Add helper text for complex settings
6. Run the rubric check. Revise until it passes.

## Degrees of freedom
- **Low**: Label + description structure is fixed
- **Medium**: Description length varies by complexity
- **Allowed variation**: Description can be omitted for self-explanatory settings

## Constraints
- Label: max 40 characters
- Description: max 120 characters
- Toggle labels describe the ON state
- Never use double negatives
- Group related settings with clear section headers

## References
- Templates: [TEMPLATES.md](TEMPLATES.md)
- Rubric: [RUBRIC.md](RUBRIC.md)
- Examples: [EXAMPLES.md](EXAMPLES.md)
