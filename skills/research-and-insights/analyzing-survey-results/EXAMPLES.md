# Examples

## Example 1: Product satisfaction survey analysis

**Input:**
```
Survey: Quarterly product satisfaction
Responses: 847 (32% response rate)
Questions:
- Overall satisfaction (1-5 scale)
- Feature satisfaction (1-5 scale, 6 features)
- NPS question
- One open-ended: "What would you most like us to improve?"
Segments: Free vs. paid users
Business context: Prioritize roadmap for next quarter
```

**Output:**
```md
# Survey Analysis: Q4 Product Satisfaction

## Executive summary
- **Key finding 1**: Overall satisfaction remains stable (3.8/5) but hides segment divergence—paid users rate 4.2 while free users rate 3.4.
- **Key finding 2**: Search functionality is the lowest-rated feature (2.9/5) and the most-requested improvement in open-ended responses.
- **Key finding 3**: NPS dropped 8 points from Q3 (42 → 34), driven by passive-to-detractor movement.
- **Primary recommendation**: Prioritize search improvements—this is the intersection of lowest satisfaction and highest demand.

## Data quality overview
| Metric | Value | Assessment |
|--------|-------|------------|
| Responses collected | 847 | |
| Response rate | 32% | Adequate |
| Completion rate | 91% | Good |
| Collection period | Dec 1-15, 2025 | |
| Sample vs. population | Over-represents paid users (45% vs. 30% of base) | Slight paid skew |

### Known biases and limitations
- Paid users over-represented; overall scores may skew slightly positive
- Survey sent post-login; excludes churned users from feedback

---

## Key findings

### Finding 1: Satisfaction stable overall but diverging by segment
**Data point**: Overall satisfaction 3.8/5 (n=847), unchanged from Q3

| Rating | Count | Percentage |
|--------|-------|------------|
| 5 - Very satisfied | 178 | 21% |
| 4 - Satisfied | 356 | 42% |
| 3 - Neutral | 195 | 23% |
| 2 - Dissatisfied | 85 | 10% |
| 1 - Very dissatisfied | 33 | 4% |

**Segment comparison**:
| Segment | Mean satisfaction | N |
|---------|-------------------|---|
| Paid users | 4.2 | 382 |
| Free users | 3.4 | 465 |

Free users are significantly less satisfied (difference of 0.8 points, p<0.01). This gap widened from Q3 (was 0.5 points).

**Implication**: Aggregate satisfaction masks growing free-tier dissatisfaction. Risk of churn or negative word-of-mouth from free users.

### Finding 2: Search is clear pain point
**Data point**: Search rated 2.9/5 (n=847), lowest of 6 features

| Feature | Mean rating | Rank |
|---------|-------------|------|
| Dashboard | 4.1 | 1 |
| Reports | 3.9 | 2 |
| Notifications | 3.7 | 3 |
| Integrations | 3.5 | 4 |
| Settings | 3.2 | 5 |
| Search | 2.9 | 6 |

**Implication**: Search is a usability bottleneck. Low search satisfaction may be inflating friction across other features.

### Finding 3: NPS declining
**Data point**: NPS = 34 (n=847), down from 42 in Q3

| NPS category | Q4 | Q3 | Change |
|--------------|----|----|--------|
| Promoters (9-10) | 41% | 45% | -4pp |
| Passives (7-8) | 32% | 29% | +3pp |
| Detractors (0-6) | 27% | 23% | +4pp |

Movement is primarily passive-to-detractor. This is a warning signal for retention.

**Implication**: Address root causes before detractor volume impacts referrals.

---

## Open-ended response themes
**Question**: "What would you most like us to improve?"
**Codable responses**: 612 (72% of respondents)

| Theme | Count | % of responses | Representative quote |
|-------|-------|----------------|---------------------|
| Search improvements | 187 | 31% | "Search is basically useless—I can never find what I'm looking for." |
| Mobile experience | 124 | 20% | "Wish I could do more from my phone." |
| Speed/performance | 98 | 16% | "It's gotten slower over the past few months." |
| More integrations | 67 | 11% | "Need [Tool X] integration to make this work for us." |
| Pricing/value | 54 | 9% | "Hard to justify the cost for what I get on free tier." |

---

## Recommendations
| Priority | Recommendation | Supporting data | Owner |
|----------|----------------|-----------------|-------|
| P0 | Prioritize search UX improvements | Lowest feature rating (2.9) + top open-ended theme (31%) | Product |
| P1 | Investigate free-tier satisfaction drivers | 0.8 point satisfaction gap, widening | Product + CS |
| P2 | Performance audit | 16% of open-ended mentioned speed | Engineering |

---

## Appendix: Full response distributions
[Detailed frequency tables for all questions]
```

---

## Example 2: Small sample survey with caveats

**Input:**
```
Survey: Beta feature feedback
Responses: 47 (from 60 beta users, 78% response rate)
Questions: Usefulness rating, likelihood to use, open-ended feedback
Context: Deciding whether to launch feature to general availability
```

**Output:**
```md
# Survey Analysis: [Feature Name] Beta Feedback

## Executive summary
- **Key finding**: Majority of beta users (74%) rated the feature as useful or very useful, with strong intent to continue using.
- **Caveat**: Small sample (n=47) limits precision; treat as directional signal, not definitive.
- **Primary recommendation**: Proceed to GA with monitoring; confidence is moderate.

## Data quality overview
| Metric | Value | Assessment |
|--------|-------|------------|
| Responses collected | 47 | Small but expected for beta |
| Response rate | 78% | High—good representation of beta cohort |
| Population | 60 beta users | |

### Known biases and limitations
- **Self-selection**: Beta users opted in; may be more engaged than average user
- **Small sample**: Margins of error are wide; ±10-15% for percentages
- **No control group**: Can't compare to users without feature

---

## Key findings

### Finding 1: High perceived usefulness
**Data point**: 74% rated useful or very useful (n=47)

| Rating | Count | Percentage | 95% CI |
|--------|-------|------------|--------|
| Very useful | 18 | 38% | 25-53% |
| Useful | 17 | 36% | 23-51% |
| Neutral | 8 | 17% | 8-31% |
| Not useful | 4 | 9% | 3-20% |

Note: Wide confidence intervals due to sample size. True "useful or very useful" is likely between 60-85%.

**Implication**: Signal is positive but not definitive. Monitor closely post-GA.

### Finding 2: Strong continued use intent
**Data point**: 79% likely or very likely to continue using (n=47)

| Likelihood | Count | Percentage |
|------------|-------|------------|
| Very likely | 21 | 45% |
| Likely | 16 | 34% |
| Neutral | 6 | 13% |
| Unlikely | 4 | 8% |

**Implication**: Retention within beta cohort looks healthy.

---

## Open-ended themes
**Responses**: 39 (83% of respondents)

| Theme | Count | Representative quote |
|-------|-------|---------------------|
| Saves time | 14 | "This cuts my [task] time in half." |
| Needs refinement | 11 | "Works well but [specific edge case] doesn't work right." |
| Want more options | 8 | "Would love to be able to [extension]." |

---

## Recommendation
**Decision**: Proceed to GA with the following conditions:
1. Fix known edge cases mentioned in feedback (see appendix)
2. Set up monitoring for adoption and completion rates
3. Plan follow-up survey at GA+30 days with larger sample

**Confidence level**: Moderate—positive signal, but validate with larger sample post-launch.
```

---

## Example 3: Edge case — conflicting data

**Input:**
```
Survey: Feature prioritization
Responses: 312
Finding: 
- When asked "How important is X?" → 67% say very important
- When asked "Would you pay more for X?" → Only 18% say yes
Business context: Evaluating whether to build premium feature
```

**Output:**
```md
# Survey Analysis: [Feature X] Prioritization

## Executive summary
- **Key finding**: Stated importance (67% "very important") contradicts willingness to pay (18% "yes"). This is a common survey artifact—stated preference ≠ purchase intent.
- **Implication**: Feature is desired but may not drive conversion or justify premium pricing.
- **Recommendation**: Do not use stated importance as evidence for premium monetization.

## Data quality overview
| Metric | Value |
|--------|-------|
| Responses | 312 |
| Response rate | 28% |
| Completion rate | 94% |

---

## The discrepancy explained

### Stated importance
**Question**: "How important is [Feature X] to you?"
| Rating | Count | Percentage |
|--------|-------|------------|
| Very important | 209 | 67% |
| Somewhat important | 72 | 23% |
| Not important | 31 | 10% |

### Willingness to pay
**Question**: "Would you pay $X/month more for [Feature X]?"
| Response | Count | Percentage |
|----------|-------|------------|
| Yes | 56 | 18% |
| Maybe | 89 | 29% |
| No | 167 | 53% |

### Why this happens
This discrepancy is typical in survey research:
1. **Social desirability**: Saying something is "important" costs nothing
2. **Hypothetical bias**: People overstate intent in hypotheticals
3. **Price sensitivity**: "Important" doesn't mean "worth paying for"

---

## Recommendation
| Approach | Recommendation |
|----------|----------------|
| Premium feature | Do NOT build as premium-only; willingness to pay is too low |
| Free feature | Consider if 67% importance means differentiation value |
| Validation | Run A/B pricing test with real payment before committing |

## Next steps
1. Treat stated importance as directional interest, not purchase signal
2. If pursuing premium: run conjoint analysis or real pricing test
3. If pursuing free: validate usage post-launch, not just stated interest
```
