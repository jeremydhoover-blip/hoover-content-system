---
name: designing-developer-onboarding
description: Designs developer onboarding experiences and documentation sequences. Use when creating getting-started guides, quickstart flows, developer portals, sandbox environments, or progressive learning paths for APIs and platforms.
---

# Designing Developer Onboarding

## Quick start
Collect or infer:
- Platform/API being onboarded to
- Target developer persona (hobbyist, enterprise, specific stack)
- Time-to-first-success target (minutes to working example)
- Authentication and access requirements
- Available sandbox/test environments

Then produce output using [TEMPLATES.md](TEMPLATES.md). Validate with [RUBRIC.md](RUBRIC.md).

## Workflow
1. Define the "aha moment": what working state proves the platform's value?
2. Map prerequisites: account creation, credentials, environment setup.
3. Design the fastest path to first success (strip non-essential steps).
4. Identify natural expansion points after initial success.
5. Create progressive complexity tiers: quickstart → tutorial → reference.
6. Build escape hatches for stuck developers.
7. Add measurement points to track onboarding completion.
8. Run the rubric check. Revise until it passes.

## Degrees of freedom
**Medium freedom**

- Default: follow templates for onboarding structure
- Allowed variation: progression depth may vary by platform complexity; persona-specific paths permitted; sandbox requirements differ by platform

## State awareness
Developer onboarding tracks through states:
- **Unaware**: Hasn't heard of platform
- **Curious**: Evaluating, needs clear value proposition
- **Committed**: Signed up, needs fast first success
- **Exploring**: First success achieved, expanding usage
- **Integrating**: Building production implementation
- **Stuck**: Encountered obstacle, needs rescue path

## References
- Templates: [TEMPLATES.md](TEMPLATES.md)
- Rubric: [RUBRIC.md](RUBRIC.md)
- Examples: [EXAMPLES.md](EXAMPLES.md)
- Onboarding patterns: [reference/onboarding-patterns.md](reference/onboarding-patterns.md)
