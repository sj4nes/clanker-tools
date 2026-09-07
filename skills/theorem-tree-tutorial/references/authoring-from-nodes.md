# Authoring a section from a theorem-tree node

Each capsule node has a `results/<id>.yaml` entry and a `nodes/<id>.md` detail
page carrying everything a tutorial section needs. Map the fields to section
parts — compress, do not transcribe.

## Field → section-part mapping

| `results/<id>.yaml` field | Tutorial section part | Treatment |
|---|---|---|
| `node` / `nodes.tsv` title | heading | plain-language name ("Least upper bound", not `supremum`) |
| `display` | the statement, set off on its own line | quote once; restate in words in one sentence |
| `parseable` | — | ignore; it is for machine indexing |
| `symbols` (meaning, type) | a short typed-symbol list | keep the types (`X : set`, `f : X → Y`, `x_n : ℕ → ℝ`); this replaces the physics "SI units" line |
| `type_check_status` / `type_check_note` | "Why the statement is well-formed" — 1 sentence, or fold into the check | the note often names the real subtlety (a quantifier order, a well-definedness obligation) — surface that |
| `hypotheses` | "What it assumes" — name each as the node it is | do not link, just name: "bounded, monotone — both first-class nodes below/above" |
| `dependencies` | *implicit* — the section only appears after its prerequisites' sections | the order carries it; do not re-list |
| `status_label` (+ `proof.lean_status`) | one sentence on epistemic status | "`proved_theorem`, kernel core" / "`proved_theorem`, `lean_status: cited` — established in <source>, not re-checked here" / "`nonconstructive_result` — the object is not computed" |
| `choice_grade` / `constructive_grade` / `convergence_mode` | **the grade beat** — 1–2 sentences | *which* assumption it rests on and what weaker thing is not enough (see below) |
| `specialization_cases` | a `chk_<id>` block, or a second `try_<id>` | pick the one landing on a memorable value; print `(want …)` |
| `counterexamples_when_dropped` | a `cx_<id>` block | **always**, for a theorem — see below |
| `proof.technique` / `proof.derives_from` | one sentence — "the proof is just <prior result> wearing a hat" | the runnable Lean core or `bc` instance is the evidence, not a re-derivation |
| `common_misuse` | "Where it breaks" — 1 sentence | the single failure most likely to bite |
| `sources` | a citation in parentheses at section end | `(Billingsley §2)` |

## The counterexample beat (`cx_<id>`)

The distinctive move of a math tutorial. For every **theorem / lemma /
proposition** section:

1. `chk_<id>` shows the conclusion holding on the capsule's own worked object.
2. `cx_<id>` takes the YAML's `counterexamples_when_dropped` entry, keeps every
   hypothesis but the named one, and **runs the object to show the conclusion
   fail** — an empty intersection, a mean that diverges, a sequence with no
   limit, a set with no least upper bound.

Reuse the capsule's counterexample verbatim; most are concrete (`X = ℚ` instead
of `ℝ`; `X ~ Cauchy`; the standard-basis sequence in `ℓ²`). If the YAML says
`none_all_hypotheses_essential` or the statement is unconditional, there is no
`cx_` block — say so in the prose ("the theorem is unconditional; there is no
small case that escapes it").

Example shape (from `hole-in-the-rationals`, `monotone_convergence_theorem`):

````markdown
```bash [name:cx_monotone_convergence_theorem, deps:chk_monotone_convergence_theorem]
# drop completeness: read the SAME bounded monotone sequence inside Q
x=$SEED
for n in 1 2 3 4 5 6; do x=$(echo "scale=40; ($x + 2/$x)/2" | bc -l); done
echo "the sequence is rational, decreasing, bounded below -- every hypothesis holds"
echo "its only candidate limit is sqrt(2) = $(echo 'scale=40; sqrt(2)' | bc -l)"
echo "sqrt(2) is not rational => inside Q this sequence has NO limit."
echo "=> drop completeness and the theorem is false."
```
````

## Surfacing the grade

Each math capsule tags every result with one grade. Do not drop it — it is the
capsule's reason for existing.

| Capsule | Tag | Teaching beat |
|---|---|---|
| `math-sets-functions-cardinality` | `choice_grade` | "This needs the **full** Axiom of Choice (`needs_full_AC`) — Zorn's lemma is doing the work. `choice_free` results like Cantor's theorem do not." |
| `math-logic-and-proof` | `constructive_grade` | "This step uses the **law of excluded middle** (`needs_LEM`) — it is not intuitionistically valid. `¬∃` from `∀¬` *is*." |
| `math-probability` | `convergence_mode` | "The CLT delivers convergence **in distribution** — not almost sure, not in probability. The reader who wants `X̄_n → μ` for a fixed run needs the SLLN instead." |
| `math-real-analysis` | `status_label` (`nonconstructive_result`) | "The limit exists but is **not computed** — `lub_axiom` hands you a supremum without a formula for it." |
| `math-number-systems` | (per-node, e.g. well-definedness) | "The construction is on equivalence classes; the runnable check is that the operation **does not depend on the representative**." |

One sentence, in the section prose or as the last line of the `chk_` block's
output. Where a whole tutorial sits at one grade (every step `choice_free`), say
it once in the capstone.

## Choosing which check to surface

A node may carry several checks. Prefer, in order:

1. A **hypothesis-dropped counterexample** that lands somewhere vivid — this is
   the `cx_` block and it is almost always the most instructive thing in the
   section.
2. A **specialization that lands on a memorable number** (`X = ∅ ⇒ |X| = 0 < 1`;
   `Bernoulli(½) ⇒ Var = ¼`; `n = 1 ⇒ Binomial = Bernoulli`).
3. A **Lean core** where `lean_status: core` — run it, and say genuine-vs-instance.
4. A **`bc` instance** — a definition made concrete, an identity at sample
   values, a bisection or brute search demonstrating the statement.

Every section gets at least one runnable block. A pure `notation_convention` or
`bridge` node with no calculation folds into the prose of the next node that has
one, or gets a one-line `echo` block stating the relationship — still runnable,
still `deps:`-wired.

## "Try it yourself" blocks

After the fixed checks, an optional `bash [name:try_<id>, deps:chk_<id>]` invites
the reader to change an input — a different sequence, a different distribution
parameter, a wider interval — parameterised off an env var with a default so
`--ci --all` runs it unchanged:

````markdown
```bash [name:try_markov_inequality, deps:chk_markov_inequality]
A=${A:-3}          # threshold; try A=10
echo "P(X >= $A) <= E[X]/$A for X ~ Exponential(1), E[X] = 1:"
echo "scale=6; bound = 1/$A; actual = e(-$A); bound; actual" | bc -l
echo "  ^ Markov bound, then the true tail -- Markov is loose, always valid"
```
````

## Compression rules

- A section is **~120–220 words of prose** plus its block(s). Longer means the
  YAML entry is doing too much or the section should split.
- Quote the statement once. Do not re-prove it — `proof.technique` in one
  sentence plus the runnable check is the evidence.
- Name hypotheses in running text as the nodes they are: "This needs
  *countable* additivity, not just finite — a first-class node." The reader
  meets the hypothesis nodes as vocabulary.
- One `common_misuse` per section, the one most likely to bite.

## Citing the capsule

Every tutorial opens with:
*"Generated from the `<capsule>` capsule (Release X.Y) with the
`theorem-tree-tutorial` skill. The mathematics, the prerequisite order, and
every calculation and proof come from that capsule — `validation/proof-checks.lean`
and `validation/instance-checks.bc` in particular."*
Each section's citation is the capsule's own `sources` for that node. The
tutorial adds no claim the capsule does not already make, and never upgrades a
`cited` result's status.
