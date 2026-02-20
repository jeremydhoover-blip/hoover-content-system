# Templates

## Executive summary (1 page max)

```md
# [Study Name] — Executive Summary

## Bottom line
[1-2 sentences: the single most important takeaway and its business implication]

## Key findings
1. **[Finding label]**: [Finding statement]. Impact: [business/product implication].
2. **[Finding label]**: [Finding statement]. Impact: [business/product implication].
3. **[Finding label]**: [Finding statement]. Impact: [business/product implication].

## Recommended actions
| Priority | Action | Owner | Finding link |
|----------|--------|-------|--------------|
| P0 | [Action] | [Team] | Finding #X |
| P1 | [Action] | [Team] | Finding #X |

## Study context
- **Method**: [Research method]
- **Participants**: [N] [participant type]
- **Confidence**: [High/Medium/Low] — [brief rationale]
```

## Design team summary

```md
# [Study Name] — Design Summary

## What users need
[2-3 sentences framing user goals and context]

## Behavioral insights
### [Insight 1 label]
- **Observed behavior**: [What users did]
- **Why it matters**: [Design implication]
- **Design direction**: [Suggested approach]

### [Insight 2 label]
- **Observed behavior**: [What users did]
- **Why it matters**: [Design implication]
- **Design direction**: [Suggested approach]

## Pain points to address
| Pain point | Severity | Current state | Opportunity |
|------------|----------|---------------|-------------|
| [Pain point] | High/Med/Low | [Current UX] | [Improvement] |

## Quotes to remember
> "[Verbatim quote]" — P[X], [context]

## Open questions
- [Question needing further research]
```

## Engineering team summary

```md
# [Study Name] — Technical Implications

## TL;DR
[2-3 sentences on what users need that affects technical decisions]

## User-reported technical issues
| Issue | Frequency | User impact | Technical area |
|-------|-----------|-------------|----------------|
| [Issue] | [X/N users] | [Impact] | [Frontend/Backend/Infra] |

## Performance expectations
- **Acceptable latency**: [User-stated or observed threshold]
- **Failure tolerance**: [How users reacted to errors]
- **Offline needs**: [Requirements for offline/degraded states]

## Mental models affecting architecture
- [User assumption about how system works] → [Technical implication]

## Data users expect
- [Data type users mentioned needing]
- [Data type users assumed was available]
```

## Stakeholder brief (email format)

```md
Subject: [Study name] findings — [key takeaway in 5 words]

Hi [Name],

We completed [study type] with [N] [participants]. Here's what matters for [their area]:

**The headline**: [1 sentence key finding]

**What this means for [their initiative]**:
- [Implication 1]
- [Implication 2]

**Recommended next step**: [Single clear action]

Full summary attached. Happy to walk through findings — let me know if [time] works.

[Your name]
```

## Variation guidance
| Element | Required | Flexible |
|---------|----------|----------|
| Bottom line / TL;DR | Yes | Placement can vary |
| Findings with implications | Yes | Number can be 3-7 |
| Confidence statement | Yes | Can be inline or section |
| Methodology details | Audience-dependent | Can omit for executives |
| Quotes | Recommended for design | Optional for engineering |
| Action recommendations | Yes | Format can vary |
