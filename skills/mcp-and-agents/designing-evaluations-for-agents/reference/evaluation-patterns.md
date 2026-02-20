# Evaluation Patterns Reference

## Table of contents
1. [Evaluation types](#evaluation-types)
2. [Scenario design patterns](#scenario-design-patterns)
3. [Verification patterns](#verification-patterns)
4. [Test suite organization](#test-suite-organization)

---

## Evaluation types

### Behavioral evaluation
Tests what the agent *does*, not just what it outputs.

```json
{
  "type": "behavioral",
  "focus": "Actions taken",
  "checks": [
    "Which tools were called",
    "In what order",
    "With what parameters"
  ],
  "best_for": "Agentic workflows, tool use"
}
```

### Output evaluation
Tests the content of the agent's response.

```json
{
  "type": "output",
  "focus": "Response content",
  "checks": [
    "Contains required information",
    "Format matches template",
    "No prohibited content"
  ],
  "best_for": "Content generation, Q&A"
}
```

### Safety evaluation
Tests boundary conditions and adversarial robustness.

```json
{
  "type": "safety",
  "focus": "Constraint adherence",
  "checks": [
    "Refuses out-of-scope requests",
    "Doesn't leak sensitive data",
    "Handles prompt injection"
  ],
  "best_for": "Production-ready agents"
}
```

### Regression evaluation
Tests that previously fixed issues stay fixed.

```json
{
  "type": "regression",
  "focus": "Known failure modes",
  "checks": [
    "Bug #X doesn't recur",
    "Edge case Y handled correctly"
  ],
  "best_for": "Continuous deployment"
}
```

---

## Scenario design patterns

### Coverage matrix
Ensure all capabilities × conditions are tested:

| Capability | Happy path | Edge case | Error case | Adversarial |
|------------|------------|-----------|------------|-------------|
| Search | ✓ | ✓ | ✓ | ✓ |
| Create | ✓ | ✓ | ✓ | ✓ |
| Update | ✓ | ✓ | ✓ | ✓ |

### Scenario categories

**Happy path**: Normal operation
```json
{
  "category": "happy_path",
  "purpose": "Verify core functionality works",
  "characteristics": "Valid input, expected context, normal conditions"
}
```

**Edge case**: Boundary conditions
```json
{
  "category": "edge_case",
  "purpose": "Test limits and unusual but valid inputs",
  "examples": ["Empty input", "Maximum length", "Special characters", "Unicode"]
}
```

**Error case**: Invalid inputs
```json
{
  "category": "error_case",
  "purpose": "Verify graceful error handling",
  "examples": ["Missing required field", "Wrong type", "Malformed data"]
}
```

**Adversarial**: Malicious inputs
```json
{
  "category": "adversarial",
  "purpose": "Test security and robustness",
  "examples": ["Prompt injection", "Social engineering", "Scope escape"]
}
```

### Scenario templates

**Capability test**:
```json
{
  "id": "<CAP>-<NNN>",
  "name": "<Capability>: <specific test>",
  "capability": "<capability_name>",
  "input": {"query": "<user input>"},
  "expected_behaviors": ["<behavior 1>", "<behavior 2>"],
  "must_not": ["<prohibited behavior>"]
}
```

**Regression test**:
```json
{
  "id": "REG-<NNN>",
  "name": "Regression: <issue description>",
  "bug_reference": "#<issue_number>",
  "input": {"query": "<input that triggered bug>"},
  "expected_behaviors": ["<correct behavior>"],
  "must_not": ["<buggy behavior>"]
}
```

**Safety test**:
```json
{
  "id": "SEC-<NNN>",
  "name": "Safety: <attack vector>",
  "attack_type": "<injection | social_engineering | scope_escape>",
  "input": {"query": "<malicious input>"},
  "must_not": ["<unsafe behavior>"],
  "blocking": true
}
```

---

## Verification patterns

### Exact match
```json
{
  "type": "exact_match",
  "target": "<exact string to match>",
  "use_when": "Output has single correct answer"
}
```

### Contains check
```json
{
  "type": "contains",
  "target": ["<required substring 1>", "<required substring 2>"],
  "all_required": true,
  "use_when": "Key information must be present"
}
```

### Pattern match
```json
{
  "type": "regex",
  "pattern": "<regex pattern>",
  "use_when": "Output has predictable structure"
}
```

### Semantic similarity
```json
{
  "type": "semantic",
  "reference": "<expected content>",
  "threshold": 0.8,
  "use_when": "Meaning matters more than exact wording"
}
```

### LLM-as-judge
```json
{
  "type": "llm_judge",
  "criteria": "<evaluation criteria>",
  "rubric": "<scoring rubric>",
  "threshold": "<pass threshold>",
  "use_when": "Quality requires nuanced judgment"
}
```

### Tool call verification
```json
{
  "type": "tool_call",
  "expected_tools": ["<tool_1>", "<tool_2>"],
  "parameter_checks": {"<tool>": {"<param>": "<expected_value>"}},
  "use_when": "Agent behavior involves tool use"
}
```

---

## Test suite organization

### By capability
```
evals/
├── search/
│   ├── content-search.eval.json
│   ├── filename-search.eval.json
│   └── no-results.eval.json
├── create/
│   └── file-creation.eval.json
└── safety/
    ├── prompt-injection.eval.json
    └── scope-escape.eval.json
```

### By scenario type
```
evals/
├── happy-path/
│   └── core-functionality.eval.json
├── edge-cases/
│   └── boundary-conditions.eval.json
├── adversarial/
│   └── security-tests.eval.json
└── regression/
    └── fixed-bugs.eval.json
```

### By run frequency
```
evals/
├── smoke/          # Run on every commit
├── full/           # Run on PR merge
├── nightly/        # Run once per day
└── release/        # Run before deployment
```

### Suite metadata
```json
{
  "suite": {
    "name": "core-agent-eval",
    "version": "1.0.0",
    "total_scenarios": 50,
    "categories": {
      "happy_path": 20,
      "edge_case": 15,
      "adversarial": 10,
      "regression": 5
    },
    "estimated_duration": "15 minutes",
    "last_updated": "2024-01-15"
  }
}
```
