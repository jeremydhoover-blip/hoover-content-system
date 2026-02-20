# Synthesis Methods

## Table of contents
- [Affinity mapping](#affinity-mapping)
- [Theming techniques](#theming-techniques)
- [Observation to insight](#observation-to-insight)
- [Handling contradictions](#handling-contradictions)

---

## Affinity mapping

### Process

1. **Extract observations:** Pull discrete observations from each session
   - Use sticky notes or cards (one observation per note)
   - Include participant identifier
   - Keep factual: what happened, what was said

2. **Cluster similar observations:** Group related observations
   - Don't pre-define categories
   - Let patterns emerge from data
   - Move observations between clusters as understanding develops

3. **Name clusters:** Create descriptive labels
   - Label should describe the pattern, not the category
   - "Users expect privacy under security" not "Navigation issues"

4. **Identify hierarchy:** Group clusters into themes
   - Themes are higher-level patterns
   - Usually 3-7 major themes per study

### Example affinity structure

```
Theme: Navigation Mental Models
├── Cluster: Privacy/Security confusion
│   ├── P2: Looked under Security for Privacy settings
│   ├── P5: "Privacy and security are the same to me"
│   └── P8: Gave up looking, used search
├── Cluster: Hierarchy too deep
│   ├── P1: Lost after second level
│   ├── P3: "Where am I?"
│   └── P6: Used back button 5 times
```

---

## Theming techniques

### Bottom-up theming
Start with individual observations, build to patterns.

1. Code each observation with descriptive tag
2. Look for tag frequency and co-occurrence
3. Group tags into themes

**Best for:** Exploratory research, when you don't know what you'll find

### Top-down theming
Start with research questions, map data to questions.

1. List research questions
2. Find observations that address each question
3. Identify patterns within each question area

**Best for:** Evaluative research, when testing specific hypotheses

### Hybrid approach
Use research questions as initial frame, but allow emergent themes.

1. Map observations to research questions
2. Note observations that don't fit any question
3. Create new themes for unexpected patterns

**Best for:** Most real-world research

---

## Observation to insight

### The distinction

| Observation | Insight |
|-------------|---------|
| What happened | What it means |
| Factual | Interpretive |
| Specific to participants | Generalizable |
| "5 of 8 users clicked Security first" | "Users group privacy and security conceptually" |

### The insight formula

```
[Observation] + [Context] + [Interpretation] = Insight

"6 users looked under Security" + "Current IA separates Privacy" + "Mental models don't match structure" = 
"Users expect privacy controls within security settings"
```

### Quality check for insights

Good insights are:
- **Grounded:** Traceable to specific observations
- **Interpretive:** Add meaning beyond raw data
- **Actionable:** Suggest what to do differently
- **Non-obvious:** Not something stakeholders already assumed

### Insight ladder

Climb from observation to insight:

1. **Observation:** "P3 clicked the wrong button"
2. **Pattern:** "5 of 8 participants clicked the wrong button"
3. **Meaning:** "Button labels don't match user expectations"
4. **Insight:** "Users interpret 'Save' as 'Save and exit' — they expect to leave the screen"
5. **Implication:** "Add confirmation or change label to 'Save and continue editing'"

---

## Handling contradictions

### When data conflicts

Don't force false consensus. Contradictory findings are often the most valuable.

### Segmentation approach
Ask: Do contradictions map to user segments?

```
New users: Want guidance
Power users: Want control
→ Insight: Different segments have opposing needs
```

### Context approach
Ask: Were participants in different contexts?

```
Desktop users: Prefer full-page view
Mobile users: Prefer condensed view
→ Insight: Context, not preference, drives behavior
```

### Outlier approach
Ask: Is one view an outlier?

```
7 participants: Found task easy
1 participant: Found task impossible
→ Check: Was outlier's situation unusual? If yes, note as edge case. If no, investigate.
```

### Genuine tension approach
Sometimes both views are valid and unresolvable.

```
Some users: Want defaults
Other users: Want customization
→ This is a design decision, not a research finding. Present both views clearly.
```

### Documenting contradictions

```md
## Conflicting finding: [Topic]

### View A (N participants):
[What they said/did]

### View B (N participants):
[What they said/did]

### Analysis:
[Is this segmentation, context, outlier, or genuine tension?]

### Recommendation:
[If tension: Present options, not false resolution]
[If segmentation: Design for segments]
[If outlier: Note but don't over-index]
```
