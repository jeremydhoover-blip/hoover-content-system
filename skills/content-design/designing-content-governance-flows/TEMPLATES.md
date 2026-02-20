# Templates

## Governance flow map
Use this structure to document content workflows:

```md
## Governance flow: [Content type]

### Overview
- **Content type**: [What content this governs]
- **Risk level**: [Low / Medium / High / Critical]
- **Typical volume**: [Content pieces per week/month]
- **SLA target**: [Creation to publication time]

### Flow diagram

```
[Creator] → [Review stage 1] → [Review stage 2] → [Approval] → [Publication]
    ↓              ↓                  ↓               ↓
 [Draft]      [Feedback]         [Feedback]      [Approved]
    ↑              ↓                  ↓               ↓
 [Revise] ← [Request changes] ← [Request changes]  [Live]
```

### Stage definitions

| Stage | Owner | Entry criteria | Exit criteria | SLA |
|-------|-------|----------------|---------------|-----|
| Draft | [Role] | [What triggers] | [What's required to advance] | [Time] |
| Review 1 | [Role] | [Requirements] | [Approval conditions] | [Time] |
| Approval | [Role] | [Requirements] | [Final sign-off] | [Time] |
| Publication | [Role] | [Approval confirmed] | [Content live] | [Time] |

### Exception handling
- **Urgent content**: [Expedited path]
- **High-risk content**: [Additional review]
- **Blocked stage**: [Escalation path]
```

## Role definition template
Use for each governance role:

```md
## Role: [Role name]

**Purpose**: [Why this role exists in the flow]
**Capacity**: [How many people, how much time]

### Permissions
| Can do | Cannot do |
|--------|-----------|
| [Action] | [Restriction] |

### Responsibilities
- [Responsibility 1]
- [Responsibility 2]
- [Responsibility 3]

### Accountability
- **Success metric**: [How role performance is measured]
- **Failure consequence**: [What happens when role fails]

### Escalation
- **Escalates to**: [Role] when [condition]
- **Escalated from**: [Role] when [condition]
```

## Review checklist template
Use for structured reviews:

```md
## Review checklist: [Content type]

**Reviewer**: [Role]
**Time budget**: [Max minutes per item]

### Required checks
- [ ] [Check 1]: [What to verify]
- [ ] [Check 2]: [What to verify]
- [ ] [Check 3]: [What to verify]

### Conditional checks (if applicable)
- [ ] [Check]: [When this applies]

### Review outcomes
| Outcome | Criteria | Next step |
|---------|----------|-----------|
| Approved | All required checks pass | Advance to next stage |
| Changes requested | 1+ checks fail, fixable | Return to creator with specifics |
| Rejected | Fundamental issues | Return to creator with rationale |
| Escalated | Reviewer uncertain | Send to [escalation role] |
```

## Governance policy summary
Use as the top-level governance document:

```md
# Content Governance Policy

## Scope
This policy governs: [Content types covered]

## Principles
1. [Principle 1]: [Why it matters]
2. [Principle 2]: [Why it matters]
3. [Principle 3]: [Why it matters]

## Roles
| Role | Scope | Authority |
|------|-------|-----------|
| [Role] | [What they govern] | [What they can decide] |

## Content risk matrix

| Content type | Risk level | Review requirements | Approval authority |
|--------------|------------|---------------------|-------------------|
| [Type] | [Level] | [Who reviews] | [Who approves] |

## Escalation hierarchy
```
[Line reviewer] → [Senior reviewer] → [Content lead] → [Legal/Exec]
```

## SLAs
| Content type | Draft to publish | Expedited path |
|--------------|------------------|----------------|
| [Type] | [Time] | [Available? Criteria?] |
```
