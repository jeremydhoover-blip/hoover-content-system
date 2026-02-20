# Examples

## Example 1: Blog post brief

**Input:**
- Need: Blog post announcing new feature
- Audience: Existing customers
- Timeline: 2 weeks
- Writer: In-house content team

**Output:**

```md
# Content Brief: DataSync 2.0 Launch Blog Post

## Overview
**Content type:** Blog post
**Owner:** Product Marketing
**Writer:** Sarah (Content Team)
**Due date:** March 10, 2026
**Status:** Briefed

---

## Objective

### What this content should accomplish
Announce DataSync 2.0 to existing customers, driving feature adoption and generating excitement about the upgrade.

### Why this matters now
DataSync 2.0 launches March 15. This is our primary channel for customer communication about the release.

### Success metrics
| Metric | Target |
|--------|--------|
| Blog pageviews (week 1) | 5,000 |
| CTA clicks (try new feature) | 500 |
| Social shares | 50 |

---

## Audience

### Primary audience
**Who:** Current customers using DataSync 1.x
**What they need:** Understand what's new and how it helps them
**What they know:** Familiar with DataSync basics; may not know limitations they've been living with
**What they feel:** Curious but potentially skeptical ("is this worth learning?")

---

## Key messages

### Must include
1. What's new in DataSync 2.0 (3 key improvements)
2. How to upgrade (it's automatic / action required)
3. Where to learn more (link to docs)

### Should include (if space allows)
- Customer quote or early adopter feedback
- Before/after comparison
- Migration timeline for breaking changes

### Must NOT include
- Pricing changes (separate communication)
- Technical architecture details (save for docs)
- Competitor comparisons (not right context)

---

## Content requirements

### Format and structure
- **Length:** 600-800 words
- **Format:** Blog post with subheadings
- **Required sections:**
  - Hook (why this matters)
  - What's new (3 key features)
  - How to get it
  - What's next / CTA

### Tone and voice
**Overall tone:** Excited but not hyperbolic; informative
**Voice reference:** See brand voice guide (link)
**Special considerations:** These are existing customers—don't oversell; respect their time

### SEO requirements
- **Primary keyword:** DataSync 2.0
- **Meta description:** Writer to draft, ~155 characters

---

## References and inputs

### Required reading
- Product spec: [link]
- Release notes: [link]
- Voice guidelines: [link]

### Source material
- Feature comparison table (attached)
- Customer beta feedback (attached)

### Examples to emulate
- Our AI Assistant launch post (link) — good balance of features and benefits

### Examples to avoid
- Feature dump posts with no user benefit framing

---

## Constraints

### Timeline
| Milestone | Date |
|-----------|------|
| First draft | March 5 |
| Review complete | March 8 |
| Final due | March 10 |
| Publish date | March 15 (launch day) |

### Technical constraints
- Must work in blog CMS
- Images max 1200px wide
- Include alt text for all images

---

## Review and approval

### Reviewers
| Reviewer | Reviews for | Turnaround |
|----------|-------------|------------|
| Product Manager | Accuracy | 1 day |
| Content Lead | Quality, voice | 1 day |

### Final approver
Marketing Director
```

---

## Example 2: Help article brief

**Input:**
- Need: New help article for complex feature
- Audience: Users who are stuck
- Writer: Technical writer

**Output:**

```md
# Content Brief: "Setting up SSO" Help Article

## Overview
**Content type:** Help article
**Owner:** Documentation team
**Writer:** Alex
**Due date:** February 25, 2026
**Status:** Briefed

---

## Objective

### What this content should accomplish
Enable admins to successfully configure SSO without contacting support.

### Why this matters now
SSO setup generates 15% of support tickets. This article should reduce that.

### Success metrics
| Metric | Target |
|--------|--------|
| "Was this helpful?" rating | >75% yes |
| SSO-related support tickets | -25% within 30 days |
| Article completion rate | >60% |

---

## Audience

### Primary audience
**Who:** IT admins setting up SSO for their organization
**What they need:** Step-by-step instructions that work
**What they know:** Familiar with SSO concepts; may not know our specific implementation
**What they feel:** Probably frustrated (SSO setup is notorious); want to get it done

---

## Key messages

### Must include
1. Prerequisites (what they need before starting)
2. Step-by-step setup instructions
3. Verification steps (how to know it worked)
4. Troubleshooting common errors

### Must NOT include
- SSO pricing or plan requirements (separate article)
- Comparison of SSO providers (out of scope)

---

## Content requirements

### Format and structure
- **Length:** As long as needed; completeness over brevity
- **Format:** Numbered steps with screenshots
- **Required sections:**
  - Prerequisites
  - Configuration steps
  - Testing your setup
  - Troubleshooting
  - Next steps / related articles

### Tone and voice
**Overall tone:** Helpful, patient, precise
**Special considerations:** Users are likely frustrated. Acknowledge complexity; be encouraging.

---

## References and inputs

### Required reading
- SSO implementation spec: [link]
- Existing (outdated) SSO article: [link]
- Support ticket themes: [link]

### Source material
- Engineering walkthrough recording: [link]
- Screenshots from staging environment

---

## Constraints

### Timeline
| Milestone | Date |
|-----------|------|
| First draft | Feb 20 |
| Engineering review | Feb 22 |
| Final | Feb 25 |

### Technical constraints
- Must match current UI (screenshots from v3.2)
- Include code blocks for CLI commands
- Accessible image alt text required

---

## Review and approval

### Reviewers
| Reviewer | Reviews for | Turnaround |
|----------|-------------|------------|
| Engineering | Technical accuracy | 2 days |
| Support lead | Covers common issues | 1 day |
```

---

## Example 3: Edge case — Urgent brief with limited information

**Input:**
- Situation: Urgent response needed; not all information available
- Constraint: Must ship tomorrow
- Challenge: Brief writer while gathering remaining details

**Output:**

```md
# Content Brief: Security Incident Customer Communication

## ⚠️ URGENT — Due: Tomorrow 9am

## Overview
**Content type:** Customer email
**Owner:** Comms team
**Writer:** Jordan
**Due date:** February 21, 2026, 9:00am
**Status:** In progress — brief being updated

---

## Objective

### What this content should accomplish
Inform affected customers about security incident with transparency while maintaining trust.

### Why this matters now
Incident occurred yesterday. Regulatory requirement to notify within 72 hours.

---

## Audience

### Primary audience
**Who:** Customers whose data may have been affected
**What they need:** Clear information about what happened, what it means for them, what we're doing
**What they feel:** Concerned, possibly angry, want honesty

---

## Key messages

### Must include
1. What happened (factual, specific)
2. What data was affected
3. What we're doing about it
4. What they should do (if anything)
5. How to contact us with questions

### Must NOT include
- Speculation about cause (investigation ongoing)
- Blame (internal or external)
- Minimizing language ("minor," "small number")

---

## Known constraints

### What we know now
- Incident type: [Confirmed]
- Affected users: [Count confirmed by 3pm today]
- Timeline: [Under investigation]

### What we're waiting on (will update brief)
- [ ] Final user count — ETA 3pm
- [ ] Root cause — ETA unknown (may not include in first comms)
- [ ] Remediation steps — ETA 5pm

---

## Tone and voice
**Overall tone:** Serious, transparent, accountable
**Do:** Be direct, take responsibility, focus on user impact and actions
**Don't:** Be defensive, use corporate speak, minimize

---

## Timeline

| Milestone | Time |
|-----------|------|
| Draft with placeholders | Today 4pm |
| Legal review | Today 6pm |
| Final information | Today 8pm |
| Final draft | Tomorrow 8am |
| Send | Tomorrow 9am |

---

## Review and approval

### Reviewers (parallel review due to timeline)
| Reviewer | Reviews for |
|----------|-------------|
| Legal | Compliance, liability |
| Security | Technical accuracy |
| Exec sponsor | Final approval |

**All reviewers must respond by 7pm today**

---

## Open questions (writer to flag)
- [Space for writer questions that can't wait]

## Updates log
- Feb 20, 2pm: Brief created
- Feb 20, 3pm: [Will update with user count]
- Feb 20, 5pm: [Will update with remediation]
```
