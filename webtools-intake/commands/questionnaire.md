---
description: Generate tailored client intake questionnaire
allowed-tools: Read, Write, Bash(mkdir:*)
argument-hint: [project-type] [industry]
---

Generate a tailored client intake questionnaire based on project type and industry. Produces D11: Client Questionnaire.

---

## Lifecycle Startup

### 1. Registry Check

Read `project-registry.md` in the current working directory.

- If it does NOT exist: create a minimal registry. Prompt the operator for the client name and project type. Create `project-registry.md` with Project Info filled in, an empty Document Log with all single-instance documents set to status `--`, and an empty Phase Log.
- If it DOES exist: parse the Project Info and Document Log.

### 2. Directory Validation

Verify these 7 subdirectories exist: `brief/`, `brand/`, `seo/`, `architecture/`, `blueprints/`, `content/`, `audit/`. Create any missing ones silently.

### 3. Input Validation

No required document inputs for this command.

### 4. Output Preparation

Check if `brief/D11-client-questionnaire.md` already exists. If yes, warn the operator:

```
D11: Client Questionnaire already exists (status: [status], updated: [date]).
Overwrite with a new questionnaire, or cancel?
```

If the operator cancels, stop.

### 5. Status Report

```
Project: [client name]
Output: brief/D11-client-questionnaire.md (new)

Ready to generate questionnaire.
```

---

## Validate Arguments

Parse the command arguments:

- **$1 = project type** (required): must be one of `new-build`, `redesign`, `landing-page`, `ecommerce`. If missing or invalid, present the valid options and ask the operator to choose.
- **$2 = industry** (optional): freeform text. If omitted, skip industry-specific questions and note this in the output.

---

## Generate Questionnaire

Build the questionnaire from three sections. Each question includes a parenthetical note explaining why it matters.

### Section A: Universal Questions

Generate these questions for all project types:

**Business Basics**
1. What is your company name and what do you do in one sentence? (Establishes core messaging and positioning)
2. What industry or sector are you in? (Shapes terminology, compliance needs, and audience expectations)
3. Where are you located and do you serve a local, regional, national, or international market? (Determines geographic targeting and language needs)
4. How large is your team? (Helps scope the "About" and "Team" sections)
5. How long have you been in business? (Influences credibility messaging and brand maturity)

**Website Goals**
6. What is the primary purpose of this website? (Drives the entire site structure and content strategy)
7. What are your top 3 goals for the website? (Helps prioritize features, content, and page structure)
8. What does success look like 6 months after launch? (Defines measurable outcomes to design toward)

**Target Audience**
9. Who is your primary target audience? Describe them. (Shapes tone, content complexity, and user journeys)
10. Is there a secondary audience? If so, who? (Determines if the site needs multiple navigation paths)
11. What does your audience need most from your website? (Identifies the core value proposition to lead with)

**Competitive Landscape**
12. Who are your top 3-5 competitors? Please share names and URLs if possible. (Enables competitive analysis and differentiation strategy)
13. What do your competitors do well online? (Identifies table-stakes elements to include)
14. What do your competitors do poorly or miss entirely? (Reveals differentiation opportunities)

**Brand**
15. Do you have existing brand guidelines (logo, colors, fonts, style guide)? (Determines whether brand extraction or creation is needed)
16. Describe your brand personality in 3-5 adjectives. (Seeds the brand voice profile)
17. Are there brands you admire -- in any industry -- for their communication style? (Provides reference points for tone and voice)

**Existing Assets**
18. What assets do you currently have? Check all that apply: logo, professional photos, video content, written content, domain name, hosting, Google Analytics. (Scopes what needs to be created vs reused)
19. Do you have existing content (brochures, presentations, case studies) that could be repurposed? (Identifies content sources for the content inventory)

**Content**
20. Who will provide the raw content for the website -- your team, or do you need content created? (Determines the scope of the content generation phase)
21. Are there specific messages, taglines, or statements that must appear on the site? (Captures non-negotiable content requirements)

**Technical Requirements**
22. What features does the site need? Examples: contact forms, booking system, e-commerce, blog, client portal, multilingual support. (Scopes technical requirements and page types)
23. Are there any third-party tools or systems the site needs to integrate with? Examples: CRM, email marketing, payment processor, calendar. (Identifies integration complexity)
24. How important is mobile experience relative to desktop? (Guides responsive design priorities)

**Timeline and Budget**
25. What is your target launch date? (Sets the project timeline)
26. What is your approximate budget range for this project? (Helps scope deliverables realistically)
27. Do you prefer to launch everything at once or in phases? (Determines MVP vs full-scope approach)

**Success Metrics**
28. How will you measure whether the website is successful? (Defines KPIs to design toward)
29. Do you have current baseline metrics -- monthly visitors, conversion rates, leads per month? (Establishes a benchmark for measuring improvement)

### Section B: Project-Type-Specific Questions

Generate ONLY the section matching the project type from $1:

**If new-build:**
1. Is this a brand new business or an established business getting its first website? (Determines brand maturity and available content)
2. Do you have a brand identity (logo, colors, fonts) or does that need to be created? (Scopes design prerequisites)
3. What is your content readiness? Have content ready / Need help creating / Starting from scratch. (Determines content generation scope)
4. What features are must-have for launch vs nice-to-have for later? (Helps define MVP)
5. Are there specific websites you admire? What do you like about them? (Provides concrete design and content direction)
6. Do you need a blog or news section? (Adds content strategy and page type considerations)
7. Do you need any third-party integrations at launch -- CRM, email marketing, booking, chat? (Scopes technical integration work)
8. What is your plan for maintaining the site after launch -- internal team or outsourced? (Influences CMS choice and training needs)

**If redesign:**
1. What is the URL of your current website? (Required for content inventory and competitive baseline)
2. What are the biggest pain points with the current site? (Identifies priority fixes)
3. What is working well that you want to keep? (Prevents losing existing strengths)
4. Do you have access to Google Analytics and Google Search Console for the current site? (Enables data-driven decisions)
5. What is driving the redesign now -- rebrand, poor performance, outdated design, new services, or something else? (Clarifies the core motivation)
6. Are you changing platforms or CMS? (Scopes migration complexity)
7. Which existing content should be migrated as-is, rewritten, or dropped? (Feeds the content inventory phase)
8. Are there SEO rankings or keywords you need to preserve? (Constrains URL structure and content decisions)
9. What pages currently get the most traffic? (Identifies high-priority pages for the redesign)
10. Do you have a list of all current pages and their purposes? (Accelerates content inventory)

**If landing-page:**
1. What is the single conversion goal -- sign up, purchase, download, book a call, or something else? (The entire page structure serves this one goal)
2. What campaign or initiative is this landing page for? (Provides messaging context)
3. Where will traffic come from -- paid ads, email, social media, organic search? (Influences messaging and page structure)
4. Is this page time-limited for a campaign or evergreen? (Determines maintenance needs)
5. What is the primary offer or value proposition? (Drives the hero section and CTA)
6. Do you have testimonials, case studies, or social proof to include? (Determines available trust elements)
7. Who is the target audience specifically for this page? (May differ from general audience)
8. What happens after someone converts -- thank you page, email sequence, sales call? (Defines the post-conversion flow)

**If ecommerce:**
1. How many products or SKUs do you have? (Scopes catalog complexity)
2. Do you have product photography and descriptions ready? (Determines content creation scope)
3. What payment methods do you need -- credit card, PayPal, invoicing, buy-now-pay-later? (Scopes payment integration)
4. Do you need shipping calculation? What regions do you ship to? (Determines shipping integration complexity)
5. Do you handle inventory management? If so, what system? (Identifies inventory sync needs)
6. Do you have a returns and refund policy defined? (Required for e-commerce compliance)
7. Do customers need accounts, or is guest checkout sufficient? (Affects user experience complexity)
8. What is your average order value? (Influences checkout optimization strategy)
9. Do you need product variants -- sizes, colors, configurations? (Scopes product data structure)
10. Are there compliance requirements -- age verification, tax rules, industry regulations? (Identifies legal constraints)
11. Do you need integration with an existing inventory, ERP, or fulfillment system? (Scopes technical integration)

### Section C: Industry-Specific Questions

Generate ONLY if $2 (industry) was provided. If $2 was omitted, write: "Industry-specific questions were not generated. Re-run with an industry argument to include them: /questionnaire [project-type] [industry]"

If $2 is provided, generate 5-8 questions tailored to that industry. Use these as guides for common industries:

- **Restaurant / Hospitality**: menu management, reservation system, delivery integration, seasonal menus, multiple locations, health/allergy info, photography needs
- **SaaS / Technology**: product demo or free trial, pricing tier presentation, documentation needs, integration marketplace, customer login portal, API docs
- **Professional services (law, accounting, consulting)**: case studies, team bios importance, client intake forms, compliance/regulatory requirements, practice areas
- **Real estate**: property listings integration (MLS/IDX), search and filter needs, virtual tour support, agent profiles, neighborhood content
- **Healthcare**: patient privacy compliance, appointment scheduling, patient portal, insurance info display, telehealth support
- **Education**: course catalog, enrollment process, student portal, accreditation display, event calendar

For any other industry, generate 5 questions about: industry-specific features needed, regulatory or compliance requirements, specialized content types, seasonal or cyclical considerations, and industry-standard integrations.

---

## Write D11

Write the complete questionnaire to `brief/D11-client-questionnaire.md`.

Start with the YAML frontmatter header:

```yaml
---
document_id: D11
title: "Client Questionnaire"
project: "[client name from registry]"
created: [today's date YYYY-MM-DD]
updated: [today's date YYYY-MM-DD]
created_by: webtools-intake
status: complete
dependencies: []
---
```

Format the body as:
- Document title as H1
- Project type and industry noted at the top
- Each section (A, B, C) as H2
- Questions numbered within each section
- After each question, leave an empty "Answer:" line for the operator to fill in during the client interview

---

## Lifecycle Completion

### 1. File Naming Validation

Verify the output file is named `D11-client-questionnaire.md` and is located in `brief/`.

### 2. Registry Update

Update `project-registry.md`:
- Set D11 row: Status = `complete`, Created = today, Updated = today, Created By = `webtools-intake`
- Phase Log: if the Discovery phase has no Started date, set Started to today and add `webtools-intake` to Plugins Used

### 3. Cross-Reference Check

Skip. D11 is a single-instance document.

### 4. Downstream Notification

```
D11: Client Questionnaire is complete.

Next step: Conduct the client intake using these questions.
Then start the Brief Generator agent to create D1: Project Brief.
```
