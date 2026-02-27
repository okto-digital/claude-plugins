# R-Document Template

Shared template for all research topic documents (R1-R8). Each topic agent produces one document following this structure.

---

## Frontmatter

```yaml
---
document_type: research-topic
document_id: R[N]
topic: "[topic name]"
title: "R[N] [Topic Name] -- [Company Name]"
project: "[client name from registry, or 'standalone']"
sources_consulted: [number]
confidence: [high/medium/low]
created: [YYYY-MM-DD]
created_by: webtools-research
status: complete
---
```

**Field definitions:**

- `document_id`: R1 through R8, matching the topic ID
- `topic`: One of: SERP & Search Landscape, Competitor Landscape, Audience & User Personas, UX/UI Patterns & Benchmarks, Content Landscape & Strategy, Reputation & Social Proof, Technology & Performance, Industry & Market Context
- `sources_consulted`: Total number of distinct sources (URLs, documents, searches) consulted
- `confidence`: Overall confidence in findings -- high (3+ sources per key finding), medium (2 sources), low (single source or inference)

---

## Body Structure

### 1. Key Findings

3-5 bullet points summarizing the most important takeaways. These are what get pulled into D15.

Each finding should be:
- Specific (include numbers, names, evidence)
- Actionable (implication for the proposal is clear)
- Sourced (reference the source number in brackets, e.g., [3])

Example:
```markdown
- The top 3 ranking competitors for "[core service] [location]" are [A], [B], and [C]. All use long-form service pages (2000+ words) with integrated case studies. [1][3][5]
- No competitor in the local market offers a pricing calculator or interactive tool -- this is a differentiation opportunity. [2][4][7]
```

### 2. Detailed Findings

Organized by sub-topic as defined in the topic specification. Each sub-section should include:
- What was found
- Evidence (quotes, data points, observations)
- Source references in brackets

Use sub-headings (###) for each sub-topic area.

### 3. Opportunities & Risks

What this research suggests for the proposal. Split into:

**Opportunities:**
- Gaps found in competitors, market, or audience needs
- Advantages the client could leverage
- Quick wins visible from the research

**Risks:**
- Challenges the proposal should address upfront
- Competitive threats
- Market or audience factors working against the client

### 4. Confidence Notes

Transparency about research limitations:
- What could not be verified (and why)
- Findings based on single sources (flagged as lower confidence)
- Areas that need deeper investigation (candidates for D3/D5/D6 deep-dives)
- Data freshness concerns (oldest source dates)

### 5. Sources

Numbered list of all sources consulted. Each entry:
```markdown
1. [URL or search query] -- [brief description of what was found] ([date accessed or "search result"])
2. [URL] -- [description] ([date])
```

For WebSearch queries, format as:
```markdown
3. WebSearch: "[query]" -- [what the results revealed] ([date])
```
