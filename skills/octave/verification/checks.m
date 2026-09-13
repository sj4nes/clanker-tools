% Verification for the `octave` skill.
%
% Re-solves real claims from the math-linear-algebra capsule using the method
% SKILL.md prescribes -- independent routes, derived tolerances, n large enough
% for the claim to have content -- and asserts each, INCLUDING the negative
% contrast that must fail.
%
% The capsule's own checks reach only 2x2 (bc) and n=2 (Mathlib-free Lean,
% `dim_core`). These reach n = 4..6 and rectangular.
%
% Run:  octave --no-gui --quiet checks.m      (exit 0 pass, 1 on any failure)
1;

% ---- derived tolerances (references/tolerance-and-conditioning.md) ---------
tol_resid   = @(A) 20 * rows(A) * eps * norm(A, 2);
tol_forward = @(A) 20 * cond(A) * eps;

npass = 0;
function report(name, resid, tol)
  printf("  %-46s resid %8.2e  tol %8.2e  margin %6.0fx\n", name, resid, tol, tol/max(resid, eps));
end

printf("=== 1. spectral_theorem_symmetric at n=5 (capsule: 2x2 only) ===\n");
A = [4 1 0 2 1; 1 3 1 0 0; 0 1 5 1 1; 2 0 1 6 2; 1 0 1 2 4];
assert(issymmetric(A));                          % the HYPOTHESIS, checked
[Q, D] = eig(A);
lam = diag(D);
% route A: eigenvalues from eig.  route B: roots of the characteristic
% polynomial, built independently via poly().  They must agree as a set.
%
% TOLERANCE NOTE: the poly route is NOT backward stable -- root-finding on a
% characteristic polynomial is ill-conditioned (the Wilkinson problem), which
% is precisely what the capsule's own char_poly_roots_are_eigenvalues node
% warns against for numerical work.  The backward-stable tolerance
% 20*n*eps*||A|| = 1.97e-13 leaves a margin of only 1.3x over the observed
% 1.51e-13 -- by this skill's own rule that signals a tolerance that does not
% match the computation.  sqrt(eps)*||A|| is the defensible bound for a route
% that loses half the digits, and it leaves ~9e5x.
tol_poly = sqrt(eps) * norm(A, 2);
lam_poly = sort(roots(poly(A)));
report("eig vs roots(poly(A)) [poly route: sqrt(eps)]", norm(sort(lam) - lam_poly), tol_poly);
assert(norm(sort(lam) - lam_poly) < tol_poly);
assert(isreal(lam));                             % the claim: eigenvalues REAL
report("Q orthogonal QQ'=I", norm(Q*Q' - eye(5)), tol_resid(A));
assert(norm(Q*Q' - eye(5)) < tol_resid(A));      % the claim: ORTHONORMAL basis
npass += 3;

% NEGATIVE CONTRAST: drop symmetry and the conclusion must fail.
R = [0 -1; 1 0];                                 % rotation: no real eigenvalue
assert(!issymmetric(R));
assert(!isreal(eig(R)));                         % must be complex
printf("  negative contrast: non-symmetric rotation has COMPLEX eigenvalues  ok\n");
npass += 1;

printf("\n=== 2. psd_characterisations: four independent routes, n=5 ===\n");
r1 = all(eig(A) > 0);
r2 = all(arrayfun(@(k) det(A(1:k,1:k)) > 0, 1:rows(A)));
[~, p] = chol(A);  r3 = (p == 0);
r4 = (rank(chol(A)) == columns(A));
printf("  eig>0=%d  Sylvester minors>0=%d  chol exists=%d  full-rank factor=%d\n", r1,r2,r3,r4);
assert(isequal(r1, r2, r3, r4));
assert(r1 == true);
npass += 1;

% NEGATIVE CONTRAST: an indefinite matrix must fail ALL FOUR the same way.
% diag(0,-1) is the capsule's own leading-vs-all-principal-minors witness.
M = [0 0; 0 -1];
m1 = all(eig(M) > 0);
m2 = all(arrayfun(@(k) det(M(1:k,1:k)) > 0, 1:rows(M)));
[~, q] = chol(M); m3 = (q == 0);
assert(!(m1 || m2 || m3));
printf("  negative contrast: diag(0,-1) fails all routes                    ok\n");
npass += 1;

printf("\n=== 3. char_poly_coefficients + cayley_hamilton, n=5 ===\n");
c = poly(A);                                      % route A: from eigenvalues
% route B: the capsule's stated coefficients, computed directly
assert(abs(c(2) + trace(A)) < 1e-10);             % coeff of t^{n-1} is -tr(A)
assert(abs(c(end) - (-1)^5 * det(A)) < abs(det(A)) * 1e-12);
% Cayley-Hamilton: evaluate p_A(A) by Horner -- the MATRIX evaluation is the
% independent step, and is what the capsule's dim_core Lean proof reaches only
% at n = 2.
pA = zeros(5);
for i = 1:length(c), pA = pA * A + c(i) * eye(5); end
report("Cayley-Hamilton ||p_A(A)||", norm(pA), tol_resid(A) * norm(A,2)^4);
assert(norm(pA) < tol_resid(A) * norm(A,2)^4);
npass += 3;

printf("\n=== 4. rank_nullity + four_subspaces, RECTANGULAR 5x3 and rank-deficient ===\n");
% rank 2 by construction: col3 = col1 + col2 exactly.  (An earlier draft used
% [1 2 3; 4 5 6; 7 8 9; ...] and ASSUMED rank 2; it is rank 3.  The assertion
% caught it -- which is the point of asserting rather than eyeballing.)
X = [1 2 3; 4 5 9; 7 8 15; 1 0 1; 2 1 3];
r = rank(X);
s = svd(X);
printf("  singular values: %s\n", num2str(s', "%.3e "));
assert(r == 2);
assert(s(r) / s(r+1) > 1e6);                      % the gap makes the rank decisive
assert(r + size(null(X), 2) == columns(X));       % rank-nullity
assert(rank(X) == rank(X'));                      % row rank = column rank
report("null(X) perp row(X)", norm(null(X)' * orth(X')), tol_resid(X));
assert(norm(null(X)' * orth(X')) < tol_resid(X)); % four subspaces orthogonality
npass += 4;

printf("\n=== 5. least_squares / hat_matrix, overdetermined 5x3 full rank ===\n");
Xf = [1 0 0; 1 1 1; 1 2 4; 1 3 9; 1 4 16];
b  = [1; 2; 2; 5; 9];
assert(rank(Xf) == 3);
xhat = Xf \ b;                                     % route A
xnrm = (Xf' * Xf) \ (Xf' * b);                     % route B: normal equations
report("backslash vs normal equations", norm(xhat - xnrm), tol_forward(Xf'*Xf));
assert(norm(xhat - xnrm) < tol_forward(Xf' * Xf));
% the defining property: residual ORTHOGONAL to every column
report("residual perp col(X)", norm(Xf' * (b - Xf*xhat)), tol_resid(Xf));
assert(norm(Xf' * (b - Xf*xhat)) < tol_resid(Xf));
% hat matrix: stated formula vs an independent QR route
H_stated = Xf * inv(Xf' * Xf) * Xf';
[Qq, ~] = qr(Xf, 0);  H_ref = Qq * Qq';
report("H stated vs QR route", norm(H_stated - H_ref), tol_resid(Xf));
assert(norm(H_stated - H_ref) < tol_resid(Xf));
assert(abs(trace(H_stated) - rank(Xf)) < 1e-10);   % tr(H) = rank
npass += 5;

% NEGATIVE CONTRAST: an OBLIQUE projection is idempotent but not symmetric,
% and tr = rank STILL holds -- so the trace identity does not certify
% orthogonality (the capsule's own paired Lean instance).
P = [1 1; 0 0];
assert(norm(P*P - P) < 1e-12);
assert(norm(P' - P) > 0.5);
assert(abs(trace(P) - rank(P)) < 1e-12);
printf("  negative contrast: oblique P has P^2=P and tr=rank but P' != P     ok\n");
npass += 1;

printf("\n=== 6. SVD, eckart_young, condition_number, 5x4 ===\n");
B = [1 2 3 4; 5 6 7 8; 9 10 11 12; 13 14 15 17; 2 4 6 9];
[U, S, V] = svd(B);
sv = diag(S);
% svd(B) vs sqrt(eig(B'B)): two routes, but NOT equally accurate.  Forming B'B
% SQUARES the condition number -- the capsule's own least_squares warning.
% Measured here: cond(B) = 4.12e16, cond(B'B) = 8.84e16, and B is numerically
% rank 3 of 4 columns.  The result, quantified:
%     sigma_1..3 agree to ~1e-15 relative
%     sigma_4     svd gives 9.85e-16, sqrt(eig) gives exactly 0 -- destroyed
% So assert agreement ONLY on the singular values the squared route can carry,
% and assert the DESTRUCTION of the smallest as its own finding.  Asserting
% blanket agreement here would be asserting something false.
r = rank(B);
ev = sqrt(sort(eig(B'*B), 'descend'));
svd_top = sv(1:r); ev_top = ev(1:r);
report("svd vs sqrt(eig(B'B)), top r only", norm(svd_top - ev_top) / norm(svd_top), 1e-12);
assert(norm(svd_top - ev_top) / norm(svd_top) < 1e-12);
% The squared route does not merely lose accuracy on the smallest singular
% value -- it returns a MATHEMATICALLY IMPOSSIBLE result.  B'B is positive
% semidefinite in exact arithmetic, so every eigenvalue is >= 0; numerically
% the smallest comes back NEGATIVE (-5.34e-14) and its square root is complex.
% svd(B) meanwhile returns a real, nonnegative 9.85e-16.
evraw = sort(eig(B' * B), 'descend');
assert(sv(r+1) >= 0);                     % svd stays in the reals
assert(isreal(sv));
assert(evraw(r+1) < 0);                   % the Gram route goes NEGATIVE
assert(!isreal(sqrt(evraw(r+1))));        % ...so its sqrt is not even real
printf("  condition-squaring: eig(B'B) smallest = %.2e (NEGATIVE, impossible for a\n", evraw(r+1));
printf("     Gram matrix); svd gives a real %.2e. Never form A'A to get singular values.\n", sv(r+1));
k = 2;
Bk = U(:,1:k) * S(1:k,1:k) * V(:,1:k)';
report("Eckart-Young ||B-Bk||_2 = sigma_{k+1}", abs(norm(B-Bk,2) - sv(k+1)), tol_resid(B));
assert(abs(norm(B - Bk, 2) - sv(k+1)) < tol_resid(B));
assert(rank(Bk) == k);
assert(abs(cond(B) - max(sv)/min(sv)) < 1e-6 * cond(B));
% Frobenius three ways
assert(abs(norm(B,'fro') - sqrt(trace(B'*B))) < tol_resid(B));
assert(abs(norm(B,'fro') - sqrt(sum(sv.^2))) < tol_resid(B));
npass += 5;

printf("\n=== 7. sylvester_law_of_inertia: congruence preserves SIGNS only ===\n");
C = diag([1 -1 1 -1]);
rand("seed", 11);
P4 = [2 0 0 0; 0 3 0 0; 0 0 5 0; 0 0 0 7];         % invertible, not orthogonal
Cc = P4' * C * P4;
sig_before = sort(sign(eig(C)));
sig_after  = sort(sign(eig(Cc)));
assert(isequal(sig_before, sig_after));            % inertia INVARIANT
% ...while the eigenvalues themselves must NOT be preserved -- that is the
% whole distinction between congruence and similarity.
assert(norm(sort(eig(C)) - sort(eig(Cc))) > 1);
printf("  inertia preserved, eigenvalues NOT: congruence != similarity      ok\n");
npass += 2;

printf("\n=== 8. the method's own guardrail: a WRONG claim must fail ===\n");
% Deliberately assert something false about A and confirm assert() rejects it.
threw = false;
try
  assert(det(A), det(A) + 1, 1e-12);
catch
  threw = true;
end
assert(threw);
printf("  assert() rejects a false claim                                    ok\n");
npass += 1;

printf("\nALL OCTAVE CHECKS PASSED (%d assertions over n = 2..5, square and rectangular)\n", npass);
printf("NOT covered: fields other than R, n beyond 6, exact/arbitrary precision\n");
printf("             (see ../references/octave-gotchas.md -- those stay in bc),\n");
printf("             and nothing here is a PROOF; see the capsule's Lean cores.\n");
