# Evals

Evaluation frameworks for validating skill outputs. Use these to check if AI-generated content meets quality standards.

## Purpose

This folder provides a **structure and example** for creating eval files—not pre-built test suites. The eval system is designed for you to:

- Build your own test cases as you use skills in production
- Validate that AI outputs meet your specific quality bar
- Create regression tests when you find edge cases
- Share evals with your team for consistent quality

## What's Here

- `writing-error-messages.eval.json` — Example eval file showing the format and structure
- Schema documentation in `governance/eval-spec.md`

**Eval files are placeholders.** You create them as you use and evaluate skill outputs.

## Example File

See `writing-error-messages.eval.json` for a working example with 5 test cases covering:
- Validation errors (empty required field)
- System errors (server unavailable)
- Network errors (offline)
- Permission errors (access denied)
- Not-found errors (deleted file)

## File Format

Each eval file follows this structure:

```json
{
  "skill": "skills/category/skill-name",
  "version": "1.0",
  "cases": [
    {
      "id": "unique-case-id",
      "description": "What this tests",
      "input": { ... },
      "expected": { ... },
      "rubric_checks": ["criterion-1", "criterion-2"]
    }
  ]
}
```

## Creating an Eval File

1. Name it `{skill-folder-name}.eval.json`
2. Add at least 3 cases (positive, negative, edge)
3. Reference criteria from the skill's RUBRIC.md
4. Test with real scenarios users would encounter

## Running Evals

Evals are data files—they don't run themselves. Use them with:
- Manual review (compare AI output to expected)
- Automated testing tools (if you build or use an eval runner)
- CI/CD pipelines (for regression testing)

## Contributing

Want to add eval coverage for a skill? See [CONTRIBUTING.md](../CONTRIBUTING.md).