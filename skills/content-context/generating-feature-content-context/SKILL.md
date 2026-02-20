---
name: generating-feature-content-context
description: Creates structured context packs that provide AI systems and content creators with complete information about a feature. Use when preparing for content generation, onboarding writers to features, or building AI-ready documentation.
---

# Generating Feature Content Context

## Quick start
Collect or infer:
- Feature name and purpose
- User goals and tasks the feature supports
- Feature states (empty, loading, error, success, etc.)
- UI components and their copy needs
- Business rules and constraints
- Edge cases and exceptions

Then produce output using [TEMPLATES.md](TEMPLATES.md). Validate with [RUBRIC.md](RUBRIC.md).

## Workflow
1. Identify the feature scope and boundaries
2. Document user goals and primary tasks
3. Map all feature states systematically
4. Catalog UI components requiring copy
5. Document business rules affecting content
6. Capture edge cases and exception handling
7. Compile terminology and naming decisions
8. Validate completeness against rubric
9. Run the rubric check. Revise until it passes.

## Degrees of freedom
**Freedom level: Low**
- Default: follow templates exactly
- Allowed variation: depth of state coverage based on feature complexity—as long as rubric passes
- Strict constraints: Must cover all states; must include terminology; must document constraints

## State awareness
- **New feature**: Build context as feature is designed; iterate with product/engineering
- **Existing feature**: Audit current copy to extract implicit context; document gaps
- **Feature update**: Start from existing context; document what's changing
- **AI consumption**: Ensure structured format; include examples for each component

## References
- Templates: [TEMPLATES.md](TEMPLATES.md)
- Rubric: [RUBRIC.md](RUBRIC.md)
- Examples: [EXAMPLES.md](EXAMPLES.md)
- Context pack schema: [reference/context-pack-schema.md](reference/context-pack-schema.md)
