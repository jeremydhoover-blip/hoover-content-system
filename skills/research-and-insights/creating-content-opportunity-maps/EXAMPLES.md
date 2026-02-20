# Examples

## Example 1: Impact vs. effort opportunity map

**Input:**
```
Context: Content team planning Q1 priorities
Scope: Help center improvements
Evidence: Support ticket analysis, user research, analytics
Team capacity: 2 content designers, limited engineering support
Decision: What to prioritize in next quarter
```

**Output:**
```md
# Content Opportunity Map: Help Center Q1

## Map dimensions
- **X-axis**: Effort — Low (days) → High (weeks+)
- **Y-axis**: Impact — Low (minor improvement) → High (significant metric movement)

## Scoring guide
**Impact**:
- 5: Reduces support tickets by >20% for topic area
- 4: Reduces tickets by 10-20% or improves completion rate >15%
- 3: Measurable improvement (<10% ticket reduction)
- 2: Quality improvement, hard to measure
- 1: Nice to have, minimal measurable impact

**Effort**:
- 1: <2 days, content-only change
- 2: 3-5 days, content-only
- 3: 1-2 weeks, may need design input
- 4: 2-4 weeks, needs design or eng
- 5: >1 month, significant eng work

## Opportunity list
| ID | Opportunity | Evidence | Impact | Effort |
|----|-------------|----------|--------|--------|
| 1 | Rewrite billing FAQ (top 10 ticket driver) | 340 tickets/mo on billing | 5 | 2 |
| 2 | Add video to setup guide | 23% abandon setup at step 3 | 4 | 4 |
| 3 | Create integration troubleshooting hub | 180 tickets/mo, scattered content | 4 | 3 |
| 4 | Localize top 20 articles to Spanish | 15% of users are Spanish-speaking | 3 | 4 |
| 5 | Improve search relevance | 42% search exits without click | 5 | 5 |
| 6 | Add "was this helpful" to all articles | No current feedback mechanism | 2 | 2 |
| 7 | Update screenshots (50 outdated) | User complaints, dated appearance | 2 | 3 |
| 8 | Consolidate duplicate articles | 23 duplicate topics identified | 3 | 2 |

## Map visualization

```
High    │ Q2: Big Bets       │ Q1: Do Now
Impact  │                    │
   5    │ #5                 │ #1
   4    │ #2, #4             │ #3
        ├────────────────────┼────────────────────
   3    │                    │ #8
   2    │ #7                 │ #6
Low     │ Q3: Avoid          │ Q4: Quick Wins
        └────────────────────┴────────────────────
             High Effort          Low Effort
               5    4    3    2    1
```

## Quadrant analysis

### Q1: Do Now — High impact, low effort
- **Opportunities**: #1 (Billing FAQ), #3 (Integration hub)
- **Recommendation**: Start immediately. Highest ROI.
- **Rationale**: Both address top ticket drivers with content-only work.

### Q4: Quick Wins — Lower impact, low effort
- **Opportunities**: #6 (Feedback mechanism), #8 (Consolidate duplicates)
- **Recommendation**: Bundle with Q1 work if capacity allows.
- **Rationale**: Low cost improvements that build foundation.

### Q2: Big Bets — High impact, high effort
- **Opportunities**: #5 (Search), #2 (Video), #4 (Localization)
- **Recommendation**: Evaluate #5 for Q2 if eng capacity opens. #2 and #4 require resourcing decision.
- **Rationale**: Impact is real but requires investment justification.

### Q3: Avoid — Lower impact, high effort
- **Opportunities**: #7 (Screenshots)
- **Recommendation**: Deprioritize. Update screenshots opportunistically when editing articles for other reasons.
- **Rationale**: Effort disproportionate to benefit.

## Summary recommendation
**Q1 Focus**:
1. **#1 Billing FAQ rewrite** — Start week 1, 3-5 days, content lead
2. **#3 Integration troubleshooting hub** — Start week 2, 1-2 weeks, content lead
3. **#8 Consolidate duplicates** — Ongoing, dedupe as we touch articles

**Q2 Planning**:
- Evaluate #5 (search) with engineering for feasibility
- Make business case for #4 (localization) if Spanish user segment grows
```

---

## Example 2: Content gap map by user journey

**Input:**
```
Context: New product launch content planning
Scope: Full customer journey
Evidence: Competitor analysis, beta user feedback, sales input
Personas: SMB buyer, Enterprise buyer
Decision: What content to create before launch
```

**Output:**
```md
# Content Gap Analysis: [Product] Launch

## Mapping approach
Map content coverage against journey stage importance by persona.

## Gap inventory
| Gap ID | Journey stage | User need | SMB importance | Enterprise importance | Current coverage |
|--------|---------------|-----------|----------------|----------------------|------------------|
| G1 | Awareness | Understand what product does | High | High | Partial (homepage only) |
| G2 | Consideration | Compare to alternatives | High | Medium | None |
| G3 | Consideration | See pricing | High | Low | None (enterprise = sales) |
| G4 | Decision | Understand security/compliance | Low | High | None |
| G5 | Decision | See case studies | Medium | High | None |
| G6 | Onboarding | Get started guide | High | High | Draft exists |
| G7 | Activation | Integration setup | High | High | None |
| G8 | Retention | Best practices | Medium | Medium | None |

## Gap severity by persona

### SMB buyer journey gaps
```
           │ No coverage    │ Partial        │ Full
───────────┼────────────────┼────────────────┼───────
High need  │ G2, G3, G7     │ G1, G6         │ —
           │ [CRITICAL]     │ [HIGH]         │
Med need   │ G5, G8         │                │ —
           │ [MEDIUM]       │                │
Low need   │ G4             │                │ —
           │ [LOW]          │                │
```

### Enterprise buyer journey gaps
```
           │ No coverage    │ Partial        │ Full
───────────┼────────────────┼────────────────┼───────
High need  │ G4, G5, G7     │ G1, G6         │ —
           │ [CRITICAL]     │ [HIGH]         │
Med need   │ G2, G8         │                │ —
           │ [MEDIUM]       │                │
Low need   │ G3             │                │ —
           │ [LOW]          │                │
```

## Prioritized gap list
| Priority | Gap | Need | Audience | Pre-launch? |
|----------|-----|------|----------|-------------|
| P0 | G1: Expanded product overview | Awareness | Both | Yes |
| P0 | G6: Getting started guide | Onboarding | Both | Yes |
| P0 | G7: Integration setup docs | Activation | Both | Yes |
| P1 | G2: Comparison content | Consideration | SMB | Yes |
| P1 | G4: Security documentation | Decision | Enterprise | Yes |
| P1 | G5: Case studies | Decision | Enterprise | 1 at launch, more post |
| P2 | G3: Pricing page | Consideration | SMB | Yes (basic) |
| P3 | G8: Best practices | Retention | Both | Post-launch |

## Launch content roadmap

### Pre-launch (Must have)
- G1: Product overview expansion — 3 days
- G6: Getting started guide (finalize) — 2 days
- G7: Integration setup docs (top 3 integrations) — 5 days
- G3: Pricing page (SMB tiers) — 1 day
- G4: Security overview page — 2 days

### Launch week
- G2: Comparison landing page (vs. top 2 competitors) — 3 days
- G5: 1 case study (beta customer) — 2 days

### Post-launch (30 days)
- G5: 2 additional case studies
- G7: Additional integration docs
- G8: Best practices series kickoff

## Dependencies
- G6 (getting started) must be final before G7 (integrations) can reference it
- G5 (case studies) requires customer approval — start process now
```

---

## Example 3: Edge case — too many opportunities, needs grouping

**Input:**
```
Context: Annual content strategy planning
Scope: Full content program
Opportunities identified: 47 individual content ideas
Decision: What themes to invest in
```

**Output:**
```md
# Content Opportunity Map: 2026 Strategy

## Approach
47 individual opportunities grouped into 8 strategic themes for map-level prioritization. Detailed prioritization within themes happens after theme selection.

## Theme groupings
| Theme | # of opportunities | Summary |
|-------|-------------------|---------|
| Developer documentation | 12 | API docs, SDK guides, code samples |
| Self-service support | 9 | Help center, troubleshooting, FAQs |
| Onboarding content | 7 | Getting started, tutorials, first-use |
| Enterprise enablement | 6 | Security docs, compliance, case studies |
| Marketing content | 5 | Landing pages, product messaging |
| Community content | 4 | Blog, thought leadership, events |
| Localization | 3 | Spanish, German, Japanese |
| Internal content | 1 | Sales enablement, training |

## Map dimensions
- **X-axis**: Resource intensity — Low (existing team) → High (new hires or contractors)
- **Y-axis**: Strategic alignment — Low (incremental) → High (tied to company goals)

## Theme scores
| Theme | Evidence | Strategic alignment | Resource intensity |
|-------|----------|---------------------|-------------------|
| Developer documentation | API adoption is 2026 growth lever | 5 | 4 |
| Self-service support | Support cost reduction target | 4 | 2 |
| Onboarding content | Activation rate is lagging | 5 | 3 |
| Enterprise enablement | Enterprise segment is priority | 5 | 3 |
| Marketing content | Campaign support | 3 | 2 |
| Community content | Brand building | 2 | 2 |
| Localization | International expansion planned | 4 | 4 |
| Internal content | Sales team request | 2 | 1 |

## Map visualization

```
High    │ Invest Strategically │ Strategic Priorities
Align   │ Localization         │ Dev Docs
   5    │                      │ Onboarding
        │                      │ Enterprise
   4    │                      │ Self-service
        ├──────────────────────┼──────────────────────
   3    │                      │ Marketing
   2    │ Community            │ Internal
Low     │ Evaluate Later       │ Opportunistic
        └──────────────────────┴──────────────────────
             High Resource          Low Resource
               5    4    3    2    1
```

## Recommendations

### Primary investment (70% of resources)
1. **Onboarding content** — Directly tied to activation metric. Manageable scope.
2. **Enterprise enablement** — Required for enterprise sales motion.
3. **Self-service support** — High ROI, supports cost reduction goal.

### Secondary investment (20% of resources)
4. **Developer documentation** — Strategic but resource-intensive. Phase over year.

### Opportunistic (10% of resources)
5. **Marketing content** — Support campaigns as needed.
6. **Internal content** — Quick wins for sales team.

### Defer to 2027
- **Localization** — Strategic but requires dedicated investment. Revisit H2.
- **Community content** — Lower priority given other investments.

## Next step
For each prioritized theme, create detailed opportunity map with individual content items.
```
