# Examples

## Example 1: Thought leadership post

**Input:**
- Topic: Why sprint planning meetings waste time
- Audience: Engineering managers and agile coaches
- Angle: Contrarian take on a common practice

**Output:**
```md
# Sprint planning is broken. Here's what to do instead.

Two hours every two weeks. That's 52 hours a year your team spends in sprint planning meetings.

I've sat through hundreds of these. And I've noticed something: the best teams spend the least time planning. The struggling teams plan endlessly.

## The ritual we don't question

Most teams follow the same script:
- Review the backlog
- Estimate stories
- Commit to a sprint goal
- Argue about scope

It feels productive. It's collaborative. It's also often theater.

## What's actually happening

Sprint planning assumes that:
1. We can accurately predict two weeks of work
2. Detailed upfront planning reduces surprises
3. Team consensus improves outcomes

The data doesn't support this. Teams that spend more time planning don't ship more. They ship the same—or less—with more frustration.

## A leaner approach

What if you did this instead?

**15-minute sprint start:**
1. State the sprint goal (one sentence)
2. Pull the top items from a pre-groomed backlog
3. Identify blockers and dependencies
4. Go

No estimates. No lengthy discussions. Those happen asynchronously or in refinement.

## Why this works

- Forces backlog hygiene (can't wing it with an unprepared backlog)
- Respects maker time (meetings are expensive)
- Embraces uncertainty (plans change anyway)

## The catch

This only works if your backlog is actually ready. If your sprint planning takes two hours, your backlog refinement is broken.

Fix that first.

---

*Have you tried cutting sprint planning? I'd love to hear what worked—or didn't. [Reply on LinkedIn →]*
```

---

## Example 2: Tutorial post

**Input:**
- Topic: Setting up automated testing in CI/CD
- Audience: Junior developers
- Platform context: GitHub Actions

**Output:**
```md
# How to add automated testing to your GitHub Actions workflow

*10 minutes · Beginner*

Every pull request should run tests automatically. Here's how to set that up in GitHub Actions—no prior CI/CD experience required.

## What you'll accomplish

By the end of this tutorial, your repo will:
- Run tests on every push and pull request
- Show pass/fail status on PRs
- Block merges if tests fail

## Prerequisites
- A GitHub repository with existing tests (we'll use Jest, but the pattern works for any test runner)
- Basic YAML familiarity (helpful but not required)

## Step 1: Create the workflow file

In your repo, create `.github/workflows/test.yml`:

```yaml
name: Run Tests

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

This workflow triggers on pushes and PRs to `main`.

## Step 2: Commit and push

```bash
git add .github/workflows/test.yml
git commit -m "Add test workflow"
git push
```

Go to the Actions tab in your repo. You should see the workflow running.

## Step 3: Require tests to pass for merges

1. Go to Settings → Branches
2. Add a branch protection rule for `main`
3. Enable "Require status checks to pass"
4. Select your test job

Now PRs can't merge until tests pass.

## Troubleshooting

**Tests pass locally but fail in CI**
Check for environment differences: Node version, missing environment variables, or relative paths.

**Workflow doesn't trigger**
Confirm the file is in `.github/workflows/` (not `.github/workflow/`). YAML indentation matters.

## Next steps

You now have automated testing on every PR. From here you can:
- [Add code coverage reporting →]
- [Set up deployment on merge →]
- [Add linting to the workflow →]
```

---

## Example 3: Listicle

**Input:**
- Topic: Best practices for API documentation
- Audience: Developer advocates and technical writers
- Format: Actionable list

**Output:**
```md
# 7 API documentation practices that developers actually appreciate

Your API might be great. But if the docs are bad, developers will find an alternative.

Here's what separates documentation that gets used from documentation that gets ignored.

## 1. Put the authentication example first

Developers can't do anything until they're authenticated. Don't bury this in a "Getting Started" guide—make it the first thing they see.

**Good**: Auth code snippet above the fold on the docs homepage
**Bad**: "See Authentication section" link in the sidebar

## 2. Show complete, runnable examples

Snippets that work when copy-pasted. Not pseudo-code. Not "configure as needed."

Every example should include:
- All required imports
- Actual parameter values (not placeholders)
- Expected response

## 3. Include error responses, not just success

Developers spend more time debugging than writing happy-path code. Document what goes wrong.

For every endpoint:
- Common error codes
- What triggers each error
- How to fix it

## 4. Version your docs with your API

If v2 breaks v1, and your docs only show v2, you've broken every existing integration.

Maintain versioned docs. Make the version selector obvious.

## 5. Let developers try it without signing up

Interactive consoles, public sandboxes, or curl commands that work immediately.

Friction before value = abandoned evaluation.

## 6. Write for scanning, not reading

Developers don't read docs linearly. They search, scan, and grab.

- Clear headings
- Consistent structure
- Syntax highlighting
- Tables for parameter lists

## 7. Update the changelog religiously

"What changed" is as important as "how it works." A missing changelog is a trust problem.

---

## Which of these is your biggest gap?

Most teams nail 1-2 of these and neglect the rest. Pick one to fix this quarter.

[See how we document our API →]
```

---

## Example 4: Edge case — Short announcement post

**Input:**
- Topic: Minor feature update
- Goal: Inform without overselling
- Length: Brief

**Output:**
```md
# Keyboard shortcuts are here

You can now navigate [Product] without touching your mouse.

Press `?` anywhere to see the full shortcut list. Highlights:
- `g` + `h` → Go to home
- `c` → Create new
- `/` → Focus search

We'll add more based on your feedback. [Let us know what you'd use →]
```
