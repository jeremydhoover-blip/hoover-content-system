# Templates

## Audit finding entry
Use this structure for each finding:

```md
### [Finding ID]: [Short description]

**Location**: [Screen name] > [Component/Element]
**Copy**: "[Exact text found]"
**Severity**: [Critical | Major | Minor]
**Issue type**: [Inconsistency | Clarity | Tone | Accessibility | Action mismatch | Redundancy]

**Problem**: [One sentence describing what's wrong]
**Impact**: [How this affects user behavior or comprehension]

**Recommendation**:
- Before: "[Current copy]"
- After: "[Suggested copy]"

**Rationale**: [Why this change improves the experience]
```

## Audit summary report
Use this as the final deliverable structure:

```md
# UI Copy Audit Report

## Audit scope
- **Screens reviewed**: [number]
- **Copy elements evaluated**: [number]
- **Date**: [audit date]
- **Auditor**: [name or "AI-assisted"]

## Executive summary
[2-3 sentences on overall quality and top priorities]

## Findings by severity

### Critical ([count])
[List finding IDs and one-line descriptions]

### Major ([count])
[List finding IDs and one-line descriptions]

### Minor ([count])
[List finding IDs and one-line descriptions]

## Pattern analysis
[Recurring issues observed across multiple screens]

## Recommendations
1. [Highest priority action]
2. [Second priority action]
3. [Third priority action]

## Detailed findings
[Include all finding entries from above template]
```

## Copy inventory table
Use for initial extraction:

```md
| Screen | Element type | Copy text | Character count | Notes |
|--------|--------------|-----------|-----------------|-------|
| [Screen name] | [Button/Label/Error/etc.] | "[text]" | [count] | [flags] |
```
