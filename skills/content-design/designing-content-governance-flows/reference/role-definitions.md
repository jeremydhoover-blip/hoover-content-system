# Content Governance Role Definitions Reference

Standard role definitions for content governance workflows.

---

## Role taxonomy

### Core governance roles

| Role | Primary responsibility | Decision scope |
|------|------------------------|----------------|
| **Content Owner** | Owns content domain/area | Final approval within domain |
| **Content Author** | Creates and updates content | Content creation |
| **Content Reviewer** | Reviews for accuracy | Quality validation |
| **Content Approver** | Approves changes | Go/no-go decision |
| **Content Publisher** | Deploys to production | Release execution |
| **Legal Reviewer** | Reviews for legal compliance | Legal/regulatory |
| **Localization Lead** | Manages translations | Translation quality |
| **Style Reviewer** | Reviews for style compliance | Voice and tone |

---

## Role definitions

### Content Owner

**Definition**: Accountable for content strategy, quality, and governance within a defined domain.

**Responsibilities**:
- Define content standards for domain
- Assign authors and reviewers
- Final approval authority
- Escalation point for disputes
- Content audit and retirement decisions

**Decision rights**:
| Decision | Authority level |
|----------|-----------------|
| New content approval | Final |
| Style exception | Final |
| Content retirement | Final |
| Author assignment | Full |
| Review escalation | Final |

**Not responsible for**:
- Individual content creation
- Technical implementation
- Translation execution

---

### Content Author

**Definition**: Creates and maintains content according to established standards.

**Responsibilities**:
- Write new content
- Update existing content
- Follow style guidelines
- Respond to review feedback
- Submit for review and approval

**Decision rights**:
| Decision | Authority level |
|----------|-----------------|
| Content creation | Full |
| Minor updates (<10% change) | Self-approve |
| Major updates (>10% change) | Requires approval |
| Word choice (within guidelines) | Full |

**Escalation path**: Content Reviewer → Content Owner

---

### Content Reviewer

**Definition**: Evaluates content for accuracy, clarity, and guideline compliance.

**Responsibilities**:
- Review content for errors
- Verify factual accuracy
- Check style compliance
- Provide actionable feedback
- Approve or request revisions

**Decision rights**:
| Decision | Authority level |
|----------|-----------------|
| Style compliance | Advisory → Approval if assigned |
| Factual accuracy | Approval required |
| Clarity assessment | Advisory |
| Revision request | Full |

**Review criteria**:
- Accuracy: Is information correct?
- Clarity: Is meaning unambiguous?
- Compliance: Does it follow guidelines?
- Completeness: Is anything missing?

---

### Content Approver

**Definition**: Makes final approval decision for content publication.

**Responsibilities**:
- Final quality check
- Approve or reject publication
- Validate review completion
- Document approval decision

**Decision rights**:
| Decision | Authority level |
|----------|-----------------|
| Publication approval | Final |
| Exception approval | Full (within scope) |
| Urgent bypass | Emergency only |
| Rejection | Full |

**Approval conditions**:
- All required reviews completed
- No open blocking issues
- Compliance checklist passed

---

### Content Publisher

**Definition**: Executes technical deployment of approved content.

**Responsibilities**:
- Deploy content to production
- Verify successful deployment
- Rollback if issues found
- Document publication

**Decision rights**:
| Decision | Authority level |
|----------|-----------------|
| Deployment timing | Full (within window) |
| Rollback | Full (technical issues) |
| Publication method | Full |
| Content changes | None |

**Not responsible for**:
- Content quality decisions
- Approval decisions
- Content strategy

---

### Legal Reviewer

**Definition**: Reviews content for legal and regulatory compliance.

**Responsibilities**:
- Identify legal risks
- Ensure regulatory compliance
- Review claims and disclosures
- Approve legally sensitive content

**Triggers for legal review**:
- Claims about product capability
- Pricing and offer terms
- User data and privacy statements
- Third-party references
- Disclaimers and terms

**Decision rights**:
| Decision | Authority level |
|----------|-----------------|
| Legal compliance | Final |
| Required disclosures | Final |
| Risk assessment | Advisory |
| Claim approval | Final |

---

### Localization Lead

**Definition**: Manages translation and localization quality.

**Responsibilities**:
- Coordinate translation workflow
- Maintain terminology glossary
- Review translation quality
- Manage localization vendors

**Decision rights**:
| Decision | Authority level |
|----------|-----------------|
| Translation quality | Final |
| Glossary updates | Full |
| Vendor selection | Recommendation |
| Localization scope | Advisory |

---

### Style Reviewer

**Definition**: Reviews content for voice, tone, and style compliance.

**Responsibilities**:
- Apply style guidelines
- Ensure voice consistency
- Flag style violations
- Provide rewrite suggestions

**Decision rights**:
| Decision | Authority level |
|----------|-----------------|
| Style compliance | Approval (if assigned) |
| Voice consistency | Advisory |
| Exception requests | Recommendation only |
| Guideline interpretation | Full |

---

## Role assignment matrix

### By content type

| Content type | Required roles | Optional roles |
|--------------|----------------|----------------|
| UI copy | Author, Style Reviewer, Owner | Legal |
| Error messages | Author, Technical Reviewer, Owner | Legal |
| Marketing copy | Author, Style, Legal, Owner | - |
| Help articles | Author, Technical, Style, Owner | Localization |
| Legal/Terms | Author, Legal (multiple), Owner | - |
| Notifications | Author, Style, Owner | Legal |

### By change magnitude

| Change size | Required approvals |
|-------------|-------------------|
| Typo fix | Self-approve (Author) |
| Minor update | 1 reviewer |
| New content | Reviewer + Approver |
| Major revision | Full review chain |
| Legal-sensitive | Legal + Approver |

---

## RACI matrix template

| Activity | Owner | Author | Reviewer | Approver | Publisher |
|----------|-------|--------|----------|----------|-----------|
| Define standards | A | I | C | I | I |
| Create content | I | R | I | I | I |
| Review content | I | I | R | I | I |
| Approve content | A | I | C | R | I |
| Publish content | I | I | I | A | R |
| Audit content | R | C | C | I | I |
| Retire content | A | R | I | R | R |

**Legend**: R = Responsible, A = Accountable, C = Consulted, I = Informed

---

## Role conflict resolution

### Common conflicts

| Conflict | Resolution |
|----------|------------|
| Author disagrees with reviewer | Escalate to Content Owner |
| Reviewer requests contradict style guide | Style guide takes precedence |
| Legal and marketing disagree | Legal has final authority on compliance |
| Urgent need vs. approval process | Emergency bypass with post-publication review |
| Multiple reviewers disagree | Content Owner decides |

### Escalation hierarchy

```
Author → Reviewer → Approver → Content Owner → Executive Sponsor
```
