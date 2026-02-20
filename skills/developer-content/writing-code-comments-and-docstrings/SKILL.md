---
name: writing-code-comments-and-docstrings
description: Generates inline code comments and documentation strings. Use when writing function/class documentation, explaining complex logic, adding TODO/FIXME annotations, or documenting APIs in code.
---

# Writing Code Comments and Docstrings

## Quick start
Collect or infer:
- Programming language and documentation conventions
- Code element type (function, class, module, method)
- Target audience (internal team, external consumers, future maintainers)
- Complexity level of the code being documented
- Whether public API or internal implementation

Then produce output using [TEMPLATES.md](TEMPLATES.md). Validate with [RUBRIC.md](RUBRIC.md).

## Workflow
1. Identify documentation type: docstring (API), inline comment (implementation), or annotation (TODO/FIXME).
2. Determine what the code does vs. why it exists—document the latter.
3. For docstrings: document parameters, return values, exceptions, and side effects.
4. For inline comments: explain non-obvious decisions, constraints, or workarounds.
5. For annotations: include context, assignee (if known), and ticket reference.
6. Verify comments don't restate what code already says.
7. Run the rubric check. Revise until it passes.

## Degrees of freedom
**Medium freedom**

- Default: follow language-specific conventions exactly
- Allowed variation: verbosity may adapt to code complexity; internal vs. external APIs may have different detail levels

## State awareness
Code documentation serves different reader states:
- **First encounter**: What does this do? Should I use it?
- **Integration**: What parameters? What's returned? What can go wrong?
- **Debugging**: Why was this implemented this way?
- **Maintenance**: What's the history? What should I not change?
- **Refactoring**: What depends on this? What's the contract?

## References
- Templates: [TEMPLATES.md](TEMPLATES.md)
- Rubric: [RUBRIC.md](RUBRIC.md)
- Examples: [EXAMPLES.md](EXAMPLES.md)
- Language conventions: [reference/language-conventions.md](reference/language-conventions.md)
