---
name: maintaining-docs-as-code
description: Manage documentation using software development practices including version control, CI/CD, automated testing, and review workflows. Use when documentation lives alongside code or requires the same rigor as code.
---

# Maintaining Docs as Code

## Quick start
Collect or infer:
- Documentation format (Markdown, AsciiDoc, RST)
- Repository structure and branching strategy
- Build tooling (static site generator, linter)
- Review and approval workflow
- Deployment target (static hosting, docs platform)

Then produce output using [TEMPLATES.md](TEMPLATES.md). Validate with [RUBRIC.md](RUBRIC.md).

## Workflow
1. Define documentation file structure and naming conventions.
2. Configure linting and validation in CI.
3. Set up build pipeline for documentation site.
4. Establish review workflow (PR requirements, reviewers).
5. Configure deployment automation.
6. Document the contribution process.
7. Run the rubric check. Revise until it passes.

## Degrees of freedom
- **Medium**: Tooling choices can vary based on ecosystem.
- Allowed variation: Static site generator, hosting platform, and CI system may vary as long as rubric passes.

## State awareness
- If documentation is in a monorepo, configure selective builds.
- If multiple contributors, establish style enforcement.
- If translations exist, handle localization workflow.
- If versioned docs needed, configure version branches or directories.

## Failure modes to avoid
- No automated validation (broken links, invalid syntax)
- Missing contribution guidelines
- Build failures not blocking merge
- No preview environment for review
- Documentation and code changes in separate PRs without linking

## References
- Templates: [TEMPLATES.md](TEMPLATES.md)
- Rubric: [RUBRIC.md](RUBRIC.md)
- Examples: [EXAMPLES.md](EXAMPLES.md)
- Tooling patterns: [reference/docs-tooling.md](reference/docs-tooling.md)
