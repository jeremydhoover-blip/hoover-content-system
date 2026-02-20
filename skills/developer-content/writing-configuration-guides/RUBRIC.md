# Rubric

Pass if all are true:
- Every parameter has type, description, and at least one valid example value
- Required parameters are clearly separated from optional parameters
- Default values are documented for all optional parameters
- Constraints (min, max, allowed values, format) are explicit where applicable
- Security-sensitive parameters are flagged with handling guidance
- A minimal "quick start" config example is provided
- Environment variable mappings are documented if supported
- Configuration priority order is stated when multiple methods exist
- Units are specified for numeric values (seconds, bytes, etc.)
- Examples use realistic values, not placeholders like "your-value-here"

Fail if any are true:
- Parameter documented without type
- Required parameter missing from quick-start example
- Secret value shown in plain text without security warning
- Default value undocumented for optional parameter
- Constraint exists but is not documented (discovered only through error)
- Configuration file format not specified (JSON, YAML, TOML, etc.)
- Environment variable naming convention inconsistent
