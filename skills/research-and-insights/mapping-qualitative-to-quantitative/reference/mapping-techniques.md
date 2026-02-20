# Mapping Techniques

## Core principle
Every quantitative metric must trace to a qualitative finding. The metric is only valid if it genuinely captures what the qualitative research revealed.

---

## Construct type mapping

Different qualitative findings require different measurement approaches:

| Qualitative finding type | Construct type | Best measurement | Example |
|--------------------------|----------------|------------------|---------|
| What users **do** | Behavioral | Analytics, observation | "Users check notifications first thing" → notification view time |
| What users **think** | Cognitive | Survey, interview | "Users don't understand pricing" → comprehension quiz |
| What users **feel** | Attitudinal | Survey, ratings | "Users feel frustrated by wait" → satisfaction rating |
| What users **want** | Preferential | Survey, choice tasks | "Users want simpler options" → preference ranking |
| What users **achieve** | Outcome | Analytics, success metrics | "Users complete tasks faster" → task completion time |

---

## Observable signal derivation

Transform abstract themes into concrete observables:

### Process
1. **State the theme**: What qualitative insight?
2. **Define extremes**: What would "maximum" and "zero" look like?
3. **Identify midpoint signals**: What behavior/attitude sits between?
4. **Select measurable proxy**: What can we actually capture?

### Example
```
Theme: "Users feel ownership over their workspace"

Maximum: User has heavily customized, named, organized their space
Zero: User uses defaults, hasn't personalized anything
Midpoint signals: Some customization, saved preferences, named items
Measurable proxy: Number of customizations made in first 30 days
```

---

## Measurement method selection

| Method | Best for | Limitations | When to use |
|--------|----------|-------------|-------------|
| **Product analytics** | Behaviors, actions, patterns | Can't capture why, intent | When action is observable in product |
| **Surveys** | Attitudes, perceptions, preferences | Self-report bias, fatigue | When need to measure perception directly |
| **Behavioral observation** | Context, workarounds, process | Small sample, observer effect | When analytics miss context |
| **Support/feedback data** | Pain points, failures | Skewed to negative, vocal users | When measuring friction or failure |
| **Transaction data** | Outcomes, conversions, value | Attribution challenges | When measuring business outcomes |

---

## Survey question transformation

### From quote to question

| Quote type | Question approach | Example |
|------------|-------------------|---------|
| Frequency statement ("I always...") | Behavioral frequency | "How often do you [behavior]?" |
| Preference statement ("I prefer...") | Preference/importance | "How important is [feature] to you?" |
| Attitude statement ("I feel...") | Agreement scale | "To what extent do you agree: [statement]" |
| Comparison ("X is better than Y") | Comparative choice | "Which do you prefer: X or Y?" |
| Satisfaction ("I'm happy/unhappy with...") | Satisfaction scale | "How satisfied are you with [aspect]?" |

### Avoiding bias

| Bias type | Example | Fix |
|-----------|---------|-----|
| Leading | "How much do you love feature X?" | "How would you rate feature X?" |
| Double-barreled | "Is it fast and easy?" | Split into two questions |
| Loaded | "Do you waste time on...?" | Neutral language: "How much time do you spend on...?" |
| Social desirability | "Do you read documentation?" | Behavioral: "When did you last consult documentation?" |

---

## Threshold definition

### Severity-based thresholds
When qualitative research reveals a pain point, use severity language to define thresholds:

| Qualitative severity | Metric threshold | Example |
|---------------------|------------------|---------|
| "Dealbreaker" / "I'd leave" | Red / Critical | >5% experience this |
| "Frustrating" / "Annoying" | Yellow / Warning | >15% experience this |
| "Minor" / "Not ideal" | Watch | >30% experience this |
| "Doesn't bother me" | Acceptable | Below other thresholds |

### Frequency-based thresholds
When qualitative research reveals prevalence:

| Qualitative prevalence | Statistical threshold |
|-----------------------|----------------------|
| "Everyone" / "Always" | >80% |
| "Most" / "Usually" | 60-80% |
| "Many" / "Often" | 40-60% |
| "Some" / "Sometimes" | 20-40% |
| "Few" / "Rarely" | <20% |

---

## Validation matrix

Before finalizing metrics, validate each:

| Validation check | Question | Red flag |
|------------------|----------|----------|
| **Face validity** | Does this metric obviously measure the theme? | Need to explain why it's relevant |
| **Construct validity** | Could another factor explain metric changes? | Many confounding variables |
| **Actionability** | Would changes in this metric change decisions? | "Interesting but so what?" |
| **Feasibility** | Can we actually collect this data? | Requires new instrumentation |
| **Gaming risk** | Could this be inflated without real improvement? | Easy to manipulate |

---

## Composite theme decomposition

When qualitative themes are broad or vague:

### Decomposition process
1. List all quotes/observations under the theme
2. Group by specific sub-themes
3. Identify measurable sub-theme
4. Create separate metrics for each
5. Decide: composite score or separate tracking?

### Example
```
Broad theme: "Product feels overwhelming"

Sub-themes:
- Too many features visible → Feature count exposure
- Don't know where to start → First action time  
- Afraid to break something → Error/undo action ratio
- Can't find what I need → Search frequency

Decision: Track separately (different intervention types)
```

---

## Leading vs. lagging indicator selection

| Indicator type | Definition | Use for | Example |
|----------------|------------|---------|---------|
| **Leading** | Predicts future outcome | Early warning, intervention | Day-7 engagement → Predicts retention |
| **Lagging** | Measures final outcome | Success measurement | 90-day retention |
| **Coincident** | Moves with outcome | Real-time monitoring | Weekly active usage |

### From qualitative to leading indicators
Qualitative research often reveals what successful users do early. Use these to build leading indicators:

```
Qualitative finding: "Successful users mentioned setting up [feature] in first week"
Leading indicator: [Feature] setup in first 7 days
Lagging indicator: 90-day retention
Hypothesis: Early [feature] setup predicts retention
Validation: Correlation analysis
```
