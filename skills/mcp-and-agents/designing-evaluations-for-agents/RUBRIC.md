# Rubric

Pass if all are true:
- Evaluation covers all stated agent capabilities
- Each scenario has specific, verifiable expected behaviors (not just outputs)
- Scenarios include happy path, edge cases, AND adversarial cases
- Expected behaviors are observable (can verify without subjective judgment)
- Must-not behaviors are explicit for each scenario
- Metrics have clear calculation method and threshold
- Pass criteria are defined and measurable
- At least one scenario tests boundary conditions
- At least one scenario tests failure handling
- Evaluation is reproducible (same input produces consistent evaluation)

Fail if any are true:
- Capability claimed but not tested
- Expected behavior is vague (e.g., "responds appropriately")
- Only happy path scenarios present
- No adversarial or edge case scenarios
- Metric has no defined threshold
- Pass criteria are subjective
- Expected outputs specified without expected behaviors
- No test for how agent handles invalid input
- Evaluation requires human judgment with no rubric
