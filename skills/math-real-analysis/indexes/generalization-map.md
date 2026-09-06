# Generalization / specialization map — Release 0.1

`A --generalizes--> B` : `A` is the more general statement; `B` is recovered as a
special case. Stored as `generalizes` / `special_case_of` in
`edges/relations.tsv` (never as `tsort` edges — that would put the general
result before the special one and often create a cycle).

```
cauchy_mean_value_theorem  --gen-->  mean_value_theorem  --gen-->  rolles_theorem
taylor_theorem             --gen-->  mean_value_theorem           (n = 1)
power_series               --gen-->  geometric_series             (a_n = 1, c = 0)
comparison_test            --gen-->  weierstrass_m_test           (in sup-norm)
uniform_continuity         --gen-->  continuity_on_set            (delta uniform in x)
uniform_convergence        --gen-->  pointwise_convergence        (N uniform in x)
abs_convergence_implies_convergence  --strengthens-->  series_convergence
ratio_test / root_test     --special_case_of-->  comparison_test  (geometric majorant)
```

## Out-of-scope generalizations (where Release 0.2+ would go)

| 0.1 node | generalizes to | added machinery |
|---|---|---|
| `heine_borel` | compactness in metric spaces; Tychonoff in general topology | metric / topological spaces |
| `bolzano_weierstrass` | sequential compactness of closed bounded sets in ℝⁿ; weak-* compactness | ℝⁿ; Banach–Alaoglu |
| `mean_value_theorem` | the MVT fails for vector-valued `f`; replaced by the MVT **inequality** | normed spaces |
| `riemann_integral` | the Lebesgue integral; the Riemann–Stieltjes integral | measure theory; functions of bounded variation |
| `ftc_part2` | fails for some bounded derivatives (Volterra); fixed by the Lebesgue / Henstock–Kurzweil integral | gauge integrals |
| `taylor_theorem` | multivariable Taylor; holomorphic Taylor (always convergent) | ℝⁿ; ℂ |
| `power_series` / `radius_of_convergence` | Laurent series; analytic continuation | complex analysis |
| `uniform_convergence` | the Arzelà–Ascoli theorem; equicontinuity; `C(K)` as a Banach space | function-space topology |

## Duals

```
supremum        <--dual-->  infimum          (inf A = -sup(-A))
limsup          <--dual-->  liminf           (liminf x_n = -limsup(-x_n))
open_set        <--dual-->  closed_set       (complementation)
```
