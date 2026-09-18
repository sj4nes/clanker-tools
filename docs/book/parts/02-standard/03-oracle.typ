#import "../../preamble.typ": keyterm, headline, practice, chref

// DRAFT 2026-09-16. Ledger rows: C-I-17, C-I-18, C-II-25..31.

= Choose an oracle that is not the thing you are checking <ch-oracle>

#headline[1691][
  What the code printed. The specification said 1692. A test that took its
  expected value from the code passed the bug, and failed the fix.
]

== Where did the expected value come from?

A function applies a whole-percent discount and rounds half-up to the cent. It
has a bug: it truncates. On most prices nobody can tell, because truncating and
rounding agree. At 19.90 with 15% off they do not. The exact answer is 1691.5
cents, so half-up gives 1692 and the bug gives 1691.

Now write a test the quick way. Call the function, see 1691, and assert 1691.
The test passes. It will keep passing. And when someone fixes the rounding, the
test fails, because it has been certifying the bug all along.#footnote[Subject
A in `test-writing`'s verification fixture, re-run 16 September 2026.]

Nothing is wrong with that test as a harness. It asserts; it can fail;
#chref(<ch-harness>) would pass it. What is wrong is the number on the right of
the assertion. The test asks the code what the code should say.

The source of that number is the #keyterm[oracle]: whatever tells a check what
the right answer is. The previous chapter asked whether a check can fail. This
one asks whether it can fail #emph[for the right reason], and that depends
entirely on where the oracle came from.

A caution before going further, because this book's running example is
exposed here. `test-writing` makes this its most prominent rule, and justifies
it by saying agents copy expected values out of the code by default. That
default has never been measured. It began as one programmer's hedged remark,
quoted in Luu's article, and was later repeated in this corpus as if it were
one of the article's findings. The rule may still be right. The claim that it
displaces something agents actually do is, for now, a premise.
#chref(<ch-premise>) is about what to do with one of those.

== Four places a real answer comes from

// intro: independent-oracle
The property that matters is independence. An #keyterm[independent oracle]
shares nothing with the thing it judges: not its code, not its author's reading
of the spec, not its data. `test-writing` names four places to find one.

*Re-derive it from the specification.* Work the rule, not the code. "Round
half-up" means add half a cent and truncate; do that by hand, or in a
calculator that shares nothing with the implementation. That is how 1692 was
found.

*Use a reference you are willing to believe.* A slow, obvious or already-trusted
implementation: the standard library, a brute-force version of the clever
algorithm, a published table.

*Use a relation instead of a value.* Negate the input and the output must
negate. Sort twice and nothing changes. Permute the items and the total does
not move. A #emph[metamorphic relation] needs no expected value at all, which
is why it still works where computing the answer is too expensive.

*Compare against an implementation that is genuinely separate.* A different
author, a different language, the other side of a network connection.

== Two implementations can be one oracle

The last of the four is the easiest to get wrong, because it looks like
independence and often is not.

`test-writing`'s fixture has two functions that render a number in any base.
One uses a division loop; the other recurses. Different algorithms, and a
differential test between them looks like an excellent check. Both call one
helper that turns a digit into a character, and the helper has a bug. Across
2,000 random inputs the two agree perfectly, because they are wrong
identically. A round trip through the standard library's own parser, which
shares no code with either, catches the bug at once.

Luu saw the pattern in the transcripts: asked for differential testing,
agents "would generally just write the same thing twice."#footnote[Luu, "How
well do agents use test/verification techniques?", section on differential
testing. A qualitative reading of transcripts, not a scored measure.] This
corpus found the limiting case in its own checks. Two assertions in `statistics`
compared a quantity with itself — one of them literally `(lam/n)/(lam/n)` — and
printed the expected 1 by construction.

So the question is not #emph[how many] ways you computed the answer. It is:
#emph[what does my oracle share with the thing it is judging?] Shared code is
the obvious answer. Shared assumptions, a shared misreading of the spec and
shared input data are the others. Two implementations built from the same
misunderstanding are one oracle, however different their code.

== An oracle can be out of date

Independence is not the only way an oracle fails. It can also be old.

The first real run of `role-deck` diagnosed a drift between a project's plan
and its code. It gathered its evidence carefully and recorded exactly what it
read, and one of the things it read was a status file last touched in late July,
seven weeks before the run, belonging to a process the project had abandoned. Every fact it
gathered was true. The conclusion was wrong, because the file described a world
that no longer existed. Nothing about the file looked dead.

This book met the same failure in its own sources. The corpus's one external
citation, Luu's article, was quoted in four places, each overstating what the
article supports. Nothing in the repository shows that any of them was checked
against the article: its address had never been recorded there. Each had been copied from an earlier quotation, and the earliest was
already wrong. Each quotation looked like a source. None of them was
the source, and each was a copy of something older and weaker than it looked.

// intro: source-authority
Call this the #keyterm[source-authority] problem: which sources count as
authoritative, and how to notice when a step reads one older than the thing it
describes. It is flagged here, not solved. The corpus has a proposed fix for
`role-deck` — declare the authoritative sources, and warn when a source
predates what it describes — and has not built it. For prose, the only fix this
book has used is the plain one: go back to the original, and write down the
date you read it.

== The document can be the oracle too

There is one more oracle hiding in skill work, and it is the skill itself.

Write the SKILL.md first and the checks second, and the checks get built to
confirm what the document already says. The prose has become the expected
value, and the harness is copying it, exactly as the discount test copied 1691.
Nothing independent has been consulted.

// intro: fixture-first
The corpus's answer is to work #keyterm[fixture-first]: build the failing case,
watch the default fail on it, and only then write the document that quotes the
result. `test-writing` was built that way. Its planted-bug fixture was committed
before its SKILL.md existed, if only by two minutes. The order does not make the prose right. It
means the prose had to agree with something it did not write.

#practice[Name your oracle, and list what it shares with the subject.][
  Pick one check you trust. For each assertion, write down where the expected
  value came from: the spec, a reference, a relation, another implementation —
  or the code itself.

  Look first for an oracle you already have. Most artifacts state the same thing
  twice, in places written at different times: a declared dependency list and
  prose naming what a step needs, a schema and an example. Written separately,
  they are independent. Gate one against the other, and make disagreement a
  failure.

  Then list what that oracle shares with the thing under test. Code, including
  helpers and parsers. The author, and so the author's reading of the spec.
  Input data. The date it was written. Any shared item is a way for both to be
  wrong together, and the check to stay green.

  An oracle that shares nothing is rare, and you do not need one for every
  assertion. You do need to know which of your assertions have one.

  Then check the checker against truth, not just form: delete something real
  and invent something false, and confirm each is caught. Checks that ask only
  whether a structure is well formed pass one that is well formed and wrong.
] <pr-oracle>

An oracle independent of the code can still be checking a claim about agents
that nobody has measured. That is the next chapter.
