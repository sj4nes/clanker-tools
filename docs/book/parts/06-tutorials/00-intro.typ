// AUTHORED. The chapters after it are generated from skills/*/tutorial/.
// States no count: the generated note lines carry those.

#import "../../preamble.typ": note, practice

= What the checks turned into

The capsules in Part IV were built to be checked by machines. A capsule is a
dependency-ordered graph of a domain's results where every node carries its
symbols, units, dimensions, assumptions and a source; what makes it more than a
formula sheet is that the graph is linearized by `tsort`, its algebra is
kernel-checked by Lean, and its arithmetic is recomputed by `bc`. None of that
is for a reader. It is there so that a claim which stops being true fails a run.

The tutorials in this part are the same material aimed at a person, and the
point worth making is that they were not written alongside the capsules. They
were cut from them. The prerequisite order a reader is walked through is the
`tsort` order. The calculation at the end of a section is the capsule's own `bc`
check, with the numbers left in. The step where a reader is asked to believe an
identity is the capsule's Lean core, and the reader runs it.

== Why this is the interesting half

A verification harness and a lesson want opposite things from the same content,
and it took building both to see that they are the same artifact under two
readings.

A harness wants a check that fails when the claim is wrong. A lesson wants a
moment where the reader predicts an answer, is wrong, and finds out immediately.
These are the same event. The dimensional check that catches a mis-stated
formula is the same line that shows a student their units do not balance; the
limiting case that proves a relation degrades correctly is the beat where the
reader sees why the assumption was there. Everything a capsule does to make
itself falsifiable turns out to be the part that teaches.

That is the return on the formal work, and it is not the return that was
expected. The capsules were built to stop a corpus of knowledge from silently
rotting. What they also produced, nearly for free, was interactive course
material in nine subjects—because a body of knowledge that can prove itself
wrong is a body of knowledge you can hand somebody and let them try.

== How to read this part

The entries are a catalog, not a reprint. The tutorials run under `upmd`, and
running them is the whole point: each is a plain Markdown file whose code blocks
execute in a real terminal, in dependency order, so the reader does the
arithmetic rather than reading someone else's. A book cannot do that, and
printing tens of thousands of words of shell blocks would be the worst of both.

So each entry gives the title, the capsule it was cut from and the method that
cut it, what it teaches, how much of it the reader runs rather than reads, and
the command. What the counts are for is the ratio: a tutorial with twenty
runnable blocks is not longer than one with three, it is more of a laboratory
and less of an essay.

They are in dependency order, and that order is derived rather than chosen. A
capsule comes before one that builds on it—which the repository states in
three different places, none of them a list of capsules in order: a `SKILL.md`
that says it builds on another, the cross-capsule `requires` edges of the atlas
capsule, and the "discharges into" column of the tutorial map. Within a capsule,
a tutorial comes after any tutorial it names as a prerequisite; where the
author numbered them, that numbering wins; and where neither settles it, the
tie is broken by how deep into the capsule's own `tsort` order the tutorial
reaches, since a lesson that ends on a later node is a later lesson.

That last rule is the one that earns its place. Two of these tutorials declare
no prerequisites and have no declared numbering, and the capsule's graph still
knows which comes first: one ends twenty-four nodes in, the other a hundred and
twenty-six. The ordering falls out of the same artifact the checks run on.

One entry names its method as the "executable-tutorial method" rather than a
skill. That one came first, and the skill was written afterwards by generalizing
what had worked—which is the order most of this corpus was built in, and the
reason Part II is a standard rather than a plan.

#practice[Cut the lesson from the harness, not beside it.][
  If you have verified material and you want to teach it, do not write a
  tutorial about it. Walk the prerequisite order the graph already gives you,
  and at each step hand the reader the check that step already has—the
  dimensional check, the limiting case, the kernel-checked identity—and let
  them run it. A lesson written beside a harness has to be kept true twice. One
  cut from the harness is true whenever the harness passes.
]
