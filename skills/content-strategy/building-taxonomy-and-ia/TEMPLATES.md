# Templates

## Default taxonomy structure

```md
# Taxonomy: [Product/Domain Name]

## Taxonomy principles
- **Mutual exclusivity:** Each item belongs to exactly one category
- **Exhaustiveness:** Every content type has a home
- **User-centric:** Categories match user mental models, not internal org structure
- **Scalable:** Structure accommodates growth without restructuring

---

## Hierarchy

### Level 0: Root

### Level 1: Primary categories
| Category | Description | Contains |
|----------|-------------|----------|
| [Category 1] | [What belongs here] | [Content types] |
| [Category 2] | [What belongs here] | [Content types] |
| [Category 3] | [What belongs here] | [Content types] |

### Level 2: Subcategories

#### [Category 1]
| Subcategory | Description | Contains |
|-------------|-------------|----------|
| [Sub 1.1] | [What belongs here] | [Content types] |
| [Sub 1.2] | [What belongs here] | [Content types] |

#### [Category 2]
| Subcategory | Description | Contains |
|-------------|-------------|----------|
| [Sub 2.1] | [What belongs here] | [Content types] |
| [Sub 2.2] | [What belongs here] | [Content types] |

### Level 3: [Only if necessary]
[Additional detail]

---

## Content type mapping

| Content type | Primary location | Cross-link locations |
|--------------|------------------|---------------------|
| [Type 1] | [Category > Sub] | [Other relevant locations] |
| [Type 2] | [Category > Sub] | [Other relevant locations] |

---

## Navigation labels

| Internal category name | User-facing label | Why |
|-----------------------|-------------------|-----|
| [Internal] | [External] | [Reasoning] |

---

## Decision rules

### Where does [content type] go?
1. If [condition], place in [Category A]
2. If [condition], place in [Category B]
3. Default to [Category C]

### Handling edge cases
- **Cross-cutting content:** Primary home in [X], cross-linked from [Y]
- **Temporary content:** Lives in [location], archived after [timeframe]
- **Deprecated content:** Moved to [archive location], redirect maintained

---

## Governance

### Adding new categories
1. [Approval process]
2. [Criteria for new category]
3. [Update process]

### Reviewing structure
- Review frequency: [quarterly/annually]
- Trigger for restructure: [criteria]
```

## Visual hierarchy map

```
[Root]
├── [Category 1]
│   ├── [Subcategory 1.1]
│   └── [Subcategory 1.2]
├── [Category 2]
│   ├── [Subcategory 2.1]
│   └── [Subcategory 2.2]
└── [Category 3]
    ├── [Subcategory 3.1]
    └── [Subcategory 3.2]
```
