---
name: writing-configuration-guides
description: Write clear, comprehensive configuration documentation for developer tools and applications. Use when documenting config files, environment variables, feature flags, or initialization parameters.
---

# Writing Configuration Guides

## Quick start
Collect or infer:
- Configuration scope (config file, environment variables, CLI flags, or combined)
- Target runtime or platform
- Required vs optional parameters
- Default values and their rationale
- Security-sensitive values

Then produce output using [TEMPLATES.md](TEMPLATES.md). Validate with [RUBRIC.md](RUBRIC.md).

## Workflow
1. Inventory all configurable parameters and group by function.
2. Classify each as required or optional; document defaults.
3. Write parameter reference with type, constraints, and examples.
4. Add a quick-start minimal config example.
5. Document environment-specific overrides if applicable.
6. Run the rubric check. Revise until it passes.

## Degrees of freedom
- **Low freedom**: Parameter reference format must follow template exactly.
- **Medium freedom**: Grouping logic and section order can adapt to product complexity.
- **Allowed variation**: Additional sections (troubleshooting, migration) as long as rubric passes.

## Failure modes to avoid
- Documenting parameters without valid example values
- Omitting units or constraints (e.g., "timeout in seconds, range 1-300")
- Mixing secret values with non-sensitive config without security callouts
- Assuming readers know environment variable inheritance

## References
- Templates: [TEMPLATES.md](TEMPLATES.md)
- Rubric: [RUBRIC.md](RUBRIC.md)
- Examples: [EXAMPLES.md](EXAMPLES.md)
- Config patterns: [reference/config-patterns.md](reference/config-patterns.md)
- Defaults rationale: [reference/defaults-rationale.md](reference/defaults-rationale.md)
