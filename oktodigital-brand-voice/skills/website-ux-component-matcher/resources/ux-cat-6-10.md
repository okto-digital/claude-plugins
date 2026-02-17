# UX Components Reference: Categories 6-10

**Part 3 of 3** -- Media & Visual, Feedback & Status, Call-to-Action, Social Proof, E-commerce Specific.
**Full reference split across:**
- `ux-index-and-patterns.md` -- Index, page patterns, appendix
- `ux-cat-1-5.md` -- Categories 1-5
- `ux-cat-6-10.md` (this file) -- Categories 6-10

**Source:** UX Component Knowledge Base - Reference Guide v1.0.0

---

## Category 6: Media & Visual

Components for displaying images, video, and visual content.

---

### Image Gallery

**Description:** Collection of images displayed together.

**Content Slots:**
| Slot | Required | Type | Limits | Purpose |
|------|----------|------|--------|---------|
| images | Yes | array | - | Gallery images |
| - src | - | image | - | Image source |
| - alt | - | text | 125 chars | Alt text |
| - caption | - | text | 100 chars | Image caption |
| gallery_title | No | text | 50 chars | Gallery heading |

**Best For:**
- Portfolio displays
- Product images
- Event photos
- Case studies

**Avoid When:**
- Single image suffices
- Images need context/explanation
- Heavy page weight concern

**Variants:**
- **grid:** Equal-sized thumbnails
- **masonry:** Variable heights
- **carousel:** One at a time with navigation

**Pairs With:** lightbox, filter-controls

**Accessibility:** Alt text for all images, keyboard navigation
**Mobile:** Swipeable carousel often better

---

### Lightbox

**Description:** Overlay that displays enlarged media with navigation.

**Content Slots:**
| Slot | Required | Type | Limits | Purpose |
|------|----------|------|--------|---------|
| media_item | Yes | image/video | - | Enlarged content |
| caption | No | text | 200 chars | Media description |
| navigation | Yes | - | - | Prev/next controls |
| close_button | Yes | - | - | Dismiss action |

**Best For:**
- Image galleries
- Product photos
- Portfolio details
- Full-size image viewing

**Avoid When:**
- Images work at current size
- Quick browsing is priority
- Touch devices are primary

**Variants:**
- **simple:** Image only
- **with-caption:** Includes description
- **gallery:** Multiple items with navigation

**Pairs With:** image-gallery, card, product-gallery

**Accessibility:** Focus trap, keyboard navigation, escape to close
**Mobile:** Often swipe navigation, close button prominent

---

### Video Embed

**Description:** Embedded video player from YouTube, Vimeo, or self-hosted.

**Content Slots:**
| Slot | Required | Type | Limits | Purpose |
|------|----------|------|--------|---------|
| video_url | Yes | url | - | Video source |
| title | No | text | 60 chars | Video title |
| description | No | text | 200 chars | Video description |
| thumbnail | No | image | - | Preview image |
| autoplay | No | boolean | false | Auto-start video |

**Best For:**
- Product demos
- Tutorials
- Testimonials
- Marketing content

**Avoid When:**
- Page load performance critical
- Content works as text/images
- Audio not appropriate

**Variants:**
- **inline:** Within content flow
- **full-width:** Spans container width
- **background:** Autoplaying ambient video
- **modal:** Opens in overlay

**Pairs With:** hero, feature sections, testimonial

**Accessibility:** Captions/transcripts, pause control, no autoplay with sound
**Mobile:** Consider data usage, offer thumbnail click-to-play

---

### Carousel / Slider

**Description:** Horizontally scrolling content with navigation controls.

**Content Slots:**
| Slot | Required | Type | Limits | Purpose |
|------|----------|------|--------|---------|
| slides | Yes | array | 3-10 | Carousel items |
| navigation | Yes | - | - | Prev/next controls |
| indicators | No | - | - | Dots or thumbnails |
| autoplay | No | boolean | false | Auto-advance |
| autoplay_speed | No | number | 5000ms | Time between slides |

**Best For:**
- Testimonials
- Featured content
- Product highlights
- Image galleries

**Avoid When:**
- Users need to compare items
- Content is critical (often missed)
- Mobile is primary (swipe fatigue)
- > 10 slides

**Variants:**
- **single:** One slide visible
- **multi:** Multiple slides visible
- **fade:** Crossfade transition
- **infinite:** Loops continuously

**Pairs With:** testimonial, card, product-card

**Accessibility:** Pause button, keyboard navigation, avoid autoplay
**Mobile:** Swipe enabled, visible indicators

---

### Avatar

**Description:** Circular image representing a user or person.

**Content Slots:**
| Slot | Required | Type | Limits | Purpose |
|------|----------|------|--------|---------|
| image | No | image | - | Person's photo |
| fallback | Yes | text | 2 chars | Initials if no image |
| name | Yes | text | 50 chars | Person's name (for alt) |
| size | Yes | enum | xs, sm, md, lg, xl | Avatar dimensions |

**Best For:**
- User profiles
- Team members
- Comments/reviews
- Testimonials

**Avoid When:**
- Person's identity not relevant
- Photo not available and initials meaningless

**Variants:**
- **image:** Photo avatar
- **initials:** Letters on colored background
- **icon:** Generic person icon
- **group:** Multiple avatars stacked

**Pairs With:** testimonial, review-card, team card

**Accessibility:** Alt text with person's name
**Mobile:** Consistent sizing across breakpoints

---

## Category 7: Feedback & Status

Components for communicating system state and user feedback.

---

### Alert / Banner

**Description:** Prominent message for important information, warnings, or errors.

**Content Slots:**
| Slot | Required | Type | Limits | Purpose |
|------|----------|------|--------|---------|
| type | Yes | enum | info, success, warning, error | Alert severity |
| title | No | text | 50 chars | Alert heading |
| message | Yes | text | 200 chars | Alert content |
| action | No | text | 20 chars | Optional action |
| dismissible | No | boolean | - | Can be closed |

**Best For:**
- Form validation results
- System status messages
- Important notifications
- Action confirmations

**Avoid When:**
- Message is routine
- Toast would be less intrusive
- Multiple simultaneous alerts

**Variants:**
- **inline:** Within content flow
- **full-width:** Spans container
- **floating:** Fixed position on screen
- **toast-style:** Auto-dismissing

**Pairs With:** forms, user actions

**Accessibility:** `role='alert'` for important, appropriate colors for severity
**Mobile:** Full-width, don't obscure content

---

### Toast Notification

**Description:** Brief, auto-dismissing notification that appears temporarily.

**Content Slots:**
| Slot | Required | Type | Limits | Purpose |
|------|----------|------|--------|---------|
| message | Yes | text | 80 chars | Notification text |
| type | Yes | enum | info, success, warning, error | Notification type |
| duration | Yes | number | 3000-8000ms | Display time |
| action | No | text | 15 chars | Optional undo/action |

**Best For:**
- Action confirmations
- Background process updates
- Non-critical notifications
- Undo opportunities

**Avoid When:**
- Message requires action
- Information is critical
- User must acknowledge

**Variants:**
- **simple:** Text only
- **with-icon:** Icon + text
- **with-action:** Includes action button
- **stacked:** Multiple toasts queue

**Pairs With:** user actions, forms

**Accessibility:** `role='status'`, don't rely solely on color, sufficient duration
**Mobile:** Full-width at bottom, swipe to dismiss

---

### Progress Indicator

**Description:** Visual representation of process completion.

**Content Slots:**
| Slot | Required | Type | Limits | Purpose |
|------|----------|------|--------|---------|
| current_value | Yes | number | 0-100 | Current progress |
| label | No | text | 30 chars | Progress description |
| show_percentage | No | boolean | - | Display % value |

**Best For:**
- File uploads
- Form completion
- Loading states
- Multi-step processes

**Avoid When:**
- Duration is unknown (use spinner)
- Progress is instant
- Multiple simultaneous processes

**Variants:**
- **bar:** Horizontal progress bar
- **circular:** Ring/donut progress
- **steps:** Discrete step indicator
- **indeterminate:** Loading without percentage

**Pairs With:** multi-step-form, file-upload, loading states

**Accessibility:** `role='progressbar'`, `aria-valuenow`, announce changes
**Mobile:** Visible and clear progress indication

---

### Empty State

**Description:** Placeholder content when no data is available.

**Content Slots:**
| Slot | Required | Type | Limits | Purpose |
|------|----------|------|--------|---------|
| illustration | No | image | - | Visual representation |
| title | Yes | text | 40 chars | Empty state heading |
| description | Yes | text | 120 chars | Explanation/guidance |
| action | No | text | 20 chars | Primary action to remedy |

**Best For:**
- Empty lists/tables
- No search results
- First-time user states
- Cleared data

**Avoid When:**
- Data is loading (use skeleton)
- Error occurred (use error state)

**Variants:**
- **simple:** Text only
- **illustrated:** With graphic/illustration
- **actionable:** Includes CTA to add content

**Pairs With:** tables, lists, search results

**Accessibility:** Clear explanation of why empty and how to add content
**Mobile:** Centered, appropriately sized

---

### Error State

**Description:** UI for displaying errors with recovery options.

**Content Slots:**
| Slot | Required | Type | Limits | Purpose |
|------|----------|------|--------|---------|
| error_code | No | text | 10 chars | Error code (404, 500) |
| title | Yes | text | 50 chars | Error heading |
| description | Yes | text | 150 chars | What happened |
| primary_action | Yes | text | 20 chars | Recovery action |
| secondary_action | No | text | 20 chars | Alternative action |

**Best For:**
- Page not found (404)
- Server errors
- Failed operations
- Connection issues

**Avoid When:**
- Error is minor (use toast)
- Inline validation (use field error)

**Variants:**
- **full-page:** Entire page is error
- **section:** Error within section
- **inline:** Error within component

**Pairs With:** retry functionality, navigation

**Accessibility:** Clear error message, actionable recovery steps
**Mobile:** Full-width, clear action buttons

---

### Skeleton Loader

**Description:** Placeholder UI mimicking content layout while loading.

**Content Slots:**
| Slot | Required | Type | Limits | Purpose |
|------|----------|------|--------|---------|
| layout_type | Yes | enum | - | Type of content loading |
| elements | Yes | array | - | Placeholder shapes |

**Best For:**
- Initial page loads
- Lazy-loaded content
- API data fetching
- Image loading

**Avoid When:**
- Load time is < 200ms
- Simple spinner suffices
- Content structure unknown

**Variants:**
- **pulse:** Animated pulsing effect
- **shimmer:** Wave animation
- **static:** No animation

**Pairs With:** card, table, list items

**Accessibility:** `aria-busy='true'`, announce when loading complete
**Mobile:** Match actual content layout

---

## Category 8: Call-to-Action

Components for driving user action and conversion.

---

### CTA Button

**Description:** Prominent button encouraging specific user action.

**Content Slots:**
| Slot | Required | Type | Limits | Purpose |
|------|----------|------|--------|---------|
| button_text | Yes | text | 5-25 chars, 4 words max | Action text |
| icon | No | icon | - | Supporting icon |
| style | Yes | enum | primary, secondary, outline | Visual emphasis |

**Best For:**
- Primary page actions
- Form submissions
- Navigation to key pages
- Conversion points

**Avoid When:**
- Multiple equal-priority actions
- Text link would be cleaner

**Writing Guidelines:**
- Use action verbs: Get, Start, Try, Join, Download, Sign Up
- Be specific: "Start Free Trial" > "Submit"
- Create urgency when appropriate

**Variants:**
- **primary:** Filled, high emphasis
- **secondary:** Less prominent
- **outline:** Border only
- **text:** Link style

**Pairs With:** forms, hero, cta-section

**Accessibility:** Clear focus state, descriptive text
**Mobile:** Min 44x44px touch target, full-width in some contexts

---

### CTA Section

**Description:** Dedicated section encouraging specific action with headline and button.

**Content Slots:**
| Slot | Required | Type | Limits | Purpose |
|------|----------|------|--------|---------|
| headline | Yes | text | 60 chars | Action-driving heading |
| subheadline | No | text | 150 chars | Supporting text |
| primary_cta | Yes | text | 25 chars | Primary action |
| secondary_cta | No | text | 25 chars | Alternative action |
| background | No | enum | color, image, gradient | Visual style |

**Best For:**
- End of page conversion
- Mid-page engagement
- Feature page conclusions
- Pricing page bottoms

**Avoid When:**
- Too many CTAs on page
- Action isn't clear
- Better served by inline CTA

**Variants:**
- **centered:** All content centered
- **split:** Text and button in columns
- **full-bleed:** Background spans viewport
- **minimal:** Simple text and button

**Pairs With:** testimonial, stats-bar, footer-nav

**Accessibility:** High contrast, clear action
**Mobile:** Stack vertically, full-width button

---

### Sticky CTA Bar

**Description:** Fixed-position CTA that remains visible while scrolling.

**Content Slots:**
| Slot | Required | Type | Limits | Purpose |
|------|----------|------|--------|---------|
| message | No | text | 60 chars | Brief text |
| cta_text | Yes | text | 20 chars | Action button |
| position | Yes | enum | top, bottom | Fixed position |
| show_after | No | number | - | Scroll distance before showing |

**Best For:**
- Long-form content
- Product pages
- Pricing pages
- Registration pushes

**Avoid When:**
- Page is short
- Primary CTA in viewport
- Would block important content

**Variants:**
- **top:** Fixed to top of viewport
- **bottom:** Fixed to bottom
- **sliding:** Slides in after scroll

**Pairs With:** long-form content, product pages

**Accessibility:** Don't cover important content, dismissible option
**Mobile:** Full-width, consider scroll direction hide/show

---

### Exit Intent Popup

**Description:** Modal that appears when user shows intent to leave page.

**Content Slots:**
| Slot | Required | Type | Limits | Purpose |
|------|----------|------|--------|---------|
| headline | Yes | text | 50 chars | Attention-grabbing heading |
| offer | Yes | text | 100 chars | Value proposition |
| cta_text | Yes | text | 20 chars | Primary action |
| dismiss_text | Yes | text | 20 chars | Close option |
| image | No | image | - | Supporting visual |

**Best For:**
- Lead capture
- Cart abandonment
- Special offers
- Newsletter signups

**Avoid When:**
- User just arrived
- Already converted
- Mobile (exit intent hard to detect)

**Variants:**
- **offer:** Discount or incentive
- **newsletter:** Email capture
- **feedback:** Exit survey
- **reminder:** Cart contents

**Pairs With:** newsletter-signup, discount offer

**Accessibility:** Focus trap, easy dismiss, don't block on mobile
**Mobile:** Often disabled or timing-based instead

---

## Category 9: Social Proof

Components for building trust through third-party validation.

---

### Review Card

**Description:** Individual customer review with rating and content.

**Content Slots:**
| Slot | Required | Type | Limits | Purpose |
|------|----------|------|--------|---------|
| rating | Yes | number | 1-5 | Star rating |
| review_title | No | text | 60 chars | Review headline |
| review_text | Yes | text | 300 chars | Review content |
| reviewer_name | Yes | text | 40 chars | Reviewer name |
| reviewer_info | No | text | 50 chars | Location, verified, date |
| product_name | No | text | 50 chars | What was reviewed |

**Best For:**
- Product pages
- Service pages
- Trust building
- Customer feedback

**Avoid When:**
- Reviews aren't genuine
- Insufficient reviews
- Negative reviews dominate

**Variants:**
- **compact:** Rating and excerpt
- **detailed:** Full review visible
- **verified:** Shows verification badge

**Pairs With:** product-card, testimonial, trust-badges

**Accessibility:** Stars have text equivalent
**Mobile:** Full-width cards

---

### Case Study Preview

**Description:** Summary card linking to detailed case study.

**Content Slots:**
| Slot | Required | Type | Limits | Purpose |
|------|----------|------|--------|---------|
| client_logo | No | image | - | Client's logo |
| client_name | Yes | text | 40 chars | Client/company name |
| headline | Yes | text | 80 chars | Result or achievement |
| metrics | No | array | 3 max | Key results with numbers |
| excerpt | No | text | 150 chars | Brief summary |
| cta_text | Yes | text | 20 chars | "Read more" action |

**Best For:**
- B2B marketing
- Service validation
- Portfolio display
- ROI demonstration

**Avoid When:**
- No permission from client
- Results aren't impressive
- B2C product pages

**Variants:**
- **minimal:** Logo, headline, CTA
- **detailed:** Includes metrics and excerpt
- **featured:** Larger, more prominent

**Pairs With:** logo-cloud, testimonial, card-grid

**Accessibility:** Clear link to full case study
**Mobile:** Stack elements vertically

---

### Trust Badges

**Description:** Collection of certification, security, or award badges.

**Content Slots:**
| Slot | Required | Type | Limits | Purpose |
|------|----------|------|--------|---------|
| section_heading | No | text | 40 chars | Optional heading |
| badges | Yes | array | 3-8 | Badge images |
| - image | - | image | - | Badge graphic |
| - alt | - | text | 50 chars | Badge description |
| - link | - | url | - | Verification link |

**Best For:**
- Checkout pages
- Contact forms
- Footer
- Pricing pages

**Avoid When:**
- Badges aren't recognizable
- Too many dilute impact
- Badges aren't legitimate

**Variants:**
- **inline:** Row of badges
- **grid:** Badges in grid
- **with-labels:** Text below badges

**Pairs With:** checkout-summary, footer-nav, pricing-table

**Accessibility:** Alt text explaining each badge
**Mobile:** May reduce to fewer badges

---

## Category 10: E-commerce Specific

Components specific to online shopping and transactions.

---

### Product Card

**Description:** Card displaying product with image, price, and purchase options.

**Content Slots:**
| Slot | Required | Type | Limits | Purpose |
|------|----------|------|--------|---------|
| image | Yes | image | - | Product photo |
| name | Yes | text | 60 chars | Product name |
| price | Yes | text | 15 chars | Product price |
| original_price | No | text | 15 chars | Pre-sale price |
| rating | No | number | 1-5 | Average rating |
| review_count | No | number | - | Number of reviews |
| badge | No | text | 15 chars | "Sale", "New", etc. |
| quick_add | No | boolean | - | Add to cart button |

**Best For:**
- Product listings
- Category pages
- Search results
- Related products

**Avoid When:**
- Product requires detailed explanation
- Single product focus
- Non-e-commerce context

**Variants:**
- **minimal:** Image, name, price
- **detailed:** Includes rating, reviews
- **quick-shop:** Hover reveals options
- **compare:** Checkbox for comparison

**Pairs With:** filter-controls, pagination, cart-preview

**Accessibility:** Clear product info, actionable elements labeled
**Mobile:** Grid of 2, larger tap targets

---

### Pricing Table

**Description:** Comparison of pricing tiers/plans side by side.

**Content Slots:**
| Slot | Required | Type | Limits | Purpose |
|------|----------|------|--------|---------|
| plans | Yes | array | 2-4 | Pricing tiers |
| - name | - | text | 20 chars | Plan name |
| - price | - | text | 20 chars | Price display |
| - period | - | text | 15 chars | "/month", "/year" |
| - description | - | text | 80 chars | Plan summary |
| - features | - | array | 10 max | Included features |
| - cta_text | - | text | 20 chars | Action button |
| - highlighted | - | boolean | - | Recommended plan |
| billing_toggle | No | - | - | Monthly/annual switch |

**Best For:**
- SaaS pricing
- Subscription services
- Membership tiers
- Plan comparisons

**Avoid When:**
- Single pricing option
- Complex per-unit pricing
- Highly customized pricing

**Variants:**
- **horizontal:** Plans side by side
- **vertical:** Plans stacked (mobile)
- **feature-matrix:** Full comparison table
- **slider:** Price changes with slider

**Pairs With:** comparison-table, cta-section, faq (accordion)

**Accessibility:** Clear plan differences, recommended plan labeled
**Mobile:** Stack vertically, recommended first

---

### Product Gallery

**Description:** Multi-image display for product with zoom and thumbnails.

**Content Slots:**
| Slot | Required | Type | Limits | Purpose |
|------|----------|------|--------|---------|
| images | Yes | array | 2-10 | Product photos |
| thumbnails | Yes | boolean | - | Show thumbnail nav |
| zoom | No | boolean | - | Enable zoom on hover |
| video | No | url | - | Product video |

**Best For:**
- Product detail pages
- E-commerce
- Detailed product view
- Multiple angles/options

**Avoid When:**
- Single product image suffices
- Low-quality images

**Variants:**
- **thumbnails-bottom:** Thumbnails below main
- **thumbnails-side:** Thumbnails beside main
- **full-screen:** Opens full-screen gallery
- **360-view:** Rotating product view

**Pairs With:** product-card, lightbox

**Accessibility:** Alt text for all images, keyboard navigation
**Mobile:** Swipeable, pinch-to-zoom

---

### Cart Preview

**Description:** Mini cart showing items and totals, often in dropdown or sidebar.

**Content Slots:**
| Slot | Required | Type | Limits | Purpose |
|------|----------|------|--------|---------|
| items | Yes | array | - | Cart contents |
| - image | - | image | - | Product thumbnail |
| - name | - | text | 40 chars | Product name |
| - quantity | - | number | - | Item quantity |
| - price | - | text | 15 chars | Line item price |
| subtotal | Yes | text | 20 chars | Cart subtotal |
| checkout_cta | Yes | text | 20 chars | Checkout button |
| view_cart_cta | No | text | 20 chars | View full cart |

**Best For:**
- E-commerce headers
- Quick cart access
- Purchase flow

**Avoid When:**
- Cart is complex (use full page)
- Many customization options

**Variants:**
- **dropdown:** Appears on hover/click
- **sidebar:** Slides in from edge
- **modal:** Overlay modal

**Pairs With:** navbar, product-card

**Accessibility:** Announce cart updates, keyboard accessible
**Mobile:** Often slides in from edge

---

### Checkout Summary

**Description:** Order summary panel showing items, totals, and payment due.

**Content Slots:**
| Slot | Required | Type | Limits | Purpose |
|------|----------|------|--------|---------|
| items | Yes | array | - | Order items |
| subtotal | Yes | text | 15 chars | Items total |
| shipping | Yes | text | 15 chars | Shipping cost |
| tax | No | text | 15 chars | Tax amount |
| discount | No | text | 15 chars | Applied discount |
| total | Yes | text | 15 chars | Final total |
| promo_code | No | field | - | Coupon input |
| trust_badges | No | array | - | Security badges |

**Best For:**
- Checkout pages
- Order review
- Payment confirmation

**Avoid When:**
- Cart is elsewhere on page

**Variants:**
- **sidebar:** Fixed in sidebar
- **collapsible:** Expands to show details
- **sticky:** Follows scroll

**Pairs With:** multi-step-form, trust-badges

**Accessibility:** Clear totals, editable quantities labeled
**Mobile:** Often collapsible to save space

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
