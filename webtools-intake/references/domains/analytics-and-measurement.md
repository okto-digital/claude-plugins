# Domain: Analytics and Measurement

**Purpose:** Validate that the brief addresses how success will be tracked -- analytics setup, KPIs, conversion events, and reporting cadence. Without measurement, there is no way to know if the website is achieving its business goals or where to improve.

---

## Priority Definitions

- **CRITICAL:** Brief cannot be accurate without this. Must resolve before drafting.
- **IMPORTANT:** Brief will be thinner without this. Resolve in second pass if time allows.
- **NICE-TO-HAVE:** Useful depth. Surface once, accept skip.

---

## 1. Analytics Foundation

| Checkpoint | Priority |
|---|---|
| Analytics platform chosen (Google Analytics 4, Matomo, Plausible, etc.) | CRITICAL |
| Current analytics in place? (For existing sites: account access, historical data) | IMPORTANT |
| Tag management approach (Google Tag Manager, direct integration) | IMPORTANT |
| Privacy-compliant analytics configuration (cookie consent integration) | IMPORTANT |
| Cross-domain tracking needed? (If business uses multiple domains) | NICE-TO-HAVE |

## 2. Key Performance Indicators

| Checkpoint | Priority |
|---|---|
| Primary KPIs defined and tied to business goals | CRITICAL |
| Baseline metrics established (current traffic, conversion rates, bounce rates) | IMPORTANT |
| Target metrics set (where these numbers need to be in 6 months) | IMPORTANT |
| KPIs distinguish between vanity metrics and actionable metrics | NICE-TO-HAVE |

## 3. Conversion Tracking

| Checkpoint | Priority |
|---|---|
| Primary conversion event defined (form submission, purchase, call, download, etc.) | CRITICAL |
| Secondary conversion events identified (newsletter signup, resource download, video view) | IMPORTANT |
| Conversion funnel mapped (entry page to conversion action) | IMPORTANT |
| Micro-conversions tracked (scroll depth, time on page, CTA clicks) | NICE-TO-HAVE |
| Attribution model discussed (first-click, last-click, multi-touch) | NICE-TO-HAVE |

## 4. Reporting and Dashboards

| Checkpoint | Priority |
|---|---|
| Who receives analytics reports? | IMPORTANT |
| Reporting frequency (weekly, monthly, quarterly) | NICE-TO-HAVE |
| Custom dashboard needed? (Looker Studio, platform-native, etc.) | NICE-TO-HAVE |
| Automated reporting setup planned? | NICE-TO-HAVE |

## 5. Marketing Integration

| Checkpoint | Priority |
|---|---|
| Google Search Console setup planned | IMPORTANT |
| Advertising pixels needed? (Google Ads, Meta, LinkedIn, etc.) | IMPORTANT |
| Email marketing tracking (UTM parameters, campaign tracking) | NICE-TO-HAVE |
| Social media referral tracking | NICE-TO-HAVE |
| Offline conversion tracking needs (call tracking, store visits) | NICE-TO-HAVE |

## 6. Data and Privacy

| Checkpoint | Priority |
|---|---|
| Cookie consent tool selected (Cookiebot, CookieYes, Complianz, etc.) | IMPORTANT |
| Consent-mode analytics (GA4 consent mode) configured | IMPORTANT |
| Data retention policies defined | NICE-TO-HAVE |
| Data ownership and access: who owns the analytics accounts? | IMPORTANT |
| Server-side tracking considered? (For accuracy despite ad blockers) | NICE-TO-HAVE |

---

## Question Templates

**How will you measure whether the website is successful?**
- Option A: By tracking leads and conversions -- form submissions, phone calls, or purchases that directly tie to revenue
- Option B: By tracking engagement and growth -- traffic trends, time on site, returning visitors, and brand search volume

**Do you currently have Google Analytics or another analytics tool on your existing site?**
- Option A: Yes, we have GA4 (or another tool) set up and want to keep the historical data flowing into the new site
- Option B: No, or we are not sure -- analytics needs to be set up from scratch as part of this project

**What conversion events should the website track?**
- Option A: Primary: contact form submission. Secondary: phone clicks, email clicks, resource downloads
- Option B: Primary: purchase completion. Secondary: add-to-cart, account creation, wishlist additions

**Do you run or plan to run paid advertising that will drive traffic to the website?**
- Option A: Yes -- we need tracking pixels installed (Google Ads, Meta, etc.) so we can measure ad performance
- Option B: No paid advertising planned -- organic and referral traffic are the primary channels

**Who should have access to the website analytics, and how often should reports be generated?**
- Option A: The business owner reviews a simple monthly summary -- keep it high-level with key metrics
- Option B: A marketing team monitors weekly -- they need detailed dashboards with segmentation and trend analysis
