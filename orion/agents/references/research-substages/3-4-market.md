# Substage 3.4 — Industry & Market Context

**Code:** R4
**Slug:** Market
**Output:** `research/R4-Market.txt`
**Hypothesis:** Industry trends create opportunities or constraints for the website approach
**Dependencies:** R3-Competitors
**Reads from:** `project.json`, `baseline-log.txt`, `research/R3-Competitors.txt`
**MCP tools:** DataForSEO (optional), web-crawler (required), WebSearch (required)

---

## Purpose

Research the broader industry environment the client operates in. Unlike previous substages focused on the client and direct competitors, this substage zooms out to the industry level. Everything is interpreted through the website lens — what functionality is expected, how customers behave, what trust signals matter, where the market is heading. Gives Concept Creation and Proposal forward-looking context to build a website relevant 2–3 years from now.

This substage has no client or competitor scope — it is purely external market and industry research.

---

## Data Sources

From `project.json`: site type, goal, languages, location.
From `baseline-log.txt`: mission, all prior findings including R1–R3 highlights.
From `research/R3-Competitors.txt`: industry context from competitor profiles, market signals from competitor positioning and coverage.

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

Use WebSearch across both layers. Identify the most authoritative sources — industry reports, trade publications, reputable news sources. Dispatch `web-crawler` sub-agent to fetch content from selected URLs. Quality over quantity.

### Step 3: DataForSEO signals

If DataForSEO MCP tools are available:

Call `kw_data_dfs_trends_explore` on core industry terms to assess macro momentum. Use primary language x location for local trends and English x global for international signals.

### Step 4: Research synthesis

Everything is filtered through the website lens — what does this mean for the site we're building?

Areas to explore: market state and maturity, customer behaviour and buying journey, website functionality expectations in this industry, payment and transaction patterns (especially for ecommerce), current digital trends, innovations and where the industry is heading globally. Note the gap between what global markets do and what the local market hasn't adopted yet.

Synthesise findings into concrete website decisions — cross-cutting insights that combine signals from multiple areas. The decision framework applies: if a finding doesn't change what we propose or build, drop it.

---

## Output

Write `research/R4-Market.txt`. Apply the decision framework and formatting rules. Append key findings to `baseline-log.txt` tagged with `[R4]`.

R7-Audience reads customer behaviour and website expectations as primary inputs for persona construction. Concept Creation reads gap analysis opportunities and trends directly.
