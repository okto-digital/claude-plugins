# Domain: Performance

**Purpose:** Validate that the brief addresses website speed and performance expectations -- page load targets, Core Web Vitals, image optimization, and caching strategy. Slow websites lose visitors, hurt SEO rankings, and undermine trust. Performance requirements must be set early, not bolted on later.

---

## Priority Definitions

- **CRITICAL:** Brief cannot be accurate without this. Must resolve before drafting.
- **IMPORTANT:** Brief will be thinner without this. Resolve in second pass if time allows.
- **NICE-TO-HAVE:** Useful depth. Surface once, accept skip.

---

## 1. Performance Expectations

| Checkpoint | Priority |
|---|---|
| Page load time target established (e.g., under 3 seconds on mobile) | IMPORTANT |
| Performance is acknowledged as a priority (not an afterthought) | CRITICAL |
| Mobile performance weighted appropriately (often slower connections) | IMPORTANT |
| Current site performance baseline known? (For redesigns) | NICE-TO-HAVE |

## 2. Core Web Vitals

| Checkpoint | Priority |
|---|---|
| LCP (Largest Contentful Paint) target: under 2.5 seconds | IMPORTANT |
| INP (Interaction to Next Paint) target: under 200ms | NICE-TO-HAVE |
| CLS (Cumulative Layout Shift) target: under 0.1 | NICE-TO-HAVE |
| Awareness of Google's page experience signals for SEO | IMPORTANT |

## 3. Image and Media Optimization

| Checkpoint | Priority |
|---|---|
| Image optimization strategy (compression, modern formats like WebP/AVIF) | IMPORTANT |
| Lazy loading for below-the-fold images | IMPORTANT |
| Video hosting approach (self-hosted vs. YouTube/Vimeo embed) | IMPORTANT |
| Hero image/video impact on load time discussed | IMPORTANT |
| Responsive image serving (different sizes for different devices) | NICE-TO-HAVE |

## 4. Caching and Delivery

| Checkpoint | Priority |
|---|---|
| CDN usage planned? (Cloudflare, Fastly, CloudFront, etc.) | IMPORTANT |
| Browser caching strategy for static assets | NICE-TO-HAVE |
| Server-side caching for dynamic content (page cache, object cache) | NICE-TO-HAVE |
| Cache invalidation approach for content updates | NICE-TO-HAVE |

## 5. Third-Party Impact

| Checkpoint | Priority |
|---|---|
| Number of third-party scripts estimated (analytics, chat, ads, fonts, etc.) | IMPORTANT |
| Third-party script loading strategy (async, defer, delayed) | NICE-TO-HAVE |
| Font loading strategy (preload, font-display swap) | NICE-TO-HAVE |
| Impact of required integrations on performance assessed | NICE-TO-HAVE |

## 6. Performance Monitoring

| Checkpoint | Priority |
|---|---|
| Performance monitoring plan post-launch | NICE-TO-HAVE |
| Alerting for performance degradation | NICE-TO-HAVE |
| Regular performance audits planned? | NICE-TO-HAVE |
| Performance budget defined (max JS size, max page weight) | NICE-TO-HAVE |

---

## Question Templates

**How important is website speed to your business?**
- Option A: Very important -- our audience expects fast load times, and we know slow sites lose visitors (especially on mobile)
- Option B: Moderately important -- speed matters but we are willing to trade some speed for richer visual experiences (video, animation, high-res imagery)

**Do you plan to use a lot of video or large imagery on the site?**
- Option A: Yes -- visual storytelling is important to our brand, so we need a strategy to keep the site fast despite media-heavy pages
- Option B: No -- the site will be primarily text and standard imagery, so performance should be straightforward

**Are you comfortable with a CDN (Content Delivery Network) for faster global delivery?**
- Option A: Yes, or we already use one -- we want the best possible speed for visitors everywhere
- Option B: Not sure what that is -- recommend what makes sense for our traffic and budget

**How many third-party tools will be embedded on the site (chat widgets, analytics, marketing pixels)?**
- Option A: Minimal -- just essential analytics (Google Analytics / Tag Manager) and maybe one other tool
- Option B: Several -- analytics, chat widget, marketing pixels, social embeds, and possibly more. We need a loading strategy to prevent slowdowns.

**Should we set specific performance targets that the site must meet at launch?**
- Option A: Yes -- define measurable targets (e.g., under 3s load time, all Core Web Vitals green) and test before launch
- Option B: No formal targets -- just make sure it feels fast and does not frustrate users
