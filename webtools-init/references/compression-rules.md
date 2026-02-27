# Compression Rules

Rules and examples for compressing webtools documents. Compression reduces token consumption for downstream plugins while preserving all substantive information.

---

## Core Principle

Compression is **lossless in substance, lossy in verbosity**. Every data point, recommendation, source, and structural element survives. Only the wordiness is reduced.

---

## What to Compress

### Verbose Explanations

Rephrase wordy passages to concise equivalents:

**Before:**
> The client's primary target audience consists of small-to-medium business owners operating within the financial services sector who are actively seeking modern, digital-first solutions to streamline their operations and improve their online presence.

**After:**
> Target audience: SMB owners in financial services seeking digital solutions for operations and online presence.

### Repetitive Phrasing

Identify patterns that restate the same point. Keep the clearest statement, remove the rest:

**Before:**
> The competitor analysis reveals that competitors are primarily using WordPress. This aligns with industry trends showing WordPress dominance. It's worth noting that the WordPress platform continues to be the most popular choice among competitors in this space.

**After:**
> Competitor analysis: WordPress dominant across the competitive set, consistent with industry trends.

### Long Evidence Chains

Preserve key evidence with source reference. Remove intermediate reasoning:

**Before:**
> According to SimilarWeb data (accessed January 2026), the competitor receives approximately 45,000 monthly visits. This traffic volume, when compared against the industry average of 30,000 monthly visits for businesses of similar size and scope, suggests that the competitor has achieved above-average visibility. This is further supported by their strong organic search presence, which Ahrefs data indicates accounts for approximately 60% of their total traffic.

**After:**
> Competitor traffic: ~45K monthly visits (SimilarWeb, Jan 2026) -- above industry avg of 30K. Organic search: ~60% of traffic (Ahrefs).

### Wordy Transitions

Remove or shorten filler between sections:

**Before:**
> Now that we have examined the competitive landscape in detail, let us turn our attention to the audience analysis, which provides important context for understanding user behavior patterns.

**After:**
(Remove entirely -- heading structure provides the transition.)

### Redundant Context

State context once at the top. Do not repeat in subsections:

**Before (in every subsection):**
> For the Apex Consulting website redesign project targeting financial services SMBs...

**After:**
(Stated once in document header. Subsections reference implicitly.)

---

## What to Preserve Exactly

### YAML Frontmatter

Preserve unchanged. Add two fields:

```yaml
compressed: true
raw_file: brief/D1-project-brief.raw.md
```

### Document Structure

All headings and section hierarchy must survive. Same heading levels, same order. Sections may be shorter but never removed.

### Data Points

Every number, statistic, percentage, date, URL, and measurable claim must appear in the compressed version:

- Traffic numbers, conversion rates, revenue figures
- Dates and timeframes
- URLs and domain names
- Tool-specific metrics (DA, DR, keyword volume, etc.)

### Source References

Every citation, attribution, and source link must survive:

- "(Source: Ahrefs, Jan 2026)" -- keep
- "[SimilarWeb](https://similarweb.com)" -- keep
- "According to the client questionnaire" -- keep

### Lists

Bullet points and numbered lists survive structurally. Individual items may be shortened but not removed:

**Before:**
- The homepage should prominently feature a clear value proposition that communicates the company's core offering
- Navigation should be intuitive and follow standard UX patterns that users expect

**After:**
- Homepage: prominent value proposition communicating core offering
- Navigation: intuitive, standard UX patterns

### Key Quotes

Shorten but attribute:

**Before:**
> The client stated during the intake meeting: "We really need to position ourselves as the go-to experts in digital transformation for small financial firms. Our biggest challenge right now is that potential clients don't even know we exist."

**After:**
> Client (intake): "Position as go-to experts in digital transformation for small financial firms. Biggest challenge: lack of awareness."

### Technical Terminology

Domain-specific terms, tool names, framework names, and technical jargon preserved exactly.

### Actionable Recommendations

Every recommendation, next step, and action item must survive. May be shortened:

**Before:**
> It is recommended that the client consider implementing a comprehensive content marketing strategy that focuses on creating in-depth, authoritative articles targeting long-tail keywords in the financial services digital transformation space.

**After:**
> Recommendation: content marketing strategy -- in-depth articles targeting long-tail keywords in financial services digital transformation.

### Links and Images

All markdown links `[text](url)` and images `![alt](src)` preserved exactly.

---

## What NOT to Do

- **Remove sections entirely** -- every section must appear, even if much shorter
- **Drop data points or sources** -- every number and citation survives
- **Change meaning or emphasis** -- if the original says "critical priority", compressed says "critical priority"
- **Summarize** -- summarization is lossy (drops detail). Compression rephrases the same detail concisely
- **Add interpretation** -- do not inject analysis or conclusions not in the original
- **Merge distinct sections** -- keep the original structure; do not collapse multiple sections into one
- **Compress tables** -- tables are already concise. Preserve as-is
- **Compress code blocks** -- preserve as-is
- **Compress YAML frontmatter** -- preserve as-is (except adding compressed/raw_file fields)

---

## Target Metrics

- **Line count reduction:** 40-60% (e.g., 500 lines to 200-300 lines)
- **Character reduction:** 50-70%
- **Data point retention:** 100% (every number, URL, source survives)
- **Section retention:** 100% (every heading survives)

---

## Idempotency Rules

1. **First compression:** Rename original to `.raw.md`, write compressed version to standard path
2. **Re-compression:** Always work from the `.raw.md` file (original source). Overwrite existing compressed version
3. **Never compress a compressed version** -- compound compression is lossy. Always start from `.raw.md`
4. **Check before compressing:** If `.raw.md` already exists at the target path, the document was already compressed. Use `.raw.md` as source

---

## Verification Checklist

After compressing, verify:

- [ ] YAML frontmatter unchanged (except added `compressed` and `raw_file` fields)
- [ ] All headings present in same order and level
- [ ] All numbers/statistics present
- [ ] All URLs and links present
- [ ] All source citations present
- [ ] All recommendations/action items present
- [ ] All tables preserved as-is
- [ ] All code blocks preserved as-is
- [ ] No sections removed entirely
- [ ] Line count reduced by 40-60%
