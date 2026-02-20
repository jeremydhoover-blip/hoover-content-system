# Hoover Content System (HCS)

A skill-based system for content creation. Each skill is a structured package with defined inputs, workflows, templates, and quality criteria.

## What This Is

HCS provides repeatable skills for:

- **UX Writing** – Error messages, empty states, dialogs, notifications, forms, onboarding
- **Content Design** – UI copy systems, patterns, audits, naming, cognitive load
- **Content Strategy** – Voice/tone, taxonomy, messaging hierarchy, roadmaps
- **Content Context** – Feature context packs, vocabulary, state maps, user journeys
- **Technical Documentation** – How-to guides, API docs, reference docs, release notes
- **Developer Content** – CLI help, SDK docs, code comments, configuration guides
- **Marketing** – Landing pages, product messaging, campaigns, app store listings
- **Editorial** – Blog posts, case studies, thought leadership, tutorials
- **MCP & Agents** – Agent instructions, system prompts, tool descriptions, evals
- **Research & Insights** – User research synthesis, feedback analysis, audit reports

## Repo Structure

```
/skills/              → Skill packages organized by category
/shared/              → Global standards (apply to ALL outputs)
/governance/          → Rules, catalog, glossary, naming conventions
/evals/               → Test cases for skill validation
```

## Skill Package Structure

Each skill folder contains:

| File | Purpose |
|------|---------|
| `SKILL.md` | Entry point. Triggers, inputs, workflow, degrees of freedom. |
| `TEMPLATES.md` | Output structures and formats. |
| `RUBRIC.md` | Pass/fail quality criteria. |
| `EXAMPLES.md` | Input/output pairs showing correct execution. |

## How to Use

1. **Find the skill** – Check `governance/skill-catalog.md` or match by trigger keywords
2. **Read SKILL.md** – Understand required inputs and workflow
3. **Apply shared standards** – All outputs follow `/shared` guidelines
4. **Use templates** – Follow `TEMPLATES.md` for output format
5. **Validate** – Check against `RUBRIC.md` criteria

## Getting Started: Write an Error Message

Here's a quick walkthrough using the `writing-error-messages` skill.

### 1. Gather inputs

You need:
- **Error type:** validation, system, network, permission, or not-found
- **Severity:** blocking, degraded, or informational
- **User action:** what the user was trying to do
- **Recovery actions:** what they can do next

**Example scenario:** User tries to save a file but their session expired.

### 2. Open the skill

Read `skills/ux-writing/writing-error-messages/SKILL.md` for the workflow.

### 3. Apply the template

From `TEMPLATES.md`, error messages use this structure:

```
Title: [What happened – max 60 chars]
Body: [Why it happened – max 150 chars, optional]
Action: [What to do – max 25 chars]
```

### 4. Write the copy

```
Title: Your session expired
Body: Sign in again to save your changes.
Action: Sign in
```

### 5. Validate against the rubric

Check `RUBRIC.md`:
- ✅ Title under 60 characters
- ✅ No user blame
- ✅ Clear recovery action
- ✅ No technical jargon

Done. You've executed a skill.

## Ready-to-Use Prompts

Don't want to read the docs? **[PROMPTS.md](PROMPTS.md)** has copy-paste prompts for every skill category:

- UX writing (errors, empty states, dialogs, onboarding)
- Content design (naming, audits, microcopy systems)
- Content strategy (voice/tone, messaging, briefs)
- Technical docs (how-tos, release notes, API docs)
- Developer content (CLI help, code comments)
- Marketing (landing pages, announcements, emails)
- MCP & agents (system prompts, tool descriptions)
- Research (synthesis, feedback analysis)
- Validation (rubric checks, style checks, accessibility)

Just fill in the brackets and go.

## Shared Standards

All outputs comply with:

| File | Governs |
|------|---------|
| `shared/style.md` | Capitalization, punctuation, formatting |
| `shared/voice.md` | Voice attributes, tone boundaries |
| `shared/accessibility.md` | Inclusive language, reading level |
| `shared/localization.md` | Translation-ready patterns |
| `shared/legal-safety.md` | Prohibited claims, disclosures |

## For AI Agents

This repo includes instruction files for AI assistants:

- `.github/copilot-instructions.md` – GitHub Copilot
- `CLAUDE.md` – Claude
- `AGENTS.md` – Generic agents
- `.cursorrules` – Cursor

Each file contains the skill trigger index for fast matching.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to add or update skills.

## License

[MIT](LICENSE)