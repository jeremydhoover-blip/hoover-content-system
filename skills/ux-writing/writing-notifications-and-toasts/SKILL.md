---
name: writing-notifications-and-toasts
description: Write clear notification and toast messages for UI. Use when showing transient alerts, system notifications, success confirmations, warnings, or in-app messages that don't require immediate action.
---

# Writing Notifications and Toasts

## Quick start
Collect or infer:
- Notification type (success, error, warning, info)
- Urgency (immediate, informational, background)
- Action required (none, optional, required)
- Persistence (auto-dismiss, manual dismiss, persistent)

Then produce output using [TEMPLATES.md](TEMPLATES.md). Validate with [RUBRIC.md](RUBRIC.md).

## Workflow
1. Classify notification type using [reference/notification-types.md](reference/notification-types.md)
2. Determine urgency and persistence
3. Write the message (what happened)
4. Add action if applicable
5. Run the rubric check. Revise until it passes.

## Degrees of freedom
- **Low**: Type determines visual treatment (color, icon)
- **Medium**: Message length varies by complexity
- **Allowed variation**: Actions optional for pure confirmations

## Constraints
- Message: max 80 characters
- Action label: max 20 characters
- Auto-dismiss: 4-8 seconds for success/info
- Never auto-dismiss errors that need attention
- One notification at a time (queue if multiple)

## References
- Templates: [TEMPLATES.md](TEMPLATES.md)
- Rubric: [RUBRIC.md](RUBRIC.md)
- Examples: [EXAMPLES.md](EXAMPLES.md)
- Notification types: [reference/notification-types.md](reference/notification-types.md)
