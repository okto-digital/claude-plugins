## Phase 6 — Proposal Generation: Methodology

**What this document defines:** The philosophy, rules, and process for turning a concept (Phase 5) into a priced, deliverable proposal. This document describes HOW to think about pricing. All numeric values live in the **Pricing Configuration** spreadsheet.

**Two sources work together:**
- **This file (methodology)** — philosophy, process steps, classification rules, quality checks. Rarely changes.
- **Pricing Configuration** (Google Sheet) — all numeric values, platform multipliers, task hour ranges, third-party costs. Updated when rates change, new platforms are added, or task estimates are refined.

**Pricing spreadsheet URL:** https://docs.google.com/spreadsheets/d/19Gli0d4hKN6C0Klm-XShtkrh9-w6uOFl/edit?usp=sharing&ouid=104410542477327660206&rtpof=true&sd=true

**Separation rule:** If you need to change a number, edit the pricing spreadsheet. If you need to change a rule, edit this file. Never duplicate values between them.

**Input:** Selected concept tier (or all three for comparison proposal), D4-Scope-Implications, D4 confirmed findings, gap analysis platform decision (if resolved), Pricing Configuration spreadsheet (fetched from URL above).

**Output:** A complete proposal document with scope, pricing, timeline, and deliverables.

---

### Proposal structure

The final proposal contains these sections in order:

1. **Executive summary** — the problem, the approach, and the recommended investment (1 page)
2. **Concept brief** — condensed version of the selected concept (sitemap, visual direction, content strategy, functionality). Not the full concept — the highlights that justify the scope.
3. **Scope of work** — the detailed pricing table with all line items (Sections A–F)
4. **Extra services** — optional add-ons priced separately
5. **Timeline** — phased delivery schedule
6. **Terms and conditions** — payment, revisions, ownership, maintenance
7. **Client responsibilities** — what only the client can provide

If presenting all three tiers: a comparison table summarises the differences with per-tier pricing.

---

### Step 1 — Platform decision

Before pricing anything, the platform must be determined. The concept is platform-agnostic — the proposal is not.

**Check D4 for a resolved platform decision.** If the gap analysis already resolved the tech platform (D4-Questions-Agency answered), use that decision.

**If no platform decision exists**, the agent presents capability requirements from the concept's Client Independence dimension and asks the operator to choose. The platform choice affects the entire pricing model — it determines the development multiplier, hosting costs, plugin/licensing costs, and ongoing maintenance model.

---

### Step 2 — Page complexity assessment

Every page in the concept sitemap gets a complexity rating. This is the foundation of all pricing.

#### Complexity levels

Five levels exist: **Homepage**, **Hard**, **Normal**, **Easy**, **Template reuse**. See Pricing Configuration for the specific design hour ranges per level.

#### Assessment rules

The agent assesses complexity based on:

1. **Section count from the concept.** The concept defines exactly how many sections each template has. More sections = higher complexity.
   - 7+ sections → Hard
   - 4–6 sections → Normal
   - 1–3 sections → Easy

2. **Section types.** Some sections are inherently more complex to design:
   - Gallery with interaction → adds complexity
   - Package/pricing cards → adds complexity
   - Multi-step process visual → adds complexity
   - Testimonial cards → standard complexity
   - Text + CTA → simple
   - Hero with segmentation → adds complexity

3. **Template reuse.** If the concept shows multiple pages sharing a template, the first page gets the design complexity rating. Subsequent pages using the same template get "template reuse."

4. **Content variation within shared templates.** If a shared template has content variants that require design adjustments, the variant with the most complex content gets the design rating, and additional variants get Easy.

**Homepage is always homepage complexity.** No exceptions. Even a simple homepage defines the visual system — header, footer, global styles, colour application, typography in practice. Every subsequent template builds on decisions made here.

---

### Step 3 — Development multiplier

The development hours depend on the platform. Applied per page.

#### Formula

```
Page design hours = complexity rating (from Pricing Configuration)
Page development hours = design hours × platform multiplier (from Pricing Configuration)
Page total hours = design hours + development hours
```

**Homepage exception:** The homepage development always includes header, footer, global styles, navigation system, responsive framework, and base component library. This foundational work benefits every subsequent page. The Pricing Configuration specifies the homepage development minimum per platform.

**Important: template pages include their content.** When a page is designed and developed as a template (homepage, hard, normal, easy complexity), the design and development hours include building the page WITH its content — layout, text placement, image handling, section population. Content is part of the template build, not a separate task.

Only **template reuse** pages need separate content placement — these are pages where the template already exists and only content needs to be populated.

---

### Step 4 — Content placement pricing

Content placement pricing only applies to **pages that reuse an existing template** — pages where the layout already exists and only new or migrated content needs to be placed into it.

#### What goes into content placement

**Template reuse pages** — the template is built (and priced) on the first page that uses it. Subsequent pages using the same template need:
- Content sourcing (from existing site, client, or new creation)
- Content formatting to fit the template structure
- Image selection and optimisation
- On-page SEO (meta title, description, heading optimisation)
- Quality check

**New content on existing template** — a page that didn't exist on the old site but uses a template built for another page. The template exists — the content is new and needs to be created and placed.

#### Placement complexity

Three levels exist: **Simple**, **Moderate**, **Complex**. See Pricing Configuration for hour ranges per level.

#### What does NOT go into content placement

- **Template pages** (homepage, hard, normal, easy complexity) — content is included in design/development hours
- **New pages that need full copywriting** — these go into Extra Services (copywriting)
- **Pages where the client provides all content** — these go into Client Responsibilities

---

### Step 5 — Functionality pricing

**Critical rule: if a feature is part of a template page, it's already included in that page's design and development hours.** The contact form on the Contact page is designed and developed as part of the Contact page template. The portfolio gallery on the Service page is part of the Service page template. The blog system on WordPress is native — the blog index and blog detail templates already cover it.

Functionality as a **separate pricing section** only applies to features that exist **outside of or in addition to the page templates.**

#### What IS separately priced functionality

| Type | Examples | Why separate |
|---|---|---|
| **External integrations** | CRM connection, email marketing sync, ERP integration, payment gateway, external booking system API | These connect the website to external systems. The complexity is in the integration, authentication, data mapping, and error handling — not in the page template. |
| **Custom interactive tools** | Quote calculator, project configurator, ROI estimator, interactive comparison tool | These are standalone applications embedded in the site. Their logic, UI, and testing are independent of the page template they sit on. |
| **Site-wide features** | Advanced search with filtering, multi-language switcher with content sync, user authentication/portal system, e-commerce cart and checkout | These span multiple pages and require their own architecture. Not tied to a single template. |
| **Third-party platform setup** | WooCommerce, LMS, membership system | These are platforms within the platform — they add significant architectural complexity beyond individual pages. |

#### What is NOT separately priced (included in templates)

| Feature | Where it's priced | Why |
|---|---|---|
| Contact form | Contact page template | The form is the primary component of the contact page — designed and built as part of that template |
| Portfolio gallery with lightbox | Service page template | The gallery is a core section of the service page |
| Testimonial display | Homepage and Service page templates | Testimonial cards are a section within those templates |
| Blog post listing + filtering | Blog index template | This is what the blog index template IS |
| FAQ accordion | Service page template | A section within the service page template |
| Image lazy loading | Overall development | Applied site-wide during development, not a standalone feature |
| Sticky header / mobile navigation | Homepage template (global components) | Part of the header/navigation system built during homepage development |

**Agent assessment rule:** Before adding ANY feature to the functionality pricing section, check: is this feature already a section in one of the page templates? If yes → it's included in the template hours. If no → price it separately. When in doubt, if the feature lives on one page and is the primary purpose of a section on that page, it's a template feature.

See Pricing Configuration for hour estimates per feature type and platform.

---

### Step 6 — Tasks and migrations pricing

Everything from D4-Scope-Implications and the concept's "Things to do (included)" section that isn't design, development, or functionality. Categories include: analytics and tracking, compliance, SEO foundation, infrastructure, launch and QA.

See Pricing Configuration for the full task library with hour estimates per task.

---

### Step 7 — Platform add-on pricing

If the platform is decided before the proposal, calculate directly using the platform multiplier in Section A. No separate add-on line needed.

If the platform is NOT decided, price the base at static HTML (the simplest implementation) and show platform options as add-ons. This makes the platform cost visible to the client.

See Pricing Configuration for platform multipliers and add-on calculations.

---

### Step 8 — Extra services pricing

Optional items from the concept's "Things to do (optional)" section, plus services the agent identifies from evidence.

#### Service identification

The agent scans the following sources:

**From the concept:**
- Things to do (optional) section — directly listed items

**From D4-Scope-Implications:**
- Items marked as optional or separately priced

**From research findings (via baseline-log):**
- Keyword research → deeper SEO strategy, content marketing plan
- Reputation findings → review acquisition strategy, social media alignment
- Content analysis → copywriting, editorial calendar, ongoing blog production
- UX findings → user testing, A/B testing setup
- Competitor landscape → competitive monitoring, quarterly tracking
- Market context → Google Business Profile, paid advertising, email marketing

#### Assessment rules

- Only include services relevant to this specific project based on evidence
- Don't pad the list — every service must connect to a research finding or gap analysis item
- Price recurring services as monthly or quarterly, always stating the per-period hours
- Third-party costs listed separately from hours
- Always note whether a service is one-time or recurring

See Pricing Configuration for hour estimates per service type.

---

### Step 9 — Proposal assembly

For each concept tier, the proposal presents a complete pricing breakdown across six sections:

**Section A — Design and development (templates and pages)**

All template pages with their design and development hours. This includes all content, interactive features, and components that are part of each template. The template IS the deliverable — form on the contact page, gallery on the service page, blog functionality — all included here.

| Page | Template | Complexity | Design (hrs) | Development (hrs) | Total (hrs) |
|---|---|---|---|---|---|
| {each page from concept sitemap} | | | | | |
| **Subtotal A** | | | **design total** | **dev total** | **section total** |

**Section B — Content placement (template reuse pages only)**

Only pages that reuse an existing template and need content populated. Template pages (homepage, hard, normal, easy) are NOT in this section — their content is included in Section A.

| Page | Template source | Placement type | Hours |
|---|---|---|---|
| {each template reuse page needing content} | | | |
| **Subtotal B** | | | **placement total** |

**Section C — External functionality** (may be empty)

Only features that exist outside of page templates. If all interactive features are part of page templates, this section states "All functionality included in template development (Section A)."

| Feature | Hours | Third-party cost | Notes |
|---|---|---|---|
| {each external feature, if any} | | | |
| **Subtotal C** | | | **functionality total** |

**Section D — Tasks and migrations**

Everything from D4-Scope-Implications: analytics, compliance, SEO foundation, infrastructure, performance optimisation. These are project tasks, not page-level work.

| Task | Category | Hours | Third-party cost |
|---|---|---|---|
| {each task} | | | |
| **Subtotal D** | | **task total** | **cost total** |

**Section E — Platform** (conditional)

Only if the base price uses static HTML and platform is presented as an option. If platform is already decided, this section doesn't exist — the platform multiplier is already applied in Section A.

**Section F — Project management**

Coordination, communication, client meetings, internal reviews, timeline management, QA oversight. Calculated as a percentage of total project hours (Sections A–D). See Pricing Configuration for the PM percentage.

**TOTAL = A + B + C + D + (E if applicable) + F**

#### Extra services menu

Presented separately from the core project pricing. The client can add any combination.

#### Tier comparison table (if presenting all three tiers)

Shows per-tier: pages, templates, design hours, development hours, content placement hours, external functionality hours, tasks hours, PM hours, total hours, project investment, platform cost, recommended extras.

---

### Step 10 — Timeline generation

Based on total hours per section and typical team allocation.

#### Timeline rules

- Design and development overlap — development starts on pages whose design is approved while remaining pages are still in design
- Content migration runs parallel with development
- Functionality development runs parallel with page development
- Tasks and migrations can start early (analytics, compliance setup) and finish late (redirects at launch)
- QA and launch is always the final phase
- Timeline scales with tier: more pages and templates = longer design and development phases

#### Timeline phases

Standard phases: Discovery and kickoff → Design → Development → Content and migration (parallel with dev) → Testing and QA → Launch → Post-launch.

The agent determines week counts based on the total hours in each section and reasonable team allocation (1-2 designers, 1-2 developers working in parallel).

---

### Agent assessment intelligence

The agent must make judgment calls on complexity and hours. These rules guide consistent assessment.

#### Complexity assessment heuristics

**A page is "hard" when:**
- It has 6+ sections in the concept
- It contains interactive sections (gallery with navigation, pricing cards with comparison, multi-step process visual)
- It serves as the primary landing for a high-volume keyword cluster
- It has content variants that require significant layout adaptation

**A page is "normal" when:**
- It has 4–5 sections
- Sections are primarily text-based with standard components (text blocks, image + text, card grids, forms)
- It follows patterns established by the homepage and hard templates

**A page is "easy" when:**
- It has 1–3 sections
- It's primarily text content (blog posts, policies, FAQ)
- It reuses component patterns from other templates with minor adaptation

**A page is "template reuse" when:**
- It uses an already-designed template with zero or near-zero design changes
- Only the content differs (regional landings 2–4, policy pages 2–4)

#### Hours validation

The agent should verify its estimates against the sanity check ranges in the Pricing Configuration. If the estimate falls significantly outside those ranges, review complexity assessments.

#### Senior professional assumption

All hour estimates assume senior professionals. If the team includes junior members, the proposal should note this and adjust hours upward. See Pricing Configuration for the junior-to-senior conversion factor.

---

### Quality checks before delivery

Before finalising the proposal, the agent verifies:

1. **Every page from the concept sitemap appears in Section A.** No page is missing, no page is double-counted.

2. **Template reuse is correctly applied.** If the concept shows 4 regional pages on one template, only the first gets the full design complexity. The other 3 are template reuse in Section A + content placement in Section B.

3. **Content placement (Section B) only contains template reuse pages.** Template pages (homepage, hard, normal, easy) are NOT in Section B — their content is included in Section A. If a template page appears in Section B, something is double-counted.

4. **No template-included features appear in Section C.** If the contact form is part of the Contact page template, it must NOT also appear as a separate functionality line item. Section C only contains external integrations and standalone tools. If Section C is empty, that's correct for many projects.

5. **Every item from D4-Scope-Implications appears** either in Section D (tasks — included) or in Extra Services (optional). Nothing from the scope implications was dropped.

6. **Third-party costs are separated from hours.** Plugin licenses, platform subscriptions, stock photo costs — these are separate line items, not hidden in hourly estimates.

7. **The tier comparison table (if presenting all three) shows clear, honest differentiation.** Tier 1 is not artificially thin to make Tier 2 look better. Tier 3 is not artificially inflated to make Tier 2 look reasonable. Each tier is a genuine, standalone business proposition.

8. **The total hours pass the sanity check.** Cross-reference against the ranges in the Pricing Configuration for this project size.

9. **Every extra service connects to a research finding.** No padding. If "advanced SEO strategy" is listed as an extra, the proposal should reference which research finding makes it relevant.

10. **The floor rule holds.** Even Tier 1 addresses every critical problem the research identified. If the cheapest option doesn't fix the accessibility score, add the migration, or set up analytics — it fails the floor test and needs to be revised.

11. **Blog detail template is not forgotten.** If the concept includes a blog, both the blog index template AND the blog post detail template must be priced. A blog index without a post template is incomplete.

12. **No double-counting across sections.** The most common error: a feature priced in Section A (as part of a template) AND in Section C (as functionality), or content priced in Section A (as part of template build) AND in Section B (as content placement). Each deliverable appears in exactly one section.

---

### Key decisions

**Why the pricing table is broken into sections A–F:**
The client sees exactly where their money goes. Templates, content placement, external functionality, tasks, and platform are different types of work with different cost drivers. Lumping them into one number hides the structure. Breaking them out builds trust and makes scope changes easy — "if we drop the blog, we save X hours from Section A."

**Why template pages include their content:**
When a designer builds a service page template, they design it WITH real content — real headlines, real images, real copy in the sections. The developer implements the same. The template IS the page with its content. Pricing design/development separately from "content population" for template pages would either double-count the work or create an artificial split where the designer builds empty boxes and someone else fills them — that's not how professional web design works.

**Why content placement only covers template reuse pages:**
The only pages where content population is genuinely separate work are pages where the template already exists. Regional landing page #2 uses the template built for regional landing page #1 — the template design and development is done. What remains is placing unique content into the existing structure. This is editorial work (content selection, formatting, SEO optimisation), not design or development.

**Why functionality is strictly scoped to external features:**
A contact form on the contact page is not "form functionality plus a contact page." It's one thing — a contact page template that includes a form. The form's design, validation, routing, and styling are part of building that template. Pricing the form separately would inflate the proposal with phantom line items. External integrations (CRM, booking APIs, payment gateways) are genuinely separate because their complexity is independent of any single page template.

**Why the development multiplier is platform-dependent:**
The same design converts to different development effort depending on the platform. The multiplier makes this transparent and lets the client see the platform cost directly.

**Why extra services are presented as a separate menu:**
The core proposal is the website. Extras are genuine options the client can add, defer, or handle themselves. Mixing them into the core price inflates the number and makes the proposal compete poorly against agencies that don't include them. Separating them shows the core investment clearly while demonstrating the range of additional value the agency can provide.

**Why the base price can use static HTML as the floor:**
Static is the simplest implementation. Every other platform adds complexity. Using static as the base makes the platform cost visible. This helps clients who might later say "can we do this cheaper?" — the answer is "yes, on a simpler platform, here's the difference." It also makes cross-platform quoting easy: same base, different add-on.
