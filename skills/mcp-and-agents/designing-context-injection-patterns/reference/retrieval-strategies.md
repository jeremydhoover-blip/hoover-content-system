# Retrieval Strategies

## Table of contents
- [Retrieval methods](#retrieval-methods)
- [Selection and ranking](#selection-and-ranking)
- [Chunking strategies](#chunking-strategies)
- [Caching patterns](#caching-patterns)
- [Failure handling](#failure-handling)

---

## Retrieval methods

### Keyword search
Best for: Exact matches, known terminology, structured queries

```
Method: BM25, TF-IDF, full-text search
Pros: Fast, predictable, no ML infrastructure
Cons: Misses synonyms, requires exact terms
Use when: Query contains specific technical terms, IDs, or names
```

### Semantic search
Best for: Natural language queries, conceptual matching

```
Method: Vector embeddings + similarity search
Pros: Handles synonyms, conceptual matches
Cons: Requires embedding infrastructure, less predictable
Use when: User query is conversational, concept-based
```

### Hybrid search
Best for: Balancing precision and recall

```
Method: Combine keyword and semantic scores
Formula: score = α * keyword_score + (1-α) * semantic_score
Typical α: 0.3-0.5
Use when: Mixed query types, production systems
```

### Structured lookup
Best for: Known entities, database records

```
Method: Direct query by ID or key
Pros: Exact, fast, reliable
Cons: Requires entity extraction, no fuzzy matching
Use when: Query mentions specific orders, users, products
```

### Graph traversal
Best for: Related entities, dependency chains

```
Method: Navigate relationships from anchor node
Pros: Finds contextually related content
Cons: Requires graph structure, can explode in scope
Use when: "Related to X", import/export chains, concept maps
```

---

## Selection and ranking

### Relevance scoring
| Signal | Weight | Description |
|--------|--------|-------------|
| Similarity score | High | Vector or keyword match strength |
| Recency | Medium | Newer content often more relevant |
| Source authority | Medium | Trusted sources ranked higher |
| User history | Low-Medium | Content user has engaged with |
| Content quality | Low | Length, structure, completeness |

### Diversity sampling
Avoid retrieving near-duplicate content:
```
1. Retrieve top N * 2 results
2. For each result after first:
   - Calculate similarity to already-selected results
   - If max_similarity > threshold: skip
3. Select until N results or exhausted
```

### Filtering rules
| Filter | Purpose | Example |
|--------|---------|---------|
| Access control | User can see this content | role = "admin" OR public = true |
| Freshness | Content not stale | updated_at > (now - max_age) |
| Content type | Match expected format | type IN ("doc", "faq") |
| Language | Match user's language | lang = user.lang OR lang = "en" |

### Score thresholds
```
Hard threshold: Only include if score > minimum
  - Prevents low-quality noise
  - Risk: May return nothing

Soft threshold: Include top N, warn if below minimum
  - Ensures some results
  - Risk: May include poor matches
```

---

## Chunking strategies

### Fixed-size chunking
```
Method: Split at token/character count
Chunk size: 200-500 tokens typical
Overlap: 10-20% for context continuity
Pros: Simple, predictable budget
Cons: May split mid-sentence or mid-concept
```

### Semantic chunking
```
Method: Split at natural boundaries (paragraphs, sections)
Markers: Headers, blank lines, topic shifts
Pros: Preserves meaning units
Cons: Variable chunk sizes, harder to budget
```

### Hierarchical chunking
```
Method: Nested chunks at different granularities
Levels: Document → Section → Paragraph → Sentence
Selection: Start broad, drill down on relevance
Pros: Flexible detail level
Cons: Complex implementation
```

### Code-aware chunking
```
Method: Split at AST boundaries (functions, classes)
Include: Complete syntactic units
Context: Add imports, class signatures for orphan functions
Pros: Meaningful code units
Cons: Requires language-specific parsing
```

---

## Caching patterns

### Query-based caching
```
Key: hash(normalized_query)
TTL: 1-24 hours (depends on source volatility)
Invalidation: Manual, time-based, or on source update
Use when: Repeated similar queries expected
```

### Entity-based caching
```
Key: entity_type + entity_id (e.g., "product:12345")
TTL: Varies by entity type
Invalidation: On entity update event
Use when: Entities are frequently referenced
```

### Session-based caching
```
Key: session_id + context_type
TTL: Session duration
Invalidation: Session end
Use when: Context reused within conversation
```

### Pre-computation
```
Method: Generate and cache likely-needed context ahead of time
Trigger: User login, session start, scheduled job
Pros: Zero retrieval latency at query time
Cons: Wasted computation if not used
```

---

## Failure handling

### Timeout handling
```
Query timeout: 2-5 seconds typical
On timeout:
  - Return cached results if available
  - Return partial results if streaming
  - Return empty with warning if no fallback
Never: Block indefinitely
```

### Empty result handling
```
Causes: No matches, overly specific query, index issues
Response options:
  - Broaden query automatically (remove filters)
  - Suggest query modifications
  - State explicitly: "No results found for [query]"
  - Fall back to related content
Never: Pretend results exist, hallucinate content
```

### Source unavailability
```
Detection: Connection error, auth failure, service down
Response by criticality:
  - Critical source: Fail with clear error
  - Important source: Warn and continue
  - Optional source: Omit silently, log
Recovery: Retry with backoff, use cache, switch to backup
```

### Degraded quality handling
```
Signals: Low relevance scores, high latency, partial results
Response:
  - Include quality indicator in context
  - Reduce confidence in answers
  - Suggest verification
Message: "Based on limited search results..." or "I found some relevant content, but coverage may be incomplete."
```
