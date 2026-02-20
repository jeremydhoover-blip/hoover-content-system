# Examples

## Example 1: Deployment workflow documentation

Input:
- Workflow: Deploy containerized application to Kubernetes
- Tools: Docker, kubectl, Helm
- Environment: Production cluster

Output:
```md
# Deploy to Production Kubernetes

## Overview
Deploy a containerized application to the production Kubernetes cluster using Helm. Use this workflow for scheduled releases and hotfixes.

## Prerequisites

### Required tools
| Tool | Minimum version | Verify command |
|------|-----------------|----------------|
| Docker | 24.0.0 | `docker --version` |
| kubectl | 1.28.0 | `kubectl version --client` |
| Helm | 3.12.0 | `helm version` |

### Required access
- [ ] Docker registry push access (verify: `docker login registry.example.com`)
- [ ] Kubernetes cluster credentials (verify: `kubectl get nodes`)
- [ ] Helm repository access (verify: `helm repo list`)

### Input artifacts
- Application source code: checked out at `./app`
- Helm chart: located at `./deploy/charts/myapp`

---

## Workflow diagram

```
[Build Image] → [Push to Registry] → [Update Chart Values] → [Deploy] → [Verify] → [Done]
                                                                ↓
                                                          [Rollback if failed]
```

---

## Step-by-step instructions

### Step 1: Build the container image

**Command:**
```bash
docker build -t registry.example.com/myapp:v1.2.3 ./app
```

**Expected output:**
```
Successfully built a1b2c3d4e5f6
Successfully tagged registry.example.com/myapp:v1.2.3
```

**Troubleshooting:**
- If `COPY failed: file not found`: Verify you're in the repository root directory
- If build hangs at apt-get: Check network connectivity to package mirrors

---

### Step 2: Push image to registry

**Command:**
```bash
docker push registry.example.com/myapp:v1.2.3
```

**Expected output:**
```
v1.2.3: digest: sha256:abc123... size: 1234
```

**Troubleshooting:**
- If `denied: access forbidden`: Run `docker login registry.example.com`
- If `connection refused`: Check VPN connection

---

### Step 3: Deploy with Helm

**Command:**
```bash
helm upgrade --install myapp ./deploy/charts/myapp \
  --namespace production \
  --set image.tag=v1.2.3 \
  --wait \
  --timeout 5m
```

**Expected output:**
```
Release "myapp" has been upgraded. Happy Helming!
```

**Troubleshooting:**
- If `timed out waiting for condition`: Check pod status with `kubectl get pods -n production`
- If `UPGRADE FAILED`: Check `helm history myapp -n production` for previous state

---

### Step 4: Verify deployment

**Command:**
```bash
kubectl rollout status deployment/myapp -n production
```

**Expected output:**
```
deployment "myapp" successfully rolled out
```

---

## Output artifacts
- Container image: `registry.example.com/myapp:v1.2.3`
- Helm release: `myapp` in namespace `production`

## Verification
```bash
curl -s https://myapp.example.com/health | jq .status
```
Expected result: `"healthy"`

---

## Rollback procedure
If deployment fails or causes issues:
```bash
helm rollback myapp -n production
```
This restores the previous release.

---

## Common issues

| Symptom | Cause | Resolution |
|---------|-------|------------|
| Pods stuck in ImagePullBackOff | Registry auth expired | Re-run `docker login` and update pull secret |
| Deployment timeout | Resource limits too low | Increase memory/CPU in values.yaml |
| Health check failing | Config not updated | Verify ConfigMap mounted correctly |
```

---

## Example 2: CI/CD pipeline documentation

Input:
- Workflow: GitHub Actions CI pipeline
- Steps: test, build, deploy to staging
- Triggers: push to main, pull request

Output:
```md
# CI/CD Pipeline

## Pipeline overview
- **Trigger**: Push to `main` branch or pull request
- **Duration**: ~8 minutes (test: 3min, build: 2min, deploy: 3min)
- **Artifacts produced**: Docker image, test coverage report

## Pipeline stages

### Stage 1: Test
- **Purpose**: Run unit and integration tests
- **Runs on**: `ubuntu-latest`
- **Dependencies**: None

#### Jobs
1. **unit-tests**: Run pytest with coverage
   - Inputs: Source code
   - Outputs: Coverage report (uploaded to Codecov)
   - Timeout: 5 minutes

2. **lint**: Run code quality checks
   - Inputs: Source code
   - Outputs: None (fail/pass only)
   - Timeout: 2 minutes

---

### Stage 2: Build
- **Purpose**: Build and push Docker image
- **Runs on**: `ubuntu-latest`
- **Dependencies**: Test stage must pass

#### Jobs
1. **build-image**: Build multi-platform image
   - Inputs: Dockerfile, source code
   - Outputs: Image pushed to registry with SHA tag
   - Timeout: 10 minutes

---

### Stage 3: Deploy (main branch only)
- **Purpose**: Deploy to staging environment
- **Runs on**: `ubuntu-latest`
- **Dependencies**: Build stage must pass

---

## Configuration

### Pipeline file
```yaml
# .github/workflows/ci.yml
name: CI
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run tests
        run: pytest --cov

  build:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Build image
        run: docker build -t myapp:${{ github.sha }} .
```

### Required secrets
| Secret | Purpose | Where to set |
|--------|---------|--------------|
| `DOCKER_USERNAME` | Registry authentication | Repository settings → Secrets |
| `DOCKER_PASSWORD` | Registry authentication | Repository settings → Secrets |
| `STAGING_KUBECONFIG` | Kubernetes access | Repository settings → Secrets |

---

## Monitoring

### Success indicators
- Green checkmark on commit in GitHub
- Slack notification to #deployments channel
- New image tag visible in registry

### Failure alerts
- Email to commit author
- Slack notification with failure details
- PR blocked from merging

---

## Manual intervention points
- **Flaky test failure**: Re-run workflow from GitHub Actions UI
- **Registry rate limit**: Wait 1 hour or use authenticated pulls
- **Staging deploy stuck**: Check cluster status, may need manual rollback
```

---

## Example 3: Edge case — Workflow with complex decision points

Input:
- Workflow: Database migration with conditional rollback
- Complexity: Different paths based on migration size and risk

Output:
```md
# Database Migration Workflow

## Overview
Safely apply database migrations with size-appropriate procedures. Small migrations run directly; large migrations require maintenance windows.

## Prerequisites

### Required tools
| Tool | Minimum version | Verify command |
|------|-----------------|----------------|
| migrate | 4.15.0 | `migrate -version` |
| psql | 14.0 | `psql --version` |

### Required access
- [ ] Database admin credentials
- [ ] Maintenance window approval (for large migrations)

---

## Workflow diagram

```
[Start] → [Analyze Migration]
              ↓
         [Size Check]
        /           \
   [Small]        [Large]
      ↓              ↓
   [Apply]    [Schedule Window]
      ↓              ↓
   [Verify]   [Notify Users]
      ↓              ↓
   [Done]     [Apply with Lock]
                     ↓
               [Verify]
                     ↓
               [Done]
```

---

## Step 1: Analyze migration

**Command:**
```bash
migrate -path ./migrations -database "$DATABASE_URL" status
```

**Expected output:**
```
Pending migrations: 3
Estimated rows affected: 1,234,567
```

---

## Step 2: Determine migration path

### Decision criteria

| Rows affected | Table lock required | Path |
|---------------|--------------------|----|
| < 10,000 | No | Small migration |
| < 10,000 | Yes | Large migration |
| >= 10,000 | Any | Large migration |

---

## Path A: Small migration

### Apply migration
```bash
migrate -path ./migrations -database "$DATABASE_URL" up
```

**Expected output:**
```
3 migrations applied successfully
```

**Troubleshooting:**
- If `pq: deadlock detected`: Retry after 30 seconds
- If migration fails mid-way: Proceed to rollback

### Rollback (if needed)
```bash
migrate -path ./migrations -database "$DATABASE_URL" down 1
```

---

## Path B: Large migration

### 1. Schedule maintenance window
- Minimum notice: 24 hours
- Post to status page
- Send user notification email

### 2. Enable maintenance mode
```bash
./scripts/maintenance-mode.sh enable
```

### 3. Create backup
```bash
pg_dump -Fc "$DATABASE_URL" > backup_$(date +%Y%m%d_%H%M%S).dump
```
**This step is non-negotiable for large migrations.**

### 4. Apply migration
```bash
migrate -path ./migrations -database "$DATABASE_URL" up
```

### 5. Verify and disable maintenance mode
```bash
./scripts/run-smoke-tests.sh && ./scripts/maintenance-mode.sh disable
```

### Rollback (if verification fails)
```bash
pg_restore -d "$DATABASE_URL" backup_*.dump
./scripts/maintenance-mode.sh disable
```

---

## Common issues

| Symptom | Cause | Resolution |
|---------|-------|------------|
| Migration hangs | Lock contention | Kill blocking queries, retry |
| Partial migration | Connection dropped | Check migration state, apply remaining |
| Performance degradation | Missing index rebuild | Run `ANALYZE` on affected tables |
```
