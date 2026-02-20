# Rubric

Pass if all are true:

- [ ] API overview page documents base URL, auth, and common patterns
- [ ] Authentication method clearly documented with working example
- [ ] Each endpoint has HTTP method and full path
- [ ] All path parameters documented with types
- [ ] All query parameters documented with types and defaults
- [ ] All request body fields documented with types, requirements, constraints
- [ ] Success response includes example and field documentation
- [ ] Error responses documented with status codes and error codes
- [ ] At least one executable curl/code example per endpoint
- [ ] Examples match documented request/response schemas
- [ ] Rate limits documented if applicable
- [ ] Pagination documented for list endpoints

Fail if any are true:

- Base URL or authentication not documented
- Parameters missing type information
- Optional parameters missing default values
- Response fields undocumented
- Error cases not covered
- Examples don't match documented schemas
- Examples not executable (missing required parameters)
- List endpoints missing pagination documentation
- Different endpoints use inconsistent documentation format
