# Rubric

## Pass if all are true
- [ ] Title states what went wrong in user terms (not technical jargon)
- [ ] Title is ≤60 characters
- [ ] Body (if present) is ≤150 characters
- [ ] Action label is ≤25 characters
- [ ] Action is specific and actionable (not generic "OK" unless dismissal is the only option)
- [ ] Message does not blame the user ("You entered..." → "Enter...")
- [ ] Message does not expose internal errors, codes, or stack traces
- [ ] Tone matches severity (calm for minor, direct for blocking)
- [ ] Message tells user how to recover or what to do next
- [ ] Error type is correctly classified per reference/error-categories.md

## Fail if any are true
- [ ] Title is vague ("Error", "Something went wrong" with no context)
- [ ] Message uses technical terms users won't understand
- [ ] Message blames or scolds the user
- [ ] Action is missing when recovery is possible
- [ ] Action label is vague when specific action exists ("OK" instead of "Try again")
- [ ] Character limits exceeded
- [ ] Message creates anxiety disproportionate to severity
- [ ] Error code or exception text visible to user
