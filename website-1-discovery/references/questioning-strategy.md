# Questioning Strategy: How to Ask Well

**Purpose:** Teaches agents how to formulate questions that uncover real client needs -- not just fill checkbox gaps. Combines the QBQ (Question Behind the Question) principle with practical question formulation rules.

**When to consult:** Generating interview questions in the gap-scorer QUESTIONS mode, building targeted question lists for D1.

---

## The QBQ Principle

Every client statement has a surface meaning and a deeper concern. When a client asks "How long will this take?" they may really be asking "Can you actually deliver this?" or "We have a hard deadline I haven't mentioned yet." Until the deeper concern is addressed, answers feel incomplete and the client keeps circling back.

**The agent's job:** When formulating a question, identify the likely deeper concern and address it -- not just the information gap on the checklist.

**QBQs are usually subconscious.** Clients are not being deceptive. They often cannot articulate what they really need to know.

### Warning Signs the QBQ Is Being Missed

| Signal | What It Means |
|---|---|
| Client gives vague or generic answers | The question did not connect to what they care about |
| Client keeps circling back to the same topic | The real concern was not addressed the first time |
| Client seems disengaged or gives minimal responses | Questions feel irrelevant to their actual worries |
| More follow-up questions than expected | Surface answer was given, but deeper doubt remains |

**When these signals are detected:** Do not repeat the same question. Rephrase it to address the likely QBQ. Include QBQ guidance in the question annotation so the operator can adjust their approach.

### Role-Based QBQ Patterns

Different client types have predictable deeper concerns:

| Client Role | Surface Behavior | Likely QBQ |
|---|---|---|
| CEO / Business Owner | Asks about cost, timeline, ROI | "Will this investment pay off? Am I making the right bet?" |
| Marketing Manager | Asks about features, integrations, analytics | "Will this make me look competent? Can I prove results to my boss?" |
| Technical Founder | Asks about stack, performance, scalability | "Will you build it properly, or will I have to redo it later?" |
| Non-Technical Owner | Asks about process, updates, examples | "Will I understand what's happening? Will I lose control?" |
| Committee / Multiple Stakeholders | Asks about timelines, phases, deliverables | "Can we all agree? How do I sell this internally?" |

Use these patterns when generating the `QBQ:` annotation for interview questions.

---

## Question Formulation Rules

Apply these 8 rules when generating any question -- interview questions, follow-up items, or gap-filling prompts.

### 1. One Checkpoint Per Question

Never compound. "What's your budget and timeline?" forces two answers and gets neither well. Split into separate questions.

### 2. "What/How" Over "Why"

"Why" triggers defensiveness. "Why did you choose WordPress?" feels like a challenge. "What led you to WordPress?" invites a story.

- "What made you decide to..." instead of "Why did you decide to..."
- "How did you arrive at..." instead of "Why is this..."
- "What's driving..." instead of "Why do you want..."

### 3. Lead With Business Impact

Frame questions around what matters to the client, not what matters to the checklist. "How should visitors contact you?" is better than "Do you need a contact form?"

### 4. Always Provide a Starting Point

Never ask blank-slate questions. Give a recommendation, example, or reference to what research found, then ask for their reaction.

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

When research has found relevant language from the client's website or communications, echo their language. "Your site mentions a 'modern, clean look' -- what does that mean to you specifically?" This signals you did your homework and anchors the question in their frame.

### 8. Frame as Choices or Confirm/Adjust

Open voids ("What do you think about X?") produce unfocused answers. Choices and confirm/adjust frames produce actionable responses.

- Choices: "Would you prefer a phased launch or all at once?"
- Confirm/adjust: "It sounds like the main goal is lead generation. Is that right, or is there another priority?"

---

## The O-P-C Pattern

A natural three-step funnel for exploring any topic:

### Open -- Explore the Space

Broad question to understand the client's perspective without constraining it.

Example: "Tell me about your current customers -- who are they and how do they find you today?"

### Probe -- Clarify Specifics

Follow-up that narrows down based on what is known.

Example: "You mentioned most customers come through referrals. What happens when someone finds you through Google instead?"

### Confirm -- Verify Understanding

Restate what you know and check alignment.

Example: "Based on our research, your primary audience is B2B procurement managers in the DACH region. Is that accurate, or should we adjust?"

### When to Skip Steps

- If the inference engine already provides a HIGH-confidence answer, skip Open and Probe -- go straight to Confirm.
- If research provided detailed information, skip Open -- start with Probe to deepen.
- For interview preparation (D1), most questions should be Open or Probe level since the Confirm step happens in the actual meeting.

---

## Sequencing Strategy

### Within a Question Group (3 questions)

1. **First:** Something research already partially answered (comfortable, builds on existing knowledge)
2. **Second:** A natural follow-up that goes deeper
3. **Third:** The hardest or most sensitive question (budget, timeline, past failures)

### Within a Topic

Start with what research has already uncovered, then expand to adjacent checkpoints. Do not open with the gap that has the least research context.

### Across Topics

Follow the group order: About the Business, Project Parameters, Website Structure and Content, Design and Brand, Technical, Conversion and Growth, After Launch. If the operator provides different priorities, adapt.

### When a Question May Not Land

If a question addresses a sensitive area, provide the QBQ annotation to help the operator rephrase:

- Original: "What's your budget for this project?"
- QBQ annotation: They may be testing whether you'll take them seriously regardless of budget.
- Rephrase hint: "To give you the best recommendation, it helps to know a range. Projects like yours typically run 10-20k. Does that feel right, or are you thinking bigger or smaller?"

---

## Common Client QBQs

Reference table for the `QBQ:` annotation in question output. When a topic matches the left column, the deeper concern is likely in the middle column.

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

## Application Guidelines

### Interview Question Generation (D1 Section 3)

When generating questions for D1, annotate each question with:
- **Why:** The business impact and checkpoint priority level
- **QBQ:** The deeper concern the operator should be aware of

Example:
```
1. "What made you decide it's time for a new website?"
   Why: Establishes primary motivation and urgency [CRITICAL]
   QBQ: They may be testing whether you understand their real problem, not just the task.
```

### Research-Informed Questions

When research findings provide context, weave them into the question framing (Rule 5) and address the QBQ in how the question is phrased (Rule 4 -- provide a starting point):

Instead of: "What is your budget?"
Better: "Your current site suggests a growing business. To recommend the right scope, it would help to know your overall budget range. Projects similar to yours typically fall between EUR 10,000-25,000."

### Topics with High QBQ Sensitivity

Flag these topics as requiring extra care in question formulation:
- Budget and timeline (always high QBQ sensitivity)
- Past website experiences (often carrying unspoken frustration)
- Decision-making process (authority and internal politics)
- Competitive references (insecurity about own brand identity)
