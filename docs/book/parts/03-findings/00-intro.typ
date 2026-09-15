#import "../../preamble.typ": keyterm

Between 13 and 15 September 2026, four audits were run against this corpus.
Each asked the same question of a different verification technology, and each
got the same answer.

The question is: #keyterm[does this check have any way of failing?]

It is not the question a passing build answers. A green run tells you the
harness ran and did not object. It does not tell you the harness was capable of
objecting — and the four audits below found, in four unrelated tools, that
mostly it was not. Arbitrary-precision arithmetic, a proof assistant, a
topological sort, and a methodology's own justification: each had a check whose
success carried no information.

None of these were discovered by a failing build. A failing build was, in every
case, the thing that could not happen. They were discovered by deliberately
breaking something and noticing that nothing complained.

What follows is what each audit found, in the order they were run, and then the
one structural property they share.
