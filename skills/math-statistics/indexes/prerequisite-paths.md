# Minimal prerequisite paths for headline results (generated)

Each list is the transitive prerequisite set of the node, printed in
`tsort` order. It is the set the graph forces to precede the node, not a
shortest teaching path. Derived from graph structure, not the flat order.

## likelihood_function
_(7 prerequisites)_

- prob_probability_space
- prob_pdf
- prob_joint_distribution
- prob_iid
- statistical_model
- iid_sample
- dominated_family

## score_function
_(10 prerequisites)_

- ra_differentiability
- prob_probability_space
- prob_pdf
- prob_joint_distribution
- prob_iid
- statistical_model
- iid_sample
- dominated_family
- likelihood_function
- log_likelihood

## fisher_information
_(12 prerequisites)_

- ra_differentiability
- prob_variance
- prob_probability_space
- prob_pdf
- prob_joint_distribution
- prob_iid
- statistical_model
- iid_sample
- dominated_family
- likelihood_function
- log_likelihood
- score_function

## score_identity
_(15 prerequisites)_

- ra_interchange_limit_integral
- ra_differentiability
- prob_probability_space
- prob_pdf
- prob_joint_distribution
- prob_iid
- prob_expectation
- statistical_model
- iid_sample
- dominated_family
- support_independent_of_theta
- likelihood_function
- interchange_derivative_integral
- log_likelihood
- score_function

## information_equality
_(19 prerequisites)_

- ra_interchange_limit_integral
- ra_differentiability
- prob_variance
- prob_probability_space
- prob_pdf
- prob_joint_distribution
- prob_iid
- prob_expectation
- statistical_model
- iid_sample
- dominated_family
- support_independent_of_theta
- likelihood_function
- interchange_derivative_integral
- log_likelihood
- score_function
- log_likelihood_smooth
- score_identity
- fisher_information

## exponential_family
_(10 prerequisites)_

- prob_random_variable
- prob_probability_space
- prob_pdf
- prob_iid
- prob_exponential
- prob_expectation
- statistical_model
- iid_sample
- dominated_family
- statistic

## sufficiency
_(7 prerequisites)_

- prob_random_variable
- prob_probability_space
- prob_iid
- prob_conditional_distribution
- statistical_model
- iid_sample
- statistic

## neyman_fisher_factorization
_(13 prerequisites)_

- prob_random_variable
- prob_probability_space
- prob_pmf
- prob_pdf
- prob_joint_distribution
- prob_iid
- prob_conditional_distribution
- statistical_model
- iid_sample
- dominated_family
- statistic
- likelihood_function
- sufficiency

## completeness_statistic
_(7 prerequisites)_

- prob_random_variable
- prob_probability_space
- prob_iid
- prob_expectation
- statistical_model
- iid_sample
- statistic

## estimator
_(8 prerequisites)_

- prob_random_variable
- prob_probability_space
- prob_iid
- statistical_model
- parametric_model
- parameter_space
- iid_sample
- statistic

## mse_bias_variance_decomposition
_(14 prerequisites)_

- prob_variance
- prob_random_variable
- prob_probability_space
- prob_iid
- prob_expectation_linearity
- prob_expectation
- statistical_model
- parametric_model
- parameter_space
- iid_sample
- statistic
- estimator
- bias
- mean_squared_error

## consistency
_(11 prerequisites)_

- prob_random_variable
- prob_probability_space
- prob_iid
- prob_conv_p
- prob_chebyshev_ineq
- statistical_model
- parametric_model
- parameter_space
- iid_sample
- statistic
- estimator

## umvue
_(13 prerequisites)_

- prob_variance
- prob_random_variable
- prob_probability_space
- prob_iid
- prob_expectation
- statistical_model
- parametric_model
- parameter_space
- iid_sample
- statistic
- estimator
- bias
- unbiased_estimator

## cramer_rao_lower_bound
_(27 prerequisites)_

- ra_interchange_limit_integral
- ra_differentiability
- prob_variance
- prob_random_variable
- prob_probability_space
- prob_pdf
- prob_joint_distribution
- prob_iid
- prob_expectation
- prob_covariance
- prob_cauchy_schwarz
- statistical_model
- parametric_model
- parameter_space
- iid_sample
- dominated_family
- statistic
- estimator
- support_independent_of_theta
- likelihood_function
- interchange_derivative_integral
- bias
- log_likelihood
- unbiased_estimator
- score_function
- score_identity
- fisher_information

## rao_blackwell_theorem
_(17 prerequisites)_

- prob_random_variable
- prob_probability_space
- prob_law_total_variance
- prob_jensen_ineq
- prob_iid
- prob_expectation
- prob_conditional_expectation
- prob_conditional_distribution
- statistical_model
- parametric_model
- parameter_space
- iid_sample
- statistic
- estimator
- bias
- sufficiency
- unbiased_estimator

## lehmann_scheffe_theorem
_(21 prerequisites)_

- prob_variance
- prob_random_variable
- prob_probability_space
- prob_law_total_variance
- prob_jensen_ineq
- prob_iid
- prob_expectation
- prob_conditional_expectation
- prob_conditional_distribution
- statistical_model
- parametric_model
- parameter_space
- iid_sample
- statistic
- estimator
- completeness_statistic
- bias
- sufficiency
- unbiased_estimator
- umvue
- rao_blackwell_theorem

## maximum_likelihood_estimator
_(10 prerequisites)_

- ra_continuity
- ra_compactness
- prob_probability_space
- prob_pdf
- prob_joint_distribution
- prob_iid
- statistical_model
- iid_sample
- dominated_family
- likelihood_function

## mle_consistency
_(16 prerequisites)_

- ra_continuity
- ra_compactness
- prob_wlln
- prob_slln
- prob_probability_space
- prob_pdf
- prob_joint_distribution
- prob_iid
- prob_conv_as
- statistical_model
- parametric_model
- iid_sample
- identifiability
- dominated_family
- likelihood_function
- maximum_likelihood_estimator

## mle_asymptotic_normality
_(40 prerequisites)_

- ra_taylor_theorem
- ra_mean_value_theorem
- ra_interchange_limit_integral
- ra_differentiability
- ra_continuity
- ra_compactness
- prob_wlln
- prob_variance
- prob_slutsky
- prob_slln
- prob_probability_space
- prob_pdf
- prob_joint_distribution
- prob_iid
- prob_expectation
- prob_covariance
- prob_conv_as
- prob_clt
- linear_algebra_background
- statistical_model
- parametric_model
- parameter_space
- iid_sample
- identifiability
- dominated_family
- true_parameter_interior
- support_independent_of_theta
- likelihood_function
- interchange_derivative_integral
- maximum_likelihood_estimator
- log_likelihood
- mle_consistency
- score_function
- log_likelihood_smooth
- score_identity
- fisher_information_matrix
- fisher_information
- mle_score_equation
- fisher_information_positive_definite
- information_equality

## bayes_estimator
_(16 prerequisites)_

- prob_random_variable
- prob_probability_space
- prob_iid
- prob_expectation
- prob_conditional_distribution
- statistical_model
- parametric_model
- parameter_space
- null_hypothesis
- loss_function
- iid_sample
- statistic
- estimator
- test_function
- decision_rule
- risk_function

## credible_interval
_(17 prerequisites)_

- prob_random_variable
- prob_probability_space
- prob_iid
- prob_expectation
- prob_conditional_distribution
- statistical_model
- parametric_model
- parameter_space
- null_hypothesis
- loss_function
- iid_sample
- statistic
- estimator
- test_function
- decision_rule
- risk_function
- bayes_estimator

## bernstein_von_mises
_(52 prerequisites)_

- ra_taylor_theorem
- ra_mean_value_theorem
- ra_interchange_limit_integral
- ra_differentiability
- ra_continuity
- ra_compactness
- prob_wlln
- prob_variance
- prob_slutsky
- prob_slln
- prob_random_variable
- prob_probability_space
- prob_pdf
- prob_joint_distribution
- prob_iid
- prob_expectation
- prob_covariance
- prob_conv_as
- prob_conditional_distribution
- prob_clt
- linear_algebra_background
- statistical_model
- parametric_model
- parameter_space
- null_hypothesis
- loss_function
- iid_sample
- identifiability
- dominated_family
- true_parameter_interior
- statistic
- estimator
- support_independent_of_theta
- likelihood_function
- interchange_derivative_integral
- test_function
- maximum_likelihood_estimator
- log_likelihood
- mle_consistency
- decision_rule
- score_function
- log_likelihood_smooth
- score_identity
- fisher_information_matrix
- fisher_information
- risk_function
- bayes_estimator
- mle_score_equation
- fisher_information_positive_definite
- information_equality
- credible_interval
- mle_asymptotic_normality

## risk_function
_(14 prerequisites)_

- prob_random_variable
- prob_probability_space
- prob_iid
- prob_expectation
- statistical_model
- parametric_model
- parameter_space
- null_hypothesis
- loss_function
- iid_sample
- statistic
- estimator
- test_function
- decision_rule

## admissibility
_(15 prerequisites)_

- prob_random_variable
- prob_probability_space
- prob_iid
- prob_expectation
- statistical_model
- parametric_model
- parameter_space
- null_hypothesis
- loss_function
- iid_sample
- statistic
- estimator
- test_function
- decision_rule
- risk_function

## bayes_rule_minimizes_bayes_risk
_(21 prerequisites)_

- prob_tower_property
- prob_random_variable
- prob_probability_space
- prob_iid
- prob_expectation
- prob_conditional_expectation
- prob_conditional_distribution
- statistical_model
- parametric_model
- parameter_space
- null_hypothesis
- loss_function
- iid_sample
- statistic
- estimator
- test_function
- decision_rule
- risk_function
- bayes_risk
- bayes_estimator
- posterior_mean_rule

## james_stein
_(25 prerequisites)_

- ra_continuity
- ra_compactness
- prob_random_variable
- prob_probability_space
- prob_pdf
- prob_normal
- prob_joint_distribution
- prob_iid
- prob_expectation
- statistical_model
- parametric_model
- parameter_space
- null_hypothesis
- loss_function
- iid_sample
- dominated_family
- statistic
- estimator
- likelihood_function
- test_function
- maximum_likelihood_estimator
- mean_squared_error
- decision_rule
- risk_function
- admissibility

## chi_squared_distribution
_(3 prerequisites)_

- prob_standard_normal
- prob_mgf
- prob_gamma

## students_t_distribution
_(5 prerequisites)_

- prob_standard_normal
- prob_mgf
- prob_independence_rv
- prob_gamma
- chi_squared_distribution

## sample_mean
_(5 prerequisites)_

- prob_probability_space
- prob_iid
- prob_expectation_linearity
- statistical_model
- iid_sample

## sample_variance
_(6 prerequisites)_

- prob_probability_space
- prob_iid
- prob_expectation_linearity
- statistical_model
- iid_sample
- sample_mean

## bias_of_sample_variance
_(10 prerequisites)_

- prob_variance
- prob_probability_space
- prob_independence_factorization
- prob_iid
- prob_expectation_linearity
- prob_covariance
- statistical_model
- iid_sample
- sample_mean
- sample_variance

## normal_sample_mean_variance_independence
_(20 prerequisites)_

- prob_random_variable
- prob_probability_space
- prob_normal
- prob_independence_rv
- prob_independence_factorization
- prob_iid
- prob_expectation_linearity
- prob_expectation
- prob_conditional_distribution
- prob_cdf
- linear_algebra_background
- statistical_model
- iid_sample
- statistic
- sample_mean
- completeness_statistic
- ancillary_statistic
- sufficiency
- sample_variance
- basu_theorem

## scaled_sample_variance_chi_squared
_(26 prerequisites)_

- prob_standard_normal
- prob_random_variable
- prob_probability_space
- prob_normal
- prob_mgf
- prob_independence_rv
- prob_independence_factorization
- prob_iid
- prob_gamma
- prob_expectation_linearity
- prob_expectation
- prob_conditional_distribution
- prob_cdf
- linear_algebra_background
- chi_squared_distribution
- statistical_model
- iid_sample
- cochran_theorem
- statistic
- sample_mean
- completeness_statistic
- ancillary_statistic
- sufficiency
- sample_variance
- basu_theorem
- normal_sample_mean_variance_independence

## t_statistic_distribution
_(29 prerequisites)_

- prob_standard_normal
- prob_random_variable
- prob_probability_space
- prob_normal_affine_closure
- prob_normal
- prob_mgf
- prob_independence_rv
- prob_independence_factorization
- prob_iid
- prob_gamma
- prob_expectation_linearity
- prob_expectation
- prob_conditional_distribution
- prob_cdf
- linear_algebra_background
- chi_squared_distribution
- statistical_model
- iid_sample
- students_t_distribution
- cochran_theorem
- statistic
- sample_mean
- completeness_statistic
- ancillary_statistic
- sufficiency
- sample_variance
- basu_theorem
- normal_sample_mean_variance_independence
- scaled_sample_variance_chi_squared

## confidence_set
_(4 prerequisites)_

- prob_probability_space
- statistical_model
- parametric_model
- parameter_space

## confidence_set_test_duality
_(13 prerequisites)_

- prob_random_variable
- prob_probability_space
- prob_iid
- prob_expectation
- statistical_model
- parametric_model
- parameter_space
- null_hypothesis
- iid_sample
- confidence_set
- statistic
- test_function
- size_of_test

## normal_mean_ci_unknown_variance
_(35 prerequisites)_

- prob_standard_normal
- prob_random_variable
- prob_probability_space
- prob_normal_affine_closure
- prob_normal
- prob_mgf
- prob_independence_rv
- prob_independence_factorization
- prob_iid
- prob_gamma
- prob_expectation_linearity
- prob_expectation
- prob_conditional_distribution
- prob_cdf
- linear_algebra_background
- chi_squared_distribution
- statistical_model
- parametric_model
- parameter_space
- iid_sample
- confidence_set
- students_t_distribution
- cochran_theorem
- pivotal_quantity
- statistic
- sample_mean
- pivot_method
- completeness_statistic
- ancillary_statistic
- sufficiency
- sample_variance
- basu_theorem
- normal_sample_mean_variance_independence
- scaled_sample_variance_chi_squared
- t_statistic_distribution

## wald_interval
_(22 prerequisites)_

- ra_differentiability
- prob_variance
- prob_standard_normal
- prob_random_variable
- prob_probability_space
- prob_pdf
- prob_joint_distribution
- prob_iid
- prob_conv_d
- statistical_model
- parametric_model
- parameter_space
- iid_sample
- dominated_family
- confidence_set
- statistic
- estimator
- likelihood_function
- asymptotic_normality_estimator
- log_likelihood
- score_function
- fisher_information

## test_function
_(9 prerequisites)_

- prob_random_variable
- prob_probability_space
- prob_iid
- statistical_model
- parametric_model
- parameter_space
- null_hypothesis
- iid_sample
- statistic

## size_of_test
_(11 prerequisites)_

- prob_random_variable
- prob_probability_space
- prob_iid
- prob_expectation
- statistical_model
- parametric_model
- parameter_space
- null_hypothesis
- iid_sample
- statistic
- test_function

## power_function
_(12 prerequisites)_

- prob_random_variable
- prob_probability_space
- prob_iid
- prob_expectation
- statistical_model
- parametric_model
- parameter_space
- null_hypothesis
- iid_sample
- alternative_hypothesis
- statistic
- test_function

## neyman_pearson_lemma
_(18 prerequisites)_

- prob_random_variable
- prob_probability_space
- prob_pdf
- prob_joint_distribution
- prob_iid
- prob_expectation
- statistical_model
- parametric_model
- parameter_space
- null_hypothesis
- iid_sample
- dominated_family
- alternative_hypothesis
- statistic
- likelihood_function
- test_function
- size_of_test
- power_function

## likelihood_ratio_test
_(14 prerequisites)_

- ra_continuity
- ra_compactness
- prob_probability_space
- prob_pdf
- prob_joint_distribution
- prob_iid
- statistical_model
- parametric_model
- parameter_space
- null_hypothesis
- iid_sample
- dominated_family
- likelihood_function
- maximum_likelihood_estimator

## wilks_theorem
_(47 prerequisites)_

- ra_taylor_theorem
- ra_mean_value_theorem
- ra_interchange_limit_integral
- ra_differentiability
- ra_continuity
- ra_compactness
- prob_wlln
- prob_variance
- prob_standard_normal
- prob_slutsky
- prob_slln
- prob_probability_space
- prob_pdf
- prob_mgf
- prob_joint_distribution
- prob_iid
- prob_gamma
- prob_expectation
- prob_covariance
- prob_conv_as
- prob_clt
- linear_algebra_background
- chi_squared_distribution
- statistical_model
- parametric_model
- parameter_space
- null_hypothesis
- iid_sample
- identifiability
- dominated_family
- true_parameter_interior
- support_independent_of_theta
- likelihood_function
- interchange_derivative_integral
- maximum_likelihood_estimator
- log_likelihood
- likelihood_ratio_test
- mle_consistency
- score_function
- log_likelihood_smooth
- score_identity
- fisher_information_matrix
- fisher_information
- mle_score_equation
- fisher_information_positive_definite
- information_equality
- mle_asymptotic_normality

## p_value
_(12 prerequisites)_

- prob_random_variable
- prob_probability_space
- prob_iid
- prob_expectation
- statistical_model
- parametric_model
- parameter_space
- null_hypothesis
- iid_sample
- statistic
- test_function
- size_of_test

## empirical_cdf
_(6 prerequisites)_

- prob_probability_space
- prob_iid
- prob_cdf
- prob_bernoulli
- statistical_model
- iid_sample

## glivenko_cantelli
_(9 prerequisites)_

- prob_slln
- prob_probability_space
- prob_iid
- prob_conv_as
- prob_cdf
- prob_bernoulli
- statistical_model
- iid_sample
- empirical_cdf

## bootstrap
_(11 prerequisites)_

- prob_random_variable
- prob_probability_space
- prob_iid
- prob_cdf
- prob_bernoulli
- statistical_model
- iid_sample
- empirical_cdf
- statistic
- plug_in_principle
- plug_in_estimator

## linear_model
_(3 prerequisites)_

- prob_random_vector
- prob_normal
- linear_algebra_background

## ordinary_least_squares
_(5 prerequisites)_

- ra_differentiability
- prob_random_vector
- prob_normal
- linear_algebra_background
- linear_model

## gauss_markov_theorem
_(19 prerequisites)_

- ra_differentiability
- prob_random_vector
- prob_random_variable
- prob_probability_space
- prob_normal
- prob_iid
- prob_expectation
- prob_covariance
- linear_algebra_background
- statistical_model
- parametric_model
- parameter_space
- linear_model
- iid_sample
- ordinary_least_squares
- statistic
- estimator
- bias
- unbiased_estimator

## ols_distribution_under_normal_errors
_(32 prerequisites)_

- ra_differentiability
- prob_standard_normal
- prob_random_vector
- prob_random_variable
- prob_probability_space
- prob_normal_affine_closure
- prob_normal
- prob_mgf
- prob_independence_rv
- prob_independence_factorization
- prob_iid
- prob_gamma
- prob_expectation_linearity
- prob_expectation
- prob_conditional_distribution
- prob_cdf
- linear_algebra_background
- chi_squared_distribution
- statistical_model
- linear_model
- iid_sample
- cochran_theorem
- ordinary_least_squares
- normal_equations
- statistic
- sample_mean
- completeness_statistic
- ancillary_statistic
- sufficiency
- sample_variance
- basu_theorem
- normal_sample_mean_variance_independence

