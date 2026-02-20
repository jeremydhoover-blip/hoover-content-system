# Examples

## Example 1: Simplifying complex business writing

**Input:**
> The implementation of the new customer relationship management system, which was undertaken by our cross-functional team over the course of the third and fourth quarters, has resulted in significant improvements to our ability to track customer interactions, manage sales pipelines, and provide personalized service offerings that are tailored to the specific needs and preferences of our diverse customer base.

**Output:**

```md
## Improved content

We implemented a new CRM system in Q3-Q4. A cross-functional team led the rollout.

The system improved three key areas:
- **Customer interaction tracking:** We now capture every touchpoint.
- **Sales pipeline management:** Reps see deals progress in real time.
- **Personalized service:** We can tailor offerings to individual customer needs.

---

## Readability changes

### Metrics comparison

| Metric | Before | After | Target |
|--------|--------|-------|--------|
| Avg. sentence length | 71 words | 11 words | 15-20 |
| Sentences | 1 | 5 | — |
| Passive voice | 100% | 0% | <15% |

### Key changes made

1. **Split mega-sentence:** Broke 71-word sentence into 5 digestible units
2. **Active voice:** "was undertaken" → "led"; "has resulted" → "improved"
3. **Bulleted list:** Three parallel improvements now scannable
4. **Front-loaded meaning:** Key result (CRM implementation) now in first sentence

### Flags for review

None — meaning preserved.
```

---

## Example 2: Improving technical documentation flow

**Input:**
> Configuration of the deployment pipeline requires modification of the config.yaml file. The config.yaml file is located in the root directory of the project. Parameters that need to be set include the environment variable which specifies the target environment, the timeout value which determines how long the system will wait for responses, and the retry count which controls the number of retry attempts. After configuration, the pipeline can be triggered.

**Output:**

```md
## Improved content

To configure the deployment pipeline:

1. Open `config.yaml` in your project root.

2. Set these parameters:

   | Parameter | Purpose | Example |
   |-----------|---------|---------|
   | `environment` | Target deployment environment | `production` |
   | `timeout` | Response wait time (seconds) | `30` |
   | `retry_count` | Retry attempts on failure | `3` |

3. Save the file and trigger the pipeline.

---

## Readability changes

### Metrics comparison

| Metric | Before | After | Target |
|--------|--------|-------|--------|
| Avg. sentence length | 22 words | 8 words | 15-20 |
| Structure | Prose | Numbered + table | — |
| Scannable elements | 0 | 3 (list + table + code) | 1+ per section |

### Key changes made

1. **Task-oriented structure:** Converted description to numbered steps
2. **Table for parameters:** Three parallel items now scannable and comparable
3. **Code formatting:** File names in monospace for visual distinction
4. **Removed redundancy:** "The config.yaml file is located..." was inferable

### Flags for review

None — meaning preserved, format improved for technical readers.
```

---

## Example 3: Improving narrative flow

**Input:**
> Sarah had been working at the company for five years. She was promoted to manager last quarter. The team she inherited was struggling. Morale was low. Deadlines were being missed. She decided to try something different. She implemented daily standups. She also started weekly one-on-ones. The results were surprising. Productivity increased. The team seemed happier. Projects started finishing on time.

**Output:**

```md
## Improved content

After five years at the company, Sarah was promoted to manager last quarter. She inherited a struggling team — morale was low, and deadlines kept slipping.

She tried something different: daily standups and weekly one-on-ones.

The results surprised her. Productivity climbed. Projects finished on time. And for the first time in months, the team seemed happy.

---

## Readability changes

### Metrics comparison

| Metric | Before | After | Target |
|--------|--------|-------|--------|
| Avg. sentence length | 5.6 words | 10.2 words | 10-15 for narrative |
| Sentence length range | 4-9 words | 5-19 words | Varied |
| Paragraphs | 1 implied | 3 | — |

### Key changes made

1. **Varied sentence length:** Broke choppy rhythm of uniform short sentences
2. **Combined related ideas:** "Morale was low. Deadlines were being missed." → "morale was low, and deadlines kept slipping"
3. **Paragraph breaks:** Grouped by story beat (context, action, result)
4. **Pacing:** Short punchy paragraph for the intervention, longer for setup and payoff
5. **Transition phrases:** "After five years" and "for the first time" add temporal flow

### Flags for review

- Added "for the first time in months" — verify this is accurate to the story.
```

---

## Example 4: Edge case — preserving technical precision while improving readability

**Input:**
> The algorithm utilizes a probabilistic approach whereby the input vector is subjected to a series of transformations including but not limited to normalization, dimensionality reduction via principal component analysis, and subsequent classification utilizing a support vector machine with a radial basis function kernel, the hyperparameters of which have been optimized through grid search cross-validation.

**Audience:** Machine learning practitioners (technical terms acceptable)

**Output:**

```md
## Improved content

The algorithm takes a probabilistic approach with three stages:

1. **Normalize** the input vector
2. **Reduce dimensions** using PCA
3. **Classify** using an SVM with RBF kernel

Hyperparameters were optimized via grid search cross-validation.

---

## Readability changes

### Metrics comparison

| Metric | Before | After | Target |
|--------|--------|-------|--------|
| Avg. sentence length | 58 words | 9 words | 15-20 |
| Structure | Run-on prose | Steps + summary | — |
| Technical terms | Spelled out redundantly | Abbreviated (audience knows them) | — |

### Key changes made

1. **Numbered list:** Pipeline stages now visible
2. **Appropriate abbreviations:** PCA, SVM, RBF — standard for ML audience
3. **Removed "including but not limited to":** Legal phrase adds nothing
4. **Separated hyperparameter note:** Distinct concern, distinct sentence

### Technical terms preserved

- Principal component analysis (abbreviated to PCA)
- Support vector machine (SVM)
- Radial basis function (RBF)
- Grid search cross-validation

No definitions added — audience familiarity assumed per brief.

### Flags for review

- Confirm abbreviations are acceptable for target publication
- "Three stages" implies these are sequential — verify that's accurate
```
