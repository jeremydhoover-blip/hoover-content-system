---
name: writing-cli-errors-and-exit-codes
description: Generates CLI error messages and defines exit code conventions. Use when writing stderr output, defining exit codes, creating error message templates, or designing error recovery guidance for command-line tools.
---

# Writing CLI Errors and Exit Codes

## Quick start
Collect or infer:
- Command name and operation context
- Error categories (user error, system error, external dependency)
- Whether error is recoverable or terminal
- Target audience (developer, operator, end user)
- Exit code numbering scheme (if existing conventions apply)

Then produce output using [TEMPLATES.md](TEMPLATES.md). Validate with [RUBRIC.md](RUBRIC.md).

## Workflow
1. Categorize the error: input validation, authentication, resource access, network, internal.
2. Determine recoverability: can the user fix this without code changes?
3. Select appropriate exit code from standard ranges.
4. Write error message with structure: what happened → why → how to fix.
5. Add contextual details that help debugging (file paths, values, constraints).
6. Ensure error is parseable if tool is used in scripts.
7. Run the rubric check. Revise until it passes.

## Degrees of freedom
**Low freedom**

- Default: follow templates exactly for error format
- Allowed variation: additional context lines permitted for complex errors; verbose mode may expand detail

## State awareness
CLI errors occur across operational states:
- **Pre-execution**: Argument validation, config parsing, auth check
- **During execution**: Resource access, network calls, processing
- **Post-execution**: Cleanup failures, result validation
- **Pipeline context**: Errors that affect downstream commands

## References
- Templates: [TEMPLATES.md](TEMPLATES.md)
- Rubric: [RUBRIC.md](RUBRIC.md)
- Examples: [EXAMPLES.md](EXAMPLES.md)
- Exit code conventions: [reference/exit-code-conventions.md](reference/exit-code-conventions.md)
- Error taxonomy: [reference/cli-error-taxonomy.md](reference/cli-error-taxonomy.md)
