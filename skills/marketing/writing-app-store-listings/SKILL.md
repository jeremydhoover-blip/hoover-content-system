---
name: writing-app-store-listings
description: Creates optimized app store listings for iOS and Android. Use when publishing apps, games, or major updates to Apple App Store or Google Play.
---

# Writing app store listings

## Quick start
Collect or infer:
- App name and category
- Target platform (iOS, Android, or both)
- Core features (3-5 key capabilities)
- Target audience and primary use cases
- Differentiators from competitors
- Screenshots/preview context

Then produce output using [TEMPLATES.md](TEMPLATES.md). Validate with [RUBRIC.md](RUBRIC.md).

## Workflow
1. Confirm platform and extract character limits from [reference/platform-requirements.md](reference/platform-requirements.md).
2. Draft app name and subtitle/short description (highest SEO value).
3. Write description: hook → features → social proof → CTA.
4. Identify and place keywords naturally (iOS) or in dedicated field (Android).
5. Write "What's New" section for version updates.
6. Run validation script to check character limits.
7. Run the rubric check. Revise until it passes.

## Degrees of freedom
- **Low**: Character limits, required fields, and keyword placement rules are fixed per platform.
- **Medium**: Tone, feature ordering, and formatting within limits.
- Allowed variation: Description structure, feature emphasis, CTA phrasing—as long as rubric passes.

## References
- Templates: [TEMPLATES.md](TEMPLATES.md)
- Rubric: [RUBRIC.md](RUBRIC.md)
- Examples: [EXAMPLES.md](EXAMPLES.md)
- Platform requirements: [reference/platform-requirements.md](reference/platform-requirements.md)
- Validation: [scripts/character_limit_validator.py](scripts/character_limit_validator.py)
