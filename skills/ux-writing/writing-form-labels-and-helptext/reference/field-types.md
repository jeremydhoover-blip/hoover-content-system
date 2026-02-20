# Field Types and Help Text Rules

Reference for form field labeling and help text patterns.

---

## Table of contents
- [Field types](#field-types)
- [Label rules](#label-rules)
- [Help text patterns](#help-text-patterns)
- [Placeholder rules](#placeholder-rules)
- [Validation message patterns](#validation-message-patterns)

---

## Field types

| Field type | Label pattern | Help text needed? | Placeholder? |
|------------|---------------|-------------------|--------------|
| Text input | Noun phrase | If format specific | Example value |
| Email | "Email" or "Email address" | Rarely | user@example.com |
| Password | "Password" | For requirements | No |
| Number | Noun phrase | If range/format specific | Example |
| Date | Noun phrase | If format specific | Format |
| Select/dropdown | Noun phrase | If options need context | Default text |
| Checkbox | Statement or question | Rarely | N/A |
| Radio group | Question or noun | If options need context | N/A |
| File upload | "Upload [thing]" | For constraints | N/A |
| Textarea | Noun phrase | If format specific | Example |

---

## Label rules

### Format
- Sentence case: "Email address" not "Email Address"
- No colons: "Email" not "Email:"
- No periods
- Max 3 words typical

### Label patterns by type
```yaml
# Text inputs
label: "[Noun]"           # "Name", "Address"
label: "[Adjective] [noun]"  # "Display name", "Street address"

# Checkboxes (actions/agreements)
label: "[Verb] + [object]"   # "Remember me"
label: "I [agreement]"       # "I agree to the terms"

# Radio groups
label: "[Question]?"      # "How did you hear about us?"
label: "[Selection noun]" # "Notification frequency"
```

### Required field indicators
| Pattern | When to use |
|---------|-------------|
| Asterisk (*) | Most forms, explained in legend |
| "(required)" | High-stakes forms |
| "(optional)" | When most fields are required |
| No indicator | When all fields required |

---

## Help text patterns

### When to use help text
- Format requirements: "Use format: MM/DD/YYYY"
- Character limits: "Max 280 characters"
- Context needed: "This will be visible on your profile"
- Consequences: "You can't change this later"

### When NOT to use help text
- Self-explanatory fields (Name, Email)
- To repeat the label
- For basic instructions ("Enter your email")

### Help text placement
| Position | Use for |
|----------|---------|
| Below field | Most help text |
| Above field | Critical context before input |
| Inline (i icon) | Longer explanations |
| Tooltip | Optional, supplementary info |

### Help text patterns
```yaml
# Format requirement
help_text: "Format: [pattern]"
help_text: "Example: [example]"

# Constraint
help_text: "[Min/Max] [count] [unit]"
help_text: "Must include [requirement]"

# Consequence
help_text: "This [will/won't] [consequence]"
help_text: "You can change this in [location]"

# Context
help_text: "Used for [purpose]"
help_text: "Visible to [audience]"
```

### Character constraints
- Max 80 characters
- One sentence
- Fragment OK if clear

---

## Placeholder rules

### Do
- Use realistic examples: "jane.doe@company.com"
- Show format: "MM/DD/YYYY"
- Indicate type: "Search products..."

### Don't
- Repeat label: label "Email" + placeholder "Email"
- Use as help text (disappears on focus)
- Put required info only in placeholder

### Placeholder patterns
| Field type | Placeholder example |
|------------|---------------------|
| Email | "you@example.com" |
| Phone | "(555) 123-4567" |
| URL | "https://example.com" |
| Search | "Search..." |
| Name | "Jane Doe" |
| Date | "MM/DD/YYYY" |

---

## Validation message patterns

### Error message structure
```yaml
error:
  pattern: "[What's wrong]. [How to fix]."
  max_length: 80
```

### Error patterns by type
| Validation | Message pattern | Example |
|------------|-----------------|---------|
| Required | "[Field] is required." | "Email is required." |
| Format | "Enter a valid [field]." | "Enter a valid email address." |
| Too short | "[Field] must be at least [n] characters." | "Password must be at least 8 characters." |
| Too long | "[Field] can't exceed [n] characters." | "Bio can't exceed 280 characters." |
| Invalid char | "[Field] can only contain [allowed]." | "Username can only contain letters and numbers." |
| Mismatch | "[Fields] don't match." | "Passwords don't match." |
| Unavailable | "That [field] is taken. Try another." | "That username is taken. Try another." |

### Success/confirmation
| Context | Pattern |
|---------|---------|
| Real-time valid | ✓ (checkmark only) |
| Availability | "[Value] is available" |
| Strength | "Strong password" |

---

## Accessibility requirements

### Labels
- Every field must have a visible label
- Label must be programmatically associated
- Don't rely only on placeholder

### Help text
- Associate with aria-describedby
- Don't put critical info only in color

### Errors
- Announce to screen readers
- Don't rely only on color
- Focus management on form submission errors

---

## Anti-patterns

| Pattern | Problem | Fix |
|---------|---------|-----|
| Placeholder as label | Disappears, accessibility issue | Use visible label |
| "Please enter..." | Verbose | Just name the field |
| "Invalid input" | No guidance | Explain what's wrong |
| Red text only | Accessibility | Add icon, message |
| Help text for everything | Clutter | Only when needed |
| ALL CAPS labels | Harder to read | Sentence case |
