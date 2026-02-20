# Examples

## Example 1: Feature launch

**Input:**
- Feature: Real-time collaboration in editor
- Audience: All users
- Channel: Email + blog
- Availability: Now, all plans

**Output:**
```md
## Work together in real time

Real-time collaboration is now available to all users. See your team's edits as they happen—no more version conflicts or waiting for saves.

### What you can do
- See cursors and selections from teammates instantly
- Co-edit any document with up to 10 collaborators
- Leave inline comments without switching tools

### Get started
Open any document and click Share to invite collaborators.

[Start collaborating →]
```

---

## Example 2: Deprecation notice

**Input:**
- Feature: Legacy API v1
- Sunset date: March 15, 2026
- Replacement: API v2
- Audience: Developers using v1

**Output:**
```md
## API v1 is being retired on March 15, 2026

Starting March 15, 2026, API v1 endpoints will no longer be available.

### Why we're making this change
API v2 offers improved performance, better error handling, and expanded functionality. Consolidating to a single API version lets us deliver updates faster.

### What you need to do
1. Review your integrations for v1 endpoint usage
2. Migrate to API v2 endpoints by March 1, 2026
3. Test in staging before the cutoff date

### Recommended alternative
API v2 is available now with full documentation at docs.example.com/api/v2.

Questions? Contact developer support or see our migration FAQ.
```

---

## Example 3: Breaking change

**Input:**
- Change: Authentication tokens now expire after 24 hours (previously no expiration)
- Effective: February 1, 2026
- Affected: Users with long-lived tokens in scripts or integrations

**Output:**
```md
## Action required: Token expiration changes on February 1

On February 1, 2026, authentication tokens will expire after 24 hours. Previously, tokens did not expire.

### What's changing
- **Before**: Tokens remained valid indefinitely
- **After**: Tokens expire 24 hours after creation

### Who's affected
Users with tokens created before February 1 that are used in automated scripts, CI/CD pipelines, or long-running integrations.

### Required action by January 31
1. Update scripts to handle token refresh
2. Implement the refresh token flow (see docs)
3. Regenerate tokens after February 1 for new expiration behavior

### Need help?
See our token migration guide or contact support.
```

---

## Example 4: Minor update (changelog style)

**Input:**
- Change: Improved search performance by 40%
- Channel: Changelog
- No action required

**Output:**
```md
### February 10, 2026 — Performance

**Faster search**: Search results now load up to 40% faster across all workspaces. No action required.
```

---

## Example 5: Edge case — Partial rollout

**Input:**
- Feature: AI-assisted writing suggestions
- Availability: Rolling out to 20% of users this week, all users by March 1
- Audience: All users (some won't have it yet)

**Output:**
```md
## AI writing suggestions are rolling out

We're introducing AI-assisted writing suggestions to help you draft faster. This feature is rolling out gradually and will be available to all users by March 1, 2026.

### What it does
- Suggests completions as you type
- Offers rephrasing options on highlight
- Works in all text fields

### When you'll get it
We're rolling this out in phases:
- This week: 20% of users
- By March 1: All users

You'll see a ✨ icon in the editor when it's enabled for your account.

### Not seeing it yet?
Hang tight—you'll have access by March 1. No action needed.
```
