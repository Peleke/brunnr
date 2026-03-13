<div align="center">

# runlet

**Turn a braindump into a daily runlist your ND brain can actually execute.**

*One braindump. Four quadrants. Entry points on every hard-to-start task.*

[![brunnr](https://img.shields.io/badge/brunnr-skill-4ade80)](https://github.com/Peleke/brunnr)
[![Version](https://img.shields.io/badge/v1.0.0-e88072)](https://github.com/Peleke/brunnr/tree/main/skills/runlet)

</div>

---

> *The Eisenhower matrix assumes you can reliably assess urgency. ADHD brains can't. Everything is urgent, or nothing is. The problem isn't the person — it's the tool.*

---

## What this does

You have a pile of tasks in your head, in your chat logs, in your notes. Some are easy to start. Some aren't. Some move the needle. Some don't.

**runlet** takes that mess and sorts it into four quadrants based on two axes that actually matter for ND cognition:

<div align="center">
<img src="https://raw.githubusercontent.com/Peleke/brunnr/main/skills/runlet/assets/hero.png" alt="runlet — chaos to order" width="100%" />
</div>

<div align="center">
<img src="https://raw.githubusercontent.com/Peleke/brunnr/main/skills/runlet/assets/flow.svg" alt="runlet flow: braindump → classify → assign → runlist" width="100%" />
</div>

---

## The Matrix

Not Eisenhower. This one uses axes that match how ND brains actually work.

|              | Low Energy Cost | High Energy Cost |
|-------------|----------------|-----------------|
| **Moves [Focus]** | **Do First** — easy to start, payoff is real | **Block Time** — needs ramp-up, but it's the work that pays |
| **Doesn't Move [Focus]** | **Batch** — low-drag maintenance, do in a clump | **Kill or Delegate** — hard AND doesn't pay? why? |

### The axes

**Energy Cost** — how hard is it to **start** this task? Not how hard it is to do. Not how long it takes. The activation barrier. This is universal — it doesn't change with your goals.

**Moves [Focus]** — does this task advance your current primary objective within 30 days? Binary. Yes or no. Defaults to "Money" but configurable: Career, Health, Launch, Job Search, whatever the current chapter demands.

---

## The ND Accommodation

Every **Block Time** item gets an **entry point** — one sentence describing the smallest physical action that starts the task. The task isn't hard. Starting is hard. Give the brain a crack to wedge into.

```markdown
- [ ] Design the API schema
  - *Entry point: open schema.ts, add one empty interface for the first endpoint*
```

Entry points are physical (open a file, click a link), completable in < 30 seconds, and unambiguous. No "think about" or "consider."

---

## Install

### Claude Code

```bash
# If you haven't added the brunnr marketplace yet
/plugin marketplace add Peleke/brunnr

# Install
/plugin install runlet@brunnr-skills
```

### CLI

```bash
# Install brunnr
uv tool install brunnr    # or: pipx install brunnr

# Install the skill
brunnr install runlet
```

---

## Usage

### Claude Code

```bash
/runlet
```

Then braindump. Paste whatever's in your head:

```
need to do outreach, fix the carousel bug, cross-post AX-07,
find atlanta meetups, rhythm pass on articles, onboard buddy to linwheel
```

### With focus

```
/runlet focus: Health

schedule physical, meal prep, research meds with psych notes,
go for a walk, cancel sugary snack subscription
```

### With carry-forward

Provide yesterday's runlist and unchecked items carry forward automatically. Three carries → forced decision: block time or kill it.

---

## Example

**Input:**
```
need to do linkedin outreach, fix the carousel bug, cross-post AX-07,
find atlanta meetups, rhythm pass on articles, reply to post comments,
follow up on old outreach, discord: join servers + answer questions
```

**Output:**

```markdown
# Runlist — 2026-03-13

**Focus**: Money

## Do First (low energy, moves money)
- [ ] LinkedIn outreach: 5 new conversations
- [ ] Reply to all post comments (< 2hr old)
- [ ] Follow up on 3-5 day old unanswered outreach

## Block Time (high energy, moves money)
- [ ] Discord: join 3 servers, answer 2-3 questions with substance
  - *Entry point: open Anthropic Discord → MCP channel → find one question you know the answer to*
- [ ] Atlanta meetup search → register for 2-3 events
  - *Entry point: open lu.ma, search "Atlanta AI", bookmark first 3 results*

## Batch (low energy, doesn't move money)
- [ ] Dev.to/Hashnode account setup + cross-post AX-07

## Kill or Delegate
- ~~Rhythm passes on AX-05/06/07~~ → weekend, not tomorrow
- ~~Fix carousel bug~~ → not revenue-blocking; backlog it
```

Plus a machine-readable `RUNLET_SUMMARY` JSON block for agent pings:

```
Morning. 3 Do First, 2 Block Time, 1 Batch.
Top: LinkedIn outreach (5 convos).
```

---

## Focus Swap

Focus isn't a filter — it's a sort key. Tasks are tagged with *all* focuses they move. Swapping focus re-sorts the runlist without losing anything:

```
Focus: Money → Focus: Health

"Meal prep" was Batch → now Do First
"LinkedIn outreach" was Do First → now Batch
```

Like changing the comparator in a heap and running heapify. Energy classifications stay the same; only quadrant assignment changes.

---

## Rules

1. **Do First is the runway.** Start every day here.
2. **Block Time always gets entry points.** No exceptions.
3. **Batch items batch by context.** Minimize context switches.
4. **Kill items get reasons.** Strikethrough + reason. Never silently delete.
5. **3-carry rule.** Three carries → block time or kill. No fourth carry.
6. **No motivation.** No "you've got this!" The list is the list.
7. **Review ≤ 2 min.** If it takes longer, cut more.

---

## How it works

1. You braindump (text, session logs, chat transcripts, anything)
2. runlet extracts atomic tasks (verb-led, completable in one sitting)
3. Each task is classified on Energy Cost (low/high) and Moves [Focus] (yes/no for each known focus)
4. Tasks are assigned to quadrants based on the primary focus
5. Block Time items get entry points. Kill items get reasons. Batch items get context groups.
6. Output: Obsidian markdown + machine-readable summary for agent pings
7. If yesterday's runlist is provided, unchecked items carry forward with tags

---

## Further reading

- [brunnr](https://github.com/Peleke/brunnr) — the skills marketplace
</div>
