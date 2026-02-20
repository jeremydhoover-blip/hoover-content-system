# Audit Frameworks

## Table of contents
- [Audit types and criteria](#audit-types-and-criteria)
- [Scoring frameworks](#scoring-frameworks)
- [Prioritization methods](#prioritization-methods)
- [Presenting findings effectively](#presenting-findings-effectively)

---

## Audit types and criteria

### Quantitative audit
Focus on measurable attributes.

| Criterion | Metric | Source |
|-----------|--------|--------|
| Traffic | Sessions, users, pageviews | Analytics |
| Engagement | Time on page, bounce rate | Analytics |
| SEO | Rankings, impressions, CTR | Search console |
| Conversion | Goal completions, conversion rate | Analytics |
| Freshness | Last modified date | CMS |
| Length | Word count | CMS/manual |

**Best for:** Establishing baseline, identifying underperformers, tracking progress

### Qualitative audit
Focus on content quality attributes.

| Criterion | Questions to answer |
|-----------|---------------------|
| Accuracy | Is information correct and current? |
| Completeness | Does it answer user questions fully? |
| Clarity | Is it easy to understand? |
| Brand alignment | Does it match voice and tone guidelines? |
| Accessibility | Is it usable by all audiences? |
| Actionability | Can users accomplish their goal? |

**Best for:** Identifying quality issues, brand alignment, user experience

### Combined audit
Most comprehensive approach.

| Phase | Focus | Output |
|-------|-------|--------|
| 1: Inventory | What exists? | Complete content list |
| 2: Quantitative | How is it performing? | Traffic and engagement data |
| 3: Qualitative | How good is it? | Quality scores |
| 4: Action | What should we do? | Prioritized recommendations |

---

## Scoring frameworks

### Simple 4-level (ROT)

| Score | Definition | Action |
|-------|------------|--------|
| **R**edundant | Duplicates other content | Merge |
| **O**utdated | Information no longer accurate | Update or remove |
| **T**rivial | Low value, low traffic | Remove |
| **Keep** | Valuable and current | No action |

### Quality matrix (5-point)

| Score | Quality | Performance | Action |
|-------|---------|-------------|--------|
| 5 | High | High | Promote, use as template |
| 4 | High | Low | Improve distribution |
| 3 | Medium | Medium | Standard maintenance |
| 2 | Low | High | Priority update |
| 1 | Low | Low | Remove or overhaul |

### Weighted scoring

Create custom score based on business priorities:

```
Content Score = (Traffic × 0.3) + (Quality × 0.4) + (Business Value × 0.3)
```

| Factor | Weight | Scoring |
|--------|--------|---------|
| Traffic | 30% | 1-5 based on percentile |
| Quality | 40% | 1-5 based on qualitative rubric |
| Business value | 30% | 1-5 based on alignment with priorities |

---

## Prioritization methods

### Traffic × Impact matrix

```
            High Impact
                 |
    PRIORITY 1   |   PRIORITY 2
   (High traffic,| (Low traffic,
    high impact) |  high impact)
-----------------+------------------
    PRIORITY 3   |   PRIORITY 4
   (High traffic,| (Low traffic,
    low impact)  |  low impact)
                 |
            Low Impact
```

| Quadrant | Example | Recommendation |
|----------|---------|----------------|
| P1 | High-traffic page with inaccurate info | Fix immediately |
| P2 | Low-traffic page blocking key user journey | Fix soon |
| P3 | High-traffic page with minor issues | Schedule for maintenance |
| P4 | Low-traffic page with minor issues | Defer or remove |

### Effort × Value matrix

| | Low Effort | High Effort |
|---|------------|-------------|
| **High Value** | Do first | Plan carefully |
| **Low Value** | Do if time allows | Don't do |

### MoSCoW for content

| Priority | Definition | Percentage guide |
|----------|------------|-----------------|
| **M**ust | Critical to fix | 10-20% |
| **S**hould | Important, not blocking | 20-30% |
| **C**ould | Nice to have | 30-40% |
| **W**on't | Not this cycle | Remainder |

---

## Presenting findings effectively

### For executives

**Lead with:**
- Business impact (revenue, support costs, brand risk)
- One-sentence summary
- Specific resource ask

**Minimize:**
- Methodology details
- Item-level data
- Technical jargon

**Format:** 1-page summary + appendix link

### For content teams

**Lead with:**
- Clear action items
- Prioritized list
- Effort estimates

**Include:**
- Specific URLs and issues
- Examples of good patterns
- Templates for fixes

**Format:** Detailed report with task list

### For product teams

**Lead with:**
- User impact
- Connection to product experience
- Specific content-product dependencies

**Include:**
- Journey mapping to content gaps
- Feature change implications
- Coordination needs

**Format:** Collaborative document with product context

### Visualization recommendations

| Finding type | Best visualization |
|--------------|-------------------|
| Distribution across categories | Pie or bar chart |
| Changes over time | Line chart |
| Traffic vs. quality | Scatter plot |
| Action breakdown | Stacked bar |
| Priority comparison | Matrix/quadrant |
| Item-level details | Table |
