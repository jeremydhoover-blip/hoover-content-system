# Examples

## Example 1: Form field cognitive load audit

**Input**: Analyze cognitive load in a shipping address form.

**Output**:
```md
## Cognitive load audit: Shipping address form

**Primary task**: Enter delivery address
**User context**: Expertise: Mixed | Frequency: Occasional | Stress: Medium (checkout pressure)

### Decision point inventory

| Decision | Type | Current load source | Severity |
|----------|------|---------------------|----------|
| Country selection | Intrinsic | Must know shipping destination | Low |
| Address line 1 vs 2 | Extraneous | Unclear what goes where | Medium |
| State format | Extraneous | Free text vs dropdown mismatch | Medium |
| Zip code format | Extraneous | No format hint, validation after submit | High |
| "Same as billing" checkbox | Germane | One decision saves re-entry | Low (beneficial) |

### Load sources by type

**Intrinsic load** (unavoidable):
- Country selection: Required for shipping logistics
- Address entry: Core task—can't be eliminated

**Extraneous load** (target for elimination):
- Address line 1/2 split: Users unsure what goes where
- State text field: Users must type exact format, risk validation errors
- Zip code validation: Only shows error after submission attempt

**Germane load** (preserve):
- "Same as billing" checkbox: Reduces effort for repeat purchasers

### Total load assessment
- Decisions required: 7 fields + 1 checkbox
- Information items to remember: Own address (low)
- Steps to completion: 8 fields → submit
- Estimated cognitive demand: Medium (reducible to Low)
```

---

## Example 2: Specific reduction recommendation

**Input**: Reduce cognitive load in a permission request dialog.

**Output**:
```md
## Reduction: Permission request clarity

**Load source**: Permission dialog uses technical language without explaining benefit
**Load type**: Extraneous
**Severity**: High

**Current state**:
> "App wants to access your location. Allow / Don't Allow"

**Problem**: User must decide without understanding benefit. No information about how data is used. Binary choice without context.

**Reduction strategy**: Progressive disclosure + Clarify benefit

**Recommended change**:
- Before: "App wants to access your location. Allow / Don't Allow"
- After: 
  > "See delivery times for your area
  > 
  > We'll use your location to show accurate delivery estimates. Your location isn't stored.
  > 
  > [Enable location] [Not now]"

**Load reduction**:
- Eliminates: Guessing why permission is needed
- Eliminates: Uncertainty about data usage
- Adds: Benefit-focused framing reduces risk assessment effort

**Risk check**: No—essential decision preserved, user still chooses. Added information helps informed decision.
```

---

## Example 3: Choice reduction

**Input**: Reduce cognitive load in a settings menu with 15 options.

**Output**:
```md
## Reduction: Settings menu choice overload

**Load source**: Flat list of 15 settings with equal visual weight
**Load type**: Extraneous
**Severity**: High

**Current state**:
Settings screen shows:
1. Account, 2. Password, 3. Two-factor auth, 4. Notifications, 5. Email preferences, 6. Language, 7. Timezone, 8. Privacy, 9. Data export, 10. Connected apps, 11. Theme, 12. Font size, 13. Sounds, 14. Help, 15. About

**Problem**: 15 items exceeds 7±2 chunking threshold. Users must scan all items to find target. No hierarchy indicates importance or frequency.

**Reduction strategy**: Chunking + Smart defaults + Progressive disclosure

**Recommended change**:
- Before: Flat list of 15 items
- After: Grouped categories

  > **Account** (3)
  > Profile, Password, Two-factor auth
  > 
  > **Preferences** (5)
  > Notifications, Language, Theme, Sounds
  > 
  > **Privacy & Data** (3)
  > Privacy, Data export, Connected apps
  > 
  > **Help** (2)
  > Help center, About

**Load reduction**:
- Items to scan: 15 → 4 categories
- Memory demand: None (recognition-based navigation)
- Frequent settings accessible in 2 taps; rare settings still available

**Risk check**: No—all settings preserved, just restructured. Popular settings (Notifications, Theme) remain easily accessible.
```

---

## Example 4: Edge case — High-stress context

**Input**: Reduce cognitive load for error recovery during payment failure.

**Output**:
```md
## Cognitive load audit: Payment failure recovery

**Primary task**: Complete purchase after payment error
**User context**: Expertise: Variable | Frequency: Rare (error state) | Stress: HIGH (money, uncertainty)

### Decision point inventory

| Decision | Type | Current load source | Severity |
|----------|------|---------------------|----------|
| Understand what happened | Intrinsic | Error occurred—must acknowledge | Medium |
| Decide how to fix | Extraneous | Multiple options, unclear which applies | HIGH |
| Re-enter payment info | Intrinsic | Payment must be collected | Medium |
| Worry about double-charge | Extraneous | No confirmation of transaction state | HIGH |

### High-stress adjustments

**Principles for high-stress contexts**:
1. Reduce reading—users scan, don't read
2. Eliminate ambiguity—state exactly what happened
3. Provide single clear action—don't offer choices
4. Reassure about consequences—address fears explicitly

**Current state (high load)**:
> "An error occurred. Please try again or contact support."

**Reduced load version**:
> "Payment didn't go through
> 
> Your card wasn't charged. Try again with the same card, or use a different payment method.
> 
> [Try again] [Use different card]
> 
> Your cart is saved. You can also complete this order later."

### Load sources eliminated
- "What happened?": Explicitly stated (payment failed)
- "Was I charged?": Explicitly stated (no)
- "What do I do?": Two clear options
- "What if I leave?": Cart is saved

**Risk check**: No essential information lost. Added context reduces anxiety and decision paralysis.
```

---

## Example 5: Edge case — Missing context

**Input**: "Make this less confusing."

**Output**:
```md
To reduce cognitive load, I need:

1. **What screen or flow?**
   - [ ] Specific screen (share screenshot or description)
   - [ ] Multi-step flow (describe steps)
   - [ ] Entire feature area

2. **What's confusing?**
   - [ ] Users don't know what to do next
   - [ ] Users make wrong choices
   - [ ] Users ask support for help
   - [ ] Specific user feedback (share quotes)

3. **User context:**
   - Expertise level: [Novice / Intermediate / Expert / Mixed]
   - Task frequency: [First-time / Occasional / Daily]
   - Stress level: [Low / Medium / High]

4. **Constraints:**
   - Can content be restructured?
   - Can options be removed?
   - Are there legal/compliance requirements?

Share the specific content or screenshot to proceed with analysis.
```
