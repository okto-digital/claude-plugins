# Substage 3.4 — Industry & Market Context

**Code:** R4
**Slug:** Market
**Output:** `research/R4-Market.json`, `research/R4-Market.md`
**Dependencies:** R3-Competitors
**Reads from:** `D1-Init.json`, `R3-Competitors.json`
**MCP tools:** DataForSEO (optional), web-crawler (required), WebSearch (required)

---

## Purpose

Research the broader industry environment the client operates in. Unlike previous substages focused on the client and direct competitors, this substage zooms out to the industry level. Everything is interpreted through the website lens — what functionality is expected, how customers behave, what trust signals matter, where the market is heading. Gives Concept Creation and Proposal forward-looking context to build a website relevant 2–3 years from now.

This substage has no client or competitor scope — it is purely external market and industry research.

---

## Data Sources

From `D1-Init.json`:
- `project.site_type`, `project.goal` — what the client offers
- `project.languages` — primary + additional languages
- `project.location` — primary + additional markets

From `R3-Competitors.json`:
- `competitors[].profile.industry` — industry context from competitor profiles
- Market signals from competitor positioning and coverage

---

## Methodology

### Step 1: Search phrase construction

Construct search phrases across two layers:

**Local layer** — primary language x primary location x primary search engine. Use local industry terminology:
- `[industry term in local language] + [market/location context]`
- `[industry term in local language] + "trends" + [year]`

**Global layer** — English x google.com regardless of client location. Target trend, innovation and future-facing content:
- `[industry term] + "trends" + [year]`
- `[industry term] + "innovations" + [year]`
- `[industry term] + "website best practices" + [year]`
- `[industry term] + "consumer behaviour" + [year]`
- `[industry term] + "market report" + [year]`

Always include current year in queries to bias toward recent content.

### Step 2: Source identification and fetching

Use WebSearch for 3–5 searches per layer (local and global). From results identify the 5–10 most authoritative sources — industry reports, trade publications, reputable news sources.

Dispatch `web-crawler` sub-agent to fetch content from selected URLs and extract relevant signals. Quality over quantity.

### Step 3: DataForSEO signals

If DataForSEO MCP tools are available:

Call `kw_data_google_trends_explore` on 3–5 core industry terms to assess macro momentum. Use primary language x location for local trends and English x global for international signals.

### Step 4: Research synthesis

Organise findings across six dimensions, always filtered through the website lens:

**Current market state**
- Market maturity in primary location (established, growing, emerging)
- Key market dynamics and structure
- Regulatory or compliance requirements affecting website functionality
- Seasonal patterns affecting content and promotional planning

**Customer behaviour**
- How customers find and research products/services in this industry
- Buying journey stages and what content is needed at each
- Common questions and objections before converting
- Content formats that resonate (video, guides, specs, reviews)
- Device and channel preferences (mobile vs desktop split)

**Website functionality expectations**
- Features considered standard or expected in this industry
- Trust signals customers look for (certifications, guarantees, review platforms)
- Navigation and IA patterns common in this industry
- Conversion patterns — what drives action

**Payment and transaction patterns** (primarily for ecommerce)
- Local payment method expectations
- Emerging payment behaviours (BNPL, subscriptions)

**Current trends**
- What is changing in how this industry operates digitally
- Shifts in customer expectations or behaviour

**Innovations and future trends**
- Where the industry is heading globally
- Technologies or approaches gaining adoption
- What global markets do that the local market hasn't adopted yet

**Gap analysis (max 5 opportunities)**
Cross-cutting insights that combine findings from multiple dimensions above into concrete website decisions. Each opportunity must reference at least two dimensions. Do not restate individual dimension findings — synthesise across them. Also note what global markets do that the local market hasn't adopted yet (`local_vs_global_gap`).

---

## Output

Write output using the templates at `templates/R4-Market-template.md`.

---

## What passes to the next substage

`research/R4-Market.json` — substage R7-Audience reads `customer_behaviour` and `website_expectations` as primary inputs for persona construction. Concept Creation reads `gap_analysis.opportunities` and `trends` directly.
