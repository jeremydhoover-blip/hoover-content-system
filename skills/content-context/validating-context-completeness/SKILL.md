---
name: validating-context-completeness
description: Validates that a context pack contains all required fields, consistent state coverage, and no conflicting definitions. Use when reviewing context packs before handoff, after major updates, or before AI integration.
---

# Validating Context Completeness

## Quick start
Collect or infer:
- Context pack to validate (full JSON/YAML or markdown context file)
- Feature scope (single feature or multi-feature system)
- Target consumer (human writer, AI agent, or both)

Then produce output using [TEMPLATES.md](TEMPLATES.md). Validate with [RUBRIC.md](RUBRIC.md).

## Workflow
1. Run structural validation: check all required sections exist.
2. Run semantic validation: check states reference valid transitions, vocabulary is used consistently, no orphan definitions.
3. Run coverage validation: ensure every state has error handling, every action has success/failure paths.
4. Generate validation report with severity levels (blocking, warning, suggestion).
5. If blocking issues exist, document remediation steps.
6. Run the rubric check. Revise until it passes.

## Degrees of freedom
**Level: Low**

- Default: follow validation rules exactly
- Allowed variation: severity thresholds may adjust for draft vs production context packs

## Behavioral logic
Context packs fail silently when incomplete. A missing state definition causes AI to hallucinate. A conflicting term causes user confusion. This skill enforces completeness as a gate, not a suggestion.

Validation must answer:
- Can every state be reached from another state?
- Does every error have a recovery path defined?
- Are all vocabulary terms used in the pack defined?
- Do any definitions contradict each other?

## Decision framework
| Condition | Action |
|-----------|--------|
| Required field missing | Blocking error |
| State unreachable | Blocking error |
| Vocabulary term used but undefined | Blocking error |
| Optional field missing | Warning |
| Definition contradicts another | Blocking error |
| State has no error handling | Warning |
| Transition has no content guidance | Suggestion |

## References
- Templates: [TEMPLATES.md](TEMPLATES.md)
- Rubric: [RUBRIC.md](RUBRIC.md)
- Examples: [EXAMPLES.md](EXAMPLES.md)
- Required fields: [reference/required-fields.md](reference/required-fields.md)
- Validation rules: [reference/validation-rules.md](reference/validation-rules.md)
- Scripts: [scripts/](scripts/)
