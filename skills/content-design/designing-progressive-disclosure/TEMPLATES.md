# Templates

## Content layering map
Use this structure to categorize content:

```md
## Progressive disclosure map: [Screen/feature name]

**User task**: [Primary goal]
**User context**: [Expertise level, frequency, stress]

### Layer 1: Essential (always visible)
Content users need immediately to complete primary task.

| Content | Why essential | Visibility |
|---------|---------------|------------|
| [Item] | [Rationale] | Always visible |

### Layer 2: Supplementary (on-demand)
Content that helps but isn't required for task completion.

| Content | Trigger | Reveal mechanism | Discoverability signal |
|---------|---------|------------------|------------------------|
| [Item] | [User action/state] | [Expand/Tooltip/Link] | [How user knows it exists] |

### Layer 3: Edge-case (conditional)
Content for unusual situations or advanced users.

| Content | Trigger condition | Reveal mechanism | Who needs this |
|---------|-------------------|------------------|----------------|
| [Item] | [State/role/flag] | [Link/Section/Modal] | [User segment] |

### Hidden content discoverability audit
- [ ] Users can tell more content exists
- [ ] Reveal triggers are clear (not mystery meat navigation)
- [ ] Essential content never hidden behind interaction
```

## Reveal mechanism specification
Use for each revealed content block:

```md
## Reveal: [Content being revealed]

**Layer**: [Supplementary / Edge-case]
**Trigger**: [Click / Hover / Scroll / State change / User type]

**Mechanism**: [Expand in place / Tooltip / Modal / Drawer / New screen / Accordion]

**Content revealed**:
```
[Exact content that appears]
```

**Discoverability signal**:
- Before reveal: [What user sees that indicates more exists]
- Example: "Learn more" link, "▼" expand icon, "..." overflow menu

**Reverse action**: [How to collapse/dismiss: Click again / Click outside / X button / Auto-dismiss]

**State persistence**: [Does revealed state persist? Across sessions? Per device?]
```

## Disclosure pattern library
Standard patterns for common scenarios:

```md
## Pattern: Form field help text

**When to use**: Additional guidance for form fields that most users don't need.

**Structure**:
- Essential: Field label + field
- Revealed: Help text explaining format or constraints

**Trigger**: Click/tap help icon (?) or focus field
**Mechanism**: Inline expand below field
**Discoverability**: Help icon visible next to label

**Example**:
- Default: `Password [________] (?)`
- Revealed: `Password [________]`
  `Must be 8+ characters with one number`

---

## Pattern: Advanced settings

**When to use**: Settings most users never change.

**Structure**:
- Essential: Common settings
- Revealed: Power-user settings

**Trigger**: Click "Advanced" or "Show more options"
**Mechanism**: Accordion expand or navigate to sub-screen
**Discoverability**: "Advanced" link at bottom of settings group

---

## Pattern: Error details

**When to use**: Technical details for debugging that most users don't need.

**Structure**:
- Essential: Human-readable error + recovery action
- Revealed: Technical details, error codes, stack trace

**Trigger**: Click "Show details" or "Technical info"
**Mechanism**: Accordion expand
**Discoverability**: "Show details" link after error message
```
