# Developer Onboarding Patterns

## Pattern selection matrix

| Developer state | Pattern | Focus |
|-----------------|---------|-------|
| Evaluating | Value-first quickstart | Show outcome before setup |
| Committed | Minimal path to success | Fastest working example |
| Exploring | Progressive tutorials | Depth after breadth |
| Stuck | Rescue flows | Diagnose and recover |
| Scaling | Production guides | Reliability and performance |

## Value-first quickstart pattern

**Use when:** Developer hasn't committed yet, needs to see value.

**Structure:**
1. Show the end result first (screenshot, demo)
2. "Try it now" with zero setup (playground, curl)
3. Then explain how to build it themselves
4. Account creation is a later step

**Example flow:**
```
Show: "Here's what you can build" [demo]
Try: "Test it now" [playground, no account]
Build: "Build it yourself" [quickstart after signup]
```

**Key metric:** Demo-to-signup conversion rate

## Minimal path to success pattern

**Use when:** Developer has committed, needs fast first win.

**Principles:**
- One goal, one path
- No branches or options until after success
- Strip every non-essential step
- Defer explanations until after working code

**Anti-patterns to avoid:**
- "First, let's understand the architecture..."
- Multiple authentication options before first request
- Comprehensive SDK documentation before quickstart
- Billing setup before any API call

**Time budget:**
| Step | Max time |
|------|----------|
| Account creation | 2 min |
| Get credentials | 1 min |
| Install SDK | 2 min |
| First working call | 2 min |
| **Total** | **7 min** |

## Progressive disclosure pattern

**Use when:** Developer achieved first success, ready to expand.

**Layer structure:**
```
Layer 1: Quickstart (5-10 min)
  └── One working example

Layer 2: Core tutorials (30-60 min each)
  ├── Use case A
  ├── Use case B
  └── Use case C

Layer 3: Reference documentation
  ├── Complete API reference
  ├── SDK reference
  └── Configuration options

Layer 4: Advanced guides
  ├── Performance optimization
  ├── Security hardening
  └── Enterprise patterns
```

**Navigation cues:**
- "Now that you've [done X], you might want to [do Y]"
- Explicit "Next steps" after each milestone
- "Prerequisites: Complete [previous guide]"

## Rescue flow pattern

**Use when:** Developer is stuck or encountered error.

**Entry points:**
- Error message links
- "Something not working?" links
- Search results
- Support escalation

**Structure:**
```md
## {Error or symptom}

### Quick fixes
Try these first:
1. {Most common fix}
2. {Second most common}

### Still not working?

#### Diagnose
{Command to check status}

#### Common causes
| Symptom | Cause | Fix |
|---------|-------|-----|
| {A} | {B} | {C} |

#### Get help
- [Community forum]
- [Support ticket]
```

## Persona-based paths pattern

**Use when:** Developer audiences have significantly different needs.

**Common personas:**
| Persona | Needs | Path |
|---------|-------|------|
| Hobbyist | Quick experiments | Simplest quickstart |
| Startup | Fast integration | SDK + tutorials |
| Enterprise | Security, compliance | Production guide first |
| Migrator | From competitor | Migration guide |

**Implementation:**
- Persona selector on landing page
- Track persona in analytics
- Customize recommendations
- Don't force choice (provide default)

## Sandbox-first pattern

**Use when:** Production access has friction (approval, billing).

**Principles:**
- Sandbox requires zero approval
- Same API, different endpoint
- Clearly labeled limitations
- Easy switch to production

**Sandbox design:**
| Feature | Sandbox | Production |
|---------|---------|------------|
| Access | Instant | Approval required |
| Data | Sample/test | Real |
| Rate limits | Lower | Higher |
| SLA | None | Guaranteed |
| Cost | Free | Paid |

## Measurement points

Track these to optimize onboarding:

| Milestone | What to measure |
|-----------|-----------------|
| Awareness → Signup | Landing page conversion |
| Signup → First call | Time to first API call |
| First call → Success | First successful response |
| Success → Production | Time to production deployment |
| Any stage → Stuck | Drop-off points, support tickets |

**Key metrics:**
- Time to first successful API call
- Completion rate by step
- Drop-off rate by step
- Support tickets per 100 signups
- Time from signup to production
