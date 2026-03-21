# Substage 3.9 — Content Landscape & Strategy

**Code:** R9
**Slug:** Content
**Output:** `research/R9-Content.txt`
**Hypothesis:** Content exists but is unstructured and not aligned with keyword opportunities
**Dependencies:** R3-Competitors, R4-Market, R5-Audience, R6-Reputation, R7-Technology, R8-UX
**Reads from:** `project.json`, `baseline-log.txt`, `research/R2-Keywords.txt`, `research/R3-Competitors.txt`, `research/R4-Market.txt`, `research/R5-Audience.txt`, `research/R6-Reputation.txt`, `research/R7-Technology.txt`, `research/R8-UX.txt`
**MCP tools:** none required; web-crawler (required)

---

## Purpose

Final research substage. Two parts: **brand voice analysis** (how everyone communicates — tone, language, messaging) and **content structure analysis** (how pages are built — what sections exist, in what order, at what depth, and how well they serve the audience).

This stage is the most context-rich in the pipeline — it synthesises signals from every prior substage. Social tone data from R6 is reused — no re-scraping of social media needed.

**Critical boundary:** Site architecture is NOT produced here. That is Concept Creation's job, using R2's keyword clusters and this stage's findings as inputs. This stage analyses what content exists and how it's structured — it does not propose what content should be created.

**For new builds (site_type = "new"):** No client content to analyse. The stage becomes a pure competitor benchmark plus voice direction recommendation based on persona needs, market context, and competitive positioning.

## Upstream Carry-Forward

R2 provides keyword clusters with page type mappings and opportunity classifications. R3 provides the competitor roster with top performing pages per competitor. R4 provides content standards for the industry and local-vs-global gap. R5 provides persona journey maps with website implications and messaging angles. R6 provides social tone signals, customer language from reviews, and messaging intelligence. R7 provides on-page SEO signals (meta tags, headings, structured data). R8 provides page structure patterns and content hierarchy observations. Read all before starting.

## Minimum Scope

Cover at least these areas. You may go beyond them if evidence warrants it.

- Voice inventory per site — tone/register (formal↔informal, expert↔approachable, corporate↔personal), language characteristics (complexity, jargon, sentence length, active/passive, person), messaging approach (value proposition clarity, benefit-led vs feature-led, emotional vs rational, storytelling vs listing), CTA language (verbs, urgency, commitment level), localisation quality (multi-language sites)
- Voice pattern analysis — industry voice convention, client position relative to convention, differentiation opportunities, recommended voice direction for Concept Creation (tone, register, person, messaging approach, CTA progression across journey stages)
- Page type inventory — which page types each site has (homepage, service, about, contact, case studies, blog, FAQ, pricing, landing pages, legal), with content blocks, sequence, and depth per page type
- Content quality assessment — E-E-A-T signals (author attribution, first-hand experience, evidence-backed claims, methodology detail), freshness (last updated, recent publications), differentiation (what stands out, where content is commoditised), multimedia usage (video, diagrams, infographics, interactive elements)
- Cluster-to-content map — for each R2 opportunity cluster: which competitor has a page targeting it, what page type, how structured, how deep. Shows exactly where new pages are needed, where existing pages need improvement, where no competitor has staked a claim
- Gap classification — Missing (persona journey requires it, client has nothing), Thin (exists but shallow/outdated), Misaligned (exists but wrong intent/persona), Competitive (adequate but competitors do better), Whitespace (no competitor covers it — content leadership opportunity)

## Analysis Scope

| Site | Brand voice | Content structure | Content quality |
|---|---|---|---|
| Client | Full | Full (all key page types) | Full |
| Direct-threat competitors | Full | Full (all key page types) | Full |
| Aspirational benchmarks (top 1-2) | Tone summary only | Full (key pages only) | Quality indicators only |
| Remaining roster competitors | Skip | Skip | Skip |
| Reference sites from INIT notes | Skip | Structure of notable pages only | Skip |

Deep content analysis (reading copy, evaluating structure, assessing quality) is the most time-intensive analysis in the pipeline. Limit full analysis to client + direct threats. Aspirational benchmarks set a quality ceiling. Remaining roster already covered structurally in R8.

## Data Sources

From `project.json`: site type, goal, languages, locations.
From `baseline-log.txt`: mission, client URL, services, all prior findings.
From `research/R2-Keywords.txt`: keyword clusters with page type mappings, intent distribution, opportunity classifications.
From `research/R3-Competitors.txt`: full competitor roster, zone map, tier classifications, top performing pages per competitor.
From `research/R4-Market.txt`: website functionality expectations, content standards, local-vs-global gap, trend implications.
From `research/R5-Audience.txt`: persona definitions, journey maps with website implications, messaging angles, content format preferences.
From `research/R6-Reputation.txt`: social tone signals, customer language from reviews, messaging intelligence.
From `research/R7-Technology.txt`: structured data presence/absence, on-page SEO signals (meta tags, headings).
From `research/R8-UX.txt`: page structure patterns, content hierarchy, conversion flow findings.

---

## Methodology — Processing Sequence

Six steps across two parts. Steps 1-2 analyse brand voice. Steps 3-5 analyse content structure and quality. Step 6 synthesises gaps.

### Part 1 — Brand Voice & Communication Style

**Step 1 — Voice inventory:** For each site in voice scope, dispatch web-crawler for homepage and key service/product pages. Enrich with social tone signals from R6 — no re-scraping needed.

Analyse across dimensions: Tone and register (formal↔informal, expert↔approachable, corporate↔personal). Language characteristics (complexity level, jargon usage and handling, sentence/paragraph length, active vs passive, person — first/second/third, consistent or mixed). Messaging approach (value proposition clarity — understand what they do within 5 seconds, benefit-led vs feature-led headlines, emotional vs rational balance, storytelling vs listing). CTA language (verbs used, urgency signals, commitment level — "Buy now" vs "Learn more" vs "Get a free quote"). Localisation quality for multi-language sites (natively written or translated, tone consistency across languages, adapted messaging or just translated words).

Cross-reference with R5: does the voice match what the primary persona expects (messaging angle per persona)? Does CTA language match persona commitment level at each journey stage? Cross-reference with R6: does website voice match social media tone? Does the website address concerns from real customer reviews?

**Step 2 — Voice pattern analysis:** Synthesise across all analysed sites. Industry voice convention: is there a dominant tone (corporate for finance, warm for services, technical for B2B)? Where does the client sit? Voice differentiation: if all competitors sound the same, adopting a different voice is a lever. If one stands out with distinctive voice and performs well, the audience responds to personality.

Produce recommended voice direction for Concept Creation: tone, register, person, messaging approach, CTA progression across journey stages. Not a full brand voice guide — a directional recommendation with enough specificity to brief content creation. E.g.: "Approachable expert tone, second person, benefit-led headlines, short paragraphs, low-commitment CTAs at awareness graduating to direct CTAs at decision stage."

### Part 2 — Content Structure Analysis

**Step 3 — Page type inventory:** For each site in content structure scope, inventory key page types that exist and map against R2's keyword clusters and R5's persona journey maps.

Page types to check: homepage (hero approach, sections, trust signals, CTAs), service/product pages (one per service or grouped, description depth, supporting evidence), about page (story, team, mission emphasis), contact page (form complexity, alternative methods, location info), case studies/portfolio (count, structure, specificity — named clients and real results vs anonymous and vague), blog/resources (publishing frequency, topic coverage, depth), FAQ/knowledge base (organisation, depth), pricing page (transparent or "contact us", package structure), landing pages (purpose-built for specific services/campaigns), legal/compliance (privacy, terms, cookie policy, accessibility statement).

Per page type: content blocks and sequence (what sections, what order, what's above the fold, scroll depth), content depth (thin <300w or substantive 1000+w, answers persona questions at relevant journey stage, includes evidence), SEO content alignment (targets R2 keywords, headings match intent, semantic variations for topical depth, R7's on-page data for meta/heading optimisation).

**Step 4 — Content quality assessment:** Beyond structure — how good is the actual content?

E-E-A-T signals: author attribution and credentials, first-hand experience (original photos, specific examples, detailed process descriptions), evidence-backed claims (data, sources), methodology descriptions vs generic promises. Freshness: last update dates, recent publications, current case studies. Differentiation: does any competitor's content genuinely stand out? Is competitor content mostly commoditised (everyone says same things)? Where does commoditisation create opportunity? Multimedia: text-only or video/diagrams/infographics/interactive/calculators? What formats correlate with top-performing pages from R3?

**Step 5 — Cluster-to-content map:** The critical bridge between content research and site architecture. For each R2 opportunity cluster (NOT_TARGETED, UNDERPERFORMING, COMPETITIVE): does any competitor have a page targeting it? If yes: what page type, how structured, what content blocks, how deep? If no competitor has a page: true content whitespace.

Produce the map showing cluster → primary keyword → competitor pages (with type and depth) → client page (or absence) → content quality notes → gap type. This is the primary input for Concept Creation's sitemap decisions — shows exactly what content exists for each opportunity and what the new site needs to provide.

### Synthesis

**Step 6 — Cross-site content gap analysis:** Synthesise across both parts.

Voice gaps: client voice misaligned with persona expectations, client voice indistinguishable from competitors, voice elements that work and should be preserved. Content structure gaps: page types competitors have that client lacks, content blocks top performers include that client misses, depth gaps (competitor substantive, client thin), SEO content gaps (pages exist but don't target right keywords). Content quality gaps: E-E-A-T signals competitors demonstrate that client doesn't, freshness gaps, multimedia gaps. Content opportunities: topics where all competitors are thin or commoditised, formats no competitor uses, questions the persona asks that no site adequately answers.

Classify each gap: Missing (persona journey requires it, client has nothing — create new, highest priority), Thin (exists but shallow/outdated/doesn't serve persona — rewrite/expand), Misaligned (exists but targets wrong intent or speaks to wrong persona — restructure), Competitive (adequate but competitors do it better — upgrade to match or exceed), Whitespace (no competitor covers it — content leadership opportunity for the proposal).

---

## Output

Write `research/R9-Content.txt`. Apply the decision framework and formatting rules. Append key findings to `baseline-log.txt` tagged with `[R9]`.

**The Research phase is now complete. All substages have been run and reviewed.**

**What R9 feeds downstream:**
- Voice direction recommendation → Concept Creation (C4-Content Strategy, C5-Visual Direction)
- Cluster-to-content map → Concept Creation sitemap (C1 — which pages serve which clusters with what content)
- Must-have content blocks per page type → Concept Creation (page structure requirements)
- Content quality bar → Concept Creation (E-E-A-T standard to target)
- Gap classification → Proposal (specific content deliverables: new pages, rewrites, multimedia additions)
- Voice pattern analysis → Proposal (content strategy positioning)
