# Workflow Patterns Reference

## Table of contents
1. [Workflow types](#workflow-types)
2. [Step patterns](#step-patterns)
3. [Decision patterns](#decision-patterns)
4. [Loop patterns](#loop-patterns)
5. [Composition patterns](#composition-patterns)

---

## Workflow types

### Sequential workflow
Steps execute in fixed order.

```
[Step 1] → [Step 2] → [Step 3] → [Done]
```

**Use when**: Steps have strict dependencies, each requires previous output.
**Example**: Parse → Validate → Transform → Save

### Branching workflow
Different paths based on conditions.

```
[Start] → [Decide] → [Path A] → [End]
                  → [Path B] → [End]
```

**Use when**: Different inputs require different handling.
**Example**: Handle text vs image vs video content

### Parallel workflow
Multiple steps execute simultaneously.

```
         ┌→ [Task A] →┐
[Start] ─┼→ [Task B] →┼→ [Merge] → [End]
         └→ [Task C] →┘
```

**Use when**: Independent tasks can run concurrently.
**Example**: Fetch data from multiple APIs

### Iterative workflow
Loop until condition met.

```
[Start] → [Do Work] → [Check] → [Done]
              ↑          │
              └──────────┘
```

**Use when**: Task requires multiple attempts or batch processing.
**Example**: Retry on failure, process items in queue

### State machine workflow
Explicit states with defined transitions.

```
[Idle] → [Processing] → [Validating] → [Complete]
   ↑          │              │              │
   └──────────┴──────────────┴──────────────┘
                    (on error)
```

**Use when**: Complex state management, multiple recovery paths.
**Example**: Order fulfillment, document approval

---

## Step patterns

### Standard step
```md
### Step N: <Name>
**Input**: <required data>
**Action**: <what happens>
**Output**: <what's produced>
**Next**: <next step or decision>

**On failure**:
- <error type>: <recovery action>
```

### Conditional step
```md
### Step N: <Name> (conditional)
**Execute if**: <precondition>
**Skip if**: <skip condition>
...
```

### Atomic step (all-or-nothing)
```md
### Step N: <Name> (atomic)
**Transaction**: All actions succeed or all rollback
**Actions**:
1. <action 1>
2. <action 2>
**Rollback**: <how to undo>
```

### Timed step
```md
### Step N: <Name>
**Timeout**: <duration>
**On timeout**: <action>
```

---

## Decision patterns

### Binary decision
```md
### Decision: <Yes/No question>
**Evaluate**: <condition>
**Branches**:
- IF true → <Step X>
- IF false → <Step Y>
```

### Multi-way decision
```md
### Decision: <Classification>
**Evaluate**: <expression>
**Branches**:
- IF <value A> → <Step X>
- IF <value B> → <Step Y>
- IF <value C> → <Step Z>
- ELSE → <Default step>
```

### Threshold decision
```md
### Decision: <Threshold check>
**Evaluate**: <metric> against <threshold>
**Branches**:
- IF above threshold → <proceed>
- IF below threshold → <remediate or abort>
```

### Human decision
```md
### Human Checkpoint: <Decision name>
**Present**: <information to show user>
**Options**:
- <Option A>: → <Step X>
- <Option B>: → <Step Y>
- Cancel: → Abort workflow
```

---

## Loop patterns

### Count-limited loop
```md
### Loop: <Name>
**Max iterations**: <N>
**For each iteration**:
1. <action>
2. <check exit condition>

**On max reached**: <action>
```

### Condition-based loop
```md
### Loop: <Name>
**While**: <condition is true>
**Actions**:
1. <action>
2. Update condition variables

**Exit when**: <success condition>
**Failsafe**: Exit after <N> iterations
```

### Retry loop
```md
### Retry: <Operation name>
**Attempts**: <max>
**Backoff**: <strategy: fixed | exponential>
**Delays**: [<delay1>, <delay2>, ...]

**Retry if**: <retriable errors>
**Abort if**: <fatal errors>
**After max attempts**: <action>
```

### Collection processing loop
```md
### Process: <Collection name>
**For each**: <item> in <collection>
**Action**: <what to do>
**On item failure**: <skip | abort | retry>
**Progress**: Report every <N> items
```

---

## Composition patterns

### Sub-workflow
```md
### Step N: Execute <Sub-workflow name>
**Input**: <parameters>
**Wait for**: Completion
**Output**: <sub-workflow result>
**On sub-workflow failure**: <action>
```

### Parallel fan-out
```md
### Parallel: <Name>
**Execute simultaneously**:
- <Task A>
- <Task B>
- <Task C>

**Wait strategy**: all | any | N of M
**Timeout**: <duration>
**On partial failure**: <strategy>
```

### Checkpoint/resume
```md
### Checkpoint: <Name>
**Save state**: <variables to persist>
**Resume from**: This point on restart

**Checkpoint triggers**:
- Every <N> items processed
- Every <duration>
- Before <risky operation>
```

### Saga pattern (compensating transactions)
```md
### Saga: <Multi-step transaction>
**Steps**:
1. <Action A> | Compensate: <Undo A>
2. <Action B> | Compensate: <Undo B>
3. <Action C> | Compensate: <Undo C>

**On failure at step N**:
Execute compensations N-1 → 1 in reverse order
```
