# Concept Section — Content Strategy

**Code:** C4
**Slug:** Content-Strategy
**Output:** `concept/C4-Content-Strategy.txt`
**Wave:** 2 (depends on C1-Sitemap)
**Hypothesis:** Brand voice is undefined and content strategy needs to be built from scratch

## Purpose

Define how the website communicates — tone of voice, messaging, and SEO content plan. Built on the sitemap (which pages exist) and grounded in audience, keyword, and content research.

## Upstream Dependency

**Reads C1-Sitemap output** to know which pages exist and their keyword mappings. The content strategy must align with the sitemap structure — every primary page needs content direction, and the SEO content plan references sitemap pages by name.

## Methodology

1. Read the context file.
2. Produce:
   - **Tone of voice** — how the site should communicate, with concrete examples (phrases, not just adjectives)
   - **Messaging pillars** — 3–5 core themes mapped to personas
   - **Value proposition** — primary statement for the homepage
   - **SEO content plan:**
     - Primary pages with keyword targets and content notes (reference sitemap pages)
     - Supporting SEO pages with keyword targets and rationale
     - Blog topic clusters with keyword targets
   - **Localisation notes** — language and cultural adaptation if secondary languages are active (from project.json language config)

**Note:** Content phasing (what launches when) is handled by C7-Project-Roadmap. Within the SEO content plan, mark launch-critical pages vs post-launch content as an inline note per entry — but the phased delivery plan lives in C7.

## Output

Follow output guide at `templates/C4-Content-Strategy-template.md`.
