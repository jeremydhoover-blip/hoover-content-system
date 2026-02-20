---
name: writing-mcp-tool-descriptions
description: Write clear, accurate tool descriptions for Model Context Protocol (MCP) servers. Use when defining tool names, descriptions, parameter schemas, and usage guidance for LLM consumption.
---

# Writing MCP Tool Descriptions

## Quick start
Collect or infer:
- Tool's primary function and when it should be invoked
- Required and optional parameters with types
- Return value structure and meaning
- Preconditions and side effects
- Error conditions and how they manifest

Then produce output using [TEMPLATES.md](TEMPLATES.md). Validate with [RUBRIC.md](RUBRIC.md).

## Workflow
1. Define the tool's singular purpose (one tool, one job).
2. Write a description that tells the LLM when to use (and not use) this tool.
3. Define parameters with precise types, constraints, and examples.
4. Document return value structure and interpretation.
5. Specify error conditions the LLM should handle.
6. Run the rubric check. Revise until it passes.

## Degrees of freedom
- **Low freedom**: Parameter schema must follow JSON Schema conventions exactly.
- **Medium freedom**: Description style can vary as long as trigger conditions are explicit.
- **Allowed variation**: Additional metadata fields as long as rubric passes.

## Failure modes to avoid
- Description doesn't explain when to use the tool
- Parameter names are ambiguous (e.g., `data`, `input`, `value`)
- Missing required vs optional distinction
- No examples for complex parameter types
- Undocumented side effects (file writes, network calls, state changes)
- Overly broad scope (tool tries to do too many things)

## References
- Templates: [TEMPLATES.md](TEMPLATES.md)
- Rubric: [RUBRIC.md](RUBRIC.md)
- Examples: [EXAMPLES.md](EXAMPLES.md)
- Schema patterns: [reference/schema-patterns.md](reference/schema-patterns.md)
- Description style: [reference/description-style.md](reference/description-style.md)
