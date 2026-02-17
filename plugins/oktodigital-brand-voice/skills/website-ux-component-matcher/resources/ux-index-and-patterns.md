# UX Components Reference: Index & Patterns

**Part 1 of 3** -- Quick reference, content type index, and page patterns.
**Full reference split across:**
- `ux-index-and-patterns.md` (this file) -- Index, page patterns, appendix
- `ux-cat-1-5.md` -- Categories 1-5: Navigation, Hero, Content Display, Disclosure, Forms
- `ux-cat-6-10.md` -- Categories 6-10: Media, Feedback, CTA, Social Proof, E-commerce

**Source:** UX Component Knowledge Base - Reference Guide v1.0.0

---

# UX Component Knowledge Base - Reference Guide

**Version:** 1.0.0
**Date:** 2025-11-26
**Purpose:** Human-readable reference for matching content to UX patterns
**Total Components:** 82
**Categories:** 10

---

## Quick Reference

### How to Use This Guide

1. **By Content Type:** Use the [Content Type Index](#content-type-index) to find components suited for specific content
2. **By Category:** Browse categories to understand component options
3. **By Pattern:** Use [Page Patterns](#page-patterns) for common component combinations

### Key Concepts

- **Content Slots:** The text/media areas within each component
- **Character Limits:** Recommended min/max characters for each slot
- **Content Types:** Tags for matching content to components
- **Anti-patterns:** When NOT to use a component
- **Variants:** Different styles/layouts of the same component

---

## Content Type Index

Quick lookup: What components work for this type of content?

| Content Type | Recommended Components |
|-------------|----------------------|
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

Common component combinations for typical pages:

### Homepage Pattern
```
announcement-bar (optional)
navbar
hero
logo-cloud
feature-grid OR value-prop
stats-bar
testimonial
cta-section
footer-nav
```

### Landing Page Pattern
```
navbar (minimal)
hero
value-prop OR feature-grid
stats-bar
testimonial
pricing-table (if applicable)
cta-section
footer-nav (minimal)
```

### Product/Service Page
```
navbar
hero (product-focused)
feature-grid
comparison-table
testimonial
pricing-table
cta-section
footer-nav
```

### Documentation Page
```
navbar
breadcrumbs
sidebar-nav (sticky)
anchor-nav (table of contents)
accordion (for FAQ sections)
footer-nav
```

### Blog/Article Page
```
navbar
breadcrumbs
article content
anchor-nav (TOC)
card grid (related posts)
newsletter-signup
footer-nav
```

---

## Appendix: Character Limit Guidelines

### Headlines and Titles

| Context | Recommended | Maximum |
|---------|-------------|---------|
| Hero headline | 40-50 chars | 60 chars |
| Card title | 10-40 chars | 60 chars |
| Section heading | 30-50 chars | 60 chars |
| Button text | 10-15 chars | 25 chars |

### Body Text

| Context | Recommended | Maximum |
|---------|-------------|---------|
| Card description | 80-100 chars | 150 chars |
| Testimonial | 150-200 chars | 300 chars |
| Feature description | 80-100 chars | 150 chars |
| Alert message | 80-120 chars | 200 chars |

### Navigation

| Context | Recommended | Maximum |
|---------|-------------|---------|
| Nav item | 8-15 chars | 20 chars |
| Breadcrumb item | 15-20 chars | 30 chars |
| Footer link | 15-20 chars | 25 chars |

### CTAs

| Context | Recommended | Maximum |
|---------|-------------|---------|
| Primary CTA | 10-15 chars | 25 chars |
| Secondary CTA | 10-15 chars | 25 chars |
| Form submit | 8-12 chars | 20 chars |

---

## Related Resources

- **YAML Schema:** `ux-components-schema.yaml` - Machine-parseable version
- **Sources:** `sources-keywords.md` - Research methodology and sources

---

**Version History:**
- 1.0.0 (2025-11-26): Initial release with 82 components
