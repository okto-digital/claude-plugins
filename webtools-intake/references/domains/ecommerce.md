# Domain: E-commerce

**Purpose:** Validate that the brief addresses online selling requirements -- product catalog, checkout flow, payment processing, shipping, and inventory management. E-commerce adds significant complexity to a website project; missing requirements surface late and are expensive to fix.

**Applicability:** Skip this entire domain if no products or services are sold directly online. Service quotes and lead generation do not qualify as e-commerce.

---

## Priority Definitions

- **CRITICAL:** Brief cannot be accurate without this. Must resolve before drafting.
- **IMPORTANT:** Brief will be thinner without this. Resolve in second pass if time allows.
- **NICE-TO-HAVE:** Useful depth. Surface once, accept skip.

---

## 1. Product Catalog

| Checkpoint | Priority |
|---|---|
| Number of products/SKUs (ballpark: under 50, 50-500, 500+) | CRITICAL |
| Product types: physical, digital, services, subscriptions, or mix | CRITICAL |
| Product variations (size, color, options) and how they are managed | IMPORTANT |
| Product categories and filtering/sorting needs | IMPORTANT |
| Product data source (manual entry, CSV import, API sync from ERP/POS) | IMPORTANT |
| Product imagery requirements (number of images per product, zoom, 360-view) | IMPORTANT |

## 2. Shopping and Checkout

| Checkpoint | Priority |
|---|---|
| Guest checkout allowed or account required? | CRITICAL |
| Checkout flow: single page or multi-step? | IMPORTANT |
| Cart behavior: persistent cart, abandoned cart recovery? | IMPORTANT |
| Discount codes, coupons, or promotional pricing | IMPORTANT |
| Gift cards or store credit | NICE-TO-HAVE |
| Cross-sell / upsell at checkout | NICE-TO-HAVE |

## 3. Payment Processing

| Checkpoint | Priority |
|---|---|
| Payment methods accepted (credit card, PayPal, iDEAL, Bancontact, SEPA, etc.) | CRITICAL |
| Payment processor chosen? (Stripe, Mollie, PayPal, Adyen, etc.) | CRITICAL |
| Recurring payments or subscriptions needed? | IMPORTANT |
| Invoice/billing for B2B customers | NICE-TO-HAVE |
| Multi-currency support needed? | IMPORTANT |
| PCI-DSS compliance approach (hosted payment fields, redirect, etc.) | IMPORTANT |

## 4. Shipping and Fulfillment

| Checkpoint | Priority |
|---|---|
| Shipping zones defined (domestic, EU, international) | CRITICAL |
| Shipping cost calculation (flat rate, weight-based, carrier-calculated, free) | IMPORTANT |
| Shipping carrier integrations (PostNL, DHL, UPS, etc.) | IMPORTANT |
| Order tracking provided to customers? | IMPORTANT |
| Fulfillment process: self-fulfilled, dropship, or third-party logistics | NICE-TO-HAVE |
| Pickup in store or local delivery option? | NICE-TO-HAVE |

## 5. Tax and Legal

| Checkpoint | Priority |
|---|---|
| Tax calculation approach (automatic by region, fixed rate, tax-inclusive pricing) | CRITICAL |
| VAT handling for EU cross-border sales (OSS scheme) | IMPORTANT |
| Returns and refund policy defined | IMPORTANT |
| Terms and conditions for online sales | IMPORTANT |
| Age-restricted products requiring verification? | NICE-TO-HAVE |

## 6. Inventory and Operations

| Checkpoint | Priority |
|---|---|
| Inventory tracking needed? (Real-time stock levels) | IMPORTANT |
| Low stock alerts and out-of-stock behavior | IMPORTANT |
| Integration with POS or warehouse management system | NICE-TO-HAVE |
| Order notification workflow (email to fulfillment team, customer confirmation) | IMPORTANT |
| Export capabilities (orders, customers, reports) | NICE-TO-HAVE |

---

## Question Templates

**How many products will you sell online?**
- Option A: A small catalog (under 50 products) -- manageable with manual entry and simple category structure
- Option B: A larger catalog (50+ products) -- requiring bulk import, advanced filtering, and possibly inventory sync with a backend system

**What payment methods do your customers expect?**
- Option A: Card payments (Visa/Mastercard) plus one local method (e.g., iDEAL, Bancontact) -- covering the most common payment preferences
- Option B: A full range including cards, PayPal, buy-now-pay-later options, and possibly invoicing for B2B -- maximizing conversion by removing payment barriers

**How will shipping work?**
- Option A: Simple flat-rate or free shipping -- keeping it straightforward for both you and the customer
- Option B: Calculated shipping based on weight, destination, and carrier rates -- more accurate but requires integration with carrier APIs

**Do you need real-time inventory tracking on the website?**
- Option A: Yes -- stock levels must be accurate to prevent overselling, especially if you also sell through physical stores or other channels
- Option B: No -- you manage stock manually and can handle the occasional out-of-stock situation after the fact

**Will you sell to customers outside your home country?**
- Option A: Yes -- we need multi-currency support, international shipping options, and cross-border tax handling
- Option B: No -- domestic sales only, keeping tax, shipping, and currency simple
