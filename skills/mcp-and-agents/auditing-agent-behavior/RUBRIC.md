# Rubric

Pass if all are true:
- Audit scope and sampling method are explicitly stated
- Evaluation criteria are derived from agent specifications (not invented)
- Sample size is sufficient for statistical relevance or exhaustive for critical paths
- Each finding includes severity, frequency, and specific examples
- Correct and incorrect behaviors are both documented
- Failure patterns are identified, not just individual failures
- Root cause hypotheses are proposed for significant issues
- Recommendations are specific and actionable (not "improve X")
- Metrics compare actual performance against defined targets
- Audit trail is reproducible (interaction IDs, timestamps, links)

Fail if any are true:
- Evaluation criteria are vague or not tied to specifications
- Sampling method introduces bias (only user-flagged interactions)
- Findings lack concrete examples or interaction references
- Recommendations are generic ("make it better", "fix errors")
- Missing severity classification for findings
- No distinction between systematic patterns and isolated incidents
- Audit scope is undefined or shifts mid-audit
- Critical safety or compliance criteria are not evaluated
