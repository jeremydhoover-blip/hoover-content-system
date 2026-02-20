# Prompt Architecture

## Table of contents
- [Architectural layers](#architectural-layers)
- [Section ordering](#section-ordering)
- [Token budgeting](#token-budgeting)
- [Modularity patterns](#modularity-patterns)

---

## Architectural layers

System prompts operate in layers, with each layer building on the previous:

### Layer 1: Identity foundation
Establishes who the agent is at the most fundamental level.

```
Contents:
- Agent name and role
- Core purpose (1 sentence)
- Key personality traits

Priority: Highest (never truncate)
Typical tokens: 50-150
```

### Layer 2: Capability boundaries
Defines what the agent can and cannot do.

```
Contents:
- Explicit capabilities (CAN)
- Explicit limitations (CANNOT)
- Tool access and usage rules

Priority: Very high
Typical tokens: 100-300
```

### Layer 3: Behavioral rules
Specifies how the agent should behave within its capabilities.

```
Contents:
- Critical rules (must never violate)
- Important guidelines (strong preference)
- Stylistic preferences (when possible)

Priority: High (critical rules never truncated)
Typical tokens: 200-500
```

### Layer 4: Output specification
Defines format and structure of responses.

```
Contents:
- Default output format
- Conditional formats
- Structural requirements

Priority: Medium-high
Typical tokens: 100-300
```

### Layer 5: Dynamic context
Injected per-session or per-request.

```
Contents:
- User profile / preferences
- Retrieved documents
- Conversation history
- Session state

Priority: Variable (depends on relevance)
Typical tokens: Variable
```

### Layer 6: Examples
Demonstrates expected behavior for ambiguous cases.

```
Contents:
- Edge case handling
- Boundary scenarios
- Format demonstrations

Priority: Medium (can trim if needed)
Typical tokens: 200-500
```

---

## Section ordering

Optimal ordering maximizes attention on critical content:

### Recommended order

1. **Identity** — First, establish who this is
2. **Critical rules** — High-stakes constraints early
3. **Capabilities** — What can/cannot do
4. **Tools** — How to use available tools
5. **Behavioral guidelines** — Preferences and style
6. **Output format** — Structural requirements
7. **Context injection point** — Dynamic content
8. **Examples** — Last, as reference material

### Rationale
- Early content gets stronger attention in long contexts
- Critical constraints should not be buried
- Context needs to be near the end to be "fresh"
- Examples are reference material, not primary instruction

### Alternative: Sandwich structure
For very long prompts, critical rules repeated:

```
1. Identity + Critical rules (brief)
2. Full capabilities and guidelines
3. Context
4. Critical rules (reminder)
5. Examples
```

---

## Token budgeting

### Budget allocation by agent type

| Agent type | Identity | Rules | Tools | Format | Context | Examples | Total |
|------------|----------|-------|-------|--------|---------|----------|-------|
| Simple chat | 50 | 150 | 0 | 50 | 500 | 100 | ~850 |
| Customer support | 100 | 300 | 200 | 150 | 2000 | 300 | ~3050 |
| Code assistant | 150 | 400 | 500 | 200 | 8000 | 500 | ~9750 |
| Research agent | 150 | 500 | 300 | 300 | 6000 | 400 | ~7650 |

### Budget principles

1. **Context dominates**: 60-80% of budget typically goes to dynamic context
2. **Static prompt is fixed cost**: Optimize for clarity, not brevity
3. **Examples are optional**: Can be trimmed under pressure
4. **Rules scale with risk**: High-risk agents need more constraint budget

### Compression strategies

When over budget:
1. First: Trim examples (keep 1-2 critical ones)
2. Second: Compress behavioral guidelines (preferences, not rules)
3. Third: Reduce context with better retrieval
4. Never: Remove critical rules or identity

---

## Modularity patterns

### Component-based prompts
Assemble prompts from reusable components:

```
system_prompt = compose(
  identity_block,
  capability_block,
  rules_block,
  tool_block,
  format_block,
  context_slot,
  example_block
)
```

Benefits:
- Reuse across agents
- Version control per component
- A/B test individual sections

### Inheritance pattern
Base agent extended for specific use cases:

```
base_agent:
  - Identity: "You are an assistant for AcmeCorp"
  - Core rules: [shared rules]
  - Tone: professional, helpful

support_agent (extends base_agent):
  - Capability additions: order lookup, returns
  - Additional rules: refund limits
  - Tools: support-specific tools

sales_agent (extends base_agent):
  - Capability additions: pricing, demos
  - Additional rules: no competitor mentions
  - Tools: sales-specific tools
```

### Conditional sections
Include sections based on context:

```
if user.is_premium:
  include(premium_capabilities)
  
if session.has_sensitive_data:
  include(stricter_data_rules)

if request.type == "code":
  include(code_format_block)
```

### Override pattern
Later sections can override earlier ones:

```
# Base rules (general)
- Be helpful and friendly

# Context-specific override
When user mentions legal topics:
- Override: Do not provide advice, redirect to legal team
```
