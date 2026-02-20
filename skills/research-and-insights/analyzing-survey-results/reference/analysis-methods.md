# Survey Analysis Methods

## Question type analysis

Different question types require different analysis approaches:

### Rating scale questions (Likert)
**Example**: "How satisfied are you?" (1-5)

| Metric | When to use | How to calculate |
|--------|-------------|------------------|
| Mean | Interval-assumed data, comparing groups | Sum of (rating × count) / N |
| Median | Ordinal data, skewed distributions | Middle value when sorted |
| Distribution | Always report alongside mean | Frequency of each rating |
| Top-box % | Executive summaries | % selecting top 1-2 ratings |
| Bottom-box % | Problem identification | % selecting bottom 1-2 ratings |

**Interpretation guidelines**:
| Mean range | Interpretation |
|------------|----------------|
| 4.5+ | Strong positive |
| 4.0-4.4 | Positive |
| 3.5-3.9 | Moderate positive |
| 3.0-3.4 | Neutral/mixed |
| 2.5-2.9 | Moderate negative |
| <2.5 | Strong negative |

**Caution**: Always check distribution shape. A 3.0 mean from "all 3s" differs from "half 1s, half 5s."

---

### NPS (Net Promoter Score)
**Question**: "How likely are you to recommend...?" (0-10)

| Category | Ratings | Meaning |
|----------|---------|---------|
| Promoters | 9-10 | Actively recommend |
| Passives | 7-8 | Satisfied but unenthusiastic |
| Detractors | 0-6 | Unlikely to recommend, may discourage |

**Calculation**: NPS = % Promoters - % Detractors

**Benchmarks** (B2B SaaS):
| NPS range | Assessment |
|-----------|------------|
| 50+ | Excellent |
| 30-49 | Good |
| 10-29 | Average |
| 0-9 | Below average |
| <0 | Concerning |

**Reporting best practice**: Report NPS AND category distribution. NPS alone hides movement patterns.

---

### Multiple choice (single select)
**Example**: "Which feature do you use most?"

| Analysis | How to do it |
|----------|--------------|
| Frequency distribution | Count and % for each option |
| Mode | Most frequently selected option |
| Chi-square test | Compare distributions across segments |

**Visualization**: Bar chart, ordered by frequency or logical order.

---

### Multiple choice (multi-select)
**Example**: "Which features do you use? (Select all that apply)"

| Analysis | How to do it |
|----------|--------------|
| Frequency per option | Count selecting each (sums to >100%) |
| Average selections | Mean number of options selected per respondent |
| Co-occurrence | Which options are frequently selected together |

**Caution**: Percentages will sum to >100%. Always clarify "% of respondents who selected X."

---

### Ranking questions
**Example**: "Rank these features from most to least important"

| Analysis | How to do it |
|----------|--------------|
| Average rank | Mean rank position for each item |
| First-place frequency | % ranking each item #1 |
| Weighted score | Points by position (1st=N points, 2nd=N-1, etc.) |

**Caution**: Ranking forces differentiation that may not exist. Pair with importance ratings for validation.

---

### Open-ended questions
**Analysis approach**:

1. **Clean responses**: Remove blank, "N/A," off-topic
2. **Code themes**: Create category scheme (deductive or emergent)
3. **Count frequency**: How often each theme appears
4. **Extract quotes**: Select representative examples
5. **Check saturation**: Are themes exhaustive?

**Coding methods**:
| Method | When to use |
|--------|-------------|
| Deductive coding | You have predefined themes from hypotheses |
| Emergent coding | Themes come from the data itself |
| Multi-code | Responses can have multiple themes |
| Single-code | Each response gets one primary theme |

---

## Segment comparison

### Identifying meaningful differences
Not all numerical differences are meaningful. Consider:

| Factor | Guidance |
|--------|----------|
| Sample size | With n>100 per segment, 5+ point differences are usually meaningful |
| Practical significance | Does the difference change decisions? |
| Consistency | Does difference appear across related questions? |
| Statistical significance | p<0.05 is conventional threshold |

### Comparison tests by data type
| Data type | Comparison test |
|-----------|-----------------|
| Means (2 groups) | t-test |
| Means (3+ groups) | ANOVA |
| Proportions | Chi-square |
| Distributions | Mann-Whitney U |

**Caution**: Multiple comparisons inflate false positive risk. Adjust expectations or use Bonferroni correction.

---

## Data quality assessment

### Response rate benchmarks
| Rate | Assessment | Implication |
|------|------------|-------------|
| >50% | Excellent | Low non-response bias risk |
| 30-50% | Good | Moderate risk, report with caveat |
| 15-30% | Adequate | Flag potential bias |
| <15% | Low | Significant bias risk; interpret cautiously |

### Sample size guidelines
| Purpose | Minimum N | Rationale |
|---------|-----------|-----------|
| Directional insight | 30 | Central limit theorem minimum |
| Reliable percentages | 100+ | ±10% margin at 95% CI |
| Segment comparison | 30+ per segment | Statistical power |
| Precise measurement | 400+ | ±5% margin at 95% CI |

### Confidence intervals for proportions
| Sample size | Margin of error (95% CI) |
|-------------|--------------------------|
| 50 | ±14% |
| 100 | ±10% |
| 200 | ±7% |
| 400 | ±5% |
| 1000 | ±3% |

---

## Common biases to address

| Bias | What it is | How to mitigate |
|------|------------|-----------------|
| Non-response bias | People who didn't respond differ from those who did | Compare demographics to population; weight if possible |
| Selection bias | Sample isn't representative of target population | Clearly define and report sample vs. population |
| Social desirability | People give "acceptable" answers | Use indirect questions; emphasize anonymity |
| Acquiescence bias | People tend to agree with statements | Mix positively and negatively worded questions |
| Recency bias | People over-weight recent experiences | Ask about specific timeframes |
| Order effects | Earlier questions influence later ones | Randomize question/option order |

---

## Reporting precision

### When to use percentages vs. raw numbers
| Scenario | Use |
|----------|-----|
| n > 100 | Percentages with base noted |
| n = 30-100 | Both percentage and count |
| n < 30 | Raw counts only ("12 of 25 respondents") |

### Decimal precision
| Sample size | Precision |
|-------------|-----------|
| <100 | Whole numbers only (67%, not 67.3%) |
| 100-500 | One decimal if needed |
| >500 | One decimal |

### Avoiding over-precision
- "67% (n=50)" implies false precision → Use "about two-thirds"
- "3.47 out of 5" implies measurement precision surveys don't have → Use "3.5" or "between 3 and 4"
