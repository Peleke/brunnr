# Rubric Templates by Tier

Grading rubrics for each tier. Every question needs a rubric; these templates ensure consistency.

---

## General Rubric Rules

1. **Specific and measurable.** "Demonstrates understanding" is never sufficient. Name what the answer must contain.
2. **Partial credit is real.** Most questions have a spectrum between wrong and right. Define the levels.
3. **Common mistakes are listed.** These become misconception log entries when triggered.
4. **Socratic follow-up is attached.** Every Tier 3+ rubric includes the first follow-up question for wrong answers.

---

## Tier 1: Recall Rubric

```markdown
**Full (1.0):** Answer includes [specific fact/term/definition].
**Partial (0.5):** Answer includes [related but imprecise fact]. Missing: [what's missing].
**Wrong (0.0):** Answer is [common wrong answer] or unrelated.
**Common mistake:** [misconception this question targets]
```

### Example
```markdown
**Full (1.0):** Correctly identifies U+200B (zero-width space), U+200D (zero-width joiner), U+00AD (soft hyphen) or similar invisible characters by codepoint or name.
**Partial (0.5):** Names the concept of invisible characters but can't cite specific codepoints or Unicode names.
**Wrong (0.0):** Confuses invisible characters with whitespace characters (space, tab, newline).
**Common mistake:** Thinking whitespace characters (U+0020, U+0009) are the same as zero-width characters.
```

---

## Tier 2: Predict Rubric

```markdown
**Full (1.0):** Correctly predicts [specific output/behavior] AND explains why.
**Partial (0.5):** Predicts [correct output] but explanation is [incomplete/wrong mechanism].
    OR: Predicts [close but wrong output] with [correct reasoning about mechanism].
**Wrong (0.0):** Prediction is wrong AND reasoning doesn't engage with the relevant mechanism.
**Common mistake:** [what readers typically get wrong about this prediction]
```

### Example
```markdown
**Full (1.0):** Predicts that `re.search(r'curl', 'сurl')` returns None, and explains that the Cyrillic с (U+0441) is a different codepoint than Latin c (U+0063), so the regex doesn't match.
**Partial (0.5):** Predicts None but explains it as "the characters look different" (wrong mechanism — they look identical; it's the codepoints that differ).
    OR: Predicts a match but correctly explains that regex operates on codepoints (contradiction reveals incomplete understanding).
**Wrong (0.0):** Predicts a match with no engagement with the codepoint/glyph distinction.
**Common mistake:** Assuming visual identity implies codepoint identity.
```

---

## Tier 3: Build Rubric

```markdown
**Full (1.0):** Implementation [passes all test cases] AND [handles edge case].
    Code is [specific quality criterion: readable / no unnecessary dependencies / O(n) or better].
**Partial — functional (0.7):** Passes [main test cases] but fails [edge case].
    Missing: [what the edge case tests].
**Partial — approach (0.4):** Correct approach but implementation has [bug type].
    Shows understanding of [concept] but fails on [mechanical detail].
**Wrong (0.0):** Implementation doesn't address the specification. Approach is [what they did instead].
**Common mistake:** [typical implementation error]
**Socratic follow-up if wrong:** [Tier 2 question targeting the same concept]
```

### Example
```markdown
**Full (1.0):** `detect_format_chars(text)` correctly identifies all characters with `unicodedata.category(char) == 'Cf'`, returns list of (position, char, unicode_name) tuples, handles empty strings.
**Partial — functional (0.7):** Checks for Cf category but misses characters where `unicodedata.name()` raises ValueError (e.g., U+FEFF BOM). Handles the common cases.
**Partial — approach (0.4):** Uses a hardcoded list of known invisible characters instead of category checking. Shows awareness of the problem but misses the generalization.
**Wrong (0.0):** Checks for whitespace characters or uses `str.isprintable()` (which doesn't catch all Cf characters).
**Common mistake:** Using `str.isprintable()` as a proxy for "invisible" — it returns False for control characters but True for some Cf characters.
**Socratic follow-up:** "What does `unicodedata.category(char)` return for a zero-width space? For a regular space? What's the difference?"
```

---

## Tier 4: Break Rubric

```markdown
**Full (1.0):** Constructs [specific adversarial input] that [defeats the function] AND explains [why it works — which assumption is violated].
**Partial — input only (0.6):** Provides a valid adversarial input but explanation of why it works is [missing/wrong].
**Partial — reasoning only (0.4):** Correctly identifies [the weakness/assumption] but constructed input doesn't actually trigger it.
**Wrong (0.0):** Input doesn't defeat the function AND reasoning doesn't identify a real weakness.
**Common mistake:** [typical failed adversarial approach]
**Socratic follow-up if wrong:** [Tier 2 question about the function's mechanism]
```

### Example
```markdown
**Full (1.0):** Constructs a string using tag characters (U+E0061-U+E007A) to hide text, which bypasses a detector that only checks for BMP invisible characters. Explains that tag characters live in Plane 14 (above U+E0000) and most detectors don't check supplementary planes.
**Partial — input only (0.6):** Uses tag characters successfully but explains it as "the detector doesn't know about these characters" without identifying the BMP/supplementary plane distinction.
**Partial — reasoning only (0.4):** Correctly identifies that supplementary plane characters bypass BMP-only detection, but the constructed string uses variation selectors (which the detector does catch).
**Wrong (0.0):** Tries to bypass the detector with regular ASCII characters or common zero-width characters that the detector already catches.
**Common mistake:** Trying to bypass detection with characters the detector already handles (ZWSP, ZWJ) instead of finding characters outside its scope.
**Socratic follow-up:** "What Unicode range does the detector check? What's the highest codepoint it knows about?"
```

---

## Tier 5: Transfer Rubric

```markdown
**Full (1.0):** Identifies a valid parallel in [target domain], maps [N key aspects] of the original concept to the new domain, AND identifies [where the parallel breaks down / a key difference].
**Partial — surface (0.5):** Identifies a valid parallel but mapping is shallow — only [1 aspect] mapped. Missing: [deeper structural parallel].
**Partial — forced (0.3):** Parallel is a stretch. The mapped concept doesn't genuinely apply to [target domain] in a useful way. Shows effort but not understanding.
**Wrong (0.0):** No valid parallel identified, or the "parallel" is restating the original concept in different words.
**Common mistake:** [typical shallow transfer attempt]
**Socratic follow-up if wrong:** [Tier 3 question to verify they can build the concept before transferring it]
```

### Example
```markdown
**Full (1.0):** Identifies SQL parameterized queries as a parallel to skeleton normalization. Maps: (1) both preprocess input before evaluation, (2) both neutralize injection by separating data from control, (3) both make the "blocklist" approach obsolete. Identifies key difference: SQL parameterization operates at the query boundary; Unicode normalization operates on the text itself before any downstream processing.
**Partial — surface (0.5):** Mentions "input sanitization" as a general concept but doesn't map specific aspects. Says "both are about cleaning input" without structural detail.
**Partial — forced (0.3):** Maps to "antivirus signature databases" (also a blocklist approach), but this is the WRONG parallel — it's an example of the approach that fails, not the one that works.
**Wrong (0.0):** Says "I can't think of a parallel" or maps to an unrelated concept.
**Common mistake:** Mapping to other blocklist-based approaches (which are the PROBLEM, not the SOLUTION parallel).
**Socratic follow-up:** "What does normalize_for_scan() do to the input BEFORE the regex runs? Can you describe that step?"
```

---

## Tier 6: Teach Rubric

```markdown
**Full (1.0):** Explanation is [accurate], [appropriate for audience], [uses concrete examples], AND [avoids jargon the audience doesn't have / defines jargon before using].
    The audience would [understand/be able to act on] the explanation.
**Partial — accurate but wrong audience (0.6):** Explanation is technically correct but uses [jargon/framing] the target audience wouldn't understand. Would work for [a different audience].
**Partial — accessible but imprecise (0.5):** Explanation is accessible to the audience but [oversimplifies / makes a technical error / omits a key aspect].
**Wrong (0.0):** Explanation is [technically wrong] OR [so abstract it teaches nothing].
**Common mistake:** [typical failure mode when teaching this concept]
**Socratic follow-up if wrong:** [Tier 1 question to verify they recall the concept before trying to teach it]
```

### Example (Tier 6, High: analogy construction)
```markdown
**Full (1.0):** Food safety analogy covers: (1) inspection alone fails — you can't detect every contaminant by looking at food (parallel: blocklist can't catch every invisible character); (2) normalization = cooking food to a safe temperature — it neutralizes threats regardless of which specific pathogen is present (parallel: stripping Cf characters + skeleton normalization neutralizes stego regardless of which technique is used); (3) where it breaks down — cooking destroys the food's original form, but Unicode normalization preserves the visible text.
**Partial — accurate but wrong audience (0.6):** Uses the analogy but explains normalization in Unicode terms ("strips category Cf characters") that a chef wouldn't understand.
**Partial — accessible but imprecise (0.5):** Good analogy but claims normalization "removes all dangerous characters" (oversimplification — homoglyph normalization maps to skeletons, it doesn't remove).
**Wrong (0.0):** Analogy doesn't map to the actual mechanism, or is just "bad food = bad Unicode."
**Common mistake:** Making the analogy too vague ("it's like washing your hands") without mapping specific aspects of the defense.
**Socratic follow-up:** "What specifically does normalize_for_scan() do? Walk me through the three steps."
```

---

## Rubric Quality Checklist

For every rubric in the assessment:

- [ ] Full marks criteria name specific elements the answer must contain
- [ ] Partial marks distinguish between "right approach, wrong details" and "wrong approach"
- [ ] Wrong answer describes a specific common wrong answer, not just "incorrect"
- [ ] Common mistake is a real misconception, not a tautology ("the common mistake is getting it wrong")
- [ ] Socratic follow-up is present for Tier 3+ questions
- [ ] Follow-up targets the same concept at a lower tier
