---
name: writing-how-to-guides
description: Create task-oriented documentation that guides users through completing specific goals. Use when users need step-by-step instructions to accomplish a discrete task.
---

# Writing How-To Guides

## Quick start
Collect or infer:
- Task goal (what the user wants to accomplish)
- Prerequisites (tools, permissions, prior knowledge)
- User skill level (beginner, intermediate, advanced)
- Platform/environment constraints

Then produce output using [TEMPLATES.md](TEMPLATES.md). Validate with [RUBRIC.md](RUBRIC.md).

## Workflow
1. Define the single task goal in one sentence.
2. List all prerequisites the user must have before starting.
3. Break the task into sequential, atomic steps (max 10 primary steps).
4. Write each step as an imperative action with expected outcome.
5. Add verification checkpoints after critical steps.
6. Include troubleshooting callouts for common failure points.
7. Run the rubric check. Revise until it passes.

## Degrees of freedom
- **Low**: Step structure and heading hierarchy must follow template exactly.
- Allowed variation: Number of steps, callout placement, and code example language may vary as long as rubric passes.

## State awareness
- If prerequisites are missing, prompt for them before generating.
- If task spans multiple tools/systems, split into linked guides.
- If step count exceeds 10, break into sub-guides or reconsider scope.

## Failure modes to avoid
- Combining multiple tasks in one guide
- Skipping prerequisite documentation
- Writing steps that describe concepts instead of actions
- Omitting expected outcomes from steps

## References
- Templates: [TEMPLATES.md](TEMPLATES.md)
- Rubric: [RUBRIC.md](RUBRIC.md)
- Examples: [EXAMPLES.md](EXAMPLES.md)
- Document structure patterns: [reference/doc-structure.md](reference/doc-structure.md)
