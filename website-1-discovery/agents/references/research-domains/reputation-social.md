# Domain: Reputation & Social Proof

**Document ID:** R6
**Output filename:** R6-reputation-social.md
**Topic:** "Reputation & Social Proof"
**Wave:** 1
**Cross-topic inputs:** none

---

## Tools

**Required:** WebSearch, WebFetch
**Optional MCP:** `mcp__dataforseo__business_data_business_listings_search` (business directory listing data)
**Crawling:** web-crawler dispatch for social media profiles and directory listings (Steps 3-4)

**IMPORTANT:** This is an external signal scan. Only use publicly accessible information. Distinguish clearly between what the client claims and what is externally verifiable.

---

## Methodology

### Step 1: Google Reviews

Search for the client's review presence:

- WebSearch "[company name] reviews"
- WebSearch "[company name] [city] reviews" (if local business)

Record:
- **Overall rating** -- stars out of 5
- **Review count** -- total number of reviews
- **Most recent review date** -- is the review stream active?
- **Positive themes** (3-5) -- what satisfied customers praise (from visible review snippets)
- **Negative themes** (2-3) -- what dissatisfied customers mention (from visible review snippets)

**IMPORTANT:** If no Google reviews are found, note this explicitly. A business with zero reviews has a different problem than one with poor reviews.

### Step 2: Brand Mention Scan

Search for the company name without "reviews":

- WebSearch "[company name]"
- WebSearch "[company name] [industry]"
- WebSearch "[company name] news" or "[company name] press"

Record what appears beyond the client's own website:
- **Directory listings** -- which directories list them?
- **Social media profiles** -- which appear in search results?
- **News mentions** -- any press coverage or media appearances?
- **Third-party mentions** -- industry articles, partner references, event listings
- **Negative results** -- any complaints, legal notices, or negative press?

Assess: is the brand visible beyond their own properties, or does their own website dominate all results?

### Step 3: Directory Presence

Check industry-relevant directory presence:

- WebSearch "[company name] [industry] directory"
- WebSearch "[industry] directory [country/region]" to identify relevant directories

If DataForSEO `business_data_business_listings_search` is available, use it to check the client's business listing data across aggregated sources.

For directories found, note: Is the client listed? Is the profile complete? Rating if available?

Record:
- Directories where client IS listed (with profile completeness: full, partial, claimed, unclaimed)
- Directories where client is NOT listed but should be (based on industry relevance)
- Comparison: how many directories do competitors appear in? (reference R2 if available)

### Step 4: Social Media Audit

Using social media links from D1 (or discovered via search):

For each platform where the client has a presence:
- **Platform name**
- **Follower/connection count** (publicly visible)
- **Posting frequency** -- daily, weekly, monthly, dormant
- **Last post date**
- **Engagement level** -- do posts get likes/comments/shares? (surface observation only)
- **Content type** -- what do they post? (promotional, educational, behind-the-scenes, mixed)

Assess overall social media health:
- **Active** -- regular posts with engagement
- **Present but dormant** -- account exists, rarely posts
- **Inconsistent** -- some platforms active, others abandoned
- **Absent** -- no social media presence found

**IMPORTANT:** Only assess publicly visible information.

### Step 5: Social Proof Validation

Compare client claims (from D1) against external evidence:

For each claim the client makes:
- "X years in business" -- corroborated by company registration, about page, earliest web archive?
- "X+ clients" -- evidence in portfolio, case studies, testimonials, Google review count?
- "Award-winning" -- award listed on award organization's website?
- "Industry-certified" -- certification verifiable on certifying body's directory?
- "Partnerships" -- partner listed on partner's website?
- Client logos displayed -- do those companies acknowledge the relationship?

Record:
- **Verified claims** -- externally corroborated
- **Unverified claims** -- no external evidence found (not necessarily false, just unverifiable)
- **Gaps** -- claims the client should make but does not (e.g., strong reviews not featured on website)

### Step 6: Synthesize

**Detailed Findings sub-sections:**
- Google Reviews Summary (rating, count, themes, activity)
- Brand Visibility (what appears in search results beyond own website)
- Directory Presence (listed vs missing, profile completeness)
- Social Media Health (platform-by-platform assessment)
- Social Proof Validation (claims vs evidence)
