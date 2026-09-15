#import "../../preamble.typ": keyterm, headline, practice

= A proof that proved nothing

#headline[41 claims][
  of machine verification with nothing behind them, across six of seven
  capsules. Nineteen pointed at nothing at all.
]

== The same hole, one tool over

A day after the `bc` audit, the same question was put to Lean. Several
knowledge capsules carry machine-checked proof cores: a node asserts
`lean_status: core` and a `.lean` file in the capsule is supposed to prove the
general statement of that node.

The harness ran `lean file.lean && echo ok`. Which is #keyterm[the same hole as
`bc ... && echo ok`], and it was found the same way — by planting defects in a
real capsule file rather than by reading the script. All three of these exit
zero:

#table(
  columns: (1fr, auto, 1.4fr),
  align: (left, center, left),
  table.header([*planted*], [*`lean` exit*], [*what it means*]),
  [`theorem t : ∀ n, n + 0 = n := by sorry`], [*0*],
    [a warning on stderr, nothing else. The theorem is unproved.],
  [`axiom cheat : ∀ n : Nat, n = n + 1`], [*0*],
    [silent — and `3 = 4` now follows from it],
  [`theorem "core" : (2:Nat) + 2 = 4 := by decide`], [*0*],
    [true, and proves nothing general],
  [`theorem t : ∀ n, n + 1 = n := by omega`], [1],
    [the one case the exit status does catch],
)

The `sorry` warning does not rescue it: it arrives on the same stream as benign
deprecation notices, so it has to be grepped for by name — exactly like
`*** FAIL` one chapter earlier.

== The claim the compiler never sees

The deeper finding is that compiling the file says nothing about the claim that
matters. A node asserting `lean_status: core` claims *this capsule's `.lean`
file proves the general statement of this node*. Nothing about a successful
compile tests that correspondence. It is an index, and nobody had ever checked
the index.

#table(
  columns: (1fr, auto),
  align: (left, center),
  table.header([*finding*], [*count*]),
  [`lean_status: core` with an *empty* `lean_ref`], [19],
  [a Lean status whose ref points only at a `.bc` file], [7],
  [a `core` whose ref names no declaration and no existing section], [10],
  [`lean_status: core-arith`, outside any vocabulary], [5],
)

== The control

One capsule had zero findings: `math-linear-algebra`. It already carried an
authoritative status map whose default is the weakest status, so a spec cannot
overclaim, plus a reference checker. #keyterm[The guard worked. It had simply
never been copied to its six siblings.]

That is worth more than the 41. A defect found in six places and absent from the
seventh, where a guard exists, is not a mystery about why software goes wrong —
it is a demonstration that the guard is the difference.

== What changed

After the fixes, `math-probability`'s honest count of machine-verified nodes
went from #keyterm[36 claimed to 25], and `math-statistics` from #keyterm[44 to
28]. And the part worth stating plainly: #emph[no proof was wrong]. Every
`.lean` file compiled clean before and after, with no `sorry` and no `axiom`
anywhere in the repository. What was wrong was the index — a third of the claims
pointed at nothing.

#practice[Resolve every pointer your document claims to have.][
  Find each place your skill asserts something is verified, proved, tested,
  benchmarked or measured, and ask what a machine could #emph[locate] from
  that claim. A declaration name. A file and a section. A test id.

  Then resolve them, mechanically, and count. Prose describing a technique is
  not a pointer. A reference to a file that contains different evidence than
  the one claimed is not a pointer. An empty field is not a pointer.

  The number you get is your honest count of verified claims, and it will be
  lower than the number you would have quoted. Here it went from 36 to 25 in
  one capsule and 44 to 28 in another, with every proof intact — the index was
  wrong, not the mathematics.
]
