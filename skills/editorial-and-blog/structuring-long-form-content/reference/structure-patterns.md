# Structure Patterns

## Table of contents
- [Content type structures](#content-type-structures)
- [Section sequencing strategies](#section-sequencing-strategies)
- [Scannable element placement](#scannable-element-placement)
- [Progressive disclosure for length](#progressive-disclosure-for-length)

---

## Content type structures

Different content types require different structural approaches:

### Reference content
**Reader behavior:** Jumps to specific sections, rarely reads linearly.
**Structure needs:** Strong navigation, standalone sections, alphabetical or logical grouping.

```
- Quick navigation (TOC or index)
- Brief intro (what this covers)
- Sections organized by topic or category
- Cross-references between related sections
- Search-friendly headings
```

### Instructional content
**Reader behavior:** Follows sequence, needs to complete steps.
**Structure needs:** Clear progression, prerequisites upfront, checkpoints.

```
- Prerequisites
- Overview of what will be accomplished
- Sequential numbered sections
- Verification points
- Troubleshooting
- Next steps
```

### Persuasive content
**Reader behavior:** May skim, needs to be hooked, follows argument.
**Structure needs:** Strong opening, logical progression, evidence placement.

```
- Hook / thesis
- Problem establishment
- Solution / argument
- Evidence
- Implications / call to action
```

### Narrative content
**Reader behavior:** Reads linearly, engaged by story.
**Structure needs:** Flow between sections, chronological or logical arc.

```
- Setup (context, characters, stakes)
- Journey (events, challenges, decisions)
- Resolution (outcomes, lessons)
- Reflection (implications, takeaways)
```

---

## Section sequencing strategies

### By reader priority (inverted pyramid)
Most important information first. Good for: news, announcements, reference.

```
1. Key takeaways / summary
2. Essential details
3. Supporting information
4. Background / context
5. Additional resources
```

### By task flow
Follow the order the reader will do things. Good for: guides, tutorials.

```
1. What you need before starting
2. First action
3. Second action
4. ... (in order)
5. What to do after completion
```

### By complexity (simple to complex)
Build understanding progressively. Good for: educational content.

```
1. Basic concepts
2. Intermediate applications
3. Advanced techniques
4. Edge cases and exceptions
```

### By scope (general to specific)
Start broad, narrow down. Good for: strategy docs, comprehensive guides.

```
1. Overview and principles
2. Categories / types
3. Specific implementations
4. Details and exceptions
```

### By frequency (common to rare)
Most-used information first. Good for: reference docs, FAQs.

```
1. Common scenarios (80% of use cases)
2. Less common scenarios
3. Edge cases
4. Deprecated or legacy information
```

---

## Scannable element placement

Long-form content needs regular visual breaks and entry points.

### Frequency guidelines

| Content type | Scannable element every... |
|--------------|---------------------------|
| Reference | 300-500 words |
| Educational | 500-700 words |
| Narrative | 700-1000 words |
| Technical | 400-600 words |

### Scannable element types

| Element | Best for | Example use |
|---------|----------|-------------|
| Subheading | Topic shifts | Breaking up sections |
| Bulleted list | Multiple items | Options, requirements |
| Numbered list | Sequences | Steps, priorities |
| Table | Comparisons | Features, options |
| Callout/box | Emphasis | Warnings, tips |
| Pull quote | Key insights | Important statements |
| Code block | Technical content | Commands, examples |
| Image/diagram | Visual concepts | Processes, architecture |

### Placement rules

1. **Never go more than 1 screen without a visual break** (varies by device, ~500-800 words)
2. **Place callouts at decision points**, not randomly
3. **Tables beat paragraphs** for comparative information
4. **Lists beat paragraphs** for 3+ items
5. **Subheadings should be scannable as a sequence** — reading just the headings should convey the structure

---

## Progressive disclosure for length

### When to split content

Consider splitting if:
- Word count exceeds 4000 words
- Content serves distinct audiences
- Sections are used independently
- Topics have different update frequencies

### Splitting strategies

**Split by audience:**
- API Reference (for developers)
- API Concepts (for architects)
- API Quickstart (for evaluators)

**Split by depth:**
- Overview
- Getting Started
- Deep Dive
- Reference

**Split by topic:**
- Part 1: Fundamentals
- Part 2: Advanced Patterns
- Part 3: Troubleshooting

### When to keep together

Keep as single document if:
- Topics are highly interdependent
- Readers need full context to act
- Content will be downloaded/printed
- SEO benefits from comprehensive single page

### Connecting split content

When content is split, always:
1. Link between parts explicitly
2. Indicate "Part X of Y" in titles
3. Provide overview page listing all parts
4. Cross-reference when concepts depend on other parts
