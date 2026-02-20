# Templates

## Standard --help output structure

```
{command} - {one-line description ending with period}

USAGE
    {command} [OPTIONS] {REQUIRED_ARG} [{OPTIONAL_ARG}]

ARGUMENTS
    {REQUIRED_ARG}    {description} (required)
    {OPTIONAL_ARG}    {description} (default: {value})

OPTIONS
    -h, --help        Show this help message
    -v, --version     Show version information
    -{short}, --{long} {VALUE}
                      {description} (default: {value})
    --{flag}          {description for boolean flag}

EXAMPLES
    {command} {example 1}
        {What this example does}

    {command} {example 2}
        {What this example does}

ENVIRONMENT
    {VAR_NAME}        {description} (overrides --{flag})

SEE ALSO
    {command} {subcommand} --help
    {related-command}
```

## Usage string conventions

### Required argument
```
{command} {ARG}
```

### Optional argument
```
{command} [{ARG}]
```

### Repeatable argument
```
{command} {ARG}...
```

### Mutually exclusive options
```
{command} {--option-a | --option-b}
```

### Optional with default
```
{command} [{ARG}]    (default: {value})
```

### Combined short flags
```
{command} [-abc]     # Equivalent to -a -b -c
```

## Argument description template

```
    {ARG_NAME}        {What it is}. {Constraints if any}. {Default if optional}.
```

**Examples:**
```
    FILE              Path to input file. Must exist and be readable.
    COUNT             Number of items to return. Range: 1-1000. Default: 10.
    FORMAT            Output format. One of: json, yaml, table. Default: table.
```

## Flag/option description template

### Flag with value
```
    -{s}, --{long} {VALUE}
                      {What it controls}. {Type and constraints}. Default: {value}.
```

### Boolean flag
```
    --{flag}          {What enabling this does}. Disabled by default.
    --no-{flag}       {What disabling this does}. Use to override config file.
```

## Subcommand help template

```
{parent} {command} - {one-line description}

USAGE
    {parent} {command} [OPTIONS] {ARGS}

DESCRIPTION
    {2-3 sentences expanding on what this command does, when to use it,
    and any important behavioral notes.}

{Rest of standard structure}
```

## Command group listing template

```
{parent} - {one-line description of command group}

USAGE
    {parent} {COMMAND} [OPTIONS]

COMMANDS
    {cmd1}            {one-line description}
    {cmd2}            {one-line description}
    {cmd3}            {one-line description}

Run '{parent} {COMMAND} --help' for more information on a command.
```
