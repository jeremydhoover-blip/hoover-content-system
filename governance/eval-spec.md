# Eval Specification

## Scope

Schema, validation rules, and authoring constraints for evaluation files. Complements `evals/README.md` with enforceable rules.

## Hard Rules

### File Requirements

1. Every skill must have exactly one eval file.
2. Eval file must be in `/evals` folder.
3. Eval file name must match skill folder name: `{skill-name}.eval.json`.
4. Eval file must be valid JSON.

### Schema

```json
{
  "skill": "string (required) - relative path to skill folder",
  "version": "string (required) - schema version, currently '1.0'",
  "cases": [
    {
      "id": "string (required) - unique kebab-case identifier",
      "description": "string (optional) - what this case tests",
      "input": {
        "prompt": "string (required) - the test prompt",
        "context": "object (optional) - additional variables"
      },
      "expected": {
        "contains": "array (optional) - strings that must appear",
        "excludes": "array (optional) - strings that must not appear",
        "format": "string (optional) - expected structure",
        "maxLength": "number (optional) - character limit"
      },
      "grading": {
        "rubricRef": "string (required) - criterion ID from RUBRIC.md",
        "passThreshold": "string (required) - 'pass' or 'strong-pass'"
      }
    }
  ]
}
```

### Case Requirements

1. Minimum 3 cases per eval file.
2. Must include at least one positive case (valid input, expected success).
3. Must include at least one negative case (invalid/missing input).
4. Must include at least one edge case (boundary conditions).
5. Each case must have unique `id` within the file.
6. Case `id` must be kebab-case and descriptive.

### Input Rules

1. `prompt` must be a realistic user request.
2. `prompt` must not include meta-instructions ("test this skill").
3. `context` keys must match input names defined in skill's SKILL.md.
4. Missing required context triggers negative case behavior.

### Expected Rules

1. `contains` items must be specific, not vague ("good copy").
2. `excludes` items should reference prohibited patterns from RUBRIC.md.
3. `format` must use predefined values: `single-sentence`, `multi-sentence`, `bulleted-list`, `numbered-list`, `paragraph`, `structured`.
4. `maxLength` must match constraints in skill's TEMPLATES.md if specified.

### Grading Rules

1. `rubricRef` must exactly match an `id` in the skill's RUBRIC.md.
2. `passThreshold` determines minimum passing grade:
   - `pass`: Meets basic criteria
   - `strong-pass`: Exceeds criteria, no issues
3. One case may reference multiple rubric criteria by using array.

## Prohibited Patterns

| Pattern | Violation |
|---------|-----------|
| `"contains": ["good"]` | Vague expectation |
| `"id": "test1"` | Non-descriptive ID |
| `"prompt": "Test the error message skill"` | Meta-instruction |
| `"rubricRef": "quality"` | Non-existent rubric ID |
| Fewer than 3 cases | Insufficient coverage |
| All positive cases | Missing negative/edge testing |
| Duplicate case IDs | Non-unique identifiers |

## Validation Checklist

Before committing an eval file:

- [ ] File name matches skill folder name
- [ ] JSON is valid
- [ ] `skill` path points to existing skill folder
- [ ] Minimum 3 cases present
- [ ] At least 1 positive, 1 negative, 1 edge case
- [ ] All `rubricRef` values exist in skill's RUBRIC.md
- [ ] All case IDs are unique and kebab-case
- [ ] No vague `contains` or `excludes` values
- [ ] `context` keys match skill's defined inputs

## Example Eval File

```json
{
  "skill": "developer-content/writing-cli-help-and-usage",
  "version": "1.0",
  "cases": [
    {
      "id": "standard-help-text-generation",
      "description": "Generate help text for a CLI command with typical inputs",
      "input": {
        "prompt": "Write help text for a 'deploy' command that pushes code to production",
        "context": {
          "command_name": "deploy",
          "flags": ["--env", "--force", "--dry-run"]
        }
      },
      "expected": {
        "contains": ["deploy", "--env", "--force", "--dry-run", "Usage"],
        "excludes": ["click here", "please"],
        "format": "structured"
      },
      "grading": {
        "rubricRef": "cli-help-includes-usage-pattern",
        "passThreshold": "pass"
      }
    },
    {
      "id": "missing-command-name-prompts",
      "description": "Skill should ask for command name if not provided",
      "input": {
        "prompt": "Write CLI help text",
        "context": {}
      },
      "expected": {
        "contains": ["command", "name", "?"],
        "format": "single-sentence"
      },
      "grading": {
        "rubricRef": "cli-help-requests-missing-input",
        "passThreshold": "pass"
      }
    },
    {
      "id": "max-length-constraint-respected",
      "description": "Output respects 500 character limit when specified",
      "input": {
        "prompt": "Write brief help text for 'status' command, max 500 characters",
        "context": {
          "command_name": "status",
          "max_length": 500
        }
      },
      "expected": {
        "contains": ["status"],
        "maxLength": 500
      },
      "grading": {
        "rubricRef": "cli-help-respects-length-constraints",
        "passThreshold": "strong-pass"
      }
    }
  ]
}
```