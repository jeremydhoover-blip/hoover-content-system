# Context Types

## Table of contents
- [Context classification](#context-classification)
- [Static context](#static-context)
- [Session context](#session-context)
- [Query context](#query-context)
- [Real-time context](#real-time-context)
- [Context attributes](#context-attributes)

---

## Context classification

| Type | Loaded when | Changes | Examples |
|------|-------------|---------|----------|
| Static | Agent initialization | Rarely | System prompts, brand guidelines, policy docs |
| Session | Conversation start | Per session | User profile, preferences, conversation history |
| Query | Each request | Per request | Retrieved documents, search results, API responses |
| Real-time | Continuous | Constantly | Live data feeds, sensor readings, market prices |

---

## Static context

### Characteristics
- Loaded once at agent startup or configuration
- Stable across conversations and users
- Low retrieval cost (cached in memory)
- High token investment justified by universal applicability

### Common sources
| Source | Content | Typical size |
|--------|---------|--------------|
| System instructions | Agent persona, capabilities, constraints | 500-2000 tokens |
| Brand/style guides | Voice, tone, terminology rules | 200-500 tokens |
| Policy summaries | Compliance rules, prohibited topics | 200-400 tokens |
| Domain knowledge | Core facts, definitions, taxonomies | 500-2000 tokens |
| Tool descriptions | Available tools and usage patterns | 300-1000 tokens |

### Best practices
- Keep static context minimal—if it doesn't apply to every query, it's not static
- Version and cache static context to avoid repeated processing
- Review quarterly for accuracy and relevance
- Compress verbose sources to essential points

---

## Session context

### Characteristics
- Loaded at session start, persists through conversation
- User-specific or conversation-specific
- Medium retrieval cost (database lookup)
- Grows during session (conversation history)

### Common sources
| Source | Content | Typical size |
|--------|---------|--------------|
| User profile | Name, preferences, tier, history summary | 100-300 tokens |
| Conversation history | Previous turns in current session | 500-3000 tokens |
| Session state | Current task, pending actions, selections | 100-500 tokens |
| User workspace | Open files, active project, recent activity | 300-1000 tokens |
| Preferences | Language, format preferences, accessibility | 50-150 tokens |

### Best practices
- Implement sliding window for conversation history
- Summarize older turns rather than truncating entirely
- Store session state explicitly rather than inferring from history
- Clear sensitive data at session end

### Conversation history strategies
| Strategy | Method | Tradeoff |
|----------|--------|----------|
| Full history | Include all turns | Rich context, token-expensive |
| Sliding window | Last N turns | Predictable budget, loses early context |
| Summarization | Compress older turns | Retains gist, loses details |
| Selective | Keep key turns (decisions, corrections) | Relevant history, complex to implement |

---

## Query context

### Characteristics
- Retrieved fresh for each request
- Content depends on user's current query
- High retrieval cost (search, API calls)
- Most flexible and powerful context type

### Common sources
| Source | Content | Typical size |
|--------|---------|--------------|
| Retrieved documents | Relevant docs from knowledge base | 1000-5000 tokens |
| Search results | Web or internal search matches | 500-2000 tokens |
| API responses | Live data from external services | 200-1000 tokens |
| Entity context | Details about mentioned entities | 300-1000 tokens |
| Code context | Current file, related files, definitions | 2000-8000 tokens |

### Best practices
- Retrieve only on explicit need—avoid speculative retrieval
- Rank and filter results before injection
- Include source attribution with every retrieval
- Set hard limits per source to prevent single-source dominance

---

## Real-time context

### Characteristics
- Continuously updated or fetched on-demand
- Time-sensitive, requires freshness tracking
- Highest retrieval cost (live APIs, streams)
- Must handle latency and failures gracefully

### Common sources
| Source | Content | Typical size |
|--------|---------|--------------|
| Live status | Order tracking, system health, user presence | 50-200 tokens |
| Market data | Prices, availability, rates | 100-500 tokens |
| Sensor data | IoT readings, location, environmental data | 50-300 tokens |
| Notifications | Alerts, updates since last check | 100-400 tokens |

### Best practices
- Cache with short TTL rather than fetching every request
- Display freshness timestamp to user
- Define acceptable staleness for each source
- Implement graceful degradation for API failures

---

## Context attributes

Every context source should have defined:

| Attribute | Description | Example |
|-----------|-------------|---------|
| Source ID | Unique identifier | `user-profile`, `faq-retrieval` |
| Content type | What information it provides | "User's order history" |
| Max tokens | Budget allocation | 500 |
| Retrieval trigger | When to fetch | "Session start", "Order ID mentioned" |
| Freshness requirement | Max acceptable age | "5 minutes", "24 hours", "N/A" |
| Fallback behavior | Action if unavailable | "Proceed without", "Ask user", "Error" |
| Attribution format | How to cite in output | "[Source name, date]" |
| Compression rule | How to shrink if over budget | "Truncate to 200 tokens" |
