# Cycles found and how they were resolved

## Release 0.1

`tsort edges/dependencies.edges` produced a total order with **no cycle**
(BSD-safe check: `tsort` stderr empty, all 394 edges respected). No cycle
resolution was needed.

Cycles that were **avoided by modeling choice** (recorded here so a later
release does not reintroduce them):

- **sufficiency ↔ factorization.** `sufficiency` is defined intrinsically (the
  conditional law of the data given `T` does not depend on `theta`);
  `neyman_fisher_factorization` is the *theorem* that this holds iff the density
  factors. Edge runs `sufficiency -> neyman_fisher_factorization` only. The
  reverse ("people check sufficiency by factoring") is a `proof_route`, not a
  prerequisite.
- **estimator ↔ decision_rule.** An estimator *is* a decision rule and a test
  *is* a decision rule, but `decision_rule` is the abstract node and `estimator`
  / `test_function` are the concrete ones. Edges run `estimator -> decision_rule`
  and `test_function -> decision_rule` (the abstract node is stated *after* the
  concrete instances that motivate it — a valid `tsort` choice, not proof order).
- **MLE ↔ score equation.** `maximum_likelihood_estimator` is defined as an
  argmax; `mle_score_equation` is the first-order *consequence* at an interior
  optimum. Edge runs `maximum_likelihood_estimator -> mle_score_equation`. Do
  not define the MLE as "a root of the score" — that loses non-interior and
  non-differentiable cases.
- **Cramer-Rao ↔ efficiency.** `asymptotic_efficiency` is defined as "asymptotic
  variance equals `I(theta)^{-1}`", which references `cramer_rao_lower_bound`.
  Edge runs `cramer_rao_lower_bound -> asymptotic_efficiency`. The CRLB does not
  depend on the notion of efficiency.
- **confidence set ↔ test.** `confidence_set_test_duality` makes the
  correspondence a *theorem*; both `confidence_set` and `test_function` are
  defined independently first (a confidence set by its coverage property, a test
  by its rejection region), so the duality node depends on both and neither
  depends on it.
