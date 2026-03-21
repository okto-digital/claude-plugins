# Substage 3.5 — Audience & Personas

**Code:** R5
**Slug:** Audience
**Output:** `research/R5-Audience.txt`
**Hypothesis:** Target audience has specific device preferences and trust thresholds that affect UX decisions
**Dependencies:** R1-SERP, R2-Keywords, R3-Competitors, R4-Market
**Reads from:** `project.json`, `baseline-log.txt`, `research/R1-SERP.txt`, `research/R2-Keywords.txt`, `research/R3-Competitors.txt`, `research/R4-Market.txt`
**MCP tools:** DataForSEO (optional — demographics enrichment only)

---

## Purpose

The only fully synthesised substage in the research phase. Distils everything gathered across R1-R4 into structured human profiles. Every layout decision, content choice, and feature recommendation in later phases should be traceable back to a persona defined here.

**This stage performs no new scraping or tool-heavy data collection. It is an interpretation layer — taking signals scattered across prior research and organising them into actionable audience definitions.**

Keep the persona count tight — one per distinct audience segment. Fewer well-researched personas beat many shallow ones. Typical range: 2-4 personas.

## Minimum Scope

Cover at least these items. You may go beyond them if evidence warrants it.

- Signal collection — extract and organise all audience signals from R1-R4 into a working evidence base before defining segments. No new research, just structured extraction
- Audience segments — 2-4 distinct segments, each meaningfully different (different needs, behaviour, or journey). Every segment must map to at least one keyword cluster from R2. Segments without keyword evidence are speculative — flag but don't build the proposal around them
- Persona profiles — one per segment, compact and decision-oriented. Fields: label, segment, demographics, goal on website, buying motivation, research behaviour, device and channel, trust threshold, mapped keyword clusters, top objections, messaging angle. Short phrases, not paragraphs
- Primary design target — one persona flagged as the primary target. Homepage, navigation, and main conversion flow optimised for this persona. Other personas served but primary takes priority on design tradeoffs
- Journey maps — per persona, mapping awareness → consideration → decision → post-conversion. Each stage connects persona behaviour → relevant keyword clusters from R2 → concrete website implication (what page/content is needed)
- Cross-persona synthesis — shared needs (universal site requirements), conflicting needs (design tradeoffs requiring resolution), coverage check (do personas collectively cover all R2 keyword clusters and R3 competitive zones)

## Data Sources

From `project.json`: goal, site type, notes (audience signals from operator).
From `baseline-log.txt`: mission, client profile, all prior findings including D2, R1-R4 highlights.
From `research/R1-SERP.txt`: intent patterns, search behaviour signals, SERP feature types (local pack → local intent, PAA → information-seeking, shopping → transactional readiness).
From `research/R2-Keywords.txt`: keyword clusters with intent distribution, page type mappings, funnel stage signals, keyword modifiers (location, comparison, price, "best").
From `research/R3-Competitors.txt`: competitor positioning, USPs, CTAs, messaging angles, zone map, tier classifications.
From `research/R4-Market.txt`: customer behaviour and buying journey (flagged as primary input from R4), website functionality expectations, trust signals, market-specific behavioural patterns.

---

## Methodology — Processing Sequence

Five steps. Step 1 collects signals. Step 2 defines segments. Step 3 builds personas. Step 4 maps journeys. Step 5 synthesises across personas.

**Step 1 — Signal collection:** Before defining segments, compile all audience signals from prior research into a working evidence base. This is extraction and organisation, not new research.

- From R1: search terms and phrasing patterns, SERP features indicating audience behaviour (local pack → local buyers, PAA → information seekers, shopping → ready to buy).
- From R2: intent distribution across clusters (proportion informational vs commercial vs transactional reveals dominant audience mode), keyword modifiers (location = local buyers, comparison = careful evaluators, "best"/"top" = quality-conscious, price = budget-conscious), funnel stage volumes (where the audience spends most of their journey).
- From R3: competitor positioning (premium vs value, specialist vs generalist → reveals which segments competitors target), CTAs (free consultation vs book now vs download guide → reveals expected audience action), USPs (speed/price/expertise/trust → reveals what audience values), tier patterns (do direct threats target the same segment or differentiate by audience).
- From R4: decision cycle length, research and comparison habits, referral patterns, website functionality expectations, trust signal requirements, market-specific behavioural differences.

**Step 2 — Segment definition:** Define distinct segments from the evidence before building personas. Segmentation dimensions to consider: by buying intent (informational researchers vs transactional buyers — if R2 shows significant volume in both), by service/product line (distinct services to distinct audiences — R3's zones often reveal this), by market (if R4's comparison shows meaningful behavioural differences between markets), by decision role (B2B: researcher/evaluator vs decision-maker/approver — need different content and trust signals), by digital sophistication (tech-savvy vs tech-averse — affects UX complexity and feature expectations). Rules: minimum 2, maximum 4. If more emerge, consolidate lowest-value segments. Each must be meaningfully different. Each must map to at least one R2 keyword cluster.

**Step 3 — Persona construction:** For each segment, build a compact profile. Be concise — short phrases, not paragraphs. The persona is a decision tool, not a character study.

Persona fields: Name and label (descriptive, e.g. "Budget-conscious SMB owner" — not fictional biography), Segment (from Step 2), Demographics (age range, location, language, role — only what's evidenced), Goal on website (one sentence — what they're trying to accomplish), Buying motivation (price/quality/trust/speed/expertise/convenience), Research behaviour (search/referrals/reviews/social/direct, what they compare), Device and channel (primary device, preferred channels), Trust threshold (what they need to see — certifications, reviews, case studies, team photos, pricing transparency, regulatory badges), Keyword clusters (which R2 clusters this persona searches for — maps persona to specific pages), Objections (top 2-3 reasons they might not convert), Messaging angle (formal/informal, technical/simple, benefit-led/feature-led, emotional/rational).

Flag one persona as the primary design target — the persona the homepage, navigation, and main conversion flow should be optimised for. When design tradeoffs arise, primary target wins.

**Step 4 — Journey map per persona:** Map awareness → consideration → decision → post-conversion. Per stage: persona behaviour, relevant keyword clusters from R2, and the website implication (what page/content is needed at this point).

- Awareness: recognises need, searches broadly. Informational clusters, question-format keywords. → Blog posts, guides, problem-framing content.
- Consideration: researches options, compares providers. Commercial clusters, comparison keywords. → Service pages, case studies, comparison pages, pricing signals.
- Decision: ready to act, needs confidence. Transactional clusters, brand + service keywords. → Clear CTAs, contact forms, trust signals, pricing, guarantees.
- Post-conversion: converted, needs onboarding or becomes referral source. Brand keywords, support keywords. → Client portal, documentation, referral programme, review prompts.

Every R2 keyword cluster should appear in at least one persona's journey. Unmapped clusters mean either the cluster isn't relevant or a persona is missing. Not every persona needs every stage — a B2B decision-maker may skip awareness, a returning customer enters at decision.

**Step 5 — Cross-persona synthesis:** After individual personas, synthesise across them. Shared needs: things all personas require (universal site requirements). Conflicting needs: where personas want different things (e.g. visible pricing vs "contact for quote") — these require design decisions, primary persona wins but secondary shouldn't be alienated. Coverage check: do personas collectively cover all R2 keyword clusters and all R3 competitive zones? Significant uncovered clusters or zones indicate a missed segment or clusters to remove from the proposal.

---

## Tooling

**No primary tools required** — this is a synthesis stage reading prior R-files.

**DataForSEO — optional demographics enrichment:**
- Demographic breakdown (age/gender) for core search terms. Cheap to run on 5-10 high-volume keywords. Validates or challenges assumptions about who's actually searching. Not required but recommended when available.

---

## Output

Write `research/R5-Audience.txt`. Apply the decision framework and formatting rules. Append key findings to `baseline-log.txt` tagged with `[R5]`.

**What R5 feeds downstream:**
- Persona profiles + primary design target → Concept Creation (site structure, page priorities, design tradeoff resolution)
- Trust thresholds per persona → R6-Reputation (what social proof each persona needs)
- Device preferences + trust thresholds + primary conversion actions → R8-UX (contextualise UX analysis per persona)
- Messaging angles + content format needs + funnel-stage content → R9-Content (content strategy per persona)
- Journey map website implications → Concept Creation sitemap (which pages serve which persona at which stage)
- Keyword cluster ↔ persona mapping → Concept Creation (every proposed page has an audience context)
- Conflicting needs → Concept Creation (explicit tradeoff list to resolve)
