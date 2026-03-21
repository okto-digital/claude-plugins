# Substage 3.4 — Industry & Market Context

**Code:** R4
**Slug:** Market
**Output:** `research/R4-Market.txt`
**Hypothesis:** Industry trends create opportunities or constraints for the website approach
**Dependencies:** R3-Competitors
**Reads from:** `project.json`, `baseline-log.txt`, `research/R1-SERP.txt`, `research/R2-Keywords.txt`, `research/R3-Competitors.txt`
**MCP tools:** DataForSEO (optional), web-crawler (optional), WebSearch (required)

---

## Purpose

Research the broader industry environment the client operates in. Unlike previous substages focused on the client and direct competitors, this substage zooms out to the industry level. Everything is interpreted through the website lens — what functionality is expected, how customers behave, what trust signals matter, where the market is heading.

**This substage has no client or competitor scope — it is purely external market and industry research. It gives Concept Creation and Proposal forward-looking context to build a website that remains relevant 2-3 years from now.**

## Upstream Carry-Forward

R1 provides keyword landscape signals (search demand patterns, SERP feature trends). R2 provides cluster intent distribution and page type recommendations. R3 provides competitive zones (service × market groupings), competitor positioning, and market signals from competitor profiles. Read all three before starting — they frame which markets and industries to research.

## Minimum Scope

Cover at least these areas. You may go beyond them if evidence warrants it. Every finding must connect to a concrete website decision — a page that should exist, a feature that's expected, a trust signal that's required, a content format that works, or a constraint that limits options. If a finding doesn't change what we propose or build, drop it.

- Market state and maturity — industry stage (growing/mature/consolidating/disrupted), local vs global digital adoption comparison. Shapes expectations for website polish and feature completeness
- Customer behaviour and buying journey — how customers research and decide, comparison patterns, reliance on reviews vs referrals vs direct search, decision cycle length. Directly shapes page types, content depth, and conversion flows. Flag explicitly as primary input for R7-Audience persona construction
- Website functionality expectations — what customers expect from websites in this industry: booking systems, configurators, live chat, calculators, portals, e-commerce. What's table stakes vs differentiating. Note the local-vs-global gap — features standard globally but not yet adopted locally
- Trust signals and credibility markers — what makes a business trustworthy online in this industry: certifications, memberships, awards, client logos, case studies, team credentials, security badges, regulatory markers. Ranked by importance
- Regulatory and compliance requirements — hard constraints that override design preferences: GDPR/privacy, cookie consent, accessibility (EAA/WCAG), industry-specific regulations (financial disclosure, healthcare restrictions, licensing display), e-commerce regulations (consumer rights, returns, PCI DSS), local legal requirements (imprint page, business registration, terms)
- Trends and forward direction — classified by horizon: Established (adopted by global leaders and some local competitors — must include), Emerging (adopted by innovators, not mainstream locally — recommend for differentiation), Speculative (early signals only — mention as future-proofing, don't build proposal around it)
- Market comparison (multi-market projects only) — where markets align (supports unified approach) vs where they diverge (argues for localisation beyond translation)

## Data Sources

From `project.json`: site type, goal, languages, locations.
From `baseline-log.txt`: mission, services/products, all prior findings including R1-R3 highlights.
From `research/R1-SERP.txt`: keyword landscape signals, search demand patterns.
From `research/R2-Keywords.txt`: cluster intent distribution, page type recommendations.
From `research/R3-Competitors.txt`: competitive zones (define which markets to research), competitor positioning, market signals from profiles.

---

## Methodology — Processing Sequence

Four steps. Step 1 scopes the research from R3's zones. Steps 2-3 gather data. Step 4 synthesises through the website lens.

**Step 1 — Define research scope from zones:** R3's competitive zones define which markets to research. Each unique market (location + language) in the zone map gets its own research thread. If there's an English/international dimension, add a global trends thread. For each thread, construct research queries in the appropriate language targeting the appropriate search engine and local sources.

**Step 2 — Search and source identification:** Construct search phrases across two layers per market thread:

- *Local layer* — local language × location × search engine. Use local industry terminology: industry term + market context, + "trends" + year, + regulations/legislation terms, + customer behaviour terms.
- *Global layer* — English × google.com. Target trend and innovation content: industry term + "trends" / "website best practices" / "consumer behaviour" / "digital transformation" / "market report" + current year.

Always include current year to bias toward recent content. Use WebSearch across both layers. Prioritise: industry body publications, market research firms (Statista, IBISWorld, local equivalents), trade press, government statistics, EU regulatory bodies, reputable business media. Avoid: generic SEO blogs, listicles, content farms, undated sources. Dispatch web-crawler for high-value sources that need full-page extraction. Quality over quantity — 5 authoritative sources per market thread beats 20 shallow ones.

**Step 3 — DataForSEO trend signals (if available):** Run trend exploration on core industry terms to assess macro momentum — search interest trajectory, seasonal patterns, emerging terms not present 12 months ago. Use primary language × location for local trends and English × global for international signals. Complements qualitative research from Step 2 with quantitative demand data.

**Step 4 — Research synthesis:** Synthesise findings across the six areas defined in Minimum Scope, filtering everything through the website lens. Each area produces concrete website implications, not generic industry observations.

For multi-market projects: produce a comparison highlighting where markets align (shared trends, similar expectations, common regulations → unified approach) and where they diverge (different maturity, different regulations, different behaviours → localisation beyond translation). This feeds Concept Creation's decision about single multi-language site vs market-specific sites vs hybrid.

---

## Tooling

**WebSearch — primary tool:**
- Industry research across local and global layers. Multiple queries per market thread across all six synthesis areas.

**DataForSEO — trend signals (optional):**
- Trend exploration on core industry terms. Quantitative demand trajectory and seasonality data.

**Web-crawler — source extraction (optional):**
- Full-page extraction from high-value industry reports and trade publications identified in Step 2.

---

## Output

Write `research/R4-Market.txt`. Apply the decision framework and formatting rules. Append key findings to `baseline-log.txt` tagged with `[R4]`.

**What R4 feeds downstream:**
- Customer behaviour and buying journey → R7-Audience (primary input for persona construction)
- Website functionality expectations → Concept Creation functional requirements (C2)
- Trust signals → Concept Creation (which trust elements pages must include)
- Regulatory checklist → Concept Creation compliance requirements (C9), Proposal (non-negotiable deliverables)
- Trend map → Concept Creation (future-proofing), Proposal (innovation narrative)
- Local-vs-global gap → Proposal (strongest differentiation arguments — "standard globally, not adopted locally")
- Market comparison → Concept Creation (site architecture decision: single vs multi-market)
