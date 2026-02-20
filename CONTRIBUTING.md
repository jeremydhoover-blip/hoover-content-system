# Contributing

Thank you for your interest in contributing to the Hoover Content System (HCS).

## Code of Conduct

By participating, you agree to uphold our [Code of Conduct](CODE_OF_CONDUCT.md).

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/YOUR-USERNAME/hcs.git`
3. Create a branch: `git checkout -b your-branch-name`
4. Make your changes
5. Push and open a pull request

## How to Contribute

### Suggesting a New Skill

Use the [Skill Request issue template](https://github.com/jeremydhoover-blip/hoover-content-system/issues/new?template=skill-request.md) to propose new skills.

### Reporting Issues

Use the [Bug Report template](https://github.com/jeremydhoover-blip/hoover-content-system/issues/new?template=bug-report.md) for problems with existing skills or standards.

### Adding a New Skill

1. Check `governance/skill-catalog.md` to ensure the skill doesn't already exist.
2. Follow naming rules in `governance/naming.md`.
3. Create skill folder with required files:
   - `SKILL.md`
   - `TEMPLATES.md`
   - `RUBRIC.md`
   - `EXAMPLES.md`
4. Create eval file in `/evals` following `governance/eval-spec.md`.
5. Add entry to `governance/skill-catalog.md`.
6. Submit pull request.

### Updating an Existing Skill

1. Review `governance/system-rules.md` for change constraints.
2. Update skill files as needed.
3. Update eval file if behavior changes.
4. Update `governance/skill-catalog.md` if triggers change.
5. Submit pull request with clear description of changes.

### Updating Shared Standards

1. Changes to `/shared` affect all skills.
2. Provide rationale for the change.
3. Verify change doesn't break existing skills.
4. Submit pull request for review.

## Pull Request Requirements

- [ ] Follows naming conventions in `governance/naming.md`
- [ ] Includes all required files for new skills
- [ ] Eval file passes validation per `governance/eval-spec.md`
- [ ] No violations of `governance/system-rules.md`
- [ ] Content follows standards in `/shared`
- [ ] Skill catalog updated if applicable

## Review Process

1. Maintainers review for compliance with governance rules.
2. Content reviewed for quality and consistency.
3. Eval coverage verified.
4. Feedback addressed before merge.

## Questions

- **General questions:** Open a [Discussion](https://github.com/jeremydhoover-blip/hoover-content-system/discussions)
- **Bugs or issues:** Use the [issue templates](https://github.com/jeremydhoover-blip/hoover-content-system/issues/new/choose)
- **Direct contact:** Reach out to [@jeremydhoover-blip](https://github.com/jeremydhoover-blip)

## Thank You

Every contribution helps make HCS better for content designers, UX writers, and teams everywhere.