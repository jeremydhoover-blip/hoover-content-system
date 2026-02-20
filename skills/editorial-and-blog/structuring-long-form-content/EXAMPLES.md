# Examples

## Example 1: Restructuring a comprehensive guide

**Input:**
- Content: 4000-word guide on API design best practices
- Current state: Wall of text with occasional bold phrases
- Target audience: Backend engineers (will reference repeatedly)
- Usage: Both learning material and ongoing reference

**Output:**

```md
# API Design Best Practices

A practical guide to designing consistent, usable, and maintainable REST APIs. Written for backend engineers building production APIs.

## Contents

- [Principles](#principles)
- [URL design](#url-design)
- [Request and response patterns](#request-and-response-patterns)
- [Error handling](#error-handling)
- [Versioning](#versioning)
- [Authentication](#authentication)
- [Documentation](#documentation)
- [Checklist](#checklist)

---

## Key takeaways

- Use nouns for resources, HTTP verbs for actions
- Return consistent error formats with actionable messages
- Version in the URL path for breaking changes
- Design for the consumer's mental model, not your database schema

---

## Principles

Before diving into specifics, these principles guide every decision:

### Consistency over cleverness

[Content...]

### Consumer-first design

[Content...]

**Section summary:** Design APIs as products. Consistency and predictability matter more than optimization.

---

## URL design

### Resource naming

[Content...]

### Collection vs. singleton

[Content...]

### Nested resources

[Content...]

**Section summary:** URLs should be readable, predictable, and reflect the resource hierarchy.

---

[Pattern continues for remaining sections...]

---

## Checklist

Use this when reviewing an API design:

- [ ] All URLs use nouns, not verbs
- [ ] HTTP methods used correctly (GET reads, POST creates, etc.)
- [ ] Error responses follow consistent format
- [ ] Versioning strategy documented
- [ ] Authentication method specified
- [ ] All endpoints documented with examples
```

**Structure decisions:**
- TOC added for navigation since this is reference material
- Key takeaways upfront for quick consultation
- Sections ordered by design process flow
- Checklist at end for practical application
- Each section self-contained with summary

---

## Example 2: Narrative long-form structure

**Input:**
- Content: 3000-word case study on platform migration
- Audience: Engineering leaders evaluating similar migrations
- Usage: Read once for decision support

**Output:**

```md
# How We Migrated 10M Users to a New Platform in 6 Months

A behind-the-scenes look at Acme Corp's database migration, including what went wrong, what we'd do differently, and the metrics we tracked.

---

## The situation

**Context:** In early 2024, we faced a scaling ceiling...

**The decision:** We needed to migrate from...

**The stakes:** 10 million active users, $2M daily transaction volume...

---

## The approach

### Phase 1: Parallel writes (Weeks 1-8)

[Content...]

> **What we learned:** Running parallel writes caught 340 edge cases we hadn't anticipated in testing.

### Phase 2: Shadow reads (Weeks 9-14)

[Content...]

### Phase 3: Cutover (Weeks 15-18)

[Content...]

---

## The results

| Metric | Before | After | Change |
|--------|--------|-------|--------|
| P95 latency | 450ms | 120ms | -73% |
| Error rate | 0.3% | 0.08% | -73% |
| Monthly cost | $180K | $95K | -47% |

---

## What we'd do differently

### Start performance testing earlier

[Content...]

### Invest more in rollback automation

[Content...]

### Communicate more with customers

[Content...]

---

## Key takeaways for your migration

1. [Actionable insight]
2. [Actionable insight]
3. [Actionable insight]

---

*Questions about our migration? [Contact the author]*
```

**Structure decisions:**
- Narrative flow (situation → approach → results → learnings)
- No TOC needed — designed for linear reading
- Callouts highlight key insights within narrative
- Data table makes results scannable
- Ends with reader-applicable takeaways

---

## Example 3: Edge case — mixed reference and learning content

**Input:**
- Content: 5000-word guide on design tokens
- Challenge: Part conceptual learning, part reference lookup
- Audience: Designers and developers with varying familiarity

**Output:**

```md
# Design Tokens Guide

## How to use this guide

| If you want to... | Start here |
|-------------------|------------|
| Understand what tokens are | [Concepts](#concepts) |
| Implement tokens in code | [Implementation](#implementation) |
| Look up token naming rules | [Reference](#reference) |
| Troubleshoot issues | [FAQ](#faq) |

---

## Part 1: Concepts

*Read this section if you're new to design tokens.*

### What are design tokens?

[Foundational explanation...]

### Why use design tokens?

[Benefits and use cases...]

### Token architecture

[Conceptual framework...]

**You're ready for implementation if you can answer:**
- What's the difference between primitive and semantic tokens?
- Why do we separate design decisions from implementation?

---

## Part 2: Implementation

*Read this section when setting up tokens or adding new ones.*

### Setup

[Step-by-step instructions...]

### Adding tokens

[Step-by-step instructions...]

### Using tokens in code

[Step-by-step instructions...]

---

## Part 3: Reference

*Use this section to look up specific rules and values.*

### Naming conventions

| Category | Pattern | Example |
|----------|---------|---------|
| Color | `color-{semantic}-{variant}` | `color-text-primary` |
| Spacing | `space-{size}` | `space-md` |
| [Continue...] | | |

### Token catalog

[Alphabetized or categorized list...]

### Platform-specific syntax

[Reference table...]

---

## FAQ

### How do I add a new color?

[Answer...]

### What if I need a one-off value?

[Answer...]

---

## Changelog

- **v2.1** (2024-02): Added dark mode tokens
- **v2.0** (2023-10): Restructured naming conventions
```

**Structure decisions:**
- Navigation table upfront acknowledges mixed use cases
- Content explicitly labeled as "read" vs. "reference" sections
- Conceptual content includes comprehension check
- Reference section optimized for lookup (tables, alphabetized)
- FAQ handles common specific questions
- Changelog since this is living documentation
