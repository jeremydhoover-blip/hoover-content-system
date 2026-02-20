# Rubric

## Pass criteria
All must be true:

### Structural requirements
- [ ] Documentation includes installation, authentication, quickstart, and error handling sections
- [ ] Every code sample is syntactically valid for the target language
- [ ] Every code sample includes required imports and setup—no hidden dependencies
- [ ] Parameter tables include type, required status, and description for all parameters
- [ ] Code samples include inline comments for non-obvious operations

### Completeness requirements
- [ ] Authentication section covers at least two methods (or explains why only one exists)
- [ ] Quickstart sample is complete and runnable without modification (except credentials)
- [ ] Error handling section includes at least three common error scenarios
- [ ] Advanced usage section covers pagination, retries, or streaming if SDK supports them

### Developer experience requirements
- [ ] Samples progress from simple to complex (quickstart → advanced)
- [ ] Each sample states its purpose in the first comment or heading
- [ ] Expected output or behavior is documented for each sample
- [ ] Troubleshooting table maps symptoms to causes to solutions

### Consistency requirements
- [ ] Variable naming follows target language conventions
- [ ] Code style matches SDK's official examples or language style guide
- [ ] Terminology is consistent throughout (same names for same concepts)

## Fail criteria
Fail if any are true:

- Code sample has syntax errors or missing imports
- Authentication sample hardcodes credentials without placeholder explanation
- Quickstart requires undocumented prerequisites
- Error handling shows generic catch-all without specific error types
- Parameter table is missing for any operation with more than two parameters
- Samples use deprecated methods without migration guidance
- Documentation references features not available in the documented SDK version
- Inline comments state the obvious (e.g., `// create a client` above `client = new Client()`)
