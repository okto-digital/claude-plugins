# Substage 3.9 — Content Landscape & Strategy

**Code:** R9
**Slug:** Content
**Output:** `research/R9-Content.txt`
**Dependencies:** R3-Competitors, R7-Audience (hard); R2-Keywords, R4-Market, R6-Reputation (soft — available from prior waves); R8-UX (optional — may not be available if running in parallel)
**Reads from:** `project.json`, `baseline-log.txt`, `research/R2-Keywords.txt`, `research/R3-Competitors.txt`, `research/R4-Market.txt`, `research/R7-Audience.txt`, `research/R6-Reputation.txt`, `research/R8-UX.txt` (if available)
**MCP tools:** none required; web-crawler (required), WebSearch (required)

---

## Purpose

Final research substage. Two parts: brand voice analysis (how everyone communicates) and content structure analysis (how pages are built). Social tone data from R6-Reputation is reused — no re-scraping needed.

Site architecture is NOT produced here — that is C1-Sitemap's job using R2 keyword clusters and these findings as input.

---

## Data Sources

From `project.json`: site type, goal, languages, location.
From `baseline-log.txt`: mission, client URL, existing tone signals, services/products list, all prior findings including D2, R2–R4, R6–R8 highlights.
From `research/R2-Keywords.txt`: semantic keyword clusters with page type mapping and volume data, untargeted keyword opportunities.
From `research/R3-Competitors.txt`: competitor ranks 1–3 for content analysis, surface-level tone from R3 (brand voice analysis here goes deeper; use R3 as baseline).
From `research/R4-Market.txt`: website expectations and content standards, market-to-website gap opportunities.
From `research/R7-Audience.txt`: persona definitions, journey map, keyword mapping, content needed per funnel stage.
From `research/R6-Reputation.txt` (soft dependency): social tone signals, content types used.
From `research/R8-UX.txt` (optional — may not be available if R8 runs in parallel): UX/UI gap analysis, page structure patterns.

---

## Methodology

### Part 1 — Brand Voice & Communication Style

#### Step 1: Tone of voice and communication style

For each site, dispatch `web-crawler` to analyse website copy across homepage and key landing pages, enriched with social post tone from R6-Reputation.

Areas to explore: overall tone and formality, language complexity, messaging pillars, value proposition clarity, emotional vs rational balance, CTA language style, localisation quality, person and voice. Also look at communication patterns — headline structure, trust communication, content length, storytelling vs feature listing.

### Part 2 — Content Structure Analysis

#### Step 2: Content structure analysis

Analyse how client and competitors structure content across key page types (homepage, service/product pages, about, contact, blog, etc.) — what sections are present, in what order, at what depth.

Cross-reference with R2-Keywords intent data: what content blocks do top-ranking pages include that lower-ranking ones miss? What questions at each funnel stage should be answered per page type?

From R4-Market, identify industry content standards — content types customers expect, depth standards, and supporting content patterns that help conversion.

---

## Output

Write `research/R9-Content.txt`. Apply the decision framework. Append key findings to `baseline-log.txt` tagged with `[R9]`.

Final research output. Concept Creation reads brand voice findings for messaging direction and gap analysis for content strategy inputs. C1-Sitemap combines this with R2 keyword clusters for site architecture.

**The Research phase is now complete. All 9 substages have been run and reviewed.**
