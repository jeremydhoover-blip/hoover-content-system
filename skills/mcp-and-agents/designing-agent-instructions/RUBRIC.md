# Rubric

Pass if all are true:
- Agent purpose is stated in one clear sentence
- Required behaviors (MUST do) are explicit and actionable
- Prohibited behaviors (MUST NOT do) are explicit and unambiguous
- Decision authority is defined (what agent decides vs. asks about)
- Output format is specified
- Error handling guidance exists
- Instructions are specific enough that two readers would interpret them the same way
- No contradictory rules exist within the instruction set
- Edge cases have explicit guidance or default behavior
- Instructions fit within reasonable context window (< 2000 tokens for most agents)

Fail if any are true:
- Purpose statement is vague (e.g., "helps users with tasks")
- Behavior rules use ambiguous words (e.g., "be helpful", "use good judgment")
- Missing prohibition rules for obviously harmful actions within scope
- No guidance for decision authority (agent doesn't know when to ask)
- Error handling not addressed
- Contradictory instructions (e.g., "always ask" conflicts with "respond quickly")
- Critical behavior hidden in prose instead of explicit rules
- Instructions assume context the agent won't have
