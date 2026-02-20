# Enforcement Patterns

## Table of contents
- [Enforcement mechanisms](#enforcement-mechanisms)
- [Detection strategies](#detection-strategies)
- [Response actions](#response-actions)
- [Implementation examples](#implementation-examples)

---

## Enforcement mechanisms

### Pre-execution checks
Validate before the agent acts.

| Mechanism | Use when | Implementation |
|-----------|----------|----------------|
| Input validation | Blocking malicious or out-of-scope requests | Pattern matching, classification, allowlist |
| Permission check | Verifying user/agent has required access | Role lookup, token validation |
| Context validation | Ensuring required context is present | Schema validation, required field check |
| Rate limiting | Preventing resource exhaustion | Counter with time window |

### Runtime checks
Monitor during execution.

| Mechanism | Use when | Implementation |
|-----------|----------|----------------|
| Output scanning | Preventing sensitive data exposure | Regex patterns, ML classifiers |
| Action interception | Requiring confirmation for high-risk ops | Approval workflow, confirmation prompt |
| Progress monitoring | Detecting runaway or stuck processes | Timeout, step counter, resource monitor |
| Boundary enforcement | Keeping agent within defined scope | Capability flags, API restrictions |

### Post-execution checks
Validate after action completes.

| Mechanism | Use when | Implementation |
|-----------|----------|----------------|
| Audit logging | Tracking all constraint-relevant events | Structured log with constraint ID |
| Output validation | Verifying output meets requirements | Schema check, length limits, format validation |
| Side-effect verification | Confirming expected state changes | State comparison, diff check |
| Compliance reporting | Demonstrating adherence | Periodic summary, alert aggregation |

---

## Detection strategies

### Pattern-based detection
For known, well-defined violations.

```
Detector: regex / keyword / structured pattern
Applies to: Secrets, PII, prohibited terms, unsafe commands
Limitations: Misses novel patterns, may false-positive
```

**Secret patterns** (examples):
- API keys: `[A-Za-z0-9]{32,}`
- AWS keys: `AKIA[0-9A-Z]{16}`
- JWT: `eyJ[A-Za-z0-9_-]+\.eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+`

### Classification-based detection
For fuzzy or context-dependent violations.

```
Detector: ML classifier / embedding similarity
Applies to: Tone violations, off-topic content, sentiment
Limitations: Requires training data, may be inconsistent
```

### Threshold-based detection
For quantitative constraints.

```
Detector: Counter / accumulator / gauge
Applies to: Rate limits, length limits, cost limits
Limitations: May allow burst violations, requires reset logic
```

### State-based detection
For workflow and sequence constraints.

```
Detector: State machine / workflow tracker
Applies to: Required confirmations, multi-step processes
Limitations: Complexity grows with state count
```

---

## Response actions

### Blocking responses
For hard constraints—stop immediately.

| Action | Effect | Use when |
|--------|--------|----------|
| Reject | Return error, take no action | Clear violation, no valid alternative |
| Sanitize | Remove violating content, proceed | Violation in output, action is valid |
| Substitute | Replace violating action with safe default | Safe fallback exists |

### Escalating responses
For soft constraints—pause and seek guidance.

| Action | Effect | Use when |
|--------|--------|----------|
| Confirm | Ask user to approve before proceeding | User has authority to override |
| Route | Transfer to human handler | Exceeds agent authority |
| Defer | Queue for later with notification | Time-sensitive but not urgent |

### Informing responses
For all constraints—maintain transparency.

| Action | Effect | Use when |
|--------|--------|----------|
| Explain | Tell user what happened and why | User-facing constraint |
| Log | Record event for audit | All constraint triggers |
| Alert | Notify operators | Security or safety constraints |

---

## Implementation examples

### Example: Secret detection with blocking

```
Constraint: HR-02 (no secrets in output)
Detection: Pre-output regex scan

Patterns:
  - /AKIA[0-9A-Z]{16}/ → AWS access key
  - /[a-f0-9]{64}/ → Hex token (64 char)
  - /-----BEGIN .* KEY-----/ → PEM key

Response:
  - Block: Do not send output
  - Log: { constraint: "HR-02", pattern: "<matched>", timestamp }
  - User message: "I found content that looks like a secret. I've removed it from my response. Please review the source material."
```

### Example: Escalation for high-value action

```
Constraint: SR-01 (refunds >$50 require human)
Detection: Parse dollar amount from user request

Trigger: amount > 50.00

Response:
  - Pause: Do not commit action
  - Message to user: "Refunds over $50 require manager approval. I've sent this request for review. You'll receive confirmation within 2 hours."
  - Route: Create ticket in support queue with context
  - Log: { constraint: "SR-01", amount, user_id, timestamp }

Resume:
  - Manager approves via ticket interface
  - Agent receives approval token
  - Agent completes action with audit trail
```

### Example: Rate limiting with backoff

```
Constraint: RL-01 (max 100 API calls per minute)
Detection: Counter with sliding window

State:
  - call_count: integer
  - window_start: timestamp

On each call:
  - If now - window_start > 60s: reset counter
  - Increment call_count
  - If call_count > 100: trigger

Response:
  - Block: Delay execution
  - Message: "I'm processing your request, but I need to pace my queries. This may take a moment."
  - Backoff: Wait (call_count - 100) * 2 seconds, max 60s

Log: { constraint: "RL-01", count: call_count, wait_time, timestamp }
```

### Example: Scope boundary with fallback

```
Constraint: SB-01 (coding questions only)
Detection: Topic classifier on user input

Categories:
  - "coding" → proceed
  - "general_knowledge" → soft decline
  - "medical|legal|financial" → hard decline

Response (general_knowledge):
  - Message: "I'm designed to help with coding questions. For general questions, you might try [alternative]. Is there a coding topic I can help with?"
  - Log: { constraint: "SB-01", category, timestamp }

Response (medical|legal|financial):
  - Message: "I can't provide [category] advice. Please consult a qualified [professional type]."
  - Log: { constraint: "SB-01", category, severity: "hard", timestamp }
  - Do not attempt partial answer
```
