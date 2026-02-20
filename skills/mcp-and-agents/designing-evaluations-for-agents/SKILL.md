---
name: designing-evaluations-for-agents
description: Design evaluation frameworks that measure agent behavior and quality. Use when creating test suites, benchmarks, or quality assessments for LLM-based agents.
---

# Designing Evaluations for Agents

## Quick start
Collect or infer:
- Agent capabilities to evaluate
- Success criteria for each capability
- Input scenarios (happy path, edge cases, adversarial)
- Expected behaviors (not just outputs)
- Measurable metrics
- Pass/fail thresholds

Then produce output using [TEMPLATES.md](TEMPLATES.md). Validate with [RUBRIC.md](RUBRIC.md).

## Workflow
1. List agent capabilities to evaluate.
2. For each capability, define success criteria.
3. Design input scenarios covering normal, edge, and adversarial cases.
4. Define expected behaviors for each scenario.
5. Choose metrics and set thresholds.
6. Create evaluation harness or test specification.
7. Run the rubric check. Revise until it passes.

## Degrees of freedom
- **Low freedom**: Expected behaviors must be specific and verifiable.
- **Medium freedom**: Scenario design can vary based on agent scope.
- **Allowed variation**: Evaluation tooling and format as long as core criteria are testable.

## Failure modes to avoid
- Evaluating outputs only, not behaviors
- Missing adversarial or edge case scenarios
- Vague success criteria ("output is good")
- No baseline or threshold defined
- Testing happy path only
- Metrics that don't reflect actual quality

## References
- Templates: [TEMPLATES.md](TEMPLATES.md)
- Rubric: [RUBRIC.md](RUBRIC.md)
- Examples: [EXAMPLES.md](EXAMPLES.md)
- Evaluation patterns: [reference/evaluation-patterns.md](reference/evaluation-patterns.md)
- Metrics guide: [reference/metrics-guide.md](reference/metrics-guide.md)
