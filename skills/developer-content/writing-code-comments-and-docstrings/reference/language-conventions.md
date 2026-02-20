# Language-Specific Documentation Conventions

## Python

### Style variants

| Style | Used by | Format |
|-------|---------|--------|
| Google | Google, most startups | `Args:`, `Returns:`, `Raises:` |
| NumPy | Scientific Python | `Parameters`, `Returns`, `Raises` sections |
| Sphinx (reST) | Many libraries | `:param name:`, `:returns:`, `:raises:` |
| Epytext | Legacy projects | `@param`, `@return`, `@raise` |

**Recommendation:** Google style for readability; NumPy for data science.

### First line rules
- Complete sentence, ends with period
- Imperative mood: "Return X" not "Returns X"
- ≤79 characters (fits in one line with indentation)
- Don't start with "This function/method/class"

### Type hints vs. docstrings
- Use type hints in signature: `def foo(x: int) -> str:`
- In docstring, describe constraints: "Must be positive integer"
- Don't duplicate type info if using type hints

## TypeScript/JavaScript

### JSDoc vs. TSDoc
- **JSDoc**: Widely supported, works in JS and TS
- **TSDoc**: Microsoft standard, stricter, better for TS-only

### Key tags
```typescript
@param name - Description
@returns Description
@throws {ErrorType} Description
@example Code example
@see RelatedSymbol
@deprecated Use X instead
@internal Not part of public API
@readonly Cannot be modified
```

### Type annotations in JSDoc
```javascript
/**
 * @param {string} name - User's name
 * @param {Object} options - Configuration object
 * @param {number} [options.timeout=5000] - Timeout in ms
 * @returns {Promise<User>}
 */
```

## Java

### Javadoc rules
- First sentence becomes summary (ends at first period)
- Use `<p>` for paragraph breaks
- Use `{@code text}` for inline code
- Use `{@link Class#method}` for cross-references

### Required tags by element
| Element | Required tags |
|---------|---------------|
| Method | @param (all), @return, @throws |
| Class | Description only |
| Interface | Description, @since |
| Package | Description in package-info.java |

### Inheritance
- Subclass methods inherit parent docs
- Use `{@inheritDoc}` to include parent description
- Override only what changes

## Go

### Godoc conventions
- Comment starts with element name: `// FunctionName does X`
- No special tags or markup
- First sentence is summary
- Blank line separates paragraphs
- Code blocks indented

```go
// ParseConfig reads the configuration file at path and returns
// the parsed configuration. It returns an error if the file
// cannot be read or contains invalid syntax.
//
// The configuration file must be valid YAML:
//
//	server:
//	  port: 8080
//
// ParseConfig validates all required fields and applies defaults
// for optional fields.
func ParseConfig(path string) (*Config, error) {
```

## Rust

### Rustdoc conventions
- Uses Markdown
- First paragraph is summary
- Code blocks are tested by default

```rust
/// Parses a configuration file and returns the configuration.
///
/// # Arguments
///
/// * `path` - Path to the configuration file
///
/// # Returns
///
/// The parsed configuration, or an error if parsing fails.
///
/// # Errors
///
/// Returns `ConfigError::NotFound` if the file doesn't exist.
/// Returns `ConfigError::Invalid` if the file contains invalid syntax.
///
/// # Examples
///
/// ```
/// let config = parse_config("config.yaml")?;
/// assert_eq!(config.port, 8080);
/// ```
pub fn parse_config(path: &str) -> Result<Config, ConfigError> {
```

## C#

### XML documentation
```csharp
/// <summary>
/// One-line summary.
/// </summary>
/// <param name="parameter">Description.</param>
/// <returns>Description of return value.</returns>
/// <exception cref="ExceptionType">When thrown.</exception>
/// <example>
/// <code>
/// var result = Method(arg);
/// </code>
/// </example>
/// <remarks>
/// Extended description and notes.
/// </remarks>
/// <seealso cref="RelatedClass"/>
```

## Inline comment conventions (all languages)

### Universal patterns
| Pattern | Use for |
|---------|---------|
| `// Why:` | Non-obvious decisions |
| `// Note:` | Important context |
| `// HACK:` | Workarounds |
| `// TODO:` | Deferred work |
| `// FIXME:` | Known bugs |
| `// PERF:` | Performance decisions |
| `// SECURITY:` | Security considerations |

### What NOT to comment
- What the code literally does
- Obvious variable names
- Standard library usage
- Language syntax
