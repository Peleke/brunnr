# Learning Check

**Does your agent learn? Three questions you can answer today.**

Take one agent you run and answer three questions about it.

1. **When it gets something wrong, what tells it?** Something outside the model: a failed test, a rejected suggestion, a user who didn't come back.
2. **When that happens, what changes, and by how much?** Can you write the update down?
3. **Is it better this month than last month,** on a number you can show, measured on examples it didn't train on?

If the answer to the first two is "I fix the prompt", the learning is happening in you, not in the agent.

## Why these three

Most agent "learning" features are memory: the model writes notes about its work and reads them back later. Nothing is weighted. A note confirmed a hundred times counts the same as one invented once.

The three questions are the three things memory doesn't give you: a **feedback signal**, an **update rule**, and **convergence**. The longer argument is in [Learning Is Not Memory](https://peleke.me/writing/learning-is-not-memory) (2026-03-09).

## Run it by hand

Copy this table into an issue or a doc and fill it in:

| # | Question | Verdict (yes / partial / no) | Evidence |
|---|---|---|---|
| 1 | What tells it it was wrong? | | |
| 2 | What changes when it's wrong? | | |
| 3 | Is it measurably better over time? | | |

Most agents fail question 1. Start with the first question that isn't "yes".

## Run it with an agent

Install the skill and point it at a repo:

```bash
brunnr install learning-check
```

Then ask: *"Run a learning check on this repo."* The skill is read-only: it cites a file and line for every "yes", writes "no" when it finds no evidence, and makes no model or API calls of its own.

## Next

[`signal-card`](../signal-card/): name the signal your agent should learn from.

---

*Part of the SIA (self-improving agents) series. Drafted with AI assistance, edited by me.*
