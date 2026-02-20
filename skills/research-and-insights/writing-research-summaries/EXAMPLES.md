# Examples

## Example 1: Executive summary from usability study

**Input:**
```
Study: Checkout flow usability test
Participants: 12 users, mix of new and returning
Method: Moderated usability testing
Raw findings:
- 8/12 users confused by "Express checkout" vs "Guest checkout"
- 6/12 users looked for order summary before payment step
- 4/12 users abandoned at shipping options (too many choices)
- 3/12 users missed the promo code field
- 11/12 users expected email confirmation immediately
Audience: VP of Product
Length: Executive brief
```

**Output:**
```md
# Checkout Redesign Study — Executive Summary

## Bottom line
Checkout confusion is costing conversions. 67% of test users struggled with terminology and flow sequencing, with 33% abandoning at shipping selection.

## Key findings
1. **Terminology confusion**: 8/12 users couldn't distinguish "Express" from "Guest" checkout. Impact: Users who want speed are delayed by decision paralysis at step one.

2. **Missing order visibility**: 6/12 users wanted to see their cart summary before entering payment. Impact: Trust gap is causing hesitation at the highest-friction step.

3. **Shipping choice overload**: 4/12 users abandoned when presented with 7 shipping options. Impact: Direct revenue loss from drop-off at near-completion.

## Recommended actions
| Priority | Action | Owner | Finding link |
|----------|--------|-------|--------------|
| P0 | Rename checkout options to "Sign in" / "Continue as guest" | Product | Finding #1 |
| P0 | Add persistent order summary sidebar | Design | Finding #2 |
| P1 | Reduce shipping options to 3 with smart defaults | Product | Finding #3 |

## Study context
- **Method**: Moderated usability testing (remote)
- **Participants**: 12 users (6 new, 6 returning)
- **Confidence**: High — consistent patterns across user types
```

---

## Example 2: Design team summary from user interviews

**Input:**
```
Study: Content creator workflow interviews
Participants: 8 professional content creators
Method: Semi-structured interviews (60 min each)
Key themes:
- Creators batch content but publish on different schedules
- Most use 3-4 tools and manually copy between them
- Fear of losing drafts mentioned by 6/8
- Collaboration usually means "I email them a doc"
- Analytics are checked weekly, not real-time
Audience: Design team
```

**Output:**
```md
# Content Creator Workflows — Design Summary

## What users need
Content creators work in intensive batching sessions, producing multiple pieces at once but publishing over days or weeks. Their workflow is fragmented across disconnected tools, creating friction at every handoff.

## Behavioral insights

### Batching behavior doesn't match publishing cadence
- **Observed behavior**: Creators produce 5-10 pieces in one session, then schedule them across 2-3 weeks
- **Why it matters**: UI optimized for single-piece flows adds friction to their actual workflow
- **Design direction**: Support multi-item creation with individual scheduling per piece

### Manual copy-paste as integration
- **Observed behavior**: 8/8 creators manually copy content between writing tool → CMS → social platforms
- **Why it matters**: Each copy risks formatting loss and version confusion
- **Design direction**: Export flows that preserve formatting and push to multiple destinations

### Draft anxiety is universal
- **Observed behavior**: 6/8 mentioned fear of losing work; 3 use personal backup systems
- **Why it matters**: Distrust in save state creates cognitive overhead during creation
- **Design direction**: Visible autosave indicator + version history access

## Pain points to address
| Pain point | Severity | Current state | Opportunity |
|------------|----------|---------------|-------------|
| Multi-tool copy-paste | High | Manual process | One-click cross-publish |
| Draft loss anxiety | High | Hidden autosave | Visible save status + history |
| Scheduling inflexibility | Medium | Single publish date | Per-item scheduling in batch |
| Collaboration friction | Medium | Email attachments | Shareable draft links |

## Quotes to remember
> "I write everything Sunday night, but I can't just dump it all Monday morning. My audience would drown." — P3, newsletter creator

> "I've lost a 2,000 word draft twice. Now I paste into Google Docs every 10 minutes like a paranoid person." — P7, blogger

## Open questions
- How do creators want to see scheduled content (calendar view vs. list)?
- What's the acceptable latency for cross-platform publishing?
```

---

## Example 3: Engineering summary from performance-related research

**Input:**
```
Study: Mobile app performance perception study
Participants: 15 mobile users
Method: Observation + interview during real usage
Technical findings:
- Users noticed delays > 2 seconds, frustration at > 4 seconds
- 9/15 assumed "spinning" meant their connection, not the app
- Pull-to-refresh was used as "fix it" gesture even when unnecessary
- 5/15 force-quit and reopened when anything felt slow
- Users expected images to load progressively, not all-at-once
Audience: Engineering team
```

**Output:**
```md
# Mobile Performance Perception — Technical Implications

## TL;DR
Users blame their connection for app delays but lose trust after 4 seconds regardless. Progressive loading and clear state indicators are expected—blocking loads feel broken.

## User-reported technical issues
| Issue | Frequency | User impact | Technical area |
|-------|-----------|-------------|----------------|
| Spinner with no progress | 9/15 users | Confusion about cause | Frontend (loading states) |
| Image "pop-in" all at once | 6/15 users | Perceived slowness | Frontend (image loading) |
| List scroll jank | 4/15 users | Frustration on long lists | Frontend (virtualization) |
| Stale data after background | 5/15 users | Distrust of displayed info | Backend (cache invalidation) |

## Performance expectations
- **Acceptable latency**: < 2 seconds for primary actions (users don't consciously notice)
- **Frustration threshold**: > 4 seconds triggers blame/abandonment
- **Failure tolerance**: Low — 5/15 force-quit as first troubleshooting step
- **Offline needs**: Users expected previously viewed content to be available offline; 0/15 expected create/edit offline

## Mental models affecting architecture
- Users assume spinner = network problem → **Implication**: Distinguish network waits from processing waits in UI
- Users expect pull-to-refresh to "fix" stale states → **Implication**: Pull-to-refresh should actually refresh, not just re-render
- Users assume images load top-to-bottom progressively → **Implication**: Avoid blocking image batches; lazy load below fold

## Data users expect
- Previously viewed items available offline (read-only cache)
- Real-time sync when returning from background
- Visual confirmation that data is current (not stale)
```

---

## Example 4: Edge case — conflicting findings

**Input:**
```
Study: Dashboard preferences research
Participants: 10 users
Findings:
- 5/10 wanted more data density
- 5/10 wanted more whitespace and simplicity
- Power users and casual users had opposite preferences
- No clear majority pattern
Audience: Product leadership
```

**Output:**
```md
# Dashboard Preferences — Executive Summary

## Bottom line
User preferences are split 50/50 between density and simplicity, segmented by usage pattern. A single design will dissatisfy half the user base.

## Key findings
1. **Preference split by user type**: Power users (daily use) want density; casual users (weekly use) want simplicity. Impact: One-size-fits-all dashboard will underserve both segments.

2. **No neutral ground**: Users who wanted density rejected "medium" mockups as "too sparse." Simplicity users rejected them as "too busy." Impact: Compromise designs tested poorly with everyone.

3. **Customization expectation**: When shown the split, 7/10 users suggested "let me choose." Impact: User-controlled density may be necessary, not a nice-to-have.

## Recommended actions
| Priority | Action | Owner | Finding link |
|----------|--------|-------|--------------|
| P0 | Define user segments (power vs. casual) with behavioral criteria | Analytics | Finding #1 |
| P1 | Design compact and comfortable view modes | Design | Finding #2 |
| P1 | Prototype view-mode switcher for validation | Design | Finding #3 |

## Study context
- **Method**: Preference testing with mockups + follow-up interviews
- **Participants**: 10 users (5 daily active, 5 weekly active)
- **Confidence**: Medium — clear segment split but small sample per segment
- **Limitation**: Self-reported preferences; actual usage may differ
```
