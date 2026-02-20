# Message map schema

## Structural requirements

A valid message map must contain these elements in hierarchy:

```
Message Map
├── Audience Definition
│   ├── Primary audience (required)
│   └── Secondary audience (optional)
├── Core Message (required, single sentence)
├── Pillars (required, exactly 3-4)
│   ├── Pillar Name/Theme
│   ├── Key Message (one sentence)
│   ├── Supporting Messages (1-3)
│   └── Proof Points (1-3, must be verifiable)
├── Boilerplate (optional but recommended)
└── Tagline Options (optional)
```

## Element definitions

### Audience definition
**Purpose**: Specify who the messaging is for to guide word choice and emphasis.

**Required fields**:
- Role or segment name
- Optional: Pain point, context, or trigger

**Quality criteria**:
- Specific enough to differentiate from other audiences
- Actionable for content decisions ("Is this word right for this audience?")

### Core message
**Purpose**: Single sentence that communicates complete value proposition.

**Constraints**:
- Maximum 30 words
- Must answer: What is it? Who is it for? Why does it matter?
- Must be understandable without reading rest of map

**Formula options**:
- `[Product] helps [audience] [achieve outcome] by [mechanism].`
- `[Product] is [category] that [differentiator] for [audience].`
- `For [audience] who [pain point], [Product] [solution].`

### Pillars
**Purpose**: Break down the value proposition into 3-4 distinct, memorable themes.

**Constraints**:
- Exactly 3-4 pillars (cognitive limit for retention)
- No overlap between pillars
- Each pillar must be independently valuable

**Common pillar types**:
- Functional benefit (what it does)
- Emotional benefit (how it feels)
- Economic benefit (cost/time savings)
- Risk reduction (what it prevents)
- Competitive differentiator (what only we do)

### Key message (per pillar)
**Purpose**: Single sentence claim for this pillar.

**Constraints**:
- One sentence, benefit-focused
- Should be defensible with proof points below

### Supporting messages
**Purpose**: Expand on the key message with specifics.

**Constraints**:
- 1-3 per pillar
- More specific than key message
- Still benefit-focused (not feature lists)

### Proof points
**Purpose**: Evidence that makes the claims believable.

**Types** (in order of strength):
1. Specific metrics ("40% faster", "10,000 customers")
2. Named customer results ("Acme Corp reduced X by Y")
3. Third-party validation (analyst quotes, certifications)
4. Feature evidence (specific capability that enables claim)

**Constraints**:
- Must be verifiable
- Must support the specific pillar (not generic company proof)
- Avoid vague language ("industry-leading", "best-in-class")

### Boilerplate
**Purpose**: Consistent company/product description for repeated use.

**Constraints**:
- 2-3 sentences
- Factual, not promotional
- Include: what it is, who it's for, scale/credibility signal

### Tagline options
**Purpose**: Short, memorable phrases for campaigns and assets.

**Constraints**:
- 5-10 words each
- Provide 2-3 options for testing
- Should align with core message but can emphasize different aspects

## Anti-patterns

| Anti-pattern | Problem | Fix |
|--------------|---------|-----|
| Feature-first | "We have AI and machine learning" | Reframe as outcome: "Predict issues before they happen" |
| Pillar overlap | Pillar 1: Speed, Pillar 2: Efficiency | Merge or differentiate themes |
| Vague proof | "Customers love us" | Add specifics: "4.8 star rating from 10,000 reviews" |
| Jargon | "Leverage our synergistic platform" | Plain language: "Work better across teams" |
| Too many pillars | 5+ themes | Consolidate to 3-4 most important |
| No audience | Generic "businesses" | Specify: "Marketing teams at B2B SaaS companies" |

## Validation checklist

Before finalizing a message map:

- [ ] Core message passes the 10-second test (someone can understand value quickly)
- [ ] Pillars are mutually exclusive (no theme overlap)
- [ ] Pillars are collectively exhaustive (cover the key value props)
- [ ] Every proof point is specific and verifiable
- [ ] Audience is defined specifically enough to guide decisions
- [ ] Messages are benefit-focused, not feature-focused
- [ ] Hierarchy is clear: each level adds detail to the level above
