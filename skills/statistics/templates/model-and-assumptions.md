# Model and assumptions

Every assumption is a line item with a checkable/untestable label and, where
checkable, the diagnostic used. math-statistics nodes in parentheses.

```yaml
model:
  family: ""                     # fully_parametric | exponential_family | semiparametric | distribution_free
  distribution: ""               # e.g. N(mu, sigma^2) iid | Bernoulli(p) | GLM with link g | none
  parameter: ""                  # theta and its space (parameter_space); interior? (true_parameter_interior)

  structural_assumptions:
    - name: independence
      statement: ""              # rows / clusters independent (iid_sample)
      status: checkable | untestable
      diagnostic: ""             # e.g. residual autocorrelation, design knowledge
    - name: distributional_form
      statement: ""              # normality / family membership
      status: checkable
      diagnostic: ""             # QQ plot, pearson_chi_squared_gof (watch small cells)
    - name: homoscedasticity
      statement: ""
      status: checkable
      diagnostic: ""             # residual-vs-fitted, Breusch-Pagan
    - name: functional_form
      statement: ""              # linearity / link correctness
      status: checkable
      diagnostic: ""
    - name: missingness
      statement: ""              # MCAR | MAR | MNAR
      status: untestable
      diagnostic: "argue from the collection mechanism; sensitivity analysis"
    - name: no_unmeasured_confounding
      statement: ""              # only if a causal reading is claimed
      status: untestable
      diagnostic: "identification argument; E-value / bounds"

  regularity_conditions:         # required for any likelihood-based (CRLB, MLE, Wilks, LRT) result
    support_independent_of_theta: ""     # FAILS for uniform(0, theta)
    interchange_derivative_integral: ""
    true_parameter_interior: ""          # FAILS at a boundary (variance = 0, p = 0)
    fisher_information_positive_definite: ""
    log_likelihood_smooth: ""
    identifiability: ""                   # FAILS for Neyman-Scott, label-switching

  sufficient_statistic: ""       # if one exists (neyman_fisher_factorization); inference depends on data only through it
  regime_expected: ""            # exact | asymptotic | distribution_free | bayesian
```
