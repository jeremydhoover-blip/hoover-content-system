---
name: writing-status-and-progress
description: Write clear status indicators and progress messages for UI. Use when showing system state, task progress, sync status, connection state, or any ongoing process feedback.
---

# Writing Status and Progress

## Quick start
Collect or infer:
- Status type (system state, task progress, sync, connection)
- Current state (pending, in-progress, completed, failed)
- Duration expectation (instant, seconds, minutes, indefinite)
- User action required (none, optional, required)

Then produce output using [TEMPLATES.md](TEMPLATES.md). Validate with [RUBRIC.md](RUBRIC.md).

## Workflow
1. Identify status type using [reference/status-states.md](reference/status-states.md)
2. Determine the current state in the lifecycle
3. Write the status label (what's happening)
4. Add detail text if duration or action needed
5. Run the rubric check. Revise until it passes.

## Degrees of freedom
- **Low**: Status must accurately reflect system state
- **Medium**: Detail text optional based on context
- **Allowed variation**: Tone adjusts for success vs. waiting states

## Constraints
- Status label: max 30 characters
- Detail text: max 100 characters
- Never lie about progress (fake progress bars)
- Indeterminate progress must say so, not show fake percentages

## References
- Templates: [TEMPLATES.md](TEMPLATES.md)
- Rubric: [RUBRIC.md](RUBRIC.md)
- Examples: [EXAMPLES.md](EXAMPLES.md)
- Status states: [reference/status-states.md](reference/status-states.md)
