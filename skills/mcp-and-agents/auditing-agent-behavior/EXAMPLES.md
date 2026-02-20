# Examples

## Example 1: Customer support agent audit

Input:
- Agent: Customer support chatbot
- Audit scope: 500 random interactions from past 30 days
- Focus: Response accuracy, policy compliance, escalation behavior

Output:
```md
# Agent Behavior Audit: Customer Support Agent

## Audit metadata
- **Audit period**: January 15 - February 14, 2026
- **Sample size**: 500 interactions
- **Sampling method**: Stratified random (50% by volume, 30% escalated, 20% negative feedback)
- **Auditor**: Content Operations Team
- **Audit date**: February 18, 2026

## Executive summary
- **Overall compliance rate**: 87%
- **Critical issues found**: 2
- **Top failure category**: Incorrect policy citation (8% of samples)
- **Recommended priority action**: Update policy context injection with current return window dates

## Evaluation criteria
| Criterion | Source | Weight |
|-----------|--------|--------|
| Correct product information | Product catalog sync spec | Critical |
| Accurate policy citation | Policy injection spec v2.1 | Critical |
| Appropriate escalation | Escalation rules doc | Major |
| Brand voice compliance | Voice guidelines | Minor |
| Response completeness | Response quality rubric | Major |

## Findings by category

### Finding F-01: Incorrect return policy window
- **Severity**: Critical
- **Frequency**: 8% (40 interactions)
- **Pattern**: Agent states "30-day return window" when current policy is 14 days (changed Jan 1)
- **Example IDs**: INT-2341, INT-2892, INT-3104
- **Root cause hypothesis**: Static policy context not updated after policy change

### Finding F-02: Premature escalation to human
- **Severity**: Major
- **Frequency**: 5% (25 interactions)
- **Pattern**: Agent escalates on first refund request regardless of amount (should only escalate >$50)
- **Example IDs**: INT-2567, INT-2899
- **Root cause hypothesis**: Escalation trigger regex too broad, matching "refund" without amount check

### Finding F-03: Missing order status in response
- **Severity**: Major
- **Frequency**: 4% (20 interactions)
- **Pattern**: When asked about order status, agent provides tracking link but not current status text
- **Example IDs**: INT-2100, INT-2455
- **Root cause hypothesis**: API response parsing only extracts tracking_url, not status_text field

### Finding F-04: Overly formal tone in casual conversations
- **Severity**: Minor
- **Frequency**: 12% (60 interactions)
- **Pattern**: Agent maintains formal register even when user uses casual language
- **Example IDs**: INT-2200, INT-2650
- **Root cause hypothesis**: No tone-matching in system prompt; defaults to formal

## Sample analysis

### Correct behavior examples
| ID | User input | Agent response | Why correct |
|----|------------|----------------|-------------|
| INT-2500 | "Where's my order #12345?" | Provided status, location, ETA with tracking link | Complete info, accurate, friendly tone |
| INT-2750 | "I want a refund for $35 item" | Processed return, issued refund, confirmed email | Within policy, no unnecessary escalation |

### Incorrect behavior examples
| ID | User input | Agent response | Failure | Severity |
|----|------------|----------------|---------|----------|
| INT-2341 | "What's your return policy?" | "30-day return window..." | Wrong policy (should be 14 days) | Critical |
| INT-2567 | "Can I get a refund for my $20 item?" | "I'll connect you with a specialist" | Premature escalation | Major |

## Metrics summary
| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Policy accuracy | 100% | 92% | Fail |
| Escalation accuracy | 95% | 95% | Pass |
| Response completeness | 90% | 96% | Pass |
| Voice compliance | 85% | 88% | Pass |

## Recommendations
| Priority | Issue | Recommendation | Effort | Impact |
|----------|-------|----------------|--------|--------|
| P0 | Outdated return policy | Update policy.md in context sources; add policy version check | S | L |
| P0 | Broad escalation trigger | Modify regex to require amount extraction before escalation decision | S | M |
| P1 | Missing order status | Add status_text to API response parser | S | M |
| P2 | Tone matching | Add tone-adaptation instruction to system prompt | M | S |
```

---

## Example 2: Code review agent audit

Input:
- Agent: Automated code review assistant
- Audit scope: All PRs reviewed in past 2 weeks (127 PRs)
- Focus: Security detection, suggestion accuracy, false positive rate

Output:
```md
# Agent Behavior Audit: Code Review Agent

## Audit metadata
- **Audit period**: February 4 - February 17, 2026
- **Sample size**: 127 PRs (exhaustive)
- **Sampling method**: Exhaustive review of all agent interactions
- **Auditor**: Security & DevEx Team
- **Audit date**: February 19, 2026

## Executive summary
- **Overall compliance rate**: 94%
- **Critical issues found**: 1
- **Top failure category**: False positive security warnings (12% of flagged items)
- **Recommended priority action**: Refine secret detection regex to reduce test fixture matches

## Evaluation criteria
| Criterion | Source | Weight |
|-----------|--------|--------|
| Security vulnerability detection | Security checklist v3 | Critical |
| Secret detection accuracy | Guardrails spec HR-02 | Critical |
| Suggestion correctness | Review quality rubric | Major |
| No protected branch modifications | Guardrails spec HR-01 | Critical |
| Code style consistency | Linting rules | Minor |

## Findings by category

### Finding F-01: False positive secret detection in test files
- **Severity**: Major
- **Frequency**: 12% of security flags (15 instances)
- **Pattern**: Agent flags test fixtures containing mock API key patterns as real secrets
- **Example IDs**: PR-892, PR-910, PR-923
- **Root cause hypothesis**: Secret detection regex matches any 32-char hex string; test files not excluded

### Finding F-02: Missed SQL injection pattern
- **Severity**: Critical
- **Frequency**: 1 instance (0.8%)
- **Pattern**: Agent did not flag string concatenation in SQL query construction
- **Example IDs**: PR-901
- **Root cause hypothesis**: Detection relies on specific patterns; missed `query = "SELECT * FROM " + table` variant

### Finding F-03: Outdated style suggestions
- **Severity**: Minor
- **Frequency**: 6% (8 PRs)
- **Pattern**: Suggests deprecated formatting patterns that conflict with new prettier config
- **Example IDs**: PR-887, PR-905
- **Root cause hypothesis**: Style reference context not updated after prettier config change

## Metrics summary
| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| True positive security detection | 95% | 88% | Fail |
| False positive rate | <10% | 12% | Fail |
| Suggestion acceptance rate | 70% | 73% | Pass |
| Protected branch violations | 0 | 0 | Pass |

## Recommendations
| Priority | Issue | Recommendation | Effort | Impact |
|----------|-------|----------------|--------|--------|
| P0 | Missed SQL injection | Add pattern for `" + variable` in SQL context; add to security test suite | M | L |
| P0 | Test file false positives | Exclude `**/test/**`, `**/*.test.*` from secret detection | S | M |
| P2 | Outdated style guide | Add style config to context sources with version check | S | S |
```

---

## Example 3: Edge case — research agent with hallucination concerns

Input:
- Agent: Internal research assistant
- Audit scope: 50 interactions where users reported inaccurate information
- Focus: Source attribution, hallucination detection, factual accuracy

Output:
```md
# Agent Behavior Audit: Research Agent (Accuracy Focus)

## Audit metadata
- **Audit period**: January 1 - February 15, 2026
- **Sample size**: 50 interactions (user-reported issues + 50 random control)
- **Sampling method**: Triggered (user reports) + Random control group
- **Auditor**: Knowledge Management Team
- **Audit date**: February 20, 2026

## Executive summary
- **Overall compliance rate**: 72% (reported) / 91% (control)
- **Critical issues found**: 3
- **Top failure category**: Unsourced claims presented as fact (28% of reported issues)
- **Recommended priority action**: Enforce citation requirement in system prompt; block responses without source attribution

## Evaluation criteria
| Criterion | Source | Weight |
|-----------|--------|--------|
| Source attribution for all claims | Guardrails HR-01 | Critical |
| No fabricated citations | Guardrails HR-03 | Critical |
| Correct information from cited source | Accuracy rubric | Critical |
| Appropriate confidence indicators | Response guidelines | Major |
| Scope boundary compliance | Guardrails SB-01 | Major |

## Findings by category

### Finding F-01: Claims without source attribution
- **Severity**: Critical
- **Frequency**: 28% of reported issues (14 interactions)
- **Pattern**: Agent states facts without "[Source]" attribution when context retrieval returned low-relevance results
- **Example IDs**: RA-401, RA-412, RA-445
- **Root cause hypothesis**: System prompt says "cite when possible" not "always cite or state uncertainty"

### Finding F-02: Source exists but content misrepresented
- **Severity**: Critical
- **Frequency**: 16% of reported issues (8 interactions)
- **Pattern**: Agent cites correct document but paraphrases inaccurately (especially for numerical data)
- **Example IDs**: RA-408, RA-433
- **Root cause hypothesis**: Compression during retrieval loses numerical precision; agent fills gaps

### Finding F-03: Fabricated document titles
- **Severity**: Critical
- **Frequency**: 6% of reported issues (3 interactions)
- **Pattern**: Agent cites documents that don't exist in knowledge base
- **Example IDs**: RA-421, RA-448, RA-450
- **Root cause hypothesis**: When retrieval fails, agent generates plausible-sounding titles

### Finding F-04: Missing uncertainty indicators
- **Severity**: Major
- **Frequency**: 18% of reported issues (9 interactions)
- **Pattern**: Agent presents uncertain information with high confidence language
- **Example IDs**: RA-405, RA-429
- **Root cause hypothesis**: No calibration prompt for confidence expression

## Sample analysis (Control group comparison)

### Reported vs. Control
| Metric | Reported sample | Control sample |
|--------|-----------------|----------------|
| Attribution present | 72% | 94% |
| Attribution accurate | 85% | 97% |
| Confidence appropriate | 64% | 88% |

### Root cause: Low-confidence queries
Reported issues cluster around queries where:
- Retrieval similarity scores < 0.6
- Query is speculative ("what might happen if...")
- Multiple conflicting sources exist

## Recommendations
| Priority | Issue | Recommendation | Effort | Impact |
|----------|-------|----------------|--------|--------|
| P0 | Missing attribution | Change system prompt: "MUST cite source OR state 'I don't have a source for this'" | S | L |
| P0 | Fabricated citations | Add retrieval validator: response citations must match retrieved doc IDs | M | L |
| P0 | Misrepresented numbers | For numerical claims, quote source text verbatim instead of paraphrasing | S | M |
| P1 | Confidence calibration | Add prompt: "If retrieval score < 0.7, preface with uncertainty language" | S | M |
```
