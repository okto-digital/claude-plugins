# UX Components Reference

Reference for matching content to UX patterns. Use this when suggesting component layouts in outlines or drafts.

---

## Content Type Index

| Content Type | Recommended Components |
|---|---|
| **FAQ** | accordion, anchor-nav, tabs |
| **Marketing** | hero, cta-section, value-prop, feature-grid |
| **Blog/Articles** | card, masonry, pagination, anchor-nav |
| **Product Info** | product-card, pricing-table, comparison-table, product-gallery |
| **Social Proof** | testimonial, review-card, logo-cloud, stats-bar, trust-badges |
| **Navigation** | navbar, footer-nav, breadcrumbs, sidebar-nav, tabs |
| **Forms** | contact-form, newsletter-signup, multi-step-form |
| **Team/People** | card, avatar, testimonial |
| **Features** | feature-grid, bento-grid, value-prop, tabs |
| **Legal/Policy** | accordion, anchor-nav |
| **Documentation** | sidebar-nav, anchor-nav, tabs, accordion |
| **E-commerce** | product-card, pricing-table, cart-preview, checkout-summary |
| **Announcements** | announcement-bar, alert, toast |
| **Media** | image-gallery, lightbox, video-embed, carousel |

---

## Page Patterns

### Homepage
```
announcement-bar (optional) > navbar > hero > logo-cloud > feature-grid OR value-prop > stats-bar > testimonial > cta-section > footer-nav
```

### Landing Page
```
navbar (minimal) > hero > value-prop OR feature-grid > stats-bar > testimonial > pricing-table (if applicable) > cta-section > footer-nav (minimal)
```

### Product/Service Page
```
navbar > hero (product-focused) > feature-grid > comparison-table > testimonial > pricing-table > cta-section > footer-nav
```

### Blog/Article Page
```
navbar > breadcrumbs > article content > anchor-nav (TOC) > card grid (related posts) > newsletter-signup > footer-nav
```

### Documentation Page
```
navbar > breadcrumbs > sidebar-nav (sticky) > anchor-nav (TOC) > accordion (FAQ) > footer-nav
```

---

## Component Catalog

82 components across 10 categories. Each entry shows name, purpose, and best content use cases.

### Navigation & Wayfinding

| Component | Purpose | Best For |
|---|---|---|
| **navbar** | Primary horizontal navigation with logo, links, CTA | Every page, brand presence |
| **mega-menu** | Large dropdown with multiple nav groups in columns | Sites with 20+ pages, e-commerce |
| **mobile-drawer** | Slide-out navigation panel for mobile | Mobile navigation, responsive sites |
| **breadcrumbs** | Hierarchical trail showing page location | Deep hierarchical sites, e-commerce |
| **pagination** | Page-by-page navigation for split content | Blog archives, search results, product listings |
| **tabs** | Switch between content panels | Related content groups, feature comparisons, settings |
| **anchor-nav** | In-page navigation linking to sections (TOC) | Long-form content, docs, FAQ, legal |
| **footer-nav** | Site-wide footer with nav columns, contact, legal | Every page |
| **sidebar-nav** | Vertical navigation for docs or dashboards | Documentation, admin, settings |

### Hero & Landing

| Component | Purpose | Best For |
|---|---|---|
| **hero** | Large prominent section with headline, subheadline, CTA | Homepage, landing pages, campaign pages |
| **announcement-bar** | Thin banner for promotions or urgent messages | Sales, product launches, important updates |
| **stats-bar** | Row of key metrics with numbers and labels | Social proof, company achievements, trust building |
| **logo-cloud** | Collection of client/partner logos | B2B credibility, trust, press mentions |
| **value-prop** | Key benefits or unique selling points with icons | Explaining product value, highlighting differentiators |

### Content Display

| Component | Purpose | Best For |
|---|---|---|
| **card** | Contained unit with image, title, description, action | Blog previews, team members, portfolio items |
| **bento-grid** | Asymmetric grid with varied cell sizes | Feature showcases, portfolio, dashboards |
| **masonry** | Variable-height grid (Pinterest-style) | Image galleries, mixed content, portfolio |
| **timeline** | Chronological display of events or milestones | Company history, project milestones, process |
| **comparison-table** | Side-by-side feature/product comparison | Pricing tiers, feature matrices, decision support |
| **feature-grid** | Grid of features with icons and descriptions | Product features, service offerings, capabilities |
| **testimonial** | Customer quote with attribution and photo | Social proof, trust building, customer success |
| **quote-block** | Standalone quote for emphasis within content | Highlighting key points, expert opinions |

### Disclosure & Progressive

| Component | Purpose | Best For |
|---|---|---|
| **accordion** | Collapsible content sections | FAQ, feature details, legal/policy, help docs |
| **collapsible** | Single expandable section | Additional details, "read more" patterns |
| **tooltip** | Small popup on hover/focus with extra info | Form field help, term definitions, icon labels |
| **modal** | Overlay dialog for focused interaction | Confirmations, forms, detail views, media |

### Forms & Input

| Component | Purpose | Best For |
|---|---|---|
| **contact-form** | Standard contact form with fields and submit | Contact pages, service inquiries |
| **newsletter-signup** | Email capture form | Blog footers, content gates, popups |
| **search-bar** | Text input with search functionality | Documentation, e-commerce, content-heavy sites |
| **filter-controls** | Sorting and filtering for content collections | Product listings, blog archives, directories |
| **multi-step-form** | Form split into sequential steps | Complex forms (checkout, onboarding, applications) |
| **rating-input** | Star or scale rating input | Reviews, feedback, surveys |

### Media

| Component | Purpose | Best For |
|---|---|---|
| **image-gallery** | Grid of images with optional lightbox | Portfolio, product photos, case studies |
| **lightbox** | Full-screen overlay for media viewing | Image detail, gallery expansion |
| **video-embed** | Embedded video player | Tutorials, testimonials, product demos |
| **carousel** | Horizontal scrolling content panels | Testimonials, product images, feature tours |
| **avatar** | User/team member photo with name and role | Team pages, comments, user profiles |

### Feedback & Status

| Component | Purpose | Best For |
|---|---|---|
| **alert** | Prominent banner for important messages | Warnings, success confirmations, errors |
| **toast** | Temporary notification popup | Action confirmations, background updates |
| **progress-indicator** | Visual progress through multi-step process | Multi-step forms, onboarding, file uploads |
| **empty-state** | Placeholder for sections with no content yet | New accounts, empty search results, first-use |
| **error-state** | Error display with recovery guidance | 404 pages, failed loads, form errors |
| **skeleton-loader** | Placeholder showing content structure while loading | Content-heavy pages, dynamic content |

### Conversion

| Component | Purpose | Best For |
|---|---|---|
| **cta-button** | Standalone call-to-action button | Primary actions, inline content CTAs |
| **cta-section** | Full-width section with headline and CTA | Page closers, mid-content conversion points |
| **sticky-cta** | Fixed CTA that stays visible while scrolling | Long pages, mobile conversion |
| **exit-intent** | Popup triggered when user is about to leave | Lead capture, special offers, newsletter signup |

### Social Proof

| Component | Purpose | Best For |
|---|---|---|
| **review-card** | Individual review with rating and text | Product reviews, service feedback |
| **case-study-preview** | Summary card linking to full case study | Portfolio sections, results showcase |
| **trust-badges** | Security, certification, or guarantee icons | Checkout pages, form sections, footer |

### E-commerce

| Component | Purpose | Best For |
|---|---|---|
| **product-card** | Product listing with image, price, action | Product grids, search results, recommendations |
| **pricing-table** | Tiered pricing comparison | SaaS pricing, service packages |
| **product-gallery** | Multiple product images with thumbnails | Product detail pages |
| **cart-preview** | Mini cart showing selected items | Header/sidebar persistent cart |
| **checkout-summary** | Order summary during checkout | Checkout flow |

---

## Character Limit Guidelines

### Headlines and Titles

| Context | Recommended | Maximum |
|---|---|---|
| Hero headline | 40-50 chars | 60 chars |
| Card title | 10-40 chars | 60 chars |
| Section heading | 30-50 chars | 60 chars |
| Button text | 10-15 chars | 25 chars |

### Body Text

| Context | Recommended | Maximum |
|---|---|---|
| Card description | 80-100 chars | 150 chars |
| Testimonial | 150-200 chars | 300 chars |
| Feature description | 80-100 chars | 150 chars |
| Alert message | 80-120 chars | 200 chars |

### Navigation

| Context | Recommended | Maximum |
|---|---|---|
| Nav item | 8-15 chars | 20 chars |
| Breadcrumb item | 15-20 chars | 30 chars |
| Footer link | 15-20 chars | 25 chars |

### CTAs

| Context | Recommended | Maximum |
|---|---|---|
| Primary CTA | 10-15 chars | 25 chars |
| Secondary CTA | 10-15 chars | 25 chars |
| Form submit | 8-12 chars | 20 chars |
