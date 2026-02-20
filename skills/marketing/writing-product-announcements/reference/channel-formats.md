# Channel formats

## Channel-specific requirements

| Channel | Max length | Headline style | CTA format | Rich media |
|---------|-----------|----------------|------------|------------|
| Email | 300-500 words | Subject line + header | Button | Yes |
| Blog | 500-1000 words | SEO-friendly H1 | Inline link or button | Yes |
| In-app banner | 50-100 words | Short, direct | Single link | Minimal |
| In-app modal | 100-200 words | Benefit statement | Button(s) | Optional |
| Changelog | 50-150 words | Feature/category label | Inline link | No |
| Social (Twitter/X) | 280 chars | None (integrated) | Link | Image optional |
| Social (LinkedIn) | 700-1300 chars | First line is hook | Link | Image recommended |

## Email announcements

**Subject line patterns**:
- Launch: "Introducing [Feature]: [Benefit]"
- Update: "[Feature] just got [better/faster/easier]"
- Deprecation: "Action required: [Feature] retiring [Date]"
- Breaking: "Action required by [Date]: [Change]"

**Structure**:
```
Subject: [Pattern from above]
Preview text: [First sentence or key benefit]

[Header/Hero: Visual or headline]

[Body: 2-4 paragraphs max]

[CTA Button]

[Footer: Docs link, unsubscribe]
```

**Guidelines**:
- Front-load the key information
- One primary CTA per email
- Use bullet points for feature lists
- Keep paragraphs to 2-3 sentences

## Blog announcements

**Structure**:
```
# [SEO-friendly headline with benefit]

[Intro paragraph: What and why, 2-3 sentences]

## What's new / What you can do
[Details with subheadings if needed]

## How to get started
[Steps or link]

## Learn more
[Links to docs, demos, related posts]
```

**Guidelines**:
- Include meta description for SEO
- Use descriptive subheadings
- Add screenshots or GIFs for visual features
- Link to documentation for technical depth
- Include publish date

## In-app announcements

### Banner format
```
[Icon] [Short message: what + action] [Link or dismiss]
```
- 50-100 characters max for message
- One action only
- Dismissible for non-critical announcements

### Modal format
```
[Optional illustration]

## [Headline: 5-8 words]

[Body: 1-2 short paragraphs]

[Primary CTA button]  [Secondary link: "Learn more" or "Maybe later"]
```

**Guidelines**:
- Reserve modals for significant changes
- Don't interrupt critical workflows
- Provide escape route (dismiss, "not now")
- Test on mobile viewports

## Changelog entries

**Format**:
```
### [Date] — [Category]

**[Feature name]**: [One sentence description.] [Learn more →]
```

**Categories**: New, Improved, Fixed, Deprecated, Security

**Guidelines**:
- Chronological order (newest first)
- Consistent date format (Month Day, Year)
- Link to detailed docs for complex changes
- Group same-day changes by category

## Social media

### Twitter/X
```
[Announcement in ≤200 chars] [Link]

[Optional: relevant hashtag]
```

**Guidelines**:
- Lead with the news, not preamble
- Use thread for complex announcements
- Include image for better engagement

### LinkedIn
```
[Hook line: news or benefit]

[2-3 sentences of context]

[Key details as bullets if needed]

[CTA: link to learn more]
```

**Guidelines**:
- More professional tone than Twitter
- Can include more context
- Tag relevant people or companies if appropriate
- Image or video significantly increases reach

## Cross-channel coordination

For major announcements, sequence channels:
1. **Internal**: Team notification, support enablement
2. **Documentation**: Update docs before announcement
3. **Email**: Primary notification to affected users
4. **Blog**: Detailed public announcement
5. **In-app**: Contextual notification
6. **Social**: Amplification
7. **Changelog**: Permanent record

Ensure consistent:
- Feature naming across all channels
- Dates and timelines
- CTA destinations (all point to same resource)
- Level of detail (social summarizes, blog expands)
