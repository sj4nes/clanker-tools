# local_asymptotic_minimax

## Type
theorem

## Statement
The local asymptotic minimax (LAM / Hajek-Le Cam) theorem: in a LAN model, for any estimator sequence and any bowl-shaped loss l, liminf_n sup_{|h| <= c} E_{theta_0 + h/sqrt n}[ l( sqrt(n)(theta_hat_n - theta_0 - h/sqrt n) ) ] >= E[ l(Z) ], where Z ~ N(0, I(theta_0)^{-1}), and the bound is attained by the MLE. No estimator can beat the Fisher-information risk locally, in a minimax sense, without any regularity assumption on the estimator.

## Symbols
- `bowl-shaped loss` — l(x) = l(-x), sublevel sets convex (squared error, absolute error, 0-1)
- `the local minimax over |h| <= c` — shrinking neighbourhoods, then c -> inf

## Epistemic status
proved_theorem  ·  regime: asymptotic

## Prerequisites (tsort edges into this node)
cramer_rao_lower_bound, le_cam_lan_theory

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: reduce to the Gaussian shift limit experiment (LAN) and apply the minimax property of the Gaussian location estimator for bowl-shaped loss (Anderson's lemma)
derives_from: le_cam_lan_theory
lean_status: cited — CITED -- Hajek 1972; van der Vaart Ch. 8. Not formalized.

## Type / well-formedness check
The strongest and cleanest optimality statement in the classical theory: no regularity on the estimator at all, and it rules out ALL superefficiency (Hodges' estimator has local minimax risk that BLOWS UP as c grows). Boundary node: stated, cited.

## Specialization / boundary cases
- squared-error loss: the local minimax risk bound is tr(I(theta_0)^{-1}), matched by the MLE
- Hodges' superefficient estimator: efficient at theta_0 but its local minimax risk over |h| <= c tends to infinity as c grows -- superefficiency is paid for by terrible risk nearby
- the semiparametric LAM bound governs efficient estimation of a functional in the presence of a nonparametric nuisance

## Hypothesis-dropped counterexamples
- **bowl_shaped_loss**: for non-bowl-shaped (asymmetric) loss the bound changes and Anderson's lemma does not apply directly
- **LAN**: non-regular models have their own (different, often faster or slower) minimax rates -- see minimax_rate

## Common misuse
- reading it as a statement about a fixed theta (it is local / minimax over shrinking neighbourhoods)
- assuming attainment implies the MLE is best at every finite n

## Related nodes (non-prerequisite)
- uses: le_cam_lan_theory, cramer_rao_lower_bound
- required_by: minimax_rate

## Sources
hajek_1972, van_der_vaart_asymptotic
