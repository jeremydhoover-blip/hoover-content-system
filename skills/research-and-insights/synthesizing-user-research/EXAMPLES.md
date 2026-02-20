# Examples

## Example 1: Usability test synthesis

**Input:**
- Method: Moderated usability testing
- Participants: 8 users (4 new, 4 experienced)
- Task: Complete account settings changes
- Raw data: Session recordings, notes, task completion rates

**Output:**

```md
# Account Settings Usability Test Synthesis

## Executive summary

Users struggle to find and complete settings changes, with 6 of 8 participants failing to locate privacy settings without help. Navigation labels don't match user mental models, and the settings hierarchy is too deep.

### Key findings
1. "Privacy" settings expected under "Security" — 6 of 8 looked there first
2. Three-level navigation is too deep — users lose context by level 2
3. Save/Cancel buttons below fold cause uncertainty about state

### Top recommendations
1. Move privacy settings under Security or create combined section
2. Flatten settings hierarchy to maximum 2 levels
3. Add sticky header showing current location and save state

---

## Methodology

**Method:** Moderated remote usability testing
**Participants:** 8 participants (4 new users <3 months, 4 experienced users >1 year)
**Recruitment criteria:** Active users who have changed at least one setting
**Sessions:** Jan 15-19, 2024, 30-45 minutes each
**Limitations:** All participants English-speaking US users; no mobile testing

### Participant breakdown

| Segment | Count | Avg. account age |
|---------|-------|------------------|
| New users | 4 | 6 weeks |
| Experienced users | 4 | 2.3 years |

### Task completion

| Task | Success rate | Avg. time |
|------|--------------|-----------|
| Change notification preferences | 87% (7/8) | 1:45 |
| Update privacy settings | 25% (2/8) | 4:30 |
| Add payment method | 100% (8/8) | 0:55 |

---

## Findings

### Finding 1: Privacy settings are hidden from mental model

**Observation:** When asked to change privacy settings, 6 of 8 participants clicked "Security" first.

**Frequency:** 6 of 8 participants (75%)

**Evidence:**
> "Privacy and security are the same thing to me. I'd look under Security for anything related to who can see my stuff." — P2, New user

> "I've been using this app for two years and I still don't know where Privacy is. I just assumed it was under Security." — P6, Experienced user

**Insight:** Users group privacy and security conceptually. The current separation creates a findability problem that experience doesn't solve.

**Recommendation:** Combine Privacy and Security into one section, or add "Privacy" as a visible option within Security.

---

### Finding 2: Three-level navigation causes context loss

**Observation:** After navigating two levels deep, 5 of 8 participants couldn't recall how to return to the main settings page.

**Frequency:** 5 of 8 participants (62%)

**Evidence:**
> "Wait, how do I get back to the main settings? Is there a back button somewhere?" — P3, New user

> "I feel lost. What section am I even in right now?" — P8, Experienced user

**Insight:** Deep hierarchy without persistent navigation breadcrumbs creates disorientation. Users focus on the task and lose spatial awareness.

**Recommendation:** Flatten to 2 levels maximum. Add persistent breadcrumb showing current location.

---

### Finding 3: Save state uncertainty

**Observation:** 4 of 8 participants were unsure whether changes had saved after making edits.

**Frequency:** 4 of 8 participants (50%)

**Evidence:**
> "Did that save? I didn't see anything happen." — P1, New user

> "I usually click Save three times just to be sure." — P7, Experienced user

**Insight:** The Save button is below the fold on most screens, and there's no confirmation message. Users develop anxiety and compensating behaviors.

**Recommendation:** Add inline save confirmation. Consider auto-save with status indicator.

---

## Recommendations summary

| Priority | Recommendation | Supporting findings | Effort |
|----------|---------------|---------------------|--------|
| High | Combine Privacy/Security sections | Finding 1 | Medium |
| High | Flatten navigation to 2 levels | Finding 2 | High |
| Medium | Add save confirmation | Finding 3 | Low |
| Medium | Add persistent breadcrumbs | Finding 2 | Low |

---

## Appendix

### Dissenting observation

P5 (experienced user) found privacy settings immediately, noting they had "memorized where everything is." This confirms the issue is discoverability, not impossibility — users can learn, but shouldn't have to.
```

---

## Example 2: Interview synthesis

**Input:**
- Method: Semi-structured interviews
- Participants: 12 users across 3 customer segments
- Focus: Understanding feature adoption barriers
- Raw data: Interview transcripts

**Output:**

```md
# Feature Adoption Research Synthesis

## Executive summary

Non-adoption of the collaboration feature stems primarily from uncertainty about how teammates will receive shared content, not from usability issues. 9 of 12 participants expressed social anxiety about sharing incomplete work.

### Key findings
1. Fear of judgment prevents sharing — 9 of 12 cited social concerns
2. Lack of visibility into recipient experience — users don't know what others see
3. No "draft" or "private" sharing option creates all-or-nothing dynamic

### Top recommendations
1. Add sharing preview: "This is how [Name] will see your shared item"
2. Introduce "Share as draft" option with explicit WIP framing
3. Create onboarding that normalizes work-in-progress sharing

---

## Methodology

**Method:** Semi-structured remote interviews, 45-60 minutes
**Participants:** 12 users across 3 segments
**Recruitment criteria:** Active users who have NOT used collaboration feature despite team access
**Sessions:** Feb 1-12, 2024
**Limitations:** Self-selected non-adopters may have stronger opinions than general population

### Participant breakdown

| Segment | Count | Role type |
|---------|-------|-----------|
| Individual contributors | 6 | Designers, writers, analysts |
| Team leads | 4 | Managers with 3-8 reports |
| Executives | 2 | Directors and above |

---

## Findings

### Finding 1: Social anxiety is the primary barrier

**Observation:** When asked why they haven't used sharing, 9 of 12 participants described concerns about how their work would be perceived.

**Frequency:** 9 of 12 participants (75%)

**Evidence:**
> "What if they think it's not ready? I'd rather just send a polished PDF." — P2, Designer

> "I don't want my boss seeing my messy first draft. It's not about the tool, it's about the politics." — P7, Analyst

> "My team is pretty judgmental. I need to know exactly what they'll see before I share anything." — P11, Team lead

**Insight:** The barrier isn't usability — it's psychological safety. Users are protecting their professional reputation.

**Recommendation:** Reduce social risk by making the sharing experience more predictable and controllable.

---

### Finding 2: Sharing is a black box

**Observation:** 8 of 12 participants didn't know what recipients see when content is shared.

**Frequency:** 8 of 12 participants (67%)

**Evidence:**
> "Does it show my cursor? Can they see my edits in real time? I have no idea." — P4, Writer

> "I shared something once and someone commented on a typo I was literally in the middle of fixing. Never again." — P9, Team lead

**Insight:** Uncertainty about the recipient experience amplifies social anxiety. Users imagine worst-case visibility.

**Recommendation:** Add a preview showing exactly what recipients will see, including what they won't see (e.g., "Your cursor is not visible").

---

### Finding 3: All-or-nothing sharing creates paralysis

**Observation:** 7 of 12 participants wanted a "draft" or "work in progress" sharing option.

**Frequency:** 7 of 12 participants (58%)

**Evidence:**
> "If I could share it as 'here's a rough draft, feedback welcome,' that would change everything." — P1, Designer

> "There's no middle ground. It's either private or fully shared. I need something in between." — P8, Analyst

**Insight:** Users want to share but need social cover for imperfect work. The current binary creates friction.

**Recommendation:** Add "Share as draft" option that frames the content as work-in-progress for recipients.

---

## Minority view

3 of 12 participants (P3, P5, P12) reported no social concerns — they simply didn't see value in real-time collaboration. These users preferred async communication and saw sharing as "solving a problem I don't have."

---

## Recommendations summary

| Priority | Recommendation | Supporting findings | Effort |
|----------|---------------|---------------------|--------|
| High | Add sharing preview | Finding 1, 2 | Medium |
| High | Implement "Share as draft" | Finding 1, 3 | Medium |
| Medium | Onboarding about WIP sharing norms | Finding 1 | Low |
```

---

## Example 3: Edge case — conflicting findings

**Input:**
- Research shows contradictory patterns across segments
- Challenge: Synthesis must acknowledge tension without false resolution

**Output:**

```md
## Finding 4: Segment-specific contradiction

**Observation:** New users (4 of 4) wanted more guidance and defaults. Power users (3 of 4) wanted fewer defaults and more control.

**This is not a mistake — it's a design tension.**

### New users said:
> "Just set it up for me. I don't know what I'm doing yet." — P2, New user

> "Too many choices. I froze." — P4, New user

### Power users said:
> "Stop defaulting things. I have my own system." — P6, Power user

> "The defaults are always wrong for my use case." — P8, Power user

**Insight:** These needs are genuinely in conflict. Optimizing for one segment may frustrate the other.

**Recommendation options:**
1. **Progressive disclosure:** Start with smart defaults, reveal customization as users advance
2. **Persona detection:** Different defaults based on account age or usage patterns
3. **Explicit choice:** Onboarding asks "Do you want us to set things up, or do you prefer to customize?"

**Note:** This finding requires product decision about primary audience. Research cannot resolve this tension — it can only surface it clearly.
```
