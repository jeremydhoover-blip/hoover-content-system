# Content Governance SLA Standards Reference

Service level agreements for content governance workflow stages.

---

## SLA overview

Content governance SLAs define maximum time allowed for each workflow stage:

```
┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐
│ Draft   │───▶│ Review  │───▶│ Approve │───▶│ Publish │───▶│ Live    │
│ (Auth)  │    │ (Rev)   │    │ (Appr)  │    │ (Pub)   │    │         │
└─────────┘    └─────────┘    └─────────┘    └─────────┘    └─────────┘
   SLA-01        SLA-02        SLA-03         SLA-04
```

---

## Standard SLA tiers

### Tier 1: Standard content
Routine content updates with no urgency.

| Stage | SLA | Start trigger | End trigger |
|-------|-----|---------------|-------------|
| Review | 3 business days | Submitted for review | Review complete |
| Revision | 2 business days | Feedback provided | Revision submitted |
| Approval | 2 business days | Review approved | Final approval |
| Publication | 1 business day | Approval granted | Content live |

**Total standard cycle**: 8 business days maximum

---

### Tier 2: Priority content
Important updates with business priority.

| Stage | SLA | Start trigger | End trigger |
|-------|-----|---------------|-------------|
| Review | 1 business day | Submitted for review | Review complete |
| Revision | 1 business day | Feedback provided | Revision submitted |
| Approval | 1 business day | Review approved | Final approval |
| Publication | 4 hours | Approval granted | Content live |

**Total priority cycle**: 3 business days + 4 hours maximum

---

### Tier 3: Urgent content
Critical updates requiring immediate attention.

| Stage | SLA | Start trigger | End trigger |
|-------|-----|---------------|-------------|
| Review | 4 hours | Submitted for review | Review complete |
| Revision | 2 hours | Feedback provided | Revision submitted |
| Approval | 2 hours | Review approved | Final approval |
| Publication | 1 hour | Approval granted | Content live |

**Total urgent cycle**: 9 hours maximum (within business hours)

---

### Tier 4: Emergency content
Safety, legal, or security issues requiring immediate fix.

| Stage | SLA | Start trigger | End trigger |
|-------|-----|---------------|-------------|
| Review | 1 hour | Submitted for review | Review complete |
| Approval | 30 minutes | Review approved | Final approval |
| Publication | 30 minutes | Approval granted | Content live |

**Total emergency cycle**: 2 hours maximum (any time)

**Emergency criteria**:
- Security vulnerability disclosed in content
- Legal compliance violation
- Safety hazard in instructions
- Major factual error causing harm

---

## SLA by content type

| Content type | Default tier | Review SLA | Full cycle |
|--------------|--------------|------------|------------|
| UI copy | Standard | 3 days | 8 days |
| Error messages | Priority | 1 day | 3 days |
| Marketing copy | Standard | 3 days | 8 days |
| Legal updates | Priority | 1 day | 3 days |
| Help articles | Standard | 3 days | 8 days |
| Incident comms | Emergency | 1 hour | 2 hours |
| Feature launch | Priority | 1 day | 3 days |
| Blog posts | Standard | 3 days | 8 days |
| Localization | Standard + 2 days | 5 days | 10 days |

---

## SLA measurement

### Clock rules

| Rule | Specification |
|------|---------------|
| Business hours | 9:00 AM - 6:00 PM local time |
| Business days | Monday - Friday (excluding holidays) |
| Clock start | When item enters queue |
| Clock stop | When item exits queue (complete or blocked) |
| Clock pause | When blocked on external dependency |

### Blocking conditions (clock pauses)
- Waiting for author response to feedback
- Waiting for external stakeholder input
- Waiting for dependent content
- System outage preventing work

---

## SLA metrics

### Key performance indicators

| Metric | Formula | Target |
|--------|---------|--------|
| On-time completion rate | (Completed on time / Total) × 100 | ≥95% |
| Average cycle time | Sum of cycle times / Count | < Tier SLA |
| Review turnaround | Average time in review | < Review SLA |
| Approval turnaround | Average time in approval | < Approval SLA |
| Escalation rate | (Escalated / Total) × 100 | <5% |
| Revision rate | (Items requiring revision / Total) × 100 | <30% |

### Reporting cadence

| Report | Frequency | Audience |
|--------|-----------|----------|
| SLA compliance | Weekly | Content team |
| Cycle time trends | Monthly | Content leadership |
| Escalation analysis | Monthly | Content owners |
| Annual review | Yearly | Executive sponsor |

---

## Escalation procedures

### Automatic escalation triggers

| Trigger | Action |
|---------|--------|
| 80% of SLA elapsed | Warning to assignee |
| 100% of SLA elapsed | Escalate to manager |
| 150% of SLA elapsed | Escalate to Content Owner |
| 200% of SLA elapsed | Escalate to Executive |

### Escalation matrix

| SLA breach | Escalate to | Response expectation |
|------------|-------------|---------------------|
| Review overdue | Review manager | Reassign or expedite |
| Approval overdue | Content Owner | Override or approve |
| Publication overdue | Tech lead | Investigate blocker |
| Multiple items overdue | Director | Process review |

---

## Exception handling

### Valid SLA exception reasons

| Reason | Documentation required | Approval required |
|--------|------------------------|-------------------|
| Resource unavailable | Unavailability dates | Manager |
| Scope increase | Change description | Content Owner |
| External dependency | Dependency details | Manager |
| Quality concern | Issue description | Content Owner |
| System outage | Incident ticket | Auto-approved |

### Exception request process
1. Document reason for exception
2. Estimate new completion date
3. Submit for approval (per table above)
4. Update tracking system
5. Communicate to stakeholders

---

## Consequences of SLA breach

### Operational consequences

| Breach level | Consequence |
|--------------|-------------|
| First breach | Documented, no action |
| Pattern (3+ in month) | Process review required |
| Critical content breach | Incident review |
| Repeated pattern | Escalation to leadership |

### Process improvement triggers

| Trigger | Action |
|---------|--------|
| >10% breach rate | Review SLA appropriateness |
| Consistent stage bottleneck | Add resources or revise process |
| Emergency tier overuse | Review tier assignment criteria |

---

## SLA revision process

### Annual review criteria
- Breach rate analysis
- Resource availability changes
- Business priority shifts
- Tool/process improvements
- Benchmark against industry

### SLA change approval
- Minor adjustment (<20%): Content Owner
- Major adjustment (>20%): Director + stakeholders
- New tier creation: Executive sponsor
