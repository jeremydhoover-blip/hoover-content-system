# Editing Heuristics

## Table of contents
- [Edit priority order](#edit-priority-order)
- [Clarity edits](#clarity-edits)
- [Concision patterns](#concision-patterns)
- [Voice consistency checks](#voice-consistency-checks)
- [When to flag vs. fix](#when-to-flag-vs-fix)

---

## Edit priority order

Apply edits in this sequence to avoid rework:

| Priority | Edit type | Examples |
|----------|-----------|----------|
| 1 | Structural | Heading hierarchy, paragraph breaks, section order |
| 2 | Factual accuracy | Claims, statistics, proper nouns |
| 3 | Clarity | Ambiguous pronouns, unclear antecedents, logical gaps |
| 4 | Concision | Redundancy, filler phrases, unnecessary qualifiers |
| 5 | Voice/tone | Formality level, terminology consistency |
| 6 | Grammar | Subject-verb agreement, tense consistency |
| 7 | Style guide mechanics | Capitalization, punctuation, number formatting |
| 8 | Spelling | Typos, commonly confused words |

---

## Clarity edits

### Ambiguous pronoun test
If a sentence has "it," "this," "they," or "that" — can you point to the exact referent? If not, make explicit.

**Before**: "The system sends the notification to the server. It processes it immediately."
**After**: "The system sends the notification to the server. The server processes the notification immediately."

### Logical gap test
Read each sentence pair. Does sentence B follow from sentence A without requiring inference?

**Gap**: "We rebuilt the search algorithm. Users love the new experience."
**Filled**: "We rebuilt the search algorithm to return results 3x faster. Users report finding what they need more quickly."

### Front-load meaning
Put the subject and main verb early. Delay qualifications.

**Before**: "In order to ensure that users are able to access their data securely, we implemented encryption."
**After**: "We implemented encryption to secure user data access."

---

## Concision patterns

### Remove without meaning loss

| Pattern | Example | Fix |
|---------|---------|-----|
| "in order to" | "in order to save" | "to save" |
| "is able to" | "is able to run" | "can run" |
| "the fact that" | "due to the fact that" | "because" |
| "at this point in time" | — | "now" |
| "it is important to note that" | — | delete or start with the note |
| "as a way to" | "as a way to improve" | "to improve" |
| Doubled words | "past history," "future plans" | "history," "plans" |

### Verb over noun phrase

| Noun phrase | Verb form |
|-------------|-----------|
| "make a decision" | "decide" |
| "perform an analysis" | "analyze" |
| "provide assistance" | "help" |
| "conduct an investigation" | "investigate" |

---

## Voice consistency checks

### Person consistency
Pick one and maintain throughout:
- **Second person** ("you"): Direct, instructional
- **Third person** ("users," "customers"): Formal, distanced
- **First person plural** ("we"): Inclusive, conversational

**Inconsistent**: "Users can customize their dashboard. You can also export your data."
**Consistent**: "You can customize your dashboard. You can also export your data."

### Tense consistency
Default to present tense for features and capabilities. Use past tense only for historical events.

**Inconsistent**: "The feature allows exports. Users were able to filter results."
**Consistent**: "The feature allows exports. Users can filter results."

### Formality markers

| Informal | Formal |
|----------|--------|
| "gonna," "wanna" | "going to," "want to" |
| "stuff," "things" | specific nouns |
| "pretty much" | "largely," "mostly" |
| "a lot of" | "many," "significant" |
| Starting with "So," | Remove or restructure |

---

## When to flag vs. fix

### Always fix silently
- Typos and spelling errors
- Obvious grammar errors
- Style guide mechanics (capitalization, punctuation)
- Redundant words and phrases
- Passive voice (when active is clearer)

### Always flag for author
- Factual claims you cannot verify
- Meaning-altering changes
- Deletions of more than one sentence
- Tone changes that affect brand voice
- Technical terminology changes
- Structural reorganization

### Judgment call (document reasoning)
- Word choice that affects nuance
- Removing examples or analogies
- Simplifying technical explanations
- Adding clarifying phrases
