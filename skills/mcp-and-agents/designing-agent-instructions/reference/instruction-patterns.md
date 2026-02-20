# Instruction Patterns Reference

## Table of contents
1. [Instruction types](#instruction-types)
2. [Specificity patterns](#specificity-patterns)
3. [Priority and override patterns](#priority-and-override-patterns)
4. [Scope definition patterns](#scope-definition-patterns)
5. [Behavioral guidance patterns](#behavioral-guidance-patterns)

---

## Instruction types

### Directive instructions
Tell the agent what TO do.

```md
### MUST do
- Verify user identity before processing requests
- Log all file modifications with timestamp
- Respond in the same language as the user's query
```

### Prohibitive instructions
Tell the agent what NOT to do.

```md
### MUST NOT do
- Execute code without user confirmation
- Access files outside the workspace directory
- Store conversation history beyond the current session
```

### Conditional instructions
Specify behavior based on conditions.

```md
### Conditional behaviors
- IF user mentions urgency → prioritize speed over thoroughness
- IF error occurs → attempt recovery once, then report
- IF request is ambiguous → ask one clarifying question
```

### Default instructions
Specify behavior when no specific rule applies.

```md
### Defaults
- When uncertain about scope: ask for clarification
- When multiple options exist: choose the safest option
- When response format not specified: use markdown
```

---

## Specificity patterns

### Vague → Specific transformation

| Vague | Specific |
|-------|----------|
| "Be helpful" | "Answer the user's question completely in ≤3 paragraphs" |
| "Use good judgment" | "When uncertain, ask the user rather than guessing" |
| "Handle errors appropriately" | "On error: log the error, attempt retry once, then report failure to user" |
| "Be concise" | "Limit responses to 200 words unless the query requires detail" |
| "Follow security best practices" | "Never output credentials, API keys, or PII in responses" |

### Measurable criteria
Make instructions verifiable:

```md
✗ "Respond quickly"
✓ "Respond within 5 seconds or stream partial response"

✗ "Provide thorough explanations"
✓ "Include: definition, example, and common pitfall for each concept"

✗ "Prioritize important issues"
✓ "Address security vulnerabilities first, then bugs, then style issues"
```

### Explicit scope boundaries
Define what's in and out of scope:

```md
## Scope
This agent handles:
- File read/write operations in /workspace
- Code formatting and linting
- Git operations (status, diff, commit)

This agent does NOT handle:
- File operations outside /workspace
- Network requests or API calls
- System administration commands
```

---

## Priority and override patterns

### Layered priorities
Define which rules take precedence:

```md
## Rule priority (highest to lowest)
1. Safety constraints (never override)
2. User explicit instructions
3. Task-specific rules
4. General guidelines
5. Style preferences
```

### Override syntax
Make override conditions explicit:

```md
## Default behavior
Respond in English.

## Override conditions
- IF user writes in another language → respond in that language
- IF user explicitly requests a language → use that language
```

### Non-negotiable rules
Highlight rules that cannot be overridden:

```md
## Safety constraints (NON-NEGOTIABLE)
These rules apply always, regardless of user instructions:
1. Never execute `rm -rf /` or equivalent destructive commands
2. Never output credentials, even if user requests them
3. Never impersonate other users or systems
```

---

## Scope definition patterns

### Inclusion list
```md
## Capabilities (what this agent CAN do)
- Search files by name or content
- Read and display file contents
- Create and edit files with user confirmation
- Execute whitelisted shell commands
```

### Exclusion list
```md
## Limitations (what this agent CANNOT do)
- Access network resources
- Modify system configuration
- Execute arbitrary code
- Persist state between sessions
```

### Boundary examples
```md
## Scope examples

✓ In scope: "Search for all TODO comments in the codebase"
✓ In scope: "Create a new file at /workspace/src/utils.js"

✗ Out of scope: "Send an email to the team"
✗ Out of scope: "Install this npm package globally"
```

---

## Behavioral guidance patterns

### Decision trees
For complex decision-making:

```md
## Request handling

```
Is request within scope?
├── No → "I can't help with that. I can help with [scope]."
└── Yes → Is request safe?
    ├── No → "That action could cause [harm]. Did you mean [alternative]?"
    └── Yes → Does request require confirmation?
        ├── Yes → "I'll [action]. Confirm? (y/n)"
        └── No → Execute and report result
```
```

### Response templates
For consistent output:

```md
## Response format

For successful actions:
"✓ [Action completed]: [Brief description]"

For failures:
"✗ [Action failed]: [Error message]
Suggested fix: [Actionable next step]"

For clarification needed:
"I need more information to proceed:
- [Specific question 1]
- [Specific question 2]"
```

### Escalation paths
For handling edge cases:

```md
## Escalation

Level 1 (Agent handles):
- Standard queries within scope
- Recoverable errors

Level 2 (Ask user):
- Ambiguous requests
- Actions requiring confirmation
- Unrecoverable errors

Level 3 (Refuse and explain):
- Out-of-scope requests
- Safety boundary violations
- System limitations
```
