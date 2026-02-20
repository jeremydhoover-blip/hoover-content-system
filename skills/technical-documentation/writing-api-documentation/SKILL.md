---
name: writing-api-documentation
description: Create comprehensive API documentation covering endpoints, authentication, parameters, responses, and error handling. Use when documenting REST, GraphQL, or RPC APIs for developers.
---

# Writing API Documentation

## Quick start
Collect or infer:
- API type (REST, GraphQL, gRPC, WebSocket)
- Authentication mechanism
- Base URL and versioning scheme
- All endpoints with methods
- Request/response schemas
- Error codes and meanings

Then produce output using [TEMPLATES.md](TEMPLATES.md). Validate with [RUBRIC.md](RUBRIC.md).

## Workflow
1. Document authentication requirements and setup.
2. Define base URL, versioning, and common headers.
3. Group endpoints by resource or domain.
4. Document each endpoint with full request/response details.
5. Document all error codes with causes and resolutions.
6. Add executable examples for each endpoint.
7. Validate against actual API behavior.
8. Run the rubric check. Revise until it passes.

## Degrees of freedom
- **Low**: Endpoint documentation structure is strict.
- Allowed variation: Grouping strategy, example complexity, and pagination/filtering documentation depth may vary as long as rubric passes.

## State awareness
- If API has rate limits, document them prominently.
- If endpoints have different auth scopes, document per-endpoint requirements.
- If API version is deprecated, note migration path.
- If schema is available (OpenAPI, GraphQL SDL), cross-validate documentation.

## Failure modes to avoid
- Documenting happy path only without error cases
- Incomplete parameter documentation (missing types, constraints)
- Examples that don't match documented schemas
- Omitting authentication requirements

## References
- Templates: [TEMPLATES.md](TEMPLATES.md)
- Rubric: [RUBRIC.md](RUBRIC.md)
- Examples: [EXAMPLES.md](EXAMPLES.md)
- API documentation structure: [reference/api-doc-structure.md](reference/api-doc-structure.md)
