# Templates

## Standard tutorial structure

```md
# {Tutorial title: verb + outcome}

{One paragraph: what you'll accomplish and why it matters.}

**Time to complete:** {X} minutes
**Difficulty:** {Beginner | Intermediate | Advanced}

## Prerequisites

Before you begin, make sure you have:
- [ ] {Prerequisite 1}
- [ ] {Prerequisite 2}
- [ ] {Prerequisite 3}

## What you'll build

{Brief description of end result. Include screenshot or diagram if visual.}

---

## Step 1: {Action verb + object}

{Why this step matters—one sentence.}

```bash
{command}
```

**Expected output:**
```
{output}
```

{Optional: brief explanation of what happened.}

---

## Step 2: {Action verb + object}

{Context for this step.}

```bash
{command}
```

**Expected output:**
```
{output}
```

### Checkpoint
{How to verify this step succeeded.}

---

## Step {N}: {Final action}

{Context.}

```bash
{command}
```

**Expected output:**
```
{output}
```

---

## Verify your work

Run this command to confirm everything is set up correctly:

```bash
{verification command}
```

You should see:
```
{expected verification output}
```

## Troubleshooting

### {Common problem 1}
**Symptom:** {what user sees}
**Cause:** {why it happens}
**Fix:** {how to resolve}

### {Common problem 2}
{Same pattern}

## Cleanup

To remove resources created in this tutorial:

```bash
{cleanup command 1}
{cleanup command 2}
```

## Next steps

- {Link to next tutorial}
- {Link to reference documentation}
- {Link to advanced topic}
```

## Step template

```md
## Step {N}: {Action verb + object}

{One sentence explaining why this step is necessary.}

```bash
{command with realistic values}
```

{If command has placeholders:}
Replace:
- `{placeholder}` with your {description}

**Expected output:**
```
{realistic output}
```

{If output varies:}
Your output may differ in {specific ways}.

{If step creates something:}
This creates a {resource} named `{name}` with {key properties}.
```

## Checkpoint template

```md
### Checkpoint

Verify step {N} succeeded:

```bash
{verification command}
```

You should see `{key indicator}` in the output.

{If checkpoint fails:}
If you see `{error indicator}` instead, {recovery action}.
```

## Branching step template (for optional or conditional paths)

```md
## Step {N}: {Action}

Choose one of the following based on your {condition}:

### Option A: {Description}
Use this if {condition A}.

```bash
{command A}
```

### Option B: {Description}
Use this if {condition B}.

```bash
{command B}
```

{Both options should converge to same state for next step.}
```

## Troubleshooting entry template

```md
### {Error message or symptom}

**You might see this if:** {condition}

**To fix:**
1. {First action}
2. {Second action}

Then retry:
```bash
{command to retry}
```
```
