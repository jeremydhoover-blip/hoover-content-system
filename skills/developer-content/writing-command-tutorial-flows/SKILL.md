---
name: writing-command-tutorial-flows
description: Generates step-by-step CLI tutorials and command sequences. Use when creating getting-started guides, multi-step workflows, command chaining examples, or progressive CLI learning paths.
---

# Writing Command Tutorial Flows

## Quick start
Collect or infer:
- Learning goal (what user will accomplish)
- Prerequisite commands or setup
- Command sequence with dependencies between steps
- Expected output at each step
- Checkpoints for user validation

Then produce output using [TEMPLATES.md](TEMPLATES.md). Validate with [RUBRIC.md](RUBRIC.md).

## Workflow
1. Define the end state: what will the user have accomplished?
2. Identify prerequisites: auth, installation, data, permissions.
3. Map the command sequence with dependencies.
4. Determine checkpoints: where can the user verify progress?
5. Write each step with command, explanation, and expected output.
6. Add troubleshooting for likely failure points.
7. Provide cleanup commands if tutorial creates resources.
8. Run the rubric check. Revise until it passes.

## Degrees of freedom
**Medium freedom**

- Default: follow templates for step structure
- Allowed variation: complexity may adapt to audience; optional advanced paths permitted; troubleshooting depth may vary

## State awareness
Tutorial flows must track user state:
- **Not started**: Prerequisites clear, environment ready
- **In progress**: Each step builds on previous
- **Checkpoint**: User can verify correct state
- **Diverged**: User deviated, needs recovery path
- **Completed**: End state achieved, cleanup offered

## References
- Templates: [TEMPLATES.md](TEMPLATES.md)
- Rubric: [RUBRIC.md](RUBRIC.md)
- Examples: [EXAMPLES.md](EXAMPLES.md)
- Tutorial structure patterns: [reference/tutorial-patterns.md](reference/tutorial-patterns.md)
