# Rubric

## Pass if all are true
- [ ] Empty state type is correctly identified
- [ ] Headline acknowledges the current state clearly
- [ ] Headline is ≤50 characters
- [ ] Support text (if present) is ≤120 characters
- [ ] Action label is ≤25 characters
- [ ] Action is relevant to populating or resolving the empty state
- [ ] First-run states include motivation or value, not just "nothing here"
- [ ] No-results states suggest how to get results
- [ ] Message does not make user feel they did something wrong
- [ ] Copy matches the content type (items, projects, messages, etc.)

## Fail if any are true
- [ ] Headline is generic ("Nothing here") without context
- [ ] Support text repeats the headline
- [ ] No action provided when user can take action to populate
- [ ] First-run state is demotivating ("You have no data")
- [ ] No-results state doesn't help user adjust their search
- [ ] Character limits exceeded
- [ ] Wrong empty state type diagnosed (e.g., treating error as first-run)
- [ ] Technical language used ("null", "0 records")
