# Examples

## Example 1: App store review analysis

**Input:**
- Source: iOS and Android app store reviews
- Volume: 847 reviews
- Period: Q4 2024
- Context: Product team wants to understand rating drivers

**Output:**

```md
# App Store Review Analysis: Q4 2024

## Executive summary

Performance issues drove 62% of 1-2 star reviews this quarter, with "crash" and "slow" appearing in 234 reviews. Rating improved from 3.2 to 3.8 after the v4.2 performance update in November, suggesting performance investment is working.

### Volume overview
- **Total feedback analyzed:** 847 reviews
- **Time period:** Oct 1 - Dec 31, 2024
- **Source(s):** iOS App Store (512), Google Play (335)

### Top themes

| Theme | Frequency | Sentiment | Trend |
|-------|-----------|-----------|-------|
| Performance/Speed | 234 (28%) | Negative | ↓ (improving) |
| Feature requests | 189 (22%) | Neutral | → |
| Ease of use | 156 (18%) | Positive | → |
| Sync issues | 98 (12%) | Negative | ↑ (worsening) |
| Customer support | 73 (9%) | Mixed | → |

---

## Methodology

**Data source:** iOS App Store and Google Play public reviews
**Volume:** 847 reviews (all reviews with text, excluding rating-only)
**Time period:** Q4 2024
**Sampling:** Full review (not sampled)
**Coding approach:** Manual coding with two passes — theme, then sentiment
**Limitations:** 
- Reviews skew toward extremes (very happy or very unhappy users)
- Platform differences: iOS users more likely to mention sync; Android users more likely to mention crashes
- Only English-language reviews analyzed

---

## Theme 1: Performance/Speed

**Frequency:** 234 mentions (28% of total)
**Sentiment breakdown:** 8 positive, 201 negative, 25 neutral
**Trend:** Decreasing — 156 mentions in Oct, 78 mentions in Dec (after v4.2)

### What customers are saying

**Negative (pre-update):**
> "App crashes every time I try to open my dashboard. Unusable." — iOS, Oct 12, 2024

> "Takes 10+ seconds to load. I've switched to [competitor] because I can't wait." — Android, Oct 28, 2024

**Positive (post-update):**
> "Whatever you did in the last update worked. App is finally fast!" — iOS, Dec 3, 2024

### Insight
The v4.2 performance update had measurable impact. Negative performance mentions dropped 50% month-over-month. Users notice and appreciate improvements.

### Recommendation
Continue performance investment. Consider proactive communication about improvements — users who churned may not know the issues are resolved.

---

## Theme 2: Sync issues

**Frequency:** 98 mentions (12% of total)
**Sentiment breakdown:** 2 positive, 89 negative, 7 neutral
**Trend:** Increasing — 24 mentions in Oct, 41 mentions in Dec

### What customers are saying

**Negative:**
> "My data from the desktop app never shows up on mobile. I've tried everything." — iOS, Nov 15, 2024

> "Sync is broken. I made changes on my phone and they disappeared when I opened my laptop." — Android, Dec 8, 2024

### Insight
Sync issues are growing while other problems decrease. This may become the primary pain point now that performance is improving.

### Recommendation
Prioritize sync reliability investigation. Consider adding sync status indicator so users know when data is synchronized.

---

## Emerging signals

These patterns appeared too infrequently for confident analysis but warrant monitoring:

| Signal | Count | Notes |
|--------|-------|-------|
| Dark mode requests | 12 | All from iOS; may increase with iOS 18 adoption |
| Accessibility complaints | 8 | Specifically: font size, contrast |
| Pricing concerns | 7 | Appeared after Nov price increase announcement |

---

## Recommendations summary

| Priority | Recommendation | Theme | Confidence |
|----------|---------------|-------|------------|
| High | Investigate sync reliability | Sync issues | High |
| High | Communicate performance improvements to churned users | Performance | Medium |
| Medium | Add sync status indicator | Sync issues | Medium |
| Low | Monitor dark mode requests | Emerging | Low |
```

---

## Example 2: NPS comment analysis

**Input:**
- Source: NPS survey open-text responses
- Volume: 324 comments
- Period: January 2025
- Context: NPS dropped 8 points; leadership wants to understand why

**Output:**

```md
# NPS Comment Analysis: January 2025

## Executive summary

The 8-point NPS drop correlates strongly with billing change confusion. 47% of detractor comments (scores 0-6) mention billing, pricing, or unexpected charges. Promoters continue citing customer support as a strength.

### Volume overview
- **Total feedback analyzed:** 324 comments (of 1,247 survey responses)
- **Response rate:** 26% included comments
- **Time period:** Jan 1-31, 2025

### By NPS segment

| Segment | Responses | With comments | Top theme |
|---------|-----------|---------------|-----------|
| Promoters (9-10) | 423 | 89 (21%) | Support quality |
| Passives (7-8) | 498 | 112 (22%) | Feature requests |
| Detractors (0-6) | 326 | 123 (38%) | Billing confusion |

Note: Detractors more likely to leave comments (38% vs 21% for promoters)

---

## Detractor analysis (Primary focus)

### Theme: Billing confusion

**Frequency:** 58 of 123 detractor comments (47%)

**What's happening:**
January billing cycle was first after pricing restructure. Customers received higher bills without clear explanation.

**Representative quotes:**
> "My bill went up 40% with no warning. I had to call support to understand why." — Score: 2

> "You changed my plan without asking. Very disappointed in how this was handled." — Score: 3

> "I've been a customer for 5 years. I found out about the price increase from my credit card statement." — Score: 0

### Insight
The billing change itself may be acceptable, but the communication was insufficient. Detractors feel surprised and disrespected, not just overcharged.

### Recommendation
1. Send proactive explanation to all affected customers
2. Review billing communication workflow for future changes
3. Consider goodwill gesture for long-tenured customers who were surprised

---

## Promoter analysis (What's working)

### Theme: Customer support

**Frequency:** 41 of 89 promoter comments (46%)

**Representative quotes:**
> "Sarah in support solved my problem in 5 minutes after I'd been stuck for hours." — Score: 10

> "Best customer service I've experienced. They actually listen." — Score: 9

### Insight
Support quality is a significant loyalty driver. Protect this during cost optimization discussions.

---

## Recommendations summary

| Priority | Recommendation | Impact | Confidence |
|----------|---------------|--------|------------|
| Critical | Send billing explanation to affected customers | NPS recovery | High |
| High | Audit billing communication process | Prevent recurrence | High |
| Medium | Recognize support team performance | Retain strength | Medium |
```

---

## Example 3: Edge case — low-volume feedback with high stakes

**Input:**
- Source: Enterprise customer feedback
- Volume: 12 comments from 3 key accounts
- Challenge: Low volume but strategically important; can't apply normal quantification

**Output:**

```md
# Enterprise Account Feedback: [Account Names]

## Context

This analysis covers feedback from 3 enterprise accounts representing $2.4M ARR. Volume is too low for statistical analysis; findings should be treated as signals, not patterns.

### Caveats
- N=12 comments total
- All from accounts in active contract negotiations
- May not represent broader enterprise sentiment

---

## Account-by-account findings

### Account A: [Company Name]
**Comments:** 5
**Overall sentiment:** Concerned
**Key issues:**
1. SLA compliance questions (mentioned 3x)
2. Integration timeline concerns (mentioned 2x)

**Representative quote:**
> "We need written confirmation of uptime guarantees before we can proceed with expansion." — IT Director

**Recommended action:** Schedule call with legal to discuss SLA documentation

---

### Account B: [Company Name]
**Comments:** 4
**Overall sentiment:** Positive with requests
**Key issues:**
1. Feature request: SSO support (mentioned 2x)
2. Training availability (mentioned 1x)

**Representative quote:**
> "We're happy overall. SSO is the one thing holding back our rollout to the rest of the organization." — CTO

**Recommended action:** Prioritize SSO in roadmap discussion; offer interim training sessions

---

## Cross-account patterns

Despite low volume, one theme appeared across all 3 accounts:

**Security documentation:** Each account asked about security certifications or compliance documentation.

> "Do you have SOC 2 Type II?" — Account A
> "We need to see your security policies before procurement approves." — Account B
> "Our CISO is asking for pen test results." — Account C

**Recommended action:** Create enterprise security documentation package for sales enablement.

---

## Limitations

This analysis is based on 12 data points from strategically important but non-representative accounts. Do not generalize to broader customer base without additional research.
```
