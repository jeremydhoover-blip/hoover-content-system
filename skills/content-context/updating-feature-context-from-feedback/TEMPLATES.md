# Templates

## Default output: Context update record

Use this structure when documenting context changes:

```md
# Context Update Record

## Metadata
- **Context pack:** <feature-name>
- **Previous version:** <x.y.z>
- **New version:** <x.y.z>
- **Update date:** <YYYY-MM-DD>
- **Update author:** <name or role>

## Feedback sources
| Source type | Reference | Date received |
|-------------|-----------|---------------|
| <user-research / support-ticket / analytics / pm-input / other> | <link or ID> | <YYYY-MM-DD> |

## Changes

### Change 1: <Short description>
- **Affected section:** <vocabulary / states / actions / constraints / error-taxonomy / tone-boundaries / other>
- **Feedback type:** <gap / correction / expansion / deprecation>
- **Change type:** <additive / modifying / removing>

**Before:**
<exact current content>

**After:**
<proposed new content>

**Rationale:**
<why this change is warranted, citing specific feedback>

**Conflicts identified:** <none / describe conflict>

---

### Change 2: <Short description>
<repeat structure>

---

## Changelog entry
- <version>: <summary of changes in imperative mood>

## Validation checklist
- [ ] All changes traceable to feedback source
- [ ] No terminology conflicts introduced
- [ ] Affected states verified against state map
- [ ] Version incremented correctly
- [ ] Changelog updated
```

## Compact change summary (for review handoffs)

Use when sharing changes for stakeholder approval:

```md
# Context Update Summary: <feature-name>

**Version:** <previous> → <new>
**Changes:** <count>

| # | Section | Change type | Summary |
|---|---------|-------------|---------|
| 1 | <section> | <type> | <one-line summary> |
| 2 | <section> | <type> | <one-line summary> |

**Requires review by:** <role or name>
**Deadline:** <date>
```

## Conflict report (when feedback contradicts)

```md
# Feedback Conflict Report

## Conflict ID: <unique-id>

**Feedback A:**
- Source: <source>
- States: <claim>

**Feedback B:**
- Source: <source>
- States: <claim>

**Resolution options:**
1. <option with rationale>
2. <option with rationale>

**Recommended resolution:** <option number>
**Rationale:** <why>
```
