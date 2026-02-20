---
name: auditing-agent-behavior
description: Systematically evaluates agent outputs and actions against expected behavior. Use when reviewing agent performance, identifying failure patterns, or validating agent compliance with specifications.
---

# Auditing Agent Behavior

## Quick start
Collect or infer:
- Agent specifications (instructions, guardrails, expected behaviors)
- Sample of agent interactions to audit
- Success criteria and failure definitions
- Audit scope (specific capabilities, time range, user segment)

Then produce output using [TEMPLATES.md](TEMPLATES.md). Validate with [RUBRIC.md](RUBRIC.md).

## Workflow
1. Define audit scope and sampling strategy
2. Establish evaluation criteria from agent specifications
3. Collect representative interaction samples
4. Categorize behaviors: correct, incorrect, edge case, unsafe
5. Identify patterns in failures and near-misses
6. Document findings with severity and frequency
7. Recommend specific remediation actions
8. Run the rubric check. Revise until it passes.

## Degrees of freedom
- **Medium**: Audit depth and sampling strategy may vary based on risk level
- Allowed variation: Categorization schemes; specific metrics tracked

## Failure modes to avoid
- Auditing without clear success criteria
- Sampling bias (only reviewing flagged interactions)
- Focusing on edge cases while missing systemic issues
- Recommendations without actionable specificity

## References
- Templates: [TEMPLATES.md](TEMPLATES.md)
- Rubric: [RUBRIC.md](RUBRIC.md)
- Examples: [EXAMPLES.md](EXAMPLES.md)
- Audit categories: [reference/audit-categories.md](reference/audit-categories.md)
