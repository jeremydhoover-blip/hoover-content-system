# Rubric

## Pass if all are true:
- Audit scope is explicitly defined with screen/flow boundaries
- Every copy element is categorized by type (button, label, error, tooltip, empty state, etc.)
- Each finding includes location, exact copy, severity, and issue type
- Severity ratings use consistent taxonomy: Critical (blocks task), Major (causes confusion), Minor (polish)
- Each recommendation includes before/after copy, not just abstract advice
- Pattern analysis identifies at least one recurring issue across screens
- Findings are actionable without requiring additional research
- Accessibility issues are flagged when copy lacks screen reader context or uses visual-only language
- No finding is marked Critical unless it directly blocks user task completion or causes error

## Fail if any are true:
- Findings are vague ("this could be clearer") without specific recommended copy
- Severity is applied inconsistently (similar issues get different ratings)
- Audit skips error states, empty states, or edge-case screens without justification
- Recommendations duplicate existing voice/tone guidance verbatim instead of applying it
- Pattern analysis is missing or lists only single-instance issues
- Copy inventory is incomplete (missing entire screens or element types)
- Findings lack location specificity (cannot identify where in UI the issue appears)
- Accessibility is ignored entirely
