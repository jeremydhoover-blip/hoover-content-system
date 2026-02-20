# Examples

## Example 1: Button component specification

**Input**: Define microcopy patterns for primary action buttons.

**Output**:
```md
## Button (Primary action)

**Function**: Action

### Copy slots

| Slot | Required | Max chars | Pattern |
|------|----------|-----------|---------|
| Label | Yes | 25 | Verb + object |

### Pattern rules
- **Label**: Start with action verb. Describe the outcome, not the mechanism.
  - Use: "Save changes", "Send message", "Create project"
  - Avoid: "Submit", "OK", "Click here", "Go"
- **Sentence case**: Capitalize first word only.
- **No punctuation**: No periods, exclamation marks.

### Variation rules
- **Allowed**: Verb choice based on action specificity
- **Not allowed**: Noun-only labels, generic verbs ("Do it"), questions

### Examples

**Correct**:
- "Save changes"
- "Send invitation"
- "Delete project"
- "Export as PDF"

**Incorrect**:
- "Submit" — Too generic; doesn't describe outcome
- "Click to save" — Describes mechanism, not outcome
- "SAVE CHANGES" — Wrong case
- "Save." — No punctuation allowed
```

---

## Example 2: Form field error pattern

**Input**: Create an error message pattern for form validation.

**Output**:
```md
## Pattern: Form validation error

**Use when**: User input fails validation rules.

**Structure**:
```
[What's wrong with the input]. [How to fix it].
```

**Constraints**:
- Max length: 80 characters
- Tone: Neutral, instructive
- Must include: Specific fix action
- Must not include: Apologies, blame, exclamation marks

**Examples**:
- ✓ "Email address isn't valid. Check for typos."
- ✓ "Password needs at least 8 characters. Add 3 more."
- ✓ "This field is required. Enter your name."
- ✗ "Invalid email" — Missing how to fix
- ✗ "Oops! That email doesn't look right!" — Overly casual, vague
- ✗ "Please enter a valid email address" — No specific fix guidance
- ✗ "Error: email validation failed" — Technical jargon, no fix
```

---

## Example 3: Toast notification system

**Input**: Define toast microcopy for success, error, and informational states.

**Output**:
```md
## Toast notification

**Function**: Feedback

### Copy slots

| Slot | Required | Max chars | Pattern |
|------|----------|-----------|---------|
| Message | Yes | 60 | [Confirmation/Status]. [Next step if applicable]. |
| Action | No | 15 | Verb or Verb + object |

### Pattern rules by state

**Success toast**:
- Confirm what happened
- Include undo action when applicable
- Example: "Message sent. Undo"

**Error toast**:
- State what failed
- Provide recovery path
- Example: "Couldn't save. Try again"

**Info toast**:
- State the update neutrally
- No action required structure
- Example: "New version available"

### Variation rules
- **Allowed**: Verb choice, specificity of confirmation
- **Not allowed**: Multiple sentences in message slot, apologetic phrasing

### Examples

**Correct**:
- Success: "Project created" | Action: "View"
- Error: "Upload failed. File too large." | Action: "Try again"
- Info: "Autosaved at 3:42 PM"

**Incorrect**:
- "Your project has been successfully created!" — Too long, unnecessary adverb
- "Oops! Something went wrong." — Vague, cutesy
- "Error" — No information content
```

---

## Example 4: Edge case — Missing design system context

**Input**: "Create microcopy patterns for our app."

**Output**:
```md
To create effective microcopy patterns, I need:

1. **Which components need patterns?**
   - [ ] Buttons (primary, secondary, destructive)
   - [ ] Form fields (labels, helpers, errors)
   - [ ] Toasts/notifications
   - [ ] Modals/dialogs
   - [ ] Empty states
   - [ ] All of the above

2. **Platform constraints?**
   - [ ] Mobile (shorter limits)
   - [ ] Desktop (more space)
   - [ ] Both

3. **Existing standards?**
   - [ ] Design system exists (share link)
   - [ ] Voice/tone guidelines exist (share or describe)
   - [ ] Starting from scratch

4. **Localization requirements?**
   - [ ] Single language
   - [ ] Multi-language (which languages?)

I can proceed with common defaults (40-char buttons, 80-char errors, mobile-first) if you prefer speed.
```

---

## Example 5: Component inventory excerpt

**Input**: Create an overview of microcopy coverage for a dashboard product.

**Output**:
```md
# Microcopy System — Dashboard v2.0

## Principles
1. Actions describe outcomes ("Save report") not mechanics ("Click to save")
2. Errors guide recovery, never blame users
3. Every state has copy—loading, empty, error, success
4. Localization-ready: avoid idioms, allow 40% expansion

## Component inventory

| Component | Function | Copy slots | Documented | Notes |
|-----------|----------|------------|------------|-------|
| Button (primary) | Action | Label | ✓ | |
| Button (destructive) | Action | Label | ✓ | Requires confirmation pattern |
| Form field | Instruction | Label, Helper, Error, Success | ✓ | |
| Toast | Feedback | Message, Action | ✓ | |
| Modal (confirmation) | Decision | Title, Body, Primary action, Secondary action | ✓ | |
| Empty state | Instruction | Headline, Description, Action | ✓ | |
| Loading state | Status | Message | ✗ | Needs definition |
| Table | Data display | Column headers, Empty row, Sort labels | ✗ | In progress |

## Global constraints
- **Mobile button labels**: Max 20 characters
- **Desktop button labels**: Max 30 characters
- **Error messages**: Max 80 characters
- **Toast messages**: Max 60 characters
- **Localization expansion**: Reserve 40% additional space
- **Screen readers**: All interactive elements need aria-labels if icon-only
```
