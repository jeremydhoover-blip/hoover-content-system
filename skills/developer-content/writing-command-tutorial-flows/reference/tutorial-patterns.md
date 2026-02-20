# Tutorial Structure Patterns

## Pattern selection guide

| User need | Pattern | Example |
|-----------|---------|---------|
| Learn new tool from scratch | Linear tutorial | "Build your first X" |
| Accomplish specific task | Task-focused tutorial | "Deploy to production" |
| Understand concept through doing | Concept tutorial | "How authentication works" |
| Fix a problem | Recovery tutorial | "Recover from X error" |
| Compare approaches | Decision tutorial | "REST vs GraphQL" |

## Linear tutorial pattern

**Use when:** Teaching fundamentals to beginners.

**Structure:**
1. Clear end goal
2. Prerequisites checklist
3. Sequential steps (each builds on previous)
4. Checkpoints every 2-3 steps
5. Comprehensive troubleshooting
6. Cleanup instructions
7. Next steps to continue learning

**Key principles:**
- No forks or options
- Explain every command
- Show all output
- Assume minimal knowledge

## Task-focused tutorial pattern

**Use when:** User needs to accomplish something specific.

**Structure:**
1. Clear outcome statement
2. Prerequisites (including prior tutorials)
3. Branching options based on user context
4. Focused steps toward goal
5. Verification of success
6. Brief troubleshooting
7. Related tasks

**Key principles:**
- Get to the point quickly
- Options for different scenarios
- Minimal explanation (link to concepts)
- Assume tool familiarity

## Recovery tutorial pattern

**Use when:** User is in a bad state and needs to fix it.

**Structure:**
1. Symptoms section (how user knows they have this problem)
2. Diagnosis steps (confirm the problem)
3. Recovery options by severity
4. Verification of fix
5. Prevention tips

**Key principles:**
- Acknowledge user frustration
- Multiple recovery paths
- Clear checkpoints
- Emphasis on not making it worse

## Step design principles

### Step size
- One logical action per step
- If step has substeps, consider splitting
- If step takes >2 minutes, add progress indicators

### Step naming
- Start with action verb: Configure, Create, Deploy, Verify
- Include object: "Configure the database", not just "Configure"
- Be specific: "Create the Dockerfile", not "Create a file"

### Command presentation
```markdown
## Step N: {Verb} {object}

{Why this step is necessary—one sentence.}

```bash
{complete command}
```

{If command has replaceable parts:}
Replace:
- `{placeholder}` with {what user should put}

**Expected output:**
```
{realistic output}
```

{Explain non-obvious parts of the output.}
```

## Checkpoint design

### When to add checkpoints
- After any destructive operation
- After any operation that could silently fail
- Every 3 steps maximum
- Before any step that depends on previous state

### Checkpoint structure
```markdown
### Checkpoint

{What user should verify}

```bash
{verification command}
```

**If successful:** {what they should see}
**If failed:** {what to do}
```

## Troubleshooting design

### Entry structure
```markdown
### {Symptom user observes}

**You might see this if:** {condition}

**To diagnose:**
```bash
{diagnostic command}
```

**To fix:**
1. {First action}
2. {Second action}

**Then:** {resume instruction}
```

### Coverage priorities
1. Errors from previous step dependencies
2. Environment-specific issues (OS, shell, permissions)
3. Common typos or misunderstandings
4. Network/authentication issues
5. Resource conflicts

## Time estimation

| Operation type | Typical time |
|----------------|--------------|
| Run a command | 30 seconds |
| Edit a file | 1-2 minutes |
| Wait for build | 1-5 minutes |
| Install dependencies | 2-5 minutes |
| Debug a failure | 5-10 minutes |
| First-time auth setup | 5-10 minutes |

Add 50% buffer for beginners. Subtract 25% for advanced users.
