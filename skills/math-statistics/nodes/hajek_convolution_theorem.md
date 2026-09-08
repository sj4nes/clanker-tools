# hajek_convolution_theorem

## Type
theorem

## Statement
In a LAN model, the limit distribution of ANY regular estimator sequence theta_hat_n (one whose local limit law does not depend on the local parameter h) can be written as a convolution N(0, I(theta_0)^{-1}) * M for some distribution M; the efficient (minimum-dispersion) regular estimator has M = delta_0 and limit exactly N(0, I(theta_0)^{-1}).

## Symbols
- `regular` — the local limit law is the same for every local parameter h (rules out Hodges superefficiency)
- `* M` — an extra independent 'noise' term -- so the efficient estimator's limit is a lower bound in the convolution order

## Epistemic status
proved_theorem  ·  regime: asymptotic

## Prerequisites (tsort edges into this node)
asymptotic_efficiency, le_cam_lan_theory

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: Hajek 1970 / Le Cam; the LAN structure + the regularity of the estimator force the convolution representation via a characteristic-function argument in the Gaussian shift experiment
derives_from: le_cam_lan_theory
lean_status: cited — CITED -- Hajek 1970; van der Vaart Ch. 8. Not formalized.

## Type / well-formedness check
The rigorous, estimator-free statement of 'you cannot beat the Fisher-information bound' -- replacing the CRLB's unbiasedness assumption with regularity. Boundary node: stated, cited. It is why 'asymptotically efficient' = 'asymptotic variance I^{-1}' is the right definition.

## Specialization / boundary cases
- the MLE (M = delta_0) is efficient; a regular but inefficient estimator has M nondegenerate, i.e. strictly more spread
- removes the Hodges superefficiency loophole: superefficient estimators are NOT regular (their local limit law depends on h)
- the semiparametric analogue bounds regular estimators of a finite-dimensional functional in a model with an infinite-dimensional nuisance

## Hypothesis-dropped counterexamples
- **regularity_of_the_estimator**: drop it and Hodges' estimator formally 'beats' I^{-1} at a point -- but only by being non-regular (badly behaved just off that point), which the theorem's hypothesis excludes
- **LAN_model**: in LAMN models the bound involves a random information and the statement changes (mixed-normal limits)

## Common misuse
- citing it to claim no estimator can have smaller asymptotic variance than I^{-1} anywhere -- superefficiency on a null set IS possible, it just cannot be regular
- applying it in non-LAN settings

## Related nodes (non-prerequisite)
- uses: le_cam_lan_theory, asymptotic_efficiency
- strengthens: cramer_rao_lower_bound

## Sources
hajek_1970, van_der_vaart_asymptotic
