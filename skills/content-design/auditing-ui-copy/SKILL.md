---
name: auditing-ui-copy
description: Systematically evaluate existing UI copy for consistency, clarity, and compliance. Use when reviewing shipped interfaces, preparing for redesigns, or establishing baseline content quality.
---

# Auditing UI Copy

## Quick start
Collect or infer:
- Screen inventory (list of screens/flows to audit)
- Current voice and tone guidelines (if they exist)
- Known problem areas or user complaints
- Target platform and audience

Then produce output using [TEMPLATES.md](TEMPLATES.md). Validate with [RUBRIC.md](RUBRIC.md).

## Workflow
1. Define audit scope: which screens, flows, or components to evaluate.
2. Extract all visible copy from each screen (labels, buttons, errors, tooltips, empty states).
3. Categorize each copy element by type and function.
4. Evaluate each element against rubric criteria (consistency, clarity, action alignment, accessibility).
5. Document findings with severity ratings (critical, major, minor).
6. Generate recommendations with before/after examples.
7. Run the rubric check. Revise until it passes.

## Degrees of freedom
- **Low freedom**: Audit structure and severity taxonomy must follow templates exactly.
- **Allowed variation**: Recommendation phrasing and prioritization rationale may adapt to team context, as long as rubric passes.

## References
- Templates: [TEMPLATES.md](TEMPLATES.md)
- Rubric: [RUBRIC.md](RUBRIC.md)
- Examples: [EXAMPLES.md](EXAMPLES.md)
