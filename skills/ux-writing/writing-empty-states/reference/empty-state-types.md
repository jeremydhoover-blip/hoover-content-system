# Empty State Types

## Table of contents
- [Type definitions](#type-definitions)
- [Diagnosis flowchart](#diagnosis-flowchart)
- [Tone guidance](#tone-guidance)
- [Common mistakes](#common-mistakes)

---

## Type definitions

| Type | Definition | User expectation | Primary goal |
|------|------------|------------------|--------------|
| **first-run** | User has never created content in this area | Onboarding, exploration | Motivate first action |
| **no-results** | Search or filter returned zero matches | Results that match query | Help refine search |
| **user-cleared** | User intentionally emptied the list | Confirmation of action | Set future expectations |
| **error-caused** | Empty because content failed to load | Content to appear | Enable retry/recovery |

---

## Diagnosis flowchart

```
Is there content in the database for this user/view?
├─ NO → Has user ever created content here?
│       ├─ NO → first-run
│       └─ YES → user-cleared
│
└─ YES → Did the fetch succeed?
         ├─ NO → error-caused
         └─ YES → Is there an active search/filter?
                  ├─ YES → no-results
                  └─ NO → user-cleared (rare: data deleted externally)
```

---

## Tone guidance

| Type | Tone | Opening patterns |
|------|------|------------------|
| **first-run** | Encouraging, welcoming | "Create your first...", "Get started with...", "Welcome to..." |
| **no-results** | Helpful, neutral | "No results for...", "We couldn't find...", "No matches" |
| **user-cleared** | Calm, confirming | "All caught up", "No [items] yet", "[Items] you [verb] will appear here" |
| **error-caused** | Direct, reassuring | "Couldn't load...", "Something went wrong" |

### Tone rules
- First-run: Emphasize value and possibility, not absence
- No-results: Be factual, offer alternatives immediately
- User-cleared: Don't make it sound like something is missing
- Error-caused: Follow error message conventions

---

## Common mistakes

| Mistake | Problem | Fix |
|---------|---------|-----|
| "Nothing to see here" | Vague, slightly dismissive | Specify what would appear and how to populate |
| "You have 0 items" | Technical, cold | "No items yet" or type-specific headline |
| Same copy for all types | Misses context-specific guidance | Diagnose type, adapt copy |
| No action for first-run | User stuck, doesn't know what to do | Always provide primary action |
| "Your search returned no results" | Overly formal, wordy | "No results for [query]" |
| Missing content type | Generic "No results" | Include what they searched for or filtered by |
