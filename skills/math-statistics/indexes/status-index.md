# Result index by node type (generated)

## primitive

## axiom

## structure
- **statistical_model** (model) — a family P = { P_theta : theta in Theta } of candidate distributions for the data
- **exponential_family** (exponential_family) — f(x; eta) = h(x) exp( eta . T(x) - A(eta) )
- **linear_model** (regression) — y = X beta + eps, X in R^{n x p} fixed full-rank, eps ~ N(0, sigma^2 I_n)

## notation_convention

## principle_law

## definition
- **parametric_model** (model) — a statistical model indexed by a finite-dimensional Theta subset of R^d
- **parameter_space** (model) — the set Theta of admissible parameter values
- **iid_sample** (model) — X_1,...,X_n drawn independently from one P_theta in the model
- **statistic** (model) — T = T(X_1,...,X_n), a measurable function of the data not depending on theta
- **likelihood_function** (model) — L(theta) = prod_i f(x_i; theta), viewed as a function of theta for fixed data
- **log_likelihood** (model) — ell(theta) = sum_i log f(x_i; theta)
- **score_function** (model) — U(theta) = d ell / d theta = sum_i d/dtheta log f(x_i; theta)
- **fisher_information** (model) — I(theta) = Var_theta(U_1(theta)) for one observation
- **fisher_information_matrix** (model) — I(theta) = Cov_theta(nabla log f(X;theta)), a d x d PSD matrix
- **natural_parameter_space** (exponential_family) — { eta : int h(x) exp(eta . T(x)) dx < inf }, a convex set
- **cumulant_function** (exponential_family) — A(eta) = log int h(x) exp(eta . T(x)) dx
- **mean_value_parametrization** (exponential_family) — the reparametrization by mu = E_eta[T(X)] = grad A(eta)
- **sufficiency** (sufficiency) — T is sufficient for theta if the conditional law of the data given T does not depend on theta
- **minimal_sufficiency** (sufficiency) — a sufficient statistic that is a function of every other sufficient statistic
- **ancillary_statistic** (sufficiency) — a statistic whose distribution does not depend on theta
- **completeness_statistic** (sufficiency) — E_theta[g(T)] = 0 for all theta implies g(T) = 0 a.s. for all theta
- **bounded_completeness** (sufficiency) — the completeness condition restricted to bounded g
- **estimator** (estimation) — a statistic theta_hat = theta_hat(X_1..X_n) used as a guess for theta (or for g(theta))
- **bias** (estimation) — b(theta) = E_theta[theta_hat] - theta
- **mean_squared_error** (estimation) — MSE(theta) = E_theta[(theta_hat - theta)^2]
- **unbiased_estimator** (estimation) — E_theta[theta_hat] = theta for every theta
- **consistency** (estimation) — theta_hat_n -> theta in probability (under P_theta) for every theta
- **asymptotic_variance** (estimation) — v(theta) with sqrt(n)(theta_hat_n - theta) -> N(0, v(theta)) in distribution
- **asymptotic_normality_estimator** (estimation) — sqrt(n)(theta_hat_n - theta) converges in distribution to a centered normal
- **relative_efficiency** (estimation) — ratio of asymptotic variances of two estimators of the same quantity
- **asymptotic_efficiency** (estimation) — an estimator whose asymptotic variance equals the Cramer-Rao bound I(theta)^{-1}
- **umvue** (estimation) — an unbiased estimator with the smallest variance for every theta among all unbiased estimators
- **plug_in_principle** (methods) — estimate a functional T(P) by T(P_hat_n) with P_hat_n the empirical distribution
- **maximum_likelihood_estimator** (methods) — theta_hat = argmax_theta L(theta) = argmax_theta ell(theta)
- **m_estimator** (methods) — theta_hat maximizes (1/n) sum m(X_i; theta), or solves (1/n) sum psi(X_i; theta) = 0
- **bayes_estimator** (methods) — the decision rule minimizing the posterior expected loss E[ L(theta, a) | x ]
- **conjugate_prior** (methods) — a prior family closed under the likelihood: posterior stays in the family
- **credible_interval** (intervals) — a set C(x) with posterior probability P(theta in C(x) | x) = 1 - alpha
- **loss_function** (decision_theory) — L(theta, a) >= 0, the cost of action a when the truth is theta
- **risk_function** (decision_theory) — R(theta, delta) = E_theta[ L(theta, delta(X)) ]
- **decision_rule** (decision_theory) — delta: data -> action space (an estimator or a test is a decision rule)
- **admissibility** (decision_theory) — delta is admissible if no rule has R(theta, .) <= R(theta, delta) everywhere with strict somewhere
- **minimax_rule** (decision_theory) — a rule minimizing sup_theta R(theta, delta)
- **bayes_risk** (decision_theory) — r(pi, delta) = int R(theta, delta) pi(dtheta) for a prior pi
- **sample_mean** (gaussian_core) — Xbar_n = (1/n) sum_{i=1}^n X_i
- **sample_variance** (gaussian_core) — S^2 = (1/(n-1)) sum_{i=1}^n (X_i - Xbar)^2
- **confidence_set** (intervals) — C(X) with P_theta(theta in C(X)) >= 1 - alpha for every theta
- **coverage_probability** (intervals) — P_theta(theta in C(X)) as a function of theta
- **pivotal_quantity** (intervals) — Q(X, theta) whose distribution does not depend on theta
- **wald_interval** (intervals) — theta_hat +- z_{1-alpha/2} se(theta_hat) with se from the estimated information; asymptotic coverage
- **null_hypothesis** (testing) — H0: theta in Theta_0, the hypothesis put on trial
- **alternative_hypothesis** (testing) — H1: theta in Theta_1 = Theta \ Theta_0
- **test_function** (testing) — phi: data -> [0,1], the probability of rejecting H0 given the data
- **size_of_test** (testing) — size = sup_{theta in Theta_0} E_theta[phi]; a level-alpha test has size <= alpha
- **power_function** (testing) — beta(theta) = E_theta[phi], the rejection probability; power on Theta_1
- **type_i_error** (testing) — Type I: reject a true H0 (prob <= size); Type II: fail to reject a false H0 (prob 1 - power)
- **likelihood_ratio_test** (testing) — reject H0 for small Lambda = sup_{Theta_0} L / sup_{Theta} L
- **wald_test** (testing) — reject when (theta_hat - theta_0)^2 n I(theta_hat) exceeds chi^2_{1,1-alpha}
- **score_test** (testing) — reject when U(theta_0)^2 / (n I(theta_0)) exceeds chi^2_{1,1-alpha}; needs only the null fit
- **p_value** (testing) — the smallest alpha at which the observed data reject H0; p(X) = sup_{Theta_0} P_theta(T >= T(x))
- **multiple_testing_fwer** (testing) — FWER = P(at least one true null rejected) across a family of m tests
- **empirical_cdf** (nonparametric) — F_hat_n(x) = (1/n) sum 1{X_i <= x}
- **order_statistic** (nonparametric) — X_(1) <= ... <= X_(n), the sorted sample
- **sample_quantile** (nonparametric) — F_hat_n^{-1}(p), a plug-in estimate of the population quantile
- **plug_in_estimator** (nonparametric) — T(F_hat_n) for a statistical functional T
- **kernel_density_estimator** (nonparametric) — f_hat_h(x) = (1/nh) sum K((x - X_i)/h)
- **ordinary_least_squares** (regression) — beta_hat = argmin_b |y - X b|^2
- **residual_sum_of_squares** (regression) — RSS = |y - X beta_hat|^2 = y^T (I - H) y
- **r_squared** (regression) — R^2 = 1 - RSS/TSS, the fraction of variance explained

## construction
- **chi_squared_distribution** (gaussian_core) — chi^2_k := Gamma(k/2, 1/2); equivalently the law of sum of k iid N(0,1)^2
- **students_t_distribution** (gaussian_core) — t_k := Z / sqrt(V/k) with Z ~ N(0,1) independent of V ~ chi^2_k
- **f_distribution** (gaussian_core) — F_{d1,d2} := (U/d1)/(V/d2) with U ~ chi^2_{d1} independent of V ~ chi^2_{d2}

## proposition
- **crlb_attainment** (estimation) — an unbiased estimator attains the CRLB for all theta iff the model is a one-parameter exponential family and theta_hat is its natural sufficient statistic
- **mle_score_equation** (methods) — an interior MLE satisfies U(theta_hat) = 0
- **mle_invariance** (methods) — if theta_hat is the MLE of theta then g(theta_hat) is the MLE of g(theta)
- **sandwich_variance** (methods) — an M-estimator has asymptotic variance A^{-1} B A^{-T} with A = -E[psi'], B = E[psi psi^T]
- **one_sample_t_test** (testing) — reject H0: mu = mu_0 when |sqrt(n)(Xbar - mu_0)/S| > t_{n-1, 1-alpha/2}; exact level alpha
- **two_sample_t_test** (testing) — pooled or Welch t-statistic for H0: mu_X = mu_Y
- **f_test_equality_of_variances** (testing) — S_X^2 / S_Y^2 ~ F_{n-1, m-1} under H0: sigma_X = sigma_Y for normal samples
- **normal_mean_ci_known_variance** (intervals) — Xbar +- z_{1-alpha/2} sigma/sqrt(n) has exact coverage 1 - alpha when sigma is known
- **normal_mean_ci_unknown_variance** (intervals) — Xbar +- t_{n-1,1-alpha/2} S/sqrt(n) has exact coverage 1 - alpha
- **normal_variance_ci** (intervals) — ((n-1)S^2/chi^2_{n-1,1-alpha/2}, (n-1)S^2/chi^2_{n-1,alpha/2}) has exact coverage
- **delta_method_standard_error** (intervals) — se(g(theta_hat)) = |g'(theta_hat)| se(theta_hat); gives an asymptotic interval for g(theta)
- **large_sample_wald_interval** (intervals) — theta_hat_MLE +- z_{1-alpha/2} / sqrt(n I(theta_hat)) has coverage -> 1 - alpha
- **p_value_uniform_under_null** (testing) — for a continuous test statistic with a simple H0, p(X) ~ Uniform(0,1) under H0
- **bonferroni_correction** (testing) — testing each of m hypotheses at level alpha/m controls FWER at alpha
- **benjamini_hochberg_fdr** (testing) — the step-up rule on ordered p-values controls the false discovery rate at alpha under independence
- **unbiased_error_variance_estimator** (regression) — sigma_hat^2 = RSS / (n - p) has E[sigma_hat^2] = sigma^2
- **coefficient_t_test** (regression) — (beta_hat_j - beta_j) / se(beta_hat_j) ~ t_{n-p} under normal errors
- **overall_f_test** (regression) — ((RSS_0 - RSS)/q) / (RSS/(n-p)) ~ F_{q, n-p} under the reduced-model null

## theorem
- **exponential_family_sufficient_statistic** (exponential_family) — in f(x;eta) = h(x) exp(eta.T(x) - A(eta)), T(X_1..X_n) = sum T(X_i) is sufficient for eta
- **exponential_family_completeness** (exponential_family) — if the natural parameter space contains an open set, the natural sufficient statistic is complete
- **neyman_fisher_factorization** (sufficiency) — T is sufficient iff f(x;theta) = g(T(x); theta) h(x) for some g, h >= 0
- **basu_theorem** (sufficiency) — a complete sufficient statistic is independent of every ancillary statistic
- **cramer_rao_lower_bound** (estimation) — Var_theta(theta_hat) >= (1 + b'(theta))^2 / (n I(theta)); = 1/(n I(theta)) if unbiased
- **rao_blackwell_theorem** (estimation) — if T is sufficient, E[theta_hat | T] is unbiased (if theta_hat was) with Var no larger
- **lehmann_scheffe_theorem** (estimation) — an unbiased function of a complete sufficient statistic is the unique UMVUE
- **mle_consistency** (methods) — under identifiability and regularity, theta_hat_n -> theta_0 in probability
- **mle_asymptotic_normality** (methods) — sqrt(n)(theta_hat_n - theta_0) -> N(0, I(theta_0)^{-1}) in distribution
- **posterior_mean_rule** (methods) — under L(theta,a) = (theta - a)^2 the Bayes estimator is E[theta | x]
- **posterior_median_rule** (methods) — under L(theta,a) = |theta - a| the Bayes estimator is a posterior median
- **bernstein_von_mises** (methods) — under regularity the posterior is asymptotically N(theta_hat, (n I)^{-1}); credible sets have frequentist coverage
- **bayes_rule_minimizes_bayes_risk** (decision_theory) — the rule minimizing the posterior expected loss for each x minimizes r(pi, .)
- **complete_class** (decision_theory) — under convexity/compactness the Bayes rules (and their limits) form a complete class
- **normal_sample_mean_variance_independence** (gaussian_core) — if X_1..X_n ~ iid N(mu, sigma^2) then Xbar and S^2 are independent
- **scaled_sample_variance_chi_squared** (gaussian_core) — for an iid normal sample, (n-1)S^2/sigma^2 has the chi-squared law with n-1 df
- **t_statistic_distribution** (gaussian_core) — sqrt(n)(Xbar - mu)/S ~ t_{n-1} for an iid N(mu, sigma^2) sample
- **cochran_theorem** (gaussian_core) — if sum of quadratic forms Q_i in iid standard normals sums to |x|^2 with ranks summing to n, the Q_i are independent chi^2_{r_i}
- **confidence_set_test_duality** (intervals) — C(x) = { theta_0 : the level-alpha test of H0: theta = theta_0 accepts at x } has coverage 1 - alpha, and conversely
- **neyman_pearson_lemma** (testing) — for H0: f0 vs H1: f1 the size-alpha likelihood-ratio test phi* = 1{f1 > k f0} is most powerful
- **karlin_rubin_theorem** (testing) — under MLR in T, the test 1{T > c} is UMP for H0: theta <= theta_0 vs H1: theta > theta_0
- **wilks_theorem** (testing) — under H0 and regularity, -2 log Lambda -> chi^2_r in distribution, r = dim drop
- **three_tests_asymptotically_equivalent** (testing) — under H0 and local alternatives the three statistics differ by o_p(1) and share the chi^2_r limit
- **pearson_chi_squared_gof** (testing) — sum (O_j - E_j)^2 / E_j -> chi^2_{k-1-d} under the fitted null
- **glivenko_cantelli** (nonparametric) — sup_x |F_hat_n(x) - F(x)| -> 0 almost surely, for every F
- **dvoretzky_kiefer_wolfowitz** (nonparametric) — P(sup_x |F_hat_n(x) - F(x)| > t) <= 2 exp(-2 n t^2); a distribution-free confidence band
- **bootstrap_consistency** (nonparametric) — for a Hadamard-differentiable functional the bootstrap distribution converges to the sampling distribution
- **ols_is_projection** (regression) — y_hat = H y with H = X(X^T X)^{-1} X^T the projection onto the column space of X
- **gauss_markov_theorem** (regression) — among linear unbiased estimators of c^T beta, OLS has the smallest variance (BLUE), needing only E[eps]=0, Cov(eps)=sigma^2 I
- **ols_distribution_under_normal_errors** (regression) — under normal errors beta_hat ~ N(beta, sigma^2 (X^T X)^{-1}) and is independent of RSS
- **partitioned_regression** (regression) — the OLS coefficient on X_2 equals that from regressing residualized y on residualized X_2
- **le_cam_lan_theory** (principles) — regular models are locally asymptotically normal; the log-likelihood ratio has a Gaussian-shift limit
- **hajek_convolution_theorem** (principles) — the limit law of any regular estimator is the efficient normal convolved with independent noise
- **local_asymptotic_minimax** (principles) — the local minimax risk of any estimator is bounded below by the efficient (CRLB) risk
- **donsker_theorem** (nonparametric) — the empirical process sqrt(n)(F_hat_n - F) converges to a Brownian bridge

## corollary

## mathematical_identity

