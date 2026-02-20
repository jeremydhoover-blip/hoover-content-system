# Examples

## Example 1: Symptom-based troubleshooting

**Input:**
- Problem: Database connection failures in Node.js application
- Context: Production environment, multiple potential causes

**Output:**

```md
# Troubleshooting: Database connection failures

Use this guide when your application fails to connect to the database or connections drop unexpectedly.

## Symptoms

You may see one or more of these:

- Application logs show `ECONNREFUSED` or `ETIMEDOUT` errors
- Error message: `Connection terminated unexpectedly`
- Requests hang and eventually timeout
- Intermittent 500 errors on database-dependent endpoints

## Quick checks

Before diving deeper, verify:

- [ ] Database server is running and accessible from your network
- [ ] Connection string credentials are correct
- [ ] No recent infrastructure changes (firewall, DNS, VPC)

## Possible causes

| Cause | Likelihood | Diagnostic |
|-------|------------|------------|
| Connection pool exhaustion | Common | Active connections at max, queries queuing |
| Network/firewall issues | Common | Cannot reach database host |
| Database server overload | Moderate | High CPU/memory on database server |
| SSL/TLS certificate issues | Rare | SSL handshake errors in logs |

## Diagnosis and resolution

### Cause 1: Connection pool exhaustion

**Identify this cause:** Check your connection pool metrics or logs.

```bash
# If using pg (node-postgres), add pool event logging:
pool.on('connect', () => console.log('Pool connection created'))
pool.on('remove', () => console.log('Pool connection removed'))
```

Signs of pool exhaustion:
- Pool size at maximum
- New queries waiting for available connections
- Connections not being released after query completion

**If this is the cause:**

1. Check for connection leaks—ensure all queries release connections:
   ```javascript
   // Bad: connection not released on error
   const result = await pool.query(sql);
   
   // Good: use pool.query() which auto-releases, or use try/finally
   const client = await pool.connect();
   try {
     const result = await client.query(sql);
   } finally {
     client.release();
   }
   ```

2. Increase pool size if workload requires it:
   ```javascript
   const pool = new Pool({ max: 20 }); // Default is 10
   ```

3. Verify: Monitor pool metrics—active connections should fluctuate, not stay at max.

### Cause 2: Network/firewall issues

**Identify this cause:** Test network connectivity to database host.

```bash
# Test TCP connectivity
nc -zv database-host.example.com 5432

# Test DNS resolution
nslookup database-host.example.com
```

Expected output for healthy connection:
```
Connection to database-host.example.com 5432 port [tcp/postgresql] succeeded!
```

**If this is the cause:**

1. Verify security group or firewall rules allow traffic on database port.
2. Check if database host IP changed (DNS propagation issue).
3. Verify VPC peering or network configuration if applicable.
4. Verify: Run connectivity test again—should succeed.

### Cause 3: Database server overload

**Identify this cause:** Check database server metrics.

```sql
-- PostgreSQL: Check active connections and state
SELECT state, count(*) FROM pg_stat_activity GROUP BY state;

-- Check for long-running queries
SELECT pid, now() - query_start AS duration, query 
FROM pg_stat_activity 
WHERE state = 'active' AND now() - query_start > interval '30 seconds';
```

Signs of overload:
- CPU consistently above 80%
- Many connections in `active` state
- Long-running queries blocking others

**If this is the cause:**

1. Terminate long-running queries if safe:
   ```sql
   SELECT pg_terminate_backend(pid) FROM pg_stat_activity 
   WHERE now() - query_start > interval '5 minutes';
   ```
2. Scale database resources or add read replicas.
3. Optimize slow queries identified in step above.
4. Verify: Server metrics return to normal ranges.

### Cause 4: SSL/TLS certificate issues

**Identify this cause:** Look for SSL-specific errors in logs.

```
Error: SSL SYSCALL error: Connection reset by peer
Error: self signed certificate in certificate chain
```

**If this is the cause:**

1. Verify certificate validity:
   ```bash
   openssl s_client -connect database-host.example.com:5432 -starttls postgres
   ```
2. Update CA certificates if expired.
3. Ensure `ssl` configuration in connection string matches server requirements.
4. Verify: Connection succeeds without SSL errors.

## Still having issues?

If none of the above resolved your issue:

1. Collect diagnostic information:
   - Application logs from the past hour
   - Database server metrics (CPU, memory, connections)
   - Network configuration (security groups, route tables)
   - Connection string (redact password)

2. Contact your database administrator or open a support ticket with the collected information.
```

---

## Example 2: Decision-tree format

**Input:**
- Problem: Build failures in CI/CD pipeline
- Context: Multiple possible failure points

**Output:**

```md
# Troubleshooting: Build failures in CI/CD

Use this guide to systematically identify why your CI/CD build is failing.

## Start here

**Where does the build fail?**

- Fails immediately at checkout → Go to [Checkout issues](#checkout-issues)
- Fails during dependency install → Go to [Dependency issues](#dependency-issues)
- Fails during test execution → Go to [Test failures](#test-failures)
- Fails during artifact build → Go to [Build issues](#build-issues)

---

## Checkout issues

### Step 1: Check repository access

Look for these error patterns:
- `Permission denied (publickey)`
- `Repository not found`
- `Authentication failed`

**Result:**
- Permission/auth errors → [Resolution: SSH keys](#resolution-ssh-keys)
- Repository not found → [Resolution: Repository access](#resolution-repository-access)
- Checkout succeeds but other error → Return to [Start here](#start-here)

---

## Resolution: SSH keys

1. Verify deploy key is added to repository settings.
2. Verify CI/CD secret contains private key with correct format (including newlines).
3. Test key locally:
   ```bash
   ssh -T git@github.com -i /path/to/key
   ```
4. **Verify:** Re-run pipeline—checkout should succeed.

---

## Dependency issues

### Step 1: Identify the failing package

Check build logs for:
- Package name that failed to install
- Network timeout or 404 errors
- Version resolution conflicts

**Result:**
- Network/404 errors → [Resolution: Registry access](#resolution-registry-access)
- Version conflicts → [Resolution: Dependency conflicts](#resolution-dependency-conflicts)
- Out of memory → [Resolution: Resource limits](#resolution-resource-limits)

---

## Resolution: Registry access

1. Verify registry URL is correct in configuration.
2. Check if private registry requires authentication.
3. Test registry access:
   ```bash
   npm ping --registry https://your-registry.com
   ```
4. **Verify:** Dependency install completes successfully.

---

## Escalation

If you've completed the relevant sections without resolution:

- Gather: Full build logs, pipeline configuration, recent changes to repository
- Contact: Platform team via #ci-cd-support channel
```

---

## Example 3: Edge case — intermittent failures

**Input:**
- Problem: Flaky test failures that pass on retry
- Context: Non-deterministic, hard to reproduce

**Output:**

```md
# Troubleshooting: Intermittent test failures

Use this guide when tests fail inconsistently—passing on some runs and failing on others with the same code.

## Symptoms

- Test suite passes locally but fails in CI
- Same test fails on retry 1, passes on retry 2
- Different tests fail on different runs
- Failure rate is non-zero but not 100%

## Quick checks

Before diving deeper, verify:

- [ ] Tests are not sharing mutable state
- [ ] Tests do not depend on execution order
- [ ] No hardcoded timeouts that might race

## Possible causes

| Cause | Likelihood | Diagnostic |
|-------|------------|------------|
| Shared state between tests | Common | Same test fails when run after specific other test |
| Timing/race conditions | Common | Failures correlate with system load |
| External service dependencies | Moderate | Failures include network or timeout errors |
| Resource constraints | Moderate | Failures correlate with memory/CPU spikes |

## Diagnosis and resolution

### Cause 1: Shared state between tests

**Identify this cause:** Run tests in isolation and in different orders.

```bash
# Run failing test in isolation
npm test -- --grep "failing test name"

# Run tests in random order (if framework supports)
npm test -- --random
```

If test passes in isolation but fails in suite, state leakage is likely.

**If this is the cause:**

1. Add proper setup/teardown to reset state:
   ```javascript
   beforeEach(() => {
     // Reset database, clear caches, etc.
   });
   ```
2. Ensure tests don't modify global variables or singletons.
3. **Verify:** Run full suite 5 times—all should pass.

### Cause 2: Timing/race conditions

**Identify this cause:** Look for:
- `setTimeout` or fixed delays in tests
- Assertions that run before async operations complete
- UI tests waiting for elements

**If this is the cause:**

1. Replace fixed delays with proper async waiting:
   ```javascript
   // Bad
   await delay(1000);
   expect(element).toBeVisible();
   
   // Good
   await waitFor(() => expect(element).toBeVisible());
   ```
2. Increase timeouts only as last resort, with justification.
3. **Verify:** Run test 10 times consecutively—all should pass.

### Cause 3: External service dependencies

**Identify this cause:** Check if failures correlate with:
- Network errors in logs
- Specific external API calls
- Time-of-day patterns (rate limits reset)

**If this is the cause:**

1. Mock external services in tests:
   ```javascript
   jest.mock('./api-client', () => ({
     fetchData: jest.fn().mockResolvedValue(mockData)
   }));
   ```
2. If integration tests required, add retry logic with backoff.
3. **Verify:** Tests pass consistently without network access.

## Still having issues?

For persistent intermittent failures:

1. Enable verbose logging for failing tests.
2. Run tests with `--bail` to stop on first failure and capture state.
3. Review recent changes that might have introduced non-determinism.
4. Escalate to team with: failure frequency, test names, relevant logs.
```

---

## Anti-pattern example

**Bad output (do not produce):**

```md
# Database Connection Troubleshooting

If you're having database issues, here are some things to try:

- Make sure your database is running
- Check your connection string
- Try restarting the application
- You might need to increase the pool size
- Check the firewall

To prevent this in the future, always use connection pooling and monitor your database.
```

**Why this fails:**
- No observable symptoms defined
- Causes not differentiated
- No diagnostics to identify which cause applies
- No verification steps
- Prevention advice mixed with troubleshooting
- No escalation path
- "Things to try" approach encourages random debugging
