# Summary Structures by Audience

## Structure selection guide

| Audience | Primary need | Lead with | Minimize | Include |
|----------|--------------|-----------|----------|---------|
| Executives | Decision support | Business impact | Methodology | ROI implications |
| Product managers | Prioritization | User problems ranked | Raw quotes | Severity + frequency |
| Designers | Inspiration + direction | User behaviors | Technical constraints | Quotes + pain points |
| Engineers | Implementation clarity | Technical implications | Business strategy | Thresholds + specs |
| Researchers | Rigor + replication | Methods + confidence | Recommendations | Limitations + gaps |

---

## Inverted pyramid structure (executives, PMs)

```
┌─────────────────────────────┐
│      BOTTOM LINE            │  ← Most important takeaway
│      (1-2 sentences)        │
├─────────────────────────────┤
│    KEY FINDINGS (3-5)       │  ← Ranked by impact
│    with implications        │
├─────────────────────────────┤
│    RECOMMENDATIONS          │  ← Actionable next steps
├─────────────────────────────┤
│    CONTEXT + CONFIDENCE     │  ← Method, sample, limitations
└─────────────────────────────┘
```

Use when: Reader may not finish; most critical info must be first.

---

## Problem-solution structure (designers, product)

```
┌─────────────────────────────┐
│    USER GOAL FRAMING        │  ← What users are trying to do
├─────────────────────────────┤
│    BARRIERS OBSERVED        │  ← What's stopping them
│    (grouped by theme)       │
├─────────────────────────────┤
│    OPPORTUNITY AREAS        │  ← Where to intervene
├─────────────────────────────┤
│    DESIGN DIRECTIONS        │  ← Suggested approaches
└─────────────────────────────┘
```

Use when: Reader needs to understand user context before solutions.

---

## Technical implications structure (engineering)

```
┌─────────────────────────────┐
│    TL;DR                    │  ← User needs affecting tech
├─────────────────────────────┤
│    ISSUES TABLE             │  ← Frequency + technical area
├─────────────────────────────┤
│    THRESHOLDS + SPECS       │  ← Concrete requirements
├─────────────────────────────┤
│    MENTAL MODEL IMPACTS     │  ← Assumptions affecting arch
└─────────────────────────────┘
```

Use when: Reader needs to map user needs to technical decisions.

---

## Narrative structure (stakeholder updates, all-hands)

```
┌─────────────────────────────┐
│    THE QUESTION             │  ← What we wanted to learn
├─────────────────────────────┤
│    WHAT WE DID              │  ← Brief method description
├─────────────────────────────┤
│    WHAT WE FOUND            │  ← Findings as story
├─────────────────────────────┤
│    WHAT IT MEANS            │  ← Implications + actions
└─────────────────────────────┘
```

Use when: Audience needs context to understand significance.

---

## Finding severity classification

| Severity | Criteria | Summary treatment |
|----------|----------|-------------------|
| Critical | Blocks primary use case; affects >50% of users | Lead the summary; P0 recommendation |
| High | Significant friction; affects 25-50% of users | Top 3 findings; P1 recommendation |
| Medium | Notable issue; affects 10-25% of users | Include if space; P2 recommendation |
| Low | Minor friction; affects <10% of users | Appendix or omit; backlog |

---

## Confidence level language

| Confidence | When to use | Language |
|------------|-------------|----------|
| High | Consistent pattern across segments; large sample | "Users consistently..." / "Clear pattern..." |
| Medium | Pattern exists but sample is limited or mixed | "Most users..." / "Initial findings suggest..." |
| Low | Emerging signal; needs validation | "Some users..." / "Early indication..." |
| Uncertain | Conflicting data; no clear pattern | "Mixed results..." / "Further research needed..." |

---

## Summary length guidelines

| Format | Word count | Findings | Use when |
|--------|------------|----------|----------|
| Micro (Slack/email) | 50-100 | 1-2 | Quick stakeholder ping |
| Brief | 150-300 | 3 | Executive update |
| Standard | 400-600 | 4-5 | Team readout |
| Detailed | 800-1200 | 5-7 | Cross-functional share |
| Full report | 1500+ | Comprehensive | Documentation/archive |
