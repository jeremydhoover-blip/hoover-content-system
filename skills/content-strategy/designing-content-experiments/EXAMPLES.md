# Examples

## Example 1: Landing page headline test

**Input:**
- Element: Homepage hero headline
- Goal: Increase demo requests
- Current conversion: 3.2% of visitors request demo
- Traffic: 50,000 visitors/month to homepage
- Hypothesis: Benefit-focused headline will outperform feature-focused

**Output:**

```md
# Experiment: Homepage headline—benefit vs. feature framing

## Overview
**Hypothesis:** If we change from feature-focused headline to benefit-focused headline, then demo request rate will increase, because users care about outcomes more than capabilities.
**Owner:** Marketing
**Status:** Design
**Start date:** March 1, 2026
**Planned end date:** March 22, 2026

---

## Hypothesis details

### What we're testing
Homepage hero headline copy

### Why we think this will work
- User research shows buyers ask "what does this do for me?" not "what features does this have?"
- Competitor analysis shows top performers lead with benefits
- Previous blog test showed benefit headlines had 15% higher CTR

### What we expect to learn
- If variant wins: Benefit framing resonates; apply to other pages
- If control wins: Our audience may be more technical/feature-driven
- If inconclusive: Need larger effect or different benefit angle

---

## Metrics

### Primary metric
**Metric:** Demo request conversion rate
**Current baseline:** 3.2%
**Minimum detectable effect:** 15% relative lift (3.2% → 3.68%)
**Direction:** Increase

### Guardrail metrics
| Metric | Acceptable range | Alert if |
|--------|------------------|----------|
| Bounce rate | ±10% of baseline | >10% increase |
| Time on page | ±15% of baseline | >15% decrease |
| Scroll depth | ±10% of baseline | >10% decrease |

---

## Design

### Control
**Headline:** "Advanced analytics platform with real-time dashboards"
**Subhead:** "Connect 200+ data sources. Build custom reports. Share with your team."

### Variant A
**Headline:** "Make better decisions with data you can trust"
**Subhead:** "See what's happening in your business right now—no data team required."

**Change from control:**
- Headline: Feature description → benefit/outcome
- Subhead: Capability list → value proposition

---

## Targeting

### Audience
- **Who:** All homepage visitors, new sessions
- **Exclusions:** Returning users (to avoid confusion), logged-in users

### Traffic allocation
| Group | Allocation |
|-------|------------|
| Control | 50% |
| Variant A | 50% |

### Randomization
**Method:** User-level (cookie-based)
**Sticky:** Yes

---

## Statistical parameters

### Sample size calculation
- **Baseline conversion:** 3.2%
- **Minimum detectable effect:** 15% relative (0.48% absolute)
- **Significance level:** 95%
- **Power:** 80%
- **Required sample per variant:** 24,500 users
- **Total sample needed:** 49,000 users

### Duration estimate
- **Daily homepage traffic:** 1,650 users (new sessions)
- **Days to reach sample:** 30 days
- **Planned duration:** 21 days (accepting higher MDE) or extend if needed

---

## Stopping criteria

### Stop early if:
- Guardrail metrics breached (bounce rate up >10%)
- Technical error discovered
- Reaching 99% confidence before planned duration

### Do not stop for:
- Early trends (positive or negative)
- Stakeholder requests for preliminary results

---

## Decision framework

| Outcome | Action |
|---------|--------|
| Variant wins (p<0.05, >15% lift) | Ship variant; test benefit framing on other pages |
| Control wins (p<0.05) | Keep control; investigate if benefit angle was wrong |
| No significant difference | Keep control; try stronger benefit differentiation |
| Guardrails breached | Stop; investigate bounce rate |
```

---

## Example 2: Help article format test

**Input:**
- Element: Help article structure
- Goal: Increase self-service success
- Current metric: 62% mark articles "helpful"
- Traffic: 8,000 article views/week
- Hypothesis: Adding TLDR summary will help skimmers

**Output:**

```md
# Experiment: Help article TLDR summary

## Overview
**Hypothesis:** If we add a TLDR summary box at the top of help articles, then article helpfulness rating will increase, because many users want quick answers without reading full article.
**Owner:** Content team
**Status:** Design

---

## Metrics

### Primary metric
**Metric:** "Was this helpful?" positive rate
**Current baseline:** 62%
**Minimum detectable effect:** 8% relative lift (62% → 67%)
**Direction:** Increase

### Guardrail metrics
| Metric | Acceptable range | Alert if |
|--------|------------------|----------|
| Support tickets from article viewers | ±5% | >5% increase |
| Article scroll depth | No floor | N/A (expected to decrease if TLDR works) |

---

## Design

### Control
Standard article format:
1. Introduction paragraph
2. Step-by-step instructions
3. Related articles

### Variant A
TLDR format:
1. **TLDR box:** 2-3 sentence summary with key action
2. Introduction paragraph  
3. Step-by-step instructions
4. Related articles

**TLDR box design:**
```
📋 Quick answer
[2-3 sentence summary]
[Key action or setting location]
```

---

## Targeting

### Audience
- **Who:** All users viewing help articles in pilot category (Account Settings)
- **Articles:** 15 articles in Account Settings category

### Traffic allocation
| Group | Allocation |
|-------|------------|
| Control | 50% |
| Variant A | 50% |

---

## Statistical parameters

- **Baseline:** 62%
- **MDE:** 8% relative (5% absolute)
- **Required per variant:** 1,500 responses
- **Weekly "helpful" responses:** ~400
- **Duration:** 8 weeks minimum

---

## Decision framework

| Outcome | Action |
|---------|--------|
| Variant wins | Roll out TLDR to all help articles |
| Control wins | Keep current format; investigate why summary didn't help |
| Inconclusive | Extend test or test different summary format |
```

---

## Example 3: Edge case — Low traffic experiment

**Input:**
- Element: Checkout error message copy
- Goal: Reduce checkout abandonment on errors
- Problem: Only ~500 error occurrences/month
- Constraint: Can't wait months for results

**Output:**

```md
# Experiment: Checkout error message copy (low traffic)

## Overview
**Hypothesis:** If we change error messages from technical to actionable, then error recovery rate will increase, because users will understand what to do.
**Owner:** UX Content

---

## Low traffic strategy

### Challenge
- 500 error occurrences/month
- Standard A/B test would require 6+ months

### Approach: Sequential testing with Bayesian analysis
- Ship variant to 100% (no holdout)
- Compare to historical baseline
- Use Bayesian credible intervals instead of frequentist significance
- Accept higher uncertainty in exchange for faster learning

### Alternative considered
- Qualitative testing: 5 user sessions observing error recovery
- Paired with quantitative to provide directional confidence

---

## Metrics

### Primary metric
**Metric:** Error recovery rate (users who complete checkout after error)
**Current baseline:** 34%
**Target improvement:** Any detectable positive change
**Measurement:** 8-week period pre vs. 8-week period post

### Guardrail metrics
| Metric | Baseline | Alert if |
|--------|----------|----------|
| Support tickets mentioning checkout | 45/week | >60/week |

---

## Design

### Control (historical)
**Error:** "Payment processing error. Code: PGW-4012"
**Recovery action:** User must figure out what to do

### Variant (new)
**Error:** "Your card was declined. Try a different card or contact your bank."
**Recovery action:** Clear next step provided

---

## Analysis plan

### Week 4 checkpoint
- Calculate Bayesian credible interval
- If 90% CI entirely above baseline: Consider shipping
- If 90% CI crosses baseline: Continue to week 8

### Week 8 analysis
- Report point estimate and credible interval
- Ship if >75% probability of improvement
- Document uncertainty in decision

---

## Limitations (documented)

- Cannot reach statistical significance with standard methods
- Results may be confounded by seasonal effects
- Decision made with acknowledged uncertainty
- Will monitor post-launch for regression

---

## Decision framework

| Outcome | Action |
|---------|--------|
| Probable improvement (>75%) | Ship; monitor closely |
| Unclear (<75% probability) | Qualitative research to investigate |
| Probable negative | Revert immediately |
```
