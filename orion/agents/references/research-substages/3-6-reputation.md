# Substage 3.6 — Reputation & Social Proof

**Code:** R6
**Slug:** Reputation
**Output:** `research/R6-Reputation.json`, `research/R6-Reputation.md`
**Dependencies:** R3-Competitors
**Reads from:** `D1-Init.json`, `D2-Client-Intelligence.json`, `R3-Competitors.json`
**MCP tools:** none required; web-crawler (required), WebSearch (required)

---

## Purpose

Audit the public trust landscape for the client and competitors rank 1–3. Covers review platforms, social media presence and communication style, and website trust signals (case studies and testimonials). Focus on signal quality over data volume — bounded samples that reveal patterns.

Review samples are direct input for messaging in Concept Creation and Proposal — what customers praise and complain about is valuable positioning intelligence.

**Important:** Social media analysis is limited to publicly visible data. Detailed audience demographics, reach data, and ad spend require paid platform tools not available in this pipeline.

---

## Data Sources

From `D1-Init.json`:
- `notes` — reference site URLs

From `D2-Client-Intelligence.json`:
- `website.url` — client domain
- `social.platforms` — known social profiles
- `reputation` — existing reputation signals

From `R3-Competitors.json`:
- `competitors` ranks 1–3 URLs and domains (all locked competitors when `deep`)
- `competitors[].social` and `competitors[].reputation` — surface-level baseline. Use as starting point to deepen, not re-discover.

---

## Scope

| Site | Reviews | Social | Website Trust Signals |
|---|---|---|---|
| Client | Full | Full (max 5 posts/platform) | Case studies + testimonials |
| Competitors rank 1–3 | Full | Full (max 5 posts/platform) | Case studies + testimonials |
| Reference sites | None | None | Case studies + testimonials only |

When `research_depth` = `deep`: expand to all locked competitors from R3, not just ranks 1–3.

---

## Methodology

### Step 1: Review audit

For each site, use WebSearch to find review profiles and dispatch `web-crawler` to extract:
- **Google Business profile** — overall rating, total review count
- **Other platforms** — Trustpilot, industry-specific platforms, app stores if applicable

Per platform capture:
- Overall rating and total count
- Review intensity — how frequently new reviews appear (active, moderate, sparse)
- 3–4 sample positive reviews — what customers praise
- 3–4 sample medium reviews — what customers find mixed
- 3–4 sample negative reviews — what customers complain about
- Response behaviour — does the business respond, how quickly, what tone

### Step 2: Social presence audit

For each active social platform, dispatch `web-crawler` or use WebSearch to record:
- Platform name, URL, follower count, verification status
- Posting frequency — active (weekly+), moderate (monthly), dormant (no recent posts)
- Up to 5 recent posts sampled per active platform
- Content type observed — video, image, carousel, text, story
- Tone of voice and communication style from sampled posts
- Engagement quality signal — average likes/comments relative to follower count

### Step 3: Website trust signals

For each site, dispatch `web-crawler` to check:
- **Case studies** — present/absent, count, structure (industry-challenge-result format vs simple text)
- **Testimonials** — present/absent, count, placement, format (text, video, star rating, named vs anonymous)
- **Other signals** — awards, certifications, partner logos, media mentions displayed on site

### Step 4: Gap analysis

Compare client against analysed competitors. Each gap is one line: what's missing + why it matters. Do not restate per-site findings — synthesise across sites. Covers reviews, social, communication style, and trust signals together in flat `gaps` + `opportunities` lists. Max 5 opportunities.

---

## Output

Write output using the templates at `${CLAUDE_PLUGIN_ROOT}/agents/references/research-substages/templates/R6-Reputation-template.md`.

---

## What passes to the next substage

`research/R6-Reputation.json` — Proposal reads `reviews.samples` for messaging intelligence (what customers praise and complain about). Concept Creation reads `gap_analysis.gaps` and `website_trust_signals` for page structure and trust element recommendations. R9-Content uses `social` tone of voice signals if available.
