---
name: test-writing
description: >-
  Write tests that can actually fail on the bug you have not thought of yet.
  Use when writing, reviewing, or strengthening tests for code — unit tests,
  integration tests, property tests, fuzz targets, regression tests for a
  reported bug, or a check added alongside a fix — and whenever a test suite
  is green but confidence is not. Six behaviours that displace the known
  default failure modes: expected values copied out of the implementation's own
  output, fixtures whose symmetry hides reversal and transposition bugs, random
  inputs that all die at the first guard, properties that are true of every
  possible answer, and checks never run against code believed correct. NOT a
  tutorial on a test framework or a runner, not a coverage-percentage target,
  and not a substitute for deciding what in the system is actually risky.
version: 1.1.0
archetype: behaviour
author: Simon Janes
tags: [testing, verification, oracles, property-testing, fuzzing, fixtures, code-review]
---

# Writing tests that can fail

You are writing a test whose job is to **fail on a bug nobody has named yet**.
A test that only confirms today's output is a regression lock, not a test, and
the two are easy to confuse because both run green.

This skill is short on purpose. It is a **nudge away from documented default
behaviour**, not a tutorial: agents given only the name of a technique fall
back to poor default testing across every condition the danluu eval measured,
and the tutorial-style skills in that eval performed *worse than no skill*.
If you want the detail, it is in
[`verification/README.md`](verification/README.md) — six planted bugs, each
with the naive test that misses it.

## The six behaviours

1. **Name the risky area first, in one line.** What in this code would be
   expensive to get wrong, and where does it touch something irreversible,
   ordered, rounded, concurrent, or parsed from outside? Test that. Not the
   getters.

2. **State the likely mistake and the alternative interpretation before you
   write the assertion.** "Half-up or truncate?" "Last-wins or first-wins?"
   "Reads forward or backward?" Each ambiguity in the spec is a test case, and
   the test you write is the one that distinguishes them. If you cannot name a
   plausible wrong answer, you do not yet know what the test is for.

3. **Get the expected value from somewhere other than the code.** **Never paste
   in what the implementation printed.** A captured expected value does not
   merely miss the bug — it certifies it, and will reject the fix. There are
   four places a real expectation comes from:

   - **re-derivation from the spec sentence** — work the rule, not the code
     ("round half-up" → add half a unit, then truncate), by hand or in a
     calculator that shares nothing with the implementation;
   - **a model-based reference oracle** — a slow, obvious, or already-trusted
     implementation you are willing to believe: the stdlib, a brute-force
     `O(n²)` version of the clever algorithm, a spreadsheet, a published table;
   - **a metamorphic relation** — related inputs with a predictable relationship
     between their outputs (negate the input and the output must negate; sort
     twice and get the identity; permute and the total must not move). This one
     needs no expected value at all, which is why it survives where the others
     are unaffordable;
   - **differential testing against a genuinely independent implementation** —
     a different author, a different language, the other side of the wire.

   Then apply the independence test: **does my oracle share code with the thing
   it is judging?** A second algorithm calling the same helper is wrong
   identically and the diff is green (fixture subject F). Calling the function
   to build its own expectation, reusing the production parser to check the
   production serializer, or diffing against a port of the same source are all
   the same mistake wearing a different hat. Two implementations are not two
   oracles; independence is the property, not the count.

4. **Break the symmetry of your fixtures, then assert that you did.** Symmetric
   matrices, palindromic buffers, identical streams, equal-length inputs and
   round numbers make reversal, transposition and off-by-one bugs
   *unobservable*. Choose asymmetric data and add a line asserting the fixture
   is asymmetric — otherwise a later edit quietly restores the symmetry and the
   test keeps passing. Check **both sides** of every boundary, and the boundary
   itself.

5. **Randomize structurally, and report the coverage number.** Uniform random
   input dies at the first guard: in the fixture, random bytes reach the branch
   under test in **0.0000%** of 20 000 inputs while a grammar-driven generator
   steered toward the interesting state reaches it in **72.3%**. So generate
   from the input's grammar, steer toward the state you suspect, and state the
   *fraction of generated inputs that reached the code you meant to test*.
   "I used a structured generator" is an adjective; the fraction is evidence.

6. **Run your new check against the code you believe is correct, too.** A check
   that fails on the bug may be failing on everything. Two runs, two
   expectations: it must fail on the defect and pass on the fix. If you have no
   fix yet, break something you know is unrelated and confirm the check stays
   green.

## Properties must discriminate

A property test earns its keep only if some wrong answer violates it.
`min <= median <= max`, `len(out) == len(in)` and "does not raise" are true of
the bug, of the fix, and of most other wrong answers. Before shipping a
property, name one plausible wrong implementation it rejects. Metamorphic
relations (negate the input and the output must negate; permute the input and
the output must not change; do it twice and get the identity) discriminate far
harder than bounds do.

## Before you call it tested

- [ ] Every expected value traces to the spec, a hand calculation, or an
      independent computation — not to a run of the code.
- [ ] Every new check has been **seen to fail**, and seen to pass on code
      believed correct.
- [ ] No fixture's symmetry can hide an index, order, or direction error; the
      asymmetry is asserted, not assumed.
- [ ] Both sides of each boundary, plus the boundary value, are present.
- [ ] Every randomized generator reports the fraction of inputs that reached
      the target branch.
- [ ] Every property names a wrong implementation it rejects.
- [ ] No oracle shares code with what it judges — not a helper, not a parser,
      not a port.

## Verification

[`verification/`](verification/) plants one bug of each documented shape and
asserts three cells per bug: the prescribed check **detects** it, the
prescribed check stays **green on the fixed code**, and the naive test
**misses** it. `sh verification/run.sh`, ~2 s.

## Related skills

- **`design-of-experiments`** — when the randomized comparison is the
  deliverable rather than the test: power, blocking, pre-registration.
- **`simulation`** — when the model-based oracle of behaviour 3 has to be a
  whole model, with its own verification and validation problem.
- **`bc`** / **`octave`** / **`lean`** — the three independent-oracle tools:
  exact decimal arithmetic, matrices at realistic dimension, and universals.
- **`docs/verifying-skills.md`** — the same discipline applied to this repo's
  own harnesses, including why `bc`'s exit status cannot signal a false claim.

## Completion report

State, briefly:

- the risky area you chose and the likely mistake you targeted;
- where each expected value came from;
- for each new check: the failure you saw it produce, and that it passes on
  code believed correct;
- for any randomized generator: the branch-coverage fraction;
- what you did **not** cover, and what would be needed to.
