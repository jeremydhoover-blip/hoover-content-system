# Component Copy Slots Reference

Canonical copy slot definitions for UI components. Use this reference when defining microcopy patterns.

---

## Slot taxonomy

Every UI component has defined **slots** where copy can appear. Slots are categorized by function:

| Slot category | Purpose | Examples |
|---------------|---------|----------|
| **Label** | Identifies the element | Button text, field label, tab name |
| **Instruction** | Tells user what to do | Helper text, placeholder, hint |
| **Feedback** | Communicates state/result | Error, success, validation |
| **Status** | Shows current state | Loading, progress, count |
| **Action** | Describes available action | Link text, menu item, CTA |

---

## Component slot definitions

### Button

| Slot | Required | Max chars | Function |
|------|----------|-----------|----------|
| `label` | Yes | 25 | Describes action outcome |

**Constraints**:
- Verb + object format preferred
- Sentence case
- No punctuation

---

### Form field

| Slot | Required | Max chars | Function |
|------|----------|-----------|----------|
| `label` | Yes | 40 | Identifies field purpose |
| `placeholder` | No | 30 | Shows example input format |
| `helper` | No | 80 | Provides additional guidance |
| `error` | Conditional | 80 | Explains validation failure |
| `success` | No | 60 | Confirms valid input |

**Constraints**:
- Label: Noun or noun phrase
- Placeholder: Example data, not instruction
- Helper: Appears below field, not inside
- Error: Problem + fix structure

---

### Toast / Snackbar

| Slot | Required | Max chars | Function |
|------|----------|-----------|----------|
| `message` | Yes | 60 | States what happened |
| `action` | No | 15 | Offers follow-up action |

**Constraints**:
- Message: Single sentence
- Action: Verb or verb phrase
- Auto-dismiss: 4-8 seconds for non-critical

---

### Modal / Dialog

| Slot | Required | Max chars | Function |
|------|----------|-----------|----------|
| `title` | Yes | 50 | Describes modal purpose |
| `body` | No | 200 | Provides context/details |
| `primary_action` | Yes | 20 | Main action button |
| `secondary_action` | No | 15 | Alternative/cancel action |

**Constraints**:
- Title: Question format for confirmations
- Body: Maximum 2-3 sentences
- Primary: Matches title verb for confirmations

---

### Empty state

| Slot | Required | Max chars | Function |
|------|----------|-----------|----------|
| `headline` | Yes | 40 | States the empty condition |
| `description` | No | 100 | Explains why or what to do |
| `action` | Yes | 25 | CTA to resolve empty state |

**Constraints**:
- Headline: Descriptive, not apologetic
- Description: Forward-looking, enables action
- Action: Creates first item or explains how

---

### Tooltip

| Slot | Required | Max chars | Function |
|------|----------|-----------|----------|
| `content` | Yes | 100 | Explains element on hover |

**Constraints**:
- Single paragraph maximum
- No interactions inside tooltip
- Supplementary info only (not critical)

---

### Error banner / Alert

| Slot | Required | Max chars | Function |
|------|----------|-----------|----------|
| `message` | Yes | 150 | Describes problem + resolution |
| `action` | No | 20 | Recovery action |
| `dismiss` | No | — | Close mechanism |

**Constraints**:
- Message: What happened + how to fix
- Dismissible only if non-blocking
- Severity indicated by styling, not copy

---

### Progress indicator

| Slot | Required | Max chars | Function |
|------|----------|-----------|----------|
| `label` | No | 30 | Describes current operation |
| `status` | No | 20 | Shows progress (%, step X of Y) |

**Constraints**:
- Label: Present tense verb phrase
- Status: Numeric or step-based
- Determinate preferred over indeterminate

---

### Navigation item

| Slot | Required | Max chars | Function |
|------|----------|-----------|----------|
| `label` | Yes | 20 | Destination name |
| `badge` | No | 4 | Count or status indicator |

**Constraints**:
- Label: Noun (destination) not verb (action)
- Badge: Number or status abbreviation
- Consistent capitalization across nav

---

### Notification

| Slot | Required | Max chars | Function |
|------|----------|-----------|----------|
| `title` | Yes | 50 | Summary of notification |
| `body` | No | 100 | Details/context |
| `action` | No | 15 | Primary response action |
| `timestamp` | No | — | When event occurred |

**Constraints**:
- Title: Event summary, scannable
- Body: Only if title insufficient
- Action: Opens relevant screen/starts task

---

## Slot interaction rules

### Hierarchy
When multiple slots exist, establish hierarchy:
1. **Label** is scanned first—must stand alone
2. **Helper/Description** supplements label
3. **Error** overrides helper when active
4. **Success** appears after error clears

### Mutual exclusivity
Some slots don't appear together:
- `placeholder` vs `value` (show placeholder only when empty)
- `error` vs `success` (never both simultaneously)
- `helper` may hide when `error` shows (space constraint)

### State-dependent slots
Slots that appear/change based on state:

| State | Visible slots | Hidden slots |
|-------|---------------|--------------|
| Default | label, helper, placeholder | error, success |
| Invalid | label, error | helper, success |
| Valid | label, success (or helper) | error |
| Disabled | label, (helper grayed) | error, success |
| Loading | label, progress indicator | helper |

---

## Platform-specific limits

### Mobile (iOS/Android)
| Slot type | Recommended max |
|-----------|-----------------|
| Button label | 20 chars |
| Toast message | 50 chars |
| Modal title | 40 chars |
| Nav item | 15 chars |

### Desktop (Web)
| Slot type | Recommended max |
|-----------|-----------------|
| Button label | 30 chars |
| Toast message | 80 chars |
| Modal title | 60 chars |
| Nav item | 25 chars |

### Localization buffer
For English source, add 30-40% to max lengths for translation:
- 20 char English → reserve 28 chars for German
- 50 char English → reserve 70 chars for German
