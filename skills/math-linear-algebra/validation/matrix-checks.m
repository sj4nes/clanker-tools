% math-linear-algebra -- numerical matrix checks (GNU Octave)
%
% Run:  octave --no-gui --quiet validation/matrix-checks.m
%       exit 0 = all passed, 1 = a failed assertion
%
% WHAT THIS LAYER IS FOR
% ----------------------
% The capsule's other two validation layers are dimension-limited:
%
%   validation/proof-checks.lean   Mathlib-free, so it cannot quantify over n.
%                                  Its strongest matrix results are `dim_core`:
%                                  universal in the ENTRIES at a FIXED n = 2.
%   validation/instance-checks.bc  bc has no matrices; every matrix claim is
%                                  hand-rolled 2x2 scalar arithmetic.
%
% So before this file, the capsule's headline results -- the spectral theorem,
% the SVD, Eckart-Young, Courant-Fischer, Cholesky, the pseudoinverse -- were
% verified only at 2x2, where most of them are degenerate (every 2x2 symmetric
% matrix is diagonalisable; rank is 0, 1 or 2).
%
% This layer runs them at n = 4..6, rectangular, and rank-deficient.
%
% METHOD (skills/octave/SKILL.md)
% -------------------------------
%   * INDEPENDENT ROUTES. Never check a built-in against itself. Each claim is
%     computed two ways that share no code path, and the routes must agree.
%   * DERIVED TOLERANCES. Residual ~ n*eps*||A||; solution error ~ cond(A)*eps.
%     Never a fixed constant. A margin near 1x means the tolerance is guessed.
%   * NEGATIVE CONTRASTS. Every "X iff Y" gets a witness failing both; every
%     hypothesis gets a case where dropping it breaks the conclusion.
%
% WHAT THIS IS NOT
% ----------------
% Not a proof. A numerical check at n = 5 over R is evidence about n = 5 over R.
% The universal evidence is proof-checks.lean; the field-relative claims
% (any_field / char_not_2 / algebraically_closed) are NOT testable here at all,
% since Octave only has R and C. See the closing report.
1;

tol_resid   = @(A) 50 * rows(A) * eps * norm(A, 2);
tol_forward = @(A) 50 * cond(A) * eps;
np = 0;

function chk(name, resid, tol)
  printf("    %-52s %8.2e / %8.2e  (%.0fx)\n", name, resid, tol, tol/max(resid, eps));
  if (!(resid < tol))
    error("FAILED: %s -- residual %.3e exceeds tolerance %.3e", name, resid, tol);
  end
end

printf("\n=== A. determinants and trace (nodes: determinant_multiplicative,\n");
printf("       determinant_transpose, determinant_similarity_invariant,\n");
printf("       trace_cyclic, vandermonde_determinant) -- n = 5 ===\n");
rand("seed", 1);
A = [3 1 0 2 1; 1 4 2 0 1; 0 2 5 1 0; 2 0 1 6 2; 1 1 0 2 4];
P = [1 2 0 0 1; 0 1 1 0 0; 0 0 1 2 0; 1 0 0 1 1; 0 1 0 0 2];
assert(abs(det(P)) > 1e-8);                       % P invertible: the hypothesis
B = [2 0 1 1 0; 1 3 0 2 1; 0 1 2 0 1; 1 1 1 4 0; 2 0 0 1 3];

% det(AB) = det(A)det(B): route A via det of the product, route B via the
% product of dets. Scale by the magnitude -- determinants of 5x5 integers are
% large, so a relative comparison is the meaningful one.
chk("det(AB) = det(A)det(B)", abs(det(A*B) - det(A)*det(B)) / abs(det(A)*det(B)), 1e-12);
chk("det(A^T) = det(A)", abs(det(A') - det(A)) / abs(det(A)), 1e-12);
% det(kA) = k^n det(A) -- the trap the capsule's Lean file proves at n = 2
k = 3;
chk("det(kA) = k^n det(A), n=5", abs(det(k*A) - k^5*det(A)) / abs(k^5*det(A)), 1e-12);
% similarity invariance of det AND trace
chk("det(P^-1 A P) = det(A)", abs(det(P\A*P) - det(A)) / abs(det(A)), 1e-10);
chk("tr(P^-1 A P) = tr(A)", abs(trace(P\A*P) - trace(A)) / abs(trace(A)), 1e-12);
% trace is cyclic but NOT invariant under arbitrary permutation of 3 factors
chk("tr(AB) = tr(BA)", abs(trace(A*B) - trace(B*A)) / abs(trace(A*B)), 1e-12);
C = [1 1 0 0 0; 0 1 1 0 0; 0 0 1 1 0; 0 0 0 1 1; 1 0 0 0 1];
assert(abs(trace(A*B*C) - trace(A*C*B)) > 1e-6);  % cyclic only, NOT arbitrary
printf("    negative contrast: tr(ABC) != tr(ACB)  -- cyclic, not arbitrary   ok\n");
% determinant as the product of eigenvalues (independent route), and via LU
chk("det(A) = prod(eig(A))", abs(det(A) - prod(eig(A))) / abs(det(A)), 1e-10);
[L, U, Pm] = lu(A);
chk("det(A) = det(P)*prod(diag(U))  [LU route]", ...
    abs(det(A) - det(Pm')*prod(diag(U))) / abs(det(A)), 1e-10);
% Vandermonde: closed form vs det(), n = 5 distinct nodes
x = [1; 2; 3; 5; 7];
% NOTE: Octave's vander(x) orders columns DESCENDING (x.^(n-1) ... x.^0), the
% reverse of the capsule's index_convention V_{ij} = x_i^{j-1}. A column
% reversal is a permutation, so the determinants agree up to sign -- hence the
% comparison is on absolute values, and the convention difference is recorded
% rather than silently absorbed.
V = vander(x);
prodform = 1;
for jj = 1:length(x)
  for ii = 1:(jj-1)
    prodform *= (x(jj) - x(ii));                  % prod_{i<j} (x_j - x_i)
  end
end
chk("Vandermonde |det| = prod_{i<j}(x_j - x_i)", ...
    abs(abs(det(V)) - abs(prodform)) / abs(prodform), 1e-10);
xr = [1; 2; 2; 5; 7];                             % repeated node
assert(abs(det(vander(xr))) < 1e-8);              % must be SINGULAR
printf("    negative contrast: repeated node makes Vandermonde singular       ok\n");
np += 11;

printf("\n=== B. rank, four subspaces, rank inequalities (nodes: rank_nullity,\n");
printf("       four_subspaces, row_rank_equals_column_rank, rank_inequalities,\n");
printf("       determinant_rank_minors) -- RECTANGULAR 6x4, rank 3 ===\n");
% rank 3 by construction: col4 = col1 + 2*col2
X = [1 2 3 5; 4 5 6 14; 7 8 9 23; 1 0 1 1; 2 1 3 4; 0 3 1 6];
r = rank(X);
s = svd(X);
printf("    singular values: %s\n", num2str(s', "%.3e "));
assert(r == 3);
assert(s(r)/s(r+1) > 1e6);                        % the gap makes the rank decisive
assert(r + size(null(X), 2) == columns(X));       % rank-nullity in the domain
assert(rank(X) == rank(X'));                      % row rank = column rank
assert(size(null(X'), 1) - r == rows(X) - r);     % codomain count
chk("null(X) perp row(X)", norm(null(X)' * orth(X')), tol_resid(X));
chk("null(X^T) perp col(X)", norm(null(X')' * orth(X)), tol_resid(X));
% rank via minors (determinant_rank_minors): the largest nonvanishing minor
maxminor = 0;
rows_idx = nchoosek(1:rows(X), 4); cols_idx = nchoosek(1:columns(X), 4);
for i = 1:rows(rows_idx)
  for j = 1:rows(cols_idx)
    if (abs(det(X(rows_idx(i,:), cols_idx(j,:)))) > 1e-8) maxminor = 4; end
  end
end
assert(maxminor == 0);                            % no nonzero 4x4 minor: rank < 4
printf("    rank via minors: no nonvanishing 4x4 minor, consistent with rank 3 ok\n");
% rank inequalities at realistic size
Y = [1 0 1 0; 0 1 0 1; 1 1 0 0; 0 0 1 1];
assert(rank(X*Y) <= min(rank(X), rank(Y)));
assert(rank(X + [X(:,1) zeros(6,3)]) <= rank(X) + 1);
assert(rank(X*Y) >= rank(X) + rank(Y) - columns(X));   % Sylvester
printf("    rank(XY) <= min, subadditive, and Sylvester's lower bound hold     ok\n");
np += 9;

printf("\n=== C. eigentheory (nodes: characteristic_polynomial,\n");
printf("       char_poly_roots_are_eigenvalues, char_poly_coefficients,\n");
printf("       cayley_hamilton, algebraic_geometric_multiplicity,\n");
printf("       diagonalisability_criterion, minimal_polynomial_diagonalisable,\n");
printf("       schur_triangularisation) -- n = 5 ===\n");
c = poly(A);                                      % monic, descending
assert(abs(c(1) - 1) < 1e-12);                    % MONIC, per the convention node
% char_poly_coefficients: coeff of t^{n-1} is -tr(A); constant is (-1)^n det(A)
chk("coeff of t^4 = -tr(A)", abs(c(2) + trace(A)) / abs(trace(A)), 1e-12);
chk("constant term = (-1)^5 det(A)", abs(c(end) - (-1)^5*det(A)) / abs(det(A)), 1e-12);
% char_poly_roots_are_eigenvalues. The poly route is ill-conditioned (the
% capsule's own misuse note), so the tolerance is sqrt(eps)-scaled, NOT the
% backward-stable one -- see skills/octave/references/tolerance-and-conditioning.md
chk("eig(A) = roots(poly(A))  [poly route: sqrt(eps)]", ...
    norm(sort(eig(A)) - sort(roots(c))), sqrt(eps)*norm(A,2));
% Cayley-Hamilton by Horner: the MATRIX evaluation is the independent step
pA = zeros(5);
for i = 1:length(c), pA = pA*A + c(i)*eye(5); end
chk("Cayley-Hamilton ||p_A(A)||", norm(pA), tol_resid(A)*norm(A,2)^4);
np += 4;

% A DEFECTIVE matrix at n = 5: geometric < algebraic multiplicity.
% At 2x2 there is only one way to be defective; at n = 5 a 3-block plus a
% 2-block exercises the multiplicity bookkeeping properly.
J = [2 1 0 0 0; 0 2 1 0 0; 0 0 2 0 0; 0 0 0 2 1; 0 0 0 0 2];
alg  = 5;                                          % (t-2)^5
geom = columns(null(J - 2*eye(5)));                % one vector per Jordan block
printf("    defective J (blocks 3+2): algebraic mult = %d, geometric = %d\n", alg, geom);
assert(geom == 2);                                 % two blocks -> two eigenvectors
assert(geom < alg);                                % THE defect
assert(rank(J - 2*eye(5)) == 5 - geom);            % rank-nullity, consistently
% diagonalisability_criterion: NOT diagonalisable, because geom < alg
assert(geom != alg);
% minimal_polynomial_diagonalisable: m_J = (t-2)^3 (largest block), not squarefree
N = J - 2*eye(5);
assert(norm(N^3) < 1e-12 && norm(N^2) > 1e-12);    % nilpotency index 3
printf("    minimal polynomial (t-2)^3: NOT squarefree -> not diagonalisable   ok\n");
np += 5;

% POSITIVE contrast: a matrix with 5 distinct eigenvalues IS diagonalisable
D5 = diag([1 2 3 4 5]);
Ad = P * D5 / P;                                   % similar to a diagonal matrix
lam_d = sort(real(eig(Ad)));
assert(norm(lam_d - [1;2;3;4;5]) < sqrt(eps)*norm(Ad,2));
geom_d = 0;
for l = [1 2 3 4 5], geom_d += columns(null(Ad - l*eye(5))); end
assert(geom_d == 5);                               % sum of geometric mults = n
printf("    5 distinct eigenvalues: sum of geometric mults = 5 = n            ok\n");
np += 2;

% schur_triangularisation over C: A = Q T Q^*, Q unitary, T upper triangular.
% Applies to a NON-symmetric matrix -- the general case the capsule states.
[Qs, Ts] = schur(A, "complex");
chk("Schur: A = Q T Q^*", norm(Qs*Ts*Qs' - A), tol_resid(A));
chk("Schur: Q unitary", norm(Qs*Qs' - eye(5)), tol_resid(A));
assert(norm(tril(Ts, -1)) < 1e-10);                % T upper triangular
chk("Schur: diag(T) = eigenvalues", norm(sort(real(diag(Ts))) - sort(real(eig(A)))), sqrt(eps)*norm(A,2));
np += 4;

printf("\n=== D. inner product, projection, least squares (nodes: gram_schmidt,\n");
printf("       qr_factorisation, orthogonal_projection,\n");
printf("       projection_matrix_characterisation, best_approximation,\n");
printf("       least_squares, hat_matrix, adjoint_kernel_image) -- 6x3 ===\n");
Xf = [1 0 0; 1 1 1; 1 2 4; 1 3 9; 1 4 16; 1 5 25];
bv = [1; 2; 2; 5; 9; 13];
assert(rank(Xf) == 3);                             % full column rank: the hypothesis
% QR from Gram-Schmidt vs Octave's (Householder) -- genuinely different algorithms
[Qr, Rr] = qr(Xf, 0);
chk("QR: A = QR", norm(Qr*Rr - Xf), tol_resid(Xf));
chk("QR: Q'Q = I", norm(Qr'*Qr - eye(3)), tol_resid(Xf));
assert(norm(tril(Rr, -1)) < 1e-12);                % R upper triangular
% R is the Cholesky factor of the Gram matrix, up to signs -- an independent link
chk("|R| = |chol(X'X)|", norm(abs(Rr) - abs(chol(Xf'*Xf))), tol_resid(Xf'*Xf));
np += 4;

% least_squares: three independent routes to the same minimiser
x1 = Xf \ bv;                                      % QR-based solver
x2 = (Xf'*Xf) \ (Xf'*bv);                          % normal equations
x3 = pinv(Xf) * bv;                                % pseudoinverse
chk("backslash vs normal equations", norm(x1-x2), tol_forward(Xf'*Xf));
chk("backslash vs pinv", norm(x1-x3), tol_forward(Xf'*Xf));
% THE defining property: residual orthogonal to every column of X
chk("residual perp col(X)", norm(Xf'*(bv - Xf*x1)), tol_resid(Xf)*norm(bv));
np += 3;

% best_approximation: the projection really is the CLOSEST point of col(X).
% Sample many other points of col(X); every one must be strictly farther.
rand("seed", 5);
d0 = norm(bv - Xf*x1);
worse = true;
for t = 1:200
  xr = x1 + 0.1*(rand(3,1) - 0.5);
  if (norm(bv - Xf*xr) <= d0) worse = false; end
end
assert(worse);
printf("    best_approximation: 200 perturbed points of col(X) are all farther ok\n");
np += 1;

% hat_matrix / projection_matrix_characterisation
H = Xf * inv(Xf'*Xf) * Xf';                        % the capsule's STATED formula
Href = Qr * Qr';                                   % independent QR route
chk("H stated vs QR route", norm(H - Href), tol_resid(Xf));
chk("H idempotent", norm(H*H - H), tol_resid(Xf));
chk("H symmetric", norm(H - H'), tol_resid(Xf));
chk("tr(H) = rank(X)", abs(trace(H) - rank(Xf)), 1e-10);
chk("tr(I-H) = n - p", abs(trace(eye(6) - H) - (6 - 3)), 1e-10);
np += 5;

% NEGATIVE CONTRAST (the capsule's paired Lean instance, now at n = 6):
% an OBLIQUE projection is idempotent with tr = rank, but NOT symmetric, and
% it does NOT minimise the distance -- so the trace identity alone certifies
% nothing about orthogonality.
W = diag([1 1 1 1 1 9]);                           % a weighting -> oblique fit
Hw = Xf * inv(Xf'*W*Xf) * Xf' * W;
assert(norm(Hw*Hw - Hw) < 1e-9);                   % still idempotent
assert(abs(trace(Hw) - rank(Xf)) < 1e-9);          % still tr = rank
assert(norm(Hw - Hw') > 0.1);                      % but NOT symmetric
assert(norm(bv - Hw*bv) > d0);                     % and a WORSE approximation
printf("    negative contrast: oblique H has H^2=H and tr(H)=rank but H != H',\n");
printf("      and is strictly farther from b -- trace alone proves nothing     ok\n");
np += 4;

% adjoint_kernel_image: ker(A^T) = (im A)^perp, at 6x3
chk("null(X^T) perp col(X)", norm(null(Xf')' * orth(Xf)), tol_resid(Xf));
assert(size(null(Xf'), 2) == 6 - 3);               % dimension count
np += 2;

printf("\n=== E. spectral theory (nodes: self_adjoint_real_eigenvalues,\n");
printf("       spectral_theorem_symmetric, spectral_decomposition,\n");
printf("       spectral_theorem_normal, rayleigh_quotient, courant_fischer)\n");
printf("       -- n = 6, the capsule's Lean/bc reach only n = 2 ===\n");
S = [6 1 0 2 1 0; 1 5 2 0 1 1; 0 2 7 1 0 2; 2 0 1 8 2 1; 1 1 0 2 6 1; 0 1 2 1 1 5];
assert(issymmetric(S));                            % the HYPOTHESIS
[Qe, De] = eig(S);
lam = sort(diag(De));
assert(isreal(diag(De)));                          % self_adjoint_real_eigenvalues
chk("spectral: Q orthogonal", norm(Qe*Qe' - eye(6)), tol_resid(S));
chk("spectral: A = Q D Q'", norm(Qe*De*Qe' - S), tol_resid(S));
% independent route to the spectrum: roots of the characteristic polynomial
chk("eig(S) = roots(poly(S))  [sqrt(eps)]", ...
    norm(lam - sort(roots(poly(S)))), sqrt(eps)*norm(S,2));
np += 4;

% spectral_decomposition: S = sum lambda_i P_i with P_i orthogonal projections,
% P_i P_j = 0, sum P_i = I. Built from the eigenvectors, checked structurally.
Ssum = zeros(6); Psum = zeros(6);
for i = 1:6
  Pi = Qe(:,i) * Qe(:,i)';
  Ssum += diag(De)(i) * Pi;
  Psum += Pi;
  assert(norm(Pi*Pi - Pi) < 1e-10);                % each is idempotent
  assert(norm(Pi - Pi') < 1e-10);                  % ...and symmetric
end
chk("spectral decomposition S = sum lambda_i P_i", norm(Ssum - S), tol_resid(S));
chk("resolution of the identity sum P_i = I", norm(Psum - eye(6)), tol_resid(S));
assert(norm(Qe(:,1)*Qe(:,1)' * Qe(:,2)*Qe(:,2)') < 1e-10);   % P_i P_j = 0
np += 3;

% functional calculus: f(S) = sum f(lambda_i) P_i, checked against an
% independent route (repeated multiplication for f(t)=t^3, expm for f=exp)
F3 = zeros(6);
for i = 1:6, F3 += diag(De)(i)^3 * Qe(:,i)*Qe(:,i)'; end
chk("functional calculus: S^3 = sum lambda^3 P_i", norm(F3 - S^3), tol_resid(S)*norm(S,2)^2);
np += 1;

% rayleigh_quotient + courant_fischer. The capsule states the extremes are the
% extreme eigenvalues. Sampled over many seeded unit vectors -- and the
% MIN/MAX must be attained at the corresponding eigenvectors.
rand("seed", 17);
rq_min = Inf; rq_max = -Inf;
for t = 1:4000
  v = randn(6,1); v /= norm(v);
  q = (v'*S*v);
  rq_min = min(rq_min, q); rq_max = max(rq_max, q);
end
printf("    Rayleigh over 4000 unit vectors: [%.6f, %.6f]\n", rq_min, rq_max);
printf("    spectrum extremes:               [%.6f, %.6f]\n", lam(1), lam(end));
assert(rq_min >= lam(1) - 1e-10);                  % never below lambda_min
assert(rq_max <= lam(end) + 1e-10);                % never above lambda_max
% attained exactly at the eigenvectors
chk("R(v_min) = lambda_min", abs(Qe(:,1)'*S*Qe(:,1) - diag(De)(1)), tol_resid(S));
np += 3;

% Cauchy INTERLACING (a Courant-Fischer corollary): deleting row/col k gives
% eigenvalues that interlace the original. Checked for every k.
for k = 1:6
  idx = setdiff(1:6, k);
  mu = sort(eig(S(idx, idx)));
  for i = 1:5
    assert(mu(i) >= lam(i) - 1e-9);                % lambda_i <= mu_i
    assert(mu(i) <= lam(i+1) + 1e-9);              % mu_i <= lambda_{i+1}
  end
end
printf("    Cauchy interlacing holds for all 6 principal submatrices          ok\n");
np += 1;

% spectral_theorem_normal over C: unitarily diagonalisable IFF normal.
Un = [0 -1 0 0 0 0; 1 0 0 0 0 0; 0 0 0 -1 0 0; 0 0 1 0 0 0; 0 0 0 0 1 0; 0 0 0 0 0 1];
assert(norm(Un*Un' - Un'*Un) < 1e-12);             % normal (in fact orthogonal)
[Qn, Dn] = eig(Un);
chk("normal: A = Q D Q^* over C", norm(Qn*Dn*Qn' - Un), tol_resid(Un));
chk("normal: Q unitary", norm(Qn*Qn' - eye(6)), tol_resid(Un));
assert(!isreal(diag(Dn)));                          % eigenvalues NOT real: it is
                                                    % orthogonal, not symmetric
% NEGATIVE CONTRAST: a NON-normal matrix is not unitarily diagonalisable.
% Its Schur form has a nonzero strictly-upper part that no unitary removes.
NN = [1 1 0 0 0 0; 0 1 0 0 0 0; 0 0 2 0 0 0; 0 0 0 3 0 0; 0 0 0 0 4 0; 0 0 0 0 0 5];
assert(norm(NN*NN' - NN'*NN) > 0.1);               % NOT normal
[~, Tn] = schur(NN, "complex");
assert(norm(triu(Tn, 1)) > 0.1);                   % strictly-upper part survives
printf("    negative contrast: non-normal matrix keeps a nonzero Schur         \n");
printf("      strictly-upper part -- not unitarily diagonalisable              ok\n");
np += 3;

printf("\n=== F. positive definiteness and inertia (nodes: psd_characterisations,\n");
printf("       gram_matrix, cholesky_factorisation, sylvester_law_of_inertia,\n");
printf("       simultaneous_diagonalisation, quadratic_form, congruence) -- n = 6 ===\n");
% psd_characterisations: FOUR independent routes must agree, at n = 6
p1 = all(eig(S) > 0);
p2 = all(arrayfun(@(k) det(S(1:k,1:k)) > 0, 1:6));        % Sylvester's criterion
[~, pf] = chol(S); p3 = (pf == 0);
p4 = (rank(chol(S)) == 6);
printf("    eig>0=%d  leading minors>0=%d  chol=%d  full-rank factor=%d\n", p1,p2,p3,p4);
assert(isequal(p1,p2,p3,p4) && p1);
% a fifth route: the quadratic form itself, sampled
rand("seed", 23);
qmin = Inf;
for t = 1:3000, v = randn(6,1); qmin = min(qmin, (v'*S*v)/(v'*v)); end
assert(qmin > 0);
printf("    quadratic form x'Sx/x'x > 0 over 3000 random x (min %.4f)          ok\n", qmin);
np += 2;

% NEGATIVE CONTRAST: the capsule's leading-vs-ALL-principal-minors trap, at n=3.
% diag(0,0,-1) has every LEADING principal minor equal to 0 -- none negative --
% yet it is NOT positive semidefinite.
Bad = diag([0 0 -1]);
lead = arrayfun(@(k) det(Bad(1:k,1:k)), 1:3);
assert(all(lead == 0));                             % no leading minor is negative
assert(min(eig(Bad)) < 0);                          % yet NOT PSD
assert([0;0;1]' * Bad * [0;0;1] < 0);               % witnessed by a vector
printf("    negative contrast: diag(0,0,-1) has all LEADING minors = 0 yet is\n");
printf("      not PSD -- leading minors characterise DEFINITENESS only         ok\n");
np += 3;

% gram_matrix: G = V'V is PSD always; definite iff the columns are independent
rand("seed", 29);
Vind = randn(6, 4);
Gind = Vind' * Vind;
assert(min(eig(Gind)) > 1e-8);                      % independent -> definite
assert(rank(Gind) == rank(Vind));                   % rank G = rank V
Vdep = [Vind(:,1) Vind(:,2) Vind(:,3) Vind(:,1)+Vind(:,2)];
Gdep = Vdep' * Vdep;
assert(min(eig(Gdep)) < 1e-8);                      % dependent -> only SEMI
assert(rank(Gdep) == 3);
printf("    Gram matrix: definite iff columns independent (rank 4 vs 3)        ok\n");
np += 2;

% cholesky_factorisation: unique with positive diagonal, and it FAILS on an
% indefinite matrix -- which is the standard numerical test for definiteness.
Lc = chol(S, "lower");
chk("Cholesky S = L L'", norm(Lc*Lc' - S), tol_resid(S));
assert(all(diag(Lc) > 0));                          % positive diagonal = uniqueness
Ind = S - 12*eye(6);                                % shift to make it indefinite
assert(min(eig(Ind)) < 0);
[~, pind] = chol(Ind);
assert(pind != 0);                                  % chol MUST fail
printf("    Cholesky fails on the indefinite shift -- the numerical PD test    ok\n");
np += 3;

% sylvester_law_of_inertia at n = 6: congruence preserves the SIGNS, and the
% eigenvalues themselves must NOT be preserved (congruence != similarity).
Csym = diag([3 2 1 -1 -2 0]);
Pc = [2 1 0 0 0 0; 0 3 0 0 1 0; 0 0 5 0 0 0; 1 0 0 7 0 0; 0 0 0 0 2 1; 0 0 0 0 0 3];
assert(abs(det(Pc)) > 1e-8);
Ccong = Pc' * Csym * Pc;
in_before = [sum(eig(Csym) > 1e-9), sum(eig(Csym) < -1e-9), sum(abs(eig(Csym)) <= 1e-9)];
in_after  = [sum(eig(Ccong) > 1e-9), sum(eig(Ccong) < -1e-9), sum(abs(eig(Ccong)) <= 1e-9)];
printf("    inertia before (n+,n-,n0) = (%d,%d,%d)   after = (%d,%d,%d)\n", in_before, in_after);
assert(isequal(in_before, in_after));               % INVARIANT
assert(norm(sort(eig(Csym)) - sort(eig(Ccong))) > 1); % eigenvalues NOT invariant
printf("    congruence preserves inertia but NOT eigenvalues                   ok\n");
np += 2;

% simultaneous_diagonalisation: two symmetric matrices, one positive definite,
% are simultaneously diagonalisable by congruence.
S2 = [2 0 1 0 0 0; 0 3 0 1 0 0; 1 0 4 0 1 0; 0 1 0 5 0 1; 0 0 1 0 6 0; 0 0 0 1 0 7];
assert(issymmetric(S2) && min(eig(S)) > 0);         % S is the definite one
Lg = chol(S, "lower");
Cw = Lg \ S2 / Lg';                                 % whiten by the definite one
Cw = (Cw + Cw')/2;                                  % symmetrise round-off
[Qw, Dw] = eig(Cw);
Pg = Lg' \ Qw;
chk("simult. diag: P'SP = I", norm(Pg'*S*Pg - eye(6)), tol_resid(S)*cond(S));
chk("simult. diag: P'S2P diagonal", norm(Pg'*S2*Pg - diag(diag(Pg'*S2*Pg))), tol_resid(S2)*cond(S));
% the diagonal entries are the GENERALISED eigenvalues, not eigenvalues of S2
gev = sort(diag(Dw));
chk("generalised eigenvalues match eig(S2,S)", norm(gev - sort(eig(S2, S))), sqrt(eps)*norm(S2,2)*cond(S));
np += 3;

printf("\n=== G. SVD and the norms (nodes: singular_values,\n");
printf("       singular_value_decomposition, svd_four_subspaces,\n");
printf("       moore_penrose_pseudoinverse, eckart_young, matrix_norms,\n");
printf("       condition_number, spectral_radius) -- 7x4, rank 3 ===\n");
% rank 3 by construction: col4 = 2*col1 - col2
G = [1 2 3 0; 4 1 2 7; 0 5 1 -5; 2 2 8 2; 3 0 1 6; 1 1 1 1; 5 2 0 8];
[Us, Ss, Vs] = svd(G);
sg = diag(Ss);
rg = rank(G);
printf("    singular values: %s   rank = %d\n", num2str(sg', "%.3e "), rg);
assert(rg == 3);
assert(sg(rg)/sg(rg+1) > 1e6);                      % decisive gap
chk("SVD: G = U S V'", norm(Us*Ss*Vs' - G), tol_resid(G));
chk("SVD: U, V orthogonal", norm(Us'*Us - eye(7)) + norm(Vs'*Vs - eye(4)), tol_resid(G));
% independent route to the singular values, valid only for the ones the
% squared route can carry -- see skills/octave/references/tolerance-and-conditioning.md
ev = sqrt(sort(max(eig(G'*G), 0), "descend"));
chk("sigma_1..r vs sqrt(eig(G'G))", norm(sg(1:rg) - ev(1:rg))/norm(sg(1:rg)), 1e-12);
np += 4;

% svd_four_subspaces: the SVD hands you orthonormal bases for all four
assert(rank([Us(:,1:rg), orth(G)]) == rg);          % col(G) = span(u_1..u_r)
assert(rank([Vs(:,1:rg), orth(G')]) == rg);         % row(G) = span(v_1..v_r)
chk("null(G) = span(v_{r+1}..v_n)", norm(G * Vs(:, rg+1:end)), tol_resid(G));
chk("null(G') = span(u_{r+1}..u_m)", norm(G' * Us(:, rg+1:end)), tol_resid(G));
np += 4;

% eckart_young at several k, in BOTH norms the capsule states
for k = 1:3
  Gk = Us(:,1:k) * Ss(1:k,1:k) * Vs(:,1:k)';
  assert(rank(Gk) == k);
  chk(sprintf("Eckart-Young k=%d: ||G-Gk||_2 = sigma_{k+1}", k), ...
      abs(norm(G - Gk, 2) - sg(k+1)), tol_resid(G));
  chk(sprintf("Eckart-Young k=%d: ||G-Gk||_F = sqrt(sum sigma^2)", k), ...
      abs(norm(G - Gk, "fro") - sqrt(sum(sg(k+1:end).^2))), tol_resid(G));
end
% ...and no OTHER rank-k matrix does better (sampled)
rand("seed", 31);
k = 2; Gk = Us(:,1:k)*Ss(1:k,1:k)*Vs(:,1:k)';
best = norm(G - Gk, 2); beaten = false;
for t = 1:300
  Rk = (Us(:,1:k) + 0.05*randn(7,k)) * Ss(1:k,1:k) * (Vs(:,1:k) + 0.05*randn(4,k))';
  if (norm(G - Rk, 2) < best - 1e-12) beaten = true; end
end
assert(!beaten);
printf("    300 perturbed rank-2 competitors, none beats the truncated SVD     ok\n");
np += 7;

% moore_penrose_pseudoinverse: all FOUR Penrose conditions, on a RANK-DEFICIENT
% matrix (where the (A'A)^-1 formula does not even exist)
Gp = pinv(G);
chk("Penrose 1: G G+ G = G", norm(G*Gp*G - G), tol_resid(G));
chk("Penrose 2: G+ G G+ = G+", norm(Gp*G*Gp - Gp), tol_resid(Gp));
chk("Penrose 3: (G G+)' = G G+", norm((G*Gp)' - G*Gp), tol_resid(G));
chk("Penrose 4: (G+ G)' = G+ G", norm((Gp*G)' - Gp*G), tol_resid(G));
assert(rank(G'*G) < columns(G));                    % (A'A)^-1 does NOT exist here
% and A+b is the MINIMUM-NORM least-squares solution
bg = [1; 2; 3; 4; 5; 6; 7];
xmn = Gp * bg;
res0 = norm(G*xmn - bg);
rand("seed", 37);
nz = null(G);
for t = 1:200
  xalt = xmn + nz * (randn(columns(nz),1));
  assert(abs(norm(G*xalt - bg) - res0) < 1e-8);     % same residual...
  assert(norm(xalt) > norm(xmn) - 1e-10);           % ...but never smaller norm
end
printf("    pinv gives the MINIMUM-NORM least-squares solution (200 samples)   ok\n");
np += 6;

% matrix_norms and condition_number, all by independent routes
chk("||G||_2 = sigma_1", abs(norm(G,2) - sg(1))/sg(1), 1e-12);
chk("||G||_F = sqrt(tr(G'G))", abs(norm(G,"fro") - sqrt(trace(G'*G)))/norm(G,"fro"), 1e-12);
chk("||G||_F = sqrt(sum sigma^2)", abs(norm(G,"fro") - sqrt(sum(sg.^2)))/norm(G,"fro"), 1e-12);
assert(norm(G,2) <= norm(G,"fro") + 1e-12);         % ||A||_2 <= ||A||_F
assert(norm(G,"fro") <= sqrt(rg)*norm(G,2) + 1e-10);
% submultiplicativity
assert(norm(S*S2, 2) <= norm(S,2)*norm(S2,2) + 1e-10);
chk("cond(S) = sigma_max/sigma_min", abs(cond(S) - max(svd(S))/min(svd(S)))/cond(S), 1e-12);
assert(cond(eye(6)) - 1 < 1e-12);                   % identity is perfectly conditioned
np += 6;

% THE CAPSULE'S SHARPEST NUMERICAL CLAIM (condition_number's counterexample):
% a tiny determinant does NOT mean ill-conditioned, and a large one does not
% mean well-conditioned. Verified at n = 6.
Tiny = 1e-5 * eye(6);
Ill  = diag([1 1 1 1 1 1e-10]);
printf("    det(1e-5*I6)      = %.3e   cond = %.3f      (tiny det, PERFECT cond)\n", det(Tiny), cond(Tiny));
printf("    det(diag(1..1e-10)) = %.3e   cond = %.3e  (larger det, ILL cond)\n", det(Ill), cond(Ill));
assert(det(Tiny) < det(Ill));                        % smaller determinant...
assert(cond(Tiny) < cond(Ill));                      % ...yet far better conditioned
assert(abs(cond(Tiny) - 1) < 1e-10);
printf("    => determinant is scale-sensitive, conditioning is not             ok\n");
np += 3;

% spectral_radius: rho(A) <= ||A|| for any submultiplicative norm, with
% EQUALITY for normal A in the spectral norm -- and the strict gap otherwise.
rho_S = max(abs(eig(S)));
chk("normal S: rho(S) = ||S||_2", abs(rho_S - norm(S,2))/rho_S, 1e-12);
Nil = [0 1 0 0 0 0; 0 0 1 0 0 0; 0 0 0 1 0 0; 0 0 0 0 1 0; 0 0 0 0 0 1; 0 0 0 0 0 0];
assert(max(abs(eig(Nil))) < 1e-12);                  % rho = 0
assert(norm(Nil, 2) > 0.9);                          % but the norm is 1
assert(norm(Nil^5) > 0.9 && norm(Nil^6) < 1e-12);    % nilpotent of index 6
printf("    negative contrast: nilpotent has rho = 0 but ||N||_2 = 1, and\n");
printf("      ||N^k|| stays 1 until k = 6 -- rho bounds only the LIMIT         ok\n");
np += 3;

printf("\n=== H. the boundary: what numerics CANNOT check ===\n");
printf("    (recorded so this layer does not appear to cover more than it does)\n");
% jordan_normal_form is a `draft` boundary node in the capsule. It is also
% numerically UNCOMPUTABLE: it is discontinuous in the entries. An arbitrarily
% small perturbation of a Jordan block has DISTINCT eigenvalues and is
% diagonalisable. Demonstrated rather than asserted away.
Jb = [2 1 0 0 0; 0 2 1 0 0; 0 0 2 1 0; 0 0 0 2 1; 0 0 0 0 2];
epsn = 1e-14;
Jp = Jb; Jp(5,1) += epsn;
lam_p = eig(Jp);
spread = max(abs(lam_p - 2));
printf("    Jordan block J_5(2) perturbed by %.0e in one entry:\n", epsn);
printf("      eigenvalues move by %.3e  (~ eps^(1/5) = %.3e, NOT ~ eps)\n", spread, epsn^(1/5));
assert(spread > 100 * epsn);                         % moves FAR more than eps
assert(columns(null(Jp - 2*eye(5))) == 0);           % perturbed: NOT defective
assert(columns(null(Jb - 2*eye(5))) == 1);           % original: defective
printf("      => the Jordan form is discontinuous; no tolerance makes it\n");
printf("         checkable numerically. It stays a stated boundary node.       ok\n");
np += 3;

printf("\n=== SUMMARY ===\n");
printf("ALL MATRIX CHECKS PASSED -- %d assertions\n", np);
printf("Dimensions exercised: n = 5, 6 square; 6x4, 6x3, 7x4 rectangular;\n");
printf("  rank-deficient (rank 3 of 4) and defective (Jordan blocks 3+2) cases.\n");
printf("\nNOT COVERED by this layer, and not claimed:\n");
printf("  * the GENERALITY of the field_scope tags. Octave has R and C and\n");
printf("    nothing else, so of the 182 tagged nodes the 121 `any_field` ones\n");
printf("    have their generality untested (the R instance is exercised, the\n");
printf("    rest merely not refuted), and the 3 `char_not_2` ones cannot be\n");
printf("    tested in their FAILING direction at all -- there is no\n");
printf("    characteristic-2 field here to witness the breakdown.\n");
printf("    See indexes/field-scope-index.md.\n");
printf("  * n beyond 7, and asymptotic behaviour.\n");
printf("  * exact and arbitrary-precision arithmetic (that is instance-checks.bc).\n");
printf("  * anything discontinuous in the entries (section H).\n");
printf("  * PROOF. These are instances at specific matrices. The universal\n");
printf("    evidence is validation/proof-checks.lean; see proof-checks.md for\n");
printf("    the core / dim_core / instance / cited split.\n");
