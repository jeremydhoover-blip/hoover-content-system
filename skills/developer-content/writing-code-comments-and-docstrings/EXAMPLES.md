# Examples

## Example 1: Python function with complex behavior

**Input:**
- Language: Python
- Function: Retry decorator with exponential backoff
- Audience: Library consumers

**Output:**

```python
def retry(
    max_attempts: int = 3,
    initial_delay: float = 1.0,
    max_delay: float = 60.0,
    exponential_base: float = 2.0,
    retryable_exceptions: tuple[type[Exception], ...] = (Exception,),
) -> Callable[[F], F]:
    """Decorator that retries a function with exponential backoff on failure.

    Wraps a function to automatically retry when specified exceptions occur.
    Delay between retries increases exponentially up to a maximum. Useful for
    network calls, API requests, or any operation with transient failures.

    Args:
        max_attempts: Maximum number of attempts before giving up. Must be >= 1.
        initial_delay: Seconds to wait before first retry. Must be > 0.
        max_delay: Maximum seconds between retries. Caps exponential growth.
        exponential_base: Multiplier for delay growth. Use 1.0 for constant delay.
        retryable_exceptions: Exception types that trigger retry. Others propagate
            immediately.

    Returns:
        Decorated function with retry behavior. Preserves original signature.

    Raises:
        ValueError: If max_attempts < 1 or delays are non-positive.
        The original exception: After all retry attempts exhausted.

    Example:
        >>> @retry(max_attempts=3, retryable_exceptions=(ConnectionError,))
        ... def fetch_data(url: str) -> dict:
        ...     return requests.get(url).json()
        >>> 
        >>> # Will retry up to 3 times on ConnectionError
        >>> data = fetch_data("https://api.example.com/data")

    Note:
        Jitter is not applied. For high-concurrency scenarios, consider adding
        random jitter to prevent thundering herd.
    """
```

---

## Example 2: TypeScript class with lifecycle

**Input:**
- Language: TypeScript
- Class: Database connection pool
- Audience: Internal team

**Output:**

```typescript
/**
 * Manages a pool of database connections with automatic lifecycle handling.
 *
 * Creates connections lazily on first use and maintains them for reuse.
 * Handles connection health checks, automatic reconnection, and graceful
 * shutdown. Thread-safe for concurrent access.
 *
 * @example
 * const pool = new ConnectionPool({
 *   host: 'localhost',
 *   maxConnections: 10,
 *   idleTimeout: 30000
 * });
 *
 * // Get a connection (creates one if needed)
 * const conn = await pool.acquire();
 * try {
 *   await conn.query('SELECT * FROM users');
 * } finally {
 *   pool.release(conn);
 * }
 *
 * // Cleanup on shutdown
 * await pool.close();
 */
export class ConnectionPool {
  /**
   * Current number of active connections.
   * Includes both in-use and idle connections.
   */
  readonly activeCount: number;

  /**
   * Creates a new connection pool with the specified configuration.
   *
   * Does not establish connections immediately; first connection is
   * created on first `acquire()` call.
   *
   * @param config - Pool configuration options
   * @throws {ConfigurationError} If required config values are missing
   */
  constructor(config: PoolConfig) { }

  /**
   * Acquires a connection from the pool.
   *
   * Returns an existing idle connection if available, otherwise creates
   * a new one up to `maxConnections`. Blocks if pool is exhausted until
   * a connection becomes available or timeout expires.
   *
   * @param timeout - Max milliseconds to wait. Defaults to config value.
   * @returns A database connection ready for queries
   * @throws {PoolExhaustedError} If no connection available within timeout
   * @throws {ConnectionError} If unable to establish new connection
   */
  async acquire(timeout?: number): Promise<Connection> { }

  /**
   * Returns a connection to the pool for reuse.
   *
   * Connection is validated before being added to idle pool. Invalid
   * connections are discarded and a new one will be created on next
   * acquire. Safe to call multiple times (subsequent calls are no-ops).
   *
   * @param connection - The connection to release
   */
  release(connection: Connection): void { }

  /**
   * Closes all connections and prevents new acquisitions.
   *
   * Waits for in-use connections to be released before closing them.
   * After close, all acquire calls will throw PoolClosedError.
   *
   * @param force - If true, closes in-use connections immediately
   * @returns Resolves when all connections are closed
   */
  async close(force?: boolean): Promise<void> { }
}
```

---

## Example 3: Inline comments for complex algorithm

**Input:**
- Language: Python
- Code: Rate limiter using token bucket
- Audience: Future maintainers

**Output:**

```python
class TokenBucketRateLimiter:
    def __init__(self, rate: float, capacity: int):
        self.rate = rate          # tokens per second
        self.capacity = capacity  # max tokens
        self.tokens = capacity    # start full
        self.last_update = time.monotonic()
        self._lock = threading.Lock()

    def acquire(self, tokens: int = 1) -> bool:
        """Attempt to acquire tokens, returning True if successful."""
        with self._lock:
            now = time.monotonic()
            elapsed = now - self.last_update
            
            # Refill tokens based on time elapsed since last check.
            # Why monotonic: avoids issues with system clock changes.
            # Why min: prevents overflow if called after long idle period.
            self.tokens = min(
                self.capacity,
                self.tokens + elapsed * self.rate
            )
            self.last_update = now
            
            if self.tokens >= tokens:
                self.tokens -= tokens
                return True
            
            # Returning False instead of blocking allows caller to decide
            # whether to wait, retry, or fail fast.
            return False

    def wait_for_token(self, tokens: int = 1, timeout: float | None = None) -> bool:
        """Block until tokens available or timeout expires."""
        deadline = time.monotonic() + timeout if timeout else float('inf')
        
        while time.monotonic() < deadline:
            if self.acquire(tokens):
                return True
            
            # Sleep calculation: estimate time until enough tokens refill.
            # Why 0.9 multiplier: wake slightly early to avoid missing the
            # exact moment due to scheduling jitter.
            with self._lock:
                tokens_needed = tokens - self.tokens
                wait_time = (tokens_needed / self.rate) * 0.9
            
            # Cap wait time to avoid sleeping past deadline
            remaining = deadline - time.monotonic()
            time.sleep(min(wait_time, remaining, 0.1))  # 0.1s max to stay responsive
        
        return False
```

---

## Example 4: Edge case—documenting workarounds and limitations

**Input:**
- Context: Code with known issues and workarounds
- Need: Warn future developers

**Output:**

```python
def parse_legacy_config(path: str) -> dict:
    """Parse configuration file in legacy format.

    Args:
        path: Path to configuration file.

    Returns:
        Parsed configuration as dictionary.

    Raises:
        ConfigParseError: If file format is invalid.

    Note:
        This parser handles the pre-2.0 config format. For new configs,
        use `parse_config()` instead. Legacy support will be removed in v4.0.
    """
    with open(path) as f:
        content = f.read()
    
    # HACK: Legacy configs may have Windows line endings even on Unix.
    # The old config writer used os.linesep inconsistently.
    # Remove when: legacy config support is dropped in v4.0
    content = content.replace('\r\n', '\n')
    
    # HACK: Some legacy configs have trailing commas in arrays.
    # This is invalid JSON but was allowed by the old parser.
    # Regex removes trailing commas before ] or }
    content = re.sub(r',\s*([}\]])', r'\1', content)
    
    try:
        data = json.loads(content)
    except json.JSONDecodeError as e:
        raise ConfigParseError(f"Invalid config at {path}: {e}") from e
    
    # NOTE: Legacy configs used "db_host" while new format uses "database.host".
    # This migration happens here for backward compatibility.
    if 'db_host' in data:
        data.setdefault('database', {})['host'] = data.pop('db_host')
        data['database']['port'] = data.pop('db_port', 5432)
    
    return data


# TODO(team-platform): Migrate remaining users off legacy config format
# Context: ~15% of users still on pre-2.0 configs as of 2024-01
# Ticket: PLAT-1234
# Blocked by: Need to communicate deprecation timeline to enterprise users
```
