# Feedback Taxonomy

## Feedback source types

| Source type | Description | Credibility weight | Typical signals |
|-------------|-------------|-------------------|-----------------|
| user-research | Structured studies, usability tests, interviews | High | Direct observation of behavior and comprehension |
| support-ticket | Customer support inquiries and complaints | Medium-high | Volume patterns, specific confusion points |
| analytics | Behavioral data, funnel analysis, error rates | Medium-high | Quantitative patterns, drop-off points |
| pm-input | Product manager requirements, stakeholder requests | Medium | Business context, roadmap alignment |
| internal-review | QA, content review, engineering feedback | Medium | Implementation feasibility, edge cases |
| social-feedback | Social media, app reviews, community forums | Low-medium | Sentiment patterns, not individual complaints |

## Feedback type classification

| Feedback type | Definition | Context pack impact |
|---------------|------------|---------------------|
| gap | Missing information that should exist | Additive change |
| correction | Existing information is inaccurate or misleading | Modifying change |
| expansion | Existing information needs more detail or coverage | Additive or modifying |
| deprecation | Information is no longer relevant or accurate | Removing change |
| conflict | Feedback contradicts existing context or other feedback | Requires resolution before change |

## Change type classification

| Change type | Definition | Version impact |
|-------------|------------|----------------|
| additive | New content added without modifying existing | Minor version bump |
| modifying | Existing content changed | Minor or patch depending on scope |
| removing | Content deleted or deprecated | Major version bump if breaking |

## Credibility validation checklist

Before applying feedback, verify:

- [ ] Source is documented with reference ID or link
- [ ] Date received is recorded
- [ ] Sample size is sufficient (for research: n≥5; for tickets: pattern across ≥10 instances)
- [ ] Feedback represents actual behavior, not stated preference
- [ ] Feedback is not from a single outlier user or edge case
- [ ] Business context does not override validated user needs without explicit rationale

## Feedback that requires escalation

Escalate before applying when:

- Feedback contradicts established brand guidelines
- Change would affect regulatory or legal content
- Multiple high-credibility sources conflict
- Change impacts more than 3 context pack sections
- Feedback suggests fundamental feature redesign beyond content scope
