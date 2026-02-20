---
name: documenting-tooling-workflows
description: Document complex developer tooling workflows that span multiple tools or systems. Use when writing guides for build pipelines, deployment processes, CI/CD workflows, or multi-tool integration patterns.
---

# Documenting Tooling Workflows

## Quick start
Collect or infer:
- Workflow goal and success criteria
- Tools involved and their versions
- Prerequisites (accounts, credentials, installed software)
- Input artifacts and output artifacts
- Decision points and branching paths
- Error states and recovery procedures

Then produce output using [TEMPLATES.md](TEMPLATES.md). Validate with [RUBRIC.md](RUBRIC.md).

## Workflow
1. Map the end-to-end workflow with all steps and decision points.
2. Identify prerequisites and document verification commands.
3. Write step-by-step instructions with expected outputs.
4. Document error states and recovery for each critical step.
5. Add a visual workflow diagram if complexity warrants.
6. Run the rubric check. Revise until it passes.

## Degrees of freedom
- **Low freedom**: Step format must include command, expected output, and troubleshooting.
- **Medium freedom**: Diagram style and sectioning can adapt to workflow complexity.
- **Allowed variation**: Additional sections (optimization, alternatives) as long as rubric passes.

## Failure modes to avoid
- Assuming tools are pre-installed without verification steps
- Omitting expected output, leaving users unsure if step succeeded
- Documenting happy path only, ignoring common failures
- Version drift: workflow breaks silently when tools update
- Missing rollback procedures for destructive operations

## References
- Templates: [TEMPLATES.md](TEMPLATES.md)
- Rubric: [RUBRIC.md](RUBRIC.md)
- Examples: [EXAMPLES.md](EXAMPLES.md)
- Workflow patterns: [reference/workflow-patterns.md](reference/workflow-patterns.md)
- Diagram conventions: [reference/diagram-conventions.md](reference/diagram-conventions.md)
