# Templates

## Default output: Readability improvement with annotations

```md
## Improved content

[Revised content here]

---

## Readability changes

### Metrics comparison

| Metric | Before | After | Target |
|--------|--------|-------|--------|
| Avg. sentence length | [X] words | [Y] words | 15-20 |
| Avg. paragraph length | [X] sentences | [Y] sentences | 3-5 |
| Passive voice | [X]% | [Y]% | <15% |
| Flesch-Kincaid grade | [X] | [Y] | [depends on audience] |

### Key changes made

1. **[Category]:** [Specific change and rationale]
2. **[Category]:** [Specific change and rationale]
3. **[Category]:** [Specific change and rationale]

### Flags for review

- [Any meaning-altering changes that need author approval]
```

## Alternative: Before/After comparison format

Use for training or stakeholder review:

```md
## Readability improvements

### Example 1: Sentence simplification

**Before:**
> [Original sentence]

**After:**
> [Improved sentence]

**Change:** [What was done and why]

---

### Example 2: Paragraph restructuring

**Before:**
> [Original paragraph]

**After:**
> [Improved paragraph]

**Change:** [What was done and why]
```

## Alternative: Inline annotation format

Use when changes need to be traceable:

```md
The system ~~is able to process~~ **processes** [simplified verb phrase] requests in real time. ~~Due to the fact that~~ **Because** [reduced wordiness] performance matters, we ~~made the decision to implement~~ **implemented** [noun-to-verb] caching.

**Summary:**
- Simplified verb phrases: 2
- Reduced wordiness: 1
- Noun-to-verb conversions: 1
```

## Reading level guidance

| Audience | Target grade level | Characteristics |
|----------|-------------------|-----------------|
| General public | 6-8 | Short sentences, common words |
| Professional | 10-12 | Industry terms OK, clear structure |
| Technical | 12-14 | Specialized vocabulary, precise |
| Academic | 14+ | Complex structures acceptable |
