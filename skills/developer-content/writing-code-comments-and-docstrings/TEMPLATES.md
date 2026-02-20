# Templates

## Python docstrings (Google style)

### Function docstring
```python
def function_name(param1: Type1, param2: Type2 = default) -> ReturnType:
    """One-line summary of what the function does.

    Extended description if the function is complex. Explain behavior,
    not implementation. Include important assumptions or constraints.

    Args:
        param1: Description of param1. Include valid ranges or formats.
        param2: Description of param2. Default behavior if omitted.

    Returns:
        Description of return value. Include structure if complex.
        None if no return value (omit section for None returns).

    Raises:
        ExceptionType: When this exception is raised.
        AnotherException: When this other condition occurs.

    Example:
        >>> result = function_name("input", param2=True)
        >>> print(result)
        expected_output

    Note:
        Any important caveats or warnings about usage.
    """
```

### Class docstring
```python
class ClassName:
    """One-line summary of the class purpose.

    Extended description of what this class represents, when to use it,
    and its relationship to other classes if relevant.

    Attributes:
        attr1: Description of public attribute.
        attr2: Description of another attribute.

    Example:
        >>> obj = ClassName(arg1, arg2)
        >>> obj.do_something()
        expected_result
    """
```

### Module docstring
```python
"""One-line summary of module purpose.

Extended description of what this module contains, how its components
relate, and when to use it vs. alternatives.

Typical usage:
    from module import ClassName
    obj = ClassName(...)

Exports:
    ClassName: Primary class for X
    helper_function: Utility for Y
"""
```

## TypeScript/JavaScript JSDoc

### Function documentation
```typescript
/**
 * One-line summary of what the function does.
 *
 * Extended description with behavior details and constraints.
 *
 * @param param1 - Description of param1
 * @param param2 - Description of param2. Defaults to X.
 * @returns Description of return value
 * @throws {ErrorType} When condition occurs
 *
 * @example
 * const result = functionName('input', { option: true });
 * console.log(result); // expected output
 */
function functionName(param1: string, param2?: Options): ReturnType {
```

### Class documentation
```typescript
/**
 * One-line summary of class purpose.
 *
 * Extended description of usage and lifecycle.
 *
 * @example
 * const instance = new ClassName(config);
 * await instance.initialize();
 */
class ClassName {
```

### Property documentation
```typescript
class Example {
  /**
   * Description of what this property represents.
   * Include valid states and when it changes.
   */
  readonly propertyName: Type;
}
```

## Java Javadoc

### Method documentation
```java
/**
 * One-line summary of what the method does.
 *
 * <p>Extended description with behavior details. Use HTML for formatting
 * if needed.
 *
 * @param param1 description of param1
 * @param param2 description of param2
 * @return description of return value
 * @throws ExceptionType when condition occurs
 * @see RelatedClass#relatedMethod
 * @since 1.0
 */
public ReturnType methodName(Type1 param1, Type2 param2) {
```

### Class documentation
```java
/**
 * One-line summary of class purpose.
 *
 * <p>Extended description of usage, thread safety, and lifecycle.
 *
 * @author Author Name
 * @version 1.0
 * @since 1.0
 */
public class ClassName {
```

## Inline comment templates

### Explanation comment
```
// Why: {Reason this approach was chosen over alternatives}
{code}
```

### Constraint comment
```
// Constraint: {What limitation this addresses and why}
{code}
```

### Warning comment
```
// WARNING: {What could break if this is changed}
{code}
```

### Performance comment
```
// Perf: {Why this specific approach, include benchmarks if available}
{code}
```

## Annotation templates

### TODO
```
// TODO({owner}): {What needs to be done}
// Context: {Why it's deferred}
// Ticket: {PROJ-123 or link}
```

### FIXME
```
// FIXME({owner}): {What's broken}
// Impact: {User-facing effect}
// Ticket: {PROJ-123 or link}
```

### HACK
```
// HACK: {What workaround this is}
// Reason: {Why the proper fix isn't possible now}
// Remove when: {Condition for removal}
```

### NOTE
```
// NOTE: {Important context for future readers}
// Related: {Links or references}
```
