# WCAG Content Requirements

Web Content Accessibility Guidelines mapped to content design decisions.

---

## Table of contents
- [Perceivable guidelines](#perceivable-guidelines)
- [Understandable guidelines](#understandable-guidelines)
- [Operable guidelines (content-related)](#operable-guidelines-content-related)
- [Robust guidelines (content-related)](#robust-guidelines-content-related)
- [Conformance levels](#conformance-levels)

---

## Perceivable guidelines

### 1.1 Text Alternatives

| Guideline | Level | Requirement | Content action |
|-----------|-------|-------------|----------------|
| 1.1.1 Non-text Content | A | Text alternatives for non-text content | Write alt text for images, icons |

**Alt text rules:**
- Informative images: Describe content and function
- Decorative images: Use empty alt (alt="")
- Functional images: Describe action/destination
- Complex images: Provide short alt + long description

### 1.3 Adaptable

| Guideline | Level | Requirement | Content action |
|-----------|-------|-------------|----------------|
| 1.3.1 Info and Relationships | A | Structure conveyed programmatically | Use proper headings, labels |
| 1.3.2 Meaningful Sequence | A | Logical reading order | Structure content linearly |
| 1.3.3 Sensory Characteristics | A | Don't rely on shape/size/location | Avoid "click the round button" |

### 1.4 Distinguishable

| Guideline | Level | Requirement | Content action |
|-----------|-------|-------------|----------------|
| 1.4.1 Use of Color | A | Color not sole differentiator | Add text/icons with color |
| 1.4.5 Images of Text | AA | Avoid text in images | Use real text, not images |

---

## Understandable guidelines

### 3.1 Readable

| Guideline | Level | Requirement | Content action |
|-----------|-------|-------------|----------------|
| 3.1.1 Language of Page | A | Page language identified | Specify lang attribute |
| 3.1.2 Language of Parts | AA | Language of passages identified | Mark language changes |
| 3.1.3 Unusual Words | AAA | Define jargon/idioms | Provide definitions |
| 3.1.4 Abbreviations | AAA | Expand abbreviations | Define on first use |
| 3.1.5 Reading Level | AAA | Lower secondary education level | Write at ~grade 8 |

**Reading level guidance:**
- Target: Grade 8 reading level for general audiences
- Test with readability tools (Flesch-Kincaid, Hemingway)
- Use short sentences (15-20 words average)
- Use common words over technical terms

### 3.2 Predictable

| Guideline | Level | Requirement | Content action |
|-----------|-------|-------------|----------------|
| 3.2.4 Consistent Identification | AA | Same function = same name | Use consistent labels |

**Consistency rules:**
- Same action → same label (always "Save", not sometimes "Submit")
- Same icon → same meaning
- Same term → same definition

### 3.3 Input Assistance

| Guideline | Level | Requirement | Content action |
|-----------|-------|-------------|----------------|
| 3.3.1 Error Identification | A | Errors identified in text | Describe the error clearly |
| 3.3.2 Labels or Instructions | A | Labels provided for inputs | Write visible labels |
| 3.3.3 Error Suggestion | AA | Suggest fixes when known | Include how to fix |
| 3.3.4 Error Prevention | AA | Reversible/confirmable for legal, financial | Warn before destructive actions |

**Error message formula:**
```
[What's wrong] + [How to fix]
```

---

## Operable guidelines (content-related)

### 2.4 Navigable

| Guideline | Level | Requirement | Content action |
|-----------|-------|-------------|----------------|
| 2.4.2 Page Titled | A | Descriptive page titles | Write meaningful titles |
| 2.4.4 Link Purpose (In Context) | A | Link purpose from text or context | Write descriptive links |
| 2.4.6 Headings and Labels | AA | Headings describe topic/purpose | Write descriptive headings |
| 2.4.9 Link Purpose (Link Only) | AAA | Link purpose from link text alone | Avoid "click here" |
| 2.4.10 Section Headings | AAA | Section headings organize content | Use logical heading hierarchy |

**Link text rules:**
- Describe destination, not mechanics
- Avoid: "Click here", "Learn more", "Read more"
- Good: "View pricing", "Download annual report (PDF)"

---

## Robust guidelines (content-related)

### 4.1 Compatible

| Guideline | Level | Requirement | Content action |
|-----------|-------|-------------|----------------|
| 4.1.2 Name, Role, Value | A | Accessible name for UI components | Label all interactive elements |
| 4.1.3 Status Messages | AA | Status announced without focus | Write clear status messages |

**Accessible names:**
- Every button, link, form field needs a name
- Name should describe the action or purpose
- Icon-only buttons need aria-label

---

## Conformance levels

### Level A (Minimum)
Must comply. Failure creates significant barriers.

**Content requirements:**
- Alt text for informative images
- Visible labels for form fields
- Error messages identify the issue
- No color-only information
- Descriptive page titles

### Level AA (Target standard)
Recommended baseline. Most regulations require this.

**Additional content requirements:**
- Error suggestions when format known
- Consistent identification across site
- Descriptive headings and labels
- Text alternatives for images of text

### Level AAA (Enhanced)
Aspirational for maximum accessibility.

**Additional content requirements:**
- Reading level: lower secondary education
- All abbreviations expanded
- All unusual words defined
- Links meaningful without context
- Sign language for audio (where applicable)

---

## Quick reference by content type

### Images
| Content type | WCAG | Action |
|--------------|------|--------|
| Photo (informative) | 1.1.1 | Descriptive alt text |
| Icon (functional) | 1.1.1 | Alt describes action |
| Decorative | 1.1.1 | alt="" |
| Chart/graph | 1.1.1 | Alt + long description |
| Logo | 1.1.1 | Company name as alt |

### Text
| Content type | WCAG | Action |
|--------------|------|--------|
| Headings | 1.3.1, 2.4.6 | Logical hierarchy, descriptive |
| Links | 2.4.4, 2.4.9 | Meaningful text |
| Labels | 3.3.2 | Visible, associated |
| Errors | 3.3.1, 3.3.3 | Identify + suggest fix |
| Instructions | 1.3.3 | Don't rely on sensory |

### Interactive
| Content type | WCAG | Action |
|--------------|------|--------|
| Buttons | 4.1.2 | Action + object label |
| Forms | 3.3.2 | Visible labels |
| Status | 4.1.3 | Announce changes |
| Modals | 2.4.2 | Descriptive title |
