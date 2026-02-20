---
name: writing-reference-docs
description: Create comprehensive reference documentation for APIs, libraries, configurations, or system components. Use when users need to look up specific details, parameters, or behaviors rather than follow a task flow.
---

# Writing Reference Docs

## Quick start
Collect or infer:
- Component type (API, configuration, CLI, library)
- Complete parameter/option list with types
- Default values and valid ranges
- Return values or output formats
- Version or compatibility constraints

Then produce output using [TEMPLATES.md](TEMPLATES.md). Validate with [RUBRIC.md](RUBRIC.md).

## Workflow
1. Identify the component type and select appropriate template.
2. Enumerate all parameters, options, or properties exhaustively.
3. Document each item with type, default, constraints, and behavior.
4. Add minimal usage examples (reference, not tutorial).
5. Cross-reference related items and concepts.
6. Validate completeness against source (schema, code, spec).
7. Run the rubric check. Revise until it passes.

## Degrees of freedom
- **Low**: Structure and completeness requirements are strict.
- Allowed variation: Example complexity and grouping strategy may vary as long as rubric passes.

## State awareness
- If source schema or code is available, cross-check for completeness.
- If documenting multiple related items, use consistent ordering.
- If item has complex behavior, link to conceptual doc rather than explaining inline.

## Failure modes to avoid
- Mixing tutorial content with reference content
- Incomplete parameter documentation (missing types or defaults)
- Inconsistent formatting across similar items
- Omitting edge cases or boundary conditions

## References
- Templates: [TEMPLATES.md](TEMPLATES.md)
- Rubric: [RUBRIC.md](RUBRIC.md)
- Examples: [EXAMPLES.md](EXAMPLES.md)
- Reference structure patterns: [reference/reference-patterns.md](reference/reference-patterns.md)
