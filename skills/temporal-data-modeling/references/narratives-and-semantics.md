# Narratives and semantics

A practitioner's translation of the *theory of narratives* (Leal, Bumpus,
Nickel, García, Fairbanks, Dixon, *Time-Varying Data as Sheaves: an Invitation
to Narratives*, arXiv:2609.09056, 2026), which itself builds on Bumpus–Leal–
Fairbanks–Karvonen–Simard, *Towards a unified theory of time-varying data*
(2026). You do not need the category theory to use this skill; this file records
what the abstractions buy you.

## 1. Time as a lattice of intervals, not a set of timestamps

The naive model of time is a totally ordered set of instants. The narrative
model uses a **category of intervals**: the objects are closed intervals
`[a,b]`, and there is a morphism `[a,b] → [c,d]` exactly when `[a,b] ⊆ [c,d]`.

Why this matters in practice: it makes **"the data on a sub-window"** and
**"how two windows overlap"** first-class. A snapshot model has instants and
nothing between them; the interval model has, for `[0,2]`:

```
            [0,2]
           /     \
       [0,1]     [1,2]
       /   \     /   \
   [0,0]  [1,1] [1,1] [2,2]
```

Every interval, and every containment between intervals, is a place data can
live and a constraint data must satisfy.

**Covers.** An interval `[a,b]` is *covered* by splitting it at an interior
point: `([a,p], [p,b])`. The modelling claim is that data on `[a,b]` should be
reconstructible from data on the two halves plus how they meet at `p`. This is
the **gluing** condition, and it is the single most useful lint in the whole
framework.

**Branching time.** Replace the line by a tree and everything still works:
a Git history, a scenario forest, "the garden of forking paths". Intervals then
live on the tree; covers split along it; cross-branch joins are `merge`
transitions.

**Changing resolution.** A partition `a = r0 ≤ r1 ≤ … ≤ rn = b` induces a
coarser interval category. Restricting a narrative along it is exactly
"downsample to these snapshots" — done functorially, so properties transported
this way stay consistent.

## 2. Persistent = sheaf, cumulative = cosheaf

A **narrative** assigns data to every interval and restriction maps to every
containment. Two dual flavours:

### Persistent (sheaf)

`F([a,b])` is information that **holds throughout** `[a,b]`. Containment
`[a,b] ⊆ [c,d]` gives a **restriction** `F([c,d]) → F([a,b])` (what still holds
on the smaller window). The sheaf condition:

```
F([a,b])  ≅  F([a,p])  ×_{F([p,p])}  F([p,b])
```

read as: **the data valid over the whole interval is exactly what the two halves
agree on at the shared instant** `p`. Reconstruction is by **pullback /
intersection / agreement**.

Persistent fields in the wild: a balance as of a date; a configuration in force;
a membership currently active; the current value of a sensor; a price on a date.

### Cumulative (cosheaf)

`F̂([a,b])` is information that **accumulates over** `[a,b]`. Containment gives an
**extension** `F̂([a,b]) → F̂([c,d])` (what the smaller window contributes to the
larger). The cosheaf condition:

```
F̂([a,b])  ≅  F̂([a,p])  +_{F̂([p,p])}  F̂([p,b])
```

read as: **the data accumulated over the whole interval is exactly the two
halves combined, glued along what they share at** `p` (so the overlap instant is
counted once). Reconstruction is by **pushout / union / aggregation**.

Cumulative fields in the wild: transactions in a period; distinct users seen in
a quarter; total downtime over a window; every file touched during a build; a
running count.

### The attribute case

A narrative valued in the *cotwisted arrow category* carries **both** a
persistent component `P`, a cumulative component `C`, and a comparison
`γ: P → C` — even within a single instant. Read `γ` as an attribute map: `P` is
the set of objects (vertices, members, accounts), `C` is the space of attributes
(labels, roles, weights, communities), and `γ` assigns attributes to objects.
Restrictions on the `P` side track how objects change; restrictions on the `C`
side track how attributes evolve. This is the right model when you need to
follow both entities and their labels through time and keep them coherent.

## 3. Conversion: the `K ⊣ P` adjunction

There are canonical functors both ways:

- **`K` : persistent → cumulative.** `(K F)([a,b])` = colimit (union / pushout)
  of the persistent values over all sub-intervals of `[a,b]`. "Accumulate what
  held."
- **`P` : cumulative → persistent.** `(P F̂)([a,b])` = limit (intersection /
  pullback) of the cumulative values over the sub-intervals. "Extract what is
  common."

`K` is left adjoint to `P` (`K ⊣ P`). They do **not** form an equivalence —
converting one way and back does not return the original. The comparison maps:

- **unit** `η_F : F → P K F` — compares the prescribed persistent data with the
  persistent narrative you get by accumulating then re-restricting.
- **counit** `ε_F̂ : K P F̂ → F̂` — compares the cumulative data reconstructed from
  its common part with the original cumulative data.

When `η` (resp. `ε`) is an isomorphism, that direction is lossless.

### Worked loss example (from the paper, Figure 1)

Time category `[0,0] → [0,1] ← [1,1]`. Persistent narrative `F`:
`F([0,0]) = {a}`, `F([1,1]) = {b}`, `F([0,1]) = {0,1}`, both restriction maps
`{0,1} → {a}` and `{0,1} → {b}` sending everything to the single point.

- `K F([0,1])` = pushout `{a} +_{ {0,1} } {b}` = a single point `{∗}`.
- `P K F([0,1])` = pullback `{a} ×_{ {∗} } {b}` = `{(a,b)}`, one element.
- Original was `{0,1}`, two elements. `{(a,b)} ≇ {0,1}` — the unit is **not** an
  isomorphism. Accumulating collapsed the two states; re-restricting cannot
  recover them.

Meanwhile the cumulative side *is* recovered here: `K P` of the cumulative
component returns `{∗}`. So this narrative is **right-rigid but not left-rigid** —
the asymmetry is real and direction matters.

## 4. Rigidity classification

For a field (equivalently, a narrative), classify the round trips:

| Class | `F → P K F` | `K P F̂ → F̂` | Store |
|---|---|---|---|
| **rigid** | iso | iso | either view; convert freely |
| **left-rigid** | iso | — | cumulatively; derive persistent |
| **right-rigid** | — | iso | persistently; derive cumulative |
| **loose** | — | — | both, or one + a documented loss |

### Sufficient condition for left-rigidity

If the ambient category is **adhesive** (pushouts along monos are stable under
pullback — true for sets, graphs, and most "structured collection" data) and the
persistent restriction maps over the interval are **monomorphisms** (inclusions —
the membership only grows, or only shrinks, and never swaps members), then the
pushout square is also a pullback, so `F ≅ P K F` and the field is **left-rigid**.

Practical reading:

- A set that **only accretes** over the interval ("all users onboarded so far"),
  or **only shrinks** ("still-eligible accounts") → left-rigid. The
  accumulate-then-restrict round trip is exact.
- A set that **both gains and loses** members over the interval (real
  membership with churn) → typically **loose**. You must store both the as-of
  series and the ever-member set, or accept that one is unrecoverable from the
  other.

This is the single check that tells you whether "we can just compute the monthly
number from the daily table" is safe.

## 5. What to take away

1. Model time as intervals with containment, so overlaps and sub-windows are
   first-class.
2. Every field is persistent (agree / intersect / pullback) or cumulative
   (aggregate / union / pushout). They carry different information.
3. Conversion between the two is lossy in general; classify the round trip
   before you rely on deriving one from the other.
4. The gluing condition — halves must agree (persistent) or combine without
   double-count (cumulative) — is your lint.
