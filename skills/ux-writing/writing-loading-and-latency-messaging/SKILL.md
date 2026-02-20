---
name: writing-loading-and-latency-messaging
description: Write clear loading states and latency messages for UI. Use when users wait for content to load, actions to complete, or when explaining delays in system response.
---

# Writing Loading and Latency Messaging

## Quick start
Collect or infer:
- Loading type (initial load, action response, background refresh)
- Expected duration (instant, short, long, unknown)
- User interruptibility (can user do other things?)
- Fallback if loading fails

Then produce output using [TEMPLATES.md](TEMPLATES.md). Validate with [RUBRIC.md](RUBRIC.md).

## Workflow
1. Classify latency tier using [reference/latency-tiers.md](reference/latency-tiers.md)
2. Determine if user can continue working or must wait
3. Write loading message appropriate to duration
4. Plan transition to loaded or error state
5. Run the rubric check. Revise until it passes.

## Degrees of freedom
- **Low**: Must show loading indicator for >1 second waits
- **Medium**: Message detail scales with expected wait time
- **Allowed variation**: Silent loading for <1 second operations

## Constraints
- Loading message: max 40 characters
- Detail text: max 100 characters
- Never show loading states for instant operations (<300ms)
- Provide time estimates for waits >30 seconds
- Always have a timeout and error fallback

## References
- Templates: [TEMPLATES.md](TEMPLATES.md)
- Rubric: [RUBRIC.md](RUBRIC.md)
- Examples: [EXAMPLES.md](EXAMPLES.md)
- Latency tiers: [reference/latency-tiers.md](reference/latency-tiers.md)
