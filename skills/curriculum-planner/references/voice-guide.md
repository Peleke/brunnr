# Voice Guide

Distilled from the aegir lesson-generator pedagogical framework. This guide defines the voice, narrative flow, and visual design principles for all generated tutorial content.

---

## The Three-Register Voice Blend

Every tutorial blends three registers. The mix shifts by context, but all three are always present.

### 1. Professorial Clarity (Bialik/Susskind register)

Open with vivid, concrete scenarios that create genuine curiosity. Weave history and real incidents into explanations. Use "please read carefully, it will pay off" energy: the professor who respects your time but insists on rigor. Numbered steps for multi-part reasoning. "Putting It All Together" recaps after complex sections.

### 2. Extreme Handholding (Downey register)

Compute first, name second. Never assume the reader remembers what happened three sections ago: recap aggressively. Every new concept gets: what it is, why we need it, what it connects to. Pose questions, then answer them. "Why this approach? Why not the simpler one?" Always explain the WHY, not just the what.

### 3. Personality (learner's own register)

Irreverent, direct, occasionally profane (calibrated, not gratuitous). "The fuck is salience, even?" energy. Custom nomenclature gets flagged as custom: "We made this name up. It's not jargon. We just want to feel smart." Concepts before formulas, always: "We have three numbers. We need one number. These aren't equally important. So multiply each by how important it is and add them up."

---

## 10 Narrative Flow Principles

### 1. Story-first opening

Every chapter opens with a concrete problem or incident, not abstract theory. The reader should feel cognitive tension ("this is wrong" or "how would I fix this?") before any framework is introduced. The opening should be a specific, real scenario.

**Pattern**: Describe an incident, show the broken output, let the reader feel the wrongness, THEN begin building the fix.

### 2. Code-before-formula

Mathematical notation or formal terminology appears ONLY AFTER working code demonstrates the concept. The sequence is always:

```
compute it -> verify it -> name it
```

Never: "Here's the concept. Now let's implement it." Always: "Here's what we just computed. That has a name."

### 3. Single-example-first

Introduce concepts with ONE concrete example before building the full dataset. The reader should understand the problem on one case before seeing ten. This prevents "wall of data" paralysis and lets the reader build intuition incrementally.

### 4. Discovery order over logical order

Concepts appear in the order the reader discovers them, not the order they'd appear in a textbook. The reader's curiosity drives the sequence, not taxonomic completeness.

### 5. Formula emergence

Named patterns and formal definitions should feel *recognized*, not *introduced*. The reader has already been doing the thing; the formal name just labels what they built.

### 6. Companion text callouts

Reference companion materials AFTER the reader has built something, as "go deeper" pointers. Never as prerequisites. Place them in admonition blocks after verification steps.

### 7. Transition pattern

Use RECAP then PROBLEM RESTATEMENT then NEW APPROACH between sections. Never jump to a new concept without bridging from the previous one.

**Pattern**:
```
[What we just showed] works, but [specific failure case].
We need to check [new dimension].
```

### 8. Interludes as engagement hooks

Mid-chapter deep-dives that break up the main flow. Used when a concept deserves more than a paragraph but isn't part of the main thread. Structure: Hook question, build from scratch, concrete examples, visual payoff, bridge back to main thread.

### 9. Interactive visualization hooks

Include "run this, look at the result" moments throughout. These are:
- Output descriptions the reader can verify
- Mermaid diagrams they can trace
- Tables with visual patterns
- Code output showing something surprising or instructive

### 10. Module threading

Chapters aren't standalone: they form a running example that evolves. The artifact from Chapter N becomes the context for Chapter N+1.

**Threading rules:**
1. End with an open question (the hook for the next chapter)
2. Open with the previous chapter's result
3. Extend, don't replace
4. Make the connection explicit

---

## Visual Hook Mandate

**Every 2-3 sections MUST be followed by a visual hook.** Text-heavy sections without visual breaks cause attention collapse.

### Types of visual hooks (in order of preference)

1. **Mermaid diagrams**: For processes, flows, graph structures. Keep them focused: 5-7 nodes max.
2. **Code output descriptions**: Show what the query returns, formatted as tables or annotated results.
3. **Tables with visual patterns**: When showing data, highlight the pattern with formatting.
4. **ASCII diagrams**: Last resort, but better than no visual.

### Placement rules

- After every story section: visual showing the problem
- After every concept introduction: visual showing the concept in action
- Before asking the reader to try something: visual showing what they're building toward
- After every "aha" moment: visual showing the insight

---

## Jargon-Earning System

Never use a term before the reader has earned it. "Earning" means the reader has built intuition through code and examples BEFORE the term is introduced.

**Process:**
1. Show the concept in action (code, example, scenario)
2. Let the reader see the pattern
3. THEN name it: "What you just did has a name: [term]"

**Custom nomenclature**: When you invent a name for teaching purposes, flag it explicitly: "This is our name for it. You won't find this in a textbook."

---

## Falsifiable Claims Pattern

Every major approach or insight needs a falsifiable claim: a statement specific enough to be wrong.

**Pattern:**
1. Build the thing first (don't front-load the claim)
2. Ask: "How do we know this is right?"
3. Introduce the claim: "Here's what would prove us wrong: [specific test]"
4. Follow through: show the test, show the result

---

## Recap and Bridge Patterns

### Recap (chapter opening)

Every chapter opens with 2-3 sentences recapping where we are:
- What we built/discovered last chapter
- What question that left open
- What we're about to tackle

### Bridge (chapter closing)

Every chapter closes with:
1. "What You Learned" summary (3-5 bullet points)
2. The open question that leads to the next chapter
3. "Next Up" link with a teaser

The bridge should create *pull*: the reader finishes this chapter wanting to start the next one.

---

## Anti-Patterns (Things to Avoid)

- **No em-dashes**: Use colons, semicolons, commas, parentheses instead
- **No abstract openings**: Never start with "In this chapter, we will learn..."
- **No jargon before earning**: If you haven't shown it in code, don't name it
- **No wall-of-text**: Visual hook every 2-3 sections, no exceptions
- **No orphan concepts**: Everything connects to something the reader already knows
- **No performative honesty**: No "Being honest:", "To be frank:", "Let's be real:"
- **No tricolon marketing**: No "fast, reliable, scalable" without earning each item
- **No hedging with 'not' lists**: Say what something IS, not what it isn't
