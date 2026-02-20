# Templates

## Content pattern entry
Use this structure for each pattern:

```md
## Pattern: [Pattern name]

**Use when**: [Trigger condition—what situation requires this pattern]
**Content type**: [Error | Confirmation | Action | Status | Instruction | Empty state]

### Structure
```
[Structural template with placeholders]
```

### Elements

| Element | Required | Constraints | Notes |
|---------|----------|-------------|-------|
| [Element name] | [Yes/No] | [Char limit, format] | [Guidance] |

### Rules
1. [Rule 1]: [Rationale]
2. [Rule 2]: [Rationale]
3. [Rule 3]: [Rationale]

### Variation boundaries
- **Fixed**: [What must remain constant]
- **Flexible**: [What can change and within what limits]

### Examples

**Correct**:
- "[Example 1]" — [Why it works]
- "[Example 2]" — [Why it works]

**Incorrect**:
- "[Example 1]" — [Why it fails]
- "[Example 2]" — [Why it fails]

### Edge cases
- [Scenario]: [How to handle]
```

## Pattern library overview
Use this as the top-level document:

```md
# Content Pattern Library

## Purpose
[What this library enables, who it's for]

## How to use this library
1. Identify the content type you need
2. Find the matching pattern
3. Apply the structure and rules
4. Check your content against correct/incorrect examples
5. Validate against variation boundaries

## Pattern index

| Pattern | Content type | Use when |
|---------|--------------|----------|
| [Name] | [Type] | [Brief trigger] |

## Global rules
These apply to all patterns:
- [Rule 1]
- [Rule 2]
- [Rule 3]

## Patterns
[Links to individual pattern entries]
```

## Pattern decision tree
Use when multiple patterns might apply:

```md
## Decision tree: [Content category]

**Start here**: What is the user's situation?

```
Is this an error?
├── Yes → Is the error user-caused or system-caused?
│   ├── User-caused → Use: Validation Error pattern
│   └── System-caused → Use: System Error pattern
└── No → Is this a confirmation?
    ├── Yes → Is the action reversible?
    │   ├── Yes → Use: Confirmation (Reversible) pattern
    │   └── No → Use: Confirmation (Irreversible) pattern
    └── No → [Continue branching]
```
```
