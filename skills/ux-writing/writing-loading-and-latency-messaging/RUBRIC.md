# Rubric

## Pass if all are true
- [ ] Latency tier correctly identified
- [ ] Loading indicator matches expected duration
- [ ] Message (if present) is ≤40 characters
- [ ] Detail text (if present) is ≤100 characters
- [ ] No loading state shown for instant operations (<300ms)
- [ ] Spinner or skeleton shown for short waits (300ms-2s)
- [ ] Message appears for medium+ waits (>2s)
- [ ] Time estimate provided for very long waits (>60s)
- [ ] Interruptible operations can be cancelled
- [ ] Timeout exists with error fallback

## Fail if any are true
- [ ] Loading shown for instant operations (perceived slowness)
- [ ] No indicator for operations >1 second
- [ ] Message implies faster completion than realistic
- [ ] No timeout (infinite loading possible)
- [ ] Character limits exceeded
- [ ] User stuck with no way to cancel or go back
- [ ] Loading message is overly technical
- [ ] No transition to error state on failure
