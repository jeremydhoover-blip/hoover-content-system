# Examples

## Example 1: File sharing error messages context pack

**Input:**
- Feature: File sharing in document editor
- AI task: Generate error messages for sharing failures
- Target system: GPT-4 class model
- Token budget: ~1500 tokens

**Output:**

```md
# Context Pack: File Sharing Error Messages

## Metadata
- **Feature:** File sharing
- **Version:** 1.0.0
- **Last updated:** 2026-02-20
- **Target AI system:** GPT-4 class
- **Token budget:** ~1500 tokens

## Feature overview
File sharing lets users share documents with others via email invitations or shareable links. Users can set permissions (view, comment, edit) and expiration dates. Sharing can fail due to recipient issues, permission conflicts, or system errors.

## Content generation scope
This context pack enables AI to generate:
- Error messages for sharing failures
- Recovery guidance for each error type

This context pack does NOT cover:
- Success confirmations
- Permission explanations
- Marketing copy

---

## Vocabulary

### Required terms
| Concept | Use this | Never use |
|---------|----------|-----------|
| Link | link | URL, hyperlink |
| Recipient | recipient | user, person, invitee |
| Access | access | permission, privilege |
| Share | share | send, distribute, transmit |

### Definitions
- **recipient:** The person receiving access to the shared file
- **access level:** What the recipient can do (view, comment, or edit)

---

## States

| State | User situation | Tone | Content focus |
|-------|---------------|------|---------------|
| invalid_email | Recipient email address is malformed | Neutral, helpful | Fix the email format |
| recipient_not_found | Email valid but not a registered user | Informative, not alarming | Explain what happens (invite sent) |
| permission_conflict | Recipient already has different access | Clear, solution-focused | Explain conflict, offer resolution |
| quota_exceeded | Sharing limit reached | Empathetic, solution-focused | Explain limit, provide upgrade path |
| network_error | Connection failed during share | Calm, reassuring | Acknowledge issue, encourage retry |

---

## Constraints

### Hard constraints (never violate)
- Never blame the user for the error
- Never expose technical error codes or stack traces
- Always provide a clear recovery action
- Never exceed character limits

### Soft constraints (prefer but can flex)
- Prefer active voice
- Prefer specific over generic guidance
- Keep sentences under 15 words when possible

### Character limits
| Content type | Limit | Rationale |
|--------------|-------|-----------|
| Headline | 50 chars | Fits modal header |
| Body | 120 chars | Fits two lines in standard modal |
| CTA | 25 chars | Fits button width |

### Prohibited content
- Never: Use "Error" or "Failed" as the first word
- Never: Use technical terms (API, timeout, 500, null)
- Never: Use exclamation points in error messages
- Never: Say "please" more than once per message

---

## Tone guidance

### Default tone
Calm, helpful, confident. We had a problem but we know how to fix it.

### Tone by state
| State | Tone adjustment |
|-------|-----------------|
| network_error | More reassuring — not their fault |
| quota_exceeded | More empathetic — acknowledge limitation |
| invalid_email | Neutral — straightforward correction |

### Tone boundaries
- Never sound: Frustrated, apologetic to excess, robotic
- Always sound: Competent, helpful, human

---

## Examples

### Example 1: Invalid email
**State:** invalid_email
**Input:** User entered "john@" in recipient field

✓ **Good:**
```
Headline: Check the email address
Body: This doesn't look like a complete email. Add the domain (like @gmail.com).
CTA: Got it
```
**Why it works:** Identifies the specific problem (incomplete), provides concrete fix (add domain with example), uses neutral tone without blame.

✗ **Bad:**
```
Headline: Invalid email format
Body: The email address you entered is invalid. Please enter a valid email address.
CTA: OK
```
**Why it fails:** "Invalid" is technical and judgmental. "Please enter a valid email" is circular—doesn't explain what's wrong. "OK" is not an action.

---

### Example 2: Network error
**State:** network_error
**Input:** Share request failed due to connectivity

✓ **Good:**
```
Headline: Couldn't share right now
Body: Check your internet connection and try again. Your sharing settings are saved.
CTA: Try again
```
**Why it works:** Acknowledges failure without alarm, provides recovery action, reassures that settings aren't lost.

✗ **Bad:**
```
Headline: Network error
Body: Failed to connect to server. Error code: ETIMEDOUT.
CTA: Retry
```
**Why it fails:** "Network error" exposes technical framing. Error code is meaningless to users. No reassurance about data.

---

### Example 3: Quota exceeded
**State:** quota_exceeded
**Input:** Free tier user hit sharing limit

✓ **Good:**
```
Headline: You've reached your sharing limit
Body: Free accounts can share with up to 5 people. Upgrade for unlimited sharing.
CTA: See plans
```
**Why it works:** Clear about the limit, explains the constraint, offers upgrade path without being pushy.

✗ **Bad:**
```
Headline: Sharing failed
Body: You have exceeded your sharing quota. Please upgrade to continue.
CTA: Upgrade now
```
**Why it fails:** "Failed" is unnecessarily negative. "Exceeded quota" is business language. "Please upgrade" is demanding.

---

## Edge cases

| Scenario | Handling |
|----------|----------|
| Multiple errors at once | Show most actionable error first (email validation before permission conflict) |
| Recipient is the owner | "This person already owns the file" — don't offer to change access |
| Self-sharing | "You already have access to this file" — friendly, not mocking |
| Expired link when sharing | "This link has expired. Create a new link to share." |
```

---

## Example 2: Compact context pack for notification content

**Input:**
- Feature: Mobile push notifications
- AI task: Generate notification copy
- Target system: Smaller model with token limits
- Token budget: ~500 tokens

**Output:**

```md
# Context: Push Notifications

## Scope
Generate: Push notification titles and bodies
Feature: Mobile alerts for account activity, reminders, and updates

## Terms
Use: notification, reminder, update
Never: alert (too alarming), ping, push

## States
- activity: Someone interacted with user's content → tone: informative, encouraging
- reminder: User has pending action → tone: helpful, not nagging
- update: Something changed in their account → tone: neutral, clear
- urgent: Security or billing issue → tone: direct, calm, action-focused

## Constraints
- Hard: Title ≤50chars; Body ≤100chars; no ALL CAPS; no exclamation points
- Hard: Always include who/what/action in activity notifications
- Soft: Front-load key info (may be truncated)
- Never: "Alert!", "Warning!", "Urgent!" in title; clickbait; vague CTAs

## Tone
Default: Friendly, brief, useful
Never: Spammy, demanding, mysterious

## Examples
**Activity (good):** 
Title: "Sarah commented on your doc"
Body: "Marketing Plan — 'Great ideas here!'"

**Activity (bad):**
Title: "New comment!" — too vague, who? where?
Body: "Check it out now!" — no useful info

**Reminder (good):**
Title: "Finish your draft?"
Body: "Marketing Plan is 80% complete. Pick up where you left off."

**Reminder (bad):**
Title: "Don't forget!!" — nagging, exclamation
Body: "You have unfinished work" — vague, guilt-inducing

**Urgent (good):**
Title: "Action needed: verify your email"
Body: "We noticed a sign-in from a new device. Verify it's you."

**Urgent (bad):**
Title: "SECURITY ALERT" — alarming, all caps
Body: "Your account may be compromised!" — panic-inducing
```

---

## Example 3: Edge case — context pack for regulated content

**Input:**
- Feature: Financial transaction confirmations
- AI task: Generate confirmation messages for money transfers
- Constraint: Must comply with financial disclosure requirements
- Token budget: ~1200 tokens

**Output:**

```md
# Context Pack: Transaction Confirmations (Regulated)

## Metadata
- **Feature:** Money transfers
- **Version:** 1.0.0
- **Last updated:** 2026-02-20
- **Target AI system:** GPT-4 class
- **Token budget:** ~1200 tokens
- **Regulatory note:** Content must include required disclosures per compliance review

## Feature overview
Money transfers let users send funds to other users or external bank accounts. All transfers require confirmation before execution. Messages must include transaction details and cannot be misleading about timing or fees.

## Content generation scope
This context pack enables AI to generate:
- Pre-transfer confirmation messages
- Post-transfer success confirmations

This context pack does NOT cover:
- Error messages (separate context pack)
- Marketing or promotional content
- Fee explanations (must use approved legal copy)

---

## Regulatory constraints (non-negotiable)

### Required disclosures
Every confirmation must include:
- Exact amount being transferred
- Recipient identifier (name or account ending)
- Transfer timing (when funds arrive)
- Fee amount (if any)

### Prohibited claims
- Never claim "instant" unless transfer is immediate
- Never hide or minimize fees
- Never promise guaranteed delivery times without qualifier
- Never use "free" if any fees apply anywhere in the flow

### Approved phrases (use exactly)
| Concept | Approved language |
|---------|-------------------|
| Timing | "typically arrives within [X]" or "arrives by [date]" |
| Fees | "Fee: $X" or "No fee for this transfer" |
| Disclaimer | "Transfer times may vary" |

---

## States

| State | Situation | Required elements |
|-------|-----------|-------------------|
| confirm_internal | Sending to another user | Amount, recipient name, timing, fee |
| confirm_external | Sending to bank account | Amount, account ending, timing, fee, bank name |
| success_internal | Transfer completed to user | Amount, recipient name, confirmation number |
| success_external | Transfer initiated to bank | Amount, account ending, expected arrival, confirmation number |

---

## Character limits
| Content type | Limit | Rationale |
|--------------|-------|-----------|
| Headline | 40 chars | Confirmation modal header |
| Body | 200 chars | Must fit required disclosures |
| Fine print | No limit | Regulatory disclosures as needed |

---

## Examples

### Example 1: Internal transfer confirmation
**State:** confirm_internal
**Input:** $50 to @sarah, no fee, instant

✓ **Good:**
```
Headline: Send $50 to Sarah?
Body: This transfer is instant with no fee. Sarah will receive $50 in their account balance.
CTA: Send $50
```
**Why it works:** Amount in headline, timing stated, fee addressed, clear CTA with amount.

✗ **Bad:**
```
Headline: Confirm transfer
Body: You're sending money to Sarah. Continue?
CTA: Send
```
**Why it fails:** Missing amount in body, no timing, no fee disclosure, CTA doesn't confirm amount.

---

### Example 2: External transfer confirmation
**State:** confirm_external
**Input:** $500 to bank account ending 4829, $1.50 fee, arrives in 1-3 days

✓ **Good:**
```
Headline: Send $500 to account •••4829?
Body: $500 will be sent to your Chase account ending in 4829. Fee: $1.50. Typically arrives within 1-3 business days.
Fine print: Transfer times may vary.
CTA: Send $501.50
```
**Why it works:** All required disclosures present, CTA includes total with fee, timing uses approved language.

✗ **Bad:**
```
Headline: Transfer $500?
Body: We'll send your money to your bank. Should arrive soon!
CTA: Send
```
**Why it fails:** Missing account identifier, no fee disclosure, "soon" violates timing requirement, CTA missing total.

---

## Edge cases

| Scenario | Handling |
|----------|----------|
| Fee waived (promotion) | "Fee: $0 (waived)" — explicitly show the waiver |
| First-time recipient | Add "First transfer to this account" in body |
| High-value transfer (>$1000) | Add "Large transfer" label, may require additional verification |
| Weekend/holiday transfer | "Typically arrives within 1-3 business days (may be longer due to [holiday])" |
```
