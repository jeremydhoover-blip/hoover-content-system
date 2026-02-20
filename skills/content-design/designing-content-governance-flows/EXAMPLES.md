# Examples

## Example 1: UI copy governance flow

**Input**: Design governance for UI copy changes in a product team.

**Output**:
```md
## Governance flow: UI copy

### Overview
- **Content type**: In-product UI text (labels, errors, help text, notifications)
- **Risk level**: Medium (affects user experience, limited legal exposure)
- **Typical volume**: 15-30 changes per sprint
- **SLA target**: 3 business days draft to merge

### Flow diagram

```
[Designer/PM creates] → [Content review] → [Eng implementation] → [QA verification] → [Ship]
         ↓                    ↓                    ↓                    ↓
      [Draft PR]         [Approved/Changes]   [Code review]        [Verified]
         ↑                    ↓                                        ↓
      [Revise] ←——— [Request changes]                              [Release]
```

### Stage definitions

| Stage | Owner | Entry criteria | Exit criteria | SLA |
|-------|-------|----------------|---------------|-----|
| Draft | Designer/PM | User story exists | Copy in PR, follows patterns | — |
| Content review | Content designer | PR opened, copy flagged for review | Approved or changes documented | 1 day |
| Implementation | Engineer | Content approved | Code merged to staging | 1 day |
| QA | QA engineer | Code in staging | Copy matches approved, no truncation | 1 day |
| Ship | Release manager | QA passed | In production | Per release cycle |

### Risk-based routing

| Copy type | Risk | Review requirement |
|-----------|------|-------------------|
| New feature copy | Medium | Content review required |
| Bug fix (typo, grammar) | Low | Peer review only |
| Error messages | Medium | Content review required |
| Legal/compliance copy | High | Content + Legal review |
| Marketing claims in UI | High | Content + Marketing + Legal |

### Exception handling
- **Urgent (P0 bug)**: Content designer approves async in Slack; formal review within 24h post-ship
- **Content designer unavailable**: Peer content designer or Content lead approves
- **Disputed feedback**: Escalate to Content lead for tiebreaker
```

---

## Example 2: Role definition

**Input**: Define the Content Reviewer role.

**Output**:
```md
## Role: Content Reviewer

**Purpose**: Ensure UI copy meets quality standards before publication
**Capacity**: 1 content designer per product team; ~30 min/day review time

### Permissions
| Can do | Cannot do |
|--------|-----------|
| Approve routine copy changes | Approve legal/compliance copy |
| Request changes with specific feedback | Block releases without documented reason |
| Flag content for escalation | Override Content Lead decisions |
| Suggest alternatives | Rewrite copy without creator input |

### Responsibilities
- Review all flagged copy PRs within SLA (1 business day)
- Apply content patterns and style guide consistently
- Document all change requests with specific, actionable feedback
- Escalate edge cases to Content Lead
- Track common issues for pattern library updates

### Accountability
- **Success metric**: 95% of reviews completed within SLA; <5% post-ship copy corrections
- **Failure consequence**: Bottleneck delays release; inconsistent quality ships

### Escalation
- **Escalates to**: Content Lead when copy involves brand positioning, legal risk, or new pattern needed
- **Escalated from**: Peer reviewers when expertise needed; Designers when disputed feedback
```

---

## Example 3: Review checklist

**Input**: Create a review checklist for marketing email copy.

**Output**:
```md
## Review checklist: Marketing email

**Reviewer**: Marketing content reviewer
**Time budget**: 15 minutes per email

### Required checks
- [ ] **Subject line**: Under 50 characters, no spam trigger words
- [ ] **Preview text**: Complements subject, not duplicates it
- [ ] **Personalization**: Dynamic fields have fallbacks (e.g., "Hi {{first_name|there}}")
- [ ] **CTA clarity**: One primary CTA, action verb, links to correct destination
- [ ] **Legal compliance**: Unsubscribe link present, physical address in footer, opt-out honored
- [ ] **Brand voice**: Matches voice guidelines, appropriate tone for segment
- [ ] **Accessibility**: Alt text on images, minimum font 14px, color contrast passes
- [ ] **Mobile rendering**: Tested in mobile preview, no truncation

### Conditional checks (if applicable)
- [ ] **Promotional claims**: If price/discount mentioned, verified with source
- [ ] **Time-sensitive language**: If urgency used, deadline is real and displayed
- [ ] **Partner mentions**: If co-branded, partner approval documented

### Review outcomes
| Outcome | Criteria | Next step |
|---------|----------|-----------|
| Approved | All required checks pass | Schedule send |
| Changes requested | 1-3 issues, easy fixes | Return to creator, re-review same day |
| Rejected | Legal compliance fails OR >3 issues | Return to creator, Content Lead notified |
| Escalated | Brand/legal uncertainty | Send to Legal or Brand for guidance |
```

---

## Example 4: Governance for AI-generated content

**Input**: Design governance flow for AI-assisted content creation.

**Output**:
```md
## Governance flow: AI-generated content

### Overview
- **Content type**: Content created with AI assistance (drafts, suggestions, rewrites)
- **Risk level**: Variable (depends on output type and publication context)
- **Principle**: AI assists; humans are accountable for all published content

### Risk matrix for AI content

| AI usage | Risk level | Governance requirement |
|----------|------------|----------------------|
| AI-generated first draft, human rewrites | Low | Standard content review |
| AI suggestions accepted with minor edits | Medium | Standard review + fact-check |
| AI generates final copy with minimal edit | High | Enhanced review + source verification |
| AI content published without human edit | Critical | Not permitted |

### Flow diagram

```
[AI generates draft] → [Human editing] → [Fact verification] → [Standard review] → [Publish]
         ↓                   ↓                   ↓                    ↓
   [AI draft logged]   [Edit documented]  [Sources checked]     [Approved]
                             ↓                   ↓                    ↓
                    [Human accountable]    [Failed: reject]       [Live]
```

### Additional requirements for AI content

| Requirement | Rationale |
|-------------|-----------|
| Log AI tool used | Audit trail for compliance |
| Document human edits | Demonstrate human oversight |
| Verify facts/claims | AI may hallucinate |
| Check for plagiarism | AI may reproduce copyrighted text |
| Apply same style standards | AI doesn't know our voice |

### AI content attestation
Before publishing AI-assisted content, human editor attests:
- [ ] I have reviewed and edited this content
- [ ] Facts and claims have been verified
- [ ] Content meets style and quality standards
- [ ] I take responsibility for this content

### Prohibited uses
- AI-generated legal or compliance copy without Legal review
- AI-generated content attributed to named human author without disclosure
- AI content in regulated contexts without appropriate review
```

---

## Example 5: Edge case — Missing context

**Input**: "Set up content governance."

**Output**:
```md
To design content governance, I need:

1. **What content types need governance?**
   - [ ] UI copy
   - [ ] Documentation
   - [ ] Marketing content
   - [ ] Legal/compliance content
   - [ ] Blog/editorial
   - [ ] All of the above

2. **Who's involved?**
   - Creators: [Roles who write content]
   - Reviewers: [Roles who check content]
   - Approvers: [Roles with final sign-off authority]
   - Publishers: [Roles who push content live]

3. **Current pain points?**
   - [ ] Content ships without review
   - [ ] Reviews take too long (specify current time)
   - [ ] Inconsistent quality
   - [ ] Unclear who approves
   - [ ] No escalation path

4. **Constraints?**
   - Legal/compliance requirements?
   - Release cycle constraints?
   - Team capacity limitations?

5. **Tooling?**
   - Where is content stored? (CMS, Git, docs)
   - How are reviews tracked? (PR, ticketing, email)

I can provide a starter governance framework based on common patterns if you share content types and team structure.
```
