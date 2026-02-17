---
name: website-seo-metadata
description: "Technical SEO metadata optimization for website content including meta tags, OpenGraph, Twitter Cards, structured data, and URL optimization. Use when generating SEO metadata, optimizing meta tags, creating social media preview metadata, or configuring structured data."
allowed-tools: Read
version: 1.0.0
---

# Website SEO Metadata

**Purpose:** Technical SEO metadata optimization including meta tags, OpenGraph, Twitter Cards, structured data, and URL optimization

**For comprehensive technical details, see:** `${CLAUDE_PLUGIN_ROOT}/skills/website-seo-metadata/resources/seo-metadata-deep-dive.md`

---

## Skill Overview

This skill provides technical SEO metadata recommendations for website content. It ensures all content has proper meta tags, social media preview metadata, URL structure, alt text, and structured data.

**What this skill does:**
- Analyze content and recommend meta titles and descriptions
- Generate OpenGraph metadata for social media previews
- Create Twitter Card metadata
- Optimize URL slugs
- Provide alt text recommendations for images
- Suggest Schema.org structured data
- Handle canonical URLs and robots directives

**What this skill does NOT do:**
- Write content (only metadata)
- Modify brand voice definitions
- Make strategic architecture decisions
- Handle CTA placement or conversion optimization

---

## Core Metadata Components

### 1. Meta Title
- **Length:** 50-60 characters (max 600px width)
- **Primary keyword** near beginning (first 5 words)
- **Brand name** at end with separator
- **Unique** per page
- **Format:** `Primary Keyword - Benefit | Brand Name`

### 2. Meta Description
- **Length:** 150-160 characters
- **Include** primary keyword naturally
- **Compelling** value proposition, answer "What will I learn/get?"
- **Unique** per page
- No direct ranking impact, but affects CTR significantly

### 3. OpenGraph Metadata
Required fields for social sharing (Facebook, LinkedIn, Slack, Discord):
- `og:title` -- Can differ from page title (~60 chars)
- `og:description` -- Social-focused copy (~200 chars)
- `og:image` -- **Absolute URL**, min 1200x630px, max 8MB
- `og:url` -- Canonical URL (absolute)
- `og:type` -- "website", "article", or "product"

Optional: `og:site_name`, `og:locale`, `og:image:alt`

Article-specific: `article:author`, `article:published_time`, `article:modified_time`, `article:section`, `article:tag`

### 4. Twitter Card Metadata
- `twitter:card` -- Use `"summary_large_image"` for most content
- `twitter:title` -- Falls back to og:title (~70 chars)
- `twitter:description` -- Falls back to og:description (~200 chars)
- `twitter:image` -- Falls back to og:image (min 300x157px)
- Optional: `twitter:site`, `twitter:creator`, `twitter:image:alt`

### 5. URL Slug
- **Format:** kebab-case (lowercase with hyphens)
- **Length:** 3-5 words
- **Include** primary keyword
- **Never change** after publication
- Remove stop words when reasonable
- Validation regex: `^[a-z0-9]+(?:-[a-z0-9]+)*$`

### 6. Image Alt Text
- **Descriptive:** ~125 characters
- **Keyword-rich** naturally
- Don't start with "Image of" or "Picture of"
- Empty `alt=""` for decorative images

### 7. Canonical URL
- **Absolute URL** required
- Self-referencing for most pages
- Points to main page for paginated content
- Points to original for syndicated content

### 8. Robots Meta Tag
- `"index, follow"` -- Published content (default)
- `"noindex, follow"` -- Draft/staging, thin content, thank-you pages
- `"noindex, nofollow"` -- Admin/private pages
- `"noarchive"` -- Time-sensitive content

### 9. Schema.org Structured Data
Common types by page:
- **Blog posts:** `BlogPosting` (headline, author, publisher, dates)
- **Service pages:** `Service` (serviceType, provider, offers)
- **Product pages:** `Product` (name, brand, offers, aggregateRating)
- **FAQ sections:** `FAQPage` (mainEntity with Question/Answer pairs)
- **Local pages:** `LocalBusiness` (address, geo, telephone, openingHours)

**Validate with:** Google Rich Results Test

---

## Decision Framework

### Step 1: Identify Page Type
Service page / Blog post / Product page / Landing page / Documentation -> Use corresponding metadata template from `resources/seo-metadata-deep-dive.md`.

### Step 2: Core Meta Tags
- [ ] Title: 50-60 chars, primary keyword first, brand name at end, unique
- [ ] Description: 150-160 chars, primary keyword, compelling, unique

### Step 3: Social Metadata
- [ ] og:title, og:description, og:image (1200x630, absolute URL), og:type, og:url
- [ ] twitter:card: "summary_large_image"

### Step 4: URL Slug
- [ ] kebab-case, 3-5 words, includes primary keyword, human-readable

### Step 5: Image Alt Text
- [ ] Descriptive (~125 chars), relevant keywords, no "Image of..."

### Step 6: Canonical URL
- [ ] Absolute URL, points to preferred version

### Step 7: Robots Directive
- [ ] Appropriate for page type and status

### Step 8: Structured Data
- [ ] Appropriate @type selected, required fields included, validated

---

## Quality Checklist

**Uniqueness:**
- [ ] Meta title unique across all pages
- [ ] Meta description unique across all pages
- [ ] URL slug unique across all pages

**Completeness:**
- [ ] Meta title, description, URL slug, canonical URL all present
- [ ] OG image present (absolute URL, 1200x630)
- [ ] All image alt text present

**Optimization:**
- [ ] Primary keyword in title, description, and URL slug
- [ ] Character limits respected
- [ ] Schema.org type appropriate for page

**Brand Consistency:**
- [ ] Brand name in meta title
- [ ] Brand voice in meta description
- [ ] Consistent separator usage

---

## Output Format

```yaml
# SEO METADATA RECOMMENDATIONS

## Core Meta Tags
title: "[Optimized title 50-60 chars]"
description: "[Optimized description 150-160 chars]"

## URL
slug: "[optimized-slug]"
canonicalUrl: "[absolute URL]"
robots: "[directive]"

## OpenGraph
ogTitle: "[Social-optimized title]"
ogDescription: "[Social-optimized description]"
ogImage: "[absolute URL to 1200x630 image]"
ogImageAlt: "[Image description]"
ogType: "[website|article|product]"
ogUrl: "[canonical URL]"

## Twitter Card
twitterCard: "summary_large_image"

## Image Alt Text
- Image 1: "[descriptive alt text]"

## Schema.org
schema:
  "@type": "[SchemaType]"
  [required fields...]
```

---

## Reference Files

- `resources/seo-metadata-deep-dive.md` -- How search engines process metadata, full OpenGraph/Twitter specifications, Schema.org JSON-LD examples, page type metadata templates, common mistakes, testing tools

---

**Version:** 1.0.0
