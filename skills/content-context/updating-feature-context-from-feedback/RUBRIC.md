# Rubric

## Pass criteria
Pass if all are true:

- [ ] Every change is traceable to at least one documented feedback source
- [ ] Feedback source type is categorized (user research, support ticket, analytics, PM input)
- [ ] Each change specifies the affected context section (vocabulary, states, actions, constraints, etc.)
- [ ] Each change includes explicit before/after content
- [ ] Change type is classified (additive, modifying, removing)
- [ ] Rationale explains why the change is warranted, not just what changed
- [ ] Terminology changes are checked against existing vocabulary for conflicts
- [ ] State changes are verified against the feature's state map
- [ ] Version is incremented following semver logic (patch for corrections, minor for additions, major for breaking changes)
- [ ] Changelog entry exists in imperative mood
- [ ] Conflicts are explicitly flagged and resolution is proposed when feedback contradicts

## Fail criteria
Fail if any are true:

- Change has no traceable feedback source
- Rationale is missing or uses only "per feedback" without specifics
- Before/after content is missing or ambiguous
- New terminology conflicts with existing vocabulary and conflict is not flagged
- State is removed without confirming deprecation across touchpoints
- Version is not incremented
- Changelog is missing or describes changes in past tense without action clarity
- Feedback from unvalidated sources is treated as confirmed requirement
- Multiple conflicting feedback items are merged without conflict resolution
