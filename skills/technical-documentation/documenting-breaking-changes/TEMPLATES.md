# Templates

## Breaking change announcement

```md
# Breaking Change: [Brief description]

**Effective date:** [Date when change takes effect]
**Affects:** [Who is impacted]
**Action required by:** [Deadline for migration]

## Summary

[One to two sentences describing what changed and why.]

## What changed

### Before

[Description or code showing previous behavior]

```[language]
[old code/configuration]
```

### After

[Description or code showing new behavior]

```[language]
[new code/configuration]
```

## Who is affected

You are affected if:

- [ ] [Condition 1 — how to check]
- [ ] [Condition 2 — how to check]

You are NOT affected if:

- [Condition that means you're safe]

### How to check

```[language]
[command or code to determine if affected]
```

## Migration guide

### Prerequisites

- [What you need before migrating]

### Step 1: [Action]

[Instructions]

### Step 2: [Action]

[Instructions]

### Step 3: Verify migration

[How to confirm migration succeeded]

## Timeline

| Date | Event |
|------|-------|
| [Date] | Change announced |
| [Date] | Deprecation warning begins |
| [Date] | Old behavior removed |

## FAQ

### Why is this changing?

[Explanation of rationale]

### What happens if I don't migrate?

[Consequence description]

### Can I get an extension?

[Extension policy or contact]

## Support

- [Link to support channel]
- [Link to migration tool if available]
- [Link to detailed documentation]
```

---

## Migration guide template

```md
# Migrating from [old] to [new]

This guide helps you migrate from [old version/behavior] to [new version/behavior].

**Estimated time:** [X minutes/hours]
**Difficulty:** [Easy/Medium/Complex]
**Downtime required:** [Yes, X minutes / No]

## Before you begin

### Prerequisites

- [ ] [Prerequisite 1]
- [ ] [Prerequisite 2]

### Backup

[Recommendation for backing up before migration]

## Migration steps

### Step 1: [Preparation]

[Detailed instructions]

**Checkpoint:** [How to verify this step completed]

### Step 2: [Core migration]

[Detailed instructions with code examples]

**Checkpoint:** [How to verify this step completed]

### Step 3: [Verification]

[How to verify entire migration succeeded]

## Rollback procedure

If you encounter issues:

1. [Rollback step 1]
2. [Rollback step 2]
3. [Contact support if needed]

## Common issues

### [Issue 1]

**Symptom:** [What you see]
**Cause:** [Why it happens]
**Solution:** [How to fix]

## Getting help

- [Support channel]
- [Documentation link]
- [Community forum]
```

---

## Deprecation notice template

```md
# Deprecation Notice: [Feature/API/Parameter]

**Deprecated:** [Date]
**End of support:** [Date]  
**Removal date:** [Date]

## What is being deprecated

[Clear description of deprecated functionality]

## Replacement

Use [new functionality] instead:

```[language]
// Old (deprecated)
[old code]

// New (recommended)
[new code]
```

## Timeline

| Phase | Date | What happens |
|-------|------|--------------|
| Deprecation | [Date] | Deprecation warnings begin |
| End of support | [Date] | No bug fixes, security only |
| Removal | [Date] | Feature no longer available |

## Migration path

[Link to migration guide or brief steps]

## Questions?

[Support contact]
```

---

## Variation rules
- All breaking changes must include before/after examples.
- All migration guides must include verification step.
- All timelines must use specific dates, not relative terms.
- Rollback procedure required for complex migrations.
