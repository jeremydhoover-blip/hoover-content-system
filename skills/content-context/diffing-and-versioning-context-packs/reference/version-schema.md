# Version Schema Reference

## Table of Contents
1. [Semantic versioning overview](#semantic-versioning-overview)
2. [Version format](#version-format)
3. [Increment rules](#increment-rules)
4. [Pre-release and build metadata](#pre-release-and-build-metadata)
5. [Version comparison](#version-comparison)

---

## Semantic versioning overview

Context packs follow semantic versioning (semver) to communicate change impact to consumers.

Version numbers encode:
- **MAJOR**: Breaking changes that require consumer updates
- **MINOR**: Backward-compatible additions
- **PATCH**: Backward-compatible corrections

Consumers can use version constraints to depend on context packs safely:
- `^1.0.0` — Accept any 1.x.x (minor/patch updates)
- `~1.2.0` — Accept any 1.2.x (patch updates only)
- `1.2.3` — Exact version only

---

## Version format

```
MAJOR.MINOR.PATCH[-PRERELEASE][+BUILD]
```

| Component | Format | Purpose |
|-----------|--------|---------|
| MAJOR | Non-negative integer | Breaking changes |
| MINOR | Non-negative integer | Additions |
| PATCH | Non-negative integer | Corrections |
| PRERELEASE | Alphanumeric + dots | Pre-release identifier |
| BUILD | Alphanumeric + dots | Build metadata |

### Valid examples
```
1.0.0
2.3.1
1.0.0-alpha
1.0.0-alpha.1
1.0.0-beta.2+build.123
0.1.0
```

### Invalid examples
```
1.0          # Missing PATCH
v1.0.0       # No 'v' prefix allowed
1.0.0.0      # Too many components
1.0.0-       # Empty prerelease
```

---

## Increment rules

### When to bump MAJOR (X.0.0)

Bump major when you make incompatible changes that require consumers to update their content.

| Change type | Example | Reason |
|-------------|---------|--------|
| State removed | Remove `verify` state | Existing content references break |
| State renamed | `uploading` → `in_progress` | References break |
| Required field removed | Remove `error_handling` | Consumers depending on it fail |
| Transition removed | Remove `idle` → `error` | Flow path breaks |
| Error code changed | `EXPIRED` → `TIMEOUT` | Error handling logic breaks |
| Vocabulary term removed | Remove `reset_token` | Term references undefined |
| Definition meaning changed | Personal → shared workspace | Content semantically incorrect |
| Core action renamed | `submit` → `send` | Action references break |

### When to bump MINOR (x.Y.0)

Bump minor when you add functionality without breaking existing usage.

| Change type | Example | Reason |
|-------------|---------|--------|
| State added | Add `processing` state | Extends capability |
| Transition added | Add new flow path | Extends capability |
| Error code added | Add `RATE_LIMITED` | Extends error handling |
| Vocabulary term added | Add `batch_upload` | Extends terminology |
| User goal added | Add "Upload folder" | Extends scope |
| Optional field added | Add `tone_boundaries` | Extends without breaking |

### When to bump PATCH (x.y.Z)

Bump patch when you make corrections that don't change meaning or structure.

| Change type | Example | Reason |
|-------------|---------|--------|
| Typo fixed | "satarts" → "starts" | No semantic change |
| Grammar improved | Better phrasing | No semantic change |
| Clarification added | More detail | Meaning unchanged |
| Formatting fixed | Whitespace, punctuation | No semantic change |
| Example updated | Better example | Meaning unchanged |

---

## Pre-release and build metadata

### Pre-release versions

Use pre-release tags for work-in-progress versions.

```
1.0.0-alpha      # First unstable release
1.0.0-alpha.1    # Alpha iteration
1.0.0-beta       # Feature complete, testing
1.0.0-rc.1       # Release candidate
```

Pre-release precedence (lowest to highest):
1. `alpha`
2. `beta`
3. `rc`
4. (release)

### Build metadata

Build metadata is ignored for version precedence but useful for traceability.

```
1.0.0+20260220           # Build date
1.0.0+sha.abc1234        # Git commit
1.0.0-beta+build.456     # Prerelease with build
```

---

## Version comparison

### Precedence rules

1. Compare MAJOR, MINOR, PATCH numerically left to right
2. Pre-release versions have lower precedence than release
3. Pre-release identifiers compared alphanumerically

### Examples

```
1.0.0 < 2.0.0 < 2.1.0 < 2.1.1
1.0.0-alpha < 1.0.0-beta < 1.0.0-rc.1 < 1.0.0
1.0.0-alpha.1 < 1.0.0-alpha.2 < 1.0.0-alpha.10
```

### Decision table

| Base | Head | Comparison |
|------|------|------------|
| 1.0.0 | 1.0.0 | Equal |
| 1.0.0 | 1.0.1 | Head newer (patch) |
| 1.0.0 | 1.1.0 | Head newer (minor) |
| 1.0.0 | 2.0.0 | Head newer (major) |
| 1.0.0 | 1.0.0-alpha | Base newer (pre-release < release) |
| 1.0.0-alpha | 1.0.0-beta | Head newer |

---

## Context pack version field

Store version in the feature section:

```yaml
feature:
  name: feature-name
  purpose: What it does
  version: 1.2.3
```

Version is optional but strongly recommended for:
- Published context packs
- Context packs with multiple consumers
- Context packs under active development
