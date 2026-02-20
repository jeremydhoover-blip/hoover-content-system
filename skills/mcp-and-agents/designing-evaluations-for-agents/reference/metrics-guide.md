# Metrics Guide Reference

## Table of contents
1. [Metric types](#metric-types)
2. [Calculating metrics](#calculating-metrics)
3. [Setting thresholds](#setting-thresholds)
4. [Aggregation patterns](#aggregation-patterns)

---

## Metric types

### Pass rate
Percentage of scenarios that pass.

```json
{
  "name": "pass_rate",
  "formula": "passed_scenarios / total_scenarios",
  "range": "0-100%",
  "typical_threshold": "≥ 85%",
  "use_case": "Overall evaluation health"
}
```

### Accuracy
Correctness of factual outputs.

```json
{
  "name": "accuracy",
  "formula": "correct_outputs / total_outputs",
  "range": "0-100%",
  "typical_threshold": "≥ 95%",
  "use_case": "Q&A, fact retrieval"
}
```

### Precision
Of the positive predictions, how many were correct.

```json
{
  "name": "precision",
  "formula": "true_positives / (true_positives + false_positives)",
  "range": "0-100%",
  "typical_threshold": "≥ 90%",
  "use_case": "Classification, filtering"
}
```

### Recall
Of the actual positives, how many were found.

```json
{
  "name": "recall",
  "formula": "true_positives / (true_positives + false_negatives)",
  "range": "0-100%",
  "typical_threshold": "≥ 85%",
  "use_case": "Search, detection"
}
```

### Safety rate
Percentage of adversarial scenarios handled correctly.

```json
{
  "name": "safety_rate",
  "formula": "adversarial_passed / adversarial_total",
  "range": "0-100%",
  "typical_threshold": "100%",
  "use_case": "Security evaluation"
}
```

### Behavior coverage
Percentage of expected behaviors observed.

```json
{
  "name": "behavior_coverage",
  "formula": "observed_behaviors / expected_behaviors",
  "range": "0-100%",
  "typical_threshold": "≥ 90%",
  "use_case": "Behavioral evaluation"
}
```

### Latency
Time to complete request.

```json
{
  "name": "latency_p95",
  "formula": "95th percentile of response times",
  "unit": "milliseconds",
  "typical_threshold": "< 5000ms",
  "use_case": "Performance evaluation"
}
```

### Token efficiency
Output quality relative to token usage.

```json
{
  "name": "token_efficiency",
  "formula": "quality_score / tokens_used",
  "use_case": "Cost optimization"
}
```

---

## Calculating metrics

### Per-scenario calculation
```python
def calculate_scenario_score(scenario_result):
    behaviors_observed = count_observed(scenario_result.behaviors)
    behaviors_expected = len(scenario_result.expected_behaviors)
    
    violations = count_violations(scenario_result.must_not)
    
    if violations > 0:
        return 0  # Any violation = fail
    
    return behaviors_observed / behaviors_expected
```

### Suite-level aggregation
```python
def calculate_suite_metrics(results):
    return {
        "pass_rate": sum(r.passed for r in results) / len(results),
        "behavior_coverage": sum(r.behavior_score for r in results) / len(results),
        "safety_rate": (
            sum(r.passed for r in results if r.category == "adversarial") /
            sum(1 for r in results if r.category == "adversarial")
        )
    }
```

### Weighted aggregation
```python
def weighted_score(metrics, weights):
    total_weight = sum(weights.values())
    weighted_sum = sum(
        metrics[name] * weight 
        for name, weight in weights.items()
    )
    return weighted_sum / total_weight

# Example
weights = {
    "accuracy": 1.0,
    "safety_rate": 3.0,  # Safety weighted 3x
    "behavior_coverage": 1.5
}
```

---

## Setting thresholds

### Baseline approach
1. Run evaluation on current agent version
2. Record metrics as baseline
3. Set threshold slightly above baseline
4. Raise threshold as agent improves

### Risk-based thresholds

| Risk level | Metric | Threshold | Rationale |
|------------|--------|-----------|-----------|
| Critical | safety_rate | 100% | No security compromises |
| High | accuracy | ≥ 95% | User trust depends on correctness |
| Medium | behavior_coverage | ≥ 85% | Most behaviors should work |
| Low | latency_p95 | < 10000ms | Performance nice-to-have |

### Blocking vs. warning thresholds

```json
{
  "thresholds": {
    "blocking": {
      "description": "Fail evaluation if below",
      "safety_rate": 100,
      "accuracy": 90
    },
    "warning": {
      "description": "Flag for review if below",
      "behavior_coverage": 85,
      "latency_p95": 5000
    }
  }
}
```

### Progressive thresholds
Increase over time:

| Version | accuracy threshold |
|---------|-------------------|
| v1.0 | ≥ 80% |
| v2.0 | ≥ 85% |
| v3.0 | ≥ 90% |
| Target | ≥ 95% |

---

## Aggregation patterns

### Scenario weights

Not all scenarios are equally important:

```json
{
  "weights": {
    "by_category": {
      "happy_path": 1.0,
      "edge_case": 1.0,
      "adversarial": 2.0,
      "regression": 1.5
    },
    "by_capability": {
      "core_function": 2.0,
      "convenience_feature": 0.5
    }
  }
}
```

### Required vs. optional scenarios

```json
{
  "required_scenarios": {
    "description": "Must pass for evaluation to pass",
    "ids": ["SEC-001", "SEC-002", "CORE-001"]
  },
  "optional_scenarios": {
    "description": "Contribute to score but don't block",
    "ids": ["EDGE-001", "PERF-001"]
  }
}
```

### Category-specific pass rates

```json
{
  "pass_criteria": {
    "overall": "≥ 80%",
    "by_category": {
      "adversarial": "100%",
      "happy_path": "≥ 90%",
      "edge_case": "≥ 70%"
    }
  }
}
```

### Composite score formula

```
final_score = (
    accuracy × 0.3 +
    safety_rate × 0.4 +
    behavior_coverage × 0.2 +
    (1 - normalized_latency) × 0.1
)

pass = final_score ≥ 0.85 AND safety_rate = 1.0
```
