<div align="center">

# dossier-generator

**Turn a thing you built into a deal.**

*One interview, one real codebase. Out comes a dossier a person decides from, a spec their agents execute, and a deck you talk through.*

[![brunnr](https://img.shields.io/badge/brunnr-skill-4ade80)](https://github.com/Peleke/brunnr)
[![Version](https://img.shields.io/badge/v1.0.0-e88072)](https://github.com/Peleke/brunnr/tree/main/skills/dossier-generator)

</div>

---

> *You built the thing. It works. It has been sitting in a repo for three weeks because packaging it feels like a different job.*

---

## What this does

The gap between "I built something" and "someone paid me for it" is usually packaging, and packaging is where builds go to die. You circle. You half-write a deck. You never send it.

**dossier-generator** closes that gap. You answer an interview about the offering, you point it at the codebase, and it emits the artifacts you actually need to put in front of a buyer.

---

## What you get

Three linked artifacts, all generated from one source.

| Artifact | Who reads it | What it is |
|----------|-------------|------------|
| **The dossier** (Markdown) | Both | Part A is a human executive summary you skim and decide from. Part B is an agent implementation spec that executes. |
| **The Part B run output** (Markdown) | An agent, then you | What you get when an agent actually runs Part B: researched comparable clients, account briefs, an offer sheet, a funnel sketch, next actions. This is the artifact you send. |
| **The deck** (HTML) | A person | Part 0 the decision, Part 1 the pitch, Part 2 the architecture. Built to be talked through on a screen recording. |

Keep all three. The Markdown is what an agent runs and what everything else is generated from. The deck is what a human's eyes consume. One does not replace the other.

---

## The I/O contract

Part A ends in a **Decisions Block**: the calls only a human can make. Part B takes that block as its input.

If a decision field is empty, Part B halts on that branch and flags it. It will not guess its way through your pricing.

That contract is the whole reason the two halves can live in one file.

---

## ROI first

The business sections carry a cost-removed argument or they do not ship. You are selling the removal of a cost, so name the cost: labor hours, escalation volume, error and liability tail, audit burden.

Price against the value removed. Not against features, and not against tokens.

---

## Confidence boundaries

Every claim gets marked as one of three things:

- **Proven.** Grounded in code that runs.
- **Reasoned.** A defensible inference you have not tested.
- **Open.** A research question you have not answered.

This is the section a sharp partner respects most, and it is the one people skip. Do not skip it.

---

## Confidentiality

The client gets a codename. Identifying detail gets scrubbed: the real stack, the niche platforms, the corpus, the naming. The architecture stays structurally executable so the work is still real, and it gets generalized into a cloud-neutral analog.

The real client name never appears in the output, even if it surfaces during research.

---

## Install

### Claude Code

```bash
# If you haven't added the brunnr marketplace yet
/plugin marketplace add Peleke/brunnr

# Install
/plugin install dossier-generator@brunnr-skills
```

### CLI

```bash
# Install brunnr
uv tool install brunnr    # or: pipx install brunnr

# Install the skill
brunnr install dossier-generator
```

---

## Usage

```bash
/dossier-generator
```

It runs an executive interview first. Expect to answer:

- **The capability.** What does the system do, in one paragraph?
- **The client.** Who was it built for, and what codename do we give them?
- **The ROI.** What cost does this remove? (Required. Everything else hangs off it.)
- **The first vertical.** Which segment do we point at first?
- **Deal flow.** The stages from cold to closed, and rough durations.
- **Entry motion.** Paid discovery or free qualifier, and what the realistic first yes looks like.
- **Confidence boundaries.** What is proven, what is reasoned, what is open.
- **The codebase.** So Part 2 describes a real architecture.

Unknown fields get marked and skipped. Nothing gets invented.

---

## The flow

1. **Interview.** The questions above.
2. **Fill the dossier.** Part A is ROI-first and honest about confidence. Part B is executable and unambiguous.
3. **Run Part B.** Best with a background agent that has web access, so the comparable-client list is researched and cited.
4. **Emit the deck.** Part 0 and Part 1 from Part A, Part 2 from the real codebase.
5. **Return.** Three artifacts, plus a note on what still needs your decision.

---

## Rules this skill enforces

1. **Codename the client.** Always. Scrub the fingerprints, keep the structure executable.
2. **ROI or it does not ship.** Name the cost being removed.
3. **Mark confidence.** Proven, reasoned, or open. Never blur them.
4. **Honor the contract.** Empty decision field means halt and flag, not guess.
5. **Ground the architecture.** Part 2 comes from code that exists. Generalized for confidentiality, never fabricated.
6. **Plain prose.** No puffery, no filler, no inflated verbs.

---

## Files

- `dossier-template.md`: the parameterized dual-format template the skill fills.
- `deck-spec.md`: the Part 0/1/2 deck outline and build approach.

---

## The pairing

The dossier is the human half plus the spec. If you want a clean, self-contained folder an agent can run without any of the sales framing, [**agent-pack**](https://github.com/Peleke/brunnr/tree/main/skills/agent-pack) builds exactly that.

---

## Further reading

- [brunnr](https://github.com/Peleke/brunnr): the skills marketplace
