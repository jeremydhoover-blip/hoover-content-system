---
name: designing-content-experiments
description: Designs and documents A/B tests and experiments for content optimization. Use when testing messaging, content formats, or user experience hypotheses.
---

# Designing Content Experiments

## Quick start
Collect or infer:
- Hypothesis to test
- Success metric and current baseline
- Audience and traffic volume available
- Technical constraints (what can be tested)
- Timeline and decision criteria

Then produce output using [TEMPLATES.md](TEMPLATES.md). Validate with [RUBRIC.md](RUBRIC.md).

## Workflow
1. Define clear, falsifiable hypothesis
2. Identify primary metric and guardrail metrics
3. Calculate required sample size for statistical significance
4. Design control and variant(s)
5. Document targeting and traffic allocation
6. Set duration and stopping criteria
7. Define decision framework (what actions follow which outcomes)
8. Run the rubric check. Revise until it passes.

## Degrees of freedom
**Freedom level: Low**
- Default: follow templates exactly
- Allowed variation: number of variants (recommend 2-3 max), specific metrics tested—as long as rubric passes
- Strict constraints: Must include sample size calculation; must define stopping criteria; must have decision framework

## State awareness
- **First experiment**: Start simple (A/B, single variable); focus on learning process
- **Mature program**: Can run multivariate tests; consider interaction effects
- **Low traffic**: Longer duration or sequential testing; consider Bayesian approach
- **High stakes**: Require higher confidence level (99% vs 95%)

## References
- Templates: [TEMPLATES.md](TEMPLATES.md)
- Rubric: [RUBRIC.md](RUBRIC.md)
- Examples: [EXAMPLES.md](EXAMPLES.md)
