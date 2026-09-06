# Bibliography — Release 0.1

Every result node cites at least one of these. `source_key` values match
`sources/source-map.tsv`.

- **[rudin_principles_3e]** W. Rudin, *Principles of Mathematical Analysis*, 3rd
  ed., McGraw–Hill, 1976. Chapters 1–8. The spine of this release. Conventions:
  ℝ built via Dedekind cuts (ch. 1 appendix); `ℕ` from 1; compactness via open
  covers; the Riemann–Stieltjes integral specialized to `α(x) = x`.
- **[abbott_understanding_2e]** S. Abbott, *Understanding Analysis*, 2nd ed.,
  Springer, 2015. Chapters 1–8. Used for the sequence/series development, the
  nested-interval and monotone-convergence framing, and the pointwise-vs-uniform
  discussion. Conventions: `ℕ` from 1; completeness stated as the
  Axiom of Completeness (= `lub_axiom`).
- **[tao_analysis_I_4e]** T. Tao, *Analysis I*, 4th ed., Hindustan Book Agency /
  Springer, 2022. Chapters 5–11. Used for the careful construction-and-then-
  characterization of ℝ (formally via Cauchy sequences of rationals), the
  explicit treatment of the axiom of choice / countable choice, and the
  epsilon-close formalism. Conventions: `ℕ` from 0; ℝ constructed, then only its
  ordered-field + lub structure used downstream.
- **[bartle_sherbert_4e]** R. Bartle & D. Sherbert, *Introduction to Real
  Analysis*, 4th ed., Wiley, 2011. Cross-check for the differentiation and
  Riemann-integration chapters (Darboux formulation, both FTC parts,
  substitution).
- **[spivak_calculus_4e]** M. Spivak, *Calculus*, 4th ed., Publish or Perish,
  2008. Cross-check for Taylor's theorem with the Lagrange remainder and the
  interior-extremum / MVT chain.

## Notes on convention clashes

- **`ℕ` includes 0**: Tao yes; Rudin/Abbott/Bartle no. This capsule follows
  Rudin/Abbott (`ℕ` from 1) and writes `ℕ₀` where 0 is needed. When importing a
  statement from Tao, shift indices.
- **Integral**: Rudin develops Riemann–Stieltjes `∫ f dα`; this capsule uses
  only `α(x) = x`, i.e. the ordinary Riemann/Darboux integral, matching Abbott
  and Bartle.
- **Completeness primitive**: Abbott takes `lub_axiom` as an axiom (matches this
  capsule); Rudin and Tao construct ℝ and prove it. This capsule cites their
  construction and takes `lub_axiom` as the primitive, per `conventions.md`.
