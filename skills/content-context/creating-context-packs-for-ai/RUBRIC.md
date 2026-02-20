# Rubric

## Pass criteria
Pass if all are true:

- [ ] Feature overview provides enough context for AI to understand the domain
- [ ] Content generation scope explicitly lists what AI should and should not generate
- [ ] Vocabulary section includes canonical terms with prohibited alternatives
- [ ] All relevant states are documented with tone guidance per state
- [ ] Hard constraints are clearly distinguished from soft constraints
- [ ] Character limits are specified with rationale for each content type
- [ ] Prohibited content patterns are explicitly listed
- [ ] Tone guidance includes boundaries (what never to sound like)
- [ ] At least 3 examples provided with good/bad pairs
- [ ] Each example explains why it's good or bad (not just shows it)
- [ ] Edge cases are documented with handling guidance
- [ ] Context pack is within target AI system's token budget
- [ ] Context pack tested with target AI system and produces acceptable output

## Fail criteria
Fail if any are true:

- Feature overview missing or too vague for AI to understand context
- Content scope undefined (AI doesn't know what it can/can't generate)
- Vocabulary missing or terms undefined
- States not documented (AI doesn't know what situation to write for)
- No constraints provided (AI has no guardrails)
- No character limits (AI produces content that won't fit UI)
- Prohibited patterns missing (AI may generate off-brand content)
- Examples show correct output but don't explain why
- No bad examples (AI can't learn from counterexamples)
- Context pack exceeds token budget (AI truncates critical info)
- Untested with target AI (may not produce usable output)
- Uses ambiguous language AI could interpret multiple ways
