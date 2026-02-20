# Templates

## Default guardrail specification

```md
# Guardrails: [Agent Name]

## Scope definition
This agent operates within: [bounded capability description]
This agent does NOT: [explicit exclusions]

## Hard constraints
These are absolute prohibitions. The agent must never:
- [Constraint 1]: [Specific prohibited behavior]
- [Constraint 2]: [Specific prohibited behavior]
- [Constraint 3]: [Specific prohibited behavior]

## Soft constraints
These require escalation or confirmation:
- [Constraint]: [Condition] → [Required action before proceeding]
- [Constraint]: [Condition] → [Required action before proceeding]

## Data handling boundaries
- PII: [Specific handling rule]
- Credentials: [Specific handling rule]
- User content: [Specific handling rule]

## Action boundaries
- Irreversible actions: [Confirmation/escalation requirement]
- External calls: [Scope and approval requirements]
- Cost-incurring operations: [Limits and approval thresholds]

## Scope boundaries
- In scope: [Explicit list]
- Out of scope: [Explicit list]
- Ambiguous cases: [Default behavior and escalation path]

## Enforcement
- Detection: [How violations are identified]
- Response: [What happens when constraint is triggered]
- Logging: [What gets recorded]
```

## Constraint statement format

```md
**[CONSTRAINT-ID]**: [Category]
- Trigger: [Condition that activates this constraint]
- Prohibition: [Exact behavior that is blocked]
- Rationale: [Why this constraint exists]
- Exception: [If any, with approval mechanism]
```

## Escalation rule format

```md
**Escalation: [Scenario]**
- Condition: [What triggers escalation]
- Action: [Pause / Ask user / Route to human / Abort]
- Message: "[Exact language to present]"
- Resume: [Conditions under which agent may proceed]
```
