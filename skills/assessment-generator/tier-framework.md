# Six-Tier Assessment Framework

Maps to the DO→NOTICE→CODE→NAME pedagogy loop.

## Overview

| Tier | Name | Loop Stage | Cognitive Verb | Difficulty Range |
|------|------|------------|----------------|------------------|
| 1 | Recall | DO | Remember | Retrieve facts → synthesize multiple facts |
| 2 | Predict | NOTICE | Simulate | Familiar input → edge case input |
| 3 | Build | CODE | Construct | Complete partial → implement from description |
| 4 | Break | CODE (adversarial) | Defeat | Find one bug → identify fundamental limitation |
| 5 | Transfer | NAME | Apply elsewhere | Close domain → distant domain |
| 6 | Teach | NAME (Feynman) | Explain | Peer audience → unrelated audience |

## Tier Progression Invariant

A concept should not be tested at Tier N+1 until it has been tested at Tier N (within the same assessment). The one exception: if the tutorial's exercises already covered Tiers 1-3, the assessment can start at Tier 4 for that concept.

## Difficulty Calibration

Each tier has three internal difficulty levels.

### What makes a question harder (universal)

| Factor | Low → High |
|--------|-----------|
| Input familiarity | From tutorial → never seen before |
| Concept combination | Single concept → multiple concepts composed |
| Domain distance | Same domain → distant domain (Tier 5-6) |
| Answer format | Multiple choice → open-ended |
| Starter code | Provided → no scaffold |
| Edge conditions | Happy path → adversarial input |

### Default distribution within each tier

```
Low:    30%  — confidence building
Medium: 50%  — core assessment
High:   20%  — stretch / depth identification
```

### Alternative distributions

| Assessment Purpose | Low | Medium | High |
|--------------------|-----|--------|------|
| Diagnostic (find gaps) | 40% | 40% | 20% |
| Standard (measure understanding) | 30% | 50% | 20% |
| Certification (prove mastery) | 20% | 40% | 40% |
| Confidence-building (early learner) | 50% | 40% | 10% |

## Tier × Difficulty Matrix (example: Unicode steganography)

| Tier | Low | Medium | High |
|------|-----|--------|------|
| 1 Recall | "What is a codepoint?" | "What Unicode range contains tag characters?" | "Name three Unicode categories that produce invisible output, with a codepoint from each" |
| 2 Predict | "What does `len('Hello')` return?" | "What does `detect_stego()` return for a string with one ZWSP?" | "What happens when `detect_stego()` receives only variation selectors with no base characters?" |
| 3 Build | "Complete `inspect_string()` — fill in the category lookup" | "Implement `encode_tags(cover, secret)` given this docstring" | "Write a Unicode normalizer that handles homoglyphs, ZWC, and tag chars" |
| 4 Break | "Find the bug in this detector (missing Cf check)" | "Construct a string that passes `detect_stego()` but contains a hidden payload" | "Identify a class of invisible characters that no blocklist approach can fully cover" |
| 5 Transfer | "How would skeleton normalization help in email phishing detection?" | "Design input validation for a web form that accepts international usernames" | "What other security domain uses the normalize-then-scan pattern? Describe the parallel." |
| 6 Teach | "Explain homoglyphs to a developer who knows Unicode" | "Explain why blocklists fail to a product manager" | "Explain normalize-then-scan to a chef using a food safety analogy" |
