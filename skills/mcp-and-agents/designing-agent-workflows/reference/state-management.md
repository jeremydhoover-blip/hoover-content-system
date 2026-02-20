# State Management Reference

## Table of contents
1. [State fundamentals](#state-fundamentals)
2. [State declaration patterns](#state-declaration-patterns)
3. [State transitions](#state-transitions)
4. [State persistence](#state-persistence)
5. [Common state bugs](#common-state-bugs)

---

## State fundamentals

### What is workflow state?
State is data that:
- Persists across steps
- Influences decision points
- Must be available for recovery
- Tracks workflow progress

### State vs. step data
| State | Step data |
|-------|-----------|
| Persists across steps | Used only within one step |
| Declared at workflow level | Local to step |
| Required for decisions | Intermediate calculations |
| Needed for recovery | Can be recomputed |

---

## State declaration patterns

### Basic state declaration
```md
## State
- `user_id`: string — ID of user initiating workflow
- `items_processed`: int — count of items completed
- `status`: enum (pending, processing, complete, failed)
```

### Typed state with defaults
```md
## State
| Variable | Type | Default | Purpose |
|----------|------|---------|---------|
| `retry_count` | int | 0 | Current retry attempt |
| `max_retries` | int | 3 | Maximum attempts allowed |
| `last_error` | string | null | Most recent error message |
| `results` | array | [] | Accumulated outputs |
```

### Complex state objects
```md
## State

### `current_item`
```json
{
  "id": "<string>",
  "status": "<pending|processing|done|error>",
  "data": "<object>",
  "error": "<string|null>"
}
```

### `progress`
```json
{
  "total": "<int>",
  "completed": "<int>",
  "failed": "<int>",
  "start_time": "<timestamp>",
  "estimated_completion": "<timestamp>"
}
```
```

---

## State transitions

### Explicit transitions
Document when state changes:

```md
### Step 3: Process item
**State changes**:
- `items_processed` += 1
- `current_item.status` = "done"
- `results.push(output)`
```

### Conditional transitions
```md
### Decision: Did step succeed?
**Branches**:
- IF success:
  - `retry_count` = 0
  - `status` = "processing"
  - → Next step
- IF failure:
  - `retry_count` += 1
  - `last_error` = error_message
  - → Retry or abort
```

### Transition guards
Prevent invalid state:

```md
### Step N: <Name>
**Precondition**: `status == "processing"`
**Guard**: IF `status != "processing"` → Error("Invalid state")
```

---

## State persistence

### When to persist
- Before human checkpoints
- Before external calls that may fail
- At regular intervals in long workflows
- Before any operation that can't be safely retried

### Persistence patterns

**Checkpoint persistence**:
```md
### Checkpoint: Before external API call
**Persist**: all state variables
**Format**: JSON
**Location**: /workflow-state/{workflow_id}.json
```

**Incremental persistence**:
```md
### After each item processed
**Persist**: `items_processed`, `results`, `last_error`
**Strategy**: Append to log, snapshot every 100 items
```

**Transactional persistence**:
```md
### Step N: Database operation
**Transaction**:
1. Persist state to staging
2. Execute database operation
3. On success: Commit state
4. On failure: Rollback state, restore previous
```

### Recovery from persisted state
```md
## Recovery procedure
1. Load persisted state from checkpoint
2. Verify state integrity
3. Identify last completed step
4. Resume from next step

**State validation on recovery**:
- `items_processed` <= `total_items`
- `status` in valid enum values
- `results.length` == `items_processed`
```

---

## Common state bugs

### Uninitialized state

**Bug**: State variable used before initialization.

```md
✗ Bug:
### Step 1
**Action**: if `retry_count` > 3, abort
(retry_count never initialized)

✓ Fix:
## State
- `retry_count`: int — default: 0
```

### Stale state

**Bug**: State not updated after relevant action.

```md
✗ Bug:
### Step N
**Action**: Process item
(items_processed not incremented)

✓ Fix:
### Step N
**Action**: Process item
**State update**: `items_processed` += 1
```

### State corruption on retry

**Bug**: Partial state update before failure.

```md
✗ Bug:
### Step N
1. Update state A
2. Make API call (fails)
3. State A is wrong for retry

✓ Fix:
### Step N (atomic)
1. temp_state = copy(state)
2. Update temp_state
3. Make API call
4. On success: state = temp_state
5. On failure: temp_state discarded
```

### Race condition in parallel

**Bug**: Multiple parallel tasks update same state.

```md
✗ Bug:
### Parallel tasks
Each task: `results.push(output)`
(Race condition on results array)

✓ Fix:
### Parallel tasks
Each task stores: `task_results[task_id] = output`
### Merge step
`results` = merge all `task_results`
```

### Inconsistent state at decision

**Bug**: Decision uses outdated state value.

```md
✗ Bug:
### Decision: Continue?
Evaluate: `items_remaining > 0`
(But items_remaining wasn't updated after last step)

✓ Fix:
### Pre-decision state refresh
**Update**: `items_remaining` = `total - items_processed`
### Decision: Continue?
Evaluate: `items_remaining > 0`
```

### Lost state on error path

**Bug**: Error handling doesn't preserve useful state.

```md
✗ Bug:
### On error
→ Abort workflow
(No information about what failed or how far we got)

✓ Fix:
### On error
**Preserve**: `last_successful_step`, `items_processed`, `error_details`
**Report**: Include preserved state in error output
→ Abort workflow
```
