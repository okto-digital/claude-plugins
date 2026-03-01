# Domain: Competitor Landscape

**Document ID:** R2
**Output filename:** R2-competitor-landscape.md
**Topic:** "Competitor Landscape"
**Wave:** 1
**Cross-topic inputs:** none

---

## Tools

**Required:** WebSearch, WebFetch
**Optional MCP:** `mcp__dataforseo__dataforseo_labs_google_competitors_domain` (discover organic competitors by domain), `mcp__dataforseo__dataforseo_labs_google_domain_rank_overview` (domain authority and ranking metrics)
**Crawling:** web-crawler dispatch for each competitor homepage (Step 2 surface scan)

**IMPORTANT:** This is BREADTH research (landscape mapping), not DEPTH research (content analysis). Identify who matters and where the gaps are.

---

## Methodology

### Step 1: Discover Competitors

Start with any competitors named in D1/D2, then expand using **location + business type** queries.

Determine from D1/D2:
- **Business type** -- the category a customer would search for (e.g., "hotel", "web design agency")
- **Location** -- city, region, or area the business serves

If DataForSEO `dataforseo_labs_google_competitors_domain` is available, run it on the client's domain to discover organic competitors programmatically.

Then run discovery queries:
- WebSearch "[business type] [city/area]"
- WebSearch "[business type] near [city]"
- WebSearch "best [business type] [region] [year]" for curated lists and rankings
- WebSearch "[industry] directory [country]" to find industry listing pages
- WebSearch "[business type] [location] reviews" for review aggregator results

**Target:** Identify 8-15 distinct competitors. Record company name, URL, and discovery source for each.

**IMPORTANT:** Do not stop at client-named competitors. The value of R2 is discovering competitors the client may not be aware of.

### Step 2: Surface Scan Each Competitor

For each discovered competitor, dispatch web-crawler for the homepage and record:

- **Tagline / value proposition** -- one-line summary of how they position themselves
- **Services listed** -- what they offer (breadth vs specialization)
- **Visual maturity** -- modern design or dated? Professional photography or stock?
- **Color palette** -- primary brand color, secondary/accent colors, overall palette mood (warm, cool, neutral, bold, muted). Note hex values when extractable.
- **Tone of voice** -- observe headline style, CTA language, about page copy. Classify as: formal/professional, friendly/approachable, technical/authoritative, casual/playful, luxury/aspirational. Note 2-3 characteristic phrases.
- **Mobile signal** -- responsive layout visible?
- **Trust signals visible** -- certifications, awards, client logos, review widgets

If DataForSEO `dataforseo_labs_google_domain_rank_overview` is available, run it per competitor for ranking metrics.

WebSearch "[competitor name] reviews" for each competitor:
- Google rating (stars out of 5)
- Review count
- Most recent review date (if visible)

**IMPORTANT:** Surface scan. Spend no more than 2-3 minutes per competitor. If crawl fails, record what is observable from search result snippets.

### Step 3: Market Positioning Map

Organize competitors along key dimensions:

- **Premium vs Budget** -- pricing signals, design quality, messaging sophistication
- **Specialist vs Generalist** -- narrow service focus vs broad offerings
- **Local vs Regional vs National** -- geographic scope of services
- **Established vs Newcomer** -- business maturity signals

Identify clusters (where most competitors sit) and gaps (underserved positions).

Note pricing signals where publicly available:
- Published pricing pages
- "Starting from" indicators
- "Request a quote" (hides pricing = likely premium)
- Free tier or freemium model presence

### Step 4: Digital Maturity Snapshot

For each competitor, assess (from surface observation):

- **Website quality:** Modern/professional, functional but dated, or clearly outdated
- **Blog/content:** Active (posts within last 3 months), stale (6+ months), or absent
- **Social media:** Active presence visible, dormant accounts, or no social links
- **SSL:** Present (https) or absent
- **Core Web Vitals signal:** Fast-loading or noticeably slow (subjective observation)

Create a simple maturity ranking: High / Medium / Low for each competitor.

### Step 5: Synthesize

**Detailed Findings sub-sections:**
- Competitor Discovery (full list with URLs and discovery source)
- Brand & Visual Profile (per competitor: colors, palette mood, tone of voice, characteristic phrases)
- Market Positioning Map (dimensions, clusters, gaps)
- Pricing Signals (what is visible about market pricing)
- Digital Maturity Comparison (table format)
- Review/Reputation Summary (ratings, review counts)
- Competitive Gaps (underserved positions, unmet needs)
