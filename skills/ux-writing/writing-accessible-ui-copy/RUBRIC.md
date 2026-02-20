# Rubric: Writing Accessible UI Copy

Evaluation criteria for accessible content across four proficiency levels.

---

## Table of contents
- [Scoring guide](#scoring-guide)
- [Dimension 1: Alt text quality](#dimension-1-alt-text-quality)
- [Dimension 2: Interactive element labels](#dimension-2-interactive-element-labels)
- [Dimension 3: Content structure](#dimension-3-content-structure)
- [Dimension 4: Language clarity](#dimension-4-language-clarity)
- [Dimension 5: Assistive technology support](#dimension-5-assistive-technology-support)
- [Scoring thresholds](#scoring-thresholds)

---

## Scoring guide

| Score | Level | Description |
|-------|-------|-------------|
| 4 | Expert | Exceeds WCAG AA; exemplary inclusive design |
| 3 | Proficient | Meets WCAG AA; consistently accessible |
| 2 | Developing | Partial compliance; some barriers remain |
| 1 | Novice | Significant barriers; fails basic requirements |

---

## Dimension 1: Alt text quality

### Level 4 — Expert
- All images have appropriate alt text (informative, decorative, or functional)
- Complex images have extended descriptions
- Alt text is concise yet complete (under 125 chars for simple images)
- Context-appropriate: same image may have different alt in different contexts
- No redundant "image of" or "photo of" prefixes

### Level 3 — Proficient
- Informative images have descriptive alt text
- Decorative images have empty alt (alt="")
- Alt text describes what matters, not just what's visible
- Length is appropriate for image complexity

### Level 2 — Developing
- Alt text present but may be too brief or too verbose
- Some decorative images incorrectly labeled
- May include "image of" prefixes
- Complex images lack extended descriptions

### Level 1 — Novice
- Alt text missing or uses filename
- Decorative images have meaningless alt
- Over-describes or under-describes consistently
- No awareness of context-dependent descriptions

---

## Dimension 2: Interactive element labels

### Level 4 — Expert
- All buttons describe specific action + object ("Save draft", not "Save")
- Links are meaningful out of context (tested in links list)
- Form labels are visible, associated, and unambiguous
- No duplicate labels where differentiation matters
- Aria-label used appropriately (only when visible text insufficient)

### Level 3 — Proficient
- Buttons have action verbs + objects
- Links avoid "click here" and "learn more" patterns
- Form fields have visible labels (not placeholder-only)
- Error messages are associated with their fields

### Level 2 — Developing
- Some generic labels ("Submit", "Continue") without context
- Links sometimes rely on surrounding text for meaning
- Labels present but occasionally ambiguous
- Aria-label overused as a crutch for poor visible text

### Level 1 — Novice
- Generic labels throughout ("Click here", "Submit")
- Links meaningless out of context
- Placeholder text used as primary label
- No awareness of label + action relationship

---

## Dimension 3: Content structure

### Level 4 — Expert
- Heading hierarchy is logical and complete (h1 → h2 → h3)
- Single h1 per page describes page purpose
- Headings alone tell the page story (navigable by heading)
- Lists used for related items (not forced into paragraphs)
- Landmarks properly applied (nav, main, aside, etc.)

### Level 3 — Proficient
- No skipped heading levels
- Headings are descriptive (not "Section 1")
- Major content sections have headings
- One h1 per page

### Level 2 — Developing
- Heading levels occasionally skipped
- Some headings used for styling, not structure
- h1 may be missing or duplicated
- Structure exists but is inconsistent

### Level 1 — Novice
- Headings used for visual styling only
- No logical hierarchy
- Missing h1 or structural landmarks
- Content structure invisible to assistive tech

---

## Dimension 4: Language clarity

### Level 4 — Expert
- Reading level appropriate for audience (typically grade 8 or below)
- Consistent terminology throughout (no synonym confusion)
- Instructions don't rely on sensory characteristics
- Complex concepts have plain-language explanations
- Abbreviations expanded on first use

### Level 3 — Proficient
- Plain language used for most content
- Jargon avoided or explained
- Instructions are task-focused, not location-focused
- Sentence structure is clear and direct

### Level 2 — Developing
- Some unnecessary complexity
- Occasional jargon without explanation
- Directional instructions ("click the button on the right")
- Inconsistent terminology

### Level 1 — Novice
- Dense, complex language throughout
- Heavy jargon without explanation
- Relies on visual/spatial references
- Assumes knowledge user may not have

---

## Dimension 5: Assistive technology support

### Level 4 — Expert
- Status changes announced appropriately (aria-live regions)
- Dynamic content updates communicate to screen readers
- Focus management is intentional and tested
- No information conveyed by color alone
- Tested with actual assistive technology

### Level 3 — Proficient
- Important status changes have announcements
- Form errors are announced and associated
- Color is supplemented with text/icons
- Focus order is logical

### Level 2 — Developing
- Some status changes not announced
- Errors may not be programmatically associated
- Color sometimes only differentiator
- Limited testing with assistive tech

### Level 1 — Novice
- No consideration for screen reader announcements
- Errors not associated with fields
- Color-only differentiation common
- No assistive technology testing

---

## Scoring thresholds

| Total score | Rating | Recommendation |
|-------------|--------|----------------|
| 18-20 | Exemplary | Ship with confidence |
| 14-17 | Passing | Minor refinements recommended |
| 10-13 | Needs work | Address gaps before shipping |
| 5-9 | Failing | Major revision required |

---

## Quick-fail criteria

Any of these result in automatic failure regardless of other scores:

| Criterion | Reason |
|-----------|--------|
| Missing alt text on informative images | WCAG 1.1.1 failure |
| No visible form labels | WCAG 1.3.1, 3.3.2 failure |
| "Click here" as sole link text | WCAG 2.4.4 failure |
| Information by color alone | WCAG 1.4.1 failure |
| No programmatic heading structure | WCAG 1.3.1 failure |

---

## Scoring worksheet

```yaml
evaluation:
  component: "[Name]"
  evaluator: "[Name]"
  date: "[Date]"
  
  scores:
    alt_text_quality: [1-4]
    interactive_labels: [1-4]
    content_structure: [1-4]
    language_clarity: [1-4]
    assistive_tech_support: [1-4]
    
  total: "[Sum]"
  quick_fail: "[yes|no]"
  quick_fail_reason: "[If applicable]"
  
  recommendation: "[Ship|Refine|Revise|Reject]"
  priority_fixes: |
    1. [Most critical issue]
    2. [Second priority]
    3. [Third priority]
```
