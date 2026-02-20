---
name: writing-sdk-docs-and-samples
description: Generates SDK documentation and code samples. Use when documenting client libraries, writing quickstarts, creating code examples, or explaining SDK architecture and usage patterns.
---

# Writing SDK Docs and Samples

## Quick start
Collect or infer:
- SDK name and target language/platform
- Authentication method and credentials pattern
- Core operations to document (CRUD, streaming, batch)
- Error handling expectations
- Target developer persona (beginner, experienced, enterprise)

Then produce output using [TEMPLATES.md](TEMPLATES.md). Validate with [RUBRIC.md](RUBRIC.md).

## Workflow
1. Identify SDK scope: single service vs. multi-service, sync vs. async, platform constraints.
2. Map core operations to documentation sections: install, configure, authenticate, execute, handle errors.
3. Write installation section with package manager commands and version constraints.
4. Document authentication with code samples showing credential instantiation.
5. Create operation samples showing happy path, then error handling, then advanced usage.
6. Add inline comments explaining non-obvious parameters and return values.
7. Write troubleshooting section for common SDK errors.
8. Run the rubric check. Revise until it passes.

## Degrees of freedom
**Medium freedom**

- Default: follow templates for structure and section ordering
- Allowed variation: sample complexity and language idioms may adapt to target audience; additional sections permitted if SDK has unusual patterns (e.g., streaming, pagination, retries)

## State awareness
Consider SDK documentation across states:
- **Not installed**: Installation instructions, prerequisites
- **Installed but not configured**: Configuration and authentication
- **Configured but first use**: Quickstart samples
- **Active use**: Advanced patterns, batch operations
- **Upgrade path**: Migration guides, breaking changes

## References
- Templates: [TEMPLATES.md](TEMPLATES.md)
- Rubric: [RUBRIC.md](RUBRIC.md)
- Examples: [EXAMPLES.md](EXAMPLES.md)
- SDK structure patterns: [reference/sdk-doc-structure.md](reference/sdk-doc-structure.md)
- Sample code conventions: [reference/code-sample-conventions.md](reference/code-sample-conventions.md)
