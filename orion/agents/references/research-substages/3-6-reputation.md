# Substage 3.6 — Reputation & Social Proof

**Code:** R6
**Slug:** Reputation
**Output:** `research/R6-Reputation.txt`
**Hypothesis:** Client lacks trust signals that competitors have established
**Dependencies:** R3-Competitors, R4-Market, R5-Audience
**Reads from:** `project.json`, `baseline-log.txt`, `research/R3-Competitors.txt`, `research/R4-Market.txt`, `research/R5-Audience.txt`
**MCP tools:** none required; web-crawler (required), WebSearch (required)

---

## Purpose

Audit the public trust landscape for the client and competitors. Covers review platforms, social media presence and communication style, and website trust signals (case studies, testimonials, credibility markers). Focus on signal quality over data volume — bounded samples that reveal patterns.

Review samples serve two purposes: direct input for messaging in Concept Creation and Proposal (what customers praise and complain about is positioning intelligence), and validation of persona objections defined in R5-Audience.

**Social media analysis is limited to publicly visible data. Detailed audience demographics, reach data, and ad spend require paid platform tools not available in this pipeline.**

## Upstream Carry-Forward

R3 provides the competitor roster with tier classifications. R4 provides trust signal requirements for this industry (R4 identifies what trust signals matter — this stage checks who has them). R5 provides persona trust thresholds and objections (R5 defines what each persona needs to see — this stage checks whether it exists). Read all three before starting.

## Minimum Scope

Cover at least these areas. You may go beyond them if evidence warrants it.

- Review audit — per platform: rating, count, recency. For deeply-analysed sites: review intensity, response behaviour, 2-3 sample reviews across positive/mixed/negative surfacing praise and complaint patterns, customer language
- Social media presence — active platforms, follower counts, posting frequency. For deeply-analysed sites: content types, tone and communication style from sampled posts, engagement quality relative to follower count
- Website trust signals — case studies (count, structure quality, specificity), testimonials (count, placement, format, credibility), other credibility markers (awards, certifications, memberships, partner logos, client logos, media mentions, team credentials, trust badges). Cross-referenced with R4's industry trust requirements and R5's persona trust thresholds
- Persona validation — compare review praise/complaint patterns against R5's persona objections. Flag mismatches where real customer voice contradicts persona assumptions
- Gap classification — each gap classified as Critical (client lacks what all direct threats have AND primary persona requires), Competitive (below competitor average), Opportunity (no competitor has what audience expects), Strength (client has what competitors lack — preserve and amplify)
- Messaging intelligence — top 3 customer praise patterns, top 3 complaint patterns, exact customer language, content formats with highest engagement, tone that resonates, minimum credibility bar to compete, what would exceed it

## Analysis Scope

| Site | Reviews | Social | Website trust signals |
|---|---|---|---|
| Client | Full | Full | Full |
| Direct-threat competitors (all zones) | Full | Full | Full |
| Aspirational benchmarks (top 1-2) | Rating + count only | Presence + follower count only | Full |
| Remaining roster competitors | Rating + count only | Presence only | Skip |
| Reference sites from INIT notes | Skip | Skip | Credibility markers only |

Deep sampling (reading individual reviews, analysing post content and engagement) is time-intensive — limit to client and direct threats. Surface-level data (rating + count) is quick enough for the full roster.

## Data Sources

From `project.json`: notes (reference site URLs).
From `baseline-log.txt`: mission, client URL, known social profiles, existing reputation signals, all prior findings.
From `research/R3-Competitors.txt`: competitor roster with tier classifications, zone map.
From `research/R4-Market.txt`: trust signal requirements for this industry (what the market demands).
From `research/R5-Audience.txt`: persona trust thresholds and objections (what each persona needs to see to convert).

---

## Methodology — Processing Sequence

Five steps. Steps 1-3 gather data at tiered depth. Step 4 synthesises and classifies gaps. Step 5 extracts messaging intelligence.

**Step 1 — Review audit:** For each site in scope, discover review profiles via web search: Google Business Profile, Trustpilot, industry-specific platforms (Clutch for agencies, G2 for software, TripAdvisor for hospitality), app stores if applicable, Facebook reviews/recommendations.

For all roster sites (surface): platform, rating, count, most recent review date. For client + direct threats (deep): all surface data plus review intensity (weekly/monthly/sporadic/stale), response behaviour (defensive/professional/personal/templated/absent, response speed), and 2-3 sample reviews across positive/mixed/negative. From samples extract: what customers praise (quality, communication, speed, value, expertise, results), what they complain about (price, delays, communication, quality, unmet expectations), what language customers use (real words feed messaging more effectively than marketing copy).

Persona validation checkpoint: compare praise/complaint patterns against R5's persona objections. If the primary persona's objection is "worried about price" but reviews never mention price and consistently complain about communication speed, flag the mismatch — persona may need updating before Concept Creation relies on it.

**Step 2 — Social media presence audit:** Platforms to check: LinkedIn company page, Facebook, Instagram, YouTube, X/Twitter, TikTok — but only platforms relevant to the industry and market. B2B services probably doesn't need TikTok. Consumer brand probably does.

For all roster sites (surface): which platforms active (posted within last 3 months), follower/subscriber count. For client + direct threats (deep): posting frequency (daily/weekly/sporadic/dormant), content types (text, images, video, reels/shorts, carousels, articles), tone and communication style from 3-5 sampled posts (formal/informal, educational/promotional, personal/corporate, visual-heavy/text-heavy), engagement quality relative to follower count (not absolute numbers), community signals (comments, questions, shares vs likes-only).

**Step 3 — Website trust signals:** For client + direct threats + aspirational benchmarks, audit the website for credibility markers. Case studies: present/absent, count, structure quality (challenge → approach → result with metrics vs simple description), specificity (named clients, real results, data vs anonymised and vague). Testimonials: present/absent, count, placement (homepage only vs distributed across service pages), format (text/video/star rating), credibility (full names + company + title vs "J.S., satisfied customer"). Other markers: awards and recognitions, certifications and professional memberships, partner/technology logos, client logos (with or without case studies), media mentions or press features, team credentials displayed, trust badges (security, payment, guarantees).

Cross-reference with R4: check the trust signal requirements R4 identified. If R4 says "case studies are table-stakes," flag any site lacking them. If R4 says "regulatory registration numbers required," check whether each site displays them. Cross-reference with R5: check each persona's trust threshold. If primary persona needs "case studies + team photos + certifications," which sites satisfy that and which don't?

**Step 4 — Gap analysis:** Compare client against competitors. Synthesise across sites — don't restate per-site findings individually.

Review landscape: client's position relative to competitors (stronger/weaker/absent), whether reviews are sparse industry-wide or client-specific gap, platforms where competitors are present but client is not, response behaviour gap. Social presence: dominant channels in this industry, client vs competitor investment level, communication style patterns, content format patterns. Trust signals: which elements are table-stakes (everyone has them), which are differentiating (only some have them), where client is strongest and weakest.

Classify each gap: Critical (client lacks what all direct threats have AND primary persona requires — must address), Competitive (below competitor average but not missing a universal standard — should address), Opportunity (no competitor has what the audience expects based on R4 and R5 — differentiation for the proposal), Strength (client has what competitors lack — preserve and amplify, feature prominently in proposal).

**Step 5 — Messaging intelligence extraction:** Extract signals specifically for Concept Creation and Proposal.

From reviews: top 3 things customers praise → emphasise on the website. Top 3 complaints → objections the website must preemptively address. Exact customer language → use in headlines, testimonial sections, FAQ content. From social: content formats with highest engagement → informs content strategy. Tone that resonates → informs website voice. From trust signals: minimum credibility bar to compete → mandatory trust elements. What would exceed the bar → aspirational trust elements that differentiate.

---

## Output

Write `research/R6-Reputation.txt`. Apply the decision framework and formatting rules. Append key findings to `baseline-log.txt` tagged with `[R6]`.

**What R6 feeds downstream:**
- Trust signal gaps → Concept Creation (which trust elements pages must include), Proposal (deliverable line items)
- Persona validation notes → R5-Audience update if mismatches found (before Concept Creation relies on personas)
- Client strengths → Proposal (assets to amplify prominently)
- Review praise/complaint patterns + customer language → Concept Creation messaging, Proposal competitive narrative
- Social tone and format signals → R9-Content (content strategy), Concept Creation (voice direction)
- Trust element placement needs → R8-UX (where credibility markers go on pages)
- Minimum credibility bar → Concept Creation (non-negotiable trust elements per page type)
