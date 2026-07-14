# Deck Spec — the human-facing talk-through deck

The deck is generated FROM the dossier, not written separately. Part 0 and Part 1 come from Part A; Part 2 comes from the real codebase (Part B's architecture task). Built to be talked through on a screen-record or Loom, so one idea per slide, presenter-friendly.

Build it with the **artifact-design skill** and deploy as an Artifact (default-private). Do not template the visual identity; derive palette and type from the subject.

## Three parts, three audiences
- **Part 0 · The Decision** (for the partner / decision-maker): the opportunity, the economics, the confidence boundaries (proven vs unproven, the honest slide), and the decision to make.
- **Part 1 · The Pitch** (for a prospect): the persuasion arc, reframe → stakes → why-it-fails → the moat (the peak) → the offering → who-buys → the motion.
- **Part 2 · The Architecture** (for the technical room): the diagram, the one invariant, the layers grounded in the real code, the through-line.

## Slide outline (adapt count to the subject)
**Part 0**
1. Title (overall).
2. For the decision: is this worth pointing a pipeline at?
3. The economics: the cost removed (from Part A's ROI section).
4. Confidence boundaries: high / medium / low, color-coded.
5. The decision: the fields to fill.

**Part 1**
6. The reframe (the hook, the ROI thesis in one line).
7. The stakes.
8. Why the obvious approach fails.
9. The moat (the peak; give it the signal accent).
10. The offering (the ladder).
11. Who buys (the vertical + ease-to-close).
12. The motion (the first yes).

**Part 2**
13. Transition ("now the build").
14. The diagram (embed the real architecture diagram; put it on a light card so it works in both themes).
15. The one invariant.
16-20. The layers, one per slide, with the REAL technical terms in monospace.
21. The through-line (every layer is the same move).

## Design guidance
- **Derive the identity from the subject.** For a compliance/trust subject: cool slate ground, an institutional accent, a warm signal color reserved for the one or two peaks. For a different subject, derive differently. Avoid the AI-default warm-cream-serif and neon-green-on-black looks.
- **Monospace for the real technical terms** in Part 2, so the engineering reads as engineering.
- **Both themes** via a token system (`prefers-color-scheme` + `:root[data-theme=...]` overrides), unless deliberately committing to one visual world.
- **Full-height scroll-snap slides**, one idea each.
- **A reserved accent** spent only on the peaks (the moat, the fail-safe), quiet everywhere else.
- Bragi prose on every slide.

## Loom teach-through
Ship a short spoken script the user reads over the deck, so the deck is talked, not read, and the recording is content. The user learns the material by teaching it.
