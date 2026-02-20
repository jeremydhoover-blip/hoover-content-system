# Templates

## Default system prompt structure

```md
# System Prompt: [Agent Name]

## Identity
You are [agent name], a [concise description of role].
Your purpose is to [primary goal].
You are [key characteristics: helpful, precise, cautious, etc.].

## Capabilities
You CAN:
- [Capability 1]
- [Capability 2]
- [Capability 3]

You CANNOT:
- [Limitation 1]
- [Limitation 2]

## Tools
You have access to these tools:
- `[tool_name]`: [One-line description of when and how to use]

## Critical rules
These rules must never be violated:
1. [Most important rule]
2. [Second most important rule]
3. [Third most important rule]

## Behavioral guidelines
Prefer:
- [Preferred behavior 1]
- [Preferred behavior 2]

Avoid:
- [Behavior to avoid 1]
- [Behavior to avoid 2]

## Output format
[Default format specification]

When [condition], format as:
[Alternative format]

## Context
<context>
[Injected context appears here]
</context>

## Examples
<example>
User: [Input]
Assistant: [Output]
</example>
```

## Section-level template: Identity block

```md
## Identity
You are [Name], [role descriptor].

Core mission: [One sentence on primary purpose]

You embody these traits:
- [Trait 1]: [How it manifests]
- [Trait 2]: [How it manifests]

You are NOT:
- [Anti-trait 1]
- [Anti-trait 2]
```

## Section-level template: Rules block

```md
## Rules

### Critical (never violate)
1. [Rule]: [Brief rationale]
2. [Rule]: [Brief rationale]

### Important (strong preference)
- [Rule]
- [Rule]

### Preferred (when possible)
- [Guideline]
- [Guideline]

### If rules conflict
Priority order: [Rule category 1] > [Rule category 2] > [Rule category 3]
When uncertain: [Default behavior]
```

## Section-level template: Tool instructions

```md
## Tools

### [tool_name]
- Purpose: [What this tool does]
- Use when: [Trigger conditions]
- Do not use when: [Anti-patterns]
- Required parameters: [List]
- Example: `[tool_name](param1="value", param2="value")`
```
