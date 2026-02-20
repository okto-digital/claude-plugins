# Domain: User Accounts

**Purpose:** Validate that the brief addresses login, membership, or gated content requirements -- registration flow, authentication, user roles, and account management. User accounts add significant technical complexity and security responsibility; they must be explicitly scoped.

**Applicability:** Skip this entire domain if the website has no login functionality, membership areas, or gated content. Admin-only CMS access does not count.

---

## Priority Definitions

- **CRITICAL:** Brief cannot be accurate without this. Must resolve before drafting.
- **IMPORTANT:** Brief will be thinner without this. Resolve in second pass if time allows.
- **NICE-TO-HAVE:** Useful depth. Surface once, accept skip.

---

## 1. Account Types and Access

| Checkpoint | Priority |
|---|---|
| What types of user accounts are needed? (Customer, member, partner, admin) | CRITICAL |
| What content or features are gated behind login? | CRITICAL |
| Free vs. paid accounts (or both) | CRITICAL |
| Different access levels or tiers? | IMPORTANT |
| Guest access: what can non-logged-in users see and do? | IMPORTANT |

## 2. Registration and Authentication

| Checkpoint | Priority |
|---|---|
| Registration flow: self-service, invitation-only, or admin-created? | CRITICAL |
| Registration fields required (name, email, company, etc.) | IMPORTANT |
| Social login options (Google, Apple, LinkedIn, etc.) | NICE-TO-HAVE |
| Two-factor authentication (2FA) needed? | IMPORTANT |
| Single sign-on (SSO) with existing systems? | NICE-TO-HAVE |
| Email verification required? | IMPORTANT |

## 3. Account Management

| Checkpoint | Priority |
|---|---|
| Profile editing (what can users update?) | IMPORTANT |
| Password reset flow | CRITICAL |
| Account deletion / data export (GDPR right to erasure) | IMPORTANT |
| Communication preferences (email opt-in/opt-out) | IMPORTANT |
| Account suspension or deactivation by admin | NICE-TO-HAVE |

## 4. Member-Exclusive Content

| Checkpoint | Priority |
|---|---|
| Types of gated content (resources, courses, tools, community, pricing) | IMPORTANT |
| Content drip or progressive access (time-based, action-based) | NICE-TO-HAVE |
| Download tracking or access logging | NICE-TO-HAVE |
| Content preview for non-members (teaser to encourage signup) | NICE-TO-HAVE |

## 5. Subscription and Billing (if paid)

| Checkpoint | Priority |
|---|---|
| Subscription model (monthly, annual, one-time, tiered) | CRITICAL |
| Payment integration for subscriptions (Stripe, PayPal, etc.) | CRITICAL |
| Free trial or freemium tier? | IMPORTANT |
| Upgrade/downgrade flow between tiers | IMPORTANT |
| Cancellation and refund process | IMPORTANT |
| Invoice and billing history access | NICE-TO-HAVE |

## 6. Security and Privacy

| Checkpoint | Priority |
|---|---|
| Password policy (minimum strength, rotation) | IMPORTANT |
| Session management (timeout, concurrent sessions) | NICE-TO-HAVE |
| Data encryption for stored personal information | IMPORTANT |
| Audit trail for sensitive actions | NICE-TO-HAVE |
| Privacy implications of user accounts addressed (consent, data handling) | IMPORTANT |

---

## Question Templates

**What will users be able to do when they log in?**
- Option A: Access exclusive content -- resources, guides, tools, or member-only pages that are hidden from public visitors
- Option B: Manage their account and transactions -- view order history, update details, manage subscriptions, or track progress

**How should users register for an account?**
- Option A: Self-service -- anyone can sign up using an email and password (or social login), with optional email verification
- Option B: Invitation or approval -- accounts are created by admin or require approval after signup, suitable for exclusive communities or B2B portals

**Are there different access levels or membership tiers?**
- Option A: Single tier -- all logged-in users see the same content and have the same capabilities
- Option B: Multiple tiers -- free and premium, or different roles (basic member, VIP, partner) with different access levels

**Is this a paid membership with subscriptions?**
- Option A: Yes -- users pay for access (monthly/annual), requiring payment processing, billing management, and cancellation flows
- Option B: No -- accounts are free, used for gating content or personalizing the experience without payment

**How important is security for the user account system?**
- Option A: Standard security -- email/password login, HTTPS, password reset, basic best practices
- Option B: Enhanced security -- two-factor authentication, SSO integration, strict session management, suitable for handling sensitive data
