# Common Pitfalls Reference

## Table of contents
1. [Ambiguity pitfalls](#ambiguity-pitfalls)
2. [Completeness pitfalls](#completeness-pitfalls)
3. [Contradiction pitfalls](#contradiction-pitfalls)
4. [Context pitfalls](#context-pitfalls)
5. [Testing for pitfalls](#testing-for-pitfalls)

---

## Ambiguity pitfalls

### Subjective terms without definition

| Pitfall | Problem | Fix |
|---------|---------|-----|
| "Be concise" | How concise? | "Limit responses to 150 words" |
| "Respond appropriately" | Appropriate how? | "Match formality to user's tone" |
| "Handle errors gracefully" | What does graceful mean? | "Log error, attempt retry, report failure" |
| "Use good judgment" | Whose judgment? | "When uncertain, ask rather than assume" |
| "Prioritize important tasks" | Important by what criteria? | "Priority order: security > functionality > style" |

### Implicit assumptions

| Pitfall | Problem | Fix |
|---------|---------|-----|
| "Check the database" | Which database? | "Query the `users` table in the primary PostgreSQL database" |
| "Follow the style guide" | Which guide? Where? | "Follow /docs/style-guide.md" |
| "Use standard format" | Standard to whom? | "Use JSON with ISO 8601 dates" |
| "Apply best practices" | Which practices? | List specific practices or link to reference |

### Undefined pronouns

| Pitfall | Problem | Fix |
|---------|---------|-----|
| "It should be validated" | What should be validated? | "The user input should be validated" |
| "They must approve" | Who must approve? | "The admin user must approve" |
| "This is required" | This what? | "User authentication is required" |

---

## Completeness pitfalls

### Missing negative cases

**Problem**: Instructions say what to do but not what not to do.

```md
✗ Incomplete:
"Answer user questions about the product."

✓ Complete:
"Answer user questions about the product.
Do NOT:
- Answer questions about competitor products
- Provide pricing or discount information
- Make promises about future features"
```

### Missing edge cases

**Problem**: Instructions cover happy path but not exceptions.

```md
✗ Missing edge cases:
"Search for files and return results."

✓ With edge cases:
"Search for files and return results.
- If no results: Report 'No matches found for [query]'
- If >100 results: Return first 100 with note 'Showing 100 of N results'
- If search times out: Report 'Search timed out, try narrower query'"
```

### Missing error guidance

**Problem**: No instructions for when things go wrong.

```md
✗ No error handling:
"Connect to the API and fetch data."

✓ With error handling:
"Connect to the API and fetch data.
- If connection fails: Retry up to 3 times with exponential backoff
- If auth fails: Report 'Authentication failed, check credentials'
- If rate limited: Wait and retry, report delay to user"
```

---

## Contradiction pitfalls

### Direct contradictions

**Problem**: Two rules directly conflict.

```md
✗ Contradictory:
"Always ask for confirmation before taking action."
"Respond quickly without unnecessary delays."

✓ Resolved:
"Ask for confirmation before destructive actions (delete, overwrite).
Execute non-destructive actions (read, search, list) immediately."
```

### Priority conflicts

**Problem**: Multiple rules apply with unclear precedence.

```md
✗ Unclear priority:
"Be thorough in your responses."
"Be concise in your responses."

✓ Clear priority:
"Default to concise responses (≤150 words).
Be thorough when:
- User explicitly asks for detail
- Topic requires nuance for safety
- Initial concise response was insufficient"
```

### Scope overlaps

**Problem**: Rules for different scenarios conflict when both apply.

```md
✗ Overlapping:
"For code questions: Show full implementation."
"For security questions: Never show sensitive code."

What about code questions involving security?

✓ Resolved:
"For code questions: Show full implementation.
Exception: Never show credentials, keys, or auth logic—describe approach instead."
```

---

## Context pitfalls

### Assuming persistent memory

**Problem**: Instructions assume the agent remembers previous interactions.

```md
✗ Assumes memory:
"Continue from where you left off."
"Reference the previous discussion."

✓ Stateless-friendly:
"Each request is independent. If context from a previous interaction is needed, user must provide it."
```

### Assuming external knowledge

**Problem**: Instructions reference information the agent won't have.

```md
✗ Assumes knowledge:
"Follow the team's conventions."
"Use the standard process."

✓ Self-contained:
"Follow these conventions: [list them]"
"Process: 1. [step] 2. [step] 3. [step]"
```

### Assuming tool availability

**Problem**: Instructions reference tools the agent might not have.

```md
✗ Assumes tools:
"Check the calendar for availability."

✓ Tool-aware:
"If calendar tool available: Check availability.
If not: Ask user to provide available times."
```

---

## Testing for pitfalls

### Ambiguity test
Read each instruction and ask: "Could two reasonable people interpret this differently?"

### Completeness test
For each action, ask: "What if this fails? What if input is invalid? What if result is empty?"

### Contradiction test
For each rule, ask: "Is there another rule that conflicts with this one? Which wins?"

### Context test
For each instruction, ask: "Does this assume something the agent won't know or have access to?"

### Adversarial test
Ask: "How could a malicious user exploit ambiguity or gaps in these instructions?"
