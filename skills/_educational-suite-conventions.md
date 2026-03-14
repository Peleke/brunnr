---
name: educational-suite-conventions
description: "Shared conventions for the educational content suite: the DO→NOTICE→CODE→NAME contract, prerequisite chain format, jargon-earning schema, skill handoff protocol, prose quality gate, and voice rules."
---

# Educational Suite Conventions
## Preamble — loaded by every skill in the educational content suite

All skills in the educational content suite MUST follow these conventions.

The suite produces teaching content: tutorials, lessons, notebooks, assessments. Every skill shares a common pedagogy model, prose quality gate, and interoperability contract.

---

## Suite Members

| Skill | Role | Reads From | Produces |
|-------|------|------------|----------|
| `lesson-generator` | Core pedagogy: DO→NOTICE→CODE→NAME, belt system, zoom levels, voice | Elicitation interview | Curriculum brief, arc syllabi, module specs |
| `outline-writer` | Narrative outlines through structured riffing | Prior module notebook, arc syllabus | Ready-to-generate outline |
| `notebook-builder` | Mechanical .ipynb generation | Approved outline | Jupyter notebook |
| `scaffold-pass` | Architectural scaffolding: designed failures, skeleton-first, accumulation artifacts, reading strategies, troubleshooting, bonus depth | Notebook or outline | Scaffolded content |
| `visual-pass` | Visual injection planning: static diagrams, animations, Manim, expected output, before/after | Any content artifact | Prioritized visual manifest + rendered assets |
| `engagement-pass` | Interactive retrofit: Plotly, widgets, concept maps, video embeds, build-a-toy | Existing notebook | Enhanced notebook |
| `technical-tutorial` | Standalone tutorials with dual arc (SPIN + DO→NOTICE→CODE→NAME) | Topic brief, war stories, prerequisite inventory | Tutorial article + companion artifact |
| `assessment-generator` | 6-tier evaluation with Socratic follow-ups and misconception logging | Tutorial output or module outline, misconception log | Assessment document + rubrics |
| `article-draft` | Technical articles with narrative structure (SPIN arc, no pedagogy loop) | Editorial map, war stories, voice target | Article |

---

## The DO→NOTICE→CODE→NAME Contract

This is the foundational pedagogy model. Every skill that introduces a concept MUST follow this loop. No exceptions.

| Stage | What Happens | Modality | Rule |
|-------|-------------|----------|------|
| **DO** | Experience it. See it, hear it, run it. No labels. | Sensory/interactive | Never skipped. Every concept starts here. |
| **NOTICE** | Guided observation. "What did you notice?" | Reflective | Pattern recognition prompts, not definitions. |
| **CODE** | Build, modify, break. Change parameters. | Tactile/code | The reader constructs understanding. |
| **NAME** | Formalize. Give it its proper name. Connect to theory. | Symbolic | Always last. Name after the reader has built the thing. |

### Concept Primitives

A concept primitive is the smallest unit where confusion is possible. Decompose every concept into primitives. Each primitive runs its own DO→NOTICE→CODE→NAME loop.

Test: "Could someone be confused about this?" If yes, it's not a primitive yet.

### Which skills use this loop

| Skill | How It Uses the Loop |
|-------|---------------------|
| `lesson-generator` | Mandatory per concept at every zoom level. Primitives tracked via sensory projection matrix. |
| `outline-writer` | Each section's narrative sketch includes per-primitive loop plan. |
| `technical-tutorial` | Dual arc: SPIN (emotional) runs in parallel with DO→NOTICE→CODE→NAME (cognitive). |
| `assessment-generator` | Tiers map to loop stages: Tier 1=DO recall, Tier 2=NOTICE predict, Tier 3-4=CODE build/break, Tier 5-6=NAME transfer/teach. |
| `notebook-builder` | Implements the loop mechanically in cell ordering. |
| `engagement-pass` | Does NOT reorder content; preserves existing loop structure. |
| `article-draft` | Does NOT use this loop (articles argue, not teach). Uses SPIN arc only. |

---

## Prerequisite Chain Format

Every section in every teaching artifact declares:

```markdown
### Section N: [Title]

**Has**: [functions, concepts, jargon earned from prior sections]
**Adds**: [new capability, concept, or artifact]
**After**: [concrete thing the reader can do that they couldn't before]
```

### The Starting State Rule

The first section establishes what the reader has coming in. Every subsequent section begins by USING something the reader built, not recapping it.

Pattern: `their_function(args) → result → "but notice [gap]"`

### No Forward References

If a section references a concept the reader hasn't built yet, restructure. Discovery order beats logical order. This rule is absolute across all suite skills.

---

## Jargon-Earning Order Schema

Every teaching artifact tracks technical terms:

```markdown
| Term | Introduced In | Earned By |
|------|---------------|-----------|
| [term] | Section N | [what the reader did/built/saw that earned this term] |
```

Rules:
- No term is used before it's earned
- "Earned" means the reader has experienced the concept (DO+NOTICE+CODE) before it gets its name (NAME)
- Terms earned in one artifact carry forward to downstream artifacts (tutorial → assessment)
- Skills that consume upstream output inherit its earned terms without re-teaching

---

## Skill Handoff Protocol

### Pipeline flows

```
lesson-generator ──→ outline-writer ──→ notebook-builder
                                              ↓
                                        scaffold-pass (designed failures, skeleton-first, accumulation)
                                              ↓
                                         visual-pass (diagrams, animations, Manim, expected output)
                                              ↓
                                        engagement-pass (Plotly, widgets, concept maps, videos)
                                              ↓
                                        assessment-generator (6-tier evaluation, Socratic follow-ups)

technical-tutorial ──→ scaffold-pass ──→ visual-pass ──→ assessment-generator

article-draft ──→ visual-pass (diagrams only; no pedagogy pipeline)
```

Each skill in the pipeline reads the output of the prior skill. Skills can be run independently (e.g., engagement-pass on an existing notebook) but the full pipeline ensures nothing is missed.

### Handoff contract

When skill A hands off to skill B:

1. **A declares output format.** The producing skill documents what it outputs (outline, notebook, tutorial, assessment).
2. **B declares input requirements.** The consuming skill documents what it needs (prerequisite chain, earned terms, concept list).
3. **Earned terms carry forward.** B inherits A's jargon-earning order. B does NOT re-teach terms A already earned unless B's audience is different.
4. **Prerequisite chain extends.** B's first section's "Has" includes everything A's last section produced.
5. **Beat/artifact sync carries forward.** If A mapped beats to artifacts, B can reference those artifacts.

### Assessment-generator ← tutorial handoff

The assessment-generator receives:
- Tutorial's prerequisite chain (what concepts exist, in what order)
- Tutorial's jargon-earning order (what terms are available at each point)
- Tutorial's exercise outputs (what the reader built; these are NOT re-tested at the same tier)
- Tutorial's SPIN phase map (assessment pacing respects narrative arc; don't test Tier 5 before Need-Payoff)

The assessment-generator produces:
- Questions at each tier that test BEYOND what the tutorial's exercises covered
- Misconception log entries (fed back to tutorial revision)
- Socratic follow-up sequences for wrong answers (walked back through Tiers 1→3)

---

## Prose Quality Gate

**MANDATORY**: Every skill in the suite that produces prose MUST enforce the Bragi Prose Gate.

This includes:
- `lesson-generator` (narrative intros, outros, section prose)
- `outline-writer` (war story descriptions, bridge text)
- `technical-tutorial` (full article prose)
- `assessment-generator` (question stems, rubric descriptions, Tier 6 teaching prompts)
- `article-draft` (full article prose)
- `notebook-builder` (markdown cells)
- `engagement-pass` (contextual intros for videos, widget descriptions)

The 29 Bragi rules are defined in `article-draft/SKILL.md` Phase 5 and `technical-tutorial/SKILL.md` Phase 5. They are identical. The canonical source is `article-draft/SKILL.md`; `technical-tutorial` inherits them.

Tutorials and assessments do NOT get a prose pass because they're "educational." The quality floor applies everywhere.

---

## Voice Rules

### Shared registers

All suite skills use the same three registers:

| Register | Voice | Source |
|----------|-------|--------|
| A | Frustrated Engineer | Mickens |
| B | Self-Deprecating Narrator | Sedaris |
| C | Respectful Tour Guide | Paul Ford |

### Default ratios by skill

| Skill | A% | B% | C% | Rationale |
|-------|----|----|----|-----------|
| `article-draft` | 40 | 30 | 30 | Articles argue; more frustration and self-deprecation |
| `technical-tutorial` | 25 | 25 | 50 | Tutorials teach; more tour guide |
| `lesson-generator` | 20 | 20 | 60 | Curriculum content is mostly explanatory |
| `assessment-generator` | 10 | 20 | 70 | Questions need clarity above all; Tour Guide dominates |
| `outline-writer` | N/A | N/A | N/A | Outlines are internal artifacts; voice applies at generation time |
| `notebook-builder` | N/A | N/A | N/A | Inherits from the outline it's building from |
| `scaffold-pass` | N/A | N/A | N/A | Structural pass; does not generate prose |
| `visual-pass` | N/A | N/A | N/A | Produces manifests and renders; does not generate narrative prose |
| `engagement-pass` | N/A | N/A | N/A | Preserves existing voice; does not change register |

### Universal voice rules

- One register per paragraph. Blend across sections, not within.
- Never use all three registers in the same paragraph.
- War stories use A+B. Concept explanations use C. Exercises use C.

---

## Engagement System

### Shared resources

These files live in `lesson-generator/` and are referenced by multiple skills:

| File | Purpose | Used By |
|------|---------|---------|
| `engagement-patterns.md` | Pattern library: when/how to use videos, Plotly, widgets, animations, concept maps, build-a-toy | lesson-generator, notebook-builder, engagement-pass, technical-tutorial |
| `interactive-templates.md` | Copy-paste code templates for all engagement patterns | notebook-builder, engagement-pass |
| `video-index.md` | YouTube video ID mappings per module/section | notebook-builder, engagement-pass |

### Budget limits (per artifact)

| Element | Max per notebook/tutorial | Required? |
|---------|--------------------------|-----------|
| Concept map | 1 | Yes (notebooks); No (tutorials) |
| Video embeds | 3 | No |
| Plotly conversions | 4 | No |
| Widgets | 3 | No |
| Animations | 2 | No |
| Build-a-toy exercise | 1+ | Yes |

### Color palette (shared)

All interactive visualizations use:
```
Primary:   #2196F3  (blue)
Secondary: #FF9800  (orange)
Success:   #4CAF50  (green)
Accent:    #E91E63  (pink)
Highlight: #9C27B0  (purple)
```

Plotly template: `plotly_white`. No dark backgrounds for plots (they live in notebooks with variable themes).

---

## Exercise Taxonomy

### Tutorial exercises (from `technical-tutorial`)

| Tier | Name | Tests |
|------|------|-------|
| Verify | Confirms understanding | Run known input, check output |
| Extend | Builds capability | Modify what you built for a new case |
| Break | Builds adversarial intuition | Defeat your own system |

### Assessment tiers (from `assessment-generator`)

| Tier | Name | DO→NOTICE→CODE→NAME Stage | Tests |
|------|------|---------------------------|-------|
| 1 | Recall | DO | Can you remember? |
| 2 | Predict | NOTICE | Can you simulate mentally? |
| 3 | Build | CODE | Can you construct it? |
| 4 | Break | CODE (adversarial) | Can you find edges/failures? |
| 5 | Transfer | NAME | Can you apply elsewhere? |
| 6 | Teach | NAME (Feynman) | Can you explain to someone else? |

### Mapping between systems

| Tutorial exercise | Assessment tier(s) | Overlap rule |
|-------------------|-------------------|--------------|
| Verify | Tier 1-2 | Assessment tests in NEW contexts the tutorial didn't cover |
| Extend | Tier 3 | Assessment tests with different parameters/domains |
| Break | Tier 4 | Assessment tests with adversarial inputs the reader hasn't seen |
| (none) | Tier 5-6 | Transfer and Teach are assessment-only; tutorials don't cover these |

The assessment-generator MUST NOT duplicate tutorial exercises at the same tier with the same context. It generates questions that test the same concept in contexts the tutorial didn't use.

---

## Shared Anti-Patterns

These are banned across the entire suite:

1. **Definition-first openings.** Never start with "X is defined as..." Start with experience (DO).
2. **Concept before code.** Never introduce notation or terminology before the reader has built something.
3. **Forward references.** Never say "we'll see later why this matters." Restructure.
4. **Jargon-before-earned.** Never use a term before the reader has experienced the concept it names.
5. **Recap instead of use.** Never "recap" a prior section. USE what was built. Run it. Then reveal the gap.
6. **Prose that sounds like ChatGPT.** Bragi gate is mandatory. No exceptions. No "educational" exemptions.
7. **Standalone code without narrative.** Every code block has a beat; every beat has a code block (in teaching artifacts).
8. **Busywork exercises.** If an exercise doesn't build capability or reveal something surprising, cut it.
9. **Toy-only assessment.** Every assessment must include at least one question using the reader's own real data/tools.
10. **Skipping DO.** Every concept starts with experience. If the reader's first encounter is a definition, the teaching has failed.
