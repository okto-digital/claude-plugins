# SEO Metadata Rules

Rules for writing meta titles, meta descriptions, and selecting schema types. Apply when generating SEO metadata in Write or Optimize modes.

---

## Meta Title

**Length:** 50-60 characters (Google uses pixel width, ~600px desktop)

**Rules:**
- Include primary keyword naturally
- Match H1 as closely as possible (PageOptimizer guidance)
- Be specific and descriptive (prevents Google rewrites)
- Front-load important terms
- Use separator: `|` or `--` before brand name
- Format: `[Primary Keyword Phrase] | [Brand Name]`

**Google rewrites titles when:** keyword-stuffed, generic ("Home", "Services"), too long, misleading, or mismatched with H1.

**Examples:**
```
Good: "Custom Web App Development | okto-digital" (43 chars)
Bad:  "Home - okto-digital" (too generic, will be rewritten)
Bad:  "Web Design Web Development Web Services..." (keyword stuffing)
```

---

## Meta Description

**Length:** 150-160 characters

**Rules:**
- NOT a direct ranking factor, but influences click-through rate
- Include primary keyword (Google bolds matching terms)
- Write a compelling summary that makes users want to click
- Include a benefit or value proposition
- Use active voice and contractions (match brand voice)
- Each page must have a unique description

**Google rewrites descriptions ~62% of the time** based on query relevance. Write them anyway -- they serve as your preferred snippet.

**Examples:**
```
Good: "We build custom web apps tailored to your business. Each project starts with discovery -- we ask questions, listen carefully, and map out exactly what you need." (161 chars)
Bad:  "okto-digital provides web services" (too vague, no value proposition)
```

---

## Schema.org Types by Page

Use JSON-LD format (Google's preference). The development team implements these -- content writers specify which type to use.

| Page Type | Schema Types |
|---|---|
| **Blog posts** | BlogPosting, Person (author), Organization (publisher) |
| **Service pages** | Service, Organization (provider), Offer (pricing) |
| **Product pages** | Product, Offer, AggregateRating, Review |
| **FAQ pages** | FAQPage, Question + Answer (nested) |
| **Case studies** | Article, Organization |
| **Local business** | LocalBusiness, PostalAddress, OpeningHoursSpecification |

---

## Pre-Publish Metadata Checklist

- [ ] Meta title 50-60 characters, includes primary keyword
- [ ] Meta description 150-160 characters, unique per page
- [ ] Title and H1 match closely
- [ ] All images have descriptive alt text
- [ ] URL slug is kebab-case and keyword-relevant
- [ ] No duplicate titles or descriptions across site
- [ ] Schema type identified for the page
