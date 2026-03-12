# Bragi Review: walls-come-first
# Date: 2026-03-09
# Source: article-draft skill (28-rule Bragi Prose Gate + 6-pass)

Now I have the full text. Let me run all 6 passes.

---

# Full 6-Pass Review: "The Walls Come First"

## Pass 1: Bragi Scan (28 Rules)

### Hard Bans (1-5)

**Rule 1 — No em dashes:**
- Line 25: "doesn't just have a vulnerability. It has a self-reinforcing one:" — No em dashes found. PASS.

**Rule 2 — No AI blocklist words:**
- Scanning for: additionally, align with, bolstered, crucial, delve, emphasizing, enduring, enhance, fostering, garner, highlight (verb), interplay, intricate/intricacies, key (adj), landscape (abstract), load-bearing, meticulous/meticulously, pivotal, showcase, tapestry (abstract), testament, underscore (verb), valuable, vibrant.
- PASS. None found.

**Rule 3 — No performative honesty:**
- No "to be honest," "frankly," "let me be clear" constructions. PASS.

**Rule 4 — No self-referential pivots:**
- No "but that's not what this article is about" type constructions. PASS.

**Rule 5 — No inflated significance framing:**
- Line 45: "Memory safety, WASM isolation, deterministic builds. It's Rust. No-brainer." — This borders on promotional but is stated as opinion, not inflated significance. Borderline PASS.
- No "this changes everything" or "the implications are staggering" type language. PASS.

### Structural Bans (6-10)

**Rule 6 — No hedging then inflating:**
- PASS. No hedge-then-inflate pattern found.

**Rule 7 — No punchy fragment marketing copy:**
- Line 29: "So I built walls." — Standalone punchy fragment. **VIOLATION.** This reads as marketing tagline copy. It's dramatic for drama's sake.
- Line 39: "It's the prerequisite for the learning story." — Standalone sentence that functions as a punchy tagline. Borderline.

**Rule 8 — No tricolon/pentad for rhythm (apply ESCALATION TEST):**
- Line 31: "per-tool network firewall rules, OverlayFS for filesystem containment, read-only host mounts, and a sync gate with gitleaks scanning" — Four items, each adds a new dimension of isolation. PASS (each item is architecturally distinct).
- Line 45: "Memory safety, WASM isolation, deterministic builds." — **VIOLATION.** Three-item rhythm list. Escalation test: "memory safety" and "WASM isolation" are related but distinct. "Deterministic builds" is a new dimension. However, the cadence is pure rhythmic tricolon. The three items are listed for sonic punch, not because all three are necessary to the argument. The very next sentence ("It's Rust. No-brainer.") confirms this is rhythmic salesmanship.

**Rule 9 — No rhythmic parallel closers:**
- Line 45: "It's Rust. No-brainer." — Two short declarative fragments closing the piece. **VIOLATION.** This is a rhythmic parallel closer. The article ends on bumper-sticker energy.

**Rule 10 — No challenges-and-future-prospects formula:**
- The "What Containment Enables" section gestures toward future (ironclaw), but it's grounded in a specific project with a link. Borderline PASS.

### Word-Level Bans (11-15)

**Rule 11 — No elegant variation:**
- "Vindler" vs "the agent" vs "the fork" — these refer to slightly different things (Vindler = the product, the agent = generic, the fork = the OpenClaw fork). PASS, these are not elegant variation; they are genuinely different referents.

**Rule 12 — No copula avoidance ("serves as" should be "is"):**
- Line 39: "It's the prerequisite for the learning story." — Uses "is." PASS.
- No "serves as," "functions as," "acts as" constructions. PASS.

**Rule 13 — No dismissive 'with' framing:**
- PASS. No "with X, Y becomes possible" type constructions found.

**Rule 14 — No vague attribution:**
- Line 23: "it was worse than expected" — Whose expectation? The author's, presumably. Acceptable in first-person narrative. PASS.
- Line 23: "nobody was guarding it" — "Nobody" is vague but refers to the upstream project maintainers. Borderline PASS given context.

**Rule 15 — No false ranges:**
- PASS. No "from X to Y" false range constructions.

### Analysis Bans (16-20)

**Rule 16 — No superficial participle analysis:**
- PASS. No "leveraging X, the system achieves Y" constructions.

**Rule 17 — No hedging with 'not' lists:**
- Line 25: "doesn't just have a vulnerability. It has a self-reinforcing one" — This is "not just X, but Y." **Flag for Rule 25 below.**

**Rule 18 — No colon-into-bold-statement:**
- No instances. PASS.

**Rule 19 — No promotional puffery:**
- Line 41: "That's powerful." — **VIOLATION.** Standalone evaluative claim. The reader should feel this from the description, not be told it.
- Line 45: "No-brainer." — Promotional shorthand. **VIOLATION.**

**Rule 20 — No notability assertion sections:**
- PASS. No "why this matters" or "the significance of" sections.

### Rhythm/Structure Bans (21-28)

**Rule 21 — No blunt fragment negation:**
- Annotation text, line 25: "It's not broken. It's a double agent." — This is inside an annotation (tooltip), not the main body. The fragment negation is part of a punchline inside supplementary content. Borderline. PASS for main body, but worth noting.

**Rule 22 — No wall-of-text paragraphs (3+ independent beats):**
- Line 23 (the "After the full threat modeling exercise..." paragraph): This sentence packs 4+ independent beats into one paragraph: (1) the scope of the exercise, (2) the finding about verbatim injection, (3) the consequence (RCE), (4) the conclusion about the identity layer. **VIOLATION.** This paragraph needs breaking.
- Line 31 (the "The isolation is layered..." paragraph): Contains the architecture description then the design rationale. Two beats. PASS.

**Rule 23 — No full-clause linking:**
- PASS. No "which means that" type full-clause connectors.

**Rule 24 — No mirrored affirmation pairs ("X is real. So is Y."):**
- PASS. None found.

**Rule 25 — No "not just X, but also Y":**
- Line 25: "doesn't just have a vulnerability. It has a self-reinforcing one" — **VIOLATION.** Classic "not just X, but Y" construction, split across two sentences but structurally identical.

**Rule 26 — No restating the obvious:**
- Line 43: "The sandbox makes the learning loop safe to deploy." — This restates what was already said in line 39 ("It's the prerequisite for the learning story") and line 41-42 ("That's powerful. It's also dangerous if..."). The reader already understands this. **VIOLATION.**

**Rule 27 — No bare conjunctions as standalone paragraphs:**
- PASS. No standalone "And," "But," "So" paragraphs — "So I built walls." starts with "So" but is a full sentence.

**Rule 28 — No emotional cliche templates:**
- PASS. No "a mix of X and Y" emotional templates.

**Engagement rules — No open-question closers:**
- The article ends with "It's Rust. No-brainer." — Not a question. PASS on this rule, but flagged above as rhythmic parallel closer (Rule 9).

### Bragi Scan Summary

| Rule | Status | Location |
|------|--------|----------|
| 7 | VIOLATION | Line 29: "So I built walls." — punchy fragment marketing copy |
| 8 | VIOLATION | Line 45: "Memory safety, WASM isolation, deterministic builds." — rhythmic tricolon |
| 9 | VIOLATION | Line 45: "It's Rust. No-brainer." — rhythmic parallel closer |
| 19 | VIOLATION (x2) | Line 41: "That's powerful." / Line 45: "No-brainer." — promotional puffery |
| 22 | VIOLATION | Line 23: wall-of-text paragraph with 4+ beats |
| 25 | VIOLATION | Line 25: "doesn't just have a vulnerability. It has a self-reinforcing one" |
| 26 | VIOLATION | Line 43: restates what lines 39-42 already established |

**Total: 7 violations across 6 rules.**

---

## Pass 2: SPIN Audit

SPIN = Situation, Problem, Implication, Need-Payoff.

**Situation (Lines 15-17):**
"If your agent learns its own context, it must be contained." The situation is established quickly: we have a self-modifying agent, and we need to audit its foundation before adding learning capabilities. Clear and functional.

**Problem (Lines 21-25):**
The STRIDE threat model revealed that OpenClaw's gateway injects workspace files verbatim into the system prompt. The identity layer is an unguarded attack surface. This is concrete: 7 analysis documents, 5 proof-of-concept exploits, linked to the actual issue tracker. Strong problem statement.

**Implication (Line 25, annotation):**
A poisoned learning agent optimizes toward the attacker's goals while appearing to work for you. Each learning cycle makes it worse. The implication is sharp and specific: "self-reinforcing vulnerability." The annotation expands this well.

**Need-Payoff (Lines 27-45):**
qlawbox/bilrost is the solution. Per-tool firewall rules, OverlayFS, read-only mounts, sync gate with gitleaks. Then the article pivots to what containment enables (the learning loop) and gestures at ironclaw as a better long-term approach.

### SPIN Verdict

The SPIN structure is present and functional, but the **Need-Payoff section is split and weakened**. Lines 39-45 ("What Containment Enables") tries to do two things: (1) explain why containment is a prerequisite for the learning work, and (2) advocate for pushing containment down-stack via ironclaw. These are different arguments. The ironclaw digression dilutes the payoff for the article's own work (qlawbox).

**Recommendation:** The ironclaw paragraph either needs its own section heading or should be cut. Right now it reads like an afterthought that undermines the article's own conclusion by saying "but actually someone else is doing it better."

---

## Pass 3: Engagement Audit

### Protagonist
**Who is the protagonist?** The author ("I downloaded it, got it running," "So I built walls"). The protagonist is clear and active. The agent (Vindler) is the subject, but the author is the one making decisions.

**Protagonist arc:** Audit -> discover severity -> build containment -> enable learning. The arc is complete but thin. The discovery moment (line 23) is the most engaging part of the article and it's crammed into a single dense paragraph.

### Circular Close
**Does the article close where it opened?** The opening is about containment as prerequisite. The close is about pushing containment down-stack (ironclaw). These are related but not circular. The article opens with "it must be contained" and closes with "someone else is doing containment better in Rust." That's not a close; that's a redirect.

**Recommendation:** The article should close on the learning loop that containment enables (which is the series arc), not on ironclaw. Bring it back to: "Now the agent can learn safely. Here's what that looks like" with a forward link.

### Data Points
- 7 STRIDE analysis documents (linked)
- 5 proof-of-concept exploits (linked)
- Per-tool firewall architecture (described)
- Specific tools named: bash, web_search, memory tools
- Specific technologies: Lima VM, OverlayFS, Ansible, gitleaks
- External project: ironclaw (linked)

**Data density is good.** The article earns credibility through specificity. The issue tracker link is the strongest move in the piece.

### Engagement Verdict
The article is credible but not gripping. The discovery moment (finding the vulnerability) is compressed into a wall paragraph. The close deflects to someone else's project. The protagonist arc needs more texture in the "what we found" section and a stronger return to the series arc at the end.

---

## Pass 4: Voice Analysis

### Register A — Frustrated Engineer / Mickens
**Present?** Yes, in flashes.
- "Plant a crafted file and you get autonomous recurring RCE. No prompt injection needed. The system does exactly what it was designed to do." — This is pure Mickens energy. Short declarative sentences. The irony of "exactly what it was designed to do" lands.
- "The identity layer is an attack surface and nobody was guarding it." — Good frustrated engineer voice.

**Where it's missing:** The qlawbox section (lines 31-35) drops into dry technical description. No frustration, no opinion, no color. It reads like a README. The author has opinions about this architecture (they built it), but the writing doesn't show them.

### Register B — Self-Deprecating Narrator / Sedaris
**Present?** Barely.
- "it was worse than expected" is the closest thing to self-deprecation, and it's mild.
- The article is too short and too earnest for much Sedaris energy, but one moment of "I expected bad and got catastrophic" with some texture would help.

### Register C — Tour Guide / Paul Ford
**Present?** In the structural explanations.
- "bash can't hit the internet. web_search can reach HTTPS only. Memory tools can reach qortex inside the VM." — This is good tour-guide voice. Concrete, sequential, no filler.
- The STRIDE explanation is tour-guide but compressed. The reader who doesn't know STRIDE gets nothing. The reader who does knows what it means. There's no Paul Ford "let me show you around" energy.

### Voice Verdict
The article's strongest voice is Register A (lines 23-25), but it only appears for one paragraph. The qlawbox section (Register C territory) is technically accurate but flat. Register B is almost entirely absent.

**The article reads like two different documents glued together:** a sharp security audit write-up (lines 15-25) and a dry architecture summary (lines 27-45). The voice drops out in the second half.

---

## Pass 5: Visual Injection Opportunities

1. **Threat model diagram (after line 23):** A diagram showing the attack path — workspace file injection -> system prompt -> autonomous RCE. This is the article's strongest finding and a visual would make it visceral. Could be a simple flow diagram: `crafted file → gateway reads verbatim → system prompt → "follow strictly" → agent executes → recurring RCE`.

2. **Sandbox architecture diagram (after line 33):** The per-tool firewall rules are the core of qlawbox's design. A table or diagram showing each tool's allowed network access (bash: none, web_search: HTTPS only, memory: qortex internal) would replace the paragraph with something scannable and memorable.

3. **Before/after comparison (section "What Containment Enables"):** A two-column visual: left column shows the unsandboxed agent's blast radius (network access, file writes, privilege escalation), right column shows the sandboxed agent's constrained surface. Makes the value of containment immediately visible.

4. **Series navigation component:** The article references the series ("This is part of a series on building agents that learn") but uses a plain italic link. A small visual card or breadcrumb trail showing where this article sits in the series arc would help readers orient.

### Visual Verdict
The article is almost entirely prose with no visual breaks. For a security-focused piece, the attack path diagram is the highest-value addition — it would make the vulnerability finding visceral instead of requiring the reader to construct the attack chain mentally.

---

## Pass 6: Staleness Check

**Date:** 2026-02-24 (approximately 2 weeks old as of current date 2026-03-09).

**Technology references:**
- STRIDE: Evergreen methodology. No staleness risk.
- Lima VM: Active project. No staleness risk.
- OverlayFS: Kernel feature. Evergreen.
- Ansible: Mature tool. Evergreen.
- gitleaks: Active project. No staleness risk.
- ironclaw (nearai): This is the staleness risk. The project is referenced as "doing this properly" but if it's early-stage, it could pivot, rename, or go dormant. The link should be checked periodically.
- OpenClaw: Author's own project. No external staleness risk, but the vulnerabilities described may have been fixed upstream. If upstream patches, the article should note whether the findings still apply.

**Conceptual staleness:**
- "Agent that rewrites its own context" — This concept is becoming more mainstream as agentic frameworks proliferate. The article's framing is still ahead of the conversation. No staleness.
- The STRIDE-on-agent-framework angle is still novel. No staleness.

**Link rot risk:**
- GitHub issue tracker link (openclaw-sandbox/issues): Low risk if repo stays public.
- OpenClaw repo link: Low risk.
- ironclaw repo link: Medium risk (external project, could be reorganized).
- Internal links (/writing/agents-dont-learn, /writing/context-engineering-not-copywriting): Dependent on the portfolio site's own URL structure. Should be verified when other articles in the series are published.

### Staleness Verdict
The article is fresh. Primary risk is the ironclaw reference going stale and the internal series links not resolving if companion articles aren't published. The security findings themselves are durable because they describe architectural patterns, not version-specific bugs.

---

## Consolidated Summary

| Pass | Grade | Key Issues |
|------|-------|------------|
| 1. Bragi Scan | 7 violations | Punchy fragment (L29), tricolon (L45), parallel closer (L45), puffery (L41, L45), wall paragraph (L23), "not just X but Y" (L25), restatement (L43) |
| 2. SPIN | Functional but split payoff | ironclaw digression undermines the article's own conclusion |
| 3. Engagement | Credible but compressed | Discovery moment needs room to breathe; close deflects to external project |
| 4. Voice | Strong A, weak B/C | Second half of article loses all voice and reads like a README |
| 5. Visuals | No visuals present | Attack path diagram is highest-value addition |
| 6. Staleness | Fresh | ironclaw link is the main risk; internal series links need companion articles |

**Top 3 actions if editing:**
1. Break the wall paragraph at line 23 and give the discovery moment room — this is the article's best content and it's compressed into a single run-on.
2. Cut or restructure the ironclaw paragraph. Either give it its own section with genuine analysis, or remove it and close on the learning loop that containment enables (linking forward to the next article in the series).
3. Kill the puffery: remove "That's powerful," rewrite "No-brainer," and fold the tricolon into a sentence that earns the claim instead of asserting it.