# Templates

## Default SDK documentation structure

```md
# {SDK Name} SDK for {Language}

## Overview
{One sentence: what the SDK does and what service it connects to.}

## Prerequisites
- {Language} {minimum version}
- {Dependency requirements}
- {Account or API key requirement}

## Installation

### {Package manager 1}
```{language}
{install command}
```

### {Package manager 2} (if applicable)
```{language}
{alternative install command}
```

## Authentication

### Option 1: {Auth method name}
```{language}
{code showing credential instantiation}
```

### Option 2: {Alternative auth method}
```{language}
{code showing alternative}
```

## Quickstart

### {Primary operation name}
```{language}
{complete working example with imports, setup, execution, cleanup}
```

**What this code does:**
1. {Step 1 explanation}
2. {Step 2 explanation}
3. {Step 3 explanation}

## Operations

### {Operation category 1}

#### {Specific operation}
```{language}
{code sample}
```

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| {param}   | {type} | {yes/no} | {what it does} |

**Returns:** {return type and structure}

### {Operation category 2}
{Repeat pattern}

## Error handling

### Common errors
| Error code | Cause | Resolution |
|------------|-------|------------|
| {code}     | {why} | {fix}      |

### Error handling pattern
```{language}
{try-catch or equivalent with specific error types}
```

## Advanced usage

### {Pattern 1: e.g., Pagination}
```{language}
{code sample}
```

### {Pattern 2: e.g., Retry logic}
```{language}
{code sample}
```

## Troubleshooting
| Symptom | Likely cause | Solution |
|---------|--------------|----------|
| {symptom} | {cause} | {solution} |

## Next steps
- {Link to API reference}
- {Link to advanced guides}
- {Link to samples repository}
```

## Code sample template

```{language}
// Purpose: {one line explaining what this sample demonstrates}
// Prerequisites: {what must be set up before running}

{imports}

{configuration or setup}

{main operation with inline comments on non-obvious lines}

{cleanup if applicable}

// Expected output:
// {what the developer should see}
```

## Inline comment conventions

```{language}
// REQUIRED: {explanation of required parameter or step}
// OPTIONAL: {explanation of optional parameter with default behavior}
// NOTE: {important context that affects behavior}
// WARNING: {potential issue or destructive behavior}
// TODO: {placeholder for user customization}
```
