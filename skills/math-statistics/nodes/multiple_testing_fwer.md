# multiple_testing_fwer

## Type
definition

## Statement
When m hypotheses H_{0,1}, ..., H_{0,m} are tested together, the family-wise error rate is FWER = P( at least one true null is rejected ). Controlling FWER <= alpha bounds the chance of ANY false positive across the family.

## Symbols
- `m` — the number of tests in the family
- `the family` — the set of hypotheses over which error is controlled -- a modelling choice

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
null_hypothesis, size_of_test

## Hypotheses
(none — unconditional within scope)
## Type / well-formedness check
A joint (across the family) Type I error criterion. If each of m independent true nulls is tested at level alpha, P(at least one rejection) = 1 - (1 - alpha)^m approx m alpha -- so per-test alpha must shrink.

## Specialization / boundary cases
- m = 20 independent tests at 0.05 each: FWER approx 1 - 0.95^20 = 0.64 -- a coin flip that SOMETHING is 'significant'
- FWER control is appropriate when even one false claim is costly (a drug's primary + key secondary endpoints)
- for large-scale screening (genomics) FWER is too strict and FDR is used instead

## Hypothesis-dropped counterexamples
- **the_family_is_well_defined**: if the analyst does not fix the family in advance, the 'number of tests' is ambiguous and any correction is gameable -- the multiplicity problem is really a pre-registration problem

## Common misuse
- defining the family narrowly after the fact to avoid a harsh correction
- applying FWER control to thousands of exploratory tests, killing all power
- ignoring multiplicity entirely across a paper's dozens of tests

## Related nodes (non-prerequisite)
- uses: size_of_test, null_hypothesis
- required_by: bonferroni_correction, benjamini_hochberg_fdr

## Sources
lehmann_romano_tsh, hochberg_tamhane_multiple_comparison
