# Examples

## Example 1: Basic how-to guide

**Input:**
- Task: Configure environment variables for a Node.js application
- Audience: Developers new to Node.js
- Platform: macOS/Linux

**Output:**

```md
# How to configure environment variables for Node.js

This guide shows you how to set up environment variables for your Node.js application using a `.env` file.

## Prerequisites

Before you begin, ensure you have:

- [ ] Node.js 18+ installed
- [ ] npm or yarn package manager
- [ ] A Node.js project with `package.json`

## Steps

### Step 1: Install the dotenv package

Add the dotenv package to your project dependencies.

```bash
npm install dotenv
```

**Expected outcome:** Package appears in `package.json` dependencies.

### Step 2: Create the environment file

Create a `.env` file in your project root directory.

```bash
touch .env
```

**Expected outcome:** Empty `.env` file exists in project root.

### Step 3: Add your environment variables

Open `.env` and add your variables in `KEY=value` format.

```env
DATABASE_URL=postgresql://localhost:5432/myapp
API_KEY=your-api-key-here
NODE_ENV=development
```

**Expected outcome:** File contains your configuration values.

### Step 4: Load variables in your application

Add dotenv configuration at the top of your entry file.

```javascript
require('dotenv').config();
```

**Expected outcome:** Variables available via `process.env.VARIABLE_NAME`.

## Verify your setup

Test that variables load correctly:

```javascript
console.log(process.env.NODE_ENV);
```

You should see: `development`

## Next steps

- [How to manage different environments](/guides/managing-environments)
- [How to secure sensitive variables](/guides/secrets-management)

## Troubleshooting

### Variables return undefined

**Symptom:** `process.env.VARIABLE_NAME` returns `undefined`.

**Solution:** Ensure `require('dotenv').config()` runs before accessing variables. Check that `.env` file is in the directory where Node runs.

### Changes not reflected

**Symptom:** Updated `.env` values don't appear in application.

**Solution:** Restart your Node.js process. Environment variables load once at startup.
```

---

## Example 2: Short-form guide

**Input:**
- Task: Clear npm cache
- Audience: Any developer
- Complexity: Simple, one-shot task

**Output:**

```md
# How to clear the npm cache

Clear corrupted or outdated cached packages when experiencing installation issues.

**Prerequisites:** npm installed.

1. Run `npm cache clean --force` to delete all cached data.
2. Verify with `npm cache verify` — you should see "Cache verified and compressed."
3. Retry your failed npm operation.

**Verify:** Run `npm cache ls` — output should be empty or show only recent entries.
```

---

## Example 3: Edge case — multi-system task

**Input:**
- Task: Set up CI/CD pipeline for a monorepo
- Audience: DevOps engineers
- Complexity: Spans multiple tools and configurations

**Output:**

```md
# How to set up CI/CD for a monorepo

This guide covers configuring continuous integration for a monorepo with selective builds. Due to the scope, this is split into linked sub-guides.

## Prerequisites

Before you begin, ensure you have:

- [ ] Monorepo with workspace configuration (npm workspaces, yarn workspaces, or pnpm)
- [ ] Admin access to your CI/CD platform
- [ ] Repository write permissions

## Overview

Setting up monorepo CI/CD involves three phases:

1. **Configure workspace detection** — [How to configure workspace detection](/guides/monorepo-workspace-detection)
2. **Set up selective builds** — [How to implement selective builds](/guides/monorepo-selective-builds)
3. **Configure deployment stages** — [How to configure staged deployments](/guides/monorepo-deployments)

## Steps

### Step 1: Verify workspace structure

Confirm your monorepo has a valid workspace configuration.

```bash
npm ls --workspaces
```

**Expected outcome:** List of all workspace packages with their locations.

### Step 2: Choose your CI platform

Select your CI/CD platform and proceed to the relevant sub-guide:

| Platform | Sub-guide |
|----------|-----------|
| GitHub Actions | [Monorepo CI with GitHub Actions](/guides/monorepo-github-actions) |
| GitLab CI | [Monorepo CI with GitLab](/guides/monorepo-gitlab-ci) |
| Azure Pipelines | [Monorepo CI with Azure](/guides/monorepo-azure-pipelines) |

### Step 3: Implement change detection

Follow the change detection sub-guide for your platform to avoid building unchanged packages.

**Expected outcome:** CI only runs jobs for packages with changes.

## Verify your setup

Push a change to a single package and confirm:
- Only that package's tests run
- Other packages are skipped
- Build time reduced compared to full builds

## Next steps

- [How to optimize monorepo build caching](/guides/monorepo-caching)
- [How to handle cross-package dependencies](/guides/monorepo-dependencies)
```

---

## Anti-pattern example

**Input:** Same as Example 1

**Bad output (do not produce):**

```md
# Environment Variables in Node.js

Environment variables are a great way to configure your application. They help you keep secrets out of your code and make your app more portable.

## What are environment variables?

Environment variables are key-value pairs that exist outside your application...

[Multiple paragraphs of conceptual explanation]

## Setting them up

You can use the dotenv package. It's really popular and easy to use.

First install it, then create a file, then add your variables...
```

**Why this fails:**
- Title doesn't use "How to" format
- Includes conceptual explanation instead of steps
- Steps not numbered or structured
- No prerequisites section
- No expected outcomes
- Promotional language ("really popular")
