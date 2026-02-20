---
name: extracting-insights-from-feedback
description: Analyzes unstructured feedback data to identify patterns, sentiment, and actionable insights. Use when processing support tickets, app reviews, NPS comments, social mentions, or other customer feedback at scale.
---

# Extracting Insights from Feedback

## Quick start
Collect or infer:
- Feedback source(s) (reviews, tickets, NPS, social, etc.)
- Volume and time range
- Current categorization (if any)
- Business questions to answer
- Stakeholder needs (product, support, marketing)

Then produce output using [TEMPLATES.md](TEMPLATES.md). Validate with [RUBRIC.md](RUBRIC.md).

## Workflow
1. Define the business questions: What decisions will this analysis inform?
2. Sample or review full dataset depending on volume.
3. Develop coding taxonomy: categories, sentiment, severity.
4. Code feedback systematically — one pass per dimension.
5. Quantify patterns: frequency, trend over time, segment distribution.
6. Identify representative quotes for each major pattern.
7. Separate signal from noise: prioritize recurring themes over one-off complaints.
8. Connect patterns to actionable recommendations.
9. Document methodology and limitations.
10. Run the rubric check. Revise until it passes.

## Degrees of freedom
- **Low freedom**: Accurate representation of feedback, transparent methodology
- **Medium freedom**: Taxonomy design, sentiment classification, quote selection
- **High freedom**: Narrative framing, prioritization, visualization choices

Default: Quantify what can be quantified. Acknowledge limitations of unstructured data. Don't over-interpret sentiment.

## References
- Templates: [TEMPLATES.md](TEMPLATES.md)
- Rubric: [RUBRIC.md](RUBRIC.md)
- Examples: [EXAMPLES.md](EXAMPLES.md)
- Coding taxonomy: [reference/feedback-taxonomy.md](reference/feedback-taxonomy.md)
