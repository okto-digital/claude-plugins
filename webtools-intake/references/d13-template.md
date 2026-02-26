# D13 Template: Client Follow-Up Questionnaire

**Purpose:** Format specification and generation rules for D13: Client Follow-Up Questionnaire. D13 is generated after the meeting to gather remaining information from the client. It is always produced (even for minimal gaps) to maintain a consistent project paper trail.

**Usage:** The brief-generator agent reads this file when generating D13 in REVIEW mode. It defines the document structure, client-friendly language principles, annotation format, and question formatting rules.

---

## Document Identity

| Field | Value |
|---|---|
| Document ID | D13 |
| Title | Client Follow-Up Questionnaire |
| Storage path | `brief/D13-client-followup.md` |
| Created by | webtools-intake (brief-generator agent) |
| Lifecycle | draft -> in-progress -> complete |
| Dependencies | Feeds into D1 (Project Brief) |

---

## YAML Frontmatter

```yaml
---
document_id: D13
title: "Client Follow-Up Questionnaire"
project: "[client name from registry]"
created: [YYYY-MM-DD]
updated: [YYYY-MM-DD]
created_by: webtools-intake
status: draft
dependencies: [D1]
meeting_date: [YYYY-MM-DD]
gaps_critical: [count]
gaps_important: [count]
total_questions: [count]
---
```

---

## Document Structure

### Header

```markdown
# Follow-Up Questions: [Client Name]

Thank you for the productive meeting on [date]. To finalize your project
brief, we need your input on a few remaining items.

Questions marked **[Required]** are essential for an accurate project scope.
All other questions help us deliver a better result but can be answered later
if needed.

Please answer directly below each question or return this document with your
responses.
```

### Question Sections

Questions are grouped by **conversation topic** (from topic-mapping.md), not by technical domain. Only include sections that have questions.

```markdown
---

## [Topic Name]

[1-2 sentence context connecting to what was discussed in the meeting.]

### [Number]. [Question title]

<!-- domain:[domain-name] priority:[CRITICAL|IMPORTANT] checkpoint:[checkpoint description] -->

[Question text in plain, non-technical language.]

[Answer format: recommendation with confirmation, free text, or options.]

**Your answer:**

---
```

### Summary Table

At the end of the document:

```markdown
---

## Summary

| Section | Questions | Required |
|---|---|---|
| [Topic 1] | [count] | [count of CRITICAL] |
| [Topic 2] | [count] | [count of CRITICAL] |
| ... | ... | ... |
| **Total** | **[total]** | **[total CRITICAL]** |

Please complete the answers above and return this document.
Once we have your responses, we will finalize the complete project brief.
```

---

## Annotation Format

Each question includes an HTML comment annotation that is invisible to the client but useful for the agency. These can be stripped before sending if the document is rendered as HTML, or left in place for plain markdown delivery (they are not visible in most markdown renderers).

```markdown
<!-- domain:ecommerce priority:CRITICAL checkpoint:Payment methods accepted -->
```

**Annotation fields:**
- `domain:` -- the source domain file name (without .md)
- `priority:` -- CRITICAL or IMPORTANT (NICE-TO-HAVE items are not included in D13)
- `checkpoint:` -- the exact checkpoint text from the domain file

---

## Question Formatting Rules

### Priority Display

- **CRITICAL** checkpoints are marked with **[Required]** in the question title
- **IMPORTANT** checkpoints have no marker (implied: helpful but not blocking)
- **NICE-TO-HAVE** checkpoints are NOT included in D13 (these are for the agency to address internally)

### Answer Formats

Use the format most natural for the answer type:

**1. Recommendation with confirmation (for MEDIUM-confidence inferences deferred to client):**

```markdown
### 3. How should shipping costs work? **[Required]**

<!-- domain:ecommerce priority:CRITICAL checkpoint:Shipping cost calculation -->

Based on our discussion about selling to the Benelux region, we recommend
a simple flat-rate shipping fee with free shipping above a certain order
amount. This keeps things straightforward for your customers.

- [ ] Yes, that approach works for us
- [ ] We would prefer a different approach: ___
```

**2. Free text (for questions with no inference available):**

```markdown
### 5. Who are your top 3 competitors?

<!-- domain:competitive-landscape priority:CRITICAL checkpoint:Named competitors with URLs -->

To make sure your website stands out, we need to know who you consider your
closest competitors. Please share their names and website addresses if possible.

**Your answer:**

```

**3. Multiple choice (for questions with clear options):**

```markdown
### 7. Who will update the website content after launch?

<!-- domain:post-launch priority:CRITICAL checkpoint:Content update responsibility -->

This helps us choose the right platform and set up editing permissions.

(a) Our team will handle updates -- we need it to be easy to edit without technical skills
(b) We would like ongoing support from the agency for content updates
(c) A mix -- we handle simple updates, agency handles structural changes

**Your choice:**

```

**4. List request (for questions expecting multiple items):**

```markdown
### 2. What are the most important pages on the website?

<!-- domain:site-structure priority:CRITICAL checkpoint:Complete page list -->

Beyond the homepage, what pages do you consider essential? We discussed
some during the meeting -- feel free to add to or adjust this list.

Pages mentioned in the meeting: About, Services, Contact, Blog

**Additional pages or changes:**

```

---

## Client-Friendly Language Principles

When writing D13 questions, the agent follows these principles:

### 1. Lead With Business Impact, Not Technical Mechanism

- Technical: "What is your Core Web Vitals target?"
- Client-friendly: "How fast should your website load? Speed affects both user experience and Google ranking."

### 2. Define Terms Inline When Necessary

- Technical: "Do you need WCAG AA compliance?"
- Client-friendly: "Should the website meet accessibility standards (making it usable for people with disabilities, including screen reader users)?"

### 3. Replace Abbreviations

- Technical: "CMS preference? SSL? CDN?"
- Client-friendly: "Which system would you like to use for editing your website content? (Examples: WordPress, Shopify, Webflow)"

### 4. Frame Questions Around Outcomes

- Technical: "Do you need a 301 redirect map?"
- Client-friendly: "When someone visits an old page on your current website, should they automatically be taken to the right page on the new site? (This prevents broken links and protects your Google rankings.)"

### 5. Use "You/Your" Language

- Passive: "The target audience should be identified."
- Client-friendly: "Who are the main people you want visiting your website?"

### 6. Provide Context From the Meeting

Every question section begins with a brief reference to what was discussed in the meeting. This shows the client their time was valued and connects the follow-up to the conversation.

- "During our meeting, you mentioned that phone orders are your biggest challenge..."
- "You shared that the website should support your expansion into the German market..."
- "Based on our discussion about your B2B model..."

### 7. Keep Questions Short

- Maximum 3 sentences per question (excluding the answer format)
- If more context is needed, put it in the section introduction, not the individual question

---

## Common Technical-to-Client Translations

These translations are used when converting domain checkpoints to D13 questions:

| Domain Concept | Client-Friendly Version |
|---|---|
| Core Web Vitals | Google's speed and responsiveness standards |
| 301 redirects | Automatically forwarding visitors from old page addresses to new ones |
| SSL/TLS certificate | The security lock icon in the browser that encrypts data |
| WCAG AA compliance | Accessibility standards for people with disabilities |
| CMS | The system you use to edit and update your website |
| CDN | A service that makes your website load faster worldwide |
| hreflang tags | Signals telling Google which language version to show |
| SEO | How well your website shows up in Google search results |
| Canonical URLs | The preferred web address when content could be found at multiple addresses |
| Schema markup | Extra information that helps Google understand and display your content in search results |
| Cookie consent | The banner asking visitors for permission to track their behavior |
| GDPR | European data protection regulation for handling personal information |
| PCI-DSS | Security standards for accepting credit card payments |
| NAP consistency | Keeping your business name, address, and phone identical everywhere online |
| Responsive design | Making the website work well on phones, tablets, and desktops |
| Staging environment | A private test version of your website for reviewing changes |
| DNS | The system that connects your domain name to your website |
| API | A way for different software tools to exchange data automatically |
| DPA | An agreement with service providers about how they handle your customers' data |
| RTL support | Support for languages read right-to-left (like Arabic or Hebrew) |
| Alt text | Descriptions for images that screen readers can read aloud |
| Color contrast ratio | Making sure text is readable against its background |

---

## Content Scope Rules

### Include in D13

- All remaining CRITICAL gaps (marked **[Required]**)
- All remaining IMPORTANT gaps (unmarked)
- Questions where MEDIUM-confidence inferences were deferred to the client by the operator
- Questions the operator explicitly flagged for client input

### Exclude from D13

- NICE-TO-HAVE gaps (these are for the agency to decide, not the client)
- Items already resolved by HIGH-confidence inference and confirmed by operator
- Items the operator answered during REVIEW mode
- Technical implementation details the client cannot meaningfully answer (e.g., "caching strategy", "security headers")

### Maximum Questions

D13 should not exceed **25 questions**. If more than 25 gaps remain after REVIEW mode:
1. Prioritize all CRITICAL items (these must be included)
2. Fill remaining slots with the most impactful IMPORTANT items
3. Note in the document footer that additional questions may follow

If fewer than 5 questions remain, the document is still generated but the header adjusts:

```markdown
# Quick Follow-Up: [Client Name]

We covered nearly everything in our meeting on [date]. Just a few
remaining items to finalize the project brief.
```

---

## Handling Returned D13

When the operator pastes completed D13 answers back into the brief-generator session:

1. Parse all answers (free text, checkbox selections, option choices)
2. Map answers back to domain checkpoints using the annotations
3. Update checkpoint statuses from MISSING to COVERED
4. Merge with existing data (inquiry form + meeting notes + inferences)
5. Re-run gap analysis to check for remaining CRITICAL items
6. If all CRITICAL resolved: proceed to BRIEF mode
7. If CRITICAL items remain: inform operator with options (answer now, follow up with client, proceed with gaps marked "[To be provided]")
