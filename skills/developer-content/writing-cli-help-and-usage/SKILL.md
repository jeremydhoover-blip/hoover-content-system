---
name: writing-cli-help-and-usage
description: Generates CLI help text, usage strings, and command documentation. Use when writing --help output, man pages, command syntax documentation, or argument descriptions for command-line tools.
---

# Writing CLI Help and Usage

## Quick start
Collect or infer:
- Command name and parent hierarchy (e.g., `tool resource action`)
- Required and optional arguments with types
- Flags/options with short and long forms
- Environment variable overrides
- Exit code meanings

Then produce output using [TEMPLATES.md](TEMPLATES.md). Validate with [RUBRIC.md](RUBRIC.md).

## Workflow
1. Map command hierarchy: identify if this is a root command, subcommand, or leaf action.
2. Classify arguments: positional (required order) vs. flags (named options).
3. Write the one-line description (≤80 characters, verb phrase).
4. Write the usage string showing required vs. optional syntax.
5. Document each argument/flag with type, default, and constraints.
6. Add examples showing common use cases (minimum 2).
7. Document related commands if part of a command group.
8. Run the rubric check. Revise until it passes.

## Degrees of freedom
**Low freedom**

- Default: follow templates exactly for `--help` output
- Allowed variation: example complexity may vary; additional sections for complex commands (e.g., environment variables, configuration files)

## State awareness
CLI help must address user states:
- **First encounter**: What does this command do?
- **Syntax check**: What's the exact argument order?
- **Option lookup**: What does this flag do?
- **Troubleshooting**: Why did my command fail?
- **Discovery**: What related commands exist?

## References
- Templates: [TEMPLATES.md](TEMPLATES.md)
- Rubric: [RUBRIC.md](RUBRIC.md)
- Examples: [EXAMPLES.md](EXAMPLES.md)
- CLI style conventions: [reference/cli-style-guide.md](reference/cli-style-guide.md)
