# Rubric

## Pass if all are true
- [ ] Notification type matches the message content
- [ ] Message clearly states what happened
- [ ] Message is ≤80 characters
- [ ] Action label (if present) is ≤20 characters
- [ ] Success/info use auto-dismiss (4-8 seconds)
- [ ] Errors requiring action do NOT auto-dismiss
- [ ] Undo actions have sufficient time before dismiss (6+ seconds)
- [ ] Visual style (color, icon) matches notification type
- [ ] One notification visible at a time (or queued)
- [ ] Dismiss option always available

## Fail if any are true
- [ ] Error auto-dismisses before user can read/act
- [ ] Success notification for failed action
- [ ] Warning used when error is appropriate
- [ ] Character limits exceeded
- [ ] No dismiss option for persistent notifications
- [ ] Multiple overlapping notifications (visual chaos)
- [ ] Undo action auto-dismisses in <5 seconds
- [ ] Message is vague ("Something happened")
