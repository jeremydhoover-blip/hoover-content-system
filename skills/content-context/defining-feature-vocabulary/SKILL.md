---
name: defining-feature-vocabulary
description: Creates the canonical vocabulary for a feature, including term definitions, usage rules, and prohibited alternatives. Use when starting content work on a new feature, resolving terminology inconsistencies, or establishing naming conventions for concepts within a feature.
---

# Defining Feature Vocabulary

## Quick start
Collect or infer:
- Feature name and scope
- Core concepts that need naming
- Existing terminology (if any) from product, engineering, or design
- User research on mental models and natural language
- Adjacent features with related terminology

Then produce output using [TEMPLATES.md](TEMPLATES.md). Validate with [RUBRIC.md](RUBRIC.md).

## Workflow
1. Inventory all concepts requiring terminology decisions.
2. Gather existing terms from all sources (code, design, support, user research).
3. Identify conflicts where different teams use different terms for the same concept.
4. Propose canonical terms following the [naming principles](reference/vocabulary-naming-principles.md).
5. Define each term with scope, usage context, and prohibited alternatives.
6. Validate against the [conflict checklist](reference/term-conflict-patterns.md).
7. Document rationale for non-obvious naming decisions.
8. Run the rubric check. Revise until it passes.

## Degrees of freedom
- **Default:** Low. Vocabulary must be precise and consistent.
- **Allowed variation:** Documentation format may adapt to team preferences. Rationale depth may vary based on contentiousness of term.

## Failure modes to avoid
- Using different terms for the same concept across the feature
- Using the same term for different concepts
- Choosing terms that conflict with platform conventions
- Ignoring user mental models in favor of internal terminology
- Creating vocabulary without checking adjacent feature terminology
- Defining terms without prohibited alternatives list

## References
- Templates: [TEMPLATES.md](TEMPLATES.md)
- Rubric: [RUBRIC.md](RUBRIC.md)
- Examples: [EXAMPLES.md](EXAMPLES.md)
- Naming principles: [reference/vocabulary-naming-principles.md](reference/vocabulary-naming-principles.md)
- Conflict patterns: [reference/term-conflict-patterns.md](reference/term-conflict-patterns.md)
