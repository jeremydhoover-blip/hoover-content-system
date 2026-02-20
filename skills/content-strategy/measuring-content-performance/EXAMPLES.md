# Examples

## Example 1: Help center content measurement

**Input:**
- Content type: Help articles and documentation
- Business goal: Reduce support costs
- Available data: Help center analytics, support ticket system
- Challenge: Prove content value to leadership

**Output:**

```md
# Content Measurement Framework: Help Center

## Business alignment

### Content goal
Enable users to solve problems without contacting support.

### Business outcome supported
Reduce cost per support interaction by increasing self-service resolution.

### Hypothesis
If we improve help content quality and discoverability, then users will successfully self-serve, resulting in fewer support tickets.

---

## Metrics hierarchy

### North star metric
**Metric:** Self-service success rate
**Definition:** (Users who viewed help content and didn't contact support within 24 hours) / (Total users who viewed help content) × 100
**Target:** 75%
**Data source:** Help center analytics + support ticket system (matched by user ID)

### Leading indicators
| Metric | Definition | Target | Data source | Frequency |
|--------|------------|--------|-------------|-----------|
| Article completion rate | % of users who scroll to bottom or click "helpful" | 70% | Help center analytics | Weekly |
| Search success rate | Searches that result in article click (not refined search) | 65% | Help center analytics | Weekly |
| Time to first helpful content | Median seconds from search to article view | <30 sec | Help center analytics | Weekly |

### Lagging indicators
| Metric | Definition | Target | Data source | Frequency |
|--------|------------|--------|-------------|-----------|
| Support ticket volume | Total tickets submitted | -20% YoY | Support system | Monthly |
| Tickets with "no docs" tag | Tickets where user couldn't find help content | <5% | Support system | Monthly |
| Cost per resolution | Total support cost / tickets resolved | -15% | Finance + Support | Quarterly |

### Health metrics (guardrails)
| Metric | Definition | Acceptable range | Alert if |
|--------|------------|------------------|----------|
| Article accuracy complaints | Support tickets citing incorrect docs | <1% of tickets | >2% |
| Content freshness | % of articles updated in last 6 months | >80% | <70% |

---

## Baselines and targets

| Metric | Current baseline | Q1 target | Q2 target | EOY target |
|--------|------------------|-----------|-----------|------------|
| Self-service success rate | 62% | 68% | 72% | 75% |
| Article completion rate | 55% | 60% | 65% | 70% |
| Support ticket volume | 10,000/mo | 9,000 | 8,500 | 8,000 |

---

## Reporting

### Cadence
- **Weekly:** Leading indicators reviewed by content team
- **Monthly:** Full scorecard reviewed with Support leadership
- **Quarterly:** Business impact presentation to executive team

---

## Value calculation
At $15 average cost per ticket:
- Current: 10,000 tickets × $15 = $150,000/month
- Target: 8,000 tickets × $15 = $120,000/month
- **Annual savings potential: $360,000**
```

---

## Example 2: Marketing content measurement

**Input:**
- Content type: Blog posts, landing pages
- Business goal: Drive qualified leads
- Available data: GA4, CRM
- Challenge: Connect content to pipeline

**Output:**

```md
# Content Measurement Framework: Marketing Content

## Business alignment

### Content goal
Attract and convert qualified prospects through educational content.

### Business outcome supported
Pipeline generation and revenue attribution.

### Hypothesis
If we create content that addresses buyer pain points, then prospects will engage and convert, resulting in qualified pipeline.

---

## Metrics hierarchy

### North star metric
**Metric:** Content-attributed pipeline
**Definition:** Pipeline value from opportunities where first touch was content
**Target:** $2M/quarter
**Data source:** CRM (Salesforce) with UTM tracking

### Leading indicators
| Metric | Definition | Target | Data source | Frequency |
|--------|------------|--------|-------------|-----------|
| Qualified content engagement | Sessions >2 min + 2+ pages OR form start | 5,000/mo | GA4 | Weekly |
| Email capture rate | Form submissions / sessions | 3% | GA4 | Weekly |
| Content-influenced MQLs | MQLs who engaged with content pre-conversion | 60% of MQLs | CRM + GA4 | Weekly |

### Lagging indicators
| Metric | Definition | Target | Data source | Frequency |
|--------|------------|--------|-------------|-----------|
| Content-attributed revenue | Closed-won where content was first touch | $500K/quarter | CRM | Quarterly |
| Content ROI | (Revenue attributed - content cost) / cost | 3x | CRM + Finance | Quarterly |

### Health metrics (guardrails)
| Metric | Definition | Acceptable range | Alert if |
|--------|------------|------------------|----------|
| Bounce rate | Single-page sessions | <70% | >75% |
| Brand search lift | Branded searches after content campaigns | >0% | Declining |

---

## Attribution model

**Model:** First-touch attribution for content
**Lookback window:** 90 days
**Rules:**
- If first touchpoint is blog/content page, credit content
- Multi-touch: Content gets credit if in path (weighted)

---

## Content scoring

| Content type | Engagement weight | Conversion weight |
|--------------|-------------------|-------------------|
| Blog post | 1x | 1x |
| Gated guide | 2x | 3x |
| Case study | 3x | 4x |
| Comparison page | 2x | 5x |

---

## Reporting

### Dashboard sections
1. Traffic and engagement (leading)
2. Conversion metrics (leading)
3. Pipeline and revenue (lagging)
4. Content-level performance (detail)
```

---

## Example 3: Edge case — Limited data environment

**Input:**
- Content type: Product UI copy
- Business goal: Improve task completion
- Challenge: No dedicated content analytics; must proxy with available data
- Available: Product analytics (clicks, task completion), support tickets

**Output:**

```md
# Content Measurement Framework: UI Copy

## Constraints
- No direct content measurement tools
- Must use proxy metrics from product analytics
- Qualitative data from support and research

---

## Proxy measurement approach

### What we can measure
| Metric | What it proxies | Data source |
|--------|-----------------|-------------|
| Task completion rate | Content clarity (users understand what to do) | Product analytics |
| Error encounter rate | Content helpfulness (users avoid mistakes) | Product analytics |
| Support tickets mentioning "unclear" | Content confusion | Support system (keyword search) |
| Time on task | Content scannability (faster = clearer) | Product analytics |

### What we can't measure (documented gaps)
| Gap | Why | Workaround |
|-----|-----|------------|
| Direct copy readability | No per-string analytics | Pre-launch testing |
| A/B test on copy | Not instrumented | Coordinate with Product for tests |
| User sentiment on copy | No survey mechanism | Periodic usability studies |

---

## Metrics hierarchy

### North star metric
**Metric:** First-attempt task success rate
**Definition:** Users who complete task without errors or backtracking / total attempts
**Proxy assumption:** If copy is clear, users succeed first try
**Target:** 85%
**Data source:** Product analytics

### Supporting indicators
| Metric | Definition | Target | Data source |
|--------|------------|--------|-------------|
| Error message trigger rate | % of sessions triggering error | <10% | Product analytics |
| "Confused" support tickets | Tickets with unclear/confusing keywords | <3% of tickets | Support (manual tag) |
| Feature adoption rate | % of users who try new feature post-launch | 40% in first month | Product analytics |

---

## Qualitative measurement

Since quantitative data is limited:

### Monthly review
- Sample 10 support tickets with content complaints
- Categorize by content issue type
- Track trends over time

### Quarterly research
- 5 user interviews focused on content comprehension
- Task-based testing with think-aloud protocol
- Before/after comparison for major copy changes

---

## Reporting

### Format
Narrative + metrics hybrid (given data limitations)

### Template
"This month, first-attempt task success was [X%], [up/down] from [Y%]. We saw [N] support tickets related to content confusion, primarily about [area]. Qualitative research suggested [insight]."
```
