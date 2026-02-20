# Templates

## Default context injection specification

```md
# Context Injection: [Agent/Feature Name]

## Context budget
- Total token limit: [number]
- System instructions: [allocation]
- Static context: [allocation]
- Dynamic context: [allocation]
- User query + response buffer: [allocation]

## Context sources

### Static context (loaded once)
| Source | Content | Max tokens | Update frequency |
|--------|---------|------------|------------------|
| [name] | [description] | [limit] | [frequency] |

### Session context (per conversation)
| Source | Content | Max tokens | Trigger |
|--------|---------|------------|---------|
| [name] | [description] | [limit] | [when loaded] |

### Query context (per request)
| Source | Content | Max tokens | Retrieval method |
|--------|---------|------------|------------------|
| [name] | [description] | [limit] | [how selected] |

## Context ordering
1. [First context block]: [rationale]
2. [Second context block]: [rationale]
3. [Third context block]: [rationale]

## Retrieval rules
- [Source]: Retrieve when [condition], select by [criteria], limit to [amount]

## Compression rules
- When over budget: [prioritization and truncation strategy]
- Chunking: [how to split large documents]
- Summarization: [when and how to compress]

## Freshness rules
- [Source]: Max age [duration], refresh [trigger]
- Stale indicator: [how to mark outdated content]

## Fallback behavior
- If [source] unavailable: [action]
- If retrieval returns empty: [action]
```

## Context block format

```md
<context source="[source-name]" type="[static|session|query]" updated="[timestamp]">
[content]
</context>
```

## Retrieval rule format

```md
**[Source-ID]**: [Source name]
- Trigger: [What causes retrieval]
- Query: [How to search/filter]
- Selection: [Ranking or filtering criteria]
- Limit: [Max items or tokens]
- Format: [How to structure for injection]
```
