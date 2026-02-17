# SEO Metadata Deep Dive

**Purpose:** Comprehensive technical documentation for SEO metadata optimization
**Audience:** Advanced users, developers, SEO specialists
**Related Skill:** website-seo-metadata

---

## Table of Contents

1. [How Search Engines Use Metadata](#how-search-engines-use-metadata)
2. [Meta Title Technical Specifications](#meta-title-technical-specifications)
3. [OpenGraph Protocol Deep Dive](#opengraph-protocol-deep-dive)
4. [Schema.org Implementation Guide](#schemaorg-implementation-guide)
5. [URL Structure & SEO](#url-structure--seo)
6. [Common Metadata Mistakes](#common-metadata-mistakes)
7. [Testing & Validation](#testing--validation)

---

## How Search Engines Use Metadata

### Google's Metadata Processing

**Title Tag Processing:**
1. Google reads `<title>` tag from HTML
2. Compares with page content for relevance
3. May rewrite if deemed misleading or irrelevant (33% of titles rewritten in 2021 study)
4. Displays in SERPs with query terms bolded
5. Uses as primary ranking signal for keyword relevance

**Meta Description Processing:**
1. NOT a direct ranking factor (confirmed by Google)
2. Influences click-through rate (CTR), which IS a ranking factor
3. Google may rewrite 62% of the time (based on query relevance)
4. Drawn from meta description OR page content
5. Dynamic snippets created for specific queries

**Structured Data Processing:**
1. Crawled and parsed during indexing
2. Validated against schema.org specifications
3. Enables rich results (FAQ, How-to, Product, Recipe, etc.)
4. Errors reported in Google Search Console
5. No direct ranking boost, but improves CTR significantly

---

## Meta Title Technical Specifications

### Character Limits Explained

**Why 50-60 Characters?**
- Google uses **pixel width**, not character count
- Desktop: ~600px width available
- Mobile: ~480px width available
- Wide characters (W, M) use more pixels than narrow (i, l)

**Actual Display Examples:**
```
52 chars, fits: "Web Development Services | YourCompany"
68 chars, truncated: "Complete Guide to Understanding React Server Components in 2024 | TechBlog..."
```

**Calculation Tool:** Use [SERP Snippet Optimizer](https://www.highervisibility.com/seo/tools/serp-snippet-optimizer/) for pixel-width preview

### Title Rewriting Scenarios

**When Google Rewrites Titles (Common Cases):**
1. **Keyword Stuffing:** "Web Design Web Development Web Services Web..."
2. **Template Boilerplate:** "Untitled Document" or "Home - YourSite"
3. **Misleading:** Title promises content not on page
4. **Too Long:** Exceeds reasonable length
5. **Generic:** "Home", "About", "Services"

**How to Prevent Rewrites:**
- Match title to H1 heading
- Include primary keyword naturally
- Be specific and descriptive
- Keep within 50-60 characters
- Avoid keyword stuffing

---

## OpenGraph Protocol Deep Dive

### Image Specifications

**Optimal Dimensions:**
- **Facebook:** 1200 x 630px (1.91:1 ratio)
- **Twitter:** 1200 x 675px (16:9 ratio for summary_large_image)
- **LinkedIn:** 1200 x 627px (1.91:1 ratio)
- **Universal Safe Size:** 1200 x 630px works across all platforms

**Technical Requirements:**
- Format: JPG (best), PNG (good), WEBP (supported), GIF (avoid for main images)
- Max File Size: 8MB (Facebook), 5MB (Twitter)
- Min Size: 200 x 200px (below this, image may not show)
- Color Space: sRGB
- Compression: Balance quality vs file size (aim for <300KB)

**Common Image Issues:**
```html
<!-- WRONG: Relative URL -->
<meta property="og:image" content="/images/og-image.jpg">

<!-- CORRECT: Absolute URL -->
<meta property="og:image" content="https://example.com/images/og-image.jpg">
```

### OpenGraph Caching

**Problem:** Social platforms cache OG images aggressively

**Facebook Cache:**
- Duration: Up to 7 days
- Clearing: Use [Facebook Sharing Debugger](https://developers.facebook.com/tools/debug/)
- Force Refresh: Click "Scrape Again" button

**Twitter Cache:**
- Duration: Up to 7 days
- Clearing: Use [Twitter Card Validator](https://cards-dev.twitter.com/validator)
- No manual refresh - wait or change URL parameter

**Best Practice:** Version OG images in filename
```html
<meta property="og:image" content="https://example.com/images/og-image-v2.jpg">
```

---

## Schema.org Implementation Guide

### JSON-LD vs Microdata

**JSON-LD (Recommended by Google):**
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Complete Guide to React",
  "author": {
    "@type": "Person",
    "name": "Jane Smith"
  }
}
</script>
```

**Advantages:**
- Cleanly separated from HTML
- Easier to generate programmatically
- Google's preferred format
- Can be added anywhere in HTML

**Microdata (Legacy):**
```html
<article itemscope itemtype="https://schema.org/Article">
  <h1 itemprop="headline">Complete Guide to React</h1>
  <p itemprop="author" itemscope itemtype="https://schema.org/Person">
    By <span itemprop="name">Jane Smith</span>
  </p>
</article>
```

**Disadvantages:**
- Clutters HTML
- Harder to maintain
- More error-prone

**Recommendation:** Always use JSON-LD unless legacy system requires Microdata

### Schema Types Priority

**Must-Have Schemas by Page Type:**

**Blog Posts:**
1. BlogPosting or Article
2. Person (author)
3. Organization (publisher)
4. ImageObject (featured image)

**Service Pages:**
1. Service
2. Organization (provider)
3. Offer (pricing)
4. AggregateRating (if reviews exist)

**Product Pages:**
1. Product
2. Offer
3. AggregateRating
4. Review

**FAQ Pages:**
1. FAQPage
2. Question + Answer (nested)

**Local Business:**
1. LocalBusiness
2. PostalAddress
3. GeoCoordinates
4. OpeningHoursSpecification

---

## URL Structure & SEO

### URL Best Practices

**Optimal URL Length:**
- **Ideal:** 50-60 characters
- **Maximum:** 2,083 characters (browser limit)
- **Google Recommendation:** Keep URLs "reasonably short"

**Hierarchical Structure:**
```
✅ GOOD:
https://example.com/services/web-development
https://example.com/blog/react/server-components

❌ BAD:
https://example.com/services/web-development/custom-websites/responsive-design/mobile-first
(Too deep - max 3-4 levels)
```

**URL Parameters:**
```
✅ GOOD (canonical points to clean URL):
https://example.com/products/widget?ref=email
<link rel="canonical" href="https://example.com/products/widget">

❌ BAD (no canonical):
https://example.com/products/widget?ref=email
https://example.com/products/widget?utm_source=twitter
(Creates duplicate content)
```

### URL Migration

**When Changing URLs (301 Redirects):**
```
Old URL: /services/web-design
New URL: /services/web-development

.htaccess:
Redirect 301 /services/web-design /services/web-development
```

**Important:**
- 301 passes 90-99% of link equity
- Update internal links to point directly to new URL
- Update sitemap.xml
- Monitor 404 errors in Search Console

---

## Common Metadata Mistakes

### 1. Duplicate Meta Descriptions

**Problem:** Same description across multiple pages
```
About Page: "YourCompany provides web services"
Services Page: "YourCompany provides web services"
Contact Page: "YourCompany provides web services"
```

**Impact:** Reduced CTR, missed keyword opportunities

**Solution:** Unique description for every page

### 2. Missing Alt Text

**Problem:** Images without alt attributes
```html
<img src="product.jpg">
```

**Impact:**
- Accessibility fail (screen readers can't describe)
- Lost image search traffic
- Missed keyword opportunity

**Solution:**
```html
<img src="product.jpg" alt="AI Writing Assistant Pro dashboard showing template library">
```

### 3. Broken Canonical URLs

**Problem:** Canonical points to wrong page
```html
<!-- Page A -->
<link rel="canonical" href="https://example.com/page-b">

<!-- Page B -->
<link rel="canonical" href="https://example.com/page-a">
```

**Impact:** Circular canonicals confuse search engines

**Solution:** Most pages should self-reference
```html
<link rel="canonical" href="https://example.com/page-a">
```

### 4. Schema Validation Errors

**Common Errors:**
- Missing required fields (e.g., Article without datePublished)
- Wrong @type for content
- Invalid URLs (relative instead of absolute)
- Mismatched data (title in schema differs from page title)

**Solution:** Validate with [Google Rich Results Test](https://search.google.com/test/rich-results)

---

## Testing & Validation

### Essential Testing Tools

**Meta Tags:**
- [HeadMeta.com](https://www.headmeta.com/) - Visual preview of all meta tags
- Chrome DevTools → Elements → `<head>` section

**OpenGraph:**
- [Facebook Sharing Debugger](https://developers.facebook.com/tools/debug/)
- [LinkedIn Post Inspector](https://www.linkedin.com/post-inspector/)
- [OpenGraph.xyz](https://www.opengraph.xyz/)

**Twitter Cards:**
- [Twitter Card Validator](https://cards-dev.twitter.com/validator)

**Schema.org:**
- [Google Rich Results Test](https://search.google.com/test/rich-results)
- [Schema Markup Validator](https://validator.schema.org/)

**Complete Site Audit:**
- [Screaming Frog SEO Spider](https://www.screamingfrogseosuite.co.uk/) - Crawl entire site for metadata issues
- Google Search Console → Coverage Report

### Pre-Launch Checklist

**Before Publishing Content:**
- [ ] Meta title 50-60 characters
- [ ] Meta description 150-160 characters
- [ ] OG image 1200x630px, absolute URL
- [ ] All images have alt text
- [ ] Canonical URL set correctly
- [ ] Schema.org markup validated
- [ ] URL slug optimized (kebab-case, keyword-rich)
- [ ] No duplicate titles/descriptions across site
- [ ] Test social previews on Facebook/Twitter/LinkedIn

---

## Advanced Topics

### Dynamic Metadata Generation

**For Blog Posts (Template Example):**
```javascript
// Generate meta title
const metaTitle = `${post.title} | ${siteName}`;

// Generate meta description (first 160 chars of content)
const metaDescription = post.excerpt ||
  post.content.substring(0, 157) + '...';

// Generate OG image (dynamic based on title)
const ogImage = `https://example.com/api/og?title=${encodeURIComponent(post.title)}`;
```

### Internationalization (i18n)

**Language-Specific Metadata:**
```html
<!-- English Version -->
<html lang="en">
<title>Web Development Services | YourCompany</title>
<link rel="alternate" hreflang="es" href="https://example.com/es/servicios">

<!-- Spanish Version -->
<html lang="es">
<title>Servicios de Desarrollo Web | YourCompany</title>
<link rel="alternate" hreflang="en" href="https://example.com/en/services">
```

---

**Document Version:** 1.0.0
**Last Updated:** 2024-11-21
**Related:** website-seo-metadata SKILL.md