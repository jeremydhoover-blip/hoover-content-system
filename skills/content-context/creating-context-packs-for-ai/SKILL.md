---
name: creating-context-packs-for-ai
description: Creates structured context documents that AI systems can consume to generate consistent, accurate content for a feature. Use when preparing a feature for AI-assisted content generation, building AI writing workflows, or enabling LLMs to write within product constraints.
---

# Creating Context Packs for AI

## Quick start
Collect or infer:
- Feature name and scope
- Existing context documents (state maps, vocabulary, content briefs)
- AI system requirements (token limits, format constraints)
- Content types the AI will generate
- Guardrails and constraints the AI must respect

Then produce output using [TEMPLATES.md](TEMPLATES.md). Validate with [RUBRIC.md](RUBRIC.md).

## Workflow
1. Gather all existing feature context (vocabulary, states, constraints, tone).
2. Identify what content the AI will generate and in what contexts.
3. Structure context following the [context pack schema](reference/context-pack-schema.md).
4. Include explicit constraints and prohibited patterns.
5. Add examples of correct and incorrect outputs.
6. Validate completeness using the [completeness checklist](reference/completeness-checklist.md).
7. Test with target AI system to verify usability.
8. Run the rubric check. Revise until it passes.

## Degrees of freedom
- **Default:** Low. Context packs must be precise and complete.
- **Allowed variation:** Format may adapt to AI system requirements. Detail level may vary by content complexity.

## Failure modes to avoid
- Omitting constraints that lead to off-brand content
- Including redundant information that wastes tokens
- Using ambiguous language that AI interprets differently than intended
- Missing state-specific guidance (AI doesn't know what state it's writing for)
- Providing examples without explaining why they're correct
- Creating context packs that exceed AI token limits

## References
- Templates: [TEMPLATES.md](TEMPLATES.md)
- Rubric: [RUBRIC.md](RUBRIC.md)
- Examples: [EXAMPLES.md](EXAMPLES.md)
- Context pack schema: [reference/context-pack-schema.md](reference/context-pack-schema.md)
- Completeness checklist: [reference/completeness-checklist.md](reference/completeness-checklist.md)
