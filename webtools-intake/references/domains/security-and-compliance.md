# Domain: Security and Compliance

**Purpose:** Validate that the brief addresses website security requirements and regulatory compliance -- SSL, data protection (GDPR/CCPA), cookie consent, and industry-specific regulations. Security failures erode trust and create legal liability; compliance gaps can result in fines.

---

## Priority Definitions

- **CRITICAL:** Brief cannot be accurate without this. Must resolve before drafting.
- **IMPORTANT:** Brief will be thinner without this. Resolve in second pass if time allows.
- **NICE-TO-HAVE:** Useful depth. Surface once, accept skip.

---

## 1. Core Security

| Checkpoint | Priority |
|---|---|
| SSL/TLS certificate planned (HTTPS on all pages) | CRITICAL |
| Security headers configured (CSP, HSTS, X-Frame-Options, etc.) | NICE-TO-HAVE |
| Regular software updates and patching plan | IMPORTANT |
| Backup strategy (frequency, retention, recovery testing) | IMPORTANT |
| DDoS protection or WAF (Web Application Firewall) needed? | NICE-TO-HAVE |

## 2. Data Protection

| Checkpoint | Priority |
|---|---|
| GDPR compliance required? (EU visitors or EU-based business) | CRITICAL |
| CCPA/CPRA compliance required? (California visitors) | IMPORTANT |
| Other regional data protection laws applicable? | NICE-TO-HAVE |
| Privacy policy exists or needs to be created | CRITICAL |
| Data Processing Agreement (DPA) needed with hosting/service providers | NICE-TO-HAVE |
| Personal data collected identified (forms, accounts, cookies, analytics) | IMPORTANT |

## 3. Cookie Consent

| Checkpoint | Priority |
|---|---|
| Cookie consent mechanism planned | CRITICAL |
| Cookie categories defined (necessary, analytics, marketing, preferences) | IMPORTANT |
| Consent management platform selected (Cookiebot, CookieYes, etc.) | IMPORTANT |
| Cookie policy/page planned | IMPORTANT |
| Consent records stored for compliance evidence | NICE-TO-HAVE |

## 4. Industry-Specific Compliance

| Checkpoint | Priority |
|---|---|
| Healthcare: HIPAA considerations for patient data | IMPORTANT |
| Finance: PCI-DSS for payment card handling | IMPORTANT |
| Education: FERPA for student information | NICE-TO-HAVE |
| Legal: client confidentiality and privilege considerations | NICE-TO-HAVE |
| Government: specific procurement or accessibility mandates | NICE-TO-HAVE |

## 5. User Data and Forms

| Checkpoint | Priority |
|---|---|
| Form data transmission encrypted (HTTPS + server-side encryption) | IMPORTANT |
| Form data storage: where and for how long? | IMPORTANT |
| Data minimization: only collecting what is needed | NICE-TO-HAVE |
| User data deletion/export capability (right to erasure, data portability) | NICE-TO-HAVE |
| Spam protection (reCAPTCHA, honeypot) without accessibility impact | IMPORTANT |

## 6. Legal Pages

| Checkpoint | Priority |
|---|---|
| Privacy Policy page | CRITICAL |
| Terms of Service / Terms and Conditions | IMPORTANT |
| Cookie Policy page | IMPORTANT |
| Impressum / Legal Notice (required in Germany, Austria, Switzerland) | IMPORTANT |
| Disclaimer or liability limitation pages | NICE-TO-HAVE |
| Refund / returns policy (for e-commerce) | NICE-TO-HAVE |

---

## Question Templates

**Does your business need to comply with GDPR (EU data protection) or similar regulations?**
- Option A: Yes -- we are based in the EU or serve EU customers, so GDPR compliance is mandatory
- Option B: Not sure -- we need to evaluate whether our visitor base and data handling trigger any data protection obligations

**Do you have an existing privacy policy, or does one need to be created?**
- Option A: We have one, but it may need updating for the new website's data collection practices
- Option B: We do not have one -- it needs to be created as part of this project (possibly with legal review)

**What personal data will the website collect?**
- Option A: Minimal -- just contact form submissions (name, email, message) and analytics cookies
- Option B: More extensive -- account registrations, payment information, file uploads, or health/financial data that requires extra protection

**Do you need a cookie consent banner?**
- Option A: Yes -- we use analytics, marketing pixels, or other non-essential cookies that require user consent
- Option B: We want to minimize cookies and use privacy-friendly analytics (like Plausible or Matomo) to reduce consent requirements

**Are there industry-specific compliance requirements we should be aware of?**
- Option A: Yes -- our industry has specific regulations (healthcare/HIPAA, finance/PCI-DSS, etc.) that affect how the website handles data
- Option B: No specific industry regulations -- standard web security and data protection best practices apply
