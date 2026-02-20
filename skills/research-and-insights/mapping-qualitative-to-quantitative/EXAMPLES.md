# Examples

## Example 1: User onboarding research to metrics

**Input:**
```
Qualitative study: New user onboarding interviews
Sample: 10 new users in first 2 weeks
Key themes:
1. "Information overload" - 7/10 felt overwhelmed by features shown upfront
2. "Aha moment" - 6/10 described a specific moment when value clicked
3. "Social proof need" - 5/10 wanted to see how others use the product
4. "Fear of mistakes" - 4/10 hesitated to try features due to fear of breaking something
Business context: Trying to improve day-7 retention
```

**Output:**
```md
# Qualitative to Quantitative Mapping

## Source study
- **Study name**: New User Onboarding Interviews
- **Method**: Semi-structured interviews
- **Sample**: 10 new users (first 2 weeks)
- **Date**: January 2026

## Theme-to-metric mapping

| Qual theme | Observable signal | Metric type | Metric definition | Collection method | Baseline | Target |
|------------|-------------------|-------------|-------------------|-------------------|----------|--------|
| Information overload | User closes/skips onboarding early | Behavioral | % of users who complete <50% of onboarding steps | Analytics | TBD | <20% |
| Information overload | User returns to help/docs in session 1 | Behavioral | Help article views in first session | Analytics | TBD | Decrease |
| Aha moment | User performs "value action" | Behavioral | % of users who [specific action] in first 3 sessions | Analytics | TBD | >60% |
| Aha moment | User self-reports value | Attitudinal | "I understand how [product] helps me" (agree/disagree) | In-app survey | TBD | >70% agree |
| Social proof need | User seeks examples | Behavioral | Template/example gallery views in first week | Analytics | TBD | Track only |
| Fear of mistakes | User avoids irreversible actions | Behavioral | Time to first [irreversible action] | Analytics | TBD | Decrease |
| Fear of mistakes | User reads warnings | Behavioral | Warning dialog "learn more" click rate | Analytics | TBD | Track only |

## Validation requirements
| Metric | Sample needed | Confidence level | Timeline |
|--------|---------------|------------------|----------|
| Onboarding completion | 500 new users | Statistical | 4 weeks |
| In-app survey | 200 responses | Directional | 2 weeks |
| Aha moment action | 500 new users | Statistical | 4 weeks |

## Assumptions log
| Assumption | Risk if wrong | Validation approach |
|------------|---------------|---------------------|
| [Specific action] = perceived value | Metric moves without retention impact | Correlate with D7 retention |
| Early onboarding exit = overwhelm | Could be confidence, not overwhelm | Exit survey on onboarding abandon |
| Help article views = confusion | Could be curiosity | Segment by subsequent completion rate |
```

---

## Example 2: Survey questions from interview themes

**Input:**
```
Theme: "Trust requires transparency"
From: Enterprise buyer interviews (8 participants)
Context: When asked about vendor evaluation, buyers emphasized needing to understand data handling, pricing logic, and company stability.
Representative quotes:
- "I need to know where my data lives before I can even consider you"
- "Hidden pricing is a dealbreaker. Just tell me what it costs."
- "How do I know you'll be around in 5 years?"
```

**Output:**
```md
# Survey Questions from Qualitative Findings

## Finding: Trust requires transparency

### Original insight
> "I need to know where my data lives before I can even consider you"
> "Hidden pricing is a dealbreaker. Just tell me what it costs."

**Observed in**: 8/8 participants
**Context**: Vendor evaluation criteria discussions

### Derived survey questions

**Data transparency (behavioral frequency)**:
- When evaluating software vendors, how often do you research their data handling practices before requesting a demo?
  - Never / Rarely / Sometimes / Often / Always

**Pricing transparency (attitude/agreement)**:
- To what extent do you agree: "I am less likely to engage with vendors who don't publish pricing information."
  - Strongly disagree / Disagree / Neutral / Agree / Strongly agree

**Company stability (importance)**:
- How important is public information about a vendor's financial stability when making purchase decisions?
  - Not at all important / Slightly / Moderately / Very / Extremely important

**Transparency satisfaction**:
- Based on your experience with [Company], how satisfied are you with the transparency of our:
  - Data handling practices: Very dissatisfied → Very satisfied
  - Pricing model: Very dissatisfied → Very satisfied
  - Company information: Very dissatisfied → Very satisfied

**Open validation**:
- What information do you wish vendors made more easily accessible during your evaluation process?

### Question validity notes
- **Face validity**: Questions directly address stated concerns from interviews
- **Risk of bias**: "Dealbreaker" language in Q2 may inflate agreement; consider neutral framing "I prefer vendors who..."
- **Alternative interpretations**: "Data handling practices" may be interpreted as security vs. privacy vs. location differently
```

---

## Example 3: Edge case — ambiguous qualitative theme

**Input:**
```
Theme: "Users feel the product is 'not for them'"
From: Churn interviews (6 churned users)
Context: Difficult to pinpoint—users expressed vague disconnect, mentioned seeing features they didn't need, feeling the product was "for bigger teams" or "for technical people"
Quotes:
- "I just felt like this wasn't built for someone like me"
- "There's a lot here I'll never use"
- "It feels very... enterprise-y?"
```

**Output:**
```md
# Qualitative to Quantitative Mapping

## Source study
- **Study name**: Churn Interviews Q1
- **Method**: Post-churn interviews
- **Sample**: 6 churned users
- **Date**: January 2026

## Theme decomposition
The theme "not for them" is composite. Decompose before measuring:

| Sub-theme | Observable signal | Confidence |
|-----------|-------------------|------------|
| Feature overwhelm | Sees features they don't use | High |
| Audience mismatch | Perceives product for different user type | Medium |
| Complexity perception | Feels product is too technical | Medium |
| Value misalignment | Core value prop doesn't resonate | Low (vague) |

## Theme-to-metric mapping

| Qual theme | Observable signal | Metric type | Metric definition | Collection method | Baseline | Target |
|------------|-------------------|-------------|-------------------|-------------------|----------|--------|
| Feature overwhelm | Inactive feature ratio | Behavioral | % of features never used by user at churn | Analytics | TBD | Decrease |
| Feature overwhelm | Self-report | Attitudinal | "This product has too many features I don't need" | Survey | TBD | <30% agree |
| Audience mismatch | Self-identification | Attitudinal | "This product is designed for people like me" | Survey | TBD | >60% agree |
| Complexity perception | Help-seeking | Behavioral | Support tickets per user in first month | Support data | TBD | Decrease |
| Complexity perception | Self-report | Attitudinal | "I find [product] easy to use" | Survey | TBD | >70% agree |

## Validation requirements
| Metric | Sample needed | Confidence level | Timeline |
|--------|---------------|------------------|----------|
| Feature usage analysis | 200 churned users | Directional | Retroactive |
| Survey (active users) | 300 responses | Directional | 2 weeks |
| Survey (churned users) | 100 responses | Directional | 4 weeks |

## Assumptions log
| Assumption | Risk if wrong | Validation approach |
|------------|---------------|---------------------|
| Low feature usage = overwhelm | Could be irrelevant features, not overwhelm | Cross-reference with survey responses |
| "Not for me" is measurable via agreement | May be post-hoc rationalization | Compare pre-churn vs. churned survey responses |
| Sub-themes are distinct | May be overlapping/correlated | Factor analysis on survey responses |

## Limitations
- **Ambiguity risk**: "Not for them" is subjective; metrics may capture symptoms, not root cause
- **Recommended approach**: Treat initial metrics as hypotheses; validate with A/B tests on interventions
```

---

## Example 4: Leading indicators from outcome research

**Input:**
```
Study: Customer success interviews
Outcome: Understanding what predicts successful long-term customers
Key themes from successful customers:
1. Early "quick win" - accomplished something valuable in first week
2. Found "their workflow" - customized product to their process
3. Team adoption - got colleagues using it too
4. Regular habit - became part of daily/weekly routine
Business need: Identify at-risk accounts earlier
```

**Output:**
```md
# Measurement Framework: Customer Success Prediction

## Research foundation
| Study | Method | Key findings | Themes to measure |
|-------|--------|--------------|-------------------|
| Success interviews | Interviews with 12 high-LTV customers | Common early behaviors | Quick win, workflow fit, team adoption, habit formation |

## Metric hierarchy

### North star metric
- **Metric**: 12-month retention rate
- **Why**: Directly measures successful long-term customer outcome
- **Qualitative origin**: Definition of "successful" customer

### Leading indicators
| Indicator | Type | Qualitative origin | Expected lead time |
|-----------|------|--------------------|--------------------|
| Time to first [value action] | Behavioral | "Quick win" theme | 60-90 days |
| Custom configuration created | Behavioral | "Found their workflow" theme | 30-60 days |
| Invited team member count | Behavioral | "Team adoption" theme | 30-60 days |
| Weekly active days | Behavioral | "Regular habit" theme | 14-30 days |

### Health metrics
| Metric | Purpose | Qualitative origin | Alert threshold |
|--------|---------|--------------------|-----------------| 
| Days since last login | Guards against silent churn | Habit theme inverse | >14 days |
| Support ticket sentiment | Early dissatisfaction signal | Not from study | Negative trend |

## Data collection plan
| Metric | Source | Owner | Frequency | Start date |
|--------|--------|-------|-----------|------------|
| Time to first [value action] | Product analytics | Data team | Daily | Immediate |
| Custom configuration created | Product analytics | Data team | Daily | Immediate |
| Invited team member count | Product analytics | Data team | Daily | Immediate |
| Weekly active days | Product analytics | Data team | Weekly | Immediate |
| Days since last login | Product analytics | CS team | Daily alert | Immediate |
```
