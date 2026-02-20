# Constraint Taxonomy

## Table of contents
- [Constraint categories](#constraint-categories)
- [Severity levels](#severity-levels)
- [Common constraint patterns](#common-constraint-patterns)
- [Anti-patterns](#anti-patterns)

---

## Constraint categories

### Data constraints
Control what information the agent can access, process, or output.

| Type | Description | Example |
|------|-------------|---------|
| Access restriction | Limits which data sources agent can read | "Do not access files in `/secrets/`" |
| Output filtering | Prevents certain data from appearing in responses | "Never include API keys in output" |
| Retention limits | Controls what the agent remembers across sessions | "Do not store PII beyond current session" |
| Transformation rules | Specifies required data handling | "Mask all but last 4 digits of card numbers" |

### Action constraints
Control what operations the agent can perform.

| Type | Description | Example |
|------|-------------|---------|
| Prohibition | Absolute block on an action | "Never delete production data" |
| Conditional gate | Action allowed only under specific conditions | "File writes require user confirmation" |
| Rate limit | Caps frequency or volume of actions | "Maximum 10 API calls per minute" |
| Scope limit | Restricts action to specific contexts | "Edits allowed only in `/user-content/`" |

### Scope constraints
Define the boundaries of agent operation.

| Type | Description | Example |
|------|-------------|---------|
| Domain boundary | Topics/areas agent will address | "Answers coding questions only" |
| Capability boundary | What the agent claims it can do | "Cannot access external websites" |
| Authority boundary | Decisions agent can make autonomously | "Cannot approve expenses over $100" |
| Temporal boundary | Time-based restrictions | "Operates during business hours only" |

### Communication constraints
Control how the agent interacts with users.

| Type | Description | Example |
|------|-------------|---------|
| Tone restriction | Required communication style | "Do not use sarcasm" |
| Disclosure rules | What must be stated to users | "Always identify as AI assistant" |
| Promise limits | What the agent can commit to | "Do not guarantee delivery dates" |
| Escalation triggers | When to involve humans | "Route complaints to human after 2 failed resolutions" |

---

## Severity levels

### Hard constraints (must never violate)
- Violations cause immediate action block
- No exception mechanism
- Examples: Security violations, legal compliance, safety-critical actions

### Soft constraints (prefer not to violate)
- Violations trigger escalation or confirmation
- May be overridden with appropriate approval
- Examples: Style preferences, efficiency guidelines, default behaviors

### Advisory constraints (should consider)
- Violations logged but not blocked
- Used for training and improvement
- Examples: Best practices, optimization suggestions

---

## Common constraint patterns

### The blocklist pattern
```
Never: [specific action/output]
Detection: [pattern or trigger]
Response: [block/alert/log]
```

### The allowlist pattern
```
Only: [permitted actions/sources]
Everything else: [deny by default]
Exception: [approval mechanism if any]
```

### The escalation pattern
```
When: [condition]
Action: [pause/confirm/route]
Resume: [approval criteria]
Timeout: [behavior if no response]
```

### The threshold pattern
```
Limit: [quantity] per [time period]
Exceeded: [action when limit hit]
Reset: [when counter resets]
```

### The context-dependent pattern
```
If [context A]: [constraint X applies]
If [context B]: [constraint Y applies]
Default: [fallback constraint]
```

---

## Anti-patterns

### Vague constraint
❌ "Be careful with sensitive data"
✅ "Do not include SSN, credit card numbers, or passwords in any output"

### Conflicting constraints
❌ "Always be helpful" + "Never provide medical information"
✅ "For medical questions, state 'I cannot provide medical advice' and suggest consulting a healthcare provider"

### Unenforceable constraint
❌ "Ensure all responses are accurate"
✅ "Cite source documents for factual claims; state 'I cannot verify this' when operating without sources"

### Missing boundary
❌ "Help users with their requests"
✅ "Help users with [specific domain] requests; for out-of-scope requests, state scope and suggest alternatives"

### Infinite escalation
❌ "If unsure, ask for clarification" (loops forever)
✅ "If unsure after 2 clarifying questions, state limitations and offer to escalate to human"
