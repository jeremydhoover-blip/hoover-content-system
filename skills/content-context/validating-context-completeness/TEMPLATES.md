# Templates

## Default output: Validation Report

Use this as the default structure:

```md
# Context Pack Validation Report

**Pack:** [context pack name]
**Version:** [version]
**Validated:** [date]
**Status:** [PASS | FAIL | PASS WITH WARNINGS]

## Summary
- Blocking issues: [count]
- Warnings: [count]
- Suggestions: [count]

## Blocking Issues
[If none: "No blocking issues found."]

### [BLOCK-001] [Issue title]
- **Location:** [section/field path]
- **Problem:** [what is wrong]
- **Impact:** [why this breaks the pack]
- **Remediation:** [specific fix]

## Warnings
[If none: "No warnings."]

### [WARN-001] [Issue title]
- **Location:** [section/field path]
- **Problem:** [what is missing or weak]
- **Recommendation:** [suggested improvement]

## Suggestions
[If none: "No suggestions."]

### [SUGG-001] [Suggestion title]
- **Location:** [section/field path]
- **Opportunity:** [what could be improved]

## Coverage Matrix

| Section | Required | Present | Status |
|---------|----------|---------|--------|
| Feature purpose | Yes | [Yes/No] | [✓/✗] |
| User goals | Yes | [Yes/No] | [✓/✗] |
| Core actions | Yes | [Yes/No] | [✓/✗] |
| States | Yes | [Yes/No] | [✓/✗] |
| Transitions | Yes | [Yes/No] | [✓/✗] |
| Error taxonomy | Yes | [Yes/No] | [✓/✗] |
| Vocabulary | Yes | [Yes/No] | [✓/✗] |
| Tone boundaries | No | [Yes/No] | [—/✓] |
| Constraints | No | [Yes/No] | [—/✓] |

## State Coverage

| State | Entry defined | Exit defined | Error handling | Content guidance |
|-------|---------------|--------------|----------------|------------------|
| [state name] | [Yes/No] | [Yes/No] | [Yes/No] | [Yes/No] |

## Next Steps
1. [First remediation action]
2. [Second remediation action]
3. Re-run validation after fixes
```

## Compact validation output (for CI/scripts)

```json
{
  "pack": "[name]",
  "version": "[version]",
  "status": "PASS | FAIL | PASS_WITH_WARNINGS",
  "blocking": [
    {
      "code": "BLOCK-001",
      "location": "[path]",
      "message": "[description]"
    }
  ],
  "warnings": [],
  "suggestions": []
}
```

## Quick checklist output (for fast review)

```md
## Quick Validation Checklist

- [ ] Feature purpose defined
- [ ] At least one user goal specified
- [ ] All core actions listed
- [ ] Every state has entry/exit conditions
- [ ] Every transition has source and target
- [ ] Error taxonomy covers all failure modes
- [ ] Vocabulary section includes all unique terms
- [ ] No orphan definitions
- [ ] No circular dependencies in states
- [ ] No conflicting term definitions
```
