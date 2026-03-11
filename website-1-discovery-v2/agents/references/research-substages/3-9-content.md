# Substage 3.9 — Content Landscape & Strategy

**Code:** R9
**Slug:** Content
**Output:** `research/R9-Content.json`, `research/R9-Content.md`
**Dependencies:** R3-Competitors, R7-Audience (hard); R2-Keywords, R4-Market, R6-Reputation (soft — available from prior waves); R8-UX (optional — may not be available if running in parallel)
**Reads from:** `D1-Init.json`, `D2-Client-Intelligence.json`, `R2-Keywords.json`, `R3-Competitors.json`, `R4-Market.json`, `R7-Audience.json`, `R6-Reputation.json`, `R8-UX.json` (if available)
**MCP tools:** none required; web-crawler (required), WebSearch (required)

---

## Purpose

Final research substage and one of the most direct inputs into Concept Creation. Three parts: brand voice analysis (how everyone communicates), content structure analysis (how pages are built), and a page structure recommendation (suggested site architecture with supporting SEO pages). The page structure output is essentially the first draft of the site map.

Social communication data from R6-Reputation is reused to enrich brand voice analysis — no re-scraping of social needed.

---

## Data Sources

From `D1-Init.json`:
- `project.site_type`, `project.goal` — what the client offers
- `project.languages` — primary + additional languages
- `project.location` — primary + additional markets

From `D2-Client-Intelligence.json`:
- `website.url` — client domain
- `website.tone_of_voice` — existing tone signals

From `R2-Keywords.json`:
- `page_groups` — keyword clusters by page type
- `gap_analysis.keywords_not_targeted` — untargeted keyword opportunities

From `R3-Competitors.json`:
- `competitors` ranks 1–3 for content analysis

From `R4-Market.json`:
- `website_expectations` — functionality and content standards in this industry
- `website_implications` — market-to-website connections

From `R7-Audience.json`:
- `personas` — persona definitions, journey map, keyword mapping
- `personas[].journey_map.content_needed` — content per funnel stage

From `R6-Reputation.json` (soft dependency):
- `sites[].social[].tone_of_voice` — social tone signals
- `sites[].social[].content_types` — content types used

From `R8-UX.json` (optional — may not be available if R8 runs in parallel):
- `gap_analysis.ux_gaps` — UX issues informing content structure
- `sites[].ux.information_architecture` — page structure patterns

---

## Methodology

### Part 1 — Brand Voice & Communication Style

#### Step 1: Tone of voice analysis

For each site, dispatch `web-crawler` to analyse website copy across homepage and key landing pages, enriched with social post tone from R6-Reputation:
- Overall tone — formal, casual, authoritative, friendly, technical, aspirational, premium
- Language complexity — simple and accessible vs jargon-heavy
- Messaging pillars — core themes repeated consistently
- Value proposition clarity — how quickly the main offer is communicated
- Emotional vs rational messaging balance
- CTA language style — aggressive, soft, inviting, urgent, benefit-led
- Localisation quality — how well copy adapts to local language and culture
- Person and voice — first, second, third person

#### Step 2: Communication patterns

- Headline structure — question, statement, benefit, feature
- Trust communication in copy — social proof language, guarantees, authority
- Content length patterns — brief and punchy vs detailed
- Storytelling vs feature listing

### Part 2 — Content Structure Analysis

#### Step 3: Page type analysis

For each key page type, analyse how client and competitors structure content — sections present, order, depth:
- Homepage structure
- Product or service category pages
- Product or service detail pages
- About page
- Contact page
- Blog or content hub (if present)

#### Step 4: Search-informed structure signals

Cross-reference with keyword intent data from R2-Keywords:
- Content blocks top-ranking pages include that lower-ranking miss
- Questions asked at each funnel stage that should be answered per page type
- Schema markup patterns detectable from R5-Technology onpage data (if available)
- FAQ and supporting content patterns correlating with strong SERP performance

#### Step 5: Industry content standards

From R4-Market, identify:
- Content types expected in this industry (guides, specs, certifications, comparison tables)
- Content depth standards — detail level customers expect
- Supporting content patterns that help conversion

### Part 3 — Page Structure Recommendation

#### Step 6: Site architecture suggestion

Produce a nested page structure recommendation. Each page classified by priority:
- `must_have` — core pages required for the site to function and convert
- `should_have` — important pages improving SEO or UX significantly
- `nice_to_have` — supporting pages adding depth and long-tail SEO value

Each page entry includes:
- Page name and type
- Purpose and which persona it primarily serves
- Target keywords from R2-Keywords mapping
- Suggested content sections in order
- SEO rationale for supporting pages

---

## Output

Write output using the templates at `templates/R9-Content-template.md`.

---

## What passes to the next phase

`research/R9-Content.json` — this is the final research substage output. Concept Creation reads `page_structure_recommendation` as the primary site architecture input, `brand_voice` findings for messaging direction, and `gap_analysis.opportunities` for content strategy recommendations.

**The Research phase is now complete. All 9 substages have been run and reviewed.**
