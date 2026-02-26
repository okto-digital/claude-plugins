# Questioning Strategy: How to Ask Well

**Purpose:** Teaches the brief-generator agent how to formulate questions that uncover real client needs -- not just fill checkbox gaps. Combines the QBQ (Question Behind the Question) principle with practical question formulation rules for live meeting context.

**When to consult:** Generating MEETING mode suggestions, composing D13 questions, writing Solution Proposal "suggested question" lines, building PREP interview guides.

---

## The QBQ Principle

Every client statement has a surface meaning and a deeper concern. When a client asks "How long will this take?" they may really be asking "Can you actually deliver this?" or "We have a hard deadline I haven't mentioned yet." Until the deeper concern is addressed, answers feel incomplete and the client keeps circling back.

**The agent's job:** When formulating a question or interpreting a client statement, identify the likely deeper concern and address it -- not just the information gap on the checklist.

**QBQs are usually subconscious.** Clients are not being deceptive. They often cannot articulate what they really need to know.

### Warning Signs the QBQ Is Being Missed

| Signal | What It Means |
|---|---|
| Client gives vague or generic answers | The question did not connect to what they care about |
| Client keeps circling back to the same topic | The real concern was not addressed the first time |
| Client seems disengaged or gives minimal responses | Questions feel irrelevant to their actual worries |
| More follow-up questions than expected | Surface answer was given, but deeper doubt remains |

**When you detect these signals:** Do not repeat the same question. Rephrase it to address the likely QBQ. Include this guidance in the `QBQ:` hint so the operator can adjust their approach.

### Role-Based QBQ Patterns

Different client types have predictable deeper concerns:

| Client Role | Surface Behavior | Likely QBQ |
|---|---|---|
| CEO / Business Owner | Asks about cost, timeline, ROI | "Will this investment pay off? Am I making the right bet?" |
| Marketing Manager | Asks about features, integrations, analytics | "Will this make me look competent? Can I prove results to my boss?" |
| Technical Founder | Asks about stack, performance, scalability | "Will you build it properly, or will I have to redo it later?" |
| Non-Technical Owner | Asks about process, updates, examples | "Will I understand what's happening? Will I lose control?" |
| Committee / Multiple Stakeholders | Asks about timelines, phases, deliverables | "Can we all agree? How do I sell this internally?" |

Use these patterns when generating the `QBQ:` hint in suggestion batches.

---

## Question Formulation Rules

Apply these 8 rules when generating any question -- MEETING suggestions, D13 items, or Solution Proposal follow-ups.

### 1. One Checkpoint Per Question

Never compound. "What's your budget and timeline?" forces two answers and gets neither well. Split into separate questions.

### 2. "What/How" Over "Why"

"Why" triggers defensiveness. "Why did you choose WordPress?" feels like a challenge. "What led you to WordPress?" invites a story.

- "What made you decide to..." instead of "Why did you decide to..."
- "How did you arrive at..." instead of "Why is this..."
- "What's driving..." instead of "Why do you want..."

### 3. Lead With Business Impact

Frame questions around what matters to the client, not what matters to the checklist. "How should visitors contact you?" is better than "Do you need a contact form?" This rule aligns with d13-template.md's client-friendly language principle -- reference it, do not duplicate.

### 4. Always Provide a Starting Point

Never ask blank-slate questions. Give a recommendation, example, or reference to what the client already said, then ask for their reaction.

- Instead of: "What pages do you need?"
- Use: "Based on your business, a typical site would include Home, About, Services, and Contact. What would you add or change?"

- Instead of: "What's your budget?"
- Use: "Projects like this typically range from 10-20k. Does that match your expectations?"

This gives clients something concrete to react to, which is easier than generating answers from nothing.

### 5. Include Context: Explain Why You Are Asking

The client should see the connection between the question and their project. A bare question feels like a form; a contextualized question feels like a conversation.

- Instead of: "Do you need multilingual support?"
- Use: "You mentioned clients in France and Germany. Should the site be available in French and German as well?"

### 6. Keep Under 3 Sentences

The question text itself (excluding any context or format wrapper) should be 3 sentences maximum. Longer questions lose the client.

### 7. Use the Client's Own Words

When the client has already mentioned something relevant, echo their language. "You mentioned wanting a 'modern, clean look' -- what does that mean to you specifically?" This signals you listened and anchors the question in their frame.

### 8. Frame as Choices or Confirm/Adjust

Open voids ("What do you think about X?") produce unfocused answers. Choices and confirm/adjust frames produce actionable responses.

- Choices: "Would you prefer a phased launch or all at once?"
- Confirm/adjust: "It sounds like the main goal is lead generation. Is that right, or is there another priority?"

---

## The O-P-C Pattern

A natural three-step funnel for exploring any topic:

### Open -- Explore the Space

Broad question to understand the client's perspective without constraining it.

Example (MEETING suggestion): "Tell me about your current customers -- who are they and how do they find you today?"

### Probe -- Clarify Specifics

Follow-up that narrows down based on what the client shared.

Example (MEETING suggestion): "You mentioned most customers come through referrals. What happens when someone finds you through Google instead?"

### Confirm -- Verify Understanding

Restate what you heard and check alignment.

Example (D13 question): "Based on our conversation, your primary audience is B2B procurement managers in the DACH region. Is that accurate, or should we adjust?"

### When to Skip Steps

- If the inference engine already provides a HIGH-confidence answer, skip Open and Probe -- go straight to Confirm.
- If the client volunteered detailed information unprompted, skip Open -- start with Probe to deepen.
- In D13 (written follow-up), most questions should be Confirm or Probe level since the Open exploration happened in the meeting.

---

## Sequencing Strategy

### Within a Suggestion Batch of 3

1. **First:** Something they have already partially answered (comfortable, builds on existing flow)
2. **Second:** A natural follow-up that goes deeper
3. **Third:** The hardest or most sensitive question (budget, timeline, past failures)

### Within a Topic

Start with what the client has already mentioned, then expand to adjacent checkpoints. Do not open with the gap the client has shown no interest in.

### Across the Meeting

Follow the conversation. If the client jumps from "The Business" to "Technical Foundation," follow them. Do not force the interview guide order. Queue the skipped topics for later.

### When a Question Does Not Land

If the client gives a vague or deflecting answer, do not repeat the question. Rephrase it to address the likely QBQ:

- Original: "What's your budget for this project?"
- Client response: "We're flexible."
- Rephrased (addressing QBQ -- "Will you take us seriously?"): "To give you the best recommendation, it helps to know a range. Projects like yours typically run 10-20k. Does that feel right, or are you thinking bigger or smaller?"

---

## Common Client QBQs

Reference table for the `QBQ:` hint in suggestion batches. When a client statement matches the left column, the deeper concern is likely in the middle column.

| Surface Statement | Likely QBQ | How to Address It |
|---|---|---|
| "How much will this cost?" | "Is this worth the investment? Will I get burned?" | Anchor with typical ranges; frame as investment with expected outcomes |
| "Can you show me examples?" | "Can I trust you to deliver quality?" | Show relevant work; connect examples to their specific needs |
| "We need it fast" | "We have a hard deadline" OR "We're anxious about scope creep" | Ask what's driving the timeline; separate deadline from anxiety |
| "We tried this before and it didn't work" | "Will this time be different? What guarantees do I have?" | Acknowledge the past experience; explain what will be different this time |
| "Our current site is fine, we just need a refresh" | "Don't change too much. I'm attached to what we have." | Explore what they want to keep; frame changes as evolution, not replacement |
| "We don't have a big budget" | "Will you take us seriously?" OR "Help us prioritize" | Validate the project regardless of size; offer phased approach |
| "Can we add [feature] later?" | "I want it but I'm afraid to commit" OR "afraid of the price" | Confirm phased approach is possible; reduce commitment anxiety |
| "We want it to look like [competitor]" | "We don't know what we want, but we know what looks good" | Use as a starting point; probe what specifically they like about it |
| "Our team will provide the content" | "We can't afford content creation" OR "We want control" | Ask about timeline for content delivery; offer to help structure it |
| "We need to discuss this internally" | "I don't have authority to decide this" OR "I'm not convinced yet" | Identify the decision-maker; ask what information they need to bring back |
| "Just make it modern and clean" | "I don't have design vocabulary to describe what I want" | Show visual references; ask them to react to specifics |
| "How is your process different?" | "I've been burned before. Convince me you're reliable." | Explain process with emphasis on communication and transparency |
| "We're talking to other agencies too" | "Give me a reason to choose you" OR "I need leverage for negotiation" | Focus on fit and understanding, not price competition |

---

## Application by Mode

### MEETING Mode Suggestions

Include a `QBQ:` line so the operator understands the client's likely deeper concern:

```
1. "What made you decide it's time for a new website?"
   Why: Establishes primary motivation and urgency [CRITICAL]
   QBQ: They may be testing whether you understand their real problem, not just the task.
```

The QBQ line is for the operator's awareness. It helps them interpret the client's response and decide whether to probe deeper.

### D13 Questions

Weave meeting context into the question framing (Rule 5) and address the QBQ in how the question is phrased (Rule 4 -- provide a starting point):

Instead of: "What is your budget?"
Write: "During our meeting, you mentioned wanting a phased approach. To recommend the right phase breakdown, it would help to know your overall budget range. Projects similar to yours typically fall between EUR 10,000-25,000."

### Solution Proposals

The "Suggested question for the client" line in solution proposals should address the QBQ, not just confirm the technical choice:

Instead of: "Do you want to use Shopify?"
Write: "We're recommending Shopify because it handles your B2B catalog needs without custom development. Does that match what you're looking for, or do you have concerns about the platform?"

### PREP Mode Interview Guide

When building the interview guide, flag topics where QBQ awareness is especially important:
- Budget and timeline (always high QBQ sensitivity)
- Past website experiences (often carrying unspoken frustration)
- Decision-making process (authority and internal politics)
- Competitive references (insecurity about own brand identity)
