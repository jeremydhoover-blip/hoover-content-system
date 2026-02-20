# Examples

## Example 1: Simple file processing command

**Input:**
- Command: `imgconv` (image converter)
- Function: Convert image formats
- Args: input file (required), output file (optional, derives from input)
- Options: format, quality, resize

**Output:**

```
imgconv - Convert images between formats.

USAGE
    imgconv [OPTIONS] INPUT [OUTPUT]

ARGUMENTS
    INPUT             Path to source image file. Must exist.
    OUTPUT            Path for converted file. Default: INPUT with new extension.

OPTIONS
    -h, --help        Show this help message
    -v, --version     Show version information
    -f, --format FORMAT
                      Target format. One of: png, jpg, webp, avif. Default: png.
    -q, --quality PERCENT
                      Compression quality for lossy formats. Range: 1-100. Default: 85.
    -r, --resize WxH  Resize to width x height in pixels. Maintains aspect ratio
                      if only one dimension specified (e.g., 800x or x600).
    --overwrite       Overwrite output file if it exists. Prompts by default.

EXAMPLES
    imgconv photo.jpg
        Convert photo.jpg to photo.png using defaults.

    imgconv -f webp -q 90 photo.jpg optimized.webp
        Convert to WebP format at 90% quality.

    imgconv -r 800x photo.jpg thumbnail.png
        Resize to 800px width, maintaining aspect ratio.

ENVIRONMENT
    IMGCONV_FORMAT    Default output format (overrides --format default)
    IMGCONV_QUALITY   Default quality (overrides --quality default)

SEE ALSO
    imgconv batch --help    Convert multiple files
    imgconv info --help     Show image metadata
```

---

## Example 2: Command group with subcommands

**Input:**
- Command group: `vault` (secrets manager CLI)
- Subcommands: login, get, set, list, delete
- Context: Enterprise tool with auth requirements

**Output:**

```
vault - Manage secrets in the corporate vault.

USAGE
    vault COMMAND [OPTIONS]

COMMANDS
    login             Authenticate with the vault server
    get               Retrieve a secret value
    set               Store or update a secret
    list              List secrets in a path
    delete            Remove a secret permanently

GLOBAL OPTIONS
    -h, --help        Show this help message
    -v, --version     Show version information
    --vault-addr URL  Vault server address. Default: $VAULT_ADDR or https://vault.internal
    --namespace NS    Vault namespace. Required for enterprise deployments.
    -o, --output FORMAT
                      Output format. One of: text, json, yaml. Default: text.

EXAMPLES
    vault login
        Start interactive authentication.

    vault get secrets/myapp/database-password
        Retrieve a specific secret value.

    vault list secrets/myapp/
        List all secrets under a path.

Run 'vault COMMAND --help' for more information on a command.
```

**Subcommand help (`vault get --help`):**

```
vault get - Retrieve a secret value.

USAGE
    vault get [OPTIONS] PATH

DESCRIPTION
    Fetches a secret from the vault at the specified path. Returns the
    current version by default. Use --version to retrieve historical values.
    Requires read permission on the path.

ARGUMENTS
    PATH              Full path to the secret (e.g., secrets/myapp/api-key).

OPTIONS
    -h, --help        Show this help message
    --version N       Retrieve specific version. Default: latest.
    --field FIELD     Return only this field from the secret data.
    -o, --output FORMAT
                      Output format. One of: text, json, yaml. Default: text.

EXAMPLES
    vault get secrets/prod/database-url
        Get the current database URL.

    vault get --field password secrets/prod/db-creds
        Get only the password field from credentials.

    vault get --version 3 secrets/prod/api-key
        Get version 3 of the API key (for rollback investigation).

SEE ALSO
    vault set --help      Store a secret
    vault list --help     List available secrets
```

---

## Example 3: Edge case—command with complex mutually exclusive options

**Input:**
- Command: `deploy`
- Context: Deployment tool with multiple target types
- Challenge: Mutually exclusive deployment targets

**Output:**

```
deploy - Deploy application to target environment.

USAGE
    deploy [OPTIONS] {--kubernetes | --lambda | --vm} APP_PATH

ARGUMENTS
    APP_PATH          Path to application directory or archive.

TARGET (exactly one required)
    --kubernetes      Deploy to Kubernetes cluster
    --lambda          Deploy as AWS Lambda function
    --vm              Deploy to virtual machine via SSH

KUBERNETES OPTIONS (only with --kubernetes)
    --namespace NS    Kubernetes namespace. Default: default.
    --replicas N      Number of pod replicas. Range: 1-100. Default: 1.
    --context CTX     Kubectl context to use. Default: current context.

LAMBDA OPTIONS (only with --lambda)
    --function-name NAME
                      Lambda function name. Required.
    --memory MB       Memory allocation. Range: 128-10240. Default: 512.
    --timeout SECONDS Execution timeout. Range: 1-900. Default: 30.

VM OPTIONS (only with --vm)
    --host HOST       Target hostname or IP. Required.
    --user USER       SSH username. Default: deploy.
    --key PATH        Path to SSH private key. Default: ~/.ssh/id_rsa.

COMMON OPTIONS
    -h, --help        Show this help message
    -v, --version     Show version information
    --dry-run         Show what would be deployed without executing.
    --rollback-on-fail
                      Automatically rollback if health check fails. Default: true.
    --no-rollback-on-fail
                      Disable automatic rollback.

EXAMPLES
    deploy --kubernetes ./myapp
        Deploy to default namespace in current Kubernetes context.

    deploy --kubernetes --namespace prod --replicas 3 ./myapp
        Deploy 3 replicas to production namespace.

    deploy --lambda --function-name my-api --memory 1024 ./dist
        Deploy as Lambda function with 1GB memory.

    deploy --vm --host 10.0.1.50 --user admin ./release.tar.gz
        Deploy archive to VM via SSH.

    deploy --kubernetes --dry-run ./myapp
        Preview Kubernetes deployment without applying.

ENVIRONMENT
    DEPLOY_TARGET     Default target type (kubernetes, lambda, vm)
    KUBECONFIG        Path to Kubernetes config (for --kubernetes)
    AWS_PROFILE       AWS profile for Lambda deployment (for --lambda)

EXIT CODES
    0                 Deployment successful
    1                 Deployment failed (rolled back if enabled)
    2                 Invalid arguments or configuration
    3                 Target unreachable

SEE ALSO
    deploy status --help     Check deployment status
    deploy rollback --help   Manually rollback deployment
    deploy logs --help       View deployment logs
```
