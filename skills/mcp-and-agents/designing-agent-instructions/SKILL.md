---
name: designing-agent-instructions
description: Design clear, unambiguous instructions that guide LLM agent behavior. Use when creating system prompts, behavioral guidelines, or operational constraints for AI agents.
---

# Designing Agent Instructions

## Quick start
Collect or infer:
- Agent's purpose and scope of responsibility
- Target behaviors to encourage
- Behaviors to prohibit
- Decision-making authority (what the agent can decide vs. must ask)
- Output format requirements
- Error handling expectations

Then produce output using [TEMPLATES.md](TEMPLATES.md). Validate with [RUBRIC.md](RUBRIC.md).

## Workflow
1. Define the agent's core purpose in one sentence.
2. List behaviors the agent MUST exhibit.
3. List behaviors the agent MUST NOT exhibit.
4. Define decision boundaries (autonomous vs. requires confirmation).
5. Specify output format and communication style.
6. Add error handling and edge case guidance.
7. Run the rubric check. Revise until it passes.

## Degrees of freedom
- **Low freedom**: Prohibition rules must be explicit and unambiguous.
- **Medium freedom**: Instruction organization and phrasing can vary.
- **Allowed variation**: Additional context sections as long as core structure is preserved.

## Failure modes to avoid
- Vague instructions that can be interpreted multiple ways
- Missing prohibition rules (agent does harmful things not explicitly forbidden)
- Over-constraining with contradictory rules
- No guidance for edge cases or errors
- Assuming the agent knows implicit context
- Instructions too long for context window

## References
- Templates: [TEMPLATES.md](TEMPLATES.md)
- Rubric: [RUBRIC.md](RUBRIC.md)
- Examples: [EXAMPLES.md](EXAMPLES.md)
- Instruction patterns: [reference/instruction-patterns.md](reference/instruction-patterns.md)
- Common pitfalls: [reference/common-pitfalls.md](reference/common-pitfalls.md)
