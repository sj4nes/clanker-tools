# role-deck — checker first, findings from building it

Not a skill yet: no `SKILL.md`, deliberately outside `skills/` so
`tools/check-skills.sh` does not see it.

    sh experiments/role-deck/run.sh     # ~1s

## What exists

| File | What it is |
|---|---|
| `decks/diagnose.json` | the rulebook: artifact types with fields, cards (role, copies, requires, produces, instrument), required roles |
| `check_deck.py` | ten static gates over the deck, by exhaustive state-space exploration |
| `budget.py` | the budget model, and why it enters through legality rather than as a wall |
| `mutation-check.sh` | plants one defect per gate and asserts each is caught |
| `run_deck.py` | the runner: external draw, artifact validation, append-only ledger, replay-based `verify` |
| `runner-check.sh` | six refusals and seven ledger-tamper cases, all asserted caught |

A deck is a bounded state machine: state is the multiset of cards played, a
card is legal when a copy remains and its required artifacts are present, play
ends at a terminal card. Legality depends on the *set* of artifacts present,
not the order they arrived — which collapses the state space to reachable
subsets of the deck and makes exhaustive checking trivial at any size a human
would author (87 states here).

## The three findings

**1. RED and YELLOW were decorative.** The hand-written v0.1.0 deck passed
every structural gate and failed `no-orphans`: nothing consumed the hunch or
the support. They were in the deck because de Bono prescribes them, not
because the process needed them. Both now have principled consumers rather
than gate-appeasing ones — `falsify` (BLACK) requires `support`, so you cannot
design a *discriminating* test before saying what each hypothesis predicts
(which is also de Bono's yellow-before-black, now enforced rather than
advised); and `close` requires `hunch`, so the verdict must say whether the
opening gut call was borne out, which is the only thing that stops it steering
silently. Tightening those two edges cut the reachable state space **183 → 87**:
fewer ways to wander.

**2. A global budget cannot be a hard wall.** `no-deadlock` and `terminal-live`
were near-vacuous in v0.2.0: artifacts only accumulate, so once a terminal was
reachable it stayed reachable. Adding a budget was meant to fix that. The naive
version — *a move is legal while `spent + cost <= budget`* — does not work. The
agent spends early on optional cards and then cannot afford the mandatory tail,
and the only strand-free wall is the entire deck:

| wall budget | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|
| dead ends | 9 | 12 | 14 | 11 | 5 | 1 | **0** |

A budget that only stops binding when it stops constraining is not a budget.
This matters more here than in a game a human plays, because **the draw is
external**: a human who strands themselves made a mistake, but an agent handed
a stranding move by a die was given an illegal position by the rulebook.

So the budget enters through **legality** instead: *a move is legal only if,
after playing it, a terminal is still reachable within the remaining budget.*
You cannot bankrupt yourself. The budget still binds — it prunes the branches
that would waste the tail — but no reachable state is ever a dead end:

| | states | complete runs | dead ends |
|---|---|---|---|
| hard wall at 11 | 74 | — | **7** |
| look-ahead at 11 | 61 | 8 | **0** |

**3. The deck's floor is 9 cards.** Eight cards — `open`, `gather`,
`hunch`, `hypothesize`, `support`, `falsify`, `run`, `close` — but `run` costs
2, because EXECUTE is the hat that spends real resources. The deck runs at
budget **11** against a total deck cost of 14, so there is slack for two extra
plays and **8 distinct complete runs**. This is the number to argue with when
asking whether the process is worth its overhead: not a feeling, a floor.

**4. `no-deadlock` is now an invariant, not a gate.** Look-ahead legality makes
a dead end structurally impossible, so no *deck* defect can fire it — the
mutation that was written for it correctly fires `budget-feasible` instead,
which rejects an unreachable terminal before the state space is even built.
`no-deadlock` is therefore an assertion about the **rule**, and it is verified
by a regression probe that disables the look-ahead and confirms 7 strands
reappear. An assertion that can never fail is worth labelling as one.

## Gates

| Gate | Catches |
|---|---|
| `schema` | undeclared artifact types |
| `exclusivity` | **hat bleed** — a card's artifact carrying a field owned by another artifact type (GREEN shipping a `ranking` means BLACK already ran, silently) |
| `acyclic` | precedence cycles |
| `reachable-cards` | a card that can never legally be played |
| `budget-feasible` | a budget below the deck's floor, or no reachable terminal at all |
| `budget-binding` | a budget at or above the whole deck's cost — decorative |
| `no-deadlock` | a reachable non-terminal state with no legal move (*invariant — see finding 4*) |
| `terminal-live` | a reachable state from which no terminal is reachable |
| `coverage` | **a path to a terminal that omits a required role** — the structural form of "the agent must not be able to finish without wearing the caution hat" |
| `no-orphans` | an artifact nothing consumes: a decorative hat |

`coverage` is the one that carries the argument from the design conversation.
It makes "the agent routed around Black" impossible by construction rather
than detectable after the fact.

## The runner

    python3 run_deck.py init   --deck decks/diagnose.json --seed 4271 --ledger run.json
    python3 run_deck.py next   --ledger run.json     # what the die drew, and what to fill
    python3 run_deck.py play   --ledger run.json --artifact-file a.json
    python3 run_deck.py reroll --ledger run.json --reason "..."
    python3 run_deck.py verify --ledger run.json     # replay and re-check everything

The agent never chooses its next hat. The runner computes the legal moves, the
draw picks one, and the agent's only job is to produce that card's artifact.

**Three properties make the ledger worth trusting.** The draw is a pure
function of `(seed, step, rerolls-at-that-step)` — nothing random is stored, so
`verify` recomputes every draw from an empty state and a hand-edited ledger does
not survive replay. Artifacts are validated against the card's declared fields
*exactly*: a missing field is an unfinished hat, an extra field is **runtime hat
bleed** — an agent still wearing the last hat or reaching into the next one.
And `spent` is derived from the play history rather than stored, so there is no
mutable counter to corrupt.

That second property is the answer to "some models ignore instructions". The
static `exclusivity` gate checks the *deck* declares its fields cleanly; the
runtime check catches an *agent* that fills in a field belonging to another
hat. Neither depends on the model complying.

`runner-check.sh` asserts six refusals (missing field, hat bleed, empty field,
playing a card the die did not draw, malformed JSON, a reroll past the
allowance) and seven tamper cases (a play deleted from the middle, a field
emptied after the fact, another hat's field spliced in, the recorded draw
rewritten, a play forged and appended, the reroll count inflated, rerolls
beyond the allowance). All thirteen are caught. Four of the seven tamper cases
are caught by the draw failing to reproduce, which is the property doing the
work.

**Finding 5: the reroll log is the behavioural signal.** A reroll is priced and
recorded with the card it was spent avoiding. "The agent rerolled away from
BLACK four times out of five" is then a measurement rather than a suspicion —
the process analogue of `experience-library`'s contribution log.

## Known limitations

- **Monotone artifacts.** Cards are consumed; artifacts are not. The budget now
  supplies the exhaustible resource that makes the state space interesting, but
  no card ever *invalidates* an earlier artifact — a diagnosis cannot go stale.
- **One producer per artifact type** — now checked (`schema`), after the
  mutation harness found that two producers would silently collapse the
  precedence map.
- **Tamper-evident, not tamper-proof.** `verify` catches drift, hand-editing,
  and a bypassed runner. It does not stop an adversary who runs the same draw
  algorithm and forges a self-consistent ledger. The threat model is a model
  that wanders, not one that attacks.
- **Field presence is not field quality.** The runner checks that every
  declared field is present and non-empty. Nothing checks that `discriminator`
  actually discriminates — that stays human, or needs the instrument.
- **`instrument` is declared but unenforced.** Cards name an instrument
  (`retrieval`, `execution`); nothing requires that the phase actually invoked
  one. Grounding condition 3 from the design conversation is still advisory.
- **No simulator.** The gates say what is *possible*; they say nothing about
  the *distribution* of sequences a random draw actually produces. That is the
  thing designers are reliably wrong about.

