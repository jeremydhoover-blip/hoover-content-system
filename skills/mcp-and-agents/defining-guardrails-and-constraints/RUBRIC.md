# Rubric

Pass if all are true:
- Every constraint uses imperative mood ("must not", "never", "do not")
- Hard constraints specify exact prohibited behaviors, not categories
- Soft constraints include explicit escalation paths
- Scope boundaries are stated in both positive and negative terms
- Data handling rules specify actions, not just principles
- Each constraint includes a detection or enforcement mechanism
- No constraint conflicts with stated agent purpose
- Ambiguous-case handling is defined with a default behavior
- Constraints are testable (can construct a pass/fail scenario)
- Language contains no hedging ("try to avoid", "generally should not")

Fail if any are true:
- Uses vague terms: "sensitive", "appropriate", "reasonable" without definition
- Constraint lacks enforcement mechanism
- Hard and soft constraints are not distinguished
- Scope boundaries are implicit or undefined
- Contains conflicting constraints
- Missing data handling or action boundaries
- Escalation paths loop indefinitely or lack resolution
- Constraints are untestable
