# Examples

## Example 1: Technical tutorial with verification

**Input:**
- Skill: Setting up a basic CI pipeline with GitHub Actions
- Audience: Developers new to CI/CD
- Prerequisites: GitHub account, existing repository with tests

**Output:**

```md
# How to Set Up Your First GitHub Actions CI Pipeline

This tutorial walks you through creating a CI pipeline that automatically runs your tests on every push. By the end, you'll have a working pipeline that catches bugs before they hit main.

**What you'll learn:**
- Create a GitHub Actions workflow file
- Configure automatic test runs on push and PR
- Read and interpret workflow results

**Prerequisites:**
- A GitHub account
- A repository with at least one test (we'll use a Node.js project; adapt commands for your language)
- Basic familiarity with YAML syntax

**Time required:** 15 minutes

---

## Step 1: Create the workflow directory

GitHub Actions looks for workflow files in a specific location.

In your repository root, create the directory:

```bash
mkdir -p .github/workflows
```

**Verify:** Run `ls -la .github/workflows`. The directory should exist (it will be empty).

---

## Step 2: Create the workflow file

Create a new file called `ci.yml`:

```bash
touch .github/workflows/ci.yml
```

Open `ci.yml` and add this content:

```yaml
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
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
      - run: npm ci
      - run: npm test
```

**Verify:** Your file should be exactly 17 lines. Double-check the indentation — YAML is sensitive to spaces.

---

## Step 3: Commit and push the workflow

```bash
git add .github/workflows/ci.yml
git commit -m "Add CI workflow"
git push origin main
```

**Verify:** Go to your repository on GitHub. Click the "Actions" tab. You should see a workflow run in progress or completed.

---

## Step 4: Interpret the results

Click on the workflow run to see details.

- **Green checkmark:** All steps passed
- **Red X:** A step failed — click to see logs
- **Yellow dot:** Currently running

**Verify:** If your tests pass locally, the workflow should show a green checkmark within 2-3 minutes.

---

## Troubleshooting

### Workflow doesn't appear in Actions tab
**Cause:** The file isn't in the correct location or has a YAML syntax error.
**Fix:** Confirm the file is at `.github/workflows/ci.yml` (not `.github/workflow/` — note the 's'). Validate YAML syntax at yamllint.com.

### Tests pass locally but fail in CI
**Cause:** Environment differences (Node version, missing dependencies, OS-specific behavior).
**Fix:** Check the Node version in the workflow matches your local version. Look at the error logs for specific failures.

### "npm ci" fails
**Cause:** Missing or outdated `package-lock.json`.
**Fix:** Run `npm install` locally, commit the updated `package-lock.json`, and push.

---

## Next steps

- Add a badge to your README showing build status
- Configure the workflow to run on multiple Node versions
- Add deployment steps for successful builds
```

---

## Example 2: Non-technical tutorial

**Input:**
- Skill: Conducting a content audit
- Audience: Content strategists new to audits
- Prerequisites: Access to website analytics, spreadsheet software

**Output:**

```md
# How to Conduct Your First Content Audit

A content audit gives you a complete picture of what content you have, how it's performing, and what to do about it. By the end of this tutorial, you'll have a prioritized spreadsheet of content actions.

**What you'll learn:**
- Create a content inventory
- Add performance data
- Score and prioritize content for action

**Prerequisites:**
- Access to your website's analytics (Google Analytics, Plausible, etc.)
- Spreadsheet software (Excel, Google Sheets)
- A website with at least 20 pages of content

**Time required:** 2-4 hours (depending on site size)

---

## Step 1: Export your page list

You need a complete list of URLs to audit.

**Option A — From sitemap:**
Open `yoursite.com/sitemap.xml` in a browser. Copy URLs to your spreadsheet.

**Option B — From analytics:**
In Google Analytics: Reports → Pages and screens → Export to CSV.

**Verify:** Your spreadsheet column A should contain full URLs for every page you want to audit. You should have at least 20 rows.

---

## Step 2: Add metadata columns

Add these columns to your spreadsheet:

| Column | What to enter |
|--------|---------------|
| B: Title | Page title (from browser tab) |
| C: Content type | Blog post, product page, help doc, etc. |
| D: Last updated | Date of last significant edit |
| E: Word count | Approximate length |
| F: Owner | Person responsible for this content |

**Verify:** Fill in 5 rows completely before proceeding. This confirms your process works before doing all pages.

---

## Step 3: Add performance data

For each URL, add these metrics from your analytics:

| Column | Metric | Where to find |
|--------|--------|---------------|
| G: Pageviews (90 days) | Total visits | GA: Pages report |
| H: Avg. time on page | Engagement | GA: Pages report |
| I: Bounce rate | Single-page sessions | GA: Pages report |

**Verify:** Spot-check 3 URLs. Do the numbers in your spreadsheet match what you see in analytics?

---

## Step 4: Score each page

Add a column J: "Action" and score each page:

| Score | Criteria | Action |
|-------|----------|--------|
| Keep | High traffic, accurate, on-brand | No changes needed |
| Update | Good topic, outdated info | Revise and republish |
| Merge | Overlaps with another page | Combine with related content |
| Remove | Low traffic, no longer relevant | Delete or redirect |

**Verify:** Every row should have an action assigned. If you're unsure, mark as "Review" and decide later.

---

## Troubleshooting

### Analytics shows more pages than you expected
**Cause:** URL parameters creating duplicate entries (e.g., `?utm_source=...`).
**Fix:** In analytics, filter to exclude query parameters, or deduplicate in your spreadsheet.

### You don't know who owns a page
**Cause:** Content ownership was never assigned.
**Fix:** Mark as "Unowned" and flag for your manager. This is a finding, not a blocker.

---

## Next steps

- Prioritize your "Update" list by traffic (fix high-traffic pages first)
- Set up a recurring quarterly audit
- Create a content calendar for updates
```

---

## Example 3: Edge case — tutorial with multiple valid paths

**Input:**
- Skill: Deploying a static site
- Challenge: Multiple valid hosting options, reader must choose

**Output:**

```md
# How to Deploy a Static Site (3 Options Compared)

This tutorial covers three popular ways to deploy a static site. Each takes under 15 minutes. Choose based on your needs.

**What you'll accomplish:**
- A live, publicly accessible website
- Automatic deploys when you push to GitHub

**Prerequisites:**
- A static site (HTML/CSS/JS files or a built site from a generator)
- A GitHub repository with your site files
- Free accounts on your chosen platform (instructions included)

## Overview

| Platform | Best for | Custom domain | Free tier |
|----------|----------|---------------|-----------|
| GitHub Pages | Simple sites | Yes (manual DNS) | Yes |
| Netlify | Sites needing forms, redirects | Yes (automatic SSL) | Yes |
| Vercel | Next.js or frequent deploys | Yes (automatic SSL) | Yes |

---

## Option 1: GitHub Pages

**Best for:** Documentation, portfolios, simple sites

### Step 1: Enable GitHub Pages

Go to your repository → Settings → Pages.

Under "Source," select:
- Branch: `main`
- Folder: `/ (root)` or `/docs` if your built files are there

Click Save.

**Verify:** A blue banner appears with your site URL (format: `username.github.io/repo-name`).

### Step 2: Wait for deployment

GitHub takes 1-3 minutes to build.

**Verify:** Visit the URL. You should see your site. If you see a 404, wait 2 more minutes and refresh.

[Continue with troubleshooting specific to GitHub Pages...]

---

## Option 2: Netlify

**Best for:** Sites needing forms, redirects, or preview deploys

[Continue with Netlify-specific steps...]

---

## Option 3: Vercel

**Best for:** Next.js sites, fastest build times

[Continue with Vercel-specific steps...]

---

## Which should you choose?

- **Just need it live?** → GitHub Pages (simplest)
- **Need forms or redirects?** → Netlify
- **Using Next.js?** → Vercel
- **Unsure?** → Start with Netlify; it handles the most use cases
```
