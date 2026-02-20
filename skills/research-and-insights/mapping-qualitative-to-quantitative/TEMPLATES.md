# Templates

## Qual-to-quant mapping table

```md
# Qualitative to Quantitative Mapping

## Source study
- **Study name**: [Name]
- **Method**: [Interview/Observation/etc.]
- **Sample**: [N participants, segment]
- **Date**: [When conducted]

## Theme-to-metric mapping

| Qual theme | Observable signal | Metric type | Metric definition | Collection method | Baseline | Target |
|------------|-------------------|-------------|-------------------|-------------------|----------|--------|
| [Theme from research] | [Behavior/attitude that indicates theme] | Behavioral / Attitudinal / Outcome | [Specific metric] | [How measured] | [Current state] | [Goal state] |

## Validation requirements
| Metric | Sample needed | Confidence level | Timeline |
|--------|---------------|------------------|----------|
| [Metric] | [N] | [Directional/Statistical] | [When] |

## Assumptions log
| Assumption | Risk if wrong | Validation approach |
|------------|---------------|---------------------|
| [Assumption] | [Impact] | [How to test] |
```

## Survey question derivation

```md
# Survey Questions from Qualitative Findings

## Finding: [Qualitative theme]

### Original insight
> "[Representative quote from research]"

**Observed in**: [X/N participants]
**Context**: [When/where this emerged]

### Derived survey questions

**Behavioral frequency**:
- In the past [timeframe], how often have you [behavior]?
  - Never / Rarely / Sometimes / Often / Always

**Attitude/agreement**:
- To what extent do you agree: "[Statement derived from theme]"
  - Strongly disagree / Disagree / Neutral / Agree / Strongly agree

**Satisfaction**:
- How satisfied are you with [aspect related to theme]?
  - Very dissatisfied / Dissatisfied / Neutral / Satisfied / Very satisfied

**Open validation**:
- [Open-ended question to capture nuance lost in closed questions]

### Question validity notes
- **Face validity**: [Does question obviously measure the theme?]
- **Risk of bias**: [Leading language, social desirability concerns]
- **Alternative interpretations**: [How might respondents misunderstand?]
```

## Metric specification

```md
# Metric Specification

## Metric name
[Clear, specific name]

## Qualitative origin
- **Source theme**: [Theme this metric measures]
- **Source study**: [Study name and date]
- **Confidence in link**: High / Medium / Low

## Definition
- **What it measures**: [Plain language description]
- **Formula**: [Exact calculation]
- **Unit**: [Percentage, count, score, etc.]

## Collection
- **Source**: [Analytics, survey, support, etc.]
- **Frequency**: [How often collected]
- **Segmentation**: [How to slice: user type, feature, etc.]

## Interpretation
- **Higher means**: [What increase indicates]
- **Lower means**: [What decrease indicates]
- **Thresholds**:
  - Red: [Value and meaning]
  - Yellow: [Value and meaning]
  - Green: [Value and meaning]

## Limitations
- **Does not capture**: [What this metric misses]
- **Can be gamed by**: [Behaviors that inflate without real improvement]
- **Confounds**: [Other factors that affect this metric]
```

## Measurement framework

```md
# Measurement Framework: [Initiative/Feature]

## Research foundation
| Study | Method | Key findings | Themes to measure |
|-------|--------|--------------|-------------------|
| [Study] | [Method] | [Findings] | [Themes] |

## Metric hierarchy

### North star metric
- **Metric**: [Primary outcome metric]
- **Why**: [How it connects to user and business value]
- **Qualitative origin**: [Source theme]

### Leading indicators
| Indicator | Type | Qualitative origin | Expected lead time |
|-----------|------|--------------------|--------------------|
| [Metric] | Behavioral / Attitudinal | [Theme] | [Days/weeks before north star moves] |

### Health metrics
| Metric | Purpose | Qualitative origin | Alert threshold |
|--------|---------|--------------------|-----------------| 
| [Metric] | [What it guards against] | [Theme] | [When to investigate] |

## Data collection plan
| Metric | Source | Owner | Frequency | Start date |
|--------|--------|-------|-----------|------------|
| [Metric] | [Source] | [Who] | [Cadence] | [When] |
```

## Variation guidance
| Element | Required | Flexible |
|---------|----------|----------|
| Qual theme origin | Yes, every metric | Specificity can vary |
| Observable signal | Yes | Wording can vary |
| Metric definition | Yes, must be precise | Format can vary |
| Baseline/target | Recommended | May be TBD initially |
| Assumptions log | Yes for new metrics | Can skip for established |
