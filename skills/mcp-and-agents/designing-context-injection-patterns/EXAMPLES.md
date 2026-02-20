# Examples

## Example 1: Customer support agent context injection

Input:
- Agent: Customer support chatbot
- Context sources: Product catalog, user order history, FAQ database, conversation history
- Constraints: 8K token context window, need real-time order status

Output:
```md
# Context Injection: Customer Support Agent

## Context budget
- Total token limit: 8,000
- System instructions: 1,000
- Static context: 500
- Dynamic context: 4,500
- User query + response buffer: 2,000

## Context sources

### Static context (loaded once)
| Source | Content | Max tokens | Update frequency |
|--------|---------|------------|------------------|
| brand-voice | Tone guidelines, greeting templates | 300 | Weekly |
| policy-summary | Return policy, shipping tiers (condensed) | 200 | Monthly |

### Session context (per conversation)
| Source | Content | Max tokens | Trigger |
|--------|---------|------------|---------|
| user-profile | Name, membership tier, preferences | 150 | Session start |
| order-summary | Last 3 orders: items, status, dates | 500 | Session start |
| conversation-history | Last 5 turns | 1,000 | Each turn |

### Query context (per request)
| Source | Content | Max tokens | Retrieval method |
|--------|---------|------------|------------------|
| faq-retrieval | Top 3 matching FAQ entries | 600 | Semantic search on user query |
| product-lookup | Product details if mentioned | 400 | Entity extraction → catalog API |
| order-detail | Full order if referenced | 350 | Order ID extraction → order API |
| real-time-status | Live tracking if asked | 200 | Shipping API on status queries |

## Context ordering
1. System instructions: Establishes agent persona and constraints
2. User profile + order summary: Personalizes conversation
3. Conversation history: Maintains continuity
4. Query-specific retrieval: Addresses current question
5. Static policies: Available for reference

## Retrieval rules
- faq-retrieval: Retrieve when query is a question; select by cosine similarity > 0.7; limit to 3 results
- product-lookup: Retrieve when product name detected; exact match then fuzzy; limit to 1 product
- order-detail: Retrieve when order ID pattern matched; exact lookup; include all line items
- real-time-status: Retrieve when query contains "where", "tracking", "status"; API call; cache 5 min

## Compression rules
- When over budget: Drop oldest conversation turns first, then reduce FAQ results to 2
- Chunking: Product descriptions truncated to first 100 tokens
- Summarization: Order history beyond 3 orders summarized as "N previous orders"

## Freshness rules
- real-time-status: Max age 5 minutes, refresh on each status query
- order-summary: Max age 1 hour, refresh if order action taken
- Stale indicator: Append "(as of [time])" to time-sensitive data

## Fallback behavior
- If user-profile unavailable: Proceed without personalization, use generic greeting
- If faq-retrieval returns empty: Offer to connect with human support
- If order-detail fails: State "I couldn't retrieve your order details. Can you confirm the order number?"
```

---

## Example 2: Code assistant context injection

Input:
- Agent: IDE code assistant
- Context sources: Current file, open files, project structure, documentation, conversation
- Constraints: 16K context window, must prioritize current file

Output:
```md
# Context Injection: Code Assistant

## Context budget
- Total token limit: 16,000
- System instructions: 800
- Static context: 200
- Dynamic context: 11,000
- User query + response buffer: 4,000

## Context sources

### Static context (loaded once)
| Source | Content | Max tokens | Update frequency |
|--------|---------|------------|------------------|
| language-config | Language, framework, linting rules | 200 | On project open |

### Session context (per conversation)
| Source | Content | Max tokens | Trigger |
|--------|---------|------------|---------|
| project-structure | Directory tree (depth 3) | 500 | Session start, on file create/delete |
| open-files-summary | File names and first-line summaries | 300 | On tab change |

### Query context (per request)
| Source | Content | Max tokens | Retrieval method |
|--------|---------|------------|------------------|
| current-file | Full content of active file | 4,000 | Always, cursor position marked |
| cursor-context | 50 lines above and below cursor | 2,000 | On edit request |
| related-files | Files importing/imported by current | 2,500 | Dependency analysis |
| symbol-definitions | Definitions for referenced symbols | 1,200 | AST extraction |
| doc-retrieval | Relevant documentation snippets | 800 | Semantic search on error/question |

## Context ordering
1. System instructions: Defines assistant behavior
2. Language config: Sets syntax and style expectations
3. Current file with cursor marker: Primary working context
4. Cursor context (expanded): Immediate focus area
5. Symbol definitions: Required for understanding references
6. Related files: Broader codebase context
7. Documentation: Reference for APIs and libraries

## Retrieval rules
- related-files: Retrieve when editing; analyze imports; select files with most references; limit to 3 files
- symbol-definitions: Retrieve for undefined symbols in cursor context; AST lookup; include full definition
- doc-retrieval: Retrieve on error messages or "how to" queries; semantic search on official docs; limit to 2 snippets

## Compression rules
- When over budget: Truncate related-files to first 500 tokens each; drop doc-retrieval
- Chunking: Large files split at function boundaries; include complete functions
- Summarization: Files >1000 tokens show structure outline with "// ... implementation" markers

## Freshness rules
- current-file: Always current (read on each request)
- project-structure: Refresh on file system events
- Stale indicator: None needed (all code context is live)

## Fallback behavior
- If symbol-definitions unavailable: Proceed with warning "Definition not found in workspace"
- If doc-retrieval returns empty: Omit section, do not hallucinate documentation
- If related-files analysis fails: Include open-files-summary as fallback
```

---

## Example 3: Edge case — multi-source research agent

Input:
- Agent: Research assistant with access to multiple knowledge bases
- Context sources: Internal docs, external APIs, cached searches, user notes
- Constraints: 32K context, must attribute all sources, handle conflicting information

Output:
```md
# Context Injection: Research Agent

## Context budget
- Total token limit: 32,000
- System instructions: 1,200
- Static context: 800
- Dynamic context: 25,000
- User query + response buffer: 5,000

## Context sources

### Static context (loaded once)
| Source | Content | Max tokens | Update frequency |
|--------|---------|------------|------------------|
| source-registry | Available sources, reliability ratings, access rules | 500 | Daily |
| citation-format | Required attribution format | 300 | Static |

### Session context (per conversation)
| Source | Content | Max tokens | Trigger |
|--------|---------|------------|---------|
| user-notes | User's pinned notes and saved snippets | 1,500 | Session start |
| search-history | Previous queries and selected results | 1,000 | Each search |
| conversation-context | Last 10 turns | 2,500 | Each turn |

### Query context (per request)
| Source | Content | Max tokens | Retrieval method |
|--------|---------|------------|------------------|
| internal-docs | Relevant internal documentation | 6,000 | Vector search, top 5 |
| external-api-1 | Results from [API source 1] | 4,000 | API query on external toggle |
| external-api-2 | Results from [API source 2] | 4,000 | API query on external toggle |
| cached-search | Previously fetched external results | 3,000 | Cache lookup before API |
| cross-reference | Overlapping content from multiple sources | 2,000 | Deduplication pass |

## Context ordering
1. System instructions with attribution requirements
2. Source registry: Establishes what sources are available and trusted
3. User notes: User's curated context takes priority
4. Internal docs: Primary knowledge base
5. Cached search results: Efficient reuse
6. External API results: Fresh external data
7. Cross-reference summary: Highlights conflicts
8. Conversation context: Maintains thread

## Retrieval rules
- internal-docs: Retrieve always; vector similarity > 0.75; limit to 5 chunks; include doc title and date
- external-api-1: Retrieve when user enables external sources; query reformulation; limit to 10 results
- cached-search: Check cache first (key: normalized query); TTL 24 hours; skip API if cache hit
- cross-reference: Run after all retrieval; identify overlapping claims; flag conflicts with source labels

## Compression rules
- When over budget: Reduce external results first; summarize internal docs to abstracts
- Chunking: Documents split at section headers; minimum chunk 200 tokens
- Summarization: Enable extractive summary for docs > 2000 tokens

## Freshness rules
- internal-docs: Max age 30 days for versioned docs; no limit for reference docs
- external-api results: Max age 24 hours; refresh on explicit "update" request
- cached-search: TTL 24 hours; indicate age in citation
- Stale indicator: "[Source name] (retrieved [date])"

## Fallback behavior
- If internal-docs unavailable: State "Internal knowledge base unavailable. Searching external sources only."
- If external-api fails: Use cached results with stale warning; if no cache, state source unavailable
- If cross-reference finds conflicts: Present both positions with source attribution; do not resolve
- If all retrieval fails: State "I couldn't find relevant information. Here's what I searched: [list sources]"
```
