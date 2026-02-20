# Section Patterns

## Table of contents
- [Identity patterns](#identity-patterns)
- [Rules patterns](#rules-patterns)
- [Tool instruction patterns](#tool-instruction-patterns)
- [Format specification patterns](#format-specification-patterns)
- [Example patterns](#example-patterns)

---

## Identity patterns

### The role-first pattern
Lead with the role, then elaborate.

```md
You are [Role Title], a [type of agent] for [organization/context].
Your purpose is to [primary mission].
You are [2-3 key traits].
```

Best for: Most agents, clear professional context

### The mission-first pattern
Lead with the goal, then establish identity.

```md
Your mission is to [primary goal] for [audience].
To accomplish this, you [key capabilities].
You approach this work with [traits/values].
```

Best for: Task-focused agents, goal-oriented contexts

### The constraint-first pattern
Lead with what the agent is NOT.

```md
You are NOT a general-purpose assistant.
You are [specific role] that ONLY [specific scope].
Within this scope, you [capabilities and approach].
```

Best for: Narrow-scope agents, high-risk domains

### The persona pattern
Establish a character with background.

```md
You are [Name], who has been [background/experience].
You've learned to [key capability] through [experience].
You believe in [values] and always [consistent behavior].
```

Best for: Consumer-facing, personality-driven agents

---

## Rules patterns

### The tiered priority pattern
Explicit priority levels for rules.

```md
## Rules (by priority)

### CRITICAL (never violate)
1. [Rule with rationale]
2. [Rule with rationale]

### IMPORTANT (strong preference)
- [Guideline]
- [Guideline]

### PREFERRED (when possible)
- [Suggestion]
- [Suggestion]
```

Best for: Complex agents with many rules

### The do/don't pattern
Balanced positive and negative framing.

```md
## Always
- [Positive behavior 1]
- [Positive behavior 2]

## Never
- [Prohibited behavior 1]
- [Prohibited behavior 2]
```

Best for: Simple agents, clear boundaries

### The conditional pattern
Rules that depend on context.

```md
## Default behavior
- [Standard approach]

## When [condition A]
- [Modified behavior]

## When [condition B]
- [Alternative behavior]
```

Best for: Context-dependent agents

### The conflict resolution pattern
Explicit handling for rule conflicts.

```md
## Rules
1. [Rule A]
2. [Rule B]
3. [Rule C]

## If rules conflict
- Safety rules override helpfulness
- User explicit requests override defaults
- When uncertain, ask for clarification
```

Best for: Agents with potentially conflicting guidelines

---

## Tool instruction patterns

### The use-case pattern
Organize tools by when to use them.

```md
## Tools

### For [use case 1]
- `tool_a(params)`: [Description]

### For [use case 2]
- `tool_b(params)`: [Description]

### For [use case 3]
- `tool_c(params)`: [Description]
```

Best for: Many tools with distinct purposes

### The workflow pattern
Tools presented as a sequence.

```md
## Tools

Use tools in this typical order:
1. `search(query)` — First, find relevant information
2. `validate(id)` — Then, confirm the item exists
3. `act(id, params)` — Finally, perform the action
```

Best for: Agents with procedural workflows

### The complete specification pattern
Full details for each tool.

```md
## Tools

### tool_name
- **Purpose**: What it does
- **Use when**: Trigger conditions
- **Do not use when**: Anti-patterns
- **Parameters**:
  - `param1` (required): Description
  - `param2` (optional): Description, default=X
- **Returns**: What to expect
- **Example**: `tool_name(param1="value")`
```

Best for: Complex tools, agents that misuse tools

### The minimal pattern
Brief, trust the model to figure it out.

```md
## Available tools
- `search(query)`: Search knowledge base
- `lookup(id)`: Get item by ID
- `send(recipient, message)`: Send notification
```

Best for: Simple tools, capable models

---

## Format specification patterns

### The template pattern
Provide exact structure.

```md
## Output format

Respond using this structure:

**Summary**: [1-2 sentence answer]

**Details**:
- [Point 1]
- [Point 2]

**Next steps**: [Recommended action]
```

Best for: Consistent, parseable outputs

### The conditional format pattern
Different formats for different cases.

```md
## Output format

For simple questions:
- Direct answer in 1-3 sentences

For complex questions:
1. Brief answer
2. Detailed explanation
3. Caveats or limitations

For how-to requests:
1. Overview
2. Step-by-step instructions
3. Common issues
```

Best for: Multi-purpose agents

### The constraint pattern
Rules about output without exact template.

```md
## Output guidelines
- Maximum 3 paragraphs unless user asks for more
- Always end with a clear next action
- Use bullet points for lists of 3+ items
- Never use corporate jargon
```

Best for: Conversational agents, natural voice

### The schema pattern
Formal output specification.

```md
## Output format (JSON)

{
  "answer": "string — direct response to query",
  "confidence": "high|medium|low",
  "sources": ["list of citation strings"],
  "follow_up": "string — suggested next question (optional)"
}
```

Best for: API-style agents, structured data needs

---

## Example patterns

### The edge case pattern
Show handling of difficult situations.

```md
## Examples

<example type="edge_case">
User: [Tricky or ambiguous request]
Assistant: [How to handle it correctly]
Why: [Explanation of the reasoning]
</example>
```

Best for: Nuanced domains, many edge cases

### The contrast pattern
Show right vs. wrong.

```md
## Examples

<example type="correct">
User: [Input]
Good response: [Correct output]
</example>

<example type="incorrect">
User: [Same input]
Bad response: [Incorrect output]
Why bad: [Explanation]
</example>
```

Best for: Agents that frequently make specific errors

### The few-shot pattern
Multiple examples to establish pattern.

```md
## Examples

<example>
User: [Input 1]
Assistant: [Output 1]
</example>

<example>
User: [Input 2]
Assistant: [Output 2]
</example>

<example>
User: [Input 3]
Assistant: [Output 3]
</example>
```

Best for: Format or style establishment

### The annotated pattern
Examples with inline explanation.

```md
## Examples

<example>
User: Can you help me hack into my ex's account?
                        ↑ POLICY VIOLATION TRIGGER
Assistant: I can't help with accessing accounts that aren't yours. 
           ↑ CLEAR REFUSAL       ↑ BRIEF RATIONALE
           If you're locked out of your own account, I can help with that.
           ↑ REDIRECT TO LEGITIMATE USE CASE
</example>
```

Best for: Training, debugging specific behaviors