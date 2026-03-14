# Engagement Patterns — Pattern Library

Reusable engagement patterns for Aegir notebooks. Referenced by both `lesson-generator/SKILL.md` and `engagement-pass/SKILL.md`.

---

## 1. Video Embeds

**When to use**: After building a concept in code, to reinforce with a different voice/visual style. Videos *complement* code — they never replace it.

**Placement rules**:
- Sequence: Build → Verify → Video → Name (always after the reader has done the work)
- Max 1 video per major section; 2-4 per core notebook total
- Place in its own markdown cell with a contextual intro (1-2 sentences explaining why this video is relevant)
- Never use a video as the *introduction* to a concept — the reader earns the concept first, then the video deepens it

**Quality bar**:
- Video must be from a trusted source (3Blue1Brown, StatQuest, McElreath, Veritasium, Numberphile)
- Video must target a *specific* concept covered in the surrounding cells (not "general probability")
- Include timestamp if the relevant section starts after the first minute

**Anti-pattern**: "Watch this video to learn about X" → then the notebook repeats what the video said. The video should add a *different angle*, not redundant coverage.

**Template**: See `interactive-templates.md` → Video Embed section.

---

## 2. Interactive Plots (Plotly)

**When to use**: When the reader would benefit from hovering, rotating, filtering, or zooming. Plotly adds value when the data has multiple dimensions or when individual data points carry meaningful context.

**Decision heuristic**:
| Use Plotly | Stay matplotlib |
|-----------|----------------|
| Scatter with meaningful hover data (entry index, description, outcome) | Simple 2D line/bar comparisons |
| 3D surfaces (parameter spaces, loss landscapes) | Static concept illustrations |
| Animated parameter sweeps | FuncAnimation internals |
| Distribution galleries (switch between distributions) | Hero-adjacent simple plots |
| Any plot where "what's that point?" is a natural question | Plots primarily for screenshot/export |

**Placement rules**:
- Replace the matplotlib version, don't add Plotly alongside it (avoid plot duplication)
- Keep the same color palette (`#2196F3`, `#FF9800`, `#4CAF50`, `#E91E63`, `#9C27B0`)
- Always include meaningful hover text — if hover just shows x/y, use matplotlib instead
- Include `fig.update_layout(template='plotly_white')` for consistency

**Quality bar**:
- Hover data must be *useful* (entry name, description, computed values) not just coordinates
- 3D plots must have clear axis labels and a sensible default camera angle
- Animated plots must have play/pause controls and reasonable frame rates

**Anti-pattern**: Converting every matplotlib plot to Plotly "because interactive." If the reader won't hover or rotate, matplotlib is cleaner and renders faster.

---

## 3. Widgets (ipywidgets)

**When to use**: When the reader should explore a parameter space — "what happens if I change this?" Widgets turn passive reading into active experimentation.

**Types**:

### `@interact` slider — simplest pattern
For single or multi-parameter sweeps where the output is a plot or printed value.
- Best for: "Try different values of X and see what happens to Y"
- Max 3 sliders per widget (more = overwhelming)

### Button-triggered simulation
For stochastic processes where the reader wants to "run it again" and see different outcomes.
- Best for: Monte Carlo, random sampling, A/B test simulation
- Include a "Run N times" button alongside "Run once"

### Constrained multi-slider
For parameters that must sum to 1 (like weights) or satisfy other constraints.
- Best for: Weight exploration (w_l + w_s + w_o = 1), prior elicitation
- Enforce constraints programmatically — don't trust the reader to keep weights summing to 1

**Placement rules**:
- Place after the static version of what they're exploring ("Now play with the parameters")
- Max 3 widgets per notebook (widget fatigue is real)
- Include a "reset to defaults" mechanism
- Always show the current parameter values in the output

**Quality bar**:
- Widget must have a clear "aha moment" — there should be a parameter value where something *interesting* happens
- Range and step size must be sensible (don't let sliders produce NaN or division by zero)
- Output must update smoothly (< 500ms per update for sliders)

**Anti-pattern**: Widgets that let you change parameters but the output doesn't change in any interesting way. If tweaking the slider just moves a line up and down linearly, it's not worth a widget.

---

## 4. Concept Maps

**When to use**: At the start of every core notebook, after imports. Shows where this module fits in the arc.

**Types**:

### Arc progress map (required)
- Shows all modules in the current arc
- Highlights the current module
- Grays out future modules
- Uses networkx → plotly for interactivity (hover shows module description)

### Concept dependency DAG (optional)
- For modules with complex prerequisites
- Shows which concepts from prior modules feed into this one
- Useful for Modules 0.4+ where concepts compound

**Placement rules**:
- Arc progress map: always cell 3 (after metadata + imports)
- Concept DAG: optional, after the intro section
- Keep maps small — 5-12 nodes max
- Use consistent colors: completed=green, current=blue, future=gray

**Quality bar**:
- Every node must be labeled clearly (module number + short title)
- Current module must be visually distinct (larger, different color, bold border)
- Hover on nodes shows the module's one-line description

**Anti-pattern**: Concept maps that are too complex to understand at a glance. If you need more than 12 nodes, you're mapping too much.

---

## 5. Animations (FuncAnimation)

**When to use**: When a concept involves evolution over time — convergence, updating, accumulation, Monte Carlo buildup.

**Types**:

### Distribution evolution
- Beta shape morphing as α, β change
- Posterior updating step by step
- Prior → data → posterior animation

### Convergence visualization
- Law of large numbers (sample mean → true mean)
- Bootstrap convergence
- Monte Carlo estimation approaching true value

### Monte Carlo buildup
- Points accumulating in a region
- Hit/miss visualization building up over time

**Placement rules**:
- Always show the static/final version first ("Here's where we end up")
- Then the animation ("Now let's watch how we get there")
- Max 1-2 per notebook (expensive to render, can be slow)
- Use `HTML(anim.to_jshtml())` for inline display — never save to file and re-embed

**Quality bar**:
- Animation must have visible progress (frame counter, iteration number, or running metric)
- Frame rate should be smooth (15-30 fps, 50-200 frames total)
- Must include play/pause via jshtml controls
- The animation must show something that a static plot *can't* — if a static plot tells the same story, skip the animation

**Anti-pattern**: Animating something that doesn't change meaningfully over time. A scatter plot that just adds points one at a time with no visible pattern emerging is not a useful animation.

---

## 6. "Build a Toy" Exercises

**When to use**: At least 1 per core notebook. These are the dopamine payoff — the reader constructs something interactive, not just fills in a function.

**Structure**:
1. **Scenario**: A concrete problem that motivates building the toy ("You want to explore how weight changes affect your scorer")
2. **Components given**: Starter code, helper functions, data — everything they need *except* the assembly
3. **Task**: Wire the components into something interactive (widget + plot, simulator, explorer)
4. **Success criteria**: Specific, verifiable outcomes ("Your simulator should show that...")
5. **Extensions**: Optional enhancements for hyperfocus sessions

**Examples by module**:
- **0.1**: Weight explorer — 3 sliders controlling SalienceScorer weights, live Spearman ρ display
- **0.2**: A/B test simulator — set n_trials, p_treatment, p_control, run experiments
- **0.3**: Prior elicitation tool — "I think X works Y% of the time, ±Z%" → Beta params + plot
- **0.4**: Bayesian updating dashboard — feed observations one at a time, watch posterior evolve
- **0.5**: Hypothesis testing calculator — input data, see p-value + effect size + power
- **0.6**: Bootstrap CI explorer — choose method (percentile, BCa), see how CIs change
- **0.7**: Bandit playground — multiple arms, Thompson vs UCB vs ε-greedy, regret tracking
- **0.8**: Capstone — integrate everything into a working trial runner

**Placement rules**:
- Place in the Exercises section (late in the notebook)
- Provide enough starter code that the task is assembly, not blank-page coding
- Include a working solution in a separate cell

**Quality bar**:
- The finished toy must be *genuinely useful* — something the reader might actually use again
- It must be interactive (widgets, not just a function call)
- Building it must require understanding the module's concepts (not just copy-paste wiring)

**Anti-pattern**: "Build a toy" that's really just "call these three functions in order." The exercise should require *thinking* about how components connect, not just following instructions.

---

## 7. Manim Integration (Future-Ready)

**Status**: Infrastructure available via MCP server. Not yet integrated into notebook generation pipeline.

**When to use** (future):
- Complex geometric derivations (vector transformations, probability spaces)
- Transformation visualizations (matrix operations, coordinate changes)
- Concepts that benefit from cinematic-quality animation (3B1B-style)

**Current pattern**: Place `# TODO: Manim animation — [description]` comments where Manim would add value. Include a description of what the animation would show and why it matters.

**Future pattern** (once MCP is integrated):
1. Generate animation via Manim MCP
2. Render to MP4/GIF
3. Embed rendered video in notebook cell
4. Include a static fallback for non-interactive viewing

**Anti-pattern**: Using Manim for something FuncAnimation handles fine. Manim is for *cinematic* quality — use it sparingly for maximum impact.

---

## General Rules

1. **Enhancement budget**: Max per core notebook:
   - 1 concept map (required)
   - 2-4 video embeds
   - 2-4 Plotly conversions
   - 2-3 widgets
   - 1-2 animations
   - 1+ "build a toy" exercises

2. **Story flow is sacred**: Enhancements *clarify*, they don't *distract*. If adding an interactive element breaks the narrative flow, don't add it. The reader's attention is precious.

3. **Progressive enhancement**: Static content must work without any interactive elements. Plotly degrades to static PNG in nbconvert. Videos are supplementary. The notebook tells its story with or without JavaScript.

4. **Performance**: Widgets and animations add render time. Keep cell execution under 5 seconds for widgets, under 15 seconds for animations. If it takes longer, add a "this may take a moment" note.
