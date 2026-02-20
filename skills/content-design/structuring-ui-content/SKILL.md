---
name: structuring-ui-content
description: Organize and sequence content within UI screens for optimal comprehension and task completion. Use when designing new screens, restructuring existing interfaces, or optimizing content hierarchy.
---

# Structuring UI Content

## Quick start
Collect or infer:
- Screen purpose and primary user task
- All content elements (headings, body, labels, actions, help text)
- User entry point and expected exit
- Constraints (viewport size, scrolling behavior, accessibility requirements)

Then produce output using [TEMPLATES.md](TEMPLATES.md). Validate with [RUBRIC.md](RUBRIC.md).

## Workflow
1. Identify the primary task users complete on this screen.
2. List all content elements required to support that task.
3. Prioritize elements by: task criticality, temporal sequence, decision dependency.
4. Apply content hierarchy: primary action visible without scroll, supporting info near point of need.
5. Group related elements; separate unrelated elements with whitespace or dividers.
6. Validate reading order matches task flow and accessibility requirements.
7. Run the rubric check. Revise until it passes.

## Degrees of freedom
- **Medium freedom**: Structure principles are fixed; specific grouping and sequencing may vary by screen type.
- **Allowed variation**: Visual hierarchy implementation (size, weight, position) may adapt to design system.

## References
- Templates: [TEMPLATES.md](TEMPLATES.md)
- Rubric: [RUBRIC.md](RUBRIC.md)
- Examples: [EXAMPLES.md](EXAMPLES.md)
