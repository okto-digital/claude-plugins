# Domain: Booking and Scheduling

**Purpose:** Validate that the brief addresses appointment booking, reservation, or scheduling requirements -- booking flow, availability management, confirmation process, and calendar integration. Booking systems need careful planning because they directly affect operations and customer experience.

**Applicability:** Skip this entire domain if the website has no appointment, reservation, or scheduling functionality. A simple "call to book" approach does not qualify -- this domain is for automated online booking.

---

## Priority Definitions

- **CRITICAL:** Brief cannot be accurate without this. Must resolve before drafting.
- **IMPORTANT:** Brief will be thinner without this. Resolve in second pass if time allows.
- **NICE-TO-HAVE:** Useful depth. Surface once, accept skip.

---

## 1. Booking Types and Services

| Checkpoint | Priority |
|---|---|
| What can be booked? (Appointments, consultations, classes, rooms, services, events) | CRITICAL |
| How many bookable services or categories? | IMPORTANT |
| Duration of bookings (fixed, variable, multi-day) | IMPORTANT |
| Booking requires selecting a specific person/provider? (e.g., specific hairdresser, consultant) | IMPORTANT |
| Group bookings or events with capacity limits? | NICE-TO-HAVE |

## 2. Availability and Scheduling

| Checkpoint | Priority |
|---|---|
| Business hours and availability rules defined | CRITICAL |
| Multiple providers/resources with separate schedules? | IMPORTANT |
| Buffer time between bookings needed? | IMPORTANT |
| Blackout dates, holidays, vacation handling | IMPORTANT |
| Real-time availability display or next-available-slot approach | IMPORTANT |
| Timezone handling for remote/virtual services | NICE-TO-HAVE |

## 3. Booking Flow and UX

| Checkpoint | Priority |
|---|---|
| Booking flow steps defined (select service, choose time, enter details, confirm) | CRITICAL |
| Account required to book, or guest booking allowed? | IMPORTANT |
| Information collected during booking (name, email, phone, notes, custom fields) | IMPORTANT |
| Booking widget placement (dedicated page, sidebar, popup, embedded) | IMPORTANT |
| Mobile booking experience optimized | IMPORTANT |

## 4. Confirmation and Communication

| Checkpoint | Priority |
|---|---|
| Booking confirmation email sent automatically | CRITICAL |
| Reminder emails/SMS before appointment | IMPORTANT |
| Calendar invitation attached (.ics file or Google Calendar integration) | IMPORTANT |
| Cancellation/rescheduling policy defined | CRITICAL |
| Self-service cancellation and rescheduling allowed? | IMPORTANT |
| No-show policy and handling | NICE-TO-HAVE |

## 5. Payment and Deposits

| Checkpoint | Priority |
|---|---|
| Payment required at booking? (Full payment, deposit, or free) | CRITICAL |
| Refund policy for cancellations | IMPORTANT |
| Different pricing for different services/time slots | IMPORTANT |
| Package or bundle pricing (e.g., 10-session pack) | NICE-TO-HAVE |
| Discount codes applicable to bookings | NICE-TO-HAVE |

## 6. Integration and Operations

| Checkpoint | Priority |
|---|---|
| Calendar sync needed? (Google Calendar, Outlook, Apple Calendar) | IMPORTANT |
| Existing booking tool in use? (Calendly, Acuity, SimplyBook, etc.) | IMPORTANT |
| Build custom vs. embed third-party booking widget | CRITICAL |
| Staff notification of new bookings | IMPORTANT |
| Reporting on bookings (volume, no-shows, revenue) | NICE-TO-HAVE |
| Waitlist functionality for fully booked slots | NICE-TO-HAVE |

---

## Question Templates

**What kind of booking does your business need?**
- Option A: Simple appointment booking -- clients select a service, pick a date/time, and submit their details
- Option B: Complex scheduling -- multiple providers, service types, locations, or resources that need to be managed together

**Do you already use a booking tool (like Calendly, Acuity, or SimplyBook)?**
- Option A: Yes -- we want to embed or integrate our existing booking tool into the website
- Option B: No -- we need a booking solution set up as part of this project

**Should customers pay when they book, or pay later?**
- Option A: Pay at booking -- collect full payment or a deposit to reduce no-shows and secure the appointment
- Option B: Pay later -- booking is free, payment happens at the appointment or is invoiced afterward

**Can customers cancel or reschedule their own bookings online?**
- Option A: Yes -- self-service rescheduling and cancellation (with a cutoff window, e.g., 24 hours before)
- Option B: No -- cancellations and changes must go through your team directly

**How should booking confirmations and reminders work?**
- Option A: Automated email confirmation at booking plus a reminder email 24 hours before the appointment
- Option B: Email confirmation plus SMS reminder -- since our clients respond better to text messages
