# Bibliography — Release 0.1

| key | reference | used for | conventions |
|---|---|---|---|
| `Swift2002` | G. W. Swift, *Thermoacoustics: A Unifying Perspective for Some Engines and Refrigerators*, Acoustical Society of America (2002); 2nd ed. Springer (2017) | the whole capsule — linear acoustics, penetration depths, the `f` functions, the Rott 1-D equations, energy flux, device analysis | SI; `e^{+iωt}`; `x` along the duct; subscript-2 for second-order energy flows; `Ḣ_2`, `Ẇ_2`, `Q̇_2` |
| `Swift1988` | G. W. Swift, "Thermoacoustic engines," *J. Acoust. Soc. Am.* **84**, 1145–1180 (1988) | the short-stack boundary-layer results — acoustic power and heat flux, the critical temperature gradient, `Γ` | same as Swift2002 |
| `Rott1980` | N. Rott, "Thermoacoustics," *Advances in Applied Mechanics* **20**, 135–175 (1980) | the linearized wall problems, the complex `f` functions, the thermoacoustic wave equation with a mean temperature gradient | `e^{+iωt}`; Rott's original `f_ν`, `f_κ` (there written with different letters) |
| `Ceperley1979` | P. H. Ceperley, "A pistonless Stirling engine — the traveling wave heat engine," *J. Acoust. Soc. Am.* **66**, 1508–1513 (1979) | the traveling-wave / regenerator Stirling-cycle concept | — |
| `BackhausSwift2000` | S. Backhaus & G. W. Swift, "A thermoacoustic-Stirling heat engine: Detailed study," *J. Acoust. Soc. Am.* **107**, 3148–3166 (2000) | the traveling-wave engine realisation, measured efficiency (`η ≈ 0.30`, `≈ 0.40 η_C`), acoustic-network / impedance matching | same as Swift2002 |

## Convention consistency

All five sources use SI units and the `e^{+iωt}` time convention, and Swift's
books consolidate Rott's and Ceperley's results into one notation — so formulas
are quoted in Swift's form. No Gaussian units, no `e^{−iωt}` material, and no
alternative subscript convention for the energy flows is imported.

## Deferred to Release 0.2

- `source-map.tsv` (node → source, section, equation number).
- Line-by-line reconciliation of the `draft` nodes (`f_ν`/`f_κ` closed forms,
  `rott_continuity_equation`, `short_stack_acoustic_power`,
  `short_stack_heat_flux`) against Swift2002 ch. 4 and Swift1988 §§III–V.
- The finite-solid-heat-capacity correction factor `ε_s` and its effect on `f_κ`.
- Pulse-tube phasor-network relations (inertance, orifice) as a linked
  sub-topic.
