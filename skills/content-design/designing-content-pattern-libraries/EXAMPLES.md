# Examples

## Example 1: Error message pattern

**Input**: Create a content pattern for validation error messages.

**Output**:
```md
## Pattern: Validation Error

**Use when**: User input fails format, range, or requirement validation
**Content type**: Error

### Structure
```
[What's wrong]. [How to fix].
```

### Elements

| Element | Required | Constraints | Notes |
|---------|----------|-------------|-------|
| Problem statement | Yes | Max 40 chars | State the specific issue |
| Fix instruction | Yes | Max 40 chars | Actionable, specific |
| Field reference | No | — | Only if error appears away from field |

### Rules
1. **State the specific problem**: "Email format invalid" not "Invalid input"
2. **Provide actionable fix**: Tell user exactly what to do
3. **No apologies or blame**: Neutral tone, no "Oops" or "You entered"
4. **No exclamation marks**: Keep tone calm

### Variation boundaries
- **Fixed**: Two-part structure (problem + fix)
- **Flexible**: Word choice for problem description, phrasing of fix instruction

### Examples

**Correct**:
- "Enter a valid email. Check for typos." — Specific problem, specific action
- "Password too short. Use 8 or more characters." — Measurable, actionable
- "Phone number required. Enter your number." — Clear requirement, clear action

**Incorrect**:
- "Invalid email" — Missing fix instruction
- "Please enter a valid email address" — No specific fix
- "Oops! That doesn't look like an email." — Unprofessional tone, vague
- "Error in field" — Not specific to actual problem

### Edge cases
- **Multiple validation failures**: Show one error at a time, starting with first field
- **Server-side validation**: Same pattern applies; don't expose technical details
```

---

## Example 2: Confirmation dialog pattern

**Input**: Create a pattern for destructive action confirmations.

**Output**:
```md
## Pattern: Destructive Action Confirmation

**Use when**: User initiates irreversible action (delete, remove permanently, cancel subscription)
**Content type**: Confirmation

### Structure
```
[Title: Action + Object]

[Consequence statement]

[Primary button: Destructive action verb]  [Secondary button: Cancel]
```

### Elements

| Element | Required | Constraints | Notes |
|---------|----------|-------------|-------|
| Title | Yes | Max 50 chars | "[Verb] [object]?" format |
| Consequence | Yes | Max 100 chars | What happens, especially if irreversible |
| Primary action | Yes | Max 20 chars | Matches title verb |
| Secondary action | Yes | Max 15 chars | Always "Cancel" |

### Rules
1. **Title is a question**: "Delete this project?" not "Delete project"
2. **State consequence explicitly**: "This can't be undone" or specific loss
3. **Primary button matches title verb**: If title says "Delete", button says "Delete"
4. **Destructive button is not default focus**: Prevent accidental confirmation
5. **No double negatives**: "Cancel" cancels the dialog, not the action

### Variation boundaries
- **Fixed**: Question title, consequence, matching button verb, Cancel as secondary
- **Flexible**: Specific consequence phrasing based on what's lost

### Examples

**Correct**:
- Title: "Delete this project?"
  Body: "All files and history will be permanently removed."
  Buttons: [Delete] [Cancel]
  — Clear action, specific consequence, matching verb

- Title: "Remove team member?"
  Body: "Alex will lose access immediately. You can re-invite them later."
  Buttons: [Remove] [Cancel]
  — Reversibility noted, specific consequence

**Incorrect**:
- Title: "Are you sure?"
  Body: "This action cannot be undone."
  Buttons: [Yes] [No]
  — Vague title, generic buttons

- Title: "Delete project"
  Body: "Click OK to continue"
  Buttons: [OK] [Cancel]
  — Not a question, "OK" doesn't describe action

- Title: "Warning"
  Body: "You are about to delete this project permanently."
  Buttons: [Confirm] [Go back]
  — "Warning" is not actionable, "Confirm" doesn't match action

### Edge cases
- **Batch deletion**: "Delete 5 projects?" with list of affected items
- **Soft delete with recovery**: Note recovery option in consequence: "You can restore this within 30 days."
```

---

## Example 3: Pattern library overview

**Input**: Create the overview structure for a content pattern library.

**Output**:
```md
# Content Pattern Library

## Purpose
Enable consistent, high-quality UI content across product teams. This library provides reusable patterns that can be applied mechanically, reducing inconsistency and review cycles.

## How to use this library
1. Identify what content you need (error, confirmation, empty state, etc.)
2. Find the matching pattern using the index or decision tree
3. Apply the structure exactly—fill in placeholders with your specifics
4. Compare your draft to correct/incorrect examples
5. Verify you're within variation boundaries
6. If edge case, check edge case handling or escalate

## Pattern index

| Pattern | Content type | Use when |
|---------|--------------|----------|
| Validation Error | Error | User input fails validation |
| System Error | Error | Backend/service failure |
| Destructive Confirmation | Confirmation | Irreversible action |
| Non-destructive Confirmation | Confirmation | Reversible action |
| Success Toast | Feedback | Action completed |
| Empty State | Instruction | No content to display |
| Permission Request | Instruction | Requesting access/capability |
| Loading State | Status | Operation in progress |

## Global rules
These apply to all patterns in this library:
1. Sentence case for all UI text (capitalize first word only)
2. No periods on buttons, labels, or headlines
3. No exclamation marks except celebratory success states
4. Maximum one sentence per UI element (except body text)
5. Action buttons use verbs ("Save") not nouns ("Submission")

## Decision tree: Error messages

```
Error occurred →
├── Input validation failed?
│   ├── Yes → Validation Error pattern
│   └── No → Continue
├── User lacks permission?
│   ├── Yes → Permission Error pattern
│   └── No → Continue
├── Network/server issue?
│   ├── Yes → System Error pattern
│   └── No → Continue
└── Unknown → System Error pattern (generic)
```
```

---

## Example 4: Edge case — Conflicting patterns

**Input**: User needs confirmation message but action is both destructive AND reversible (soft delete with 30-day recovery).

**Output**:
```md
## Edge case: Destructive action with recovery option

**Situation**: Action seems destructive (delete) but has recovery window (soft delete).

**Pattern conflict**: 
- Destructive Confirmation pattern: Emphasizes irreversibility
- Non-destructive Confirmation pattern: Downplays consequence

**Resolution**: Use Destructive Confirmation pattern with modified consequence.

### Application

**Structure** (from Destructive Confirmation):
```
[Title: Action + Object]

[Consequence statement — modified to note recovery]

[Primary button: Destructive verb]  [Secondary button: Cancel]
```

**Example**:
- Title: "Delete this project?"
- Body: "This project will be moved to Trash. You can restore it within 30 days."
- Buttons: [Delete] [Cancel]

**Rationale**: 
- Title and button maintain "delete" framing—user's mental model
- Consequence reduces anxiety by noting recovery option
- Still uses destructive pattern structure for safety

**When to use each**:
| Scenario | Pattern |
|----------|---------|
| Permanent delete (no recovery) | Destructive Confirmation |
| Soft delete (30-day Trash) | Destructive Confirmation + recovery note |
| Archive (always recoverable, no urgency) | Non-destructive Confirmation |
```

---

## Example 5: Edge case — Missing context

**Input**: "Create patterns for our product."

**Output**:
```md
To design content patterns, I need:

1. **Which content types need patterns?**
   - [ ] Error messages
   - [ ] Confirmation dialogs
   - [ ] Success feedback
   - [ ] Empty states
   - [ ] Form instructions
   - [ ] Notifications
   - [ ] Other: [specify]

2. **Existing examples**
   Share 3-5 examples of current content (good and bad) for each type

3. **Voice and tone parameters**
   - [ ] Existing guidelines (share link)
   - [ ] None yet (I'll recommend defaults)

4. **Constraints**
   - Character limits?
   - Localization requirements?
   - Platform-specific rules?

5. **Who will use this library?**
   - [ ] Writers only
   - [ ] Designers
   - [ ] Developers
   - [ ] AI/automation

I can create a starter pattern library with common patterns (errors, confirmations, empty states) using industry defaults if you prefer to start quickly.
```
