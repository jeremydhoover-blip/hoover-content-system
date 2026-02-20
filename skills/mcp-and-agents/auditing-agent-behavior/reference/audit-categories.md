# Audit Categories

## Table of contents
- [Behavior categories](#behavior-categories)
- [Severity classification](#severity-classification)
- [Common failure patterns](#common-failure-patterns)
- [Audit checklist by agent type](#audit-checklist-by-agent-type)

---

## Behavior categories

### Correctness
Agent provides accurate, factual responses.

| Sub-category | Description | Indicators |
|--------------|-------------|------------|
| Factual accuracy | Information matches authoritative sources | User reports, fact-check comparison |
| Computational accuracy | Calculations and reasoning are correct | Manual verification, test cases |
| Source fidelity | Cited sources actually contain claimed info | Source lookup, quote comparison |
| Temporal accuracy | Time-sensitive info is current | Date verification, staleness check |

### Compliance
Agent follows defined rules and constraints.

| Sub-category | Description | Indicators |
|--------------|-------------|------------|
| Guardrail adherence | Hard constraints never violated | Constraint trigger logs |
| Scope compliance | Stays within defined boundaries | Out-of-scope response detection |
| Policy compliance | Follows organizational policies | Policy checklist verification |
| Escalation compliance | Routes appropriately when required | Escalation trigger analysis |

### Quality
Agent responses meet quality standards.

| Sub-category | Description | Indicators |
|--------------|-------------|------------|
| Completeness | Addresses all parts of user request | Coverage analysis |
| Clarity | Response is understandable | Readability metrics, user follow-ups |
| Conciseness | No unnecessary verbosity | Length analysis, signal-to-noise |
| Actionability | User can act on the response | Task completion rate |

### Safety
Agent avoids harmful outputs.

| Sub-category | Description | Indicators |
|--------------|-------------|------------|
| No harmful content | Avoids offensive, dangerous content | Content classifier results |
| No data leakage | Doesn't expose sensitive information | PII/secret detection |
| No unauthorized actions | Doesn't exceed permissions | Action log analysis |
| Appropriate uncertainty | Expresses confidence appropriately | Calibration analysis |

### User experience
Agent interaction is positive.

| Sub-category | Description | Indicators |
|--------------|-------------|------------|
| Responsiveness | Appropriate response time | Latency metrics |
| Tone | Matches expected voice | Voice checklist |
| Helpfulness | Actually assists with user goal | Task success rate, user feedback |
| Recovery | Handles errors gracefully | Error interaction analysis |

---

## Severity classification

### Critical
Immediate action required. Stop or fix before continuing.

- Safety violations (harmful output, data leakage)
- Hard guardrail breaches
- Factual errors with significant consequences
- Security vulnerabilities
- Legal/compliance violations

### Major
Action required within sprint. Significant user impact.

- Soft guardrail breaches without escalation
- Consistent accuracy issues in specific domain
- Poor handling of common use cases
- Misleading confidence in uncertain situations
- Incomplete responses to standard queries

### Minor
Action recommended. Low immediate impact.

- Voice/tone inconsistencies
- Suboptimal but correct responses
- Occasional unnecessary verbosity
- Style guideline deviations
- Minor formatting issues

---

## Common failure patterns

### The confident hallucination
Agent presents fabricated information with high confidence.

```
Symptoms:
- Citations that don't exist
- Facts that contradict authoritative sources
- Plausible-sounding but incorrect details

Root causes:
- Missing uncertainty expression training
- Retrieval failures without fallback
- Pressure to "always be helpful"

Audit approach:
- Verify citations against source material
- Cross-check facts with authoritative sources
- Compare confidence language with retrieval scores
```

### The scope creep
Agent answers questions outside defined boundaries.

```
Symptoms:
- Provides advice in prohibited domains
- Attempts tasks beyond capabilities
- Makes commitments beyond authority

Root causes:
- Scope definition not in context
- Helpful-by-default overrides boundaries
- User persistence overcomes soft limits

Audit approach:
- Test boundary queries
- Check for scope-related escalations
- Review interactions where agent says "yes" to novel requests
```

### The broken telephone
Agent distorts information during transformation.

```
Symptoms:
- Summaries that miss key points
- Paraphrases that change meaning
- Numbers that drift from source

Root causes:
- Compression losing precision
- Context truncation
- Abstractive summarization errors

Audit approach:
- Compare outputs to source verbatim
- Track numerical accuracy specifically
- Check key terms preservation
```

### The premature escalation
Agent escalates when it could resolve.

```
Symptoms:
- High escalation rate for resolvable queries
- Escalation on trigger words regardless of context
- User frustration with handoffs

Root causes:
- Overly sensitive trigger rules
- Lack of confidence in own capabilities
- Missing context for resolution

Audit approach:
- Review escalated interactions for resolvability
- Compare escalation triggers with outcomes
- Measure human agent "return to bot" rate
```

### The stale context
Agent uses outdated information.

```
Symptoms:
- References old policies or products
- Contradicts recent changes
- Users correct agent frequently

Root causes:
- Static context not refreshed
- Cache TTL too long
- Update propagation failure

Audit approach:
- Compare agent knowledge with current truth
- Check context timestamps
- Test recently changed information
```

---

## Audit checklist by agent type

### Customer support agent
- [ ] Policy citations match current policies
- [ ] Refund/credit amounts within authority
- [ ] Escalation triggers appropriate
- [ ] Personal data handling correct
- [ ] Tone matches brand voice
- [ ] Promises align with actual capabilities

### Code assistant
- [ ] Code suggestions compile/run
- [ ] Security issues detected accurately
- [ ] No secrets in output
- [ ] Respects file boundaries
- [ ] Suggestions follow project style
- [ ] Dependencies exist and are correct

### Research assistant
- [ ] All claims have attribution
- [ ] Citations are real and correct
- [ ] Numerical accuracy preserved
- [ ] Uncertainty expressed appropriately
- [ ] Scope boundaries respected
- [ ] Conflicting sources presented fairly

### Writing assistant
- [ ] Style guidelines followed
- [ ] Factual claims accurate
- [ ] No plagiarism
- [ ] Appropriate for audience
- [ ] Complete response to prompt
- [ ] No harmful content generated
