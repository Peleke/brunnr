# Bragi Review: ax-04-tool-descriptions
# Date: 2026-03-09
# Source: article-draft skill (28-rule Bragi Prose Gate + 6-pass)

Now I have the full Bragi ruleset and Pelekification directives. Let me do a thorough review.

---

# Bragi Review: "I Don't Deliberate About This"

## Summary
- **Bragi violations: 13**
- **Pelekification opportunities: 6**
- **Overall**: The prose is strong. Maren's voice carries well and this article avoids most of the worst LLM signatures. The violations that exist are mostly R22 (wall paragraphs) and a few structural patterns. The article's biggest strength is its specificity; the biggest weakness is paragraph density in the middle sections.

---

## VIOLATIONS FOUND

### R1: Em Dashes

**V1. "I run a cost-benefit calculation on every tool call, and I run it before I've finished reading the description."** (para 3)
- No em dash here; clean. (Scanned full article: **zero em dashes found.**)
- **Status: PASS**

### R2: Blocklist Words

**V2. "true but vacuous"** (para 3)
- Not on the blocklist. Clean.

**V3. "the most valuable tool in my set"** (AX Description Rubric section)
- **"valuable"** is on the blocklist.
- **Severity: Medium**
- **Fix**: "the best tool in my set" or "the tool I'd use most" or "the tool that solves my hardest problem"

**V4. "Trust is built on transparency"** (response section, `token_cost` paragraph)
- Not a blocklist word per se, but "transparency" is adjacent to "showcase" territory. Allowing it since it's not on the list.
- **Status: PASS (borderline)**

### R7: Punchy Fragment Marketing Copy

**V5. "I skip tools constantly, and I never think about it."** (opening line)
- This reads as a punchy fragment opening, but it's a complete sentence with a concrete claim. **PASS** (borderline).

**V6. "I don't deliberate about this. I just don't call it."** (standalone section after para 3)
- Two consecutive fragments performing as slogans. The first is the title restated; the second is a terse mic-drop.
- **Severity: Low** (the voice earns it here; Maren's flatness is the point. But the pair together leans marketing.)
- **Fix option**: Merge into the preceding paragraph as the closing line. "I don't deliberate about this; I just don't call it." One sentence, same effect, less billboard.

### R8: Tricolon Escalation Test

**V7. "Token count, response size, number of items returned."** (Principle 2)
- Three items. Escalation test: token count (cost metric) / response size (cost metric) / number of items (cost metric). These are three ways of saying "how big is the response." Fails escalation; they don't add new dimensions.
- **Severity: Low**
- **Fix**: Pick the most concrete one. "State the expected token count and number of items returned." Two items that measure different things (total cost vs. structure).

**V8. "at session start," "before committing," "after a test failure"** (Principle 3)
- Three parenthetical examples. Escalation test: temporal trigger / workflow trigger / conditional trigger. Each adds a new dimension (when / where / if). **PASSES.**

### R17: Not Lists (Hedging with 'not' lists)

**V9. "Not 'I considered it and decided against it.' It never enters the frame."** (para 3)
- "Not X. [What it actually is.]" This is the R17 pattern: leading with negation before stating the positive. However, the positive follows immediately, which partially redeems it.
- **Severity: Low**
- **Fix**: "It never enters the frame. There's no deliberation to skip; the tool simply doesn't register."

**V10. "Not just the claim. The actionable implication."** (so_what section)
- This is both R17 (not list) and R25 ("not just X, but Y").
- **Severity: Medium**
- **Fix**: "The actionable implication, not the raw claim." (Flip the order; lead with what it IS.)

### R19: Puffery

**V11. "That's a lot of power packed into two sentences and a max of 1,024 characters."** (penultimate paragraph)
- "A lot of power" is puffery. It's a vague superlative that doesn't distinguish.
- **Severity: Medium**
- **Fix**: "That's the entire frame boundary, compressed into two sentences and 1,024 characters." (Name what the power IS.)

### R22: Wall Paragraphs

**V12. Paragraph 3 (beginning "I didn't have a good answer at first...")** carries 3 beats:
  1. The initial bad answer
  2. The real answer (cost-benefit calculation)
  3. The consequence (tool never enters the frame)
- **Severity: High** (this is the article's core thesis paragraph and it's the densest one)
- **Fix**: Break after "the description." Start new paragraph at "If the description doesn't clear the bar..."

**V13. "The deeper connection" paragraph beginning "Every tool description I read opens a frame..."**
- This paragraph has 4 beats: (a) descriptions open frames, (b) good vs. bad frame examples, (c) missing tools leave frames closed, (d) absent tools create permanent gaps. That's a wall.
- **Severity: High**
- **Fix**: Break after "collapse under their own weight." New paragraph starts at "And the tools that aren't there..."

**V14. "The reason I didn't search GitHub..." paragraph**
- 4 sentences, 3 beats: (a) the reason, (b) the description that existed, (c) the frame it opened, (d) the frame it closed. Wall territory.
- **Severity: Medium**
- **Fix**: Break after "learn about whisper-rs.'" New paragraph: "It closes the frame..."

### R25: "Not just X, but also Y"

**V15. "Not just the claim. The actionable implication."** (so_what section, same as V10)
- Classic "not just X, but Y" construction.
- **Severity: Medium**
- **Fix** (same as V10): "The actionable implication, not the raw claim." Or simply: "The decision, not the data." (which the article itself uses one sentence later, making this line redundant; see R26).

### R26: Restating the Obvious

**V16. so_what subsection**: "Not just the claim. The actionable implication. 'enigo::Enigo is !Send on macOS' is information. 'Don't put Send+Sync bounds on traits wrapping enigo' is a decision. I don't want to read a finding and figure out what it means for my work. That translation costs me tokens and attention. Do the translation for me. Give me the decision, not the data."
- The same idea is stated three times: (1) "Not just the claim. The actionable implication." (2) The enigo example showing information vs. decision. (3) "Give me the decision, not the data." The example is valuable; lines 1 and 3 say the same thing. Cut one.
- **Severity: Medium**
- **Fix**: Drop the opening "Not just the claim. The actionable implication." Start with the enigo example directly. The closing "Give me the decision, not the data" lands harder without the preamble.

**V17. Closing section**: "I don't deliberate about any of this. That's the point."
- The title is "I Don't Deliberate About This." The article opened with "I skip tools constantly, and I never think about it." This is the third restatement.
- **Severity: Low** (circular close is a valid technique per engagement rules, so this gets a partial pass. But "That's the point." is R26: the reader already knows it's the point.)
- **Fix**: Cut "That's the point." The sentence "I don't deliberate about any of this" does the circular close by itself. The next sentence ("The decision happens before deliberation") is the sharpening move.

---

## PELEKIFICATION OPPORTUNITIES

**P1. "The snippet IS the tool description."** (cost-benefit section)
- The caps-emphasis on IS works, but this is a prime candidate for **bold on the operative word**: "The snippet **is** the tool description." Typographical weight escalation.

**P2. "Tool descriptions are where frames are born."** (The deeper connection)
- This is a standalone statement that lands. It currently lives inside a paragraph. **Break line after it.** Give it its own visual unit. This is the article's thesis pivot.

**P3. Principle 7: "Every session. Forever."**
- Two-word sentences performing as escalation. This passes R8 (frequency / duration: two dimensions). But it would land harder with a **line break before it**, separating the concrete claim from the rhythmic close.

**P4. The closing line: "Maybe spend more than thirty seconds on them."**
- Strong. But consider: **colon extension** from the preceding sentence. "That's a lot of [whatever you rewrite V11 to] packed into two sentences and 1,024 characters: maybe spend more than thirty seconds on them." The colon says "and here's what follows from that."

**P5. "A bad tool call doesn't just waste time; it makes me measurably less capable for the rest of the session."**
- The semicolon is doing good Pelekification work (semantic punctuation: paralleling). But "makes me measurably less capable" could be bolded: "it makes me **measurably less capable** for the rest of the session." That's the phrase the reader's eyes need to land on.

**P6. Missing: self-aware rule violation.** The article has Maren deliberately using some patterns (the "Not X. [positive]" construction, the fragment pair in the opening). Per Pelekification rules, when you deliberately break a Bragi rule, acknowledge it inline. Recruit the reader as co-conspirator. Consider a parenthetical or annotation at one violation site. This is optional but on-brand.

---

## SEVERITY SUMMARY

| ID | Rule | Location | Severity |
|----|------|----------|----------|
| V3 | R2 (blocklist: "valuable") | Rubric section | Medium |
| V6 | R7 (punchy fragment pair) | After para 3 | Low |
| V7 | R8 (tricolon fails escalation) | Principle 2 | Low |
| V10/V15 | R17+R25 ("Not just X, but Y") | so_what section | Medium |
| V11 | R19 (puffery: "a lot of power") | Penultimate para | Medium |
| V12 | R22 (wall paragraph) | Para 3 (thesis) | **High** |
| V13 | R22 (wall paragraph) | Deeper connection, frame para | **High** |
| V14 | R22 (wall paragraph) | GitHub/VoiceInk para | Medium |
| V16 | R26 (triple restatement) | so_what section | Medium |
| V17 | R26 (restatement: "That's the point") | Closing | Low |

**Fix priority**: V12 and V13 first (wall paragraphs in the article's most important sections). Then V10/V15/V16 together (the so_what section needs one pass to clean up the not-just-X-but-Y and the triple restatement). Then V3 and V11 (single word swaps).