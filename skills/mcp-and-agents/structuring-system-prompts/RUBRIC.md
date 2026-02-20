# Rubric

Pass if all are true:
- Identity section states who the agent is and its primary purpose in ≤3 sentences
- Capabilities are stated in both positive (CAN) and negative (CANNOT) terms
- Critical rules are numbered and placed prominently, not buried
- Rules are prioritized or ordered by importance
- Tool instructions include purpose, trigger condition, and usage example
- Output format is specified with structure or template
- Conflict resolution is addressed (what to do when guidelines conflict)
- Prompt is scannable (uses headers, lists, formatting)
- Examples demonstrate ambiguous cases, not obvious ones
- Total token count is tracked and within budget

Fail if any are true:
- Identity is vague ("You are a helpful assistant")
- Critical and preferred guidelines are mixed without distinction
- No capability boundaries stated
- Tools listed without usage guidance
- Rules are purely negative (only "don't" without "do")
- Conflicting instructions exist at different levels
- No output format specification
- Examples are trivial or obvious
- Prompt is a wall of text without structure
