# Rubric

## Pass criteria
Pass if all are true:

- [ ] Report includes explicit PASS/FAIL/PASS WITH WARNINGS status
- [ ] Every blocking issue includes location, problem, impact, and remediation
- [ ] Coverage matrix accounts for all required sections per reference/required-fields.md
- [ ] State coverage table shows entry, exit, error handling, and content guidance status
- [ ] No blocking issue is listed without a specific remediation step
- [ ] Warnings are distinguished from blocking issues by severity
- [ ] Validation checks structural completeness (fields exist)
- [ ] Validation checks semantic consistency (references resolve, no contradictions)
- [ ] Validation checks coverage completeness (all states have error handling)
- [ ] Report includes next steps if any issues found

## Fail criteria
Fail if any are true:

- [ ] Report declares PASS when blocking issues exist
- [ ] Missing sections are not flagged (false negative)
- [ ] Non-issues are flagged as blocking (false positive)
- [ ] Remediation steps are generic ("fix this") instead of specific
- [ ] State coverage is not analyzed
- [ ] Vocabulary consistency is not checked
- [ ] Report does not distinguish severity levels
- [ ] Orphan definitions (referenced but undefined) are not detected
- [ ] Circular state dependencies are not detected

## Severity classification rules

| Issue type | Severity |
|------------|----------|
| Required field missing | Blocking |
| State with no entry condition | Blocking |
| State with no exit condition | Blocking |
| Vocabulary term used but not defined | Blocking |
| Conflicting definitions | Blocking |
| Unreachable state | Blocking |
| Optional field missing | Warning |
| State without error handling | Warning |
| Transition without content guidance | Suggestion |
| Redundant definition | Suggestion |
