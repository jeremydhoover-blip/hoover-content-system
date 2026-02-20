# Rubric

## Pass if all are true
- [ ] Label clearly names what the setting controls
- [ ] Label is ≤40 characters
- [ ] Description (if present) explains the effect of the setting
- [ ] Description is ≤120 characters
- [ ] Toggle labels describe the ON state (not what's disabled)
- [ ] No double negatives ("Disable notifications" toggle = confusing)
- [ ] Default value is specified and sensible
- [ ] Setting type matches the interaction (binary = toggle, options = select)
- [ ] Related settings are grouped logically
- [ ] Destructive settings have appropriate warnings

## Fail if any are true
- [ ] Label is vague ("Setting 1", "Option")
- [ ] Toggle describes OFF state ("Disable..." as a toggle)
- [ ] Double negative logic ("Don't hide...")
- [ ] Description repeats the label without adding information
- [ ] Character limits exceeded
- [ ] No default specified for required setting
- [ ] Destructive action (delete account) lacks confirmation
- [ ] Technical jargon without explanation
