# Socratic Follow-Up Sequences

When a learner answers wrong, walk them back through lower tiers for the same concept. This is how assessments become learning tools, not just measurement tools.

---

## The Walkback Pattern

```
Wrong at Tier N
    ↓
Follow-up at Tier N-1 (same concept, different phrasing)
    ↓
If wrong → Follow-up at Tier N-2
    ↓
If wrong at Tier 1 → Log misconception. Stop. Reader needs source content.
    ↓
If right → Step back up to Tier N-1, then re-attempt Tier N.
```

### Rules

1. **One tier down per step.** Don't skip from Tier 4 to Tier 1. Walk down.
2. **Same concept, different phrasing.** The follow-up isn't "try again." It's a different question about the same idea.
3. **Max 3 steps.** If you're at Tier 4 and walk back to Tier 1 (3 steps), that's the limit. Don't spiral.
4. **Tier 1 is the floor.** If Tier 1 is wrong, the reader doesn't have the concept at all. Log it and move on.
5. **On recovery, step back up.** If the reader gets the Tier 2 follow-up right, try Tier 3 before re-attempting Tier 4.

---

## Sequence Templates

### Tier 4 → 3 → 2 → 1 (full walkback)

```markdown
**Original (Tier 4, Break):**
"Construct a string that passes `detect_stego()` but contains hidden text."

**Wrong answer.** Reader tried zero-width spaces, which the detector catches.

---

**Follow-up 1 (Tier 3, Build):**
"Let's step back. Write a version of `detect_stego()` that checks for characters in the Unicode Cf category. What characters would it catch that a blocklist misses?"

*Purpose: verify the reader can build the mechanism before trying to break it.*

**If wrong →**

---

**Follow-up 2 (Tier 2, Predict):**
"What does `unicodedata.category(char)` return for a zero-width space? For a regular space? For a tag character?"

*Purpose: verify the reader can predict behavior of the tools involved.*

**If wrong →**

---

**Follow-up 3 (Tier 1, Recall):**
"What is Unicode category Cf? What does the 'C' stand for? What does the 'f' stand for?"

*Purpose: verify basic recall of the concept.*

**If wrong → Log misconception:**
```yaml
concept: "Unicode character categories"
tier_failed: 4
walkback_depth: 3
wrong_answer_pattern: "doesn't know Unicode category system"
suggested_remediation: "revisit Part 2, cells 4-6 on character categories"
```
```

### Tier 5 → 4 → 3 (partial walkback)

```markdown
**Original (Tier 5, Transfer):**
"How does the normalize-then-scan pattern apply to SQL injection defense?"

**Wrong answer.** Reader mapped to "input validation" generically, not parameterized queries.

---

**Follow-up 1 (Tier 4, Break):**
"What happens if you try to detect SQL injection with a blocklist of known SQL keywords? Construct an input that bypasses it."

*Purpose: make the reader experience WHY blocklists fail (parallel to Unicode blocklists).*

**If right →** Re-attempt Tier 5 with new understanding.
**If wrong →**

---

**Follow-up 2 (Tier 3, Build):**
"Implement `normalize_for_scan()` for the Unicode case. What does it do to the input before the regex runs?"

*Purpose: verify the reader can build the mechanism they're being asked to transfer.*

**If right →** Step back up to Tier 4.
**If wrong → Log misconception.**
```

### Tier 6 → 5 → 4 (teaching → transfer → break)

```markdown
**Original (Tier 6, Teach):**
"Explain normalize-then-scan to a product manager using a food safety analogy."

**Wrong answer.** Analogy was too vague ("it's like washing food").

---

**Follow-up 1 (Tier 5, Transfer):**
"Before we try the analogy again: can you name another security domain that uses the same normalize-then-scan pattern? What are the structural parallels?"

*Purpose: verify the reader sees the pattern before mapping it to a metaphor.*

**If wrong →**

---

**Follow-up 2 (Tier 4, Break):**
"Why can't a blocklist solve this problem? Construct a specific example that defeats a blocklist approach."

*Purpose: the reader needs to FEEL the limitation before they can explain it.*
```

---

## Recovery Path

When a follow-up is answered correctly, the reader steps back UP. Don't re-ask the original question immediately. Rebuild through intermediate tiers.

```
Original: Tier 4 (wrong)
    ↓
Follow-up: Tier 3 (wrong)
    ↓
Follow-up: Tier 2 (RIGHT ✓)
    ↓
Re-attempt: Tier 3 (RIGHT ✓)  ← intermediate step, NOT the original
    ↓
Re-attempt: Tier 4 (original, rephrased)
```

### Rephrasing the re-attempt

The re-attempt at the original tier uses the same concept but different specifics:

- Different input data
- Different function or context
- Different adversarial approach
- Same cognitive demand

This prevents pattern-matching the answer from the follow-up conversation.

---

## Misconception Log Schema

When a Socratic sequence bottoms out (Tier 1 wrong, or wrong at max depth):

```yaml
- concept: string           # the concept being tested
  source_section: string     # where it was taught in the source content
  original_tier: int         # which tier the original question was at
  walkback_depth: int        # how many steps down before bottoming out
  wrong_answer_pattern: string  # what the reader said/did wrong (pattern, not verbatim)
  timestamp: ISO 8601
  suggested_remediation: string  # specific cells, sections, or exercises to revisit
```

### Who reads the misconception log

| Consumer | How They Use It |
|----------|----------------|
| `lesson-generator` (revision mode) | Targets confused concepts for re-teaching. May add a new section, interlude, or war story to address the gap. |
| `assessment-generator` (next run) | Generates misconception-targeted questions. These are distributed throughout the assessment, not clustered. |
| The learner | Transparency. "Here's where you have gaps. Here's what to revisit." |
| `outline-writer` | When planning a new module that depends on the misconceived concept, adds explicit bridging. |

### Misconception patterns to log

| Pattern | What It Means | Remediation Direction |
|---------|---------------|----------------------|
| Wrong at Tier 1 | Doesn't have the concept at all | Revisit source content from the DO stage |
| Right at Tier 1-2, wrong at Tier 3 | Knows it but can't build it | More CODE exercises with scaffolding |
| Right at Tier 1-3, wrong at Tier 4 | Can build but can't think adversarially | Needs more Break exercises; exposure to failure modes |
| Right at Tier 1-4, wrong at Tier 5 | Understands the specific case but can't generalize | More cross-domain examples; explicit principle extraction |
| Right at Tier 1-5, wrong at Tier 6 | Understands deeply but can't simplify for others | Practice audience-calibrated explanation; work on analogies |

---

## When to Skip Socratic Follow-Ups

Not every wrong answer needs a walkback:

- **Tier 1-2 wrong answers:** No follow-up needed. Just show the correct answer. The reader either remembers or they don't; Socratic questioning at Tier 0 doesn't exist.
- **Time-constrained assessments:** Skip follow-ups. Log wrong answers for later analysis.
- **The reader explicitly says "I don't know":** Skip directly to showing the answer and log as misconception. Don't interrogate.
- **The wrong answer is a typo/careless error:** If the reasoning is clearly correct but the answer has a mechanical error, mark as partial credit and move on. No Socratic sequence for typos.
