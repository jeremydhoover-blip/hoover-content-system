# Writing Accessible UI Copy

Write inclusive, accessible content that works for all users regardless of ability, assistive technology, or context of use.

---

## Table of contents
- [Core principles](#core-principles)
- [When to apply](#when-to-apply)
- [Key techniques](#key-techniques)
- [Inputs required](#inputs-required)
- [Quality criteria](#quality-criteria)

---

## Core principles

### 1. Content must be perceivable
All users must be able to access information regardless of sensory ability. Text alternatives, clear structure, and sufficient contrast matter.

### 2. Content must be understandable
Use plain language, consistent terminology, and predictable patterns. Complexity excludes users with cognitive disabilities.

### 3. Content must support assistive technology
Screen readers, voice control, and other assistive tools rely on properly structured, labeled content.

### 4. Content must work in any context
Users may have situational disabilities (bright sunlight, noisy environment, one-handed use). Accessible content is resilient content.

---

## When to apply

| Scenario | Accessibility focus |
|----------|---------------------|
| Images and icons | Alt text, decorative vs. informative |
| Interactive elements | Button labels, link text, form labels |
| Dynamic content | Status announcements, live regions |
| Navigation | Headings, landmarks, skip links |
| Data visualization | Text alternatives, patterns not just color |
| Errors and validation | Clear identification, programmatic association |
| Time-based content | Captions, transcripts, pause controls |

---

## Key techniques

### Alt text
```yaml
image:
  type: "informative"
  alt: "[What it shows and why it matters]"
  # Not: "image of..." or filename

image:
  type: "decorative"
  alt: ""
  # Empty alt for purely decorative images
```

### Button and link labels
```yaml
# Accessible
button: "Save draft"
link: "View pricing plans"

# Inaccessible
button: "Click here"
link: "Learn more"  # Without context
```

### Form labels
```yaml
field:
  label: "Email address"
  # Visible, programmatically associated
  help_text: "We'll send confirmation here"
  error: "Enter a valid email address"
  # Error associated with field via aria-describedby
```

### Headings
```yaml
structure:
  h1: "Account settings"  # One per page
  h2: "Profile"           # Major sections
  h3: "Display name"      # Subsections
  # No skipping levels (h1 → h3)
```

### Status announcements
```yaml
status:
  message: "3 items added to cart"
  aria_live: "polite"
  # Announced to screen readers without focus change
```

---

## Inputs required

| Input | Purpose | Required? |
|-------|---------|-----------|
| UI component | What element needs copy | Yes |
| Visual context | What sighted users see | Yes |
| User task | What user is trying to do | Yes |
| Assistive tech context | Screen reader, voice, etc. | Recommended |
| WCAG level target | A, AA, or AAA | Recommended |

---

## Quality criteria

### Must have
- [ ] All images have appropriate alt text (informative or empty)
- [ ] Interactive elements have descriptive labels
- [ ] Headings follow logical hierarchy
- [ ] Link text is meaningful out of context
- [ ] Form fields have visible, associated labels
- [ ] Errors identify the field and explain the fix
- [ ] No information conveyed by color alone

### Should have
- [ ] Reading level appropriate for audience (aim for grade 8)
- [ ] Consistent terminology throughout
- [ ] Status changes announced to assistive tech
- [ ] Time-based content has text alternatives
- [ ] Complex images have extended descriptions

### Avoid
- [ ] "Click here" or "Learn more" without context
- [ ] "Image of..." in alt text
- [ ] Placeholder text as only label
- [ ] ALL CAPS for emphasis
- [ ] Directional instructions ("click the button on the left")
- [ ] Relying on sensory characteristics alone

---

## WCAG alignment

| Guideline | Requirement | Copy implication |
|-----------|-------------|------------------|
| 1.1.1 Non-text Content | Text alternatives | Alt text for images |
| 1.3.1 Info and Relationships | Programmatic structure | Proper headings, labels |
| 2.4.4 Link Purpose | Clear link text | Descriptive links |
| 2.4.6 Headings and Labels | Descriptive headings | Meaningful hierarchy |
| 3.1.5 Reading Level | Lower secondary level | Plain language |
| 3.3.2 Labels or Instructions | Input labels | Visible form labels |
| 3.3.3 Error Suggestion | Error guidance | Actionable error copy |
| 4.1.2 Name, Role, Value | Accessible names | Button/control labels |

---

## Related skills
- [Writing error messages](../writing-error-messages/SKILL.md)
- [Writing form labels and help text](../writing-form-labels-and-helptext/SKILL.md)
- [Reducing cognitive load](../../content-design/reducing-cognitive-load/SKILL.md)
