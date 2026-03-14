# Engagement Pass

A retrofit skill that adds interactive engagement elements to existing Jupyter notebooks.

## What It Does

Analyzes a static notebook and adds:
- **Concept map** — interactive arc progress map after imports
- **Plotly conversions** — key matplotlib plots upgraded with hover context
- **Video embeds** — curated YouTube videos at concept introduction points
- **Widgets** — parameter exploration via sliders and buttons
- **Animations** — FuncAnimation for time-evolution concepts
- **"Build a toy" exercises** — interactive construction exercises

## When to Use

Use this skill on notebooks that are already written and working but are purely static (matplotlib only, no widgets, no videos). The `lesson-generator` skill now generates with engagement built in — use `engagement-pass` only for upgrading older notebooks.

## Invocation

Say any of:
- "Add engagement to Module 0.1"
- "Make the probability notebook interactive"
- "Retrofit Module 0.2"
- "Engagement pass on 0.1-taste-demo-core.ipynb"

## Process

1. **Analyze** — Scan for enhancement opportunities (static plots, missing concept map, parameter explorations, exercise gaps)
2. **Prioritize** — Apply engagement budget (max 1 concept map, 3 videos, 4 Plotly conversions, 3 widgets, 2 animations, 1+ build-a-toy)
3. **Apply** — Insert enhancements using templates from `lesson-generator/interactive-templates.md`
4. **Validate** — Verify all cells run, story flow preserved, no widget overload

## Quality Checklist

After every engagement pass, verify:

- [ ] Concept map present after imports
- [ ] 1-3 strategic video embeds at concept introductions
- [ ] Key plots converted to Plotly (hover data is useful)
- [ ] At least 1 widget for parameter exploration
- [ ] 0-1 animations for dynamic concepts
- [ ] At least 1 "build a toy" exercise
- [ ] Story flow preserved
- [ ] All cells run sequentially without error

## What It Does NOT Do

- **Rewrite narrative** — Story, voice, and flow are sacred
- **Restructure exercises** — Exercise order stays the same; "build a toy" is added alongside
- **Add theory content** — Only interactive wrappers around existing content
- **Fix bugs** — Fix code errors before running an engagement pass
- **Change belt level** — Core stays Core, Depth stays Depth

## Example: Before/After

**Before** (static matplotlib):
```python
ax.scatter(salience_scores, intuitive, c='#2196F3')
```

**After** (Plotly with hover):
```python
plotly_scatter_with_context(
    x=salience_scores, y=intuitive_ratings,
    labels=[f"Entry {i}" for i in range(len(ENTRIES))],
    descriptions=[e.task[:60] for e in ENTRIES],
    title="SalienceScorer vs. Intuitive Ratings"
)
```

Hover over any point to see which entry it is and what the task was.

## Reference Files

All engagement patterns, templates, and video mappings live in `lesson-generator/`:
- `engagement-patterns.md` — When/how to use each pattern
- `interactive-templates.md` — Copy-paste code blocks
- `video-index.md` — YouTube video IDs per module

## License

MIT
