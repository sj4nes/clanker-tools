# Base dimensions and quantity table

## Basis

`[M L T Θ N]` — mass, length, time, thermodynamic temperature, amount of
substance. (No electric current `I` or luminous intensity in this release.)

Energy is `M L^2 T^-2`; it enters from mechanics and is treated as a primitive
physical quantity here.

## Quantity → dimension

| Quantity | Symbol | SI unit | Dimension |
|---|---|---|---|
| energy / internal energy / heat / work | `E, U, Q, W` | J | `M L^2 T^-2` |
| temperature | `T` | K | `Θ` |
| pressure | `P` | Pa | `M L^-1 T^-2` |
| volume | `V` | m³ | `L^3` |
| amount of substance | `n` | mol | `N` |
| universal gas constant | `R` | J mol⁻¹ K⁻¹ | `M L^2 T^-2 Θ^-1 N^-1` |
| molar heat capacity | `c_v, c_p` | J mol⁻¹ K⁻¹ | `M L^2 T^-2 Θ^-1 N^-1` |
| heat capacity (extensive) | `C` | J K⁻¹ | `M L^2 T^-2 Θ^-1` |
| entropy (extensive) | `S` | J K⁻¹ | `M L^2 T^-2 Θ^-1` |
| molar entropy | `s` | J mol⁻¹ K⁻¹ | `M L^2 T^-2 Θ^-1 N^-1` |
| heat-capacity ratio | `γ` | — | `1` |
| efficiency / COP | `η`, `COP` | — | `1` |
| Joule–Thomson coefficient | `μ_JT` | K Pa⁻¹ | `M^-1 L T^2 Θ` |
| Helmholtz / Gibbs free energy | `F, G` | J | `M L^2 T^-2` |

The `bc` worksheet `validation/dimensional-checks.bc` tracks each quantity as a
five-tuple of lowercase exponents `(m, l, t, h, n)` — `h` for `Θ`, `n` for `N` —
and prints `0 0 0 0 0` when `[LHS] − [RHS]` is consistent.
