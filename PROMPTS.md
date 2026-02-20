# Prompts

Ready-to-use prompts for executing skills. Copy, fill in the brackets, and paste into your AI assistant.

---

## UX Writing

### Error Messages
```
Write an error message for [describe the scenario].

- Error type: [validation / system / network / permission / not-found]
- Severity: [blocking / degraded / informational]
- User was trying to: [action]
- Recovery options: [what user can do next]

Follow the writing-error-messages skill.
```

### Empty States
```
Write an empty state for [feature/screen] when [empty condition].

- User goal: [what they want to accomplish]
- Available actions: [what they can do from here]

Include headline, description, and CTA.
```

### Confirmation Dialogs
```
Write a confirmation dialog for [action, e.g., "deleting a project"].

- Reversible: [yes / no]
- Consequence: [what happens if confirmed]
```

### Onboarding
```
Write onboarding copy for [feature].

Steps:
1. [First step]
2. [Second step]
3. [Third step]

User goal: [what they want to achieve]
```

### Notifications
```
Write a [success / error / warning / info] notification for [event].

- Action needed: [yes / no]
- Max length: [characters, if any]
```

---

## Content Design

### Feature Naming
```
Suggest names for [feature description].

- What it does: [core function]
- User benefit: [why it matters]
- Naming patterns to match: [existing conventions]
```

### Copy Audit
```
Audit this UI copy for style, voice, accessibility, and localization issues:

[paste copy here]
```

### Microcopy System
```
Design microcopy for [feature/flow].

- Components: [buttons, labels, tooltips, helpers]
- States: [default, loading, success, error, empty]
```

---

## Content Strategy

### Voice and Tone
```
Define voice and tone for [product/brand].

- Brand personality: [key attributes]
- Audience: [who uses this]

Include voice attributes, tone by context, and do/don't examples.
```

### Messaging Hierarchy
```
Create messaging hierarchy for [feature/product].

- Primary value: [main benefit]
- Audience: [who this is for]
- Differentiators: [what sets it apart]
```

### Content Brief
```
Write a content brief for [project].

- Objective: [what it should achieve]
- Audience: [who will read it]
- Key messages: [main points]
- Deliverables: [what to produce]
```

---

## Technical Documentation

### How-To Guide
```
Write a how-to guide for [task].

- Goal: [what user wants to accomplish]
- Prerequisites: [what they need first]
- Expected outcome: [what success looks like]
```

### Release Notes
```
Write release notes for [version].

New:
- [Feature 1]
- [Feature 2]

Improved:
- [Improvement 1]

Fixed:
- [Bug fix 1]

Breaking changes: [if any]
```

### API Documentation
```
Document this API endpoint:

- Method: [GET / POST / PUT / DELETE]
- Endpoint: [/path]
- Purpose: [what it does]
- Parameters: [list]
- Response: [format]
- Errors: [possible codes]
```

---

## Developer Content

### CLI Help
```
Write CLI help for [command].

- Purpose: [what it does]
- Syntax: [command structure]
- Options: [flags and parameters]
- Examples: [common usage]
```

### Code Comments
```
Write comments for this [language] code:

[paste code here]

Explain purpose and any non-obvious logic.
```

---

## Marketing

### Landing Page
```
Write landing page copy for [product/feature].

- Audience: [who this is for]
- Main benefit: [key value]
- Supporting benefits: [secondary points]
- CTA: [desired action]
```

### Product Announcement
```
Write an announcement for [feature/release].

- What's new: [describe]
- Why it matters: [user benefit]
- Availability: [when/how to access]
```

### Email Campaign
```
Write a marketing email for [purpose].

- Goal: [desired action]
- Audience: [segment]
- Key message: [main point]
- CTA: [call to action]
```

---

## MCP & Agents

### System Prompt
```
Write a system prompt for an agent that [purpose].

- Users: [who it serves]
- Capabilities: [what it can do]
- Constraints: [what it must NOT do]
- Tone: [how it should communicate]
```

### Tool Description
```
Write a tool description for [tool name].

- Purpose: [what it does]
- When to use: [trigger scenarios]
- Inputs: [parameters]
- Output: [what it returns]
```

### Agent Instructions
```
Write instructions for [agent name/purpose].

- Role: [what it is]
- Tasks: [what it should do]
- Knowledge: [what it has access to]
- Guardrails: [what to avoid]
```

---

## Research & Insights

### Research Synthesis
```
Synthesize these findings into content recommendations:

[paste findings]

Focus: [what content decisions this should inform]
```

### Feedback Analysis
```
Extract content insights from this feedback:

[paste feedback]

Identify pain points, language patterns, and opportunities.
```

---

## Validation

### Rubric Check
```
Validate this against the [skill-name] rubric:

[paste content]

Flag failures with specific fixes.
```

### Style Check
```
Check this against style standards (capitalization, punctuation, formatting):

[paste content]
```

### Accessibility Check
```
Check this for accessibility (reading level, inclusive language, screen reader):

[paste content]
```

---

## Tips

1. **Be specific** – More detail in brackets = better output
2. **Add context** – Product name, audience, existing patterns
3. **Validate after** – Run a rubric check on generated content
4. **Chain prompts** – Strategy first, then execution
