# Rubric

## Pass if all are true
- [ ] Every field has a visible label (not placeholder-only)
- [ ] Label clearly states what to enter
- [ ] Label is ≤40 characters
- [ ] Placeholder (if present) is a format hint, not the label
- [ ] Placeholder is ≤40 characters
- [ ] Help text (if present) adds useful information not in label
- [ ] Help text is ≤100 characters
- [ ] Required/optional status is indicated consistently
- [ ] Validation errors are specific to what's wrong
- [ ] Validation errors are ≤80 characters

## Fail if any are true
- [ ] Field relies on placeholder as only label
- [ ] Label is vague ("Input", "Enter value")
- [ ] Placeholder repeats the label ("Email" placeholder on Email field)
- [ ] Help text repeats label or placeholder
- [ ] Required fields not marked, but some fields are optional
- [ ] Validation error is generic ("Invalid input")
- [ ] Character limits exceeded
- [ ] Label uses unnecessary articles ("The email address")
- [ ] Placeholder shows fake data that looks real ("John Smith")
