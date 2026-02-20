# Security Policy

## Scope

The Hoover Content System (HCS) is a skills repository covering content design, UX writing, content strategy, technical documentation, developer content, marketing, editorial, AI/MCP agent design, and research synthesis. It contains documentation, templates, and guidelines—not executable code. Security concerns focus on content integrity, appropriate use, and AI safety.

## Reporting Issues

### Content Integrity Issues

Report if you find:
- Guidance that could lead to harmful, misleading, or deceptive content
- Templates that produce legally problematic outputs
- Examples containing sensitive, proprietary, or inappropriate information
- Broken references to governance files or shared standards
- Skills that contradict each other or established standards

### AI and Agent Safety Issues

Report if you find:
- Agent instructions or system prompts that could enable harmful outputs
- Guardrails in `mcp-and-agents` skills that can be bypassed
- Context injection patterns that expose sensitive information
- Evaluation frameworks that don't catch harmful edge cases
- Tool descriptions that misrepresent capabilities or risks

### Misuse Concerns

Report if you observe:
- Skills being used to generate deceptive or manipulative content
- Marketing or conversion copy skills producing misleading claims
- Outputs that violate the constraints in `shared/legal-safety.md`
- Patterns that bypass guardrails defined in skills

## How to Report

1. **Public issues:** Open a GitHub issue for non-sensitive concerns.
2. **Private reports:** For sensitive matters, contact maintainers directly via the repository's security advisory feature.

## Response

- Maintainers will acknowledge reports within 7 days.
- Valid issues will be addressed in the next update cycle.
- Reporters will be credited unless they request anonymity.

## Out of Scope

- Vulnerabilities in tools used alongside this repo (report to those projects)
- AI model behavior outside of skill instructions (report to model providers)
- General content feedback (use standard issues or discussions)

## Content Safety

All skills must comply with `shared/legal-safety.md`. Skills producing content that violates these standards should be reported for review.
