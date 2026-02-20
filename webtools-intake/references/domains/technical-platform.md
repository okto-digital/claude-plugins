# Domain: Technical Platform

**Purpose:** Validate that the brief addresses the technology foundation -- CMS/platform choice, hosting, infrastructure, and third-party integrations. Platform decisions constrain everything downstream: what can be built, how fast, at what cost, and who can maintain it.

---

## Priority Definitions

- **CRITICAL:** Brief cannot be accurate without this. Must resolve before drafting.
- **IMPORTANT:** Brief will be thinner without this. Resolve in second pass if time allows.
- **NICE-TO-HAVE:** Useful depth. Surface once, accept skip.

---

## 1. CMS / Platform Choice

| Checkpoint | Priority |
|---|---|
| Platform preference or requirement (WordPress, Webflow, Shopify, custom, headless, etc.) | CRITICAL |
| Reason for platform preference (existing expertise, business requirement, budget) | IMPORTANT |
| Who will manage the site day-to-day? (Technical vs. non-technical users) | CRITICAL |
| Content editing frequency and complexity (simple text updates vs. complex layouts) | IMPORTANT |
| Platform migration from an existing system? Which one? | IMPORTANT |

## 2. Hosting and Infrastructure

| Checkpoint | Priority |
|---|---|
| Current hosting provider (if existing site) | IMPORTANT |
| Hosting requirements (shared, VPS, cloud, managed) | IMPORTANT |
| Geographic hosting preference (data residency, CDN requirements) | NICE-TO-HAVE |
| Expected traffic volume (monthly visitors, peak periods) | IMPORTANT |
| Uptime requirements (99.9%, business-critical, etc.) | NICE-TO-HAVE |

## 3. Third-Party Integrations

| Checkpoint | Priority |
|---|---|
| CRM integration needed? (HubSpot, Salesforce, Pipedrive, etc.) | IMPORTANT |
| Email marketing platform? (Mailchimp, ActiveCampaign, Brevo, etc.) | IMPORTANT |
| Payment processing needed? (Stripe, PayPal, Mollie, etc.) | IMPORTANT |
| Booking/scheduling system? (Calendly, Acuity, custom) | IMPORTANT |
| Live chat or chatbot? (Intercom, Drift, Tidio, etc.) | NICE-TO-HAVE |
| Social media feeds or embeds? | NICE-TO-HAVE |
| Other business tools to connect (ERP, inventory, accounting) | IMPORTANT |

## 4. Technical Requirements

| Checkpoint | Priority |
|---|---|
| SSL certificate (required for all modern sites) | CRITICAL |
| Email setup (domain email, transactional email, contact forms) | IMPORTANT |
| Backup and recovery strategy | IMPORTANT |
| Staging/development environment needed? | NICE-TO-HAVE |
| Version control or deployment workflow | NICE-TO-HAVE |

## 5. Development Approach

| Checkpoint | Priority |
|---|---|
| Custom development vs. template/theme-based | IMPORTANT |
| Design system or component library preference | NICE-TO-HAVE |
| Front-end framework preferences or constraints | NICE-TO-HAVE |
| API requirements (headless CMS, external data sources) | NICE-TO-HAVE |
| Progressive web app (PWA) requirements | NICE-TO-HAVE |

## 6. Domain and DNS

| Checkpoint | Priority |
|---|---|
| Domain name confirmed and owned | CRITICAL |
| Domain registrar access available | IMPORTANT |
| DNS management: who controls it? | IMPORTANT |
| Subdomains needed (blog.domain.com, shop.domain.com) | NICE-TO-HAVE |
| Email DNS records (SPF, DKIM, DMARC) for domain email | NICE-TO-HAVE |

---

## Question Templates

**Do you have a preference for the website platform (CMS)?**
- Option A: WordPress -- it is the most widely used, has extensive plugin support, and is familiar to most web professionals
- Option B: A managed platform like Webflow or Squarespace -- prioritizing ease of use and visual editing over maximum flexibility

**Who will update the website content after launch?**
- Option A: Someone on your team who is comfortable with a CMS but not a developer -- they need an intuitive editing experience
- Option B: A developer or agency will handle all updates -- the editing experience matters less than technical capability

**What third-party tools does the website need to connect with?**
- Option A: Basic integrations -- email marketing (Mailchimp/ActiveCampaign), Google Analytics, and contact form submissions to email
- Option B: Deeper integrations -- CRM (HubSpot/Salesforce), booking system, payment processing, and possibly custom API connections

**Do you own your domain name and have access to manage it?**
- Option A: Yes, we own the domain and can provide DNS access for setup
- Option B: We are not sure -- we need help locating our domain registration and getting access

**Do you have current hosting, or do we need to set up hosting as part of this project?**
- Option A: We have hosting and want to keep it -- the new site should deploy to our existing server
- Option B: We need hosting recommendations -- set us up with something reliable and appropriate for our needs
