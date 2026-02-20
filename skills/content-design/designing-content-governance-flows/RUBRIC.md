# Rubric

## Pass if all are true:
- Every content type has explicit flow stages defined
- Each stage has clear entry and exit criteria (no "when ready" vagueness)
- Roles have explicit permissions (what they can and cannot do)
- Responsibilities are assigned to specific roles, not shared ambiguously
- Review checklists exist with pass/fail criteria
- SLAs are defined for each stage
- Escalation paths exist for exceptions and blockers
- Exception handling covers: urgent content, high-risk content, absent approvers
- Failure modes are anticipated and have mitigation
- Governance scales with risk (low-risk content has lighter process)

## Fail if any are true:
- Stages use undefined criteria ("when appropriate", "as needed")
- Multiple roles share same responsibility without tiebreaker
- Review criteria are subjective ("good quality") without measurable checks
- No SLAs defined (unlimited time per stage)
- No escalation path for blocked content
- All content treated same regardless of risk level
- Role permissions overlap without conflict resolution
- Process requires people not available (single point of failure)
- Exception path doesn't exist (only happy path documented)
- Governance creates bottleneck without alternative (all content funnels through one person)
