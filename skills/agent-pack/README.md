<div align="center">

# agent-pack

**Package finished work so an agent can execute it, not just read it.**

*A folder, a README that states the contract, the documents, zipped.*

[![brunnr](https://img.shields.io/badge/brunnr-skill-4ade80)](https://github.com/Peleke/brunnr)
[![Version](https://img.shields.io/badge/v1.0.0-e88072)](https://github.com/Peleke/brunnr/tree/main/skills/agent-pack)

</div>

---

> *A PDF does not run.*

---

## What this does

You finish a piece of work and send it. The person on the other end skims it and decides. Then they hand it to their agents, and the agents have nothing to run, because what you sent was written for eyes.

So the deliverable splits in two. A person skims and judges. An agent parses and acts. They need different surfaces.

**agent-pack** builds the second one: a self-contained folder a fleet can execute without a human re-explaining it.

<div align="center">
<img src="https://raw.githubusercontent.com/Peleke/brunnr/main/skills/agent-pack/assets/flow.svg" alt="One source, two audiences: a human pack to skim and decide from, an agent pack to parse and execute" width="100%" />
</div>

---

## The standard

The shape is fixed on purpose, so whoever opens it, a person or a model, starts in the same place every time.

```
pack/
  README.md      # the contract: context, input, output, rules, goal
  <documents>    # source files, named by what they are
```

Zip it, and the whole thing travels as one attachment. The value is not the format. It is that the format does not change.

---

## The contract

The README is the entrypoint, and it does one job: it states the contract. Three things, written down instead of implied.

| Part | What it answers |
|------|-----------------|
| **Context** | What this is and why it exists. |
| **Input** | What the agent consumes to start. Usually the decisions a human already made. |
| **Output** | What the agent returns, and in what format. |

Plus the **rules** it works under: confidentiality, tone, and what it may not invent.

If a required input is missing, the receiving agent halts on that branch and flags it. It does not guess.

---

## Install

### Claude Code

```bash
# If you haven't added the brunnr marketplace yet
/plugin marketplace add Peleke/brunnr

# Install
/plugin install agent-pack@brunnr-skills
```

### CLI

```bash
# Install brunnr
uv tool install brunnr    # or: pipx install brunnr

# Install the skill
brunnr install agent-pack
```

---

## Usage

```bash
/agent-pack
```

Point it at the work and say who it is going to.

```
/agent-pack

Package the Q3 migration research for the platform team's agents.
They own the rollout; I've already picked the target regions.
```

It gathers the artifacts, writes the contract, assembles the folder, scrubs anything confidential, and zips it.

---

## Example

**Input:** a pile of research, a spec, and a decision you already made.

**Output:**

```
migration-pack/
  README.md
  architecture.md
  target-regions.md
  rollout-constraints.md
```

Where `README.md` opens like this:

```markdown
# Q3 Migration, Agent Pack

Start here. This is a self-contained pack for an agent to execute
the region-by-region rollout.

## The contract
- **Context.** We are moving 14 services off the legacy cluster.
  The region order is already decided; see target-regions.md.
- **Input (what you consume).** The region list and the freeze
  windows in rollout-constraints.md. If a freeze window is missing
  for a region, halt on that region and flag it. Do not guess.
- **Output (what you produce).** One migration plan per region,
  plus a rollback note for each.

## Rules
- Never schedule inside a freeze window.
- Mark unknowns TODO(verify) rather than filling them in.
```

That is the whole idea. The agent knows where to start, what it may assume, and when to stop and ask.

---

## Rules this skill enforces

1. **Entrypoint first.** A pack without a README is a pile of files. The README is what makes it runnable.
2. **The contract is explicit.** Context, input, and output get written down.
3. **Halt on missing input.** The receiving agent flags a gap instead of inventing one.
4. **Confidentiality by default.** Scrub before it leaves your machine. Codename real clients.
5. **Name files by what they are**, not by how they were built.
6. **Plain prose.** Both people and models read the README. Keep it direct.

---

## The pairing

An agent pack usually ships next to a human pack: a deck, a one-pager, a summary. Build both from one source. The audiences differ; the truth does not.

If you want the other half too, [**dossier-generator**](https://github.com/Peleke/brunnr/tree/main/skills/dossier-generator) builds the human-facing deck and executive summary from the same work.

---

## Files

- `README-template.md`: the entrypoint template the skill fills.

---

## Further reading

- [brunnr](https://github.com/Peleke/brunnr): the skills marketplace
