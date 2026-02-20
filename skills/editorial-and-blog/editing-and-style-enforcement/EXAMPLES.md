# Examples

## Example 1: Blog post edit with house style

**Input:**
- Draft: "We're thrilled to announce that our new Dashboard feature is now available! This will allow users to be able to customize their workspace, utilize advanced filtering, and access real-time data. The Dashboard was built from the ground up to address customer pain points that we've been hearing about for awhile now."
- Style guide: Sentence case headings, no exclamation marks, "customer" not "user", avoid corporate enthusiasm phrases
- Channel: Company blog

**Output:**

```md
## Edited content

We're releasing the new Dashboard feature today. It lets customers customize their workspace, use advanced filtering, and access real-time data. The Dashboard addresses customer pain points we've heard consistently in feedback.

---

## Change log

| Location | Original | Change | Rationale |
|----------|----------|--------|-----------|
| Sentence 1 | "thrilled to announce" | "releasing" | Avoid corporate enthusiasm per style guide |
| Sentence 1 | "!" | "." | No exclamation marks per style guide |
| Sentence 2 | "will allow users to be able to" | "lets customers" | Concision + "customer" terminology |
| Sentence 2 | "utilize" | "use" | Simpler word |
| Sentence 3 | "built from the ground up" | removed | Cliché, adds no value |
| Sentence 3 | "for awhile now" | "consistently in feedback" | More specific, correct spelling |

## Flags for author review

None.
```

---

## Example 2: Technical content with fact-checking flags

**Input:**
- Draft: "The API processes requests 10x faster than the previous version. Simply call the endpoint and it handles everything automatically. Error handling is built-in so you don't need to worry about edge cases."
- Style guide: AP style
- Audience: Developers

**Output:**

```md
## Edited content

The API processes requests 10x faster than the previous version. Call the endpoint, and it handles the request automatically. Error handling is built in, though you should still handle specific edge cases in your implementation.

---

## Change log

| Location | Original | Change | Rationale |
|----------|----------|--------|-----------|
| Sentence 2 | "Simply call" | "Call" | "Simply" minimizes complexity inappropriately |
| Sentence 2 | added comma | "endpoint, and" | Comma before conjunction joining independent clauses |
| Sentence 3 | "built-in" | "built in" | AP style: no hyphen when used as predicate adjective |
| Sentence 3 | "so you don't need to worry" | "though you should still handle" | Corrects misleading claim |

## Flags for author review

- [ ] Sentence 1: "10x faster" — verify this claim with engineering; provide benchmark context
- [ ] Sentence 3: Clarify which edge cases require handling vs. which are covered by built-in error handling
```

---

## Example 3: Edge case — preserving intentional style choices

**Input:**
- Draft: "Yeah, we messed up. The update broke saved preferences for about 12 hours on Tuesday. Here's what happened and what we're doing about it."
- Style guide: Company blog guidelines (formal)
- Context: Incident postmortem, CEO requested conversational tone to convey authenticity

**Output:**

```md
## Edited content

Yeah, we messed up. The update broke saved preferences for about 12 hours on Tuesday. Here's what happened and what we're doing about it.

---

## Change log

| Location | Original | Change | Rationale |
|----------|----------|--------|-----------|
| — | — | No changes | Informal tone is intentional per author direction |

## Flags for author review

- [ ] Confirm CEO approval for informal opening ("Yeah, we messed up") — deviates from standard blog voice
- [ ] Consider adding specific time window (e.g., "between 2 PM and 2 AM EST")

## Style deviations

| Deviation | Style guide rule | Reason for departure |
|-----------|------------------|---------------------|
| Informal opening | Formal tone for company blog | Author-directed for authenticity in incident communication |
| Contraction "we're" | Avoid contractions | Matches conversational intent |
```

---

## Example 4: Heavy structural edit

**Input:**
- Draft: A 500-word article with information scattered across paragraphs, no clear structure, mixing benefits and features randomly
- Style guide: Chicago Manual of Style
- Request: Restructure for clarity

**Output:**

```md
## Edited content

[Restructured article with clear sections: Introduction, Key Features, Benefits, Getting Started]

---

## Change log

| Location | Original | Change | Rationale |
|----------|----------|--------|-----------|
| Structure | No headings | Added 4 section headings | Improve scannability |
| Para 1-2 | Mixed feature/benefit claims | Separated into distinct sections | Logical grouping |
| Para 3 | Buried lede | Moved key benefit to introduction | Lead with value |
| Throughout | Passive voice (8 instances) | Active voice | Clarity and directness |

## Flags for author review

- [ ] New structure changes the emphasis — confirm this aligns with article goals
- [ ] Moved "Getting Started" CTA to end — verify this is the desired user action
```
