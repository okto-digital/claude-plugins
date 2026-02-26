# Inference Rules: Real-Time Confidence Engine

**Purpose:** Codified inference patterns that the brief-generator agent uses to derive conclusions from client input. Instead of asking every question, the agent matches input against these rules to propose answers with confidence levels. Rules are applied continuously during MEETING mode and in batch during REVIEW mode.

**Usage:** The agent reads this file at session start. During input processing, each new data point triggers a scan of applicable rules. Matching rules produce inferences that are scored, queued, and surfaced according to the mode's behavior profile.

---

## Confidence Level Definitions

### HIGH (auto-accept, surface immediately)

The inference is a near-certainty based on strong logical necessity or universal convention. Wrong less than 10% of the time.

**Criteria (any one is sufficient):**
- Universal industry standard (e.g., SSL for all websites)
- Legal requirement triggered by explicit conditions (e.g., GDPR for EU businesses collecting personal data)
- Direct logical implication (e.g., "redesign" implies existing site exists)
- Multiple explicit data points converge on the same conclusion

**Action in MEETING mode:** Surface immediately in the acknowledgment. Auto-include in the brief. Operator can override but is not asked to confirm.

**Action in REVIEW mode:** Listed in "auto-resolved" section. Operator reviews in batch.

### MEDIUM (propose for confirmation)

The inference is reasonable and likely correct, but could be wrong in some cases. Correct roughly 60-85% of the time.

**Criteria:**
- Strong industry convention (not universal but common)
- Two or more indirect data points pointing to the same conclusion
- Reasonable default for the project type, business model, or industry
- Cross-domain implication where the connection is plausible but not certain

**Action in MEETING mode:** Queue silently. Surface only when the operator asks for suggestions or when the topic is active.

**Action in REVIEW mode:** Listed in "proposed solutions" section. Operator confirms, corrects, or defers to client.

### LOW (ask the question)

The inference is a guess. Multiple valid answers exist with no strong contextual preference. Correct less than 50% of the time.

**Criteria:**
- Single indirect data point with multiple possible interpretations
- No industry convention (highly business-specific decision)
- Contradictory signals in the input
- Truly subjective preference (e.g., visual style, brand tone)

**Action in MEETING mode:** Queue as a question in the suggestion queue. Do not surface as a proposal.

**Action in REVIEW mode:** Listed in "questions" section. Goes to D13 if not resolved by operator.

---

## Confidence Progression

Inferences can upgrade as more data arrives:

```
LOW  -->  MEDIUM  (corroborating data point added)
MEDIUM  -->  HIGH  (third data point or explicit statement)
Any  -->  EXPLICIT  (client or operator directly confirms)
```

The agent tracks the inference trail: which data points contributed to each inference and when. This is useful in REVIEW mode when showing the operator how a conclusion was reached.

---

## Universal Safe Defaults

These inferences apply to ALL projects regardless of type, industry, or scope. They are always HIGH confidence.

| Inference | Confidence | Covers Checkpoint |
|---|---|---|
| SSL/TLS certificate required | HIGH | security-and-compliance / Core Security / SSL |
| Mobile responsive design required | HIGH | design-and-brand / responsive behavior |
| Privacy policy page needed | HIGH | security-and-compliance / Legal Pages / Privacy Policy |
| HTTPS on all pages | HIGH | security-and-compliance / Core Security / SSL |
| Spam protection on forms | HIGH | security-and-compliance / User Data and Forms / Spam protection |
| Software update plan needed | HIGH | security-and-compliance / Core Security / Update plan |
| Backup strategy needed | HIGH | security-and-compliance / Core Security / Backup strategy |

---

## Geographic Inference Rules

### Rule: EU-Based Business

**Trigger:** Business location is in an EU/EEA country, OR target audience includes EU visitors, OR shipping to EU countries.

**Inferences:**

| Inference | Confidence | Checkpoint |
|---|---|---|
| GDPR compliance required | HIGH | security-and-compliance / Data Protection / GDPR |
| Cookie consent mechanism needed | HIGH | security-and-compliance / Cookie Consent / mechanism |
| Cookie categories must be defined | MEDIUM | security-and-compliance / Cookie Consent / categories |
| Data Processing Agreements needed with vendors | MEDIUM | security-and-compliance / Data Protection / DPA |
| Right to erasure capability needed | MEDIUM | security-and-compliance / User Data / deletion capability |
| Privacy policy must include GDPR-specific clauses | HIGH | security-and-compliance / Legal Pages / Privacy Policy |

### Rule: DACH Region (Germany, Austria, Switzerland)

**Trigger:** Business located in Germany, Austria, or Switzerland.

**Additional inferences (on top of EU rules):**

| Inference | Confidence | Checkpoint |
|---|---|---|
| Impressum / Legal Notice page required | HIGH | security-and-compliance / Legal Pages / Impressum |
| Cookie consent must be opt-in (not opt-out) | HIGH | security-and-compliance / Cookie Consent / mechanism |

### Rule: Benelux Region

**Trigger:** Business located in Netherlands, Belgium, or Luxembourg.

| Inference | Confidence | Checkpoint |
|---|---|---|
| iDEAL payment support likely needed (if e-commerce) | MEDIUM | ecommerce / Payment Processing / methods |
| Bancontact support likely needed (if Belgium + e-commerce) | MEDIUM | ecommerce / Payment Processing / methods |
| Dutch and/or French language may be relevant (Belgium) | LOW | multilingual domain applicability |

### Rule: US-Based or US-Targeting

**Trigger:** Business located in the US or explicitly targeting US audience.

| Inference | Confidence | Checkpoint |
|---|---|---|
| CCPA/CPRA compliance may be required (California visitors) | MEDIUM | security-and-compliance / Data Protection / CCPA |
| ADA accessibility compliance may be required | MEDIUM | accessibility / legal requirements |

---

## Business Model Inference Rules

### Rule: B2B Model

**Trigger:** Client describes business as B2B, or target audience is businesses/companies.

| Inference | Confidence | Checkpoint |
|---|---|---|
| Longer sales cycle than B2C | MEDIUM | target-audience / decision journey |
| Multiple stakeholders involved in purchase decisions | MEDIUM | target-audience / decision process |
| Case studies / testimonials important for trust | MEDIUM | content-strategy / social proof |
| LinkedIn as primary social channel | MEDIUM | content-strategy / distribution |
| Net-30 or invoice payments possible (if e-commerce) | LOW | ecommerce / Payment Processing / invoice |
| Quote request flow may be needed instead of direct cart | MEDIUM | forms-and-lead-capture / form types |
| Account/portal for order history likely useful (if e-commerce) | MEDIUM | user-accounts domain applicability |
| Pricing page likely needed | MEDIUM | site-structure / page list |

### Rule: B2C Model

**Trigger:** Client describes business as B2C, or target audience is consumers.

| Inference | Confidence | Checkpoint |
|---|---|---|
| Faster purchasing decisions | MEDIUM | target-audience / decision journey |
| Social proof (reviews, ratings) very important | MEDIUM | content-strategy / social proof |
| Guest checkout preferred (if e-commerce) | MEDIUM | ecommerce / Shopping and Checkout / guest checkout |
| Instagram/TikTok may be relevant social channels | LOW | content-strategy / distribution |
| SEO likely high priority (consumers search online) | MEDIUM | seo-and-discoverability / priority |

### Rule: E-commerce Active

**Trigger:** Products or services sold directly online.

| Inference | Confidence | Checkpoint |
|---|---|---|
| Payment processor needed | HIGH | ecommerce / Payment Processing / processor |
| Product catalog structure needed | HIGH | ecommerce / Product Catalog / categories |
| Shipping strategy needed (physical goods) | HIGH | ecommerce / Shipping / zones |
| Tax calculation needed | HIGH | ecommerce / Tax and Legal / tax approach |
| Returns/refund policy needed | MEDIUM | ecommerce / Tax and Legal / returns policy |
| Terms and conditions for online sales needed | MEDIUM | security-and-compliance / Legal Pages / Terms |
| Conversion tracking important | HIGH | analytics-and-measurement / conversion events |
| PCI-DSS compliance approach needed | MEDIUM | security-and-compliance / Industry-Specific / PCI-DSS |
| Order notification workflow needed | MEDIUM | ecommerce / Inventory / notification |

---

## Project Type Inference Rules

### Rule: Redesign / Migration

**Trigger:** Project type is redesign, or client mentions existing website, or "replacing current site."

| Inference | Confidence | Checkpoint |
|---|---|---|
| migration-and-redesign domain is ACTIVE | HIGH | domain applicability |
| Existing site URL must be documented | HIGH | migration / Current Site / URL |
| Content migration scope must be defined | HIGH | migration / Content Migration / scope |
| 301 redirect plan needed | HIGH | migration / URL and SEO / redirects |
| Current site analytics should be reviewed | MEDIUM | migration / Current Site / baseline |
| High-value pages must be identified | HIGH | migration / URL and SEO / high-value pages |
| Domain may stay the same (if not explicitly changing) | MEDIUM | migration / URL and SEO / domain change |
| Platform change may be involved | LOW | migration / Technical / platform change |

### Rule: New Build (No Existing Site)

**Trigger:** Project type is new-build, or client has no current website.

| Inference | Confidence | Checkpoint |
|---|---|---|
| migration-and-redesign domain is INACTIVE | HIGH | domain applicability |
| SEO starts from scratch (no existing rankings to preserve) | HIGH | seo / starting position |
| All content must be created new | HIGH | content-strategy / existing content |
| Domain may need to be registered | LOW | technical-platform / domain status |

### Rule: Landing Page

**Trigger:** Project type is landing-page.

| Inference | Confidence | Checkpoint |
|---|---|---|
| Single page or very few pages | HIGH | site-structure / page count |
| Single conversion goal | HIGH | forms-and-lead-capture / primary CTA |
| Campaign-driven traffic likely | MEDIUM | analytics-and-measurement / traffic source |
| SEO less relevant (paid traffic focus) | MEDIUM | seo / priority level |
| blog-and-editorial domain is INACTIVE | HIGH | domain applicability |
| user-accounts domain is INACTIVE | HIGH | domain applicability |

---

## Industry Inference Rules

### Rule: Restaurant / Hospitality

**Trigger:** Industry is restaurant, cafe, bar, hotel, hospitality.

| Inference | Confidence | Checkpoint |
|---|---|---|
| Menu page needed | HIGH | site-structure / page list |
| booking-and-scheduling domain likely ACTIVE | MEDIUM | domain applicability |
| Location map important | HIGH | site-structure / local features |
| Photography very important (food, ambiance) | HIGH | design-and-brand / imagery |
| Local SEO critical | HIGH | seo / local SEO |
| Google Business Profile integration | MEDIUM | seo / local SEO |
| Opening hours prominent | HIGH | site-structure / key content |
| Mobile important (searching while out) | HIGH | design-and-brand / mobile priority |

### Rule: Professional Services (Law, Accounting, Consulting)

**Trigger:** Industry is law firm, accounting, consulting, professional services.

| Inference | Confidence | Checkpoint |
|---|---|---|
| Trust and credibility are primary design goals | HIGH | design-and-brand / visual direction |
| Team/partner bios page needed | MEDIUM | site-structure / page list |
| Case studies or client testimonials important | MEDIUM | content-strategy / social proof |
| Client confidentiality considerations | MEDIUM | security-and-compliance / Industry-Specific / legal |
| B2B model likely (but not always) | MEDIUM | business-context / business model |
| Contact form as primary conversion | MEDIUM | forms-and-lead-capture / primary CTA |

### Rule: SaaS / Software

**Trigger:** Industry is SaaS, software, technology product.

| Inference | Confidence | Checkpoint |
|---|---|---|
| Pricing page needed | HIGH | site-structure / page list |
| Demo or free trial CTA likely | MEDIUM | forms-and-lead-capture / primary CTA |
| Documentation section possible | LOW | site-structure / page list |
| user-accounts domain likely ACTIVE | MEDIUM | domain applicability |
| Integration/API page possible | LOW | site-structure / page list |
| Competitor comparison page useful | MEDIUM | site-structure / page list |
| Performance and uptime important messaging | MEDIUM | content-strategy / key messages |

### Rule: Healthcare

**Trigger:** Industry is healthcare, medical, dental, wellness.

| Inference | Confidence | Checkpoint |
|---|---|---|
| HIPAA compliance may be required (if US) | MEDIUM | security-and-compliance / Industry-Specific / HIPAA |
| Patient privacy critical | HIGH | security-and-compliance / data protection |
| booking-and-scheduling domain likely ACTIVE | MEDIUM | domain applicability |
| Accessibility extra important | HIGH | accessibility / compliance level |
| Trust signals critical (credentials, certifications) | HIGH | design-and-brand / trust elements |

### Rule: E-commerce / Retail

**Trigger:** Industry is retail, online store, shop (distinct from e-commerce domain activation).

| Inference | Confidence | Checkpoint |
|---|---|---|
| Product photography critical | HIGH | design-and-brand / imagery |
| Search and filtering important | MEDIUM | site-structure / navigation |
| Reviews/ratings important | MEDIUM | content-strategy / social proof |
| Seasonal promotions likely | MEDIUM | business-context / seasonality |
| Email marketing integration likely | MEDIUM | forms-and-lead-capture / email integration |

### Rule: Education

**Trigger:** Industry is education, training, courses, school, university.

| Inference | Confidence | Checkpoint |
|---|---|---|
| Course catalog or program listing needed | HIGH | site-structure / page list |
| Application/enrollment form likely | MEDIUM | forms-and-lead-capture / form types |
| user-accounts domain possible (student portal) | LOW | domain applicability |
| FERPA compliance possible (if US) | LOW | security-and-compliance / Industry-Specific / FERPA |
| Calendar/events page likely | MEDIUM | site-structure / page list |

---

## Cross-Domain Inference Rules

These rules derive conclusions by combining information from different domains.

### Rule: Budget Constrains Scope

**Trigger:** Budget range is known.

| Budget Range | Inference | Confidence |
|---|---|---|
| Under 5,000 EUR | Phased approach recommended | MEDIUM |
| Under 5,000 EUR | Template-based design likely | MEDIUM |
| Under 5,000 EUR | Limited custom functionality | MEDIUM |
| 5,000 - 15,000 EUR | Custom design feasible | MEDIUM |
| 5,000 - 15,000 EUR | E-commerce adds significant complexity at this level | MEDIUM |
| 15,000+ EUR | Custom features and integrations feasible | MEDIUM |
| 15,000+ EUR | Phased approach optional (not forced by budget) | LOW |

### Rule: Timeline Constrains Scope

**Trigger:** Launch date is known.

| Timeline | Inference | Confidence |
|---|---|---|
| Under 4 weeks | Template-based, minimal customization | MEDIUM |
| Under 4 weeks | Content must be ready or near-ready | HIGH |
| 1-3 months | Standard project, custom design feasible | MEDIUM |
| 3+ months | Complex features and phased delivery possible | MEDIUM |

### Rule: Audience Age/Accessibility

**Trigger:** Target audience includes elderly users, government audience, or educational context.

| Inference | Confidence | Checkpoint |
|---|---|---|
| WCAG AA compliance should be targeted | HIGH | accessibility / compliance level |
| Larger font sizes recommended | MEDIUM | design-and-brand / typography |
| High contrast design preferred | MEDIUM | design-and-brand / visual style |
| Simple navigation critical | MEDIUM | site-structure / navigation model |

### Rule: Content Volume Implies Blog

**Trigger:** Client mentions regular content creation, news, articles, thought leadership.

| Inference | Confidence | Checkpoint |
|---|---|---|
| blog-and-editorial domain is ACTIVE | HIGH | domain applicability |
| Content publishing schedule needed | MEDIUM | blog-and-editorial / frequency |
| Author profiles may be needed | LOW | blog-and-editorial / attribution |
| RSS feed useful | LOW | blog-and-editorial / distribution |
| SEO content strategy important | MEDIUM | seo / content strategy alignment |

### Rule: International Audience Implies Multilingual

**Trigger:** Client mentions international markets, multiple countries, or non-English speaking audience while being in a different primary language region.

| Inference | Confidence | Checkpoint |
|---|---|---|
| multilingual domain may be ACTIVE | MEDIUM | domain applicability |
| Shipping to multiple countries likely (if e-commerce) | MEDIUM | ecommerce / Shipping / zones |
| Multi-currency consideration needed (if e-commerce) | MEDIUM | ecommerce / Payment Processing / currency |
| Legal pages may need per-jurisdiction variants | LOW | security-and-compliance / Legal Pages |

### Rule: CRM Mentioned Implies Lead Strategy

**Trigger:** Client mentions CRM (HubSpot, Salesforce, Pipedrive, etc.)

| Inference | Confidence | Checkpoint |
|---|---|---|
| Lead capture is a primary website function | HIGH | forms-and-lead-capture / priority |
| Form submissions must sync to CRM | HIGH | forms-and-lead-capture / CRM integration |
| Lead qualification or scoring may be relevant | LOW | forms-and-lead-capture / lead flow |
| Email marketing automation likely in place | MEDIUM | forms-and-lead-capture / follow-up automation |
| Conversion tracking for lead attribution important | MEDIUM | analytics-and-measurement / conversion events |

---

## Negative Inference Rules

Sometimes the absence of information is informative.

| Absent Information | After X Data Points | Inference | Confidence |
|---|---|---|---|
| No mention of existing website | 10+ data points | Likely new build, migration-and-redesign INACTIVE | MEDIUM |
| No mention of products/services sold online | 10+ data points | E-commerce likely not needed | MEDIUM |
| No mention of multiple languages | 10+ data points | Single language likely | MEDIUM |
| No mention of user login/accounts | 10+ data points | user-accounts likely INACTIVE | MEDIUM |
| No mention of booking/appointments | 10+ data points | booking-and-scheduling likely INACTIVE | MEDIUM |
| No mention of blog/content publishing | 10+ data points | blog-and-editorial likely INACTIVE | LOW |

**Important:** Negative inferences require a sufficient volume of input before triggering. A client who has shared only 3 data points may simply not have gotten to e-commerce yet. After 10+ substantive data points across multiple topics, absence becomes more meaningful.

---

## Inference Conflict Resolution

When two rules produce contradictory inferences:

1. **Explicit data overrides all inferences.** If the client says "we do not need e-commerce," that overrides any industry inference suggesting e-commerce.
2. **Higher confidence wins.** A HIGH inference overrides a conflicting MEDIUM inference.
3. **More specific wins.** An industry-specific rule overrides a general business model rule.
4. **Most recent wins.** If the client provides contradictory information at different times, the most recent statement takes precedence (but flag the contradiction to the operator).
5. **When truly tied: ask.** If two MEDIUM inferences conflict, downgrade both to LOW and generate a question.
