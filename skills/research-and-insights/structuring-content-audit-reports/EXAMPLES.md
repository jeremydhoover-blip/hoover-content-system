# Examples

## Example 1: Full site content audit

**Input:**
- Scope: Marketing website (312 pages)
- Audience: Content team and VP Marketing
- Criteria: Accuracy, SEO, brand alignment, traffic performance
- Goal: Create content roadmap for next 2 quarters

**Output:**

```md
# Content Audit Report: Marketing Website

**Audit date:** January 2025
**Prepared by:** Content Strategy Team
**Audience:** Content Team, VP Marketing

---

## Executive summary

Of 312 pages audited, 41% need significant updates due to outdated product information, inconsistent terminology, or poor performance. The top priority is updating 28 product pages that reference deprecated features — these pages receive 45K monthly visits and risk confusing users.

### By the numbers

| Metric | Value |
|--------|-------|
| Content items audited | 312 |
| Items needing action | 127 (41%) |
| Estimated effort | 180-220 hours |

### Recommended actions

| Priority | Action | Items affected | Effort |
|----------|--------|---------------|--------|
| High | Update product pages with deprecated features | 28 | 60 hrs |
| High | Consolidate duplicate topic articles | 15 pairs | 30 hrs |
| Medium | Refresh blog posts >18 months old | 52 | 80 hrs |
| Low | Remove zero-traffic pages | 32 | 10 hrs |

---

## Methodology

**Scope:** All pages under /products, /solutions, /blog, /resources
**Criteria:** 
- Accuracy: Product info matches current reality
- SEO: Title, meta, headings optimized
- Brand: Voice and terminology aligned
- Performance: >100 sessions/month threshold

**Sample:** Full audit (all 312 pages)
**Limitations:** Did not audit gated content or support docs

### Scoring criteria

| Score | Definition |
|-------|------------|
| Keep | Accurate, on-brand, >100 sessions/month |
| Update | Valuable topic, needs content refresh |
| Merge | Same topic as another page |
| Remove | Outdated, <100 sessions/month for 6+ months |

---

## Findings by action

### Keep as-is (185 items, 59%)

These items are performing well and need no changes.

**Characteristics:**
- Updated within last 12 months
- Above-average traffic for category
- No terminology or product accuracy issues

**Top performers:**
| URL | Monthly traffic | Notes |
|-----|-----------------|-------|
| /products/overview | 12,400 | Strong SEO position |
| /solutions/enterprise | 8,200 | High conversion |
| /blog/getting-started-guide | 5,100 | Evergreen value |

### Update (67 items, 21%)

These items have value but need refresh.

**Common issues:**
- Deprecated feature references: 28 items
- Outdated screenshots: 19 items
- Old pricing/packaging info: 12 items
- Terminology inconsistency: 8 items

| Issue type | Count | Example | Effort |
|------------|-------|---------|--------|
| Deprecated features | 28 | /products/analytics references removed dashboard widget | 2 hrs/page |
| Outdated screenshots | 19 | /blog/how-to-export shows old UI | 1 hr/page |
| Old pricing | 12 | /solutions/startup has 2023 pricing | 0.5 hr/page |

**Priority items (high traffic + accuracy issues):**

| URL | Monthly traffic | Issue |
|-----|-----------------|-------|
| /products/integrations | 6,200 | Lists 3 deprecated integrations |
| /products/api | 4,800 | API v1 references (v2 is current) |
| /solutions/teams | 3,100 | Removed feature prominently displayed |

### Merge (15 pairs, 30 items)

These items overlap and should be consolidated.

| Items to merge | Traffic (combined) | Recommended outcome |
|---------------|-------------------|---------------------|
| /blog/how-to-import + /resources/import-guide | 2,400 | Comprehensive import guide |
| /products/security + /trust-center/security | 3,800 | Single security page |
| /solutions/small-business + /solutions/startup | 1,200 | Combined SMB page |

### Remove (32 items, 10%)

These items should be deleted or redirected.

**Criteria met:**
- <100 sessions/month for 6+ months
- No business justification to keep
- No inbound links of value

| URL | Last 6mo traffic | Reason | Redirect to |
|-----|------------------|--------|-------------|
| /blog/summer-2022-update | 12 | Time-sensitive, outdated | /blog |
| /events/webinar-archive-2021 | 8 | Old events | /events |
| /products/legacy-tool | 45 | Product sunset | /products |

---

## Priority recommendations

### Immediate (This sprint)

1. **Update 28 pages with deprecated feature references**
   - Items: Product pages with highest traffic + inaccuracy
   - Impact: 45K monthly visitors seeing incorrect information
   - Owner: Product Marketing
   - Effort: 60 hours

### Short-term (This quarter)

1. **Consolidate duplicate content (15 pairs)**
   - Items: Blog + resource overlaps
   - Impact: Reduce maintenance burden, improve SEO
   - Owner: Content team
   - Effort: 30 hours

2. **Refresh 52 blog posts >18 months old**
   - Items: Evergreen topics with stale examples
   - Impact: Maintain organic traffic
   - Owner: Content team
   - Effort: 80 hours

### Long-term (Next quarter+)

1. **Implement content governance process**
   - Trigger: Prevent future accumulation of outdated content
   - Depends on: Audit completion, workflow tooling

---

## Appendix

### A: Full inventory
[Link to spreadsheet with all 312 pages]

### B: Traffic data source
Google Analytics, Jan 1 - Dec 31, 2024

### C: Terminology inconsistencies found
| Incorrect term | Correct term | Pages affected |
|----------------|--------------|----------------|
| "sync" | "synchronize" | 14 |
| "admin" | "administrator" | 8 |
| "workspace" | "organization" | 6 |
```

---

## Example 2: Section audit with urgent findings

**Input:**
- Scope: Help center (89 articles)
- Audience: Support leadership
- Trigger: Increased support tickets about documented topics
- Criteria: Accuracy, findability, completeness

**Output:**

```md
# Help Center Audit: Urgent Findings

**Audit date:** February 2025
**Audience:** Support Leadership

---

## Executive summary

12 help center articles contain incorrect information that directly contradicts current product behavior. These 12 articles correlate with a 34% increase in related support tickets over the past 90 days.

### Urgent action required

| Article | Issue | Tickets (90d) | Impact |
|---------|-------|---------------|--------|
| /help/export-data | Steps don't match new UI | 147 | Users can't export |
| /help/billing-faq | Wrong pricing tiers | 89 | Billing confusion |
| /help/permissions | Outdated role names | 72 | Access setup failures |

**Recommended immediate action:** Update these 12 articles before end of week.

---

## Full findings

[Continue with standard audit structure...]
```

---

## Example 3: Edge case — audit with limited actionability

**Input:**
- Audit reveals many issues
- Resources severely constrained
- Challenge: Report must acknowledge limitations while still being useful

**Output:**

```md
# Content Audit Report: Recommendations Under Constraints

## Context

This audit identified 127 items needing action. Current team capacity is ~20 hours/month for content maintenance. This report prioritizes ruthlessly to fit constraints.

## Realistic action plan

### With current resources (20 hrs/month)

**Month 1:**
- Fix 3 critical accuracy issues (6 hrs)
- Remove 10 zero-traffic pages (2 hrs)
- Remaining: 12 hrs buffer/review

**Months 2-6:**
- 10 updates per month
- Total: 50 items addressed

### What won't get done

67 items (53%) will remain unaddressed at current capacity:
- 42 blog posts needing refresh
- 15 pages needing merge
- 10 low-priority updates

### If resources increase

| Additional hrs/month | Additional items addressed |
|---------------------|---------------------------|
| +10 hrs | +30 items (6 months) |
| +20 hrs | +60 items (6 months) |

### Risk acknowledgment

Unaddressed items carry these risks:
- SEO decay for outdated blog posts
- Continued support tickets for inaccurate content
- Brand inconsistency

This report documents the trade-off being made due to resource constraints.
```
