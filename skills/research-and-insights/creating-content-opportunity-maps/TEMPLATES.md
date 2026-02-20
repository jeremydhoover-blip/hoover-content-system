# Templates

## 2x2 opportunity map

```md
# Content Opportunity Map: [Scope]

## Map dimensions
- **X-axis**: [Dimension] — Low → High
- **Y-axis**: [Dimension] — Low → High

## Opportunity list
| ID | Opportunity | Evidence | X score | Y score |
|----|-------------|----------|---------|---------|
| 1 | [Description] | [Source] | [1-5] | [1-5] |
| 2 | [Description] | [Source] | [1-5] | [1-5] |

## Map visualization

```
High Y │  Q2: [Label]      │  Q1: [Label]
       │  [IDs]            │  [IDs]
       │                   │
       ├───────────────────┼──────────────────
       │  Q3: [Label]      │  Q4: [Label]
Low Y  │  [IDs]            │  [IDs]
       │                   │
       └───────────────────┴──────────────────
              Low X              High X
```

## Quadrant analysis

### Q1: [High Y, High X] — [Quadrant name]
- **Opportunities**: [IDs and names]
- **Recommendation**: [Action]
- **Rationale**: [Why this priority]

### Q2: [High Y, Low X] — [Quadrant name]
- **Opportunities**: [IDs and names]
- **Recommendation**: [Action]

### Q3: [Low Y, Low X] — [Quadrant name]
- **Opportunities**: [IDs and names]
- **Recommendation**: [Action]

### Q4: [Low Y, High X] — [Quadrant name]
- **Opportunities**: [IDs and names]
- **Recommendation**: [Action]

## Summary recommendation
[Top 3-5 opportunities to prioritize and why]
```

## Gap analysis map

```md
# Content Gap Analysis: [Product/Journey]

## Mapping approach
Map current content coverage against user need intensity.

## Gap inventory
| Gap ID | User need | Need intensity | Current coverage | Gap severity |
|--------|-----------|----------------|------------------|--------------|
| G1 | [Need] | High/Med/Low | None/Partial/Full | Critical/High/Med/Low |

## Visual map

```
           │ No coverage    │ Partial coverage │ Full coverage
───────────┼────────────────┼──────────────────┼───────────────
High need  │ [CRITICAL]     │ [HIGH]           │ [Maintain]
           │ G1, G2         │ G3               │ —
───────────┼────────────────┼──────────────────┼───────────────
Med need   │ [HIGH]         │ [MEDIUM]         │ [Maintain]
           │ G4             │ G5, G6           │ —
───────────┼────────────────┼──────────────────┼───────────────
Low need   │ [MEDIUM]       │ [LOW]            │ [Deprioritize]
           │ G7             │ G8               │ —
```

## Prioritized gap list
| Priority | Gap | User need | Recommended action |
|----------|-----|-----------|-------------------|
| P0 | [Gap] | [Need] | [Action] |
| P1 | [Gap] | [Need] | [Action] |

## Evidence sources
- [Research study, support data, analytics that informed ratings]
```

## Journey-based opportunity map

```md
# Content Opportunities by User Journey: [Persona/Segment]

## Journey stages
| Stage | User goal | Current content | Gaps/Opportunities |
|-------|-----------|-----------------|-------------------|
| Awareness | [Goal] | [Exists] | [Opportunity] |
| Consideration | [Goal] | [Exists] | [Opportunity] |
| Decision | [Goal] | [Exists] | [Opportunity] |
| Onboarding | [Goal] | [Exists] | [Opportunity] |
| Activation | [Goal] | [Exists] | [Opportunity] |
| Retention | [Goal] | [Exists] | [Opportunity] |

## Opportunity prioritization
| Stage | Opportunity | Impact | Effort | Priority |
|-------|-------------|--------|--------|----------|
| [Stage] | [Opp] | H/M/L | H/M/L | [Rank] |

## Recommended roadmap
### Phase 1: [Timeframe]
- [Opportunity] — [Rationale]

### Phase 2: [Timeframe]
- [Opportunity] — [Rationale]

## Dependencies and sequencing
- [Opportunity X] must come before [Opportunity Y] because [reason]
```

## Scoring rubric for dimensions

```md
# Scoring Guide: [Map Name]

## Dimension 1: [Name]
| Score | Criteria |
|-------|----------|
| 5 | [Description of highest score] |
| 4 | [Description] |
| 3 | [Description] |
| 2 | [Description] |
| 1 | [Description of lowest score] |

## Dimension 2: [Name]
| Score | Criteria |
|-------|----------|
| 5 | [Description of highest score] |
| 4 | [Description] |
| 3 | [Description] |
| 2 | [Description] |
| 1 | [Description of lowest score] |

## Scoring notes
- [Any calibration guidance]
- [How to handle uncertainty]
```

## Variation guidance
| Element | Required | Flexible |
|---------|----------|----------|
| Dimension definitions | Yes | Dimensions can vary by context |
| Evidence source per opportunity | Yes | Format can vary |
| Scoring criteria | Recommended | Can be implicit if clear |
| Prioritization recommendation | Yes | Format can vary |
| Visual map | Recommended | Text table acceptable |
