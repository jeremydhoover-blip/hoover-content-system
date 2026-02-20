# Templates

## Default output: Agent evaluation specification

Use this as the default structure:

```json
{
  "evaluation_name": "<descriptive name>",
  "agent": "<agent identifier>",
  "version": "<evaluation version>",
  "capabilities_tested": ["<capability 1>", "<capability 2>"],
  
  "scenarios": [
    {
      "id": "<unique_id>",
      "name": "<descriptive name>",
      "category": "<happy_path | edge_case | adversarial | regression>",
      "capability": "<which capability this tests>",
      
      "input": {
        "query": "<user input or trigger>",
        "context": "<relevant context provided>",
        "files": ["<file paths if applicable>"]
      },
      
      "expected_behaviors": [
        "<observable behavior 1>",
        "<observable behavior 2>",
        "<observable behavior 3>"
      ],
      
      "must_not": [
        "<prohibited behavior 1>",
        "<prohibited behavior 2>"
      ],
      
      "evaluation_criteria": {
        "type": "<exact_match | contains | regex | llm_judge | human_review>",
        "check": "<what to check>",
        "threshold": "<pass condition>"
      }
    }
  ],
  
  "metrics": {
    "<metric_name>": {
      "description": "<what it measures>",
      "calculation": "<how to calculate>",
      "threshold": "<pass/fail threshold>",
      "weight": "<importance weight if aggregating>"
    }
  },
  
  "pass_criteria": {
    "minimum_pass_rate": "<percentage>",
    "required_scenarios": ["<scenario_ids that must pass>"],
    "blocking_failures": ["<failure types that auto-fail evaluation>"]
  }
}
```

## Variant: Simple behavioral evaluation

```md
# Evaluation: <Agent Name> - <Capability>

## Scenarios

### Scenario 1: <Name>
**Input**: <query>
**Expected**:
- [ ] <behavior 1>
- [ ] <behavior 2>

### Scenario 2: <Name>
**Input**: <query>
**Expected**:
- [ ] <behavior 1>
- [ ] <behavior 2>

## Pass criteria
Pass if: All expected behaviors observed in all scenarios.
```

## Variant: Graded evaluation with rubric

```md
# Evaluation: <Agent Name>

## Grading rubric

| Criterion | 0 (Fail) | 1 (Partial) | 2 (Pass) |
|-----------|----------|-------------|----------|
| <criterion 1> | <fail description> | <partial description> | <pass description> |
| <criterion 2> | <fail description> | <partial description> | <pass description> |

## Scenarios

### Scenario 1: <Name>
**Input**: <query>
**Grade each criterion 0-2**

| Criterion | Score | Evidence |
|-----------|-------|----------|
| <criterion 1> | | |
| <criterion 2> | | |

**Scenario score**: Sum / Max possible

## Overall pass criteria
- Minimum scenario score: 70%
- No criterion scores 0 on any scenario
```

## Variant: Regression test suite

```json
{
  "suite_name": "regression-v1",
  "description": "Tests for known failure modes and fixed bugs",
  
  "tests": [
    {
      "id": "REG-001",
      "description": "Fixed: Agent used to hallucinate file paths",
      "bug_reference": "#123",
      "input": {"query": "Show me the config file"},
      "must_not": ["reference non-existent files", "hallucinate paths"],
      "verification": "All file paths in response exist in workspace"
    }
  ],
  
  "execution": {
    "run_on": ["pre-commit", "nightly"],
    "fail_fast": true
  }
}
```
