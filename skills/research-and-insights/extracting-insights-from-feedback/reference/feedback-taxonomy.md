# Feedback Taxonomy

## Table of contents
- [Theme categories](#theme-categories)
- [Sentiment classification](#sentiment-classification)
- [Severity levels](#severity-levels)
- [Coding best practices](#coding-best-practices)

---

## Theme categories

### Standard feedback taxonomy

Use this as a starting framework, then customize for your product:

#### Product experience
| Category | Includes | Example signals |
|----------|----------|-----------------|
| Performance | Speed, crashes, reliability | "slow," "crash," "freeze," "timeout" |
| Usability | Ease of use, learnability, navigation | "confusing," "can't find," "intuitive" |
| Features | Functionality, capabilities | "wish you had," "need," "missing" |
| Bugs | Defects, errors | "broken," "doesn't work," "error" |
| Design | Visual, layout, aesthetics | "ugly," "clean," "hard to read" |

#### Service experience
| Category | Includes | Example signals |
|----------|----------|-----------------|
| Support quality | Responsiveness, helpfulness | "support," "agent," "helped" |
| Documentation | Help content, guides | "instructions," "documentation," "FAQ" |
| Onboarding | Getting started experience | "setup," "learning," "tutorial" |

#### Business relationship
| Category | Includes | Example signals |
|----------|----------|-----------------|
| Pricing | Cost, value perception | "expensive," "worth," "pricing" |
| Billing | Charges, invoices | "charged," "bill," "refund" |
| Communication | Updates, notifications | "email," "notification," "warned" |
| Trust | Privacy, security | "privacy," "data," "secure" |

#### Competitive context
| Category | Includes | Example signals |
|----------|----------|-----------------|
| Comparisons | Competitor mentions | Competitor names, "switched from," "better than" |
| Switching | Churn signals | "canceling," "leaving," "alternative" |

### Custom taxonomy development

1. **Start broad:** Use standard categories
2. **First pass:** Code 50-100 items
3. **Identify gaps:** Note items that don't fit
4. **Refine:** Add categories for recurring gaps
5. **Merge:** Combine categories with <5% of items
6. **Document:** Write clear definitions with examples

---

## Sentiment classification

### Three-level sentiment

| Sentiment | Definition | Signals |
|-----------|------------|---------|
| Positive | Expresses satisfaction, praise, recommendation | "love," "great," "recommend," "best" |
| Negative | Expresses dissatisfaction, criticism, frustration | "hate," "terrible," "worst," "disappointed" |
| Neutral | Factual, mixed, or ambiguous | Questions, feature requests without valence |

### Handling mixed sentiment

Many feedback items contain both positive and negative elements:

> "I love the features but the app is too slow."

**Options:**
1. **Primary sentiment:** Code based on overall tone (this is negative — the praise sets up the complaint)
2. **Split coding:** Code themes separately (Features: positive, Performance: negative)
3. **Mixed category:** Use "mixed" when genuinely balanced

**Recommendation:** Use split coding when possible; it preserves information.

### Sentiment confidence

Not all sentiment is equally clear:

| Confidence | Example | Handling |
|------------|---------|----------|
| High | "This app is terrible" | Code as confident |
| Medium | "I expected better" | Code with note |
| Low | "It's okay I guess" | Consider neutral |
| Ambiguous | "Interesting approach" | Mark for review |

---

## Severity levels

### For negative feedback

| Level | Definition | Example |
|-------|------------|---------|
| Critical | Prevents core use case, causes harm | "Lost all my data," "Got charged 10x" |
| High | Significant friction, workaround required | "Have to restart every time," "Can't export" |
| Medium | Frustrating but usable | "Slow loading," "Confusing menu" |
| Low | Minor annoyance | "Typo in settings," "Icon looks weird" |

### For feature requests

| Level | Definition | Example |
|-------|------------|---------|
| Blocking | User cannot adopt without it | "Need SSO for enterprise security policy" |
| Important | Significant value, strong interest | "Would save me hours per week" |
| Nice-to-have | Would improve experience | "Would be cool if..." |
| Edge case | Highly specific need | One user's unique workflow |

### Severity signals

| Signal | Likely severity |
|--------|-----------------|
| Mentions switching/canceling | Critical or High |
| Multiple exclamation marks | Higher than average |
| Detailed workaround described | High |
| "It would be nice if" | Low or Nice-to-have |
| Time/money impact quantified | Higher severity |

---

## Coding best practices

### Consistency rules

1. **One pass per dimension:** Code all items for theme first, then sentiment, then severity
2. **Document edge cases:** When in doubt, write the decision down for future reference
3. **Multiple codes OK:** Single item can have multiple themes
4. **Primary code:** If forced to pick one, which theme is dominant?

### Reducing bias

1. **Blind to identity:** Code without looking at customer tier or recency
2. **Order randomization:** Don't code chronologically (recency bias)
3. **Inter-rater reliability:** Have second person code 10-20% independently
4. **Calibration:** Review disagreements and update definitions

### Handling edge cases

| Edge case | Handling |
|-----------|----------|
| Spam/irrelevant | Exclude from analysis, count as excluded |
| Multiple languages | Code in original language or translate consistently |
| Very long responses | Code dominant themes (max 3-4 per item) |
| Employee feedback | Tag and analyze separately |
| Duplicate feedback | Count once, note duplication |

### Documentation template

```md
## Taxonomy: [Category name]

**Definition:** [Clear description]

**Includes:**
- [Specific topic]
- [Specific topic]

**Excludes:**
- [What goes elsewhere]

**Example quotes:**
- "[Quote]" — coded as [this category] because [reason]
- "[Quote]" — NOT coded as [this category] because [reason]
```
