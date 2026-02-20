# Templates

## Default output: Agent workflow specification

Use this as the default structure:

```md
# Workflow: <Name>

## Goal
<One sentence: What this workflow accomplishes.>

## Success criteria
The workflow succeeds when:
- [ ] <Measurable outcome 1>
- [ ] <Measurable outcome 2>

## State
Track these values across steps:
- `<state_var>`: <type> — <purpose>

---

## Steps

### Step 1: <Name>
**Input**: <What this step needs>
**Action**: <What the agent does>
**Output**: <What this step produces>
**Next**: <Step 2> | <Decision 1>

**On failure**:
- <Error type>: <Recovery action>

---

### Decision 1: <Question>
**Evaluate**: <condition>
**Branches**:
- IF <condition A> → <Step X>
- IF <condition B> → <Step Y>
- ELSE → <Default step>

---

### Step 2: <Name>
...

---

## Human checkpoints
Pause and request approval before:
- <High-risk action>
- <Irreversible change>

## Termination conditions
Workflow ends when:
- SUCCESS: <success condition>
- FAILURE: <max retries exceeded / unrecoverable error>
- ABORT: <user cancellation>
```

## Variant: Linear workflow

```md
# Workflow: <Sequential Task>

## Steps (execute in order)

1. **<Step name>**
   - Action: <what to do>
   - Verify: <how to confirm success>
   - On fail: <recovery>

2. **<Step name>**
   - Action: <what to do>
   - Verify: <how to confirm success>
   - On fail: <recovery>

3. **<Step name>**
   ...

## Completion
Workflow complete when all steps verify successfully.
```

## Variant: Branching workflow

```md
# Workflow: <Conditional Task>

## Decision tree

```
[Start]
    │
    ▼
[Analyze input]
    │
    ├─ Type A? ──► [Handle Type A] ──► [Verify A] ──► [Done]
    │
    ├─ Type B? ──► [Handle Type B] ──► [Verify B] ──► [Done]
    │
    └─ Unknown ──► [Ask for clarification] ──► [Start]
```

## Step definitions

### Analyze input
- Examine: <what to look at>
- Classify as: Type A | Type B | Unknown
- Store classification in: `input_type`

### Handle Type A
- Precondition: `input_type == "A"`
- Actions: <specific actions>

### Handle Type B
- Precondition: `input_type == "B"`
- Actions: <specific actions>
```

## Variant: Retry-loop workflow

```md
# Workflow: <Retryable Task>

## Configuration
- `max_attempts`: 3
- `backoff`: exponential (1s, 2s, 4s)

## Steps

### Attempt task
```
attempt = 1
WHILE attempt <= max_attempts:
    result = execute_task()
    IF result.success:
        RETURN success
    ELSE:
        log_error(result.error)
        wait(backoff[attempt])
        attempt += 1

RETURN failure("Max attempts exceeded")
```

### Execute task
- Action: <what to do>
- Success if: <condition>
- Retriable errors: <error types to retry>
- Fatal errors: <error types to abort>

## Termination
- SUCCESS: Task completes successfully
- FAILURE: Max attempts exceeded or fatal error encountered
```

## Variant: Parallel workflow

```md
# Workflow: <Parallel Tasks>

## Parallel execution

### Phase 1 (parallel)
Execute simultaneously:
- **Task A**: <description>
- **Task B**: <description>
- **Task C**: <description>

Wait for all to complete.

### Phase 2 (sequential)
After all Phase 1 tasks complete:
- **Merge results**: <how to combine outputs>
- **Validate**: <final check>

## Failure handling
- If ANY parallel task fails: <strategy: abort all | continue others | retry>
- Timeout for parallel phase: <duration>
```
