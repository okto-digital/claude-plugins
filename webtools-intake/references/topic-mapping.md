# Topic Mapping: Conversation Topics for Meeting Mode

**Purpose:** Maps the 21 technical domain checklists to 9 conversation topics that match how client meetings naturally flow. The brief-generator agent uses this mapping in MEETING mode to navigate the interview, track coverage, and suggest questions grouped by topic instead of by technical domain.

**Usage:** The agent reads this file at session start alongside the domain files. In MEETING mode, all gap tracking, suggestions, and coverage reporting use conversation topics -- never raw domain names.

---

## Core Conversation Topics

These 9 topics represent how website project discussions flow in a real meeting. The order reflects the most natural conversation sequence, but the agent adapts to whatever order the client actually discusses things.

### 1. The Business

**Domains:** business-context, competitive-landscape

**What this covers:** Who the client is, what they do, who they compete with, what makes them different, how they make money.

**Why it comes first:** Every other decision depends on understanding the business. This is where most meetings start naturally.

**Typical meeting time:** 10-15 minutes

**CRITICAL checkpoints to watch for:**
- Company identity (name, industry, location, model)
- Core offering and value proposition
- Key differentiators from competitors
- Revenue model and how the website supports it
- Primary point of contact and decision-maker

---

### 2. The Audience

**Domains:** target-audience

**What this covers:** Who visits the website, what they need, how they find the business, what hesitations they have, what convinces them.

**Why it follows The Business:** Once you know who the business is, the next question is who they serve.

**Typical meeting time:** 8-12 minutes

**CRITICAL checkpoints to watch for:**
- Primary audience identified (role, demographics, or segment)
- Core audience needs the site must address
- Key hesitations or objections before converting
- How the audience currently finds the business

---

### 3. Goals and Success

**Domains:** project-scope (goals, timeline, budget portions), analytics-and-measurement

**What this covers:** What the website needs to achieve, how success is measured, what the budget and timeline look like, what KPIs matter.

**Why here:** After business and audience, the meeting naturally turns to "so what do you actually want this website to do?"

**Typical meeting time:** 8-10 minutes

**CRITICAL checkpoints to watch for:**
- Primary website purpose (lead gen, sales, brand, support)
- Top 3 specific goals
- Definition of success at 6 months
- Budget range
- Target launch date
- Primary KPIs

---

### 4. The Website Vision

**Domains:** site-structure, content-strategy

**What this covers:** What pages the site needs, how it should be organized, what content exists, who creates content, what the messaging hierarchy looks like.

**Why here:** With goals defined, the conversation turns to what the website actually looks like in terms of pages and content.

**Typical meeting time:** 10-15 minutes

**CRITICAL checkpoints to watch for:**
- Complete page list (at least the main pages)
- Navigation model (how users move through the site)
- Content creation responsibility (client, agency, or shared)
- Key messages that must appear on the site

---

### 5. Look and Feel

**Domains:** design-and-brand

**What this covers:** Brand identity, visual style, imagery preferences, typography, responsive behavior, examples of admired websites.

**Typical meeting time:** 5-10 minutes

**CRITICAL checkpoints to watch for:**
- Brand guidelines status (existing, in progress, none)
- Visual style direction (adjectives, reference sites)
- Logo and brand assets availability

---

### 6. Technical Foundation

**Domains:** technical-platform, performance, security-and-compliance

**What this covers:** CMS/platform choice, hosting, integrations, speed requirements, compliance needs (GDPR, accessibility, industry-specific), security.

**Note:** This topic contains the most technical checkpoints. In MEETING mode, questions should be translated to business language. Example: "Core Web Vitals" becomes "How fast should the website load?"

**Typical meeting time:** 8-12 minutes

**CRITICAL checkpoints to watch for:**
- Platform preference or constraint (WordPress, Shopify, custom, etc.)
- Third-party integrations needed (CRM, email, accounting, etc.)
- Hosting arrangement (client provides, agency manages, or needs setup)
- GDPR compliance applicability
- SSL/security requirements

---

### 7. Lead Capture and Conversion

**Domains:** forms-and-lead-capture, analytics-and-measurement (conversion tracking subset)

**What this covers:** How visitors become customers -- contact forms, CTAs, lead flows, follow-up automation, conversion tracking.

**Typical meeting time:** 5-8 minutes

**CRITICAL checkpoints to watch for:**
- Primary conversion action (form submission, phone call, purchase, signup)
- Form types needed (contact, quote request, newsletter, etc.)
- CRM or email marketing integration for lead follow-up
- Conversion tracking setup

---

### 8. Findability

**Domains:** seo-and-discoverability, accessibility

**What this covers:** How people find the site (SEO, local search, directories), how accessible it is for people with disabilities.

**Note:** Clients rarely bring up SEO or accessibility unprompted. The agent should suggest this topic if it hasn't been discussed, but the questions should focus on outcomes: "Do you want to show up when people search for [their service]?" rather than "What's your keyword strategy?"

**Typical meeting time:** 5-8 minutes

**CRITICAL checkpoints to watch for:**
- Whether SEO is a priority (organic search matters for this business)
- Target keywords or search terms (even if informal)
- Local SEO needs (physical location, service area)
- Accessibility requirements (legal, ethical, or contractual)

---

### 9. After Launch

**Domains:** post-launch

**What this covers:** Who maintains the site after launch, content update process, hosting management, support arrangement, monitoring.

**Why last:** This is naturally the closing topic of a meeting -- "what happens after we build this?"

**Typical meeting time:** 3-5 minutes

**CRITICAL checkpoints to watch for:**
- Who updates content after launch (client self-service, agency retainer, or hybrid)
- Hosting and domain management responsibility
- Support arrangement expectations

---

## Conditional Topic Extensions

These topics are activated when the corresponding conditional domains become applicable. They attach to existing core topics rather than creating new standalone topics.

| Extension | Attaches To | Domain | Activated When |
|---|---|---|---|
| **Online Store** | Technical Foundation + Lead Capture | ecommerce | Products or services sold directly online |
| **Content Publishing** | The Website Vision | blog-and-editorial | Regular content publishing planned (blog, news, articles) |
| **Multiple Languages** | Technical Foundation | multilingual | Site needs more than one language |
| **Member Access** | Technical Foundation + Lead Capture | user-accounts | Login, membership, or gated content needed |
| **Moving From Current Site** | Technical Foundation | migration-and-redesign | Existing site to migrate or replace |
| **Bookings and Appointments** | Lead Capture | booking-and-scheduling | Online appointment or reservation functionality |

**How extensions work in MEETING mode:**

When a conditional domain becomes active (either from inquiry form data or during the meeting), the agent:
1. Adds the extension's checkpoints to the parent topic's suggestion queue
2. Announces the activation briefly: "Online Store added to discussion topics."
3. When the parent topic comes up, extension questions are woven in naturally
4. Extension checkpoints appear in the coverage dashboard under their parent topic

**Example:** If e-commerce is active, when the operator reaches "Technical Foundation" or "Lead Capture," the suggestion queue includes product catalog, payment, shipping, and inventory questions alongside the standard technical and conversion questions.

---

## Default Conversation Flow Order

The recommended order for a typical 60-90 minute meeting:

```
1. The Business .................. 10-15 min
2. The Audience .................. 8-12 min
3. Goals and Success ............. 8-10 min
4. The Website Vision ............ 10-15 min
5. Look and Feel ................. 5-10 min
6. Technical Foundation .......... 8-12 min
   + Online Store extension ...... +8-12 min (if applicable)
   + Multiple Languages ext. ..... +3-5 min (if applicable)
   + Moving From Current Site .... +5-8 min (if applicable)
   + Member Access extension ..... +3-5 min (if applicable)
7. Lead Capture and Conversion ... 5-8 min
   + Bookings extension .......... +3-5 min (if applicable)
8. Findability ................... 5-8 min
9. After Launch .................. 3-5 min
```

**Total base meeting:** ~62-95 minutes
**With all extensions:** ~78-130 minutes

The agent uses this order for "next topic" suggestions but adapts to the actual conversation flow. If the client jumps to a later topic, the agent follows.

---

## Reverse Mapping: Domain to Topic

For checkpoint scoring, the agent needs to know which topic each domain belongs to:

| Domain File | Topic | Extension? |
|---|---|---|
| business-context.md | The Business | No |
| competitive-landscape.md | The Business | No |
| target-audience.md | The Audience | No |
| project-scope.md | Goals and Success | No |
| analytics-and-measurement.md | Goals and Success + Lead Capture | No (split) |
| site-structure.md | The Website Vision | No |
| content-strategy.md | The Website Vision | No |
| design-and-brand.md | Look and Feel | No |
| technical-platform.md | Technical Foundation | No |
| performance.md | Technical Foundation | No |
| security-and-compliance.md | Technical Foundation | No |
| forms-and-lead-capture.md | Lead Capture and Conversion | No |
| seo-and-discoverability.md | Findability | No |
| accessibility.md | Findability | No |
| post-launch.md | After Launch | No |
| ecommerce.md | Technical Foundation + Lead Capture | Yes: Online Store |
| blog-and-editorial.md | The Website Vision | Yes: Content Publishing |
| multilingual.md | Technical Foundation | Yes: Multiple Languages |
| user-accounts.md | Technical Foundation + Lead Capture | Yes: Member Access |
| migration-and-redesign.md | Technical Foundation | Yes: Moving From Current Site |
| booking-and-scheduling.md | Lead Capture and Conversion | Yes: Bookings and Appointments |

**Split domains:** analytics-and-measurement has checkpoints that belong to both "Goals and Success" (KPIs, baseline metrics, reporting) and "Lead Capture" (conversion events, tracking setup). The agent assigns individual checkpoints to the most relevant topic. Similarly, e-commerce and user-accounts checkpoints span Technical Foundation and Lead Capture.
