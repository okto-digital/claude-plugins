# Domain Quick Reference

**Purpose:** Compact index of all 21 domain checklists. Contains CRITICAL checkpoint names and section-level counts. Used by the brief-generator for coarse checkpoint mapping during MEETING mode. Full checkpoint details, question templates, and priority descriptions are in the individual domain files, accessible to the checkpoint-scorer sub-agent on demand.

**Generated from:** `${CLAUDE_PLUGIN_ROOT}/references/domains/*.md`

---

## Conditional Domain Triggers

| Extension | Attaches To | Domain | Activated When |
|---|---|---|---|
| Online Store | Technical Foundation + Lead Capture | ecommerce | Products or services sold directly online |
| Content Publishing | The Website Vision | blog-and-editorial | Regular content publishing planned (blog, news, articles) |
| Multiple Languages | Technical Foundation | multilingual | Site needs more than one language |
| Member Access | Technical Foundation + Lead Capture | user-accounts | Login, membership, or gated content needed |
| Moving From Current Site | Technical Foundation | migration-and-redesign | Existing site to migrate or replace |
| Bookings and Appointments | Lead Capture | booking-and-scheduling | Online appointment or reservation functionality |

---

## How to Read Each Entry

```
## domain-name [UNIVERSAL or CONDITIONAL: trigger]

### Section Name (total: XC YI ZN)
CRITICAL: checkpoint name | checkpoint name | ...
```

- `XC` = CRITICAL count, `YI` = IMPORTANT count, `ZN` = NICE-TO-HAVE count
- Only CRITICAL checkpoint names are listed (pipe-separated)
- Sections with no CRITICAL checkpoints show `(no CRITICAL)`
- For full checkpoint details, question templates, and priority descriptions: read the domain file

---

## UNIVERSAL DOMAINS

---

## business-context [UNIVERSAL]

### 1. Business Identity (8: 5C 2I 1N)
CRITICAL: Company name and legal entity | Industry and sub-sector | Location(s) and service area | Business model (B2B, B2C, etc.) | Core offering in one sentence

### 2. Website Purpose (5: 3C 2I 0N)
CRITICAL: Primary purpose of the website | What problem the website solves | New build, redesign, or expansion

### 3. Business Goals (5: 2C 2I 1N)
CRITICAL: Top 3 business goals the website must support | Definition of success at 6 months

### 4. Market Position (4: 1C 2I 1N)
CRITICAL: Key differentiators from competitors

### 5. Revenue and Business Model (4: 2C 1I 1N)
CRITICAL: How the business makes money | Which revenue streams the website supports

### 6. Stakeholders and Decision Making (5: 2C 2I 1N)
CRITICAL: Primary point of contact | Who approves final deliverables

**Domain total: 31 checkpoints, 15 CRITICAL**

---

## competitive-landscape [UNIVERSAL]

### 1. Competitor Identification (5: 2C 2I 1N)
CRITICAL: At least 3 named competitors | Competitor website URLs

### 2. Competitor Web Presence Analysis (6: 2C 3I 1N)
CRITICAL: Competitor strengths to match or exceed | Competitor weaknesses or gaps to exploit

### 3. Differentiation Strategy (4: 1C 2I 1N)
CRITICAL: Clear positioning statement

### 4. Market Dynamics (4: 0C 2I 2N)
(no CRITICAL)

### 5. Competitive Content and Messaging (4: 0C 2I 2N)
(no CRITICAL)

**Domain total: 23 checkpoints, 5 CRITICAL**

---

## target-audience [UNIVERSAL]

### 1. Primary Audience Definition (6: 3C 2I 1N)
CRITICAL: Primary audience clearly identified | Professional context: role, industry, seniority (B2B) | What problem or need brings them to the website

### 2. Secondary Audience (4: 0C 3I 1N)
(no CRITICAL)

### 3. Audience Behavior (5: 1C 3I 1N)
CRITICAL: How does the audience discover businesses like this

### 4. Decision Journey (5: 2C 2I 1N)
CRITICAL: What information the audience needs before taking action | Common objections or hesitations

### 5. Audience Language and Expectations (4: 0C 3I 1N)
(no CRITICAL)

### 6. Existing Audience Data (4: 0C 1I 3N)
(no CRITICAL)

**Domain total: 28 checkpoints, 6 CRITICAL**

---

## project-scope [UNIVERSAL]

### 1. Timeline (5: 1C 3I 1N)
CRITICAL: Target launch date or deadline

### 2. Budget (5: 1C 2I 2N)
CRITICAL: Budget range established

### 3. Phasing Strategy (5: 0C 2I 3N)
(no CRITICAL)

### 4. Deliverables (5: 0C 4I 1N)
(no CRITICAL)

### 5. Stakeholder and Approval Process (5: 1C 3I 1N)
CRITICAL: Decision-maker identified

### 6. Risks and Constraints (5: 0C 2I 3N)
(no CRITICAL)

**Domain total: 30 checkpoints, 3 CRITICAL**

---

## analytics-and-measurement [UNIVERSAL]

### 1. Analytics Foundation (5: 1C 3I 1N)
CRITICAL: Analytics platform chosen

### 2. Key Performance Indicators (4: 1C 2I 1N)
CRITICAL: Primary KPIs defined and tied to business goals

### 3. Conversion Tracking (5: 1C 2I 2N)
CRITICAL: Primary conversion event defined

### 4. Reporting and Dashboards (4: 0C 1I 3N)
(no CRITICAL)

### 5. Marketing Integration (5: 0C 2I 3N)
(no CRITICAL)

### 6. Data and Privacy (5: 0C 2I 3N)
(no CRITICAL)

**Domain total: 28 checkpoints, 3 CRITICAL**

---

## site-structure [UNIVERSAL]

### 1. Page Inventory (6: 2C 3I 1N)
CRITICAL: Complete list of pages/sections | Estimated page count

### 2. Navigation Model (5: 1C 2I 2N)
CRITICAL: Primary navigation items identified

### 3. Information Architecture (5: 2C 1I 2N)
CRITICAL: Logical grouping from user perspective | Key user paths identified

### 4. User Flows (5: 1C 1I 3N)
CRITICAL: Primary user flow: entry to conversion

### 5. Content Hierarchy per Page (4: 0C 3I 1N)
(no CRITICAL)

### 6. Special Structural Needs (5: 0C 3I 2N)
(no CRITICAL)

**Domain total: 30 checkpoints, 6 CRITICAL**

---

## content-strategy [UNIVERSAL]

### 1. Existing Content Inventory (5: 1C 3I 1N)
CRITICAL: What content exists today

### 2. Content Creation Responsibility (6: 1C 4I 1N)
CRITICAL: Who writes the website copy

### 3. Messaging Hierarchy (5: 3C 1I 1N)
CRITICAL: Primary message | Value proposition | Calls to action defined

### 4. Tone and Voice (5: 0C 1I 4N)
(no CRITICAL)

### 5. Content Types and Formats (5: 1C 2I 2N)
CRITICAL: Page types needed

### 6. Content Governance (5: 0C 3I 2N)
(no CRITICAL)

**Domain total: 31 checkpoints, 6 CRITICAL**

---

## design-and-brand [UNIVERSAL]

### 1. Brand Identity Status (5: 2C 3I 0N)
CRITICAL: Logo exists and web-ready | Brand colors defined

### 2. Visual Style Preferences (6: 2C 2I 2N)
CRITICAL: Design direction described | Reference websites the client likes

### 3. Typography (4: 0C 1I 3N)
(no CRITICAL)

### 4. Imagery and Media (6: 0C 4I 2N)
(no CRITICAL)

### 5. Layout and Composition (4: 0C 2I 2N)
(no CRITICAL)

### 6. Responsive Behavior (4: 1C 1I 2N)
CRITICAL: Mobile experience priority level

**Domain total: 29 checkpoints, 5 CRITICAL**

---

## technical-platform [UNIVERSAL]

### 1. CMS / Platform Choice (5: 2C 3I 0N)
CRITICAL: Platform preference or requirement | Who manages the site day-to-day

### 2. Hosting and Infrastructure (5: 0C 3I 2N)
(no CRITICAL)

### 3. Third-Party Integrations (7: 0C 5I 2N)
(no CRITICAL)

### 4. Technical Requirements (5: 1C 2I 2N)
CRITICAL: SSL certificate

### 5. Development Approach (5: 0C 1I 4N)
(no CRITICAL)

### 6. Domain and DNS (5: 1C 2I 2N)
CRITICAL: Domain name confirmed and owned

**Domain total: 32 checkpoints, 4 CRITICAL**

---

## performance [UNIVERSAL]

### 1. Performance Expectations (4: 1C 2I 1N)
CRITICAL: Performance acknowledged as a priority

### 2. Core Web Vitals (4: 0C 2I 2N)
(no CRITICAL)

### 3. Image and Media Optimization (5: 0C 4I 1N)
(no CRITICAL)

### 4. Caching and Delivery (4: 0C 1I 3N)
(no CRITICAL)

### 5. Third-Party Impact (4: 0C 1I 3N)
(no CRITICAL)

### 6. Performance Monitoring (4: 0C 0I 4N)
(no CRITICAL)

**Domain total: 25 checkpoints, 1 CRITICAL**

---

## security-and-compliance [UNIVERSAL]

### 1. Core Security (5: 1C 2I 2N)
CRITICAL: SSL/TLS certificate planned

### 2. Data Protection (6: 2C 1I 3N)
CRITICAL: GDPR compliance required | Privacy policy exists or needs creation

### 3. Cookie Consent (5: 1C 3I 1N)
CRITICAL: Cookie consent mechanism planned

### 4. Industry-Specific Compliance (5: 0C 2I 3N)
(no CRITICAL)

### 5. User Data and Forms (5: 0C 3I 2N)
(no CRITICAL)

### 6. Legal Pages (6: 1C 3I 2N)
CRITICAL: Privacy Policy page

**Domain total: 32 checkpoints, 5 CRITICAL**

---

## forms-and-lead-capture [UNIVERSAL]

### 1. Contact and Inquiry Forms (6: 1C 4I 1N)
CRITICAL: Primary contact form defined

### 2. Call-to-Action Strategy (6: 1C 3I 2N)
CRITICAL: Primary CTA defined

### 3. Lead Flow and Routing (5: 2C 1I 2N)
CRITICAL: Where do form submissions go | Who receives and responds

### 4. CRM and Automation Integration (5: 0C 3I 2N)
(no CRITICAL)

### 5. Newsletter and Email Capture (5: 0C 3I 2N)
(no CRITICAL)

### 6. Form UX and Conversion Optimization (6: 0C 3I 3N)
(no CRITICAL)

**Domain total: 33 checkpoints, 4 CRITICAL**

---

## seo-and-discoverability [UNIVERSAL]

### 1. Search Visibility Goals (5: 1C 3I 1N)
CRITICAL: Is organic search a significant traffic channel

### 2. Keyword Strategy Foundation (5: 1C 2I 2N)
CRITICAL: Primary keyword themes aligned with services

### 3. Technical SEO Requirements (6: 1C 1I 4N)
CRITICAL: Existing URL preservation (301 redirects for redesigns)

### 4. Local SEO (5: 1C 2I 2N)
CRITICAL: Business serves a specific geographic area

### 5. Content and Search Intent (4: 0C 2I 2N)
(no CRITICAL)

### 6. Domain and Migration SEO (5: 2C 1I 2N)
CRITICAL: Domain name confirmed | Redirect plan for URL changes

**Domain total: 30 checkpoints, 6 CRITICAL**

---

## accessibility [UNIVERSAL]

### 1. Compliance Level (4: 1C 3I 0N)
CRITICAL: Target WCAG compliance level defined

### 2. Visual Accessibility (5: 0C 3I 2N)
(no CRITICAL)

### 3. Assistive Technology Support (5: 0C 4I 1N)
(no CRITICAL)

### 4. Content Accessibility (5: 0C 2I 3N)
(no CRITICAL)

### 5. Interactive Accessibility (5: 0C 2I 3N)
(no CRITICAL)

### 6. Testing and Maintenance (5: 0C 0I 5N)
(no CRITICAL)

**Domain total: 29 checkpoints, 1 CRITICAL**

---

## post-launch [UNIVERSAL]

### 1. Maintenance Plan (5: 1C 3I 1N)
CRITICAL: Who handles ongoing maintenance

### 2. Content Updates (5: 1C 3I 1N)
CRITICAL: Who updates content post-launch

### 3. Hosting and Infrastructure Management (5: 0C 4I 1N)
(no CRITICAL)

### 4. Support Arrangement (5: 0C 2I 3N)
(no CRITICAL)

### 5. Growth and Iteration (5: 0C 0I 5N)
(no CRITICAL)

### 6. Documentation and Handover (5: 0C 2I 3N)
(no CRITICAL)

**Domain total: 30 checkpoints, 2 CRITICAL**

---

## CONDITIONAL DOMAINS

---

## ecommerce [CONDITIONAL: Products or services sold directly online]

### 1. Product Catalog (6: 2C 4I 0N)
CRITICAL: Number of products/SKUs | Product types (physical, digital, services, subscriptions)

### 2. Shopping and Checkout (6: 1C 3I 2N)
CRITICAL: Guest checkout or account required

### 3. Payment Processing (6: 2C 3I 1N)
CRITICAL: Payment methods accepted | Payment processor chosen

### 4. Shipping and Fulfillment (6: 1C 3I 2N)
CRITICAL: Shipping zones defined

### 5. Tax and Legal (5: 1C 3I 1N)
CRITICAL: Tax calculation approach

### 6. Inventory and Operations (5: 0C 3I 2N)
(no CRITICAL)

**Domain total: 34 checkpoints, 7 CRITICAL**

---

## blog-and-editorial [CONDITIONAL: Regular content publishing planned]

### 1. Content Publishing Goals (5: 2C 3I 0N)
CRITICAL: Purpose of the blog | Who writes the content

### 2. Blog Structure and Taxonomy (6: 0C 3I 3N)
(no CRITICAL)

### 3. Content Types and Formats (7: 1C 2I 4N)
CRITICAL: Standard articles (text + images)

### 4. Editorial Workflow (5: 0C 3I 2N)
(no CRITICAL)

### 5. Distribution and Engagement (5: 0C 3I 2N)
(no CRITICAL)

### 6. SEO for Blog Content (5: 0C 2I 3N)
(no CRITICAL)

**Domain total: 33 checkpoints, 3 CRITICAL**

---

## multilingual [CONDITIONAL: Site needs more than one language]

### 1. Language Requirements (5: 3C 1I 1N)
CRITICAL: Languages needed | Primary/default language | Content parity across languages

### 2. Translation Approach (5: 1C 3I 1N)
CRITICAL: Professional vs machine vs hybrid translation

### 3. URL and Site Structure (5: 1C 3I 1N)
CRITICAL: URL strategy for languages (subdirectories, subdomains, separate domains)

### 4. Content Management (5: 1C 2I 2N)
CRITICAL: CMS supports multilingual natively or via plugin

### 5. Regional and Cultural Considerations (5: 0C 2I 3N)
(no CRITICAL)

### 6. SEO for Multilingual (5: 0C 2I 3N)
(no CRITICAL)

**Domain total: 30 checkpoints, 6 CRITICAL**

---

## user-accounts [CONDITIONAL: Login, membership, or gated content needed]

### 1. Account Types and Access (5: 3C 1I 1N)
CRITICAL: Types of user accounts needed | What is gated behind login | Free vs paid accounts

### 2. Registration and Authentication (6: 1C 3I 2N)
CRITICAL: Registration flow (self-service, invitation, admin-created)

### 3. Account Management (5: 1C 3I 1N)
CRITICAL: Password reset flow

### 4. Member-Exclusive Content (4: 0C 1I 3N)
(no CRITICAL)

### 5. Subscription and Billing (6: 2C 3I 1N)
CRITICAL: Subscription model | Payment integration for subscriptions

### 6. Security and Privacy (5: 0C 3I 2N)
(no CRITICAL)

**Domain total: 31 checkpoints, 7 CRITICAL**

---

## migration-and-redesign [CONDITIONAL: Existing site to migrate or replace]

### 1. Current Site Assessment (5: 2C 3I 0N)
CRITICAL: Current site URL and platform | Current site CMS access available

### 2. Content Migration (6: 2C 4I 0N)
CRITICAL: Content migration scope | Content that must be preserved exactly

### 3. URL and SEO Preservation (6: 4C 2I 0N)
CRITICAL: Complete URL inventory | 301 redirect plan | High-value pages identified | Domain change involved

### 4. Data Migration (5: 0C 3I 2N)
(no CRITICAL)

### 5. Technical Migration (6: 1C 4I 1N)
CRITICAL: Platform change involved

### 6. Transition Planning (6: 0C 3I 3N)
(no CRITICAL)

**Domain total: 34 checkpoints, 9 CRITICAL**

---

## booking-and-scheduling [CONDITIONAL: Online appointment or reservation functionality]

### 1. Booking Types and Services (5: 1C 3I 1N)
CRITICAL: What can be booked

### 2. Availability and Scheduling (6: 1C 4I 1N)
CRITICAL: Business hours and availability rules defined

### 3. Booking Flow and UX (5: 1C 4I 0N)
CRITICAL: Booking flow steps defined

### 4. Confirmation and Communication (6: 2C 3I 1N)
CRITICAL: Booking confirmation email | Cancellation/rescheduling policy

### 5. Payment and Deposits (5: 1C 2I 2N)
CRITICAL: Payment required at booking

### 6. Integration and Operations (6: 1C 3I 2N)
CRITICAL: Build custom vs embed third-party widget

**Domain total: 33 checkpoints, 7 CRITICAL**

---

## Summary

| Domain | Type | Checkpoints | CRITICAL |
|---|---|---|---|
| business-context | UNIVERSAL | 31 | 15 |
| competitive-landscape | UNIVERSAL | 23 | 5 |
| target-audience | UNIVERSAL | 28 | 6 |
| project-scope | UNIVERSAL | 30 | 3 |
| analytics-and-measurement | UNIVERSAL | 28 | 3 |
| site-structure | UNIVERSAL | 30 | 6 |
| content-strategy | UNIVERSAL | 31 | 6 |
| design-and-brand | UNIVERSAL | 29 | 5 |
| technical-platform | UNIVERSAL | 32 | 4 |
| performance | UNIVERSAL | 25 | 1 |
| security-and-compliance | UNIVERSAL | 32 | 5 |
| forms-and-lead-capture | UNIVERSAL | 33 | 4 |
| seo-and-discoverability | UNIVERSAL | 30 | 6 |
| accessibility | UNIVERSAL | 29 | 1 |
| post-launch | UNIVERSAL | 30 | 2 |
| **Universal subtotal** | | **441** | **72** |
| ecommerce | CONDITIONAL | 34 | 7 |
| blog-and-editorial | CONDITIONAL | 33 | 3 |
| multilingual | CONDITIONAL | 30 | 6 |
| user-accounts | CONDITIONAL | 31 | 7 |
| migration-and-redesign | CONDITIONAL | 34 | 9 |
| booking-and-scheduling | CONDITIONAL | 33 | 7 |
| **Conditional subtotal** | | **195** | **39** |
| **Grand total** | | **636** | **111** |
