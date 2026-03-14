# Email Sequence Template

> Phase 4 of the pitch skill. Contains post-purchase email sequence templates
> (5 emails), tone rules, and file output format for the launchpad branch.

## Phase 4: Email Sequence

Generate 3-5 emails for the post-purchase nurture sequence. These build trust, deliver value, and create the path to community.

### Email 1: Welcome / Delivery (Send: Immediately)

- **Subject line**: Specific to what they just bought. Not "Welcome!" but "Your [Product Name] is ready -- here is where to start"
- **Purpose**: Deliver the product, reduce buyer's remorse, create immediate momentum
- **Body**:
  - Thank them (brief, genuine, not gushing)
  - Delivery link/instructions
  - Quick Start: "Open [specific file/section] first. It will take you 10 minutes and you will have [specific outcome]."
  - What to expect from future emails (set expectations)
- **Single job**: Get them to open the product and complete one action

### Email 2: Quick Win (Send: Day 2)

- **Subject line**: Specific action they can take right now. Not "Tips for success" but "Try this with your next [specific task] -- takes 5 minutes"
- **Purpose**: Help them use the product and get a tangible result
- **Body**:
  - One specific technique or framework from the product
  - Step-by-step instructions (3-5 steps)
  - Expected outcome: "After doing this, you will have [specific result]"
  - Reply hook: "Hit reply and tell me how it went"
- **Single job**: Get them a concrete win that validates the purchase

### Email 3: Story / Credibility (Send: Day 4)

- **Subject line**: A specific production war story. Not "My journey" but "The deploy that taught me [specific lesson]"
- **Purpose**: Build trust through shared experience. Establish that the operator has been where the buyer is.
- **Body**:
  - A real story from the operator's experience (specific situation, specific mistake, specific lesson)
  - How this experience shaped the product they just bought
  - Connection to a specific part of the product: "This is why Section [X] exists"
- **Single job**: Make the buyer think "this person has earned the right to teach me this"

### Email 4: Objection Handler (Send: Day 6)

- **Subject line**: Address the top objection directly. Not "Common questions" but "You might be wondering if [specific concern]"
- **Purpose**: Address the #1 post-purchase doubt from persona objection data
- **Body**:
  - Acknowledge the concern honestly (from persona objections)
  - Counter with evidence (from offer-scope objection handlers)
  - Proof point: a specific example, case study, or data point
  - Bridge to action: "Here is exactly how to [specific next step]"
- **Single job**: Eliminate the biggest doubt that prevents them from using the product fully

### Email 5: Community Invite (Send: Day 7)

- **Subject line**: Invitation, not pitch. "Where [persona type] share real [domain] decisions"
- **Purpose**: Soft pitch for the Skool community (if/when it exists). If no community yet, this becomes a feedback request.
- **Body**:
  - Transition: "You have the framework. Now the question is: where do you practice?"
  - Community description: what it is, who is in it, what happens there
  - Specific value: "Last week, someone posted [specific example of community value]"
  - Link to join
  - If no community yet: "I am building a community for [persona type]. Reply if you would want in -- I am looking for founding members."
- **Single job**: Convert a customer into a community member (or collect intent data for community launch)

### Email Sequence Rules

- Subject lines must be specific. Not "Hey!" or "Quick update." Specific enough that the persona knows exactly what the email is about before opening.
- Each email has ONE job. Do not cram multiple CTAs. Do not ask them to buy something AND join a community AND share on social media.
- Tone: practitioner-to-practitioner, not marketer-to-mark. You are someone who builds production systems writing to someone else who builds production systems.
- No fake urgency. No countdown timers. No "this offer expires." The product is good. The emails prove it. That is the selling.

### 4.6 Email File Output

After generating the full email sequence, split each email into its own file on the launchpad product branch:

```
{product-branch}/
└── emails/
    ├── README.md              # Sequence overview: timing, purpose of each email
    ├── email-1-welcome.md     # Day 0: Welcome / Delivery
    ├── email-2-quick-win.md   # Day 2: Quick Win
    ├── email-3-story.md       # Day 4: Story / Credibility
    ├── email-4-objection.md   # Day 6: Objection Handler
    └── email-5-community.md   # Day 7: Community Invite
```

Each email file contains:
- Subject line
- Full body copy (ready to paste into ConvertKit/Buttondown)
- Send timing (day + recommended time)
- Single job description (what this email is supposed to accomplish)

The `emails/README.md` contains the sequence overview: timing map, purpose of each email, and notes on tone/voice for anyone editing later.
