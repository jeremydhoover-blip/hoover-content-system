# Templates

## Default output: AI context pack

```md
# Context Pack: <Feature Name>

## Metadata
- **Feature:** <name>
- **Version:** <x.y.z>
- **Last updated:** <YYYY-MM-DD>
- **Target AI system:** <system name or "general">
- **Token budget:** <approximate token count>

## Feature overview
<2-3 sentences describing what the feature does and who uses it>

## Content generation scope
This context pack enables AI to generate:
- <content type 1> (e.g., error messages)
- <content type 2> (e.g., empty states)
- <content type 3> (e.g., confirmation dialogs)

This context pack does NOT cover:
- <out of scope content>

---

## Vocabulary

### Required terms
| Concept | Use this | Never use |
|---------|----------|-----------|
| <concept> | <canonical term> | <prohibited terms> |

### Definitions
- **<term>:** <precise definition>

---

## States

The AI must know what state the UI is in before generating content.

| State | User situation | Tone | Content focus |
|-------|---------------|------|---------------|
| <state> | <what user experiences> | <tone range> | <what to emphasize> |

---

## Constraints

### Hard constraints (never violate)
- <constraint 1>
- <constraint 2>

### Soft constraints (prefer but can flex)
- <constraint 1>
- <constraint 2>

### Character limits
| Content type | Limit | Rationale |
|--------------|-------|-----------|
| <type> | <N chars> | <why this limit> |

### Prohibited content
- Never: <prohibited pattern 1>
- Never: <prohibited pattern 2>

---

## Tone guidance

### Default tone
<description of baseline tone>

### Tone by state
| State | Tone adjustment |
|-------|-----------------|
| <error state> | <more empathetic, solution-focused> |
| <success state> | <celebratory but brief> |

### Tone boundaries
- Never sound: <too casual, too formal, etc.>
- Always sound: <helpful, competent, etc.>

---

## Examples

### Example 1: <Content type>
**State:** <state>
**Input:** <trigger or context>

✓ **Good:**
```
<correct output>
```
**Why it works:** <explanation>

✗ **Bad:**
```
<incorrect output>
```
**Why it fails:** <explanation>

---

### Example 2: <Content type>
<repeat structure>

---

## Edge cases

| Scenario | Handling |
|----------|----------|
| <edge case> | <how to handle> |

---

## Validation checklist
- [ ] Vocabulary section complete
- [ ] All states documented
- [ ] Hard constraints listed
- [ ] Character limits specified
- [ ] At least 3 examples with good/bad pairs
- [ ] Edge cases documented
- [ ] Token count within budget
```

## Compact context pack (for token-limited systems)

```md
# Context: <Feature Name>

## Scope
Generate: <content types>
Feature: <1-sentence description>

## Terms
Use: <term1>, <term2>
Never: <prohibited1>, <prohibited2>

## States
- <state1>: <tone + focus>
- <state2>: <tone + focus>

## Constraints
- Hard: <constraint1>; <constraint2>
- Limits: <type1> ≤<N>chars; <type2> ≤<N>chars
- Never: <prohibited pattern>

## Examples
Good (<state>): "<example>"
Bad (<state>): "<example>" — <why bad>
```

## Context pack for specific content type

```md
# Error Message Context: <Feature Name>

## When to use
Generate error messages for <feature> when <triggers>.

## Error types covered
| Error type | Cause | Recovery path |
|------------|-------|---------------|
| <type> | <cause> | <what user should do> |

## Template
```
<Headline: What happened>
<Body: Why it happened + how to fix>
<CTA: Action to resolve>
```

## Constraints
- Headline: ≤50 chars, no periods, no blame
- Body: ≤100 chars, include recovery action
- CTA: ≤20 chars, action verb + noun

## Prohibited
- "Error", "Failed", "Invalid" in headlines
- Technical jargon
- Blame language ("You did...", "Your fault...")

## Examples
<state>: 
✓ "Couldn't save changes. Check your connection and try again." [Save again]
✗ "Network error occurred. Request failed." [Retry]
```
