---
name: designing-progressive-disclosure
description: Layer information and options to match user attention and need. Use when designing onboarding flows, complex forms, settings interfaces, or any screen with more information than users need at once.
---

# Designing Progressive Disclosure

## Quick start
Collect or infer:
- Full content inventory (everything that could appear)
- User task and immediate goal
- User expertise level and context
- Interaction constraints (platform, accessibility)

Then produce output using [TEMPLATES.md](TEMPLATES.md). Validate with [RUBRIC.md](RUBRIC.md).

## Workflow
1. List all content and options that exist for this screen/flow.
2. Categorize each item by: essential (always visible), supplementary (on-demand), edge-case (hidden until triggered).
3. Define trigger conditions: what user action or state reveals each layer.
4. Design reveal mechanism: expand, drill-down, tooltip, modal, new screen.
5. Ensure hidden content is discoverable (users know more exists).
6. Validate that essential content remains accessible without interaction.
7. Run the rubric check. Revise until it passes.

## Degrees of freedom
- **Medium freedom**: Layering principles are fixed; reveal mechanisms may vary by platform and component.
- **Allowed variation**: Specific triggers and reveal patterns depend on design system and interaction model.

## References
- Templates: [TEMPLATES.md](TEMPLATES.md)
- Rubric: [RUBRIC.md](RUBRIC.md)
- Examples: [EXAMPLES.md](EXAMPLES.md)
