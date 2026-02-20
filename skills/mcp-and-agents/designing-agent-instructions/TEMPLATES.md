# Templates

## Default output: Agent instruction set

Use this as the default structure:

```md
# Agent: <Agent Name>

## Purpose
<One sentence: What this agent does and why it exists.>

## Core behaviors

### MUST do
- <Required behavior 1>
- <Required behavior 2>
- <Required behavior 3>

### MUST NOT do
- <Prohibited behavior 1>
- <Prohibited behavior 2>
- <Prohibited behavior 3>

## Decision authority

### Can decide autonomously
- <Decision type 1>
- <Decision type 2>

### Must ask user first
- <Decision type requiring confirmation>
- <Irreversible action>

## Output format
<Specify how the agent should structure responses.>

## Error handling
When encountering errors:
1. <First response>
2. <If that fails>
3. <Escalation path>

## Constraints
- <Resource limit>
- <Scope boundary>
- <Time constraint>
```

## Variant: Task-specific agent

```md
# Agent: <Task> Handler

## Task scope
This agent handles: <specific task type>
This agent does NOT handle: <out-of-scope items>

## Input requirements
Before proceeding, verify:
- [ ] <Required input 1>
- [ ] <Required input 2>

If any are missing, ask the user for them specifically.

## Process
1. <Step 1>
2. <Step 2>
3. <Step 3>
4. Verify result against <criteria>

## Success criteria
The task is complete when:
- <Criterion 1>
- <Criterion 2>

## Failure recovery
If the task fails:
- <Recovery action>
- Report to user with: <specific information to include>
```

## Variant: Multi-capability agent

```md
# Agent: <Multi-purpose Agent>

## Capabilities

### Capability A: <Name>
**Trigger**: When user asks about <topic>
**Behavior**: <What to do>
**Constraints**: <Limits>

### Capability B: <Name>
**Trigger**: When user wants to <action>
**Behavior**: <What to do>
**Constraints**: <Limits>

## Capability selection
When requests are ambiguous:
1. Ask clarifying question
2. Default to <safest interpretation>

## Cross-capability rules
- <Rule that applies across all capabilities>
- <Another universal rule>
```

## Variant: Safety-critical agent

```md
# Agent: <Safety-Critical Agent>

## Purpose
<Purpose statement>

## Safety constraints (non-negotiable)
These rules override all other instructions:
1. <Safety rule 1>
2. <Safety rule 2>
3. <Safety rule 3>

## Allowed actions
Explicitly allowed:
- <Action 1>
- <Action 2>

## Prohibited actions
Never do these under any circumstances:
- <Prohibited action 1>
- <Prohibited action 2>

## Ambiguity resolution
When unsure whether an action is allowed:
1. Default to NOT taking the action
2. Ask the user for clarification
3. Log the ambiguity for review

## Incident response
If a safety boundary is approached:
1. <Immediate action>
2. <Notification>
3. <Logging>
```
