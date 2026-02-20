# Examples

## Example 1: Adding a missing state based on support tickets

**Input:**
- Existing context pack: File sharing feature (v1.2.0)
- Feedback: 47 support tickets in Q4 mention users confused when share link expires but file still exists
- Feedback type: Gap

**Output:**

```md
# Context Update Record

## Metadata
- **Context pack:** file-sharing
- **Previous version:** 1.2.0
- **New version:** 1.3.0
- **Update date:** 2026-02-20
- **Update author:** Content Design

## Feedback sources
| Source type | Reference | Date received |
|-------------|-----------|---------------|
| support-ticket | SUPPORT-2024-Q4-sharing-cluster | 2026-01-15 |

## Changes

### Change 1: Add "link-expired-file-exists" state
- **Affected section:** states
- **Feedback type:** gap
- **Change type:** additive

**Before:**
States: active, expired, revoked, deleted

**After:**
States: active, link-expired-file-exists, fully-expired, revoked, deleted

**Rationale:**
47 support tickets indicate users expect to re-share files after link expiration. Current state model conflates link expiration with file unavailability. New state distinguishes "link expired but file still shareable" from "file no longer available."

**Conflicts identified:** Requires renaming "expired" to "fully-expired" for clarity.

---

### Change 2: Update error taxonomy for expired link state
- **Affected section:** error-taxonomy
- **Feedback type:** expansion
- **Change type:** additive

**Before:**
Expired state errors: "This link has expired."

**After:**
Link-expired-file-exists errors: "This link has expired. The owner can create a new link."
Fully-expired errors: "This file is no longer available."

**Rationale:**
Differentiated messaging supports the new state model and reduces support ticket volume.

**Conflicts identified:** None.

---

## Changelog entry
- 1.3.0: Add link-expired-file-exists state, rename expired to fully-expired, expand error taxonomy for expiration scenarios

## Validation checklist
- [x] All changes traceable to feedback source
- [x] No terminology conflicts introduced
- [x] Affected states verified against state map
- [x] Version incremented correctly
- [x] Changelog updated
```

---

## Example 2: Correcting vocabulary based on user research

**Input:**
- Existing context pack: Notification preferences (v2.0.1)
- Feedback: Usability study shows 8/10 participants confused "mute" with "block"
- Feedback type: Correction

**Output:**

```md
# Context Update Record

## Metadata
- **Context pack:** notification-preferences
- **Previous version:** 2.0.1
- **New version:** 2.1.0
- **Update date:** 2026-02-20
- **Update author:** Content Design

## Feedback sources
| Source type | Reference | Date received |
|-------------|-----------|---------------|
| user-research | UR-2026-02-notif-study | 2026-02-10 |

## Changes

### Change 1: Replace "mute" with "pause notifications"
- **Affected section:** vocabulary
- **Feedback type:** correction
- **Change type:** modifying

**Before:**
- mute: Temporarily stop notifications from a conversation

**After:**
- pause notifications: Temporarily stop notifications from a conversation (does not affect the sender's ability to message you)

**Rationale:**
8/10 usability study participants interpreted "mute" as blocking the sender. "Pause notifications" aligns with user mental model and differentiates from blocking behavior.

**Conflicts identified:** UI strings using "mute" require update. Engineering ticket filed.

---

## Changelog entry
- 2.1.0: Replace "mute" with "pause notifications" in vocabulary to resolve user confusion with blocking

## Validation checklist
- [x] All changes traceable to feedback source
- [x] No terminology conflicts introduced
- [x] Affected states verified against state map
- [x] Version incremented correctly
- [x] Changelog updated
```

---

## Example 3: Edge case — conflicting feedback from different sources

**Input:**
- Existing context pack: Payment methods (v3.1.0)
- Feedback A: PM requests adding "wallet" terminology for stored payment methods
- Feedback B: User research shows "wallet" confuses users who expect cryptocurrency features
- Feedback type: Conflict

**Output:**

```md
# Feedback Conflict Report

## Conflict ID: payment-methods-wallet-terminology

**Feedback A:**
- Source: PM input (PRD-2026-02-payments)
- States: Use "wallet" to describe stored payment methods for brand alignment

**Feedback B:**
- Source: User research (UR-2026-01-payment-study)
- States: 6/10 participants associated "wallet" with cryptocurrency; causes confusion

**Resolution options:**
1. Use "wallet" with contextual qualifier: "Payment wallet" — addresses brand goal while reducing crypto association
2. Use "saved payment methods" — neutral, tested well in research, but deviates from brand preference
3. A/B test both terms before committing to context pack

**Recommended resolution:** Option 3
**Rationale:** Conflicting signals from brand strategy and user research warrant validation before permanent context change. A/B test with conversion metrics will provide evidence-based resolution.

---

# Context Update Record (pending resolution)

## Metadata
- **Context pack:** payment-methods
- **Previous version:** 3.1.0
- **New version:** 3.1.1-beta
- **Update date:** 2026-02-20
- **Update author:** Content Design

## Feedback sources
| Source type | Reference | Date received |
|-------------|-----------|---------------|
| pm-input | PRD-2026-02-payments | 2026-02-01 |
| user-research | UR-2026-01-payment-study | 2026-01-20 |

## Changes

### Change 1: Add terminology experiment flag
- **Affected section:** vocabulary
- **Feedback type:** expansion
- **Change type:** additive

**Before:**
- saved cards: Credit or debit cards stored for future use

**After:**
- saved cards: Credit or debit cards stored for future use
- [EXPERIMENT] wallet vs. saved payment methods: Under A/B test through 2026-03-15

**Rationale:**
Conflicting feedback requires experimental validation before permanent vocabulary change.

**Conflicts identified:** Documented above.

---

## Changelog entry
- 3.1.1-beta: Add experimental vocabulary flag for wallet terminology pending A/B test results

## Validation checklist
- [x] All changes traceable to feedback source
- [x] No terminology conflicts introduced
- [x] Affected states verified against state map
- [x] Version incremented correctly
- [x] Changelog updated
```
