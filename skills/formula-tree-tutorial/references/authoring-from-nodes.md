# Authoring a section from a node entry

Each capsule node entry (in `formulas/<domain>.md` or the node's detail page)
already carries everything a tutorial section needs. Map its fields to the
section parts — compress, do not transcribe.

## Field → section-part mapping

| Node-entry field | Tutorial section part | Treatment |
|---|---|---|
| title / id | heading | plain-language name ("Kinetic energy", not `kinetic_energy`) |
| statement / primary_formula | the formula, set off on its own line | verbatim; define it in words in one sentence |
| symbols (meaning, unit, dimension) | a short symbol list | keep SI units; drop the dimension vector unless the check uses it |
| assumptions / validity regime | "When it holds" — 1–2 sentences | name every assumption node; link nothing, just name them |
| prerequisites | *implicit* — the section only appears after its prereq sections | do not list them again; the order carries it |
| dimensional check | a `bash [name:chk_<id>]` block | reuse the capsule's `bc` lines; print the zero-vector |
| limiting / special case | same block or a second `try_<id>` block | print value + `(want …)` |
| derivation status / Lean check | one sentence; optionally a `bin:` Lean block | "the algebra is machine-checked (capsule `derivation-checks.lean` #N)" |
| common misuse / failure modes | "Where it breaks" — 1 sentence | the single most important failure |
| sources | a citation in parentheses at section end | `(Swift 2002 §4)` |

## Choosing which check to surface

A node may have several checks in the capsule. Pick, in order of preference:

1. A **limiting case that lands on a memorable number** (`v=0 ⇒ K=0`;
   `sin 0.1 − 0.1 ≈ −1.7e-4`; `Γ=1 ⇒ dẆ/dx = 0`). Most instructive.
2. The **dimensional check**, if the units are the point of the lesson (new
   quantity, tricky combination).
3. A **worked number** from the section's own symbols using the `setup` scenario.

Every section gets at least one runnable block. If a node genuinely has no
calculation (a pure convention or a bridge concept), fold it into the prose of
the next node that does, or give it a one-line `echo` block that states the
relationship — still runnable, still `deps:`-wired.

## "Try it yourself" blocks

After the fixed check, an optional `bash [name:try_<id>, deps:chk_<id>]` block
invites the reader to change an input:

````markdown
```bash [name:try_delta_kappa, deps:chk_delta_kappa]
# change FREQ and see the thermal penetration depth move
FREQ=${FREQ:-100}
echo "scale=6; sqrt(2 * $ALPHA_AIR / (8*a(1)/2 * $FREQ))" | bc -l
echo "  ^ delta_kappa (m) for air at ${FREQ} Hz"
```
````

Keep it parameterized off an env var with a default, so `--ci --all` runs it
unchanged and the reader can `FREQ=400 upmd ...` or edit the block.

## Compression rules

- A section is **~120–200 words of prose** plus its block(s). If it is longer,
  the capsule entry is doing too much or the section should split.
- Quote the formula once. Do not re-derive it — the capsule's derivation status
  and the runnable check are the evidence.
- Name assumptions in running text: "This is the *nonrelativistic*,
  *point-particle* form." The reader meets the assumption nodes as vocabulary.
- One failure mode per section, the one most likely to bite. The rest stay in
  the capsule.

## Citing the capsule

Every tutorial opens with a line: *"Generated from the `<capsule>` capsule
(Release X.Y) with the `formula-tree-tutorial` skill. The physics, the order,
and every calculation come from that capsule."* Then each section's source
citation is the capsule's own source for that node. The tutorial adds no
claims the capsule does not already make.
