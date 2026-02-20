# Readability Techniques

## Table of contents
- [Sentence-level techniques](#sentence-level-techniques)
- [Paragraph-level techniques](#paragraph-level-techniques)
- [Flow and rhythm](#flow-and-rhythm)
- [Structural techniques](#structural-techniques)

---

## Sentence-level techniques

### Front-load meaning
Put the subject and main verb early. Move qualifications to the end.

| Before | After |
|--------|-------|
| "In situations where users need to reset their password, they should click the 'Forgot Password' link." | "To reset your password, click 'Forgot Password.'" |
| "Due to the complexity of the implementation, we have decided to delay the launch." | "We're delaying the launch due to implementation complexity." |

### Choose active voice
Active voice is clearer and more direct. Use passive only when the actor is unknown or unimportant.

| Passive | Active |
|---------|--------|
| "The report was written by the team." | "The team wrote the report." |
| "Errors are handled by the system." | "The system handles errors." |
| "The bug was discovered during testing." | (Keep passive — who discovered it isn't the point) |

### Reduce nominalizations
Convert noun phrases back to verbs.

| Nominalization | Verb form |
|----------------|-----------|
| "make a decision" | "decide" |
| "perform an analysis" | "analyze" |
| "provide an explanation" | "explain" |
| "reach a conclusion" | "conclude" |

### Cut filler phrases

| Cut | Keep |
|-----|------|
| "It is important to note that" | (delete, start with the note) |
| "In order to" | "To" |
| "Due to the fact that" | "Because" |
| "At this point in time" | "Now" |
| "The reason why is that" | "Because" |
| "Is able to" | "Can" |

### Specify over generalize

| Vague | Specific |
|-------|----------|
| "Soon" | "Within two weeks" |
| "Significant improvement" | "40% faster" |
| "Many users" | "2,000 users" |
| "Recently" | "Last month" |

---

## Paragraph-level techniques

### One idea per paragraph
Each paragraph should have one main point. If you're explaining two things, use two paragraphs.

**Test:** Can you summarize the paragraph in one sentence? If not, split it.

### Lead with the topic sentence
State the paragraph's main idea first. Support it after.

**Before:**
> There are several factors to consider, including cost, implementation time, and team capacity. The vendor's track record also matters. When evaluating options, reliability should be weighted heavily.

**After:**
> Reliability should be your top priority when evaluating options. Other factors — cost, implementation time, team capacity, and vendor track record — matter, but they're secondary.

### Transition between paragraphs
Each paragraph should connect to the previous one. Use:
- **Continuation:** "Additionally," "Furthermore," "Building on this,"
- **Contrast:** "However," "Despite this," "On the other hand,"
- **Consequence:** "As a result," "Therefore," "This means,"
- **Example:** "For instance," "Consider this case,"

### Paragraph length guidelines

| Context | Target length |
|---------|---------------|
| Web content | 2-4 sentences |
| Print/PDF | 3-5 sentences |
| Technical docs | 3-6 sentences |
| Email | 1-3 sentences |

---

## Flow and rhythm

### Vary sentence length
Monotonous rhythm kills engagement. Mix sentence lengths.

**Choppy (all short):**
> The system failed. Users were angry. We investigated. The bug was found. We fixed it.

**Improved (varied):**
> The system failed, and users were angry. We investigated immediately. The bug — a race condition in the authentication flow — was found within hours. We pushed a fix the same day.

### The short sentence for emphasis
Short sentences stand out. Use them for key points.

> The migration took six months. We tested everything. We planned for every scenario. It still broke.

### Control reading pace
- **Speed up:** Short sentences, simple words, active voice
- **Slow down:** Longer sentences, commas, subordinate clauses

Use slow pace for complex ideas that need digestion. Use fast pace for action or emphasis.

### Lists break monotony
When you have 3+ parallel items, use a list:

**Before:**
> The system supports exports to CSV, JSON, XML, and PDF formats.

**After:**
> The system supports exports to:
> - CSV
> - JSON
> - XML
> - PDF

---

## Structural techniques

### Subheadings as signposts
Readers scan subheadings. They should:
- Tell readers what's coming
- Use parallel structure
- Be specific (not "More Information")

| Weak | Strong |
|------|--------|
| "Background" | "Why We Built This" |
| "Details" | "How the Algorithm Works" |
| "More" | "Advanced Configuration" |

### Visual breaks
Web readers need visual variety. Add every 500-800 words:
- Subheading
- List
- Table
- Callout/blockquote
- Image or diagram

### Information hierarchy
Put the most important information first:
1. Key takeaway or action
2. Essential context
3. Supporting details
4. Background/history
5. Exceptions and edge cases

### Scannable formatting

| Technique | Use for |
|-----------|---------|
| **Bold** | Key terms, emphasis (sparingly) |
| *Italic* | New terms, titles, light emphasis |
| `Code` | Commands, file names, variables |
| > Blockquote | Callouts, quotes, warnings |
| Lists | 3+ parallel items, steps |
| Tables | Comparisons, specifications |
