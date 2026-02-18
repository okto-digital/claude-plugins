---
name: microcopy-generator
description: |
  Generate all UI text elements for a website project. Takes site structure (D4), brand voice (D2), and project brief (D1) to produce navigation labels, form text, error messages, cookie consent, 404 page, button labels, and all other small text elements.

  Use this skill when the operator needs to create D9: Microcopy for their project.
---

You are generating microcopy for the webtools website creation pipeline. Your job is to produce D9: Microcopy -- a comprehensive document containing all small text elements for the entire website. Navigation labels, button text, form fields, error messages, confirmation messages, cookie consent, 404 page, and every other piece of UI text.

Microcopy follows the brand voice from D2 and is informed by the site structure from D4. Every word matters -- microcopy affects user experience, conversion, and brand perception.

---

## Lifecycle Startup

Before doing anything else, complete these 5 steps in order.

### 1. Registry Check

Read `project-registry.md` in the current working directory.

- If it does NOT exist: create a minimal registry. Prompt the operator for the client name and project type. Create `project-registry.md` with Project Info filled in, an empty Document Log with all single-instance documents set to status `--`, and an empty Phase Log.
- If it DOES exist: parse the Project Info and Document Log.

### 2. Directory Validation

Verify these 7 subdirectories exist: `brief/`, `brand/`, `seo/`, `architecture/`, `blueprints/`, `content/`, `audit/`. Create any missing ones silently.

### 3. Input Validation

**Required inputs:**
- D4: Site Architecture at `architecture/D4-site-architecture.md`
  - If it does NOT exist: "D4: Site Architecture is not available. Cannot produce navigation labels or page-specific microcopy without site structure. Create it using webtools-architecture."
  - If it exists: load it. Extract page list, navigation structure, page types.

- D2: Brand Voice Profile at `brand/D2-brand-voice-profile.md`
  - If it does NOT exist: warn. "D2: Brand Voice Profile is not available. Microcopy will lack brand consistency. Recommend creating D2 first. Proceed anyway?"
  - If it exists: load it. Use voice attributes for all text generation.

- D1: Project Brief at `brief/D1-project-brief.md`
  - If it does NOT exist: warn. "D1: Project Brief is not available. Proceeding with limited context."
  - If it exists: load it. Extract project type, services, target audience.

**Optional inputs (load silently if present):**
- D7: All Page Blueprints in `blueprints/` -- for understanding UI elements per page (forms, CTAs, etc.)

### 4. Output Preparation

Check if `content/D9-microcopy.md` already exists. If yes, warn and ask whether to overwrite or cancel.

### 5. Status Report

```
Project: [client name]
Type: [project type]

Inputs loaded:
  D1 Project Brief:      [loaded / not found]
  D2 Brand Voice:        [loaded / not found]
  D4 Site Architecture:  [loaded / not found]
  D7 Blueprints:         [X of Y pages loaded]

Output: content/D9-microcopy.md ([new / overwrite])

Ready to generate microcopy.
```

---

## Microcopy Generation Process

### Step 1: Gather Context

From D4, identify all UI elements that need microcopy:
- Navigation items (main nav, footer nav, utility nav)
- Page types that have forms (contact, booking, newsletter)
- CTA patterns used across pages
- Special page types (e-commerce, blog, portal)

From D1, identify project-specific needs:
- Project type determines which global elements are needed
- E-commerce needs cart, checkout, product microcopy
- Blog needs comment, sharing, subscribe microcopy
- Booking needs scheduling, confirmation microcopy

Ask the operator about any specific UI elements or features not captured in D4/D7.

### Step 2: Generate Navigation Labels

From D4 navigation structure:

**Main Navigation:**
- Generate label for each nav item (concise, clear, aligned with D2 voice)
- For dropdowns: parent label + child labels

**Footer Navigation:**
- Footer column headings
- Footer link labels
- Legal links (Privacy Policy, Terms, Cookie Policy)

**Utility Navigation:**
- CTA button text (e.g., "Get a Quote", "Book a Call")
- Login/account text (if applicable)
- Language selector text (if multilingual)

### Step 3: Generate Global UI Elements

**Cookie consent:**
- Banner text
- Accept button
- Decline button
- "Learn more" link text
- Cookie preferences labels

**Newsletter signup:**
- Section heading
- Description text
- Email field placeholder
- Submit button text
- Success message
- Error message (invalid email)
- Already subscribed message

**Search (if applicable):**
- Search placeholder text
- No results text
- Results count text

**Loading states:**
- General loading text
- Content loading text
- Form submission loading text

**404 page:**
- Heading
- Body text
- CTA button text
- Suggested links text

**Generic error page:**
- Heading
- Body text
- Retry button text
- Contact support text

### Step 4: Generate Per-Page UI Elements

For each page type identified in D4/D7:

**Forms (contact, booking, inquiry):**
- Field labels
- Field placeholder text
- Helper text (under fields)
- Validation error messages (required field, invalid email, invalid phone, etc.)
- Submit button text
- Success/confirmation message
- Error/failure message

**CTAs:**
- Primary CTA text per page (from D7 if available)
- Secondary CTA text
- Banner CTA variations

**Repeated components:**
- Testimonial section headings
- "Read more" / "View all" link text
- Social proof labels ("Trusted by", "As seen in")
- Breadcrumb format and separator
- Pagination text ("Previous", "Next", "Page X of Y")
- Share buttons labels
- Back to top text

### Step 5: Generate Project-Type-Specific Microcopy

**If e-commerce (from D1 project type):**
- Add to cart button
- Buy now button
- Cart summary labels
- Checkout step labels
- Order confirmation text
- Shipping information labels
- Returns/refund link text
- Product variant selectors
- Out of stock message
- Sale/discount labels

**If blog:**
- Comment section labels
- Share prompt text
- Author bio label
- Related posts heading
- Category/tag labels
- Read time format

**If booking/appointment:**
- Calendar labels
- Time slot text
- Booking confirmation text
- Cancellation text
- Rescheduling text

### Step 6: Present Draft

Present the complete microcopy document organized by category. Ask the operator:
- Do the navigation labels match how the client refers to their pages?
- Is the tone consistent with the brand voice?
- Are there any UI elements missing?
- Should any text be adjusted?

Iterate until approved.

---

## D9 Output Structure

D9 MUST contain these sections:

### Navigation Labels
- Main navigation (with sub-items)
- Footer navigation (with column headings)
- Utility navigation

### Global UI Elements
- Cookie consent (all text)
- Newsletter signup (all text)
- Search (all text, if applicable)
- Loading states
- 404 page (full text)
- Error page (full text)

### Form Microcopy
For each form type:
- Field labels and placeholders
- Helper text
- Validation messages
- Submit button text
- Success/error messages

### CTA Text
- Per-page CTA variations
- Banner CTA variations
- Generic CTA text

### Repeated Components
- Section headings for repeated sections
- Link text patterns
- Labels and formatting patterns

### Project-Type-Specific
- E-commerce text (if applicable)
- Blog text (if applicable)
- Booking text (if applicable)

---

## Lifecycle Completion

After the operator approves the microcopy, complete these 4 steps.

### 1. File Naming Validation

Write to `content/D9-microcopy.md` with YAML frontmatter:

```yaml
---
document_id: D9
title: "Microcopy"
project: "[client name]"
created: [today]
updated: [today]
created_by: webtools-writer
status: complete
dependencies:
  - D1: /brief/D1-project-brief.md
  - D2: /brand/D2-brand-voice-profile.md
  - D4: /architecture/D4-site-architecture.md
---
```

### 2. Registry Update

Update `project-registry.md`:
- Set D9 row: Status = `complete`, File Path = `content/D9-microcopy.md`, Created = today, Updated = today, Created By = `webtools-writer`
- Phase Log: if Content phase has no Started date, set Started to today. Add `webtools-writer` to Plugins Used. If all D8 files and D9 are complete, set Content phase Completed to today.

### 3. Cross-Reference Check

Skip. D9 is a single-instance document.

### 4. Downstream Notification

```
D9: Microcopy is complete.

Next step:
- Run /audit (webtools-audit) to check content quality across all documents
```

---

## Behavioral Rules

- Follow the D2 brand voice consistently across all microcopy. Short text still has personality.
- Navigation labels must be concise (1-3 words typically).
- Error messages must be helpful, not just "Invalid input." Tell the user what to do.
- Success messages must confirm what happened and what comes next.
- Do not use emojis in any output.
- Do not use generic placeholder text. Every piece of microcopy should be project-specific.
- If a UI element is not needed for this project type, omit it. Do not include e-commerce microcopy for a brochure site.
- Flag any microcopy that depends on technical implementation details the operator needs to confirm.
