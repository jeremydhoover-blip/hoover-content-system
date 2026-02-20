# Vocabulary Naming Principles

## Core principles

### 1. User mental model alignment
Terms should match how users naturally think and talk about concepts.

| Principle | Guideline | Example |
|-----------|-----------|---------|
| Use research-validated terms | If user research shows a term is understood, prefer it | "Workspace" over "org" when research confirms comprehension |
| Match domain conventions | Align with terms users know from similar products | "Folder" for hierarchical organization in file systems |
| Avoid internal jargon | Don't expose engineering or business terminology | "Project" not "entity" or "resource" |

### 2. Precision over brevity
A slightly longer term that's accurate is better than a short term that's ambiguous.

| Principle | Guideline | Example |
|-----------|-----------|---------|
| One term, one concept | Each term should refer to exactly one thing | "pause notifications" not "mute" (which implies blocking) |
| Scope clarity | Definition should specify boundaries | "member" = person in workspace (not user in general) |
| Distinguish similar concepts | Related concepts need distinguishable terms | "owner" vs "member" vs "guest" |

### 3. Consistency at all costs
Inconsistent terminology creates cognitive load and support burden.

| Principle | Guideline | Example |
|-----------|-----------|---------|
| Same term everywhere | Use identical term across all touchpoints | "workspace" in nav, settings, emails, help docs |
| Same definition everywhere | Term meaning shouldn't shift by context | "member" always means workspace member |
| Adjacent feature alignment | Check neighboring features for term reuse | If "project" exists elsewhere, align or differentiate |

### 4. Actionability for verbs
Verb terms should clearly imply what will happen.

| Principle | Guideline | Example |
|-----------|-----------|---------|
| Clear outcome | User should predict result from term | "Delete" not "Remove" when it's permanent |
| Appropriate force | Match term intensity to action severity | "Cancel subscription" not "Unsubscribe" for paid accounts |
| Specific over generic | Avoid terms that could mean many things | "Invite" not "Add" for people (implies consent) |

## Naming decision checklist

Before finalizing a term, verify:

- [ ] **Comprehension:** Would a new user understand this term without explanation?
- [ ] **Uniqueness:** Is this term used for only one concept in the product?
- [ ] **Differentiation:** Does this term clearly differ from related concepts?
- [ ] **Consistency:** Is this term used identically across all contexts?
- [ ] **Platform alignment:** Does this term fit platform conventions (iOS, Android, web)?
- [ ] **Localization readiness:** Can this term be translated accurately?
- [ ] **Searchability:** Will users find help content using this term?

## Term formation patterns

### Noun terms (objects, concepts)
| Pattern | Use when | Examples |
|---------|----------|----------|
| Simple noun | Concept is familiar and unambiguous | folder, file, project |
| Noun + qualifier | Need to distinguish from similar concept | team workspace, personal account |
| Compound noun | Two concepts combine to form new one | dashboard, checkbox |

### Verb terms (actions)
| Pattern | Use when | Examples |
|---------|----------|----------|
| Simple verb | Action is common and clear | save, delete, create |
| Verb + object | Need to specify what's affected | invite member, create project |
| Phrasal verb | Natural language pattern exists | sign in, log out |

### State terms (conditions)
| Pattern | Use when | Examples |
|---------|----------|----------|
| Adjective | Describing current condition | active, pending, archived |
| Past participle | Result of completed action | saved, deleted, invited |
| Present participle | Ongoing process | loading, uploading, syncing |

## Anti-patterns to avoid

| Anti-pattern | Problem | Fix |
|--------------|---------|-----|
| **Synonym variation** | Using "save/store/keep" interchangeably | Pick one, prohibit others |
| **Abbreviation in UI** | "Config" instead of "Configuration" | Spell out in UI, abbreviate in code only |
| **Category-as-instance** | Calling a specific thing by its type ("content" for a blog post) | Use specific term |
| **False cognate** | Term means different things in different languages | Research localization implications |
| **Trademark conflict** | Using terms that belong to other products | Legal review for risk terms |
| **Feature name as concept** | "Use Smart Inbox to organize" | Describe the concept, not the feature name |
