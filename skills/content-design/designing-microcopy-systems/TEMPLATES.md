# Templates

## Component copy specification
Use this structure for each component type:

```md
## [Component name]

**Function**: [Action | Feedback | Navigation | Instruction | Status]

### Copy slots

| Slot | Required | Max chars | Pattern |
|------|----------|-----------|---------|
| [Label] | [Yes/No] | [count] | [structure rule] |
| [Helper text] | [Yes/No] | [count] | [structure rule] |
| [Error] | [Yes/No] | [count] | [structure rule] |
| [Success] | [Yes/No] | [count] | [structure rule] |

### Pattern rules
- **Label**: [Verb phrase | Noun phrase | Question]. [Additional constraints].
- **Helper text**: [When to include]. [What to avoid].
- **Error**: [Structure: What went wrong + How to fix]. [Tone: Neutral, not apologetic].
- **Success**: [Structure: Confirmation + Next action if applicable].

### Variation rules
- **Allowed**: [What can change]
- **Not allowed**: [What must stay consistent]

### Examples

**Correct**:
- Label: "[example]"
- Helper: "[example]"
- Error: "[example]"

**Incorrect**:
- Label: "[bad example]" — [why it fails]
```

## Microcopy system overview
Use this as the top-level document structure:

```md
# Microcopy System

## Principles
1. [Principle 1: e.g., "Actions describe outcomes, not mechanics"]
2. [Principle 2]
3. [Principle 3]

## Component inventory

| Component | Function | Copy slots | Documented |
|-----------|----------|------------|------------|
| [Button] | Action | Label | ✓ |
| [Form field] | Instruction | Label, Helper, Error | ✓ |
| [Toast] | Feedback | Message, Action | ✓ |

## Global constraints
- **Character limits**: [Platform-specific limits]
- **Localization**: [Expansion factor, avoid idioms]
- **Accessibility**: [Screen reader considerations]

## Components
[Link to each component specification]
```

## Pattern definition format
Use for documenting recurring patterns:

```md
## [Pattern name]: [e.g., "Error message structure"]

**Use when**: [Trigger condition]

**Structure**:
```
[What happened]. [How to fix].
```

**Constraints**:
- Max length: [count] characters
- Tone: [Neutral | Reassuring | Urgent]
- Must include: [required element]
- Must not include: [prohibited element]

**Examples**:
- ✓ "Password must be at least 8 characters. Add more characters."
- ✗ "Invalid password" — [Missing how to fix]
- ✗ "Oops! Something went wrong with your password." — [Unnecessarily cute, vague]
```
