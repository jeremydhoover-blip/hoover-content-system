# Templates

## Cognitive load audit
Use this structure to analyze a screen or flow:

```md
## Cognitive load audit: [Screen/flow name]

**Primary task**: [What user is trying to accomplish]
**User context**: [Expertise: Novice/Intermediate/Expert] | [Frequency: First-time/Occasional/Daily] | [Stress: Low/Medium/High]

### Decision point inventory

| Decision | Type | Current load source | Severity |
|----------|------|---------------------|----------|
| [What user must decide] | [Intrinsic/Extraneous/Germane] | [Why it's demanding] | [High/Medium/Low] |

### Load sources by type

**Intrinsic load** (complexity inherent to task—minimize but can't eliminate):
- [Source]: [Why unavoidable]

**Extraneous load** (removable friction—target for elimination):
- [Source]: [Reduction strategy]

**Germane load** (productive learning—preserve or enhance):
- [Source]: [Why valuable]

### Total load assessment
- Decisions required: [count]
- Information items to remember: [count]
- Steps to completion: [count]
- Estimated cognitive demand: [Low/Medium/High/Overload]
```

## Reduction recommendation
Use this structure for each reduction:

```md
## Reduction: [Short description]

**Load source**: [What causes the cognitive demand]
**Load type**: [Extraneous]
**Severity**: [High/Medium/Low]

**Current state**:
[Description or screenshot reference]

**Problem**: [Specific cognitive demand created]

**Reduction strategy**: [Chunking | Defaults | Progressive disclosure | Recognition over recall | Eliminate | Simplify language | Reduce choices]

**Recommended change**:
- Before: [Current content/interaction]
- After: [Proposed content/interaction]

**Load reduction**: [What mental effort is eliminated]

**Risk check**: [Does this removal lose essential information? Yes—mitigate how / No]
```

## Load reduction checklist
Use for systematic review:

```md
## Load reduction checklist: [Screen name]

### Memory demands
- [ ] User doesn't need to remember information from previous screens
- [ ] Labels match user's vocabulary (recognition, not recall)
- [ ] System shows current state; user doesn't have to remember it
- [ ] Related information is visually grouped

### Choice complexity
- [ ] Smart defaults reduce decisions needed
- [ ] Number of options is appropriate (ideally 3-7)
- [ ] Choices are meaningfully distinct (no overlapping options)
- [ ] Recommended option is indicated when appropriate

### Information timing
- [ ] Information appears at point of need, not before
- [ ] Details are progressively disclosed, not front-loaded
- [ ] Help text is available but not intrusive

### Language clarity
- [ ] No jargon without explanation
- [ ] Instructions describe outcomes, not mechanisms
- [ ] Error messages include next action

### Visual parsing
- [ ] Whitespace separates distinct sections
- [ ] Hierarchy is clear without reading every word
- [ ] Primary action is visually dominant
```
