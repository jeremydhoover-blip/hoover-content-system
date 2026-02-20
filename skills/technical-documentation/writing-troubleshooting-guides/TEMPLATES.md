# Templates

## Symptom-based troubleshooting guide

```md
# Troubleshooting: [Problem description]

Use this guide when you experience [specific observable symptom].

## Symptoms

You may see one or more of these:

- [Observable symptom 1]
- [Observable symptom 2]
- [Error message or code, if applicable]

## Quick checks

Before diving deeper, verify:

- [ ] [Common quick check 1]
- [ ] [Common quick check 2]

## Possible causes

| Cause | Likelihood | Diagnostic |
|-------|------------|------------|
| [Cause 1] | Common | [Brief diagnostic indicator] |
| [Cause 2] | Common | [Brief diagnostic indicator] |
| [Cause 3] | Rare | [Brief diagnostic indicator] |

## Diagnosis and resolution

### Cause 1: [Cause name]

**Identify this cause:** [How to confirm this is the issue]

```[language]
[diagnostic command or check]
```

**If this is the cause:**

1. [Resolution step 1]
2. [Resolution step 2]
3. Verify: [How to confirm resolution worked]

### Cause 2: [Cause name]

**Identify this cause:** [How to confirm this is the issue]

**If this is the cause:**

1. [Resolution step 1]
2. Verify: [How to confirm resolution worked]

### Cause 3: [Cause name]

**Identify this cause:** [How to confirm this is the issue]

**If this is the cause:**

1. [Resolution step 1]
2. Verify: [How to confirm resolution worked]

## Still having issues?

If none of the above resolved your issue:

1. Collect diagnostic information: [what to gather]
2. [Escalation path: support channel, issue tracker, etc.]
```

---

## Decision-tree troubleshooting guide

```md
# Troubleshooting: [Problem description]

Use this guide to systematically identify and resolve [problem type].

## Start here

**What do you see?**

- [Symptom A] → Go to [Section A](#section-a)
- [Symptom B] → Go to [Section B](#section-b)
- [Symptom C] → Go to [Section C](#section-c)

---

## Section A

### Step 1: Check [first thing]

```[language]
[diagnostic command]
```

**Result:**
- [Expected output] → Problem is [diagnosis]. Go to [Resolution A1](#resolution-a1).
- [Other output] → Go to Step 2.

### Step 2: Check [second thing]

[Continue branching...]

---

## Resolution A1

[Step-by-step fix]

**Verify:** [How to confirm resolution]

---

## Resolution A2

[Alternative fix for different diagnosis]

---

## Escalation

If you've reached this point without resolution:

- Gather: [diagnostic data to collect]
- Contact: [support channel]
```

---

## Error code reference guide

```md
# Error: [ERROR_CODE]

## Message

`[Full error message text]`

## Meaning

[One to two sentences explaining what this error means.]

## Common causes

1. **[Cause 1]** — [Brief explanation]
2. **[Cause 2]** — [Brief explanation]

## Resolution

### For cause 1:

1. [Step 1]
2. [Step 2]

### For cause 2:

1. [Step 1]
2. [Step 2]

## Related errors

- [`RELATED_ERROR_1`](./related-error-1.md)
- [`RELATED_ERROR_2`](./related-error-2.md)
```

---

## Variation rules
- Symptoms section must describe observable user experience, not internal state.
- Each cause must have both diagnostic criteria and resolution steps.
- Resolution must include verification step.
- Escalation section required for all guides.
- Decision trees must terminate in either resolution or escalation.
