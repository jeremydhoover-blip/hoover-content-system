# Workflow Patterns Reference

## Table of contents
1. [Workflow types](#workflow-types)
2. [Step documentation patterns](#step-documentation-patterns)
3. [Decision point patterns](#decision-point-patterns)
4. [Error handling patterns](#error-handling-patterns)
5. [Verification patterns](#verification-patterns)

---

## Workflow types

### Linear workflow
Sequential steps with no branching.

```
[Step 1] → [Step 2] → [Step 3] → [Done]
```

**Best for**: Simple processes, initial setup, one-time tasks  
**Documentation focus**: Clear step ordering, prerequisites

### Branching workflow
Steps vary based on conditions.

```
[Start] → [Check] → [Path A] → [End]
              ↘ [Path B] ↗
```

**Best for**: Environment-specific processes, conditional logic  
**Documentation focus**: Decision criteria, all paths documented

### Parallel workflow
Independent steps that can run simultaneously.

```
         ┌→ [Step A] →┐
[Start] ─┼→ [Step B] →┼→ [Join] → [End]
         └→ [Step C] →┘
```

**Best for**: CI/CD pipelines, multi-service deployments  
**Documentation focus**: Dependencies, synchronization points

### Iterative workflow
Repeated steps until condition met.

```
[Start] → [Do Work] → [Check] → [Done]
              ↑          ↓
              └──────────┘
```

**Best for**: Retry logic, batch processing, polling  
**Documentation focus**: Exit conditions, maximum iterations, backoff

---

## Step documentation patterns

### Minimal step (simple command)
```md
### Step N: <Action>
```bash
<command>
```
```

### Standard step (recommended minimum)
```md
### Step N: <Action>

**Command:**
```bash
<command>
```

**Expected output:**
```
<success output>
```

**Troubleshooting:**
- If `<error>`: <fix>
```

### Detailed step (complex operations)
```md
### Step N: <Action>

**Purpose**: <why this step exists>

**Prerequisites**: <what must be true before running>

**Command:**
```bash
<command with explanatory comments>
```

**Expected output:**
```
<success output with key indicators highlighted>
```

**Duration**: <typical time>

**Troubleshooting:**
| Error | Cause | Fix |
|-------|-------|-----|
| <error 1> | <cause> | <fix> |
| <error 2> | <cause> | <fix> |

**Rollback**: <how to undo if needed>
```

---

## Decision point patterns

### Binary decision
```md
## Decision: <Question>

| Condition | Action |
|-----------|--------|
| <condition A> | Proceed to [Step X](#step-x) |
| <condition B> | Proceed to [Step Y](#step-y) |
```

### Multi-way decision
```md
## Decision: <Question>

Evaluate `<check>` and follow the appropriate path:

| Result | Meaning | Next step |
|--------|---------|-----------|
| `<value 1>` | <meaning> | [Path A](#path-a) |
| `<value 2>` | <meaning> | [Path B](#path-b) |
| `<value 3>` | <meaning> | [Path C](#path-c) |
| Other | Unexpected state | [Troubleshoot](#troubleshooting) |
```

### Implicit decision (with defaults)
```md
## Decision: <Question>

**Default path**: <most common choice>

Only deviate if:
- <condition requiring alternate path>
- <another condition>
```

---

## Error handling patterns

### Inline troubleshooting
Best for 1-2 common errors per step.

```md
**Troubleshooting:**
- If `<error>`: <fix>
```

### Table troubleshooting
Best for multiple error cases.

```md
| Symptom | Cause | Resolution |
|---------|-------|------------|
| <symptom 1> | <cause> | <fix> |
| <symptom 2> | <cause> | <fix> |
```

### Dedicated troubleshooting section
Best for complex workflows with many failure modes.

```md
## Troubleshooting

### <Error category 1>
**Symptoms**: <what you observe>
**Diagnosis**:
```bash
<diagnostic command>
```
**Resolution**: <step-by-step fix>

### <Error category 2>
...
```

### Rollback procedures
```md
## Rollback procedure

### Automatic rollback
If the workflow includes automatic rollback:
```bash
<rollback command>
```

### Manual rollback
If automatic rollback fails:
1. <manual step 1>
2. <manual step 2>

### Point of no return
After [Step N], rollback requires:
- <special procedure>
- <data restoration>
```

---

## Verification patterns

### Per-step verification
```md
**Verify:**
```bash
<verification command>
```
Expected: `<expected output>`
```

### Milestone verification
```md
## Checkpoint: <Phase complete>

Before proceeding, confirm:
- [ ] <condition 1> (`<check command>`)
- [ ] <condition 2> (`<check command>`)
- [ ] <condition 3> (`<check command>`)
```

### End-to-end verification
```md
## Final verification

Run the smoke test:
```bash
./scripts/smoke-test.sh
```

Expected results:
- [ ] API responds with 200 OK
- [ ] Database queries return data
- [ ] Background jobs processing

If any check fails, proceed to [Rollback](#rollback-procedure).
```
