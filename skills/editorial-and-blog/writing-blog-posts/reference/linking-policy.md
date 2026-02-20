# Linking policy

## Internal linking rules

### Minimum requirements
- At least one internal link per blog post
- Link to related content within the first half of the post
- Use descriptive anchor text (not "click here")

### Link placement strategy

| Position | Purpose | Example |
|----------|---------|---------|
| Introduction | Orient reader to related context | "We covered [related topic] last month" |
| Body | Provide depth on subtopics | "For details on this step, see [tutorial]" |
| Conclusion | Guide next action | "Ready to go deeper? [Related post]" |
| Related posts | Extend session | Curated list at post end |

### Anchor text guidelines

**Good anchor text:**
- Describes destination content
- Uses natural phrasing
- Includes keywords where appropriate

**Bad anchor text:**
- "Click here"
- "Read more"
- "This article"
- Over-optimized keyword stuffing

### Examples
✅ "Learn more about [API authentication best practices]"
✅ "We explored this in our [guide to sprint planning]"
❌ "[Click here] to read the full guide"
❌ "For more, [read this]"

---

## External linking rules

### When to link externally

| Link to | When |
|---------|------|
| Primary sources | Citing research, statistics, studies |
| Official documentation | Referencing tools, platforms, APIs |
| Expert content | Crediting ideas or frameworks from others |
| News sources | Time-sensitive references with context |

### External link quality criteria

**Link to:**
- Primary sources over secondary coverage
- Official docs over blog posts about those docs
- Recent content (check publication dates)
- Authoritative domains (established publications, .gov, .edu for research)

**Avoid linking to:**
- Direct competitors (unless explicit comparison post)
- Low-quality or thin content
- Outdated information without noting the date
- Pages with excessive ads or poor UX

### External link attributes

| Link type | rel attribute | Opens in |
|-----------|--------------|----------|
| Trusted source | (none needed) | Same tab or new tab |
| Untrusted/UGC | `rel="nofollow"` | New tab |
| Sponsored/affiliate | `rel="sponsored"` | New tab |

### Competitor linking policy

**Generally avoid** linking to competitors unless:
- It's an explicit comparison post
- They're the canonical source (created the framework, owns the data)
- Not linking would reduce credibility or seem evasive

When linking to competitors:
- Ensure context is fair and factual
- Focus on your differentiation in surrounding copy
- Consider nofollow if purely informational

---

## Link maintenance

### Broken link prevention
- Check all links before publishing
- Set up periodic link audits (quarterly)
- Use relative links for internal content when possible

### Link updates
- When content is redirected, update internal links
- When external sources change, verify or update
- Archive external sources for critical references (Wayback Machine)

---

## Link density guidelines

### Per post recommendations
- Internal links: 2-5 per 1000 words
- External links: 1-3 per 1000 words
- Total links: Don't exceed 100 per page (technical limit)

### Over-linking signals
- Every sentence has a link
- Same destination linked multiple times
- Links interrupt reading flow
- Link text is longer than surrounding content

### Under-linking signals
- No internal links in a 1500+ word post
- Claims without supporting sources
- No "what to read next" guidance

---

## Formatting links

### Inline link style
Links should flow naturally in sentences.

✅ "This approach aligns with [atomic design principles] popularized by Brad Frost."
❌ "This approach aligns with atomic design principles (link: https://atomicdesign.com)."

### Link lists
Use when referencing multiple related resources:

```md
## Further reading
- [Resource 1 title]
- [Resource 2 title]
- [Resource 3 title]
```

### Call-to-action links
Prominent links at section or post end:

```md
→ [Ready to try this? Start your free trial]
```
