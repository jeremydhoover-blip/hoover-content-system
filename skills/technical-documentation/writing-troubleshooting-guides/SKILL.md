---
name: writing-troubleshooting-guides
description: Create diagnostic documentation that helps users identify and resolve problems systematically. Use when users encounter errors, unexpected behavior, or need to debug issues.
---

# Writing Troubleshooting Guides

## Quick start
Collect or infer:
- Problem category (error type, symptom pattern, failure domain)
- Observable symptoms users can identify
- Potential root causes ranked by likelihood
- Diagnostic steps to isolate cause
- Resolution steps for each cause

Then produce output using [TEMPLATES.md](TEMPLATES.md). Validate with [RUBRIC.md](RUBRIC.md).

## Workflow
1. Define the problem scope with specific, observable symptoms.
2. List possible causes from most to least common.
3. Write diagnostic steps that progressively narrow down the cause.
4. Provide resolution steps for each identified cause.
5. Include verification that the problem is resolved.
6. Add escalation path if resolution fails.
7. Run the rubric check. Revise until it passes.

## Degrees of freedom
- **Medium**: Problem organization can vary (symptom-first vs. cause-first).
- Allowed variation: Diagnostic depth and branching complexity may vary as long as rubric passes.

## State awareness
- If symptom is ambiguous, include differentiating diagnostic steps.
- If causes span multiple systems, organize by system boundary.
- If resolution requires elevated permissions, state prerequisites.
- If problem has known temporary workarounds, document separately from fix.

## Failure modes to avoid
- Listing causes without diagnostic steps to identify them
- Providing resolutions without verifying they solved the problem
- Omitting escalation paths for unresolved issues
- Mixing prevention advice with troubleshooting

## References
- Templates: [TEMPLATES.md](TEMPLATES.md)
- Rubric: [RUBRIC.md](RUBRIC.md)
- Examples: [EXAMPLES.md](EXAMPLES.md)
- Troubleshooting patterns: [reference/troubleshooting-patterns.md](reference/troubleshooting-patterns.md)
