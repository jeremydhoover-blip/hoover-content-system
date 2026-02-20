# Cognitive Load Classification Reference

Framework for identifying, measuring, and categorizing cognitive load in UI content.

---

## Load type taxonomy

### Intrinsic load
**Definition**: Cognitive effort required by the inherent complexity of the task.

**Characteristics**:
- Cannot be eliminated, only managed
- Determined by task complexity
- Varies by user expertise

**Examples**:
| Task | Intrinsic load | Why |
|------|----------------|-----|
| Setting a reminder | Low | Simple concept, familiar pattern |
| Configuring API authentication | High | Multiple concepts, technical knowledge required |
| Choosing a subscription plan | Medium | Comparison, trade-offs |

---

### Extraneous load
**Definition**: Cognitive effort caused by poor design, not the task itself.

**Characteristics**:
- Can and should be eliminated
- Caused by content/design problems
- Wastes user cognitive resources

**Examples**:
| Problem | Load cause | Fix |
|---------|------------|-----|
| Jargon in error message | User must translate | Use plain language |
| Required field unmarked | User discovers by failing | Mark required fields |
| Instructions after form | User must scroll back | Instructions before form |

---

### Germane load
**Definition**: Cognitive effort spent on learning and schema building.

**Characteristics**:
- Beneficial cognitive load
- Helps users build mental models
- Should be supported, not eliminated

**Examples**:
| Pattern | Germane load | Benefit |
|---------|--------------|---------|
| Consistent navigation | Learn once, use everywhere | Transfers to future tasks |
| Progressive onboarding | Build knowledge step by step | Creates lasting understanding |
| Clear feedback | Understand cause and effect | Improves future decisions |

---

## Load indicators

### High load signals
Content or design likely causing high cognitive load:

| Signal | Description | Detection |
|--------|-------------|-----------|
| **Dense text blocks** | Large paragraphs without breaks | >4 sentences continuous |
| **Multiple concepts per screen** | Too many ideas competing | >3 distinct topics visible |
| **Inconsistent patterns** | Same action, different UI | Varies across screens |
| **Hidden requirements** | Rules revealed after failure | Validation-only messaging |
| **Abstract language** | Concepts without examples | No concrete references |
| **Deep nesting** | Many levels to navigate | >3 levels to reach content |
| **Unclear hierarchy** | Everything looks equally important | No visual differentiation |
| **Competing actions** | Multiple CTAs with equal weight | Unclear primary action |

---

### Low load signals
Content or design supporting low cognitive load:

| Signal | Description | Detection |
|--------|-------------|-----------|
| **Chunked content** | Information in digestible pieces | 1-3 sentences per chunk |
| **Single focus** | One primary concept per view | Clear single topic |
| **Consistent patterns** | Same action, same UI | Predictable interactions |
| **Proactive guidance** | Rules shown before input | Helper text visible |
| **Concrete language** | Specific examples and references | Tangible descriptions |
| **Shallow navigation** | Few levels to content | ≤3 levels to reach |
| **Clear hierarchy** | Important items stand out | Visual differentiation |
| **Primary action emphasis** | One clear next step | Single dominant CTA |

---

## Load measurement framework

### Heuristic scoring

Score each dimension 1-5 (1 = low load, 5 = high load):

| Dimension | 1 (Low) | 3 (Medium) | 5 (High) |
|-----------|---------|------------|----------|
| **Vocabulary complexity** | Common words | Some domain terms | Technical jargon |
| **Sentence complexity** | Simple, short | Compound sentences | Complex, nested |
| **Concept count** | 1 concept | 2-3 concepts | 4+ concepts |
| **Decision points** | 0-1 decisions | 2-3 decisions | 4+ decisions |
| **Visual density** | Spacious | Moderate | Cramped |
| **Navigation depth** | 1-2 levels | 3 levels | 4+ levels |
| **Recall required** | None | Some context | External reference |
| **Pattern familiarity** | Standard | Modified standard | Novel |

**Interpretation**:
- 8-16: Low load (appropriate for general audience)
- 17-28: Medium load (appropriate for familiar users)
- 29-40: High load (requires expertise or redesign)

---

## Load by user state

Different user states have different load tolerance:

| User state | Load tolerance | Design response |
|------------|----------------|-----------------|
| **New user** | Low | Guided, minimal choices |
| **Task-focused** | Medium-low | Clear path, minimal distractions |
| **Exploring** | Medium | Options visible, easy navigation |
| **Expert** | Medium-high | Efficient, power features accessible |
| **Stressed** | Very low | Critical info only, clear actions |
| **Error recovery** | Very low | Problem + fix, nothing else |

---

## Load by context

Environmental factors affecting load tolerance:

| Context | Impact | Accommodation |
|---------|--------|---------------|
| **Mobile** | Smaller viewport, possible distraction | Reduce density, larger targets |
| **Multitasking** | Split attention | Persistent state, clear re-entry |
| **Time pressure** | Reduced processing capacity | Prioritize critical info |
| **Accessibility need** | Possible processing differences | Multiple modalities, clear structure |
| **Non-native language** | Translation overhead | Simple vocabulary, avoid idioms |

---

## Content load factors

### Vocabulary load
| Level | Characteristics | Example |
|-------|-----------------|---------|
| Low | Common words, no jargon | "Save your changes" |
| Medium | Some domain terms, explained | "Save your changes to the draft" |
| High | Technical terms, assumed knowledge | "Commit staged changes to HEAD" |

### Structure load
| Level | Characteristics | Example |
|-------|-----------------|---------|
| Low | Short sentences, clear structure | "Enter your email. We'll send a link." |
| Medium | Compound sentences, some nesting | "Enter your email address, and we'll send you a link to reset your password." |
| High | Long sentences, multiple clauses | "Upon entering your registered email address in the field provided, a password reset link will be dispatched to the inbox associated with your account within 5-10 minutes." |

### Decision load
| Level | Characteristics | Example |
|-------|-----------------|---------|
| Low | Single choice, clear default | "Save" button only |
| Medium | 2-3 options, distinguishable | "Save", "Save as", "Discard" |
| High | Multiple options, trade-offs | 5 export formats with technical differences |

---

## Load transfer patterns

### Shifting load to the system
Move cognitive work from user to interface:

| User load | System solution |
|-----------|-----------------|
| Remembering format | Show format example, auto-format input |
| Calculating | Compute and display results |
| Cross-referencing | Show related info in context |
| Recalling previous input | Pre-fill from history |
| Understanding jargon | Replace with plain language |

### Acceptable user load
Some cognitive effort is appropriate:

| Acceptable load | Why |
|-----------------|-----|
| Reading important warnings | Safety/consequence awareness |
| Making explicit choices | User agency, accountability |
| Learning new concepts | Skill building (germane load) |
| Confirming significant actions | Prevents errors |
