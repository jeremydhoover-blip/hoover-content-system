# Templates

## Default audit report structure

```md
# Agent Behavior Audit: [Agent Name]

## Audit metadata
- **Audit period**: [Date range]
- **Sample size**: [N interactions]
- **Sampling method**: [Random / Stratified / Triggered / Exhaustive]
- **Auditor**: [Name/Team]
- **Audit date**: [Date]

## Executive summary
- **Overall compliance rate**: [X%]
- **Critical issues found**: [Count]
- **Top failure category**: [Category name]
- **Recommended priority action**: [One-line summary]

## Evaluation criteria
| Criterion | Source | Weight |
|-----------|--------|--------|
| [Criterion 1] | [Spec reference] | [Critical/Major/Minor] |
| [Criterion 2] | [Spec reference] | [Critical/Major/Minor] |

## Findings by category

### [Category 1]: [Category name]
- **Rate**: [X% of samples]
- **Severity**: [Critical/Major/Minor]
- **Pattern**: [Description of common failure pattern]
- **Example IDs**: [interaction-123, interaction-456]
- **Root cause hypothesis**: [Why this is happening]

### [Category 2]: [Category name]
[Same structure]

## Sample analysis

### Correct behavior examples
| ID | User input | Agent response | Why correct |
|----|------------|----------------|-------------|
| [ID] | [Summary] | [Summary] | [Criterion met] |

### Incorrect behavior examples
| ID | User input | Agent response | Failure | Severity |
|----|------------|----------------|---------|----------|
| [ID] | [Summary] | [Summary] | [What went wrong] | [Level] |

## Metrics summary
| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| [Metric 1] | [Target] | [Actual] | [Pass/Fail] |
| [Metric 2] | [Target] | [Actual] | [Pass/Fail] |

## Recommendations
| Priority | Issue | Recommendation | Effort | Impact |
|----------|-------|----------------|--------|--------|
| P0 | [Issue] | [Specific action] | [S/M/L] | [S/M/L] |
| P1 | [Issue] | [Specific action] | [S/M/L] | [S/M/L] |

## Appendix
- Full interaction logs: [Link]
- Evaluation rubric: [Link]
- Previous audit comparison: [Link if applicable]
```

## Finding entry format

```md
**Finding [ID]**: [Title]
- **Severity**: [Critical/Major/Minor]
- **Frequency**: [X% of samples / N occurrences]
- **Description**: [What the agent did wrong]
- **Expected behavior**: [What should have happened]
- **Impact**: [User impact, business impact, safety impact]
- **Example**: [Specific interaction reference]
- **Recommendation**: [How to fix]
```

## Interaction annotation format

```md
**Interaction [ID]**
- **Timestamp**: [ISO timestamp]
- **User segment**: [If relevant]
- **Input**: "[User message]"
- **Output**: "[Agent response]"
- **Evaluation**:
  - [Criterion 1]: [Pass/Fail] — [Note]
  - [Criterion 2]: [Pass/Fail] — [Note]
- **Overall**: [Correct/Incorrect/Edge case/Unsafe]
- **Notes**: [Additional observations]
```
