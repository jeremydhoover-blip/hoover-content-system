---
name: structuring-system-prompts
description: Designs the architecture and organization of system prompts for AI agents. Use when creating initial agent instructions, refactoring existing prompts, or establishing prompt standards.
---

# Structuring System Prompts

## Quick start
Collect or infer:
- Agent purpose and primary use cases
- Required capabilities and tools
- Behavioral constraints and guardrails
- Context sources and injection points
- Voice and tone requirements

Then produce output using [TEMPLATES.md](TEMPLATES.md). Validate with [RUBRIC.md](RUBRIC.md).

## Workflow
1. Define agent identity and core purpose
2. Establish capability boundaries and tool access
3. Structure behavioral rules by priority (critical → preferred)
4. Design context slots and injection points
5. Specify output format requirements
6. Add examples for ambiguous behaviors
7. Optimize for token efficiency without losing clarity
8. Run the rubric check. Revise until it passes.

## Degrees of freedom
- **Low**: Critical sections (identity, guardrails) must follow established patterns
- Allowed variation: Section ordering; example verbosity; formatting style

## Failure modes to avoid
- Conflicting instructions at different prompt levels
- Critical rules buried in verbose sections
- Over-specification that prevents helpful behavior
- Under-specification that allows unsafe behavior

## References
- Templates: [TEMPLATES.md](TEMPLATES.md)
- Rubric: [RUBRIC.md](RUBRIC.md)
- Examples: [EXAMPLES.md](EXAMPLES.md)
- Prompt architecture: [reference/prompt-architecture.md](reference/prompt-architecture.md)
- Section patterns: [reference/section-patterns.md](reference/section-patterns.md)
