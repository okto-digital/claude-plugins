# Substage 3.6 — Reputation & Social Proof

**Code:** R6
**Slug:** Reputation
**Output:** `research/R6-Reputation.txt`
**Hypothesis:** Client lacks trust signals that competitors have established
**Dependencies:** R3-Competitors
**Reads from:** `project.json`, `baseline-log.txt`, `research/R3-Competitors.txt`
**MCP tools:** none required; web-crawler (required), WebSearch (required)

---

## Purpose

Audit the public trust landscape for the client and competitors rank 1–3. Covers review platforms, social media presence and communication style, and website trust signals (case studies and testimonials). Focus on signal quality over data volume — bounded samples that reveal patterns.

Review samples are direct input for messaging in Concept Creation and Proposal — what customers praise and complain about is valuable positioning intelligence.

**Important:** Social media analysis is limited to publicly visible data. Detailed audience demographics, reach data, and ad spend require paid platform tools not available in this pipeline.

---

## Data Sources

From `project.json`: notes (reference site URLs).
From `baseline-log.txt`: mission, client URL, known social profiles, existing reputation signals, all prior findings including D2 and R3 highlights.
From `research/R3-Competitors.txt`: competitor ranks 1–3 URLs and domains (all locked competitors when `deep`), surface-level social and reputation baseline from R3. Use as starting point to deepen, not re-discover.

---

## Scope

| Site | Reviews | Social | Website Trust Signals |
|---|---|---|---|
| Client | Full | Full | Case studies + testimonials |
| Competitors rank 1–3 | Full | Full | Case studies + testimonials |
| Reference sites | None | None | Case studies + testimonials only |

When `research_depth` = `deep`: expand to all locked competitors from R3, not just ranks 1–3.

---

## Methodology

### Step 1: Review audit

For each site, use WebSearch to find review profiles and dispatch `web-crawler` to extract:
- **Google Business profile** — overall rating, total review count
- **Other platforms** — Trustpilot, industry-specific platforms, app stores if applicable

Per platform capture: overall rating and count, review intensity (how frequently new reviews appear), sample reviews across positive/mixed/negative to surface patterns in what customers praise and complain about, and response behaviour (does the business respond, how quickly, what tone).

### Step 2: Social presence audit

For each active social platform, dispatch `web-crawler` or use WebSearch. Capture: platform presence and follower count, posting frequency, content types used, tone of voice and communication style from sampled posts, and engagement quality relative to follower count.

### Step 3: Website trust signals

For each site, dispatch `web-crawler` to check:
- **Case studies** — present/absent, count, structure (industry-challenge-result format vs simple text)
- **Testimonials** — present/absent, count, placement, format (text, video, star rating, named vs anonymous)
- **Other signals** — awards, certifications, partner logos, media mentions displayed on site

### Step 4: Gap analysis

Compare client against analysed competitors. Synthesise across sites — don't restate per-site findings. Cover reviews, social, communication style, and trust signals together.

---

## Output

Write `research/R6-Reputation.txt`. Apply the decision framework and formatting rules. Append key findings to `baseline-log.txt` tagged with `[R6]`.

Proposal reads review samples for messaging intelligence. Concept Creation reads gap analysis and website trust signals for page structure and trust element recommendations. R9-Content uses social tone of voice signals if available.
