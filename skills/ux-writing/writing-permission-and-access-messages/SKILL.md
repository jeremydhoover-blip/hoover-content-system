---
name: writing-permission-and-access-messages
description: Write clear permission requests and access messages for UI. Use when requesting permissions, explaining access requirements, showing access denied states, or guiding users through permission flows.
---

# Writing Permission and Access Messages

## Quick start
Collect or infer:
- Permission type (location, camera, notifications, data access, role-based)
- Current state (requesting, granted, denied, expired)
- Why the permission is needed
- Impact of granting or denying

Then produce output using [TEMPLATES.md](TEMPLATES.md). Validate with [RUBRIC.md](RUBRIC.md).

## Workflow
1. Identify permission type and current state
2. Write the headline (what access is needed)
3. Write the explanation (why and what user gets)
4. Specify available actions
5. Run the rubric check. Revise until it passes.

## Degrees of freedom
- **Low**: Must explain why permission is needed
- **Medium**: Explanation detail varies by permission sensitivity
- **Allowed variation**: Pre-request prompts optional but recommended for sensitive permissions

## Constraints
- Headline: max 60 characters
- Explanation: max 150 characters
- Action labels: max 20 characters
- Always explain the benefit of granting permission
- Never request unnecessary permissions

## References
- Templates: [TEMPLATES.md](TEMPLATES.md)
- Rubric: [RUBRIC.md](RUBRIC.md)
- Examples: [EXAMPLES.md](EXAMPLES.md)
