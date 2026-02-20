# Templates

## Default output: Configuration reference

Use this as the default structure for configuration documentation:

```md
# Configuration Reference

## Quick start

Minimal configuration to get started:

```<format>
<minimal config example>
```

## Configuration methods

This application accepts configuration via:
- [ ] Configuration file (`<filename>`)
- [ ] Environment variables
- [ ] CLI flags
- [ ] Programmatic API

Priority order (highest to lowest): <list>

---

## Required parameters

### `<parameter_name>`
- **Type**: <string | number | boolean | array | object>
- **Format**: <specific format if applicable>
- **Description**: <what it controls>
- **Example**: `<valid value>`

---

## Optional parameters

### `<parameter_name>`
- **Type**: <type>
- **Default**: `<default value>`
- **Description**: <what it controls>
- **Constraints**: <min/max, allowed values, regex pattern>
- **Example**: `<valid value>`

---

## Environment variables

| Variable | Maps to | Example |
|----------|---------|---------|
| `<ENV_VAR>` | `<parameter>` | `<value>` |

---

## Security-sensitive parameters

> ⚠️ These parameters contain secrets. Never commit to version control.

### `<secret_parameter>`
- **Type**: <type>
- **Description**: <purpose>
- **Secure handling**: <how to manage: env var, secret manager, etc.>

---

## Full configuration example

```<format>
<complete config with comments>
```
```

## Variant: Environment-specific configuration

```md
# Environment Configuration

## Base configuration
<shared across all environments>

## Development overrides
<dev-specific values and why>

## Production overrides
<prod-specific values and why>

## Validation
Run `<validation command>` to verify configuration.
```

## Variant: Feature flag configuration

```md
# Feature Flags

## Flag reference

### `<flag_name>`
- **Type**: boolean
- **Default**: `false`
- **Stage**: <experimental | beta | ga>
- **Description**: <what it enables>
- **Dependencies**: <other flags or config required>

## Enabling flags

### Via config file
```<format>
<example>
```

### Via environment variable
```bash
<FEATURE_FLAG_NAME>=true
```
```
