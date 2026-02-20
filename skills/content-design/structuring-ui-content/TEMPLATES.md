# Templates

## Content structure map
Use this to document content organization:

```md
## Screen: [Screen name]

**Primary task**: [What users accomplish here]
**Entry point**: [How users arrive—nav, link, redirect]
**Exit point**: [Primary action | Back | Close]

### Content hierarchy

| Priority | Element | Purpose | Position |
|----------|---------|---------|----------|
| 1 | [Primary action] | [Task completion] | [Above fold, prominent] |
| 2 | [Key information] | [Decision support] | [Above fold] |
| 3 | [Supporting details] | [Context] | [Below fold or expandable] |
| 4 | [Secondary actions] | [Alternative paths] | [Less prominent] |

### Content groups

**Group 1: [Name]**
- [Element]
- [Element]
- [Relationship: why these belong together]

**Group 2: [Name]**
- [Element]
- [Element]
- [Relationship]

### Reading order
1. [First element users should see]
2. [Second element]
3. [...]
n. [Final action]

**Accessibility note**: [DOM order matches visual order: Yes/No. If no, explain.]
```

## Screen type patterns
Use these established patterns as defaults:

```md
## Pattern: Form screen

**Structure**:
1. Title (what user is doing)
2. Form fields (in task sequence)
3. Help text (inline, per field)
4. Validation feedback (inline, per field)
5. Primary action (Submit/Save)
6. Secondary action (Cancel)

**Rules**:
- Primary action right-aligned or full-width on mobile
- Don't interrupt field sequence with unrelated content
- Group related fields (e.g., address fields together)
- Place optional fields after required fields

---

## Pattern: Confirmation screen

**Structure**:
1. Status indicator (success/error icon)
2. Headline (what happened)
3. Supporting details (transaction ID, summary)
4. Primary next action
5. Secondary actions (if applicable)

**Rules**:
- Headline states outcome, not action taken ("Payment complete" not "You clicked submit")
- Include reference info users might need later
- Primary action moves user forward, not backward

---

## Pattern: Settings screen

**Structure**:
1. Section title
2. Setting label + current state
3. Setting description (if needed)
4. Control (toggle, dropdown, etc.)
5. [Repeat for each setting]
6. Save action (if not auto-save)

**Rules**:
- Group settings by category
- Show current state without requiring interaction
- Destructive settings at bottom with visual differentiation
```

## Content flow diagram
Use for complex multi-step flows:

```md
## Flow: [Flow name]

### Step sequence

```
[Step 1 screen] → [Step 2 screen] → [Step 3 screen] → [Confirmation]
       ↓                                    ↓
   [Error state]                     [Error state]
```

### Content per step

| Step | Screen | Primary content | Primary action | Exit options |
|------|--------|-----------------|----------------|--------------|
| 1 | [Name] | [What's shown] | [Action label] | [Back, Cancel] |
| 2 | [Name] | [What's shown] | [Action label] | [Back, Cancel] |

### State handling
- **Incomplete data**: [How handled]
- **Error recovery**: [How handled]
- **Abandonment**: [How handled]
```
