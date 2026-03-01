# Domain: Technology & Performance

**Document ID:** R7
**Output filename:** R7-tech-performance.md
**Topic:** "Technology & Performance"
**Wave:** 1
**Cross-topic inputs:** none

---

## Tools

**Required:** WebSearch, WebFetch
**Optional MCP:** `mcp__dataforseo__on_page_lighthouse` (Lighthouse audit data), `mcp__dataforseo__on_page_instant_pages` (page-level performance data), `mcp__dataforseo__domain_analytics_technologies_domain_technologies` (technology stack detection)
**Crawling:** web-crawler dispatch for client homepage (Step 3 technology detection)

**IMPORTANT:** This is a baseline assessment using publicly accessible methods only. Not a security audit, penetration test, or comprehensive WCAG accessibility audit.

---

## Methodology

### Step 1: PageSpeed Insights

Fetch Google PageSpeed API for the client's homepage (both strategies):

**Mobile:**
```
https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=[client_url]&strategy=mobile
```

**Desktop:**
```
https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=[client_url]&strategy=desktop
```

**NOTE:** These API URLs are NOT WAF-blocked. WebFetch works directly -- no crawl cascade needed.

If DataForSEO `on_page_lighthouse` is available, use it for richer Lighthouse audit data. If `on_page_instant_pages` is available, use it for additional page-level metrics.

Extract from the response:
- **Performance score** (0-100)
- **First Contentful Paint (FCP)** -- when first content appears
- **Largest Contentful Paint (LCP)** -- when main content loads
- **Cumulative Layout Shift (CLS)** -- visual stability
- **Total Blocking Time (TBT)** -- interactivity delay
- **Speed Index** -- how quickly content is visually populated

Classify each metric: Good / Needs Improvement / Poor (using Google's thresholds).

### Step 2: Competitor Performance Comparison

Run PageSpeed API for 2-3 competitor URLs:
- From D1/D2 -- competitors mentioned
- From WebSearch -- top-ranking competitor for the client's core service query

Create a comparison table:

| Metric | Client | Competitor A | Competitor B | Competitor C |
|--------|--------|-------------|-------------|-------------|
| Mobile Score | XX | XX | XX | XX |
| Desktop Score | XX | XX | XX | XX |
| LCP | Xs | Xs | Xs | Xs |
| CLS | X.XX | X.XX | X.XX | X.XX |
| TBT | Xms | Xms | Xms | Xms |

Note where the client outperforms, matches, or lags behind competitors.

### Step 3: Technology Detection

Review D1 for existing tech detection, then supplement:

Dispatch web-crawler for client homepage and examine page source. If DataForSEO `domain_analytics_technologies_domain_technologies` is available, use it for comprehensive stack detection.

Detect:
- **CMS / Framework** -- meta generator tag, common framework signatures in HTML/JS
- **Hosting signals** -- server header, CDN indicators (Cloudflare, Fastly, AWS CloudFront)
- **JavaScript frameworks** -- React, Vue, Angular, jQuery, Next.js signatures
- **CSS frameworks** -- Bootstrap, Tailwind CSS, Foundation signatures
- **Analytics** -- Google Analytics (GA4 / UA), Tag Manager, other analytics scripts
- **Chat/support** -- live chat widgets (Intercom, Drift, Tawk.to, Zendesk)
- **CRM/forms** -- form handling (HubSpot, Mailchimp, custom forms)
- **Booking/scheduling** -- Calendly, Acuity, custom booking
- **Payment** -- Stripe, PayPal, Mollie, other payment integrations
- **Other third-party** -- maps, social embeds, video players, review widgets

WebSearch "[detected CMS] performance benchmarks" to compare against platform norms.

### Step 4: Mobile Usability

Assess mobile experience:

- Mobile PageSpeed score (from Step 1)
- Viewport meta tag present? (`<meta name="viewport" ...>`)
- Responsive layout signals (media queries in CSS, responsive framework detected)
- Touch-friendly indicators (button sizes, tap targets mentioned in PageSpeed report)
- Mobile-specific features (click-to-call, mobile nav pattern)

### Step 5: Accessibility Baseline

Quick-check indicators from page source (NOT a WCAG audit):

- **Language attribute** -- `<html lang="...">` present?
- **Heading hierarchy** -- H1 present? Sequential order (H1 > H2 > H3)?
- **Image alt text** -- pattern check: do images have alt attributes? (sample 5-10 images)
- **Form labels** -- do form inputs have associated labels?
- **Color contrast** -- any extremely low-contrast text visible?
- **Skip navigation** -- skip-to-content link present?
- **ARIA landmarks** -- main, nav, footer roles defined?

Rate as: Good baseline / Some gaps / Significant gaps. Do NOT claim WCAG compliance levels.

### Step 6: Synthesize

**Detailed Findings sub-sections:**
- Performance Baseline (PageSpeed scores, Core Web Vitals with classification)
- Competitor Performance Comparison (table from Step 2)
- Technology Stack (CMS, frameworks, hosting, third-party integrations)
- Mobile Usability Assessment
- Accessibility Baseline (quick-check results)
- Platform Benchmarks (client performance vs platform norms)
