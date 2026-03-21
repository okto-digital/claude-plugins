# Substage 3.8 — Technology & Performance

**Code:** R8
**Slug:** Technology
**Output:** `research/R8-Technology.txt`
**Hypothesis:** Current site is technically adequate but has specific performance or accessibility gaps
**Dependencies:** R4-Competitors, R5-Market
**Reads from:** `project.json`, `baseline-log.txt`, `research/R4-Competitors.txt`, `research/R5-Market.txt`
**MCP tools:** DataForSEO (required), web-crawler (optional)

---

## Purpose

Audit the technical foundation of the client website, competitors from the roster, and any reference sites from INIT notes. Covers technology stack, Core Web Vitals, Lighthouse scores, WCAG accessibility compliance, and regulatory compliance surface scan. Findings are compared across all analysed sites to identify where the client stands technically and what the proposal should recommend.

**This is a surface scan, not a certified audit. WCAG findings flag critical violations at AA level. Compliance findings flag visible signals only — not a legal assessment. Always caveat accordingly in the output.**

## Upstream Carry-Forward

R4 provides the competitor roster with tier classifications and zone map. R5 provides the regulatory and compliance checklist — R5 identifies what the law and industry standards require, this stage verifies whether actual sites comply. Read both before starting.

For new builds (site_type = "new"): skip client analysis entirely. The stage becomes a pure benchmark exercise — what technical standards do competitors and reference sites set that the new build must meet or exceed?

## Minimum Scope

Cover at least these areas. You may go beyond them if evidence warrants it.

- Technology stack per domain — CMS/framework, hosting/infrastructure signals, analytics and tracking tools, marketing tools, performance tools (CDN, image optimisation, caching), e-commerce tools (if applicable), security signals (SSL type, WAF). Run on full roster + client + reference sites
- Performance scorecard — Lighthouse scores (Performance, Accessibility, Best Practices, SEO) and Core Web Vitals (LCP, INP, CLS, TTFB) per page for all fully-analysed sites. Benchmarked against standard thresholds
- WCAG accessibility surface scan — overall score, critical AA violations, missing alt text, contrast failures, keyboard navigation issues, mobile accessibility. Cross-referenced with R5's EAA/accessibility requirements where applicable. Caveated as automated scan, not certified audit
- Regulatory compliance surface scan — verify R5's compliance checklist against actual sites: cookie consent (present, type, timing), privacy policy, third-party tracking before consent, data collection form notices, industry-specific requirements from R5, local legal requirements (imprint page, business registration). Caveated as surface check, not legal assessment
- Cross-site comparison — where the client stands relative to competitors on each dimension. Tech stack landscape (dominant pattern, outliers), performance ranking, accessibility ranking, compliance comparison
- Gap classification — each gap classified as Critical (regulatory/performance failure where competitors succeed), Competitive (below competitor average), Opportunity (all sites perform poorly — differentiation), Non-issue (client at or above average)

## Analysis Scope

| Site | Analysis depth | Pages |
|---|---|---|
| Client | Full (tech + performance + compliance) | Homepage + max 3 subpages |
| Direct-threat competitors (all zones) | Full | Homepage + max 3 subpages |
| Aspirational benchmarks (top 1-2) | Full | Homepage + max 3 subpages |
| Remaining roster competitors | Tech stack detection only | Domain-level only |
| Reference sites from INIT notes | Tech + performance only, no gap analysis | Homepage + max 3 subpages |

Tech stack detection is one API call per domain — cheap enough for the entire roster. Lighthouse and on-page analysis require multiple calls per page across 4 pages per site — limit to direct threats + aspirational benchmarks. Typically 5-8 sites get full analysis including the client.

## Data Sources

From `project.json`: site type, notes (reference site URLs).
From `baseline-log.txt`: mission, client URL, all prior findings including R4 and R5 highlights.
From `research/R4-Competitors.txt`: competitor roster with tier classifications (which competitors are direct threats vs aspirational vs niche), zone map.
From `research/R5-Market.txt`: regulatory and compliance checklist (what requirements apply to this industry and market).

---

## Methodology — Processing Sequence

Six steps. Step 1 selects pages. Steps 2-5 gather data at increasing depth. Step 6 synthesises.

**Step 1 — Subpage selection:** For each site receiving full analysis, identify 3 most representative subpages. Priority: (1) primary conversion page — product, pricing, booking, contact, request-a-quote, (2) category or service listing page — organises the site's main offerings, (3) content or secondary page — portfolio, FAQ, landing page, blog post, about. Log selected pages and rationale in the output.

**Step 2 — Technology stack detection:** Run on all sites in scope (entire roster + client + reference sites). One call per domain. Extract and categorise: CMS/framework, hosting/infrastructure, analytics and tracking (GA version, Tag Manager, Hotjar, Meta Pixel), marketing tools (email, CRM, live chat, A/B testing), performance tools (CDN, image optimisation, lazy loading, caching), e-commerce (payment gateways, cart systems, product feeds — if applicable), security (SSL type, WAF, DDoS indicators). Full-roster coverage reveals industry tech patterns — knowing 80% of competitors use WordPress while one uses headless is useful signal even without Lighthouse data.

**Step 3 — Performance and on-page analysis:** Run on fully-analysed sites only. Per page (homepage + up to 3 subpages): Lighthouse scores (Performance, Accessibility, Best Practices, SEO — each 0-100) and Core Web Vitals (LCP, INP, CLS, TTFB) plus on-page signals (meta tags, heading structure, image optimisation, mobile readiness, structured data).

Benchmarks: LCP ≤2.5s good / 2.5-4.0s needs improvement / >4.0s poor. INP ≤200ms / 200-500ms / >500ms. CLS ≤0.1 / 0.1-0.25 / >0.25. TTFB ≤800ms / 800-1800ms / >1800ms. Lighthouse scores ≥90 good / 50-89 needs improvement / <50 poor.

**Step 4 — WCAG accessibility surface scan:** Derived from Lighthouse accessibility audit in Step 3. Check: overall score, critical AA violations (missing form labels, no skip navigation, focusable elements without visible focus, ARIA misuse), image accessibility (missing alt text, decorative images not marked), colour contrast failures, keyboard navigation (unreachable elements, focus traps), mobile accessibility (touch targets, viewport, reflowability). Cross-reference with R5: if R5 identifies EAA obligations or industry-specific accessibility requirements, flag violations against those specific requirements. Caveat: "Surface scan based on automated Lighthouse testing, not a certified WCAG audit."

**Step 5 — Regulatory compliance surface scan:** Verify R5's compliance checklist against actual sites. GDPR/privacy (all markets): cookie consent banner (present, type, timing relative to cookie setting), privacy policy (present, accessible from footer), third-party tracking before consent, data collection form notices, cookie policy. Industry-specific (from R5): financial disclaimers, healthcare content restrictions, e-commerce requirements (return policy, terms, business registration), local legal (imprint page where required). Use web scraping to check homepage footer links, policy pages, and form pages. Caveat: "Surface-level compliance check, not a legal assessment."

**Step 6 — Cross-site comparison and gap analysis:** Synthesise across all sites — don't restate per-site findings. Compare: tech stack landscape (dominant CMS, outliers, technology-performance correlations), performance ranking (all fully-analysed sites by Lighthouse and CWV — where does the client sit), accessibility ranking (industry-wide problems vs client-specific gaps), compliance comparison (who meets R5's checklist vs who has gaps). Classify each gap: Critical (client fails where competitors succeed AND it's a regulatory or performance requirement — must fix), Competitive (below competitor average but not failing a hard requirement — should fix), Opportunity (all sites including competitors perform poorly — differentiation for the proposal), Non-issue (client at or above average — note but don't emphasise).

---

## Tooling

**DataForSEO — primary tool:**
- Domain technology detection — full tech stack per domain. One call per domain, entire roster.
- Lighthouse audit — scores per page. One call per page, fully-analysed sites only.
- On-page instant analysis — Core Web Vitals and on-page signals per page. One call per page, fully-analysed sites only.

**Web-crawler — compliance checks (optional):**
- Dispatch for cookie consent, privacy policy, and form page verification on fully-analysed sites. Fallback: use WebSearch to check policy pages directly.

**Estimated API calls per project:** 15-20 domain technology calls + 30-65 Lighthouse/on-page calls depending on number of fully-analysed sites. Main cost driver is Step 3 per-page analysis.

---

## Output

Write `research/R8-Technology.txt`. Apply the decision framework and formatting rules. Append key findings to `baseline-log.txt` tagged with `[R8]`.

**What R8 feeds downstream:**
- Tech stack landscape → Concept Creation technical architecture (C3)
- Performance benchmarks → Concept Creation (realistic targets for new build)
- Accessibility findings → Concept Creation compliance requirements (C9), Proposal (deliverable line items)
- Compliance gaps → Concept Creation (C9), Proposal (non-negotiable elements, regulatory risk argument)
- Gap classification → Proposal (priority ordering of technical recommendations)
- Cross-site comparison → R9-UX (performance constraints for UX analysis), R10-Content (structured data gaps)
