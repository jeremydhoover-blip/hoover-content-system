# Diff Format Reference

## Table of Contents
1. [Structural diff](#structural-diff)
2. [Semantic diff](#semantic-diff)
3. [Output formats](#output-formats)
4. [Change classification](#change-classification)

---

## Structural diff

Structural diff identifies what physically changed between two context pack versions.

### Diff operations

| Symbol | Operation | Meaning |
|--------|-----------|---------|
| `+` | Added | Element exists in head, not in base |
| `-` | Removed | Element exists in base, not in head |
| `~` | Modified | Element exists in both, values differ |
| ` ` | Unchanged | Element identical in both |

### Diffable elements

| Element | Granularity | Example |
|---------|-------------|---------|
| Section | Presence | `states` added or removed |
| Key | Presence | `states.idle` added or removed |
| Value | Content | `states.idle.entry` value changed |
| Array item | Membership | `user_goals[0]` added or removed |

### Structural diff algorithm

```
FOR each key IN union(base.keys, head.keys):
  IF key IN base AND key NOT IN head:
    EMIT removed(key, base[key])
  ELSE IF key NOT IN base AND key IN head:
    EMIT added(key, head[key])
  ELSE IF base[key] != head[key]:
    IF is_object(base[key]) AND is_object(head[key]):
      RECURSE(base[key], head[key])
    ELSE:
      EMIT modified(key, base[key], head[key])
```

---

## Semantic diff

Semantic diff classifies structural changes by their impact on consumers.

### Impact levels

| Level | Consumer impact | Version effect |
|-------|-----------------|----------------|
| Breaking | Must update content | Major bump |
| Additive | May use new features | Minor bump |
| Corrective | No action required | Patch bump |
| None | Identical | No change |

### Classification rules

#### Breaking changes
```
BREAKING IF:
  - State removed
  - State renamed (detected as remove + add with similar content)
  - Transition removed
  - Transition.trigger changed
  - Error code removed or changed
  - Vocabulary term removed
  - Vocabulary definition meaning changed
  - Core action removed or renamed
  - User goal removed
```

#### Additive changes
```
ADDITIVE IF:
  - State added
  - Transition added
  - Error code added
  - Vocabulary term added
  - Core action added
  - User goal added
  - Optional section added
```

#### Corrective changes
```
CORRECTIVE IF:
  - Typo fixed (same words, different spelling)
  - Grammar improved (same meaning, different structure)
  - Clarification added (superset of previous meaning)
  - Content guidance improved (same state, better guidance)
  - Message pattern improved (same error, better message)
```

---

## Output formats

### Human-readable diff

Full narrative format for review:

```md
## Breaking Changes

### [BREAK-001] State removed: verify
- **Section:** states.verify
- **Was:** [full previous definition]
- **Now:** Removed
- **Impact:** [consumer impact]
- **Migration:** [steps to update]
```

### Machine-readable diff

JSON format for automation:

```json
{
  "breaking": [
    {
      "code": "BREAK-001",
      "type": "state_removed",
      "path": "states.verify",
      "base_value": {"entry": "...", "exit": "..."},
      "head_value": null,
      "migration": "Remove references to verify state"
    }
  ],
  "additive": [],
  "corrective": []
}
```

### Inline diff

Git-style format for visual comparison:

```diff
## states

  idle:
    entry: Page load
-   exit: User clicks button
+   exit: User selects action

- verify:
-   entry: Code received
-   exit: Code validated

+ processing:
+   entry: Action initiated
+   exit: Action completes
```

### Summary format

Compact format for CI output:

```
DIFF: file-upload 1.2.0 → 1.3.0
BREAKING: 0 | ADDITIVE: 2 | CORRECTIVE: 1
RECOMMEND: 1.3.0 (MINOR)
```

---

## Change classification

### Meaning change detection

To determine if a definition change is corrective or breaking:

#### Corrective indicators
- Character edits only (Levenshtein distance < 3)
- Same key nouns and verbs
- Added clarifying phrases without contradiction
- Improved grammar without meaning change

#### Breaking indicators
- Key nouns replaced
- Key verbs replaced
- Scope narrowed or expanded
- Preconditions changed
- Postconditions changed
- Examples contradict previous examples

### Rename detection

Detect renamed elements (avoid false positive for remove + add):

```
IF state removed AND state added:
  similarity = compute_similarity(removed.content, added.content)
  IF similarity > 0.8:  # 80% content similarity threshold
    CLASSIFY AS renamed(old_name, new_name)
    EMIT breaking_change (rename is breaking)
  ELSE:
    CLASSIFY AS removed + added separately
```

### Array diff

For arrays (user_goals, core_actions):

```
FOR each item IN base_array:
  IF item NOT IN head_array:
    EMIT removed(item)

FOR each item IN head_array:
  IF item NOT IN base_array:
    EMIT added(item)
```

Array item removal is breaking.
Array item addition is additive.

---

## Diff ordering

Present changes in this order:

1. **Breaking changes** (most important first)
   - State removals/renames
   - Transition removals
   - Error code changes
   - Vocabulary changes
   - Action changes

2. **Additions**
   - New states
   - New transitions
   - New errors
   - New vocabulary

3. **Corrections**
   - Typos
   - Clarifications
   - Formatting

This ordering ensures reviewers see breaking changes first.
