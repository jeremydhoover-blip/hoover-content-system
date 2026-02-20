# Metric Definitions Reference

Standard definitions for common content metrics. Use these to ensure consistency across teams and reports.

---

## Engagement metrics

### Pageviews
**Definition:** Total number of times a page was viewed (includes repeat views from same session)
**When to use:** Understanding content popularity
**Limitation:** Inflated by refreshes, doesn't indicate engagement quality
**Better alternative:** Unique pageviews or engaged sessions

### Unique pageviews
**Definition:** Number of sessions in which a page was viewed (one count per session per page)
**When to use:** Understanding reach/audience size
**Limitation:** Still doesn't indicate engagement quality

### Time on page
**Definition:** Time elapsed from page load to next navigation event
**Calculation:** Timestamp of next page - timestamp of current page
**When to use:** Proxy for content engagement
**Limitation:** Last page of session has 0 time; users may leave tab open; doesn't work for single-page sessions
**Better alternative:** Engaged time (requires scroll/click tracking)

### Engaged time
**Definition:** Time user actively interacts with page (scrolling, clicking, visible tab)
**Calculation:** Sum of active interaction intervals
**When to use:** More accurate engagement measurement
**Limitation:** Requires JavaScript tracking; can impact performance

### Scroll depth
**Definition:** Maximum percentage of page scrolled during session
**Calculation:** (Scroll position / page height) × 100
**When to use:** Understanding if users reach important content
**Limitation:** Long pages may have lower scroll depth even with engagement

### Bounce rate
**Definition:** Percentage of single-page sessions
**Calculation:** (Single-page sessions / total sessions) × 100
**When to use:** Understanding landing page effectiveness
**Limitation:** Not inherently bad (user may have found answer); misleading for blogs

### Article completion rate
**Definition:** Percentage of users who reached article end or indicated completion
**Calculation:** (Users scrolling to bottom OR clicking "helpful") / total viewers × 100
**When to use:** Help center, documentation
**When to avoid:** Marketing content where middle CTAs are desired

---

## Conversion metrics

### Conversion rate
**Definition:** Percentage of users who complete desired action
**Calculation:** (Conversions / total users or sessions) × 100
**When to use:** Measuring content effectiveness at driving action
**Variations:** Session-based, user-based, click-based (document which)

### Micro-conversion rate
**Definition:** Completion of intermediate steps (not final conversion)
**Examples:** Email signup, PDF download, video play
**When to use:** Content that supports longer journeys

### Click-through rate (CTR)
**Definition:** Percentage of users who click a link or CTA
**Calculation:** (Clicks / impressions or views) × 100
**When to use:** CTA effectiveness, internal linking
**Limitation:** High CTR with low conversion may indicate misleading content

---

## Search metrics

### Search success rate
**Definition:** Searches resulting in content click without refinement
**Calculation:** (Searches with click on first results page) / total searches × 100
**When to use:** Help center, documentation search quality
**Target benchmark:** >60% is good, >75% is excellent

### Zero-results rate
**Definition:** Searches returning no results
**Calculation:** (Zero-result searches / total searches) × 100
**When to use:** Content gap identification
**Target:** <5%

### Search refinement rate
**Definition:** Searches followed by another search
**Calculation:** (Searches followed by new search) / total searches × 100
**When to use:** Query understanding quality
**Target:** <20%

---

## Support/self-service metrics

### Self-service rate
**Definition:** Users who resolved issue without human support
**Calculation:** (Users who viewed help and didn't contact support) / total help viewers × 100
**When to use:** Help center ROI
**Complexity:** Requires user ID matching across systems

### Ticket deflection
**Definition:** Estimated support tickets avoided due to content
**Calculation:** Requires baseline comparison or control group
**When to use:** Business case for content investment
**Limitation:** Correlation, not provable causation

### Content-mentioned tickets
**Definition:** Support tickets referencing documentation issues
**Calculation:** Manual tagging or keyword search
**When to use:** Content quality monitoring
**Tags to track:** "unclear docs," "outdated," "missing info," "wrong instructions"

---

## Attribution metrics

### First-touch attribution
**Definition:** Credits conversion to first interaction
**When to use:** Understanding awareness-stage content
**Limitation:** Ignores nurture content value

### Last-touch attribution
**Definition:** Credits conversion to final interaction before conversion
**When to use:** Understanding decision-stage content
**Limitation:** Ignores awareness/consideration content

### Multi-touch attribution
**Definition:** Distributes credit across touchpoints
**Models:** Linear (equal), time-decay (recent > older), position-based (first and last weighted)
**When to use:** Full funnel understanding
**Limitation:** Complexity; requires sophisticated tracking

### Content-influenced
**Definition:** Conversions where content appeared anywhere in path
**Calculation:** All conversions with content touchpoint (regardless of position)
**When to use:** Broader content value story
**Limitation:** May overcount; content appears in many paths

---

## Quality metrics

### Accuracy rate
**Definition:** Percentage of content verified as factually correct
**Calculation:** Requires manual audit or user reports
**When to use:** Documentation, help content
**Measurement:** Sample-based audits + error reports

### Freshness
**Definition:** Recency of content updates
**Calculation:** (Articles updated in period / total articles) × 100
**When to use:** Documentation maintenance
**Common threshold:** 80% updated within 6 months

### Consistency score
**Definition:** Adherence to style guide and terminology
**Calculation:** Manual audit or linting tools
**When to use:** Content governance

---

## Metric selection framework

Choose metrics based on content goal:

| Goal | Primary metric | Supporting metrics |
|------|----------------|-------------------|
| Awareness | Unique pageviews, reach | Time on page, scroll depth |
| Engagement | Engaged time, completion rate | Bounce rate (inverse) |
| Conversion | Conversion rate | CTR, micro-conversions |
| Self-service | Self-service rate | Search success, ticket deflection |
| Revenue | Attributed pipeline/revenue | Content-influenced conversions |
| Quality | Accuracy rate, freshness | Error reports, user feedback |
