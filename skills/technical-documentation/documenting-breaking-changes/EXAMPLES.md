# Examples

## Example 1: API breaking change

**Input:**
- Change: Authentication header format changing
- Affects: All API users
- Timeline: 3-month migration window

**Output:**

```md
# Breaking Change: Authentication Header Format

**Effective date:** March 1, 2024
**Affects:** All API integrations
**Action required by:** March 1, 2024

## Summary

The Authorization header format is changing from direct API key to Bearer token format. This improves compatibility with OAuth standards and third-party tools.

## What changed

### Before

API key passed directly in the Authorization header:

```http
Authorization: sk_live_abc123xyz
```

### After

API key must be prefixed with "Bearer ":

```http
Authorization: Bearer sk_live_abc123xyz
```

## Who is affected

You are affected if:

- [ ] You make API calls using the `Authorization` header
- [ ] You use any of our official SDKs older than v2.0

You are NOT affected if:

- You use SDK version 2.0 or later (updated automatically)
- You only use the web dashboard (no API integration)

### How to check

Review your API integration code for Authorization header usage:

```bash
# Search your codebase
grep -r "Authorization.*sk_live" .
grep -r "Authorization.*sk_test" .
```

Or check your API logs for deprecation warnings (appearing January 1, 2024).

## Migration guide

### Prerequisites

- Access to your API integration code
- Ability to deploy code changes

### Step 1: Update header format

Find all locations where you set the Authorization header and add the "Bearer " prefix:

**Before:**
```javascript
headers: {
  'Authorization': process.env.API_KEY
}
```

**After:**
```javascript
headers: {
  'Authorization': `Bearer ${process.env.API_KEY}`
}
```

### Step 2: Test with test API key

Run your integration tests with a test API key to verify the new format works:

```bash
curl -H "Authorization: Bearer sk_test_abc123" \
  https://api.example.com/v1/users
```

Expected response: 200 OK with user data.

### Step 3: Deploy to production

Deploy your updated code before March 1, 2024.

### Step 4: Verify migration

After deployment, verify your integration works by checking:

1. API calls succeed without deprecation warnings
2. Dashboard shows no authentication errors

## Timeline

| Date | Event |
|------|-------|
| December 1, 2023 | Change announced |
| January 1, 2024 | Deprecation warnings in API responses |
| February 15, 2024 | Email reminder to accounts still using old format |
| March 1, 2024 | Old format rejected with 401 error |

## FAQ

### Why is this changing?

The new format aligns with OAuth 2.0 Bearer token standards, improving compatibility with API gateways, testing tools like Postman, and third-party integrations.

### What happens if I don't migrate?

Starting March 1, 2024, API requests using the old format will receive a `401 Unauthorized` error with message: `Invalid Authorization header format. Use: Bearer <token>`.

### What if I need more time?

Contact support@example.com before February 15, 2024 to discuss your situation. We may grant extensions for complex enterprise integrations.

### Are test keys affected?

Yes, both `sk_live_` and `sk_test_` keys require the new format.

## Support

- Email: support@example.com
- Slack: #api-support channel
- Documentation: [Authentication guide](/docs/authentication)
```

---

## Example 2: Configuration breaking change

**Input:**
- Change: Config file format changing from JSON to YAML
- Affects: Self-hosted deployments
- Provides: Migration tool

**Output:**

```md
# Breaking Change: Configuration File Format

**Effective date:** Version 4.0.0 (April 2024)
**Affects:** Self-hosted deployments
**Action required by:** Before upgrading to v4.0.0

## Summary

Configuration files are changing from JSON (config.json) to YAML (config.yaml). YAML provides better readability, comments support, and multi-line strings.

## What changed

### Before (config.json)

```json
{
  "database": {
    "host": "localhost",
    "port": 5432,
    "ssl": true
  },
  "logging": {
    "level": "info",
    "format": "json"
  }
}
```

### After (config.yaml)

```yaml
# Database configuration
database:
  host: localhost
  port: 5432
  ssl: true

# Logging configuration  
logging:
  level: info
  format: json
```

## Who is affected

You are affected if:

- [ ] You run a self-hosted deployment
- [ ] You have a `config.json` file in your installation

You are NOT affected if:

- You use our hosted cloud service
- You use environment variables exclusively (no config file)

### How to check

```bash
# Check if you have a config file
ls config.json

# If file exists, you need to migrate
```

## Migration guide

### Prerequisites

- Node.js 16+ (for migration tool)
- Write access to configuration directory

### Option A: Automated migration (recommended)

Use our migration tool:

```bash
npx @example/config-migrate ./config.json ./config.yaml
```

The tool will:
1. Read your existing config.json
2. Convert to YAML format
3. Preserve all values
4. Add helpful comments

**Verify:** Check that `config.yaml` contains your settings.

### Option B: Manual migration

1. Create `config.yaml` with same values as `config.json`
2. Use the template above as reference
3. Test with `--validate-config` flag

```bash
./app --validate-config --config ./config.yaml
```

### Step 2: Update startup command

If you specify config file in your startup:

**Before:**
```bash
./app --config ./config.json
```

**After:**
```bash
./app --config ./config.yaml
```

### Step 3: Remove old config

After verifying the new config works:

```bash
rm config.json
```

## Rollback procedure

If you encounter issues after upgrading:

1. Downgrade to v3.x: `npm install @example/app@3`
2. Your original config.json still works
3. Contact support if needed

## Timeline

| Date | Event |
|------|-------|
| January 2024 | Announcement and migration tool released |
| April 2024 | v4.0.0 released (YAML required) |
| October 2024 | v3.x end of support |

## Support

- Migration tool issues: [GitHub Issues](https://github.com/example/config-migrate/issues)
- Documentation: [Configuration reference](/docs/configuration)
```

---

## Example 3: Edge case — behavioral change (no code changes required)

**Input:**
- Change: Default pagination limit changing from 100 to 20
- Impact: Users relying on implicit default get fewer results
- No code change required if explicit limit used

**Output:**

```md
# Breaking Change: Default Pagination Limit

**Effective date:** February 1, 2024
**Affects:** API consumers not specifying explicit `limit` parameter
**Action required by:** February 1, 2024 (if affected)

## Summary

The default `limit` for paginated endpoints is changing from 100 to 20 to improve performance and reduce unintentional data over-fetching.

## What changed

### Before

```bash
GET /api/users
# Returns up to 100 users by default
```

### After

```bash
GET /api/users
# Returns up to 20 users by default
```

## Who is affected

You are affected if:

- [ ] You call paginated endpoints without specifying `limit`
- [ ] Your code assumes you receive up to 100 results

You are NOT affected if:

- You always specify `limit` parameter explicitly
- You already use `limit=20` or less
- You handle pagination properly with `has_more` flag

### How to check

Search your code for API calls without `limit`:

```bash
# Look for paginated endpoints without limit
grep -r "/users" . | grep -v "limit="
grep -r "/projects" . | grep -v "limit="
```

Or check API logs for requests without `limit` parameter.

## Migration guide

### If you need more than 20 results

Add explicit `limit` parameter to your requests:

**Before:**
```bash
GET /api/users
```

**After:**
```bash
GET /api/users?limit=100
```

Maximum allowed limit remains 100.

### If you're already handling pagination

No changes needed. Your code already handles variable result sizes.

### Verify

After adding explicit limit:
1. Count results returned
2. Confirm you receive expected number
3. Ensure your pagination logic handles `has_more` correctly

## No action required if

Your code already:
- Specifies `limit` on all paginated requests
- Properly iterates through pages using `has_more`
- Doesn't assume specific result count

## Timeline

| Date | Event |
|------|-------|
| January 15, 2024 | Announcement |
| February 1, 2024 | Default changes |

## FAQ

### Why is this changing?

Analysis showed 80% of requests don't need 100 results. The new default reduces server load and improves response times for most users.

### Can I still request 100 results?

Yes. Add `limit=100` to your request. Maximum limit unchanged.

## Support

- Documentation: [Pagination guide](/docs/pagination)
```

---

## Anti-pattern example

**Bad output (do not produce):**

```md
# Important Update

We're changing how authentication works. Please update your code.

The old way won't work anymore after we release the next version.

If you have questions, contact support.
```

**Why this fails:**
- No specific date
- No before/after examples
- No migration steps
- No way to identify if affected
- "Next version" is vague
- No code examples
- No timeline
