# Bragi Review: silent-plugin
# Date: 2026-03-09
# Source: article-draft skill (28-rule Bragi Prose Gate)

The article file doesn't exist on disk yet. I'll review the text you provided inline. Here's the compact Bragi review.

---

## Bragi Review: "Silent Plugin, Eight Layers Deep"

### R1: No em dashes

- **Closing paragraph** (per your note): contains at least one `---`. Confirm the closing prose uses `--` or restructures to avoid it.
- **"The Symptom" section**: `"you don't need the system to tell you where it failed -- you need the system to tell you what it produced at each stage"` -- if the final version has an em dash here, flag it. Rewrite as two sentences or use a period.

### R7: No punchy fragment marketing

- **"No error. No warning. Nothing."** in The Symptom -- three consecutive fragments for dramatic effect. This is borderline marketing cadence. Appears again in The Second Root Cause: "No error. No warning." Same pattern.
- **"No linwheel. No wildcard. No `group:plugins`."** in The Second Root Cause -- triple fragment, same pattern again.
- Fix: Merge into flowing prose. E.g., "The log showed no error, no warning, and no mention of the plugin." For the second instance: "The allowlist contained no linwheel tools, no wildcard, and no plugin group entries."

### R8: No tricolon for rhythm (escalation test)

- **"No error. No warning. Nothing."** -- classic ascending tricolon. Fails the escalation test because it's used for dramatic punch, not informational escalation.
- **"No linwheel. No wildcard. No `group:plugins`."** -- same structure. Three parallel negations for rhythm.
- Fix: Already covered above. Merge these into single sentences.

### R19: No puffery

- **"This is the worst kind of bug"** -- inflated claim. "Worst kind" is puffery. The article proves the bug is subtle and hard to find; let the evidence do the work. Rewrite: "The bug where everything looks correct at every layer you check, until you find the layer you haven't checked."
- **"eight layers"** in the title -- this is fine; it's literally true. Not puffery.

### R22: No wall paragraphs (1 thought per visual unit)

- **"The Root Cause" paragraph 2** ("Meanwhile, the tool policy system..."): This paragraph packs three distinct thoughts: (a) how `*` flows into a Set, (b) that `isOptionalToolAllowed` never checks for `*`, and (c) that the policy filtering layer compiles `*` differently but optional tools never reach it. Split into three visual units.
- **"Why This Was Hard to Find"**: If the 6 reasons are a numbered list, fine. If any of those list items are multi-sentence paragraphs, each should contain one thought only.
- **"The Lesson" section**: Two paragraphs, but the second paragraph contains two thoughts: (a) the temptation to add logging, (b) the faster approach. These are fine as a contrast pair, but verify they're actually two short paragraphs, not one block.

### R26: No restating obvious

- **"The Lesson" closing**: "You don't need the system to tell you where it failed -- you need the system to tell you what it produced at each stage." This restates the binary-search method already described in the paragraph above it and in "The Debugging Method" section. The reader already has this. Cut or compress.
- **"The Fix" sections**: "Two lines" before a code block is borderline R26 -- the reader can see it's two lines. But it's short enough to let pass.

### Additional flags

**R5 (inflated significance)**: "This is the worst kind of bug" (already caught under R19, but also R5).

**R25 ("not just X but Y")**: Not present. Clean.

**R10 (challenges-and-future-prospects)**: The closing paragraph about "three subsystems evolving independently" smells like a challenges-and-future-prospects windup. If it ends with forward-looking implications ("as the system grows..."), cut it. If it's a factual observation about root cause, keep it tight.

**R21 (blunt fragment negation)**: "Nothing." as a standalone sentence in The Symptom. Pure fragment negation for effect. Kill it or fold into the preceding sentence.

---

### MDX Conversion?

Yes, this article benefits from MDX:

1. **The 8-layer diagram** is a natural SVG. A vertical pipeline showing layers 1-8 with color-coding (green for pass, red for the two failure layers at 5 and 8) would make the architecture section immediately scannable. This is worth building.
2. **Code blocks** with syntax highlighting are standard MDX.
3. **The debug log output** could use a styled callout component if one exists in the site.

### SVGs needed?

One SVG, high value: the **8-layer filtering pipeline**. Label each layer, mark layers 5 and 8 in red, show the data flow narrowing. This is the article's central explanatory device and text alone undersells it.

### Pelekification opportunities

1. **The `Set.has()` insight is the crown jewel.** The wildcard sitting in a Set, "inert, matching nothing" -- that's a great line. Build the article's thesis around it: systems that look like they support wildcards but actually do exact matching are a class of bug, not a one-off.
2. **Name the bug class.** "Semantic wildcard, syntactic literal" or something shorter. Give readers a handle they can reuse. This is the kind of conceptual naming that makes articles get cited.
3. **The "binary search the layers" debugging method is yours.** It's the portable takeaway. Make it a titled subsection with a concrete 3-step recipe, not prose buried in "The Lesson." This is the part people will bookmark.
4. **Show the actual bash commands.** The Debugging Method section references bash but the prompt text shows `[bash code]` as placeholder. The real commands are the proof. Include them.
5. **Cut "The Lesson" down to 2 sentences.** The debugging method section already teaches the lesson. Don't re-teach it in prose. End on the concrete method, not a moral.

---

### Summary of required fixes

| Rule | Location | Severity |
|------|----------|----------|
| R1 | Closing paragraph, possibly Lesson section | Must fix |
| R7 | "No error. No warning. Nothing." (x2), "No linwheel..." | Must fix |
| R8 | Same tricolons as R7 | Must fix |
| R19 | "worst kind of bug" | Must fix |
| R22 | Root Cause paragraph 2 (3 thoughts in 1 block) | Must fix |
| R26 | Lesson section restates Debugging Method | Should fix |
| R21 | "Nothing." standalone fragment | Should fix |
| R5 | "worst kind of bug" (overlap with R19) | Already covered |

Article is structurally strong. The core material (two bugs, two layers, Set vs. compiled wildcard) is genuinely interesting and well-sequenced. The fixes are all surface-level: kill the tricolons, split the wall paragraph, cut the puffery, remove the em dash. The bigger opportunity is the SVG and the Pelekification moves (name the bug class, promote the debugging recipe).