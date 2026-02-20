# Templates

## Default output: Step-by-step tutorial

```md
# [Outcome-focused title: "How to X" or "Building Y"]

[Brief intro: what the reader will accomplish and why it matters — 2-3 sentences]

**What you'll learn:**
- [Outcome 1]
- [Outcome 2]
- [Outcome 3]

**Prerequisites:**
- [Prerequisite 1]
- [Prerequisite 2]

**Time required:** [X minutes/hours]

---

## Step 1: [Action-oriented step title]

[Brief context: why this step is necessary]

[Specific instruction]

```[code/command if applicable]
```

**Verify:** [What the reader should see or be able to confirm]

---

## Step 2: [Next action-oriented step title]

[Continue pattern...]

---

## Troubleshooting

### [Common error or issue]
**Cause:** [Why this happens]
**Fix:** [How to resolve]

### [Another common issue]
**Cause:** [Why this happens]
**Fix:** [How to resolve]

---

## Next steps

- [Related tutorial or feature to explore]
- [Resource for deeper learning]
```

## Alternative: Concept-then-practice tutorial

For tutorials that require foundational understanding:

```md
# [Title]

## What is [concept]?

[Brief explanation — 2-3 sentences max]

## When to use [concept]

[Use cases or scenarios]

## Tutorial: [Practical application]

[Steps follow standard pattern...]
```

## Alternative: Comparison tutorial

For tutorials showing multiple approaches:

```md
# [Title: "X ways to accomplish Y"]

## Overview

| Approach | Best for | Complexity |
|----------|----------|------------|
| [Approach 1] | [Use case] | [Low/Medium/High] |
| [Approach 2] | [Use case] | [Low/Medium/High] |

## Approach 1: [Name]

[Steps...]

## Approach 2: [Name]

[Steps...]

## Which should you choose?

[Decision guidance]
```

## Checkpoint patterns

Use these to help readers verify progress:

```md
**Verify:** Your terminal should show:
```
Output here
```

**Verify:** Open `config.json`. You should see:
```json
{
  "setting": "value"
}
```

**Verify:** Navigate to `localhost:3000`. You should see the login page.

**Checkpoint:** At this point, your file structure should look like:
```
project/
├── src/
│   └── index.js
└── package.json
```
```
