# CLI Style Guide

## One-line description rules

| Rule | Correct | Incorrect |
|------|---------|-----------|
| Start with verb | "Convert images between formats." | "Image converter utility." |
| End with period | "List all resources." | "List all resources" |
| ≤80 characters | "Deploy application to cloud." | "Deploy application to cloud infrastructure including Kubernetes and serverless." |
| No version numbers | "Manage configuration files." | "Manage configuration files (v2.0)." |
| No redundant "command" | "Sync local and remote files." | "Command to sync files." |

## Argument naming conventions

### Positional arguments
- Use UPPER_CASE in usage strings: `FILE`, `PATH`, `COUNT`
- Use lower-case in descriptions: "file", "path", "count"
- Prefer descriptive names: `SOURCE` and `DEST` over `ARG1` and `ARG2`

### Common argument names
| Name | Use for |
|------|---------|
| `FILE` | Single file path |
| `PATH` | Directory or file path |
| `DIR` | Directory only |
| `URL` | Web address |
| `NAME` | Identifier or resource name |
| `PATTERN` | Glob or regex pattern |
| `COMMAND` | Subcommand name |
| `KEY=VALUE` | Key-value pair input |

## Flag naming conventions

### Short flags
- Single letter, case-sensitive
- Reserve common flags:
  - `-h` for help
  - `-v` for version (or verbose, but prefer `--verbose`)
  - `-q` for quiet
  - `-f` for force or file
  - `-o` for output
  - `-n` for dry-run or count

### Long flags
- Use kebab-case: `--output-format`, not `--outputFormat`
- Be explicit: `--recursive` not `--r`
- Boolean flags: `--flag` to enable, `--no-flag` to disable

### Flag value conventions
| Value type | Format | Example |
|------------|--------|---------|
| File path | Accepts relative or absolute | `--config ./config.yaml` |
| Enum | List valid values | `--format {json,yaml,table}` |
| Number | Show range if constrained | `--count N (1-100)` |
| Duration | Use unit suffix | `--timeout 30s` |
| Size | Use unit suffix | `--max-size 10MB` |

## Description writing rules

### Do
- Explain what happens when used
- State type constraints
- Document defaults
- Note side effects

### Don't
- Repeat the flag name as description
- Use jargon without explanation
- Assume knowledge of internals
- Include marketing language

### Examples of good descriptions

```
--recursive       Process directories recursively. Without this flag,
                  only files in the specified directory are processed.

--timeout SECONDS Maximum time to wait for response. Range: 1-300.
                  Default: 30. Use 0 for no timeout.

--force           Skip confirmation prompts and overwrite existing files.
                  Use with caution in scripts.
```

### Examples of bad descriptions

```
--recursive       Enable recursive mode.
                  (Just restates the flag name)

--timeout         Timeout value.
                  (Missing type, range, default)

--force           Forces the operation.
                  (Doesn't explain what that means)
```

## Example formatting

### Structure
```
    {command with realistic arguments}
        {One line explaining the goal, not the syntax}
```

### Good examples
```
    vault get secrets/prod/db-password
        Retrieve the production database password.

    imgconv -r 800x -q 85 photo.jpg thumbnail.webp
        Create an 800px-wide WebP thumbnail at 85% quality.
```

### Bad examples
```
    vault get PATH
        Get a secret at PATH.
        (Uses placeholder instead of realistic value)

    imgconv -r 800x -q 85 photo.jpg thumbnail.webp
        Use -r to resize and -q to set quality.
        (Restates options instead of explaining goal)
```

## Terminal width considerations

- Target 80 characters for compatibility
- Wrap long descriptions at option column (typically 18-20 chars)
- For very long option names, put description on next line

```
    --very-long-option-name
                      Description starts on next line when option
                      name is too long.
```
