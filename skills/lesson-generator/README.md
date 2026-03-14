# Lesson Generator

A recursive curriculum generation and revision system for Claude Code.

```
Person → Elicitation → Curriculum Brief → Course Map
                                              ↓
                                         Arc Syllabi
                                              ↓
                              outline-writer → Narrative Outline
                                              ↓
                              notebook-builder → Jupyter Notebook
                                              ↓
                              (optional) engagement-pass → Interactive Upgrade
```

## What It Does

Generates educational content at three zoom levels:

| Level | Input | Output |
|-------|-------|--------|
| **Course** | Elicitation interview | Curriculum brief + arc map |
| **Arc** | Course context + theme | Module breakdown + publication checkpoints |
| **Module** | Arc syllabus + prior module | Outline → Notebook (via companion skills) |

Plus **revision mode** for targeted updates with cascade awareness.

## Companion Skills

The lesson-generator defines *pedagogy and voice*. Three companion skills handle specific stages of the module generation pipeline:

| Skill | Location | Role |
|-------|----------|------|
| **outline-writer** | `.claude/skills/outline-writer/` | Riffing → narrative outline. Reads prior module, discovers war stories, negotiates scope, produces a ready-to-generate outline. |
| **notebook-builder** | `.claude/skills/notebook-builder/` | Outline → .ipynb JSON. Translates approved outlines into mechanically correct Jupyter notebooks using Python generation scripts. |
| **engagement-pass** | `.claude/skills/engagement-pass/` | Retrofits existing static notebooks with interactive engagement elements (Plotly, widgets, videos, animations, concept maps). |

### When to Use Which

- **Starting a new module from scratch**: outline-writer → notebook-builder (lesson-generator rules govern both)
- **Upgrading an existing static notebook**: engagement-pass
- **Designing a new course or arc**: lesson-generator directly (course/arc zoom levels)
- **Revising existing content**: lesson-generator revision mode

## Four-Layer Pedagogy

Every concept explanation follows this progression:

1. **Intuition** — Spatiotemporal analogies, physical metaphors
2. **Code + Visualization** — Runnable demos that make concepts visible
3. **CS Speak** — Terminology, complexity, engineering considerations
4. **Mathematical Formalism** — Rigorous notation, definitions, proofs

## Triggers

**Generation:**
- "I want to learn [topic]"
- "Design a curriculum for..."
- "Generate week N syllabus"
- "Create the [notebook-name] notebook"

**Revision:**
- "Update [artifact] to include..."
- "Add [topic] to week N"
- "Fix [issue] in [notebook]"

## Elicitation Dimensions

Course design starts with structured discovery across five dimensions:

1. **Identity** — Cognitive profile, learning style, failure modes
2. **Destination** — Concrete capabilities, capstone vision
3. **Terrain** — Knowledge gaps, emotional blockers, transfer opportunities
4. **Constraints** — Time, energy, environment, accountability
5. **Arc** — Curriculum shape, theory/practice ratio, escape hatches

## Output Structure

```
project/
├── syllabus/
│   ├── README.md              ← Course map
│   ├── curriculum-brief.yaml  ← Elicitation output
│   └── week-NN-[theme].md     ← Week syllabi
└── notebooks/
    └── NN-[module]/
        └── NNx-[name].ipynb   ← Lessons
```

## Engagement System

The lesson-generator includes a built-in engagement system that adds interactive elements to every generated notebook. The system is defined across several reference files that compose with the main skill.

### Reference Files

| File | Purpose |
|------|---------|
| `engagement-patterns.md` | Pattern library — when/how to use each engagement type (video, Plotly, widgets, animations, concept maps, "build a toy") |
| `interactive-templates.md` | Copy-paste code templates for all engagement patterns |
| `video-index.md` | YouTube video ID mappings per module/section (Arc 0) |

### How They Compose with the Skill

`SKILL.md` sections 13-18 define *when* to use engagement patterns during notebook generation. The reference files define *how*:

```
SKILL.md (sections 13-18)     → "Every notebook needs a concept map after imports"
engagement-patterns.md         → "Concept maps use networkx → plotly, max 12 nodes"
interactive-templates.md       → "Here's the arc_progress_map() function to copy"
video-index.md                 → "Module 0.3 uses StatQuest Beta Distribution video"
```

### Adding a New Video

1. Find the video on YouTube, copy the 11-character ID
2. Add an entry to the appropriate module table in `video-index.md`
3. Include: target section (specific cell reference), timing rationale
4. Use `embed_video()` from `interactive-templates.md` in the notebook

### Adding a New Interactive Pattern

1. Define the pattern type in `engagement-patterns.md` (when to use, quality bar, anti-patterns)
2. Add a copy-paste template in `interactive-templates.md`
3. Add a section reference in `SKILL.md` (after section 18)
4. Update the engagement budget limits in `engagement-patterns.md`

### Extending to a New Arc

1. Add a new module table in `video-index.md` for the arc
2. Research and map videos to specific module sections
3. The engagement patterns and templates are arc-agnostic — they work as-is

### Decision Tree: When to Use What

```
Reader would benefit from hovering/rotating/filtering?
  YES → Plotly
  NO  → Does it evolve over time?
          YES → FuncAnimation (or Manim for geometric/cinematic)
          NO  → Does the reader need to explore parameters?
                  YES → ipywidgets (@interact or button)
                  NO  → matplotlib (keep it simple)
```

### Related Skills

| Skill | When to Use |
|-------|-------------|
| `outline-writer` | Before generating a new notebook — produces the narrative outline |
| `notebook-builder` | After outline is approved — constructs the .ipynb file |
| `engagement-pass` | After generation or for existing notebooks — retrofits interactive elements |

See `docs/engagement-system.md` for the full architecture overview.

## Usage

Install as a Claude Code skill:

```bash
# Skills live in .claude/skills/
cp -r lesson-generator /path/to/project/.claude/skills/
```

Then just ask Claude to generate curriculum content. The skill auto-detects the appropriate zoom level and mode.

## License

MIT
