# Substage 3.2 — SERP Research

**Code:** R2
**Slug:** SERP
**Output:** `research/R2-SERP.txt`
**Hypothesis:** Client is invisible in local search for core services
**Dependencies:** none (first substage)
**Reads from:** `project.json`, `baseline-log.txt`
**MCP tools:** DataForSEO (required)

---

## Purpose

Establish the SERP landscape for the client's services. SERP results are a real-time snapshot of what Google considers the most relevant answers — reading them correctly tells you what type of content Google rewards, how competitive the space is, and what the user's intent is. Every SERP is Google's current best answer to what the user wants — and that tells us what the website needs to be.

**Breadth research (landscape mapping), not depth research (keyword targeting). Map the battlefield — do not plan the attack.**

## Minimum Scope

Cover at least these signals. You may go beyond them if evidence warrants it.

- Result types present — organic, local pack, featured snippets, knowledge panels, shopping, image/video carousels, PAA boxes. The mix signals query intent and SERP complexity
- Who is ranking — domains in positions 1-10, classified as commercial, directory, media, marketplace, or informational
- Domain authority distribution — high-authority domains vs smaller niche sites. Mixed SERPs with smaller sites signal opportunity
- Client position — current ranking per keyword (position 1-10 or null). Redesign baseline or new-build zero-presence confirmation
- SERP volatility — same domains across related queries (settled, competitive) vs shifting results (contested, opportunity)
- Local vs global signals — local pack presence, local TLDs vs global results. Determines local SEO vs authority-building strategy
- Ad presence — paid ad count above organic. Heavy ads = organic pos 1 is visual pos 4-5, affects traffic estimate calibration
- People Also Ask — adjacent questions and topics. Seeds keyword expansion and FAQ content signals
- AI Overview presence — flag queries where AI Overviews appear. Reduced click-through, reduced traffic potential
- Intent classification — navigational, informational, commercial, transactional per keyword
- Seed keywords — consolidated list per keyword: keyword, volume, intent, client position, source layer
- Competitor domains — consolidated list per domain: domain, type (commercial/directory/media/marketplace/informational), appearances, local appearances, scope

## Data Sources

From `project.json`: site type, goal, languages, location, research config (serp_max_keywords, research_depth), notes.
From `baseline-log.txt`: mission, client profile, services/products, client URL, any prior findings.

---

## Language x Location x Search Engine Rules

**What drives results is location + language — not the domain.** Google personalises by detected location regardless of domain. google.com and google.sk return the same results for the same location. In DataForSEO, set `location`, `language`, and `search_engine` explicitly per query.

**Matrix rules:**
- Primary location + primary language + primary engine → always
- Primary location + English + primary engine → if English is used in that market (B2B, expats, tourism)
- Global + English + google.com → always (global demand check — only case where google.com adds distinct results)
- Secondary language + own location + own engine → per secondary market (Czech → CZ + google.cz, Hungarian → HU + google.hu)
- Cross-border market + own language + own engine → per stated market

Never mix languages and locations across wrong engines. A Slovak query never runs on google.com. A Czech query never runs on google.sk.

---

## Methodology — Operational Layers

Four layers from narrowest to widest. Each layer only expands if the previous is complete.

**Layer 1 — Brand & Current Rankings:** Client brand name, brand + service, brand + city. Redesign clients: also check current keyword rankings and organic traffic for the domain. New builds: null results confirm zero presence. Flag shady/off-brand keywords separately — do NOT merge into seed list.

**Layer 2 — Commercial Service/Product Keywords:** For each service/product from baseline-log.txt: bare term, + city, + country, + transactional modifiers (buy/order/price/near me). Generate natural phrasing variants per language — do not literally translate. Cap: max 5 queries per service/product category. Respect `research_config.serp_max_keywords` as total cap. Relevance guardrail: only keywords for services the client actually delivers — drop off-topic before applying caps.

**Layer 3 — Geographic Expansion:** Only if client operates in multiple cities/regions/markets. City: top 3 commercial queries per city, cap 3 cities. Region: use region name modifier. Country: primary always, secondary only if stated in INIT. Cross-border: own language x location x engine pair. Never expand beyond the client's stated operational footprint.

**Layer 4 — Language Overlay:** Applied to all previous layers. Every query runs in the correct language on the correct engine per the matrix rules above.

---

## Competitor Extraction

From all SERP results across all layers:
- Count domain appearances across all queries
- Classify each domain: `commercial`, `directory`, `media`, `marketplace`, `informational`
- Only `commercial` domains carry forward as competitors
- Directories and marketplaces noted separately as channel opportunities
- Flag separately: city-level competitors, national competitors, cross-border competitors
- A domain with 3 local appearances is more relevant than one with 10 national appearances — the client competes with local businesses first
- Cap: top 10 commercial domains total. Top 5 by frequency become the competitor shortlist for R4-Competitors

---

## Tooling

**DataForSEO — primary tool:**
- SERP analysis per keyword — core endpoint. Returns full SERP including result types, positions, domains, URLs, titles, descriptions. Run per query across all layers with correct location + language + engine parameters.
- Intent classification — classifies query intent. Run on the full keyword list after all SERP queries are complete.
- Volume estimation — first pass volume estimate on seed keywords before full expansion in R3-Keywords.
- Current rankings (redesign only) — what the client domain currently ranks for.
- Current traffic (redesign only) — estimated organic traffic for the client domain.

**Web search — spot-check and validation:**
Manual spot-checks on 3-5 highest-priority queries to visually confirm result types, ad density, local pack presence, People Also Ask boxes, and AI Overview presence. Some SERP features are not fully captured by API — visual confirmation adds signal quality.

---

## Output

Write `research/R2-SERP.txt`. Apply the decision framework and formatting rules. Append key findings to `baseline-log.txt` tagged with `[R2]`.

**What R2 feeds downstream:**
- Seed keyword list → R3-Keywords
- Competitor domain list → R4-Competitors
- Result type patterns → R10-Content (what content formats Google rewards)
- Ad density → Concept Creation sitemap (traffic estimate calibration)
- People Also Ask → R3-Keywords (expansion seeds) and R10-Content (FAQ signals)
- Intent classification → Concept Creation (page type mapping across sitemap)
- AI Overview presence → R10-Content (reduced-traffic-potential flags)
