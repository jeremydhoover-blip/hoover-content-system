# Information Architecture Principles

## Core IA laws

### 1. Hick's Law
**Time to decide increases with the number and complexity of choices.**

Application:
- Limit top-level navigation to 5-7 items
- Progressive disclosure: show less upfront, reveal on demand
- Group related items to reduce perceived choices

### 2. Miller's Law
**Working memory holds approximately 7 (±2) items.**

Application:
- Maximum 7 items at any single navigation level
- Chunk related content into meaningful groups
- Use hierarchy to offload memory requirements

### 3. Jakob's Law
**Users spend most of their time on other sites and expect yours to work similarly.**

Application:
- Follow conventions for navigation patterns
- Use familiar category names when appropriate
- Don't innovate on basic IA patterns without strong reason

---

## Taxonomy requirements

### Mutual exclusivity (MECE principle)
Every item belongs in exactly one category. If content could fit multiple places:
- Choose primary home based on user's most likely entry point
- Use cross-links for secondary discovery
- Document the decision rule

**Test:** Can you unambiguously answer "where does this go?"

### Exhaustiveness
Every piece of content has a home. No orphans.

**Test:** Take any content item—can you place it without creating a new category?

### User-centric categorization
Categories match how users think, not how the organization is structured.

**Anti-pattern:** Mirroring org chart ("Sales content," "Engineering content")
**Pattern:** User goals ("Getting started," "Troubleshooting")

**Test:** Would a new user predict what's in this category from its name?

---

## Depth vs. breadth tradeoff

| Approach | Pros | Cons | Use when |
|----------|------|------|----------|
| **Shallow (broad)** | Faster scanning, less clicking | More choices at each level | Expert users, small content set |
| **Deep (narrow)** | Fewer choices per level | More clicks to destination | Large content sets, novice users |
| **Balanced (3 levels max)** | Compromise | Requires careful grouping | Most situations |

### The 3-level rule
Never exceed 3 levels of hierarchy:
- Level 1: Category (5-7 items)
- Level 2: Subcategory (5-7 items per parent)
- Level 3: Content or sub-subcategory (only if essential)

Beyond 3 levels, users lose context and navigation becomes frustrating.

---

## Navigation patterns

### Primary navigation
- Persistent, visible on all pages
- Contains top-level categories
- Maximum 7 items

### Secondary navigation
- Contextual to current section
- Shows subcategories of current area
- Can be sidebar, tabs, or in-page links

### Utility navigation
- Cross-cutting functions (search, account, help)
- Not part of content hierarchy
- Consistent position across site

---

## Common IA failures

| Failure | Symptom | Fix |
|---------|---------|-----|
| **Org-chart IA** | Categories match departments | Restructure around user goals |
| **Feature-based IA** | Categories match product features | Group by user tasks instead |
| **Flat structure** | Everything at one level | Introduce meaningful hierarchy |
| **Too deep** | 5+ clicks to content | Flatten and use cross-links |
| **Ambiguous categories** | Users guess wrong frequently | Clarify names, add descriptions |
| **Duplicate homes** | Same content in multiple places | Choose primary, cross-link |

---

## Testing taxonomy

### Card sorting (open)
- Users group items and name categories
- Reveals user mental models
- Use for: Greenfield IA

### Card sorting (closed)
- Users sort items into predefined categories
- Tests if your categories make sense
- Use for: Validating proposed structure

### Tree testing
- Users find items in hierarchy without visual UI
- Tests findability independent of design
- Use for: Validating before implementation

### First-click testing
- Measures where users click first for a task
- 87% of users who get first click right succeed
- Use for: Critical paths

---

## Governance checklist

Before finalizing taxonomy:
- [ ] Maximum 7 items at each level
- [ ] Maximum 3 levels of depth
- [ ] No overlapping categories
- [ ] Every content type has a home
- [ ] User-facing labels use user language
- [ ] Decision rules documented for edge cases
- [ ] Process defined for adding new categories
- [ ] Review schedule established
