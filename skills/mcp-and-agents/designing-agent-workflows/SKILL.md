---
name: designing-agent-workflows
description: Design multi-step workflows that orchestrate agent actions toward complex goals. Use when planning agent task sequences, decision trees, or state machines for autonomous operation.
---

# Designing Agent Workflows

## Quick start
Collect or infer:
- Workflow goal and success criteria
- Required steps and their dependencies
- Decision points and branching conditions
- State that must be tracked across steps
- Failure modes and recovery strategies
- Human checkpoints (where to pause for approval)

Then produce output using [TEMPLATES.md](TEMPLATES.md). Validate with [RUBRIC.md](RUBRIC.md).

## Workflow
1. Define the workflow goal and measurable success criteria.
2. Map all steps and their dependencies (what must complete before what).
3. Identify decision points and document all branches.
4. Define state that persists across steps.
5. Add failure handling for each step.
6. Insert human checkpoints for irreversible or high-risk actions.
7. Run the rubric check. Revise until it passes.

## Degrees of freedom
- **Low freedom**: Decision criteria must be explicit and deterministic.
- **Medium freedom**: Step ordering can adapt to dependencies.
- **Allowed variation**: Diagram style and notation as long as logic is clear.

## Failure modes to avoid
- Undefined behavior at decision points
- Missing failure handling for any step
- State not explicitly tracked between steps
- No human checkpoint before irreversible actions
- Infinite loops without termination conditions
- Implicit assumptions about step ordering

## References
- Templates: [TEMPLATES.md](TEMPLATES.md)
- Rubric: [RUBRIC.md](RUBRIC.md)
- Examples: [EXAMPLES.md](EXAMPLES.md)
- Workflow patterns: [reference/workflow-patterns.md](reference/workflow-patterns.md)
- State management: [reference/state-management.md](reference/state-management.md)
