# Substage 3.7 — Audience & Personas

**Code:** R7
**Slug:** Audience
**Output:** `research/R7-Audience.json`, `research/R7-Audience.md`
**Dependencies:** R1-SERP, R2-Keywords, R3-Competitors, R4-Market
**Reads from:** `D1-Init.json`, `D2-Client-Intelligence.json`, `R1-SERP.json`, `R2-Keywords.json`, `R3-Competitors.json`, `R4-Market.json`
**MCP tools:** none (synthesis only — no new data collection)

---

## Purpose

The only fully synthesised substage in the research phase — performs no new scraping or API calls. Distils everything gathered across R1–R4 into structured human profiles. Every layout decision, content choice, and feature recommendation in later phases should be traceable back to a persona defined here.

Maximum 3 personas total — one per primary audience segment.

---

## Data Sources

From `D1-Init.json`:
- `project.goal`, `project.site_type` — what the client offers and wants to achieve
- `notes` — audience signals from operator

From `D2-Client-Intelligence.json`:
- `profile` — client markets, industry, description
- Audience context from client digital footprint

From `R1-SERP.json`:
- `keywords` — intent patterns, search behaviour signals

From `R2-Keywords.json`:
- `keywords` — keyword gap and audience segment signals
- `page_groups` — how search demand clusters around page types

From `R3-Competitors.json`:
- `competitors` — competitor audience targeting signals, positioning, messaging

From `R4-Market.json`:
- `customer_behaviour` — discovery patterns, buying journey, content preferences, device preferences
- `website_expectations` — standard functionality, trust signals, conversion patterns
- `payment_patterns` — payment method expectations
- `website_implications` — market-to-website connections

---

## Methodology

### Step 1: Audience segment definition

Before building personas, define distinct audience segments based on all available research. Each segment gets:
- Segment name and description
- Size and importance signal (primary, secondary, tertiary)
- How they were identified (INIT notes, competitor targeting, search intent, market research)

Personas are built from segments — not the other way around.

### Step 2: Persona construction

For each segment (max 3) construct a full persona profile:
- **Demographics:** name, age, location, occupation, income level, lifestyle
- **Psychographics:** personality type, values, beliefs, lifestyle preferences
- **Buying motivation:** what problem they solve, emotional triggers, objections
- **Digital behaviour:** where they search, preferred content types, device and channel preferences
- **Trust threshold:** how much convincing before converting (high, medium, low)
- **Decision process:** research-heavy vs impulsive, influences they trust
- **Marketing messaging:** 1–2 positioning statements that resonate with this persona
- **Keyword mapping:** which keywords from R2-Keywords this persona uses at each funnel stage
- **Primary flag:** one persona is flagged as the primary design target

### Step 3: Psychographics and buying motivation table

For each persona build a structured evidence table connecting research findings to persona characteristics:

| Psychographic Factor | Source | Key Findings | Patterns Identified | Strategic Implications |
|---|---|---|---|---|

Factors: lifestyle preferences, values and beliefs, emotional triggers, buying behaviour, brand perception and loyalty.

### Step 4: Industry benchmarks per persona

Map relevant industry benchmarks from R4-Market to each persona segment:
- Expected conversion rate for this audience type
- Average CAC signals
- Retention likelihood
- Most effective acquisition channel for this segment

These give Concept Creation concrete performance targets.

### Step 5: User journey map per persona

Map the five-stage journey — awareness, consideration, decision, retention, advocacy:

| Stage | User Mindset | Where They Go | Pain Points | Content Needed | Website Implication |
|---|---|---|---|---|---|

`Website Implication` per stage is the most important column — translates persona behaviour directly into website page and content requirements.

---

## Output

Write output using the templates at `templates/R7-Audience-template.md`.

---

## What passes to the next substage

`research/R7-Audience.json` — Concept Creation reads `personas`, `journey_map.website_implication` and `keyword_mapping` directly for site structure and content planning. R8-UX and R9-Content use persona device preferences and trust thresholds to contextualise their findings.
