# Rubric

## Pass criteria
Pass if all are true:

- [ ] Entry state is explicitly identified
- [ ] Every state has a defined type (standard, error, loading, empty, success, permission, edge)
- [ ] Every state (except entry) has at least one documented inbound transition
- [ ] Every non-terminal state has at least one documented outbound transition
- [ ] Terminal states are explicitly labeled
- [ ] Error states are present and cover at least: network failure, validation failure, permission denial
- [ ] Loading/pending states are documented for any async operation
- [ ] Empty states are documented where applicable (no data, no results, first use)
- [ ] Each state specifies content requirements (headline, body, CTA, error message)
- [ ] Transitions specify the trigger (user action or system event)
- [ ] Edge cases section exists with at least 2 documented scenarios
- [ ] No orphan states exist (states unreachable from entry)

## Fail criteria
Fail if any are true:

- Entry state is not identified
- Any state lacks a type classification
- Non-entry state has no inbound transition documented
- Non-terminal state has no outbound transition documented
- Error states are missing entirely
- Async operations exist but no loading state is documented
- Content requirements are missing for any state
- Transitions lack triggers (just arrows without explanation)
- Diagram and documentation are inconsistent (states in one but not the other)
- Happy path only — no error or edge case states
- Permission-dependent feature lacks permission-gated states
