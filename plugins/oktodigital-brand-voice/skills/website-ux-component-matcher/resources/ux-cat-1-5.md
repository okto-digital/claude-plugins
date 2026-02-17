# UX Components Reference: Categories 1-5

**Part 2 of 3** -- Navigation & Wayfinding, Hero & Landing, Content Display, Disclosure & Progressive, Forms & Input.
**Full reference split across:**
- `ux-index-and-patterns.md` -- Index, page patterns, appendix
- `ux-cat-1-5.md` (this file) -- Categories 1-5
- `ux-cat-6-10.md` -- Categories 6-10

**Source:** UX Component Knowledge Base - Reference Guide v1.0.0

---

## Category 1: Navigation & Wayfinding

Components for site navigation and user orientation.

---

### Navbar (Navigation Bar)

**Description:** Primary horizontal navigation containing logo, menu links, and CTAs.

**Content Slots:**
| Slot | Required | Type | Limits | Purpose |
|------|----------|------|--------|---------|
| logo | Yes | image | - | Brand identification |
| nav_items | Yes | array | 3-7 items, 20 chars each | Primary navigation links |
| cta_button | No | text | 5-20 chars | Primary action (e.g., "Sign Up") |

**Best For:**
- Site-wide navigation
- Brand presence on every page
- Quick access to key sections

**Avoid When:**
- Single-page apps with minimal sections
- Landing pages needing maximum focus on conversion

**Variants:**
- **sticky:** Remains visible while scrolling
- **transparent:** Overlays hero, becomes solid on scroll
- **centered-logo:** Logo centered with nav items on both sides

**Pairs With:** mega-menu, mobile-drawer, announcement-bar

**Accessibility:** Use semantic `<nav>` element, `aria-label` for landmark
**Mobile:** Collapse to hamburger menu below 768px

---

### Mega Menu

**Description:** Large dropdown menu displaying multiple navigation groups in columns.

**Content Slots:**
| Slot | Required | Type | Limits | Purpose |
|------|----------|------|--------|---------|
| category_headings | Yes | array | 2-5 items, 25 chars each | Section headers |
| menu_items | Yes | array | 8 items/group, 30 chars each | Navigation links |
| featured_content | No | object | - | Promotional image/content |

**Best For:**
- Sites with 20+ pages
- E-commerce with many categories
- Enterprise sites with complex hierarchy

**Avoid When:**
- Simple sites with < 10 pages
- Mobile-first designs
- Touch is primary input

**Variants:**
- **full-width:** Spans entire viewport
- **contained:** Width limited to content area
- **with-featured:** Includes promotional image column

**Pairs With:** navbar, search-bar

**Accessibility:** 0.5s hover delay, `aria-expanded`, keyboard navigation with arrow keys
**Mobile:** Replace with accordion or mobile drawer

---

### Mobile Navigation Drawer

**Description:** Slide-out panel containing navigation for mobile devices.

**Content Slots:**
| Slot | Required | Type | Limits | Purpose |
|------|----------|------|--------|---------|
| menu_items | Yes | array | 3-12 items, 25 chars each | Primary navigation |
| secondary_links | No | array | 6 items max, 20 chars each | Utility links |
| cta_button | No | text | 20 chars | Primary action |

**Best For:**
- Mobile navigation
- Sites with many sections
- Responsive designs

**Avoid When:**
- Desktop-only sites
- Sites with only 2-3 pages

**Variants:**
- **left-slide:** Slides in from left
- **right-slide:** Slides in from right
- **full-screen:** Covers entire viewport

**Pairs With:** navbar, accordion

**Accessibility:** Focus trap when open, escape to close, `aria-modal`
**Mobile:** Touch-friendly targets min 44x44px

---

### Breadcrumb Navigation

**Description:** Hierarchical trail showing current page location within site structure.

**Content Slots:**
| Slot | Required | Type | Limits | Purpose |
|------|----------|------|--------|---------|
| path_items | Yes | array | 2-6 items, 30 chars each | Page hierarchy |
| separator | Yes | text | >, /, >>, chevron | Visual separator |

**Best For:**
- Deep hierarchical sites
- E-commerce category pages
- Documentation sites

**Avoid When:**
- Flat site structure
- Single-level sites
- Homepage (always omit)

**Variants:**
- **full-path:** Shows complete hierarchy
- **collapsed:** Truncates middle items with ellipsis

**Pairs With:** page-header, sidebar-nav

**Accessibility:** Use `<nav>` with `aria-label='Breadcrumb'`, `<ol>/<li>` structure, `aria-current='page'` on last item
**Mobile:** May truncate or show only parent on small screens

---

### Pagination

**Description:** Page-by-page navigation for content split across multiple pages.

**Content Slots:**
| Slot | Required | Type | Limits | Purpose |
|------|----------|------|--------|---------|
| prev_label | No | text | 15 chars | Previous page button |
| next_label | No | text | 15 chars | Next page button |
| page_count | Yes | number | - | Total pages |

**Best For:**
- Blog archives
- Search results
- Product listings

**Avoid When:**
- Content fits on single page
- Infinite scroll is more appropriate
- < 10 items total

**Variants:**
- **numbered:** Page numbers with ellipsis
- **prev-next-only:** Simple previous/next buttons
- **load-more:** Single button to append content

**Pairs With:** card-grid, table, search-bar

**Accessibility:** Use `<nav>` with `aria-label='Pagination'`, `aria-current='page'` on active
**Mobile:** May simplify to prev/next only

---

### Tab Navigation

**Description:** Horizontal or vertical tabs for switching between content panels.

**Content Slots:**
| Slot | Required | Type | Limits | Purpose |
|------|----------|------|--------|---------|
| tab_labels | Yes | array | 2-7 items, 3-20 chars each | Tab labels |
| tab_panels | Yes | array | - | Panel content |

**Best For:**
- Related content that shouldn't all display at once
- Feature comparisons
- Settings/preferences pages
- Dashboard sections

**Avoid When:**
- Content should be visible simultaneously for comparison
- Only 1-2 sections (use headings instead)
- Deep content that spans multiple screens

**Variants:**
- **horizontal:** Tabs above content
- **vertical:** Tabs beside content
- **underlined:** Minimal style with underline indicator
- **boxed:** Each tab in distinct container

**Pairs With:** card, form, table

**Accessibility:** `role='tablist'`, `role='tab'`, `role='tabpanel'`, arrow key navigation, `aria-selected`
**Mobile:** Consider scrollable tabs or converting to accordion

---

### Anchor Navigation / Table of Contents

**Description:** In-page navigation linking to sections within the same page.

**Content Slots:**
| Slot | Required | Type | Limits | Purpose |
|------|----------|------|--------|---------|
| toc_title | No | text | 30 chars | Heading (e.g., "On this page") |
| anchor_items | Yes | array | 3-15 items, 50 chars each | Links to sections |

**Best For:**
- Long-form content
- Documentation
- FAQ pages
- Legal/policy pages

**Avoid When:**
- Short pages (< 3 sections)
- Pages users typically scan quickly

**Variants:**
- **sidebar-sticky:** Fixed in sidebar while scrolling
- **inline-top:** At top of content area
- **collapsible:** Can be expanded/collapsed

**Pairs With:** accordion, long-form-content, documentation-layout

**Accessibility:** Use `<nav>` with `aria-label`, highlight current section
**Mobile:** Often hidden or collapsed

---

### Footer Navigation

**Description:** Site-wide footer with navigation columns, contact info, and legal links.

**Content Slots:**
| Slot | Required | Type | Limits | Purpose |
|------|----------|------|--------|---------|
| column_headings | Yes | array | 2-5 items, 20 chars each | Column headers |
| column_links | Yes | array | 8 items/column, 25 chars each | Navigation links |
| social_links | No | array | 6 items max | Social media links |
| contact_info | No | object | - | Email, phone, address |
| legal_links | Yes | array | 4 items max, 20 chars each | Privacy, terms, etc. |
| copyright | Yes | text | 80 chars | Copyright notice |

**Best For:**
- Every website
- Secondary navigation
- Contact and legal information

**Avoid When:**
- Never - every site needs a footer

**Variants:**
- **multi-column:** 3-5 columns of organized links
- **minimal:** Single row with essential links
- **cta-focused:** Includes newsletter signup

**Pairs With:** newsletter-signup, logo-cloud, contact-form

**Accessibility:** Use `<footer>` element, `role='contentinfo'`, clear link labels
**Mobile:** Stack columns vertically, consider accordion for link groups

---

### Sidebar Navigation

**Description:** Vertical navigation typically used in documentation or dashboards.

**Content Slots:**
| Slot | Required | Type | Limits | Purpose |
|------|----------|------|--------|---------|
| section_headings | No | array | 25 chars each | Group headings |
| nav_items | Yes | array | 30 items max, 35 chars each | Navigation links |

**Best For:**
- Documentation sites
- Admin dashboards
- Settings pages
- Multi-page wizards

**Avoid When:**
- Marketing sites
- Simple brochure sites
- Mobile-primary experiences

**Variants:**
- **collapsible:** Sections expand/collapse
- **icon-only:** Collapsed state shows only icons
- **nested:** Multi-level hierarchy with indentation

**Pairs With:** anchor-nav, search-bar, breadcrumbs

**Accessibility:** Use `<nav>` element, `aria-expanded` for collapsible sections
**Mobile:** Convert to drawer or hide behind hamburger

---

## Category 2: Hero & Landing Sections

Components for page introductions and key messaging.

---

### Hero Section

**Description:** Large, prominent section at top of page with headline, subheadline, and CTA.

**Content Slots:**
| Slot | Required | Type | Limits | Purpose |
|------|----------|------|--------|---------|
| headline | Yes | text | 10-60 chars, 8 words max | Primary attention-grabbing statement |
| subheadline | Yes | text | 50-200 chars, 3 sentences max | Supporting text |
| primary_cta | Yes | text | 5-25 chars, 4 words max | Primary action button |
| secondary_cta | No | text | 25 chars | Alternative action |
| hero_image | No | image | - | Visual supporting message |

**Writing Guidelines:**
- Headline should be understandable in under 5 seconds
- Use action verbs for CTA: Get, Start, Try, Join

**Best For:**
- Homepage
- Landing pages
- Product pages
- Campaign pages

**Avoid When:**
- Documentation pages
- Utility pages (settings, account)
- When immediate content access is priority

**Variants:**
- **centered:** Text centered, image as background or below
- **split:** Text on one side, image on other (50/50)
- **video-background:** Autoplaying video behind text
- **minimal:** Text-only, no imagery

**Pairs With:** logo-cloud, stats-bar, feature-grid

**Accessibility:** Ensure text contrast over images, provide alt text for hero images
**Mobile:** Stack vertically, reduce image size, ensure CTA is thumb-reachable

---

### Announcement Bar

**Description:** Thin banner at top of page for promotions, news, or urgent messages.

**Content Slots:**
| Slot | Required | Type | Limits | Purpose |
|------|----------|------|--------|---------|
| message | Yes | text | 20-100 chars | Brief announcement |
| link_text | No | text | 20 chars | CTA link |
| dismiss_button | No | boolean | default: true | Allow users to close |

**Best For:**
- Sales and promotions
- Product launches
- Important updates
- Event announcements

**Avoid When:**
- No current announcement needed
- Message is too long/complex
- Already have multiple banners

**Variants:**
- **sticky:** Remains at top while scrolling
- **dismissible:** User can close it
- **countdown:** Includes timer for limited offers

**Pairs With:** navbar, hero

**Accessibility:** `role='alert'` for urgent messages, proper color contrast
**Mobile:** May wrap to 2 lines, ensure touch target for dismiss

---

### Statistics Bar / Metrics Section

**Description:** Row of key metrics or achievements with numbers and labels.

**Content Slots:**
| Slot | Required | Type | Limits | Purpose |
|------|----------|------|--------|---------|
| stats | Yes | array | 3-5 items | Collection of statistics |
| - value | - | text | 10 chars | The number (e.g., "10K+", "99%") |
| - label | - | text | 25 chars | What the number represents |

**Best For:**
- Social proof
- Company achievements
- Product metrics
- Trust building

**Avoid When:**
- Numbers aren't impressive
- Metrics can't be verified
- Too many stats dilute impact

**Variants:**
- **inline:** Single row, evenly spaced
- **boxed:** Each stat in its own card
- **animated:** Numbers count up on scroll

**Pairs With:** hero, testimonial, logo-cloud

**Accessibility:** Ensure numbers are readable, not just decorative
**Mobile:** 2x2 grid or vertical stack

---

### Logo Cloud / Client Logos

**Description:** Collection of client, partner, or press logos for social proof.

**Content Slots:**
| Slot | Required | Type | Limits | Purpose |
|------|----------|------|--------|---------|
| section_heading | No | text | 50 chars | Optional heading |
| logos | Yes | array | 4-12 items | Client/partner logos |

**Common Headings:** "Trusted by", "As seen in", "Our clients", "Partners"

**Best For:**
- Building trust
- Social proof
- B2B credibility
- Press mentions

**Avoid When:**
- No recognizable clients yet
- Logos are low quality
- < 4 logos available

**Variants:**
- **static-grid:** Fixed grid of logos
- **carousel:** Scrolling/rotating logos
- **grayscale:** All logos in same color for consistency

**Pairs With:** hero, stats-bar, testimonial

**Accessibility:** Alt text for each logo, consistent sizing
**Mobile:** 2 columns or horizontal scroll

---

### Value Proposition Section

**Description:** Section highlighting key benefits or unique selling points.

**Content Slots:**
| Slot | Required | Type | Limits | Purpose |
|------|----------|------|--------|---------|
| section_heading | Yes | text | 60 chars | Section title |
| section_subheading | No | text | 150 chars | Supporting text |
| benefits | Yes | array | 3-6 items | Individual benefits |
| - icon | - | icon | - | Visual representation |
| - title | - | text | 40 chars | Benefit headline |
| - description | - | text | 150 chars | Benefit explanation |

**Best For:**
- Explaining product value
- Highlighting differentiators
- Marketing pages

**Avoid When:**
- Benefits aren't clearly defined
- Technical documentation

**Variants:**
- **icon-grid:** Icons with titles and descriptions in grid
- **alternating:** Image and text alternate sides
- **centered-stack:** Vertically stacked, centered

**Pairs With:** hero, feature-grid, cta-section

**Accessibility:** Decorative icons should have `aria-hidden`
**Mobile:** Stack vertically, may hide icons

---

## Category 3: Content Display

Components for presenting various types of content.

---

### Card

**Description:** Contained unit of content with image, title, description, and action.

**Content Slots:**
| Slot | Required | Type | Limits | Purpose |
|------|----------|------|--------|---------|
| image | No | image | - | Visual representation |
| eyebrow | No | text | 20 chars | Category or label above title |
| title | Yes | text | 10-60 chars | Card heading |
| description | No | text | 150 chars, 3 lines max | Supporting text |
| metadata | No | text | 30 chars | Date, author, read time |
| cta | No | text | 20 chars | Action link or button |

**Writing Guidelines:**
- 10-12 characters ideal for dashboard card titles
- Limit description to 100 chars for cleaner aesthetic

**Best For:**
- Blog post previews
- Product listings
- Team members
- Feature highlights
- Portfolio items

**Avoid When:**
- Content requires detailed comparison
- Information density is high priority
- Tabular data is more appropriate

**Variants:**
- **vertical:** Image on top, content below
- **horizontal:** Image on side, content beside
- **overlay:** Text overlays image
- **minimal:** No image, text-only

**Pairs With:** card-grid, masonry, pagination, filter-controls

**Accessibility:** Entire card clickable via pseudo-element, not wrapping link
**Mobile:** Full-width cards, may switch horizontal to vertical

---

### Bento Grid

**Description:** Asymmetric grid layout with varied cell sizes for visual hierarchy.

**Content Slots:**
| Slot | Required | Type | Limits | Purpose |
|------|----------|------|--------|---------|
| grid_items | Yes | array | 4-8 items | Grid cells |
| - size | - | enum | small, medium, large, featured | Cell size |
| - title | - | text | 40 chars | Item heading |
| - description | - | text | 120 chars | Item description |
| - icon/image | - | media | - | Visual element |

**Best For:**
- Feature showcases
- Portfolio displays
- Dashboard overviews
- Marketing sections

**Avoid When:**
- All items have equal importance
- Mobile is primary target
- Need consistent information structure

**Variants:**
- **Apple-style:** Clean, minimal, with subtle animations
- **feature-focused:** One large hero item with smaller surrounding
- **dashboard:** Data-focused with charts and metrics

**Pairs With:** feature-grid, card

**Accessibility:** Clear visual hierarchy, semantic headings
**Mobile:** Stack to single column, prioritize important items

---

### Masonry Grid

**Description:** Variable-height grid layout that fills vertical space efficiently.

**Content Slots:**
| Slot | Required | Type | Limits | Purpose |
|------|----------|------|--------|---------|
| grid_items | Yes | array | - | Variable-sized items |
| columns | Yes | number | 2-4 | Number of columns |

**Best For:**
- Image galleries
- Pinterest-style layouts
- Mixed content types
- Portfolio displays

**Avoid When:**
- Consistent item heights needed
- Predictable scanning patterns required
- Mobile-first design

**Variants:**
- **pure-masonry:** Variable heights, no gaps
- **with-gutters:** Consistent spacing between items
- **lazy-loading:** Loads items as user scrolls

**Pairs With:** lightbox, filter-controls, pagination

**Accessibility:** Provide alternative list view option
**Mobile:** Reduce to 1-2 columns

---

### Timeline

**Description:** Chronological display of events, milestones, or process steps.

**Content Slots:**
| Slot | Required | Type | Limits | Purpose |
|------|----------|------|--------|---------|
| timeline_items | Yes | array | 3-15 items | Timeline entries |
| - date | - | text | 20 chars | When event occurred |
| - title | - | text | 50 chars | Event title |
| - description | - | text | 200 chars | Event description |
| - icon | - | icon | - | Visual marker |

**Best For:**
- Company history
- Project milestones
- Process explanations
- Career/resume displays

**Avoid When:**
- Non-chronological content
- Too many items (> 15)
- Events have no clear order

**Variants:**
- **vertical:** Items stack vertically
- **horizontal:** Items flow horizontally
- **alternating:** Items alternate left/right

**Pairs With:** card, icon-grid

**Accessibility:** Proper heading hierarchy, screen reader friendly
**Mobile:** Always vertical on small screens

---

### Comparison Table

**Description:** Side-by-side comparison of features, products, or options.

**Content Slots:**
| Slot | Required | Type | Limits | Purpose |
|------|----------|------|--------|---------|
| column_headers | Yes | array | 2-5 columns | Products/options being compared |
| row_labels | Yes | array | 5-20 rows | Features being compared |
| cells | Yes | array | - | Comparison values |
| highlight_column | No | number | - | Column to emphasize (recommended) |

**Best For:**
- Product comparisons
- Pricing tier comparisons
- Feature matrices
- Decision support

**Avoid When:**
- Items have vastly different features
- > 5 columns (too complex)
- Mobile is primary (tables are hard on mobile)

**Variants:**
- **feature-matrix:** Checkmarks for feature presence
- **value-comparison:** Text/numbers in cells
- **sticky-header:** Header stays visible while scrolling

**Pairs With:** pricing-table, tabs

**Accessibility:** Proper table semantics, `<th>` headers, scope attributes
**Mobile:** Horizontal scroll or card-based alternative

---

### Feature Grid

**Description:** Grid of features with icons, titles, and descriptions.

**Content Slots:**
| Slot | Required | Type | Limits | Purpose |
|------|----------|------|--------|---------|
| section_heading | No | text | 60 chars | Section title |
| features | Yes | array | 3-9 items | Feature items |
| - icon | - | icon | - | Visual representation |
| - title | - | text | 35 chars | Feature name |
| - description | - | text | 120 chars | Feature explanation |
| - link | - | text | 20 chars | Optional learn more link |

**Best For:**
- Product features
- Service offerings
- Capabilities overview
- How it works sections

**Avoid When:**
- Features need detailed explanation
- > 9 features (too overwhelming)
- Complex technical documentation

**Variants:**
- **3-column:** Three items per row
- **icon-left:** Icons beside text
- **card-style:** Each feature in bordered card

**Pairs With:** hero, value-prop, cta-section

**Accessibility:** Decorative icons have `aria-hidden`
**Mobile:** Stack to 1-2 columns

---

### Testimonial

**Description:** Customer quote with attribution and optional photo.

**Content Slots:**
| Slot | Required | Type | Limits | Purpose |
|------|----------|------|--------|---------|
| quote | Yes | text | 100-300 chars | Customer testimonial |
| author_name | Yes | text | 40 chars | Person's name |
| author_title | No | text | 50 chars | Job title, company |
| author_photo | No | image | - | Person's headshot |
| company_logo | No | image | - | Company logo |
| rating | No | number | 1-5 | Star rating |

**Best For:**
- Social proof
- Building trust
- Customer success stories
- Product validation

**Avoid When:**
- No real testimonials available
- Quotes are generic or unverifiable
- Quote is too long (> 300 chars)

**Variants:**
- **single:** One prominent testimonial
- **carousel:** Multiple testimonials cycling
- **grid:** Multiple testimonials in grid
- **video:** Video testimonial embed

**Pairs With:** logo-cloud, stats-bar, cta-section

**Accessibility:** Use `<blockquote>` with `<cite>` for attribution
**Mobile:** Full-width, consider carousel for multiple

---

### Quote Block

**Description:** Standalone quote for emphasis within content.

**Content Slots:**
| Slot | Required | Type | Limits | Purpose |
|------|----------|------|--------|---------|
| quote_text | Yes | text | 50-200 chars | The quotation |
| attribution | No | text | 60 chars | Source of quote |

**Best For:**
- Highlighting key points
- Expert opinions
- Within articles/blog posts
- Callout content

**Avoid When:**
- Quote is very long
- No clear attribution
- Overused within single page

**Variants:**
- **pull-quote:** Large, styled prominently
- **bordered:** Left border styling
- **centered:** Full-width, centered text

**Pairs With:** long-form content, article layout

**Accessibility:** Use `<blockquote>` with `<cite>`
**Mobile:** Full-width, adjust font size

---

## Category 4: Disclosure & Progressive

Components for revealing content progressively.

---

### Accordion

**Description:** Collapsible content sections that expand/collapse on click.

**Content Slots:**
| Slot | Required | Type | Limits | Purpose |
|------|----------|------|--------|---------|
| items | Yes | array | 3-15 items | Accordion panels |
| - trigger | - | text | 10-80 chars | Clickable header |
| - content | - | text | 50-500 chars | Revealed content |

**Best For:**
- FAQ sections
- Feature details
- Legal/policy content
- Help documentation

**Avoid When:**
- Content should always be visible for SEO
- Only 1-2 items (not worth hiding)
- Critical information users must see

**Variants:**
- **single-expand:** Only one panel open at a time
- **multi-expand:** Multiple panels can be open
- **nested:** Accordions within accordions

**Pairs With:** search-bar, anchor-nav

**Accessibility:** `aria-expanded`, keyboard navigation, proper focus management
**Mobile:** Touch-friendly tap targets, full-width

---

### Collapsible Section

**Description:** Single expandable/collapsible content area.

**Content Slots:**
| Slot | Required | Type | Limits | Purpose |
|------|----------|------|--------|---------|
| trigger_text | Yes | text | 50 chars | Clickable text/button |
| content | Yes | text | - | Hidden content |
| default_state | No | enum | open, closed | Initial state |

**Best For:**
- "Read more" functionality
- Secondary information
- Optional details

**Avoid When:**
- Content is essential
- Single short piece of content
- Primary content path

**Variants:**
- **read-more:** Expands inline text
- **show-details:** Reveals additional section
- **toggle:** Can be opened and closed repeatedly

**Pairs With:** card, long-form content

**Accessibility:** `aria-expanded`, proper button semantics
**Mobile:** Full-width tap target

---

### Tooltip

**Description:** Small popup providing additional context on hover/focus.

**Content Slots:**
| Slot | Required | Type | Limits | Purpose |
|------|----------|------|--------|---------|
| trigger_element | Yes | - | - | Element that triggers tooltip |
| tooltip_text | Yes | text | 20-100 chars | Tooltip content |

**Best For:**
- Term definitions
- Icon explanations
- Form field hints
- Abbreviated content

**Avoid When:**
- Content is essential (hidden on mobile)
- Long explanations needed
- Touch devices are primary

**Variants:**
- **hover:** Appears on mouse hover
- **focus:** Appears on keyboard focus
- **click:** Appears on click (mobile-friendly)

**Pairs With:** icons, form fields, tables

**Accessibility:** `aria-describedby`, keyboard accessible
**Mobile:** Consider alternatives (inline text, modal)

---

### Modal / Dialog

**Description:** Overlay window that appears above page content.

**Content Slots:**
| Slot | Required | Type | Limits | Purpose |
|------|----------|------|--------|---------|
| title | Yes | text | 50 chars | Modal heading |
| content | Yes | - | - | Modal body content |
| primary_action | No | text | 20 chars | Primary button |
| secondary_action | No | text | 20 chars | Secondary button |
| close_button | Yes | boolean | true | Dismiss modal |

**Best For:**
- Confirmation dialogs
- Form submissions
- Important alerts
- Focused tasks

**Avoid When:**
- Content should be inline
- Multiple modals needed
- Long, scrolling content

**Variants:**
- **centered:** Centered on screen
- **full-screen:** Covers entire viewport
- **side-panel:** Slides in from edge
- **confirmation:** Simple yes/no dialog

**Pairs With:** forms, alerts

**Accessibility:** Focus trap, `aria-modal`, escape to close, return focus on close
**Mobile:** Often full-screen on small devices

---

## Category 5: Forms & Input

Components for user data collection.

---

### Contact Form

**Description:** Standard form for user inquiries with name, email, and message.

**Content Slots:**
| Slot | Required | Type | Limits | Purpose |
|------|----------|------|--------|---------|
| heading | No | text | 50 chars | Form title |
| name_field | Yes | field | - | User's name |
| email_field | Yes | field | - | User's email |
| message_field | Yes | field | 1000 chars | Message content |
| subject_field | No | field | 100 chars | Message subject |
| submit_button | Yes | text | 20 chars | Submit action |
| success_message | Yes | text | 150 chars | Confirmation message |

**Best For:**
- Contact pages
- Support requests
- General inquiries

**Avoid When:**
- Simple email link suffices
- Complex data collection needed

**Variants:**
- **simple:** Name, email, message only
- **detailed:** Additional fields (phone, company, subject)
- **embedded:** Within footer or sidebar

**Pairs With:** footer-nav, contact information

**Accessibility:** Proper labels, error messages, form validation
**Mobile:** Full-width fields, appropriate keyboard types

---

### Newsletter Signup

**Description:** Email capture form for newsletter subscriptions.

**Content Slots:**
| Slot | Required | Type | Limits | Purpose |
|------|----------|------|--------|---------|
| heading | No | text | 50 chars | Signup prompt |
| description | No | text | 100 chars | Value proposition |
| email_field | Yes | field | - | Email input |
| submit_button | Yes | text | 15 chars | Subscribe action |
| privacy_text | No | text | 100 chars | Privacy note |
| success_message | Yes | text | 100 chars | Confirmation |

**Best For:**
- Email list building
- Content marketing
- Audience engagement

**Avoid When:**
- No newsletter exists
- Already have too many CTAs
- Primary action is different

**Variants:**
- **inline:** Single row (email + button)
- **stacked:** Email above button
- **with-incentive:** Includes offer (discount, free resource)

**Pairs With:** footer-nav, cta-section, blog content

**Accessibility:** Clear labels, success/error states
**Mobile:** Full-width, prominent button

---

### Search Bar

**Description:** Input field for searching site content.

**Content Slots:**
| Slot | Required | Type | Limits | Purpose |
|------|----------|------|--------|---------|
| placeholder | Yes | text | 30 chars | Input placeholder |
| search_button | No | text | 10 chars | Search action |
| autocomplete | No | boolean | - | Show suggestions |

**Best For:**
- Sites with substantial content
- E-commerce product search
- Documentation search
- Blog archives

**Avoid When:**
- Site has < 10 pages
- Content is highly structured (use nav instead)

**Variants:**
- **icon-only:** Expands on click
- **full-width:** Prominent search experience
- **with-filters:** Includes category/type filters

**Pairs With:** navbar, sidebar-nav, filter-controls

**Accessibility:** `role='search'`, proper labeling, keyboard accessible
**Mobile:** Often icon-only that expands

---

### Filter Controls

**Description:** UI for filtering/sorting lists of content.

**Content Slots:**
| Slot | Required | Type | Limits | Purpose |
|------|----------|------|--------|---------|
| filter_categories | Yes | array | - | Filter groupings |
| - category_name | - | text | 20 chars | Filter type label |
| - options | - | array | 10 max | Available filters |
| sort_options | No | array | 5 max | Sort choices |
| clear_filters | Yes | text | 15 chars | Reset action |

**Best For:**
- Product listings
- Search results
- Portfolio/gallery
- Blog archives

**Avoid When:**
- < 10 items to filter
- Single category content
- Complex filtering needs

**Variants:**
- **sidebar:** Vertical filter list
- **horizontal:** Filters in row above content
- **dropdown:** Filters in dropdown menus
- **tags:** Clickable filter tags

**Pairs With:** card-grid, masonry, pagination, search-bar

**Accessibility:** Announce filter changes, maintain focus
**Mobile:** Slide-out filter panel or modal

---

### Multi-Step Form

**Description:** Form split across multiple steps/pages with progress indicator.

**Content Slots:**
| Slot | Required | Type | Limits | Purpose |
|------|----------|------|--------|---------|
| steps | Yes | array | 2-7 steps | Form sections |
| - step_title | - | text | 30 chars | Step name |
| - fields | - | array | - | Step form fields |
| progress_indicator | Yes | - | - | Shows current position |
| back_button | Yes | text | 15 chars | Previous step |
| next_button | Yes | text | 15 chars | Next step |
| submit_button | Yes | text | 20 chars | Final submit |

**Best For:**
- Complex data collection
- Checkout processes
- Application forms
- Onboarding flows

**Avoid When:**
- < 5 fields total
- All fields required for submission
- Users need to see all fields at once

**Variants:**
- **numbered:** Steps shown as numbers
- **progress-bar:** Visual progress bar
- **breadcrumb:** Steps as breadcrumb trail

**Pairs With:** modal, form validation

**Accessibility:** Announce step changes, preserve data, allow back navigation
**Mobile:** Full-screen steps, clear progress

---

### Rating Input

**Description:** Star rating or score input for user feedback.

**Content Slots:**
| Slot | Required | Type | Limits | Purpose |
|------|----------|------|--------|---------|
| label | Yes | text | 40 chars | What is being rated |
| max_rating | Yes | number | 5 or 10 | Maximum score |
| current_value | No | number | - | Pre-selected value |

**Best For:**
- Product reviews
- Service feedback
- User satisfaction
- Content rating

**Avoid When:**
- Nuanced feedback needed
- Rating isn't meaningful
- Binary choice is better

**Variants:**
- **star:** Traditional star icons
- **numeric:** Number scale
- **emoji:** Sentiment icons
- **slider:** Continuous scale

**Pairs With:** review-card, feedback form

**Accessibility:** Keyboard navigation, current value announced
**Mobile:** Large touch targets for stars
