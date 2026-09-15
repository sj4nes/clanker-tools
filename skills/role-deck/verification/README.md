# `role-deck` skill — verification run

`role-deck` is partly a **behaviour-modification** skill (the six behaviours
displace how a process gets followed) and partly a **tool-fact** skill (the
deck format, which an agent's prior is genuinely empty on). Per
`docs/verifying-skills.md` §7 the unit is the section, not the document, and
the table at the bottom classifies each.

What verification means here:

> **plant a defect of each documented shape in a deck or a ledger, and confirm
> the gate that claims it catches it — and that a clean deck and an honest
> ledger still pass.**

Plus the thing a static gate cannot do: **run the deck** and check that what it
actually generates matches what its author intended.

## Run

```
sh skills/role-deck/verification/run.sh
```

Tooling: Python 3 (stdlib only), macOS `/bin/sh`. ~50 s wall, of which ~18 s is
user time — the rest is process spawn across ~100 python invocations in the
mutation harnesses. Runs from any directory. Five harnesses:

| Harness | What it does |
|---|---|
| `check_deck.py` × 3 decks | 16 gates, exhaustive over every reachable state |
| `simulate.py` × 3 decks | exact marginals by DP over the state space; declared orderings asserted; the real die cross-checked |
| `mutation-check.sh` | 30 planted deck defects, each asserted caught **by the gate that claims it** |
| `condition-check.py` | two invariants over 300 die-driven runs |
| `runner-check.sh` | 8 refusals, 11 ledger-tamper cases, and a completed map-form run |

**107 assertions**, plus the premise fixture (run separately; see
`premise-fixture/RESULT.md`).

## Why decks, not a closed-form case

A methodology skill usually re-solves a problem with a known answer. Here the
object under test *is* a formal one — a deck is a bounded state machine — so
the known answer is available directly: exhaustive exploration of the reachable
state space, and exact marginals by dynamic programming rather than sampling. Monte Carlo
appears only as an **independent oracle** for the closed forms, run through the
real hash die so the comparison also tests that the die honours the declared
weights.

All three shipped decks were **hand-written naive first and were wrong.** That
is the evidence base: not a toy built to pass, but three real decks whose
defects the tooling found — `invent` v0.1.0 passed every gate and the simulator
and was wrong anyway.

## What each behaviour demonstrates

| `SKILL.md` behaviour | Prescribed check | Result |
|---|---|---|
| b1 externalise the draw | `coverage` — no path to an exit may skip a required role | `decide` v0.1.0 had a floor of **5**: `frame → criteria → steelman → attack → defer`. A decision deferred with **no evidence gathered, no alternatives considered, no probe run** — and every other gate passed it. |
| b1 the die never chooses the answer | exits are agent-chosen from earned exits | `decide` v0.2.0 committed in **14.5%** of runs; weighting `commit` to 8 reached only **26.4%**, because `defer`/`drop` go legal one card earlier. Letting the draw pick the outcome makes the deck structurally indecisive. |
| b2 instruments execute | `--command` required; output hashed into the ledger | a grounded card played without `--command` is **refused**; stripping the instrument block, editing its captured output, or forging one onto an ungrounded card all fail `verify`. |
| b3 budget through legality | look-ahead: a terminal must stay reachable | a hard wall at budget 11 leaves **7 dead ends**; the look-ahead leaves **0**, still pruning 13 branches. The only strand-free *wall* is the entire deck. |
| b4 ledger replays | recompute every draw from an empty state | **11 tamper cases caught**; 4 of them by nothing more than the draw failing to reproduce. |
| b5 typed artifacts | fields validated **exactly** | an extra field is refused as **HAT BLEED**; `exclusivity` catches the same at deck level, including a stray index field. |
| b6 check *and* simulate | exact path enumeration | `diagnose` v0.5.0 recorded the RED gut call **after** the evidence in **50%** of runs, and after the discriminating test in 6%. **Every static gate passed it.** Only the simulator saw it. |

## Negative-contrast testing

Every gate has a planted defect asserted to fire it, and the harness checks the
**specific** gate, not merely a nonzero exit. Three of the planted defects were
wrong when first written, and all three are recorded in the files, because the
failure mode is worth knowing:

| My mistake | What it looked like | What it was |
|---|---|---|
| "unplayable card" mutation required the terminal's output | `acyclic` fired, not `reachable-cards` | the defect was a **cycle**; the mutation tested nothing it claimed |
| hand-forced runner test for the conditional | passed trivially | the runner **refuses cards the die did not draw**, so most plays were silently rejected |
| look-ahead regression probe after condition branching | 8 phantom strands | it unpacked a state as a bare counts tuple when states became `(counts, flags)`, so every **terminal** looked like a dead end |

The `no-deadlock` gate deserves a note: under look-ahead legality a dead end is
structurally impossible, so **no deck defect can fire it**. It is an invariant
on the *rule*, verified by a regression probe that disables the look-ahead and
confirms the strands reappear — not by a mutation. An assertion that can never
fail is labelled as one rather than counted as coverage.

## Findings folded back

Nineteen, in [`../references/findings.md`](../references/findings.md). The three
that changed the design rather than a deck:

- **a global budget cannot be a hard wall** — it enters through legality;
- **the die must never choose the answer** — terminals became agent-chosen;
- **a preference that can strand is a bug** — `preserve_exit` yields.

No correctness fix was needed in `SKILL.md`, because the document was written
after the machinery and quotes it. That is a consequence of the order of work,
not evidence the prose is right; the displacement table is where that is tested.

## The gates are necessary, not sufficient

Everything here constrains **when** and **whether**. Nothing touches quality,
and five things stay human — they are named in `SKILL.md`'s "What a deck cannot
do", and they are the honest boundary of the whole idea.

## Displacement table

| `SKILL.md` section | Default behaviour it displaces | Where the default visibly fails |
|---|---|---|
| b1 externalise the draw | the agent picks its own next step, leaving an unauditable and unrepeatable record | `decide` v0.1.0 floor of 5 — an exit with no evidence, alternatives or probe. **Note:** the stronger claim, that an agent would SKIP the work, was fixtured and REFUTED 8/8 — see `premise-fixture/RESULT.md` |
| b1 die never picks the outcome | let the draw end the run | commit 14.5%, unfixable by weights (26.4% at weight 8) |
| b2 instruments execute | attest that you consulted something | refusal without `--command`; 3 instrument tamper cases |
| b3 budget through legality | a hard spending cap | 7 dead ends at a wall, 0 with look-ahead |
| b4 replayable ledger | trust the transcript of what happened | 11 tamper cases, 4 caught by draw replay alone |
| b5 typed artifacts | phases described in prose | extra field refused as HAT BLEED |
| b6 check and simulate first | ship the deck you wrote | hunch after the evidence in 50% of runs, invisible to every gate |
| writing a deck (`requires`, orphans, exits, conditions, options) | — | *tool-fact*: the format is payload the agent's prior is empty on; each rule maps to a gate in `references/deck-format.md` |
| field presence ≠ field quality | assume a satisfied gate means good work | `judgement` |
| a command is not the right command | assume grounding implies relevance | `judgement` |
| a condition is only as honest as its declaration | assume a null field is null truthfully | `judgement` |
| tamper-evident, not tamper-proof | assume verification is adversarial security | `judgement` |
| guardrails (floor too big; relax a gate; steps undefendable) | run the process because it exists | `judgement` |

**7 covered · 5 judgement · 1 tool-fact · 4 gaps** (one closed by the premise
fixture — which refuted the claim it was testing).

### Gaps — logged in [`BACKLOG.md`](../../../BACKLOG.md)

1. ~~**The founding premise is unfixtured.**~~ **CLOSED 2026-09-15 — and the
   premise was REFUTED.** 8 fresh agents, given a bug whose cause is visible
   only by running the code, all ran it unprompted. The claim was struck from
   `SKILL.md` rather than reworded. See `premise-fixture/RESULT.md`. The
   successor question — whether agents skip the *ordering* discipline, which
   none of the 8 exhibited — is a hypothesis, not a finding, and needs its own
   fixture.
2. **The reroll log is claimed as a behavioural signal** and never exercised —
   no fixture drives an agent that systematically rerolls away from a hat and
   confirms the log makes it visible.
3. **`terminal-live` and `options-sweep` have no isolating mutation.** Both
   fire only alongside other gates, so neither has been seen to fail alone.
4. **The `die` gate has never fired on a real bias.** The cross-check confirms
   the hash die tracks the declared weights; nothing plants a biased die and
   confirms detection.
5. **`decide`'s `expected_order` has no regression mutation.** `diagnose`'s
   does — that is how the hunch bug stays fixed — but decide's six declared
   orderings are asserted only on the current deck.
