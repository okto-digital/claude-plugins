# Concept Section — Technical Architecture

**Code:** C3
**Slug:** Technical-Architecture
**Output:** `concept/C3-Technical-Architecture.txt`
**Wave:** 2 (depends on C2-Functional)
**Hypothesis:** WordPress with managed hosting covers all requirements without custom architecture

## Purpose

Recommend the technology stack and operational architecture based on functional requirements and technical research. Every choice has a rationale tied to project needs, not generic preference. Covers both build-time decisions (CMS, hosting, integrations) and run-time operations (deployment, testing, monitoring, updates).

## Upstream Dependency

**Reads C2-Functional output** to understand what the tech stack must support. Functional requirements determine platform choice — not the other way around.

## Methodology

1. Read the context file.
2. For each technology category, recommend a solution:
   - **CMS or framework** — based on content management needs, client capability, industry standards
   - **Hosting approach** — managed, cloud, headless
   - **Key integrations** — payment, booking, CRM, ERP, analytics, email marketing
   - **Performance strategy** — CDN, caching, image optimisation
   - **GDPR compliance approach** — cookie consent platform, data handling
   - **SEO technical foundation** — schema markup, sitemap, robots, canonical strategy
   - **Deployment pipeline** — staging, CI/CD, version control. Scaled to project complexity.
   - **Testing approach** — QA strategy, browser/device scope, performance testing. Proportionate to scale.
   - **Monitoring** — uptime, performance tracking, error logging.
   - **Update strategy** — CMS/plugin update cadence, backup verification, security patches.
3. Each recommendation includes: suggested solution, rationale (tied to requirements), alternatives considered, complexity signal.
4. Skip categories that don't apply.

**Boundary notes:**
- GDPR: C3 covers technical implementation (which consent platform, data storage). C9 covers compliance strategy and governance.
- Testing: C3 covers QA infrastructure and browser/device scope. C9 covers accessibility-specific testing approach.
- Updates: C3 covers what systems need maintaining and with what tools. C7 covers schedule, ownership, and cadence.

## Output

Follow output guide at `templates/C3-Technical-Architecture-template.md`.
