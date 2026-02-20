# Tutorial Structure Patterns

## Table of contents
- [Core structure requirements](#core-structure-requirements)
- [Step design principles](#step-design-principles)
- [Verification patterns](#verification-patterns)
- [Handling complexity](#handling-complexity)
- [Common structural mistakes](#common-structural-mistakes)

---

## Core structure requirements

Every tutorial needs these structural elements:

### Required elements

| Element | Purpose | Location |
|---------|---------|----------|
| Outcome statement | What reader will accomplish | First paragraph |
| Prerequisites | What reader needs before starting | Before first step |
| Time estimate | Sets expectations | Near prerequisites |
| Numbered steps | Clear progression | Body |
| Verification points | Confirms success | End of each step |
| Troubleshooting | Addresses common failures | End or inline |

### Information hierarchy

```
1. What you'll accomplish (outcome)
2. What you need (prerequisites)
3. How long it takes (time)
4. How to do it (steps)
5. What to do if it breaks (troubleshooting)
6. What to do next (further learning)
```

Never bury prerequisites in step 3 or reveal time estimates at the end.

---

## Step design principles

### Atomic steps
Each step should accomplish exactly one thing that can succeed or fail independently.

**Too broad:**
> Step 1: Set up your development environment and create a new project

**Properly atomic:**
> Step 1: Install Node.js
> Step 2: Create a new project directory
> Step 3: Initialize the project

### Action-first wording
Start every step title with a verb.

| Weak | Strong |
|------|--------|
| "The configuration file" | "Create the configuration file" |
| "Dependencies" | "Install dependencies" |
| "About authentication" | "Configure authentication" |

### Context-action-verification pattern

Each step follows this internal structure:

```
[WHY: Brief context — why this step matters]

[WHAT: Specific action to take]

[code/command if applicable]

[CHECK: How to verify success]
```

Example:
```md
## Step 3: Configure the database connection

The app needs to know where to find your database.

Open `config.js` and add:

```javascript
module.exports = {
  database: {
    host: 'localhost',
    port: 5432,
    name: 'myapp'
  }
}
```

**Verify:** Run `npm run check-config`. You should see "Database configuration: OK"
```

---

## Verification patterns

Readers need to know if they've succeeded before moving on.

### Verification types

| Type | When to use | Example |
|------|-------------|---------|
| Visual | UI tutorials | "You should see the dashboard" |
| Output | Command line | "Terminal shows: `Server running`" |
| File state | Configuration | "Your file should now contain..." |
| Test | Code tutorials | "Run `npm test` — all tests pass" |
| Behavior | Integration | "Click Submit; the form clears" |

### Writing effective verifications

**Vague:** "It should work now."
**Specific:** "Navigate to localhost:3000. You should see the login page with email and password fields."

**Vague:** "Check that it's configured correctly."
**Specific:** "Run `app config --verify`. Output should show `Config valid: 3 services connected`."

### When verification isn't obvious

Some steps don't have visible output. Handle with:

```md
**Verify:** This step has no visible output. If the command completed without error, you're good. Continue to Step 4, which will fail if this step wasn't successful.
```

---

## Handling complexity

### Decision points

When the reader must choose, provide decision guidance:

```md
## Step 3: Choose your deployment target

| If you... | Choose | Why |
|-----------|--------|-----|
| Want simplest setup | Option A | Fewer configuration steps |
| Need custom domain | Option B | Built-in DNS management |
| Already use AWS | Option C | Integrates with existing setup |

**Unsure?** Choose Option A. You can migrate later.
```

### Conditional steps

When a step applies only to some readers:

```md
## Step 4: Configure SSL (if using custom domain)

> **Skip this step if** you're using the default domain (*.netlify.app).

[Step content...]
```

### Long tutorials

For tutorials over 15 steps:

1. Group steps into phases
2. Add checkpoint summaries between phases
3. Consider breaking into a series

```md
## Phase 1: Project setup (Steps 1-5)
[Steps...]

### Checkpoint
At this point, you should have:
- [ ] Node.js installed
- [ ] Project created
- [ ] Dependencies installed
- [ ] Config file created
- [ ] Dev server running

If any of these aren't working, review the steps above before continuing.

## Phase 2: Building features (Steps 6-12)
[Steps...]
```

---

## Common structural mistakes

### Mistake 1: Explanation before action
**Wrong:** Two paragraphs explaining what CI is, then finally how to set it up.
**Right:** State what you're building, then explain concepts as needed within steps.

### Mistake 2: Unexplained choices
**Wrong:** "Set the timeout to 30000."
**Right:** "Set the timeout to 30000 (30 seconds). This balances reliability with test speed."

### Mistake 3: Hidden prerequisites
**Wrong:** Step 4 suddenly requires Docker, not mentioned in prerequisites.
**Right:** All requirements listed upfront, or conditional steps clearly marked.

### Mistake 4: Skipping failure states
**Wrong:** Only showing the happy path.
**Right:** Including what errors look like and how to resolve them.

### Mistake 5: Version ambiguity
**Wrong:** "Install Node.js"
**Right:** "Install Node.js 18 or later (this tutorial tested on Node 20)"

### Mistake 6: Assumed environment
**Wrong:** Using `pbcopy` without noting it's macOS-only.
**Right:** Providing alternatives for different operating systems, or stating the assumed environment in prerequisites.
