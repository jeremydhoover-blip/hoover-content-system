# Templates

## Default experiment design

```md
# Experiment: [Experiment name]

## Overview
**Hypothesis:** If we [change], then [outcome], because [rationale].
**Owner:** [Name]
**Status:** Design / Running / Analyzing / Complete
**Start date:** [Date]
**Planned end date:** [Date]

---

## Hypothesis details

### What we're testing
[Specific element being changed]

### Why we think this will work
[Evidence or reasoning supporting the hypothesis]

### What we expect to learn
- If variant wins: [Implication]
- If control wins: [Implication]
- If inconclusive: [What we'll do next]

---

## Metrics

### Primary metric
**Metric:** [Exactly what we're measuring]
**Current baseline:** [Current value]
**Minimum detectable effect:** [% change we want to detect]
**Direction:** [Increase / Decrease]

### Guardrail metrics
| Metric | Acceptable range | Alert if |
|--------|------------------|----------|
| [Guardrail 1] | [Range] | [Outside range] |
| [Guardrail 2] | [Range] | [Outside range] |

*Experiment is invalid if guardrails are breached.*

---

## Design

### Control
**Description:** [Current experience]
**Screenshot/copy:** [Link or embed]

### Variant A
**Description:** [Changed experience]
**Screenshot/copy:** [Link or embed]
**Change from control:** [Specific difference]

### Variant B (if applicable)
**Description:** [Changed experience]
**Screenshot/copy:** [Link or embed]
**Change from control:** [Specific difference]

---

## Targeting

### Audience
- **Who:** [Target user segment]
- **Exclusions:** [Who's excluded and why]

### Traffic allocation
| Group | Allocation |
|-------|------------|
| Control | [X%] |
| Variant A | [X%] |
| Variant B | [X%] |
| Holdout | [X%] |

### Randomization
**Method:** [User-level / Session-level]
**Sticky:** [Yes/No—user sees same variant across sessions]

---

## Statistical parameters

### Sample size calculation
- **Baseline conversion:** [X%]
- **Minimum detectable effect:** [Y%]
- **Significance level (α):** 0.05 (95% confidence)
- **Power (1-β):** 0.80 (80% power)
- **Required sample per variant:** [N users]
- **Total sample needed:** [N × variants]

### Duration estimate
- **Daily traffic to experiment:** [N users]
- **Days to reach sample:** [N days]
- **Planned duration:** [N days + buffer]

---

## Stopping criteria

### Stop early if:
- [ ] Primary metric shows >95% probability of winner with required sample
- [ ] Guardrail metrics breached (stop and investigate)
- [ ] Technical error affecting results

### Do not stop for:
- Early positive or negative trends before sample size reached
- Stakeholder pressure for results

---

## Decision framework

| Outcome | Action |
|---------|--------|
| Variant wins (statistically significant) | Ship variant to 100% |
| Control wins (statistically significant) | Keep control; document learning |
| No significant difference | [Keep control OR extend test OR iterate variant] |
| Guardrails breached | Investigate; do not ship variant |

---

## Results (to be completed)

### Summary
**Outcome:** [Variant / Control / Inconclusive]
**Confidence:** [Statistical significance]
**Primary metric change:** [+/-X%]

### Data
| Variant | Users | Conversions | Rate | vs Control |
|---------|-------|-------------|------|------------|
| Control | [N] | [N] | [X%] | — |
| Variant A | [N] | [N] | [X%] | [+/-X%] |

### Learnings
[What we learned regardless of outcome]

### Next steps
[Follow-up experiments, implementation, or iterations]
```

## Sample size calculator reference

```
Required sample size per variant:

n = (2 × (Z_α/2 + Z_β)² × p × (1-p)) / (MDE)²

Where:
- Z_α/2 = 1.96 for 95% confidence
- Z_β = 0.84 for 80% power
- p = baseline conversion rate
- MDE = minimum detectable effect (absolute)

Quick reference (per variant, 95% confidence, 80% power):
| Baseline | 5% lift | 10% lift | 20% lift |
|----------|---------|----------|----------|
| 1% | 310,000 | 78,000 | 20,000 |
| 5% | 60,000 | 15,000 | 4,000 |
| 10% | 28,000 | 7,000 | 2,000 |
| 20% | 12,500 | 3,200 | 800 |
```
