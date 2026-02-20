# Examples

## Example 1: Feature screen intent map

**Input**: Map user intents for a file sharing feature.

**Output**:
```md
## Intent map: File sharing modal

### User context
- **Primary persona**: Knowledge worker sharing project files
- **Task context**: Has selected a file and clicked "Share"
- **Expertise level**: Intermediate (familiar with cloud storage)
- **Emotional state**: Focused, mild time pressure

### Intent inventory

| UI Element | User intent | Mental model | User vocabulary | System term | Copy recommendation |
|------------|-------------|--------------|-----------------|-------------|---------------------|
| Modal title | Confirm I'm sharing the right file | "Sending" a file to someone | "share", "send" | "Share" | "Share [filename]" |
| Email input | Tell the system who to share with | Like emailing an attachment | "send to", "share with" | "Add collaborator" | "Share with" |
| Permission dropdown | Control what they can do with it | Like physical document—give or lend | "let them edit", "just look" | "Permission level" | "Can edit" / "Can view" |
| Message field | Explain why I'm sharing | Like email body | "add a note", "message" | "Optional message" | "Add a message (optional)" |
| Share button | Complete the sharing action | Sending/delivering | "share", "send" | "Share" | "Share" |

### Vocabulary reconciliation

| User says | System says | Resolution |
|-----------|-------------|------------|
| "send to" | "share with" | Use "Share with"—encompasses both mental models |
| "let them edit" | "Editor access" | Use "Can edit"—matches user verb + simpler |
| "just look at it" | "Viewer access" | Use "Can view"—parallel to "Can edit" |
| "send" | "Share" | Use "Share"—broader, matches feature name |

### Intent-copy alignment score

| Element | Score | Rationale |
|---------|-------|-----------|
| Modal title | 5 | Includes filename, uses "Share" |
| Email input | 4 | "Share with" bridges vocabulary |
| Permission dropdown | 5 | "Can edit/view" matches user mental model |
| Message field | 5 | "Add a message" matches email mental model |
| Share button | 5 | Single word, matches intent |
```

---

## Example 2: Intent analysis from support data

**Input**: Analyze user intents from support tickets about password reset.

**Output**:
```md
## Intent analysis: Password reset

### Research inputs
- Source: Support tickets tagged "password"
- Sample size: 247 tickets over 3 months
- Date: 2026 Q1

### Intent clusters

**Intent cluster 1: Forgotten password recovery**
- Description: User cannot remember password, wants to regain access
- Frequency: 68% of tickets
- Current success rate: 73% (27% contact support after attempting reset)
- Sample quotes:
  - "I forgot my password and the reset link doesn't work"
  - "How do I get back into my account?"
  - "I need to change my password but I don't know the old one"
- Vocabulary patterns: "forgot", "get back in", "reset", "change", "locked out"

**Intent cluster 2: Security-motivated change**
- Description: User knows password but wants to change it proactively
- Frequency: 22% of tickets
- Current success rate: 89%
- Sample quotes:
  - "I want to update my password for security"
  - "How do I make my password stronger?"
  - "Where do I change my password?"
- Vocabulary patterns: "change", "update", "make stronger", "security"

**Intent cluster 3: Password requirement confusion**
- Description: User doesn't understand password rules during creation
- Frequency: 10% of tickets
- Current success rate: 45%
- Sample quotes:
  - "It keeps saying invalid but I don't know why"
  - "What's wrong with my password?"
  - "Why won't it accept my password?"
- Vocabulary patterns: "invalid", "won't accept", "what's wrong", "requirements"

### Intent vs. feature gap analysis

| User intent | Product capability | Gap | Recommended action |
|-------------|-------------------|-----|-------------------|
| "Get back in" (recovery) | Password reset flow | Reset email delays cause drop-off | Add copy: "Check spam folder. Link expires in 1 hour." |
| "Change password" (security) | Settings > Security > Password | Hard to find | Add "Change password" link in profile dropdown |
| "Why won't it accept" (requirements) | Validation error shown | Error doesn't explain requirements | Change error from "Invalid" to specific: "Add a number" |
```

---

## Example 3: Vocabulary reconciliation decision

**Input**: Users call the feature "workspace" but product calls it "organization."

**Output**:
```md
## Vocabulary reconciliation: Organization vs. Workspace

### Context
- **User vocabulary**: "workspace", "team space", "our area"
- **System vocabulary**: "Organization", "Org"
- **Frequency of user term in support**: 4x more common than "organization"
- **Competitor terminology**: Slack: "Workspace", Notion: "Workspace", Figma: "Organization"

### Options analysis

| Option | Pros | Cons |
|--------|------|------|
| Switch to "Workspace" | Matches user mental model, lower learning curve | Migration cost, URL changes, brand equity loss |
| Keep "Organization" | No migration needed, formal/enterprise feel | Ongoing vocabulary mismatch, support burden |
| Bridge both | Acknowledges both terms | May confuse—are they different things? |

### Recommended resolution: Bridge with transition

**Short-term** (immediate):
- In UI copy, use "Organization" as primary but add contextual bridges
- Help text: "Your organization (sometimes called a workspace)..."
- Search: Index both terms

**Long-term** (next major version):
- Evaluate full rename to "Workspace" based on user research
- If enterprise customers use "Organization", consider audience-based terminology

### Copy applications

| Location | Current | Recommended |
|----------|---------|-------------|
| Settings header | "Organization settings" | "Organization settings" (keep) |
| Empty state | "Create an organization" | "Create your workspace" |
| Invite modal | "Invite to organization" | "Invite to your workspace" |
| Error message | "Organization not found" | "We couldn't find that workspace" |

### Rationale
- Use "workspace" in user-facing conversational contexts
- Use "Organization" in formal/settings contexts where enterprise buyers expect it
- Never mix in same sentence: "Workspace" OR "Organization", not both
```

---

## Example 4: Edge case — No user research available

**Input**: Map intents for a new feature with no user research.

**Output**:
```md
## Intent map: [New feature] — Hypothesis-based

### Disclaimer
No user research available. This map uses behavioral inference and industry patterns. Validate with user testing before finalizing.

### Inferred user context
- **Assumed persona**: [Based on target audience]
- **Task context**: [Inferred from feature purpose]
- **Expertise level**: [Assumed from product positioning]
- **Emotional state**: [Inferred from task type]

### Hypothesized intent inventory

| UI Element | Hypothesized intent | Assumed mental model | Likely vocabulary | Confidence |
|------------|---------------------|---------------------|-------------------|------------|
| [Element] | [Best guess] | [Industry pattern] | [Common terms] | [High/Medium/Low] |

### Validation plan
To confirm these hypotheses:
1. [ ] Review analytics after launch (where do users drop off?)
2. [ ] Monitor support tickets for vocabulary patterns
3. [ ] Conduct 5 user interviews within 30 days
4. [ ] A/B test terminology options

### Risk mitigation
- Use most common industry vocabulary for low-risk launch
- Build in easy copy updates (no hardcoded strings)
- Add feedback mechanism for users to report confusion
```

---

## Example 5: Edge case — Missing context

**Input**: "Write copy that matches user intent."

**Output**:
```md
To map user intents to copy, I need:

1. **What screen or feature?**
   - [ ] Specific screen (share screenshot or wireframe)
   - [ ] Feature area (describe)
   - [ ] Full flow (list screens)

2. **User research available?**
   - [ ] Yes (share findings, quotes, or summary)
   - [ ] Support ticket themes available
   - [ ] Analytics data available
   - [ ] No research—need hypothesis-based approach

3. **Who are the users?**
   - Primary persona: [description]
   - Expertise level: [Novice / Intermediate / Expert]
   - Context when using feature: [describe]

4. **Known vocabulary issues?**
   - [ ] Users use different terms than product (specify)
   - [ ] Competitor terminology differs (specify)
   - [ ] No known issues

I can proceed with a hypothesis-based approach using industry patterns, but copy should be validated with users before finalizing.
```
