# Examples

## Example 1: Basic CLI workflow tutorial

**Input:**
- Tool: Docker
- Goal: Build and run first container
- Audience: Developers new to containers
- Duration: ~10 minutes

**Output:**

```md
# Build and Run Your First Docker Container

Learn the core Docker workflow by building a simple web server container from scratch.

**Time to complete:** 10 minutes
**Difficulty:** Beginner

## Prerequisites

Before you begin, make sure you have:
- [ ] Docker Desktop installed ([installation guide](https://docs.docker.com/get-docker/))
- [ ] Terminal or command prompt open
- [ ] A text editor

Verify Docker is running:
```bash
docker --version
```

You should see output like `Docker version 24.0.0, build abc123`.

## What you'll build

A containerized web server that responds with "Hello, Docker!" when accessed at http://localhost:8080.

---

## Step 1: Create the application file

Create a simple web server that Docker will run.

```bash
mkdir my-first-container && cd my-first-container
```

Create a file named `server.py` with this content:

```python
from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Hello, Docker!')

HTTPServer(('0.0.0.0', 8080), Handler).serve_forever()
```

---

## Step 2: Create the Dockerfile

The Dockerfile tells Docker how to build your container image.

Create a file named `Dockerfile` (no extension) with this content:

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY server.py .
EXPOSE 8080
CMD ["python", "server.py"]
```

This Dockerfile:
- Starts from a lightweight Python image
- Sets up a working directory
- Copies your server code
- Exposes port 8080
- Runs the server when container starts

### Checkpoint

Your directory should now contain two files:
```bash
ls
```

**Expected output:**
```
Dockerfile  server.py
```

---

## Step 3: Build the container image

Convert your Dockerfile into a runnable image.

```bash
docker build -t my-first-app .
```

**Expected output:**
```
[+] Building 15.2s (8/8) FINISHED
 => [internal] load build definition from Dockerfile
 => [internal] load .dockerignore
 => [internal] load metadata for docker.io/library/python:3.11-slim
 => [1/3] FROM docker.io/library/python:3.11-slim
 => [2/3] WORKDIR /app
 => [3/3] COPY server.py .
 => exporting to image
 => => naming to docker.io/library/my-first-app
```

Verify the image exists:
```bash
docker images my-first-app
```

**Expected output:**
```
REPOSITORY      TAG       IMAGE ID       CREATED          SIZE
my-first-app    latest    a1b2c3d4e5f6   10 seconds ago   125MB
```

---

## Step 4: Run the container

Start a container from your image.

```bash
docker run -d -p 8080:8080 --name my-server my-first-app
```

The flags mean:
- `-d`: Run in background (detached)
- `-p 8080:8080`: Map port 8080 on your machine to port 8080 in container
- `--name my-server`: Give the container a friendly name

**Expected output:**
```
a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0u1v2w3x4y5z
```

(This is the container ID—yours will differ.)

---

## Step 5: Test your container

Verify the web server is responding.

```bash
curl http://localhost:8080
```

**Expected output:**
```
Hello, Docker!
```

On Windows without curl, open http://localhost:8080 in your browser.

---

## Verify your work

Check that everything is running correctly:

```bash
docker ps
```

You should see:
```
CONTAINER ID   IMAGE          COMMAND               STATUS          PORTS                    NAMES
a1b2c3d4e5f6   my-first-app   "python server.py"   Up 2 minutes    0.0.0.0:8080->8080/tcp   my-server
```

## Troubleshooting

### "port is already allocated"
**Symptom:** Error when running `docker run`
**Cause:** Port 8080 is already in use
**Fix:** Use a different port:
```bash
docker run -d -p 9090:8080 --name my-server my-first-app
```
Then access at http://localhost:9090

### "Cannot connect to the Docker daemon"
**Symptom:** Error on any docker command
**Cause:** Docker Desktop isn't running
**Fix:** Start Docker Desktop and wait for it to initialize

### Container exits immediately
**Symptom:** `docker ps` shows no running containers
**Cause:** Error in server.py or Dockerfile
**Fix:** Check logs:
```bash
docker logs my-server
```

## Cleanup

Remove the resources created in this tutorial:

```bash
docker stop my-server
docker rm my-server
docker rmi my-first-app
```

Remove the project directory:
```bash
cd ..
rm -rf my-first-container
```

## Next steps

- [Push your image to Docker Hub](https://docs.docker.com/get-started/04_sharing_app/)
- [Use Docker Compose for multi-container apps](https://docs.docker.com/compose/gettingstarted/)
- [Dockerfile best practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
```

---

## Example 2: Multi-step workflow with branching

**Input:**
- Tool: Cloud CLI (generic)
- Goal: Deploy application to staging or production
- Audience: Developers with CLI experience
- Branches: Different commands for staging vs. production

**Output:**

```md
# Deploy Your Application to the Cloud

Deploy a containerized application to your cloud environment with proper configuration.

**Time to complete:** 15-20 minutes
**Difficulty:** Intermediate

## Prerequisites

Before you begin, make sure you have:
- [ ] Cloud CLI installed and authenticated (`cloud auth status` shows logged in)
- [ ] Docker image pushed to registry (from previous tutorial)
- [ ] Environment variables configured for target environment

Verify your authentication:
```bash
cloud auth status
```

You should see your email and active project.

## What you'll build

A deployed application accessible at `https://{app-name}.{region}.cloud.example.com`.

---

## Step 1: Select your target environment

Choose whether to deploy to staging or production.

```bash
cloud config get-value project
```

**Expected output shows your project ID.**

Set the target environment:

### Option A: Staging deployment
Use this for testing and validation.

```bash
export DEPLOY_ENV=staging
export REPLICAS=1
export DOMAIN=staging.cloud.example.com
```

### Option B: Production deployment
Use this for live traffic. Requires additional approvals.

```bash
export DEPLOY_ENV=production
export REPLICAS=3
export DOMAIN=cloud.example.com
```

---

## Step 2: Validate your container image

Ensure the image you're deploying exists and is accessible.

```bash
cloud artifacts docker images list \
  --repository=my-apps \
  --filter="package=my-app"
```

**Expected output:**
```
IMAGE                           DIGEST         CREATE_TIME          UPDATE_TIME
my-app                         sha256:abc123   2024-01-15T10:30:00  2024-01-15T10:30:00
```

### Checkpoint

If no images appear, you need to build and push first:
```bash
docker build -t my-app .
docker push registry.cloud.example.com/my-apps/my-app
```

---

## Step 3: Create the deployment configuration

Generate the deployment manifest for your environment.

```bash
cloud deploy config generate \
  --image=registry.cloud.example.com/my-apps/my-app:latest \
  --environment=$DEPLOY_ENV \
  --replicas=$REPLICAS \
  --output=deploy.yaml
```

**Expected output:**
```
Generated deployment configuration: deploy.yaml
Environment: staging
Replicas: 1
```

Review the generated configuration:
```bash
cat deploy.yaml
```

---

## Step 4: Deploy to target environment

Apply the deployment configuration.

```bash
cloud deploy apply deploy.yaml --wait
```

**Expected output (staging):**
```
Deploying my-app to staging...
  Creating deployment... done
  Waiting for rollout... done
  
Deployment successful!
URL: https://my-app.staging.cloud.example.com
```

**Expected output (production):**
```
Deploying my-app to production...
  
⚠️  Production deployment requires approval.
  Approval request sent to: admin@example.com
  
Waiting for approval...
```

### Checkpoint

Verify deployment status:
```bash
cloud deploy status my-app --environment=$DEPLOY_ENV
```

You should see `Status: Running` with healthy replicas.

---

## Verify your work

Test the deployed application:

```bash
curl https://my-app.$DOMAIN/health
```

**Expected output:**
```json
{"status": "healthy", "version": "1.0.0"}
```

## Troubleshooting

### Deployment stuck in "Pending"
**Symptom:** Status shows Pending for more than 5 minutes
**Cause:** Insufficient resources or image pull failure
**Fix:** 
```bash
cloud deploy logs my-app --environment=$DEPLOY_ENV
```
Look for error messages about resource limits or image access.

### "Image not found" error
**Symptom:** Deployment fails immediately with image error
**Cause:** Image doesn't exist or wrong registry path
**Fix:** Verify image exists:
```bash
cloud artifacts docker images describe \
  registry.cloud.example.com/my-apps/my-app:latest
```

### Health check failures
**Symptom:** Deployment succeeds but pods restart
**Cause:** Application not responding on health endpoint
**Fix:** Check application logs:
```bash
cloud deploy logs my-app --environment=$DEPLOY_ENV --tail=50
```

## Cleanup

To remove the deployment (staging only—production requires approval):

```bash
cloud deploy delete my-app --environment=staging --force
```

Remove local configuration:
```bash
rm deploy.yaml
unset DEPLOY_ENV REPLICAS DOMAIN
```

## Next steps

- [Configure custom domains](docs/custom-domains)
- [Set up continuous deployment](docs/ci-cd)
- [Monitor application performance](docs/monitoring)
```

---

## Example 3: Edge case—tutorial with recovery from wrong state

**Input:**
- Tool: Git
- Goal: Clean up after accidental commit to wrong branch
- Audience: Developers who made a mistake
- Challenge: User starting state is unknown/wrong

**Output:**

```md
# Recover from Committing to the Wrong Branch

Fix the common mistake of committing changes to main instead of a feature branch.

**Time to complete:** 5 minutes
**Difficulty:** Intermediate

## Prerequisites

- [ ] Git installed
- [ ] You've committed to the wrong branch and haven't pushed yet
- [ ] You know which branch should have the commits

## Step 1: Verify your current state

First, understand what happened.

```bash
git log --oneline -5
```

**Expected output:**
```
a1b2c3d (HEAD -> main) Your accidental commit message
e4f5g6h Previous commit on main
...
```

Identify how many commits need to move. In this example, we'll move the last 1 commit.

### Checkpoint

Confirm you're on the wrong branch:
```bash
git branch
```

You should see `* main` (or whichever branch you accidentally committed to).

---

## Step 2: Create the correct branch (if it doesn't exist)

If your target feature branch doesn't exist, create it now.

### Option A: Branch doesn't exist
```bash
git branch feature/my-work
```

### Option B: Branch exists
Skip this step and proceed to Step 3.

---

## Step 3: Move commits to the correct branch

Cherry-pick your commits to the correct branch.

```bash
git checkout feature/my-work
git cherry-pick a1b2c3d
```

Replace `a1b2c3d` with your commit hash from Step 1.

**Expected output:**
```
[feature/my-work 7h8i9j0] Your accidental commit message
 Date: Mon Jan 15 10:30:00 2024 -0800
 1 file changed, 10 insertions(+)
```

For multiple commits, cherry-pick each one in order (oldest first).

---

## Step 4: Remove commits from the wrong branch

Go back to the original branch and reset.

```bash
git checkout main
git reset --hard HEAD~1
```

Replace `1` with the number of commits you moved.

⚠️ **Warning:** `git reset --hard` is destructive. Ensure your commits are safely on the feature branch before running this.

### Checkpoint

Verify main no longer has your commits:
```bash
git log --oneline -3
```

Your accidental commit should not appear.

---

## Verify your work

Confirm commits are on the correct branch:

```bash
git log --oneline feature/my-work -3
```

Your commits should appear here.

```bash
git log --oneline main -3
```

Your commits should NOT appear here.

## Troubleshooting

### Already pushed to remote
**Symptom:** You pushed before realizing the mistake
**Cause:** Commits are now on remote main
**Fix:** This requires force-push (coordinate with your team):
```bash
git push origin main --force-with-lease
```
⚠️ This rewrites history. Never do this on shared branches without team coordination.

### Cherry-pick has conflicts
**Symptom:** Error message about merge conflicts
**Cause:** Feature branch has changes that conflict
**Fix:** Resolve conflicts, then:
```bash
git add .
git cherry-pick --continue
```

### Reset removed too many commits
**Symptom:** Lost commits you wanted to keep
**Fix:** Use reflog to recover:
```bash
git reflog
git reset --hard HEAD@{N}
```
Replace `N` with the entry number showing your desired state.

## Next steps

- [Understanding git reset](docs/git-reset)
- [Preventing accidental commits](docs/branch-protection)
```
