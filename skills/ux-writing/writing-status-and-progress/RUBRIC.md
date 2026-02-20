# Rubric

## Pass if all are true
- [ ] Status label accurately reflects current system state
- [ ] Status label is ≤30 characters
- [ ] Detail text (if present) is ≤100 characters
- [ ] Progress indicator type matches actual knowledge (determinate only if known)
- [ ] Indeterminate progress doesn't show fake percentages
- [ ] State transitions make sense (pending → in-progress → completed/failed)
- [ ] Failed states include recovery guidance or action
- [ ] User knows if action is required from them
- [ ] Long-running tasks set duration expectations
- [ ] Completed states confirm what happened

## Fail if any are true
- [ ] Progress percentage shown when actual progress is unknown
- [ ] Status doesn't update as state changes
- [ ] Stuck states with no timeout or recovery
- [ ] "Loading..." used for everything without context
- [ ] Failed state with no explanation or next step
- [ ] Character limits exceeded
- [ ] Past-tense label for in-progress state ("Uploaded" while still uploading)
- [ ] No visual indicator accompanying status text
