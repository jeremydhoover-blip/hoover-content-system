# Governance

## Scope

This folder defines rules for the skill repository itself—how skills are created, named, organized, and evaluated. These rules govern the system, not content outputs.

## Purpose

- Enforce consistency across all skill packages
- Define the contract between skills and shared standards
- Provide schemas and specifications for contributors

## Files

| File | Governs |
|------|---------|
| `system-rules.md` | Skill behavior, conflict resolution, inheritance |
| `naming.md` | Naming conventions for skills, files, folders, identifiers |
| `glossary.json` | Canonical terms, prohibited synonyms, product vocabulary |
| `skill-catalog.md` | Master list of all skills with category, purpose, triggers |
| `eval-spec.md` | Schema and validation rules for eval files |

## How It All Works Together

```
┌─────────────────────────────────────────────────────────────┐
│                      GOVERNANCE LAYER                       │
│  (Rules for building and maintaining the skill system)      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   system-rules.md ──► Defines skill structure requirements  │
│          │            (every skill needs SKILL.md, etc.)    │
│          ▼                                                  │
│   naming.md ─────────► Defines naming conventions           │
│          │            (gerund prefixes, kebab-case, etc.)   │
│          ▼                                                  │
│   skill-catalog.md ──► Lists all skills with triggers       │
│          │            (source of truth for skill discovery) │
│          ▼                                                  │
│   eval-spec.md ──────► Defines eval file schema             │
│          │            (how to structure test cases)         │
│          ▼                                                  │
│   glossary.json ─────► Defines canonical terminology        │
│                       (consistent terms across all skills)  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                       SHARED LAYER                          │
│  (Rules for content outputs—applies to ALL skill outputs)   │
├─────────────────────────────────────────────────────────────┤
│   style.md ──────► Capitalization, punctuation, formatting  │
│   voice.md ──────► Voice attributes, tone boundaries        │
│   accessibility.md ► Inclusive language, reading level      │
│   localization.md ─► Translation-ready patterns             │
│   legal-safety.md ─► Prohibited claims, disclosures         │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                       SKILL LAYER                           │
│  (Domain-specific rules that extend shared standards)       │
├─────────────────────────────────────────────────────────────┤
│   SKILL.md ─────► Entry point: inputs, workflow, triggers   │
│   TEMPLATES.md ─► Output structure and format               │
│   RUBRIC.md ────► Pass/fail quality criteria                │
│   EXAMPLES.md ──► Input/output pairs showing execution      │
└─────────────────────────────────────────────────────────────┘
```

## Rule Precedence

When rules conflict, they resolve in this order:

1. **Governance rules** (highest priority) — Cannot be overridden
2. **Shared standards** — Apply to all outputs, skills can extend but not contradict
3. **Skill-level rules** — Domain-specific, scoped to the skill

## Governance vs. Shared

| Governance | Shared |
|------------|--------|
| Rules for building skills | Rules for content outputs |
| "Skill names use gerunds" | "Use sentence case" |
| "Each skill needs an eval" | "Don't use ableist terms" |
| Applied when maintaining repo | Applied when doing content work |

## How to Use This Folder

**When adding a skill:**
1. Check `naming.md` for naming rules
2. Add entry to `skill-catalog.md`
3. Follow structure defined in `system-rules.md`
4. Create eval file per `eval-spec.md` (optional for initial contribution)

**When updating a skill:**
1. Check `system-rules.md` for change constraints
2. Update `skill-catalog.md` if triggers change
3. Update eval file if behavior changes

**When resolving conflicts:**
1. `governance/` rules override skill-level rules
2. `shared/` standards override skill-specific content rules
3. Skill rules override defaults only within their scope