# Verification: Yarkovsky da/dt

**Headline:** NOTES.md claim da/dt = +0.030 AU/Myr is CORRECT (code gives 0.0302; more precisely 0.0302 AU/Myr).

| Check | Result | Strength |
|---|---|---|
| Independent analytic (Gauss eq., da/dt = 2a²f·v/GM, averaged over mean anomaly via Kepler solver) | 0.03018 AU/Myr vs code 0.0302 | Strong (independent, first principles) |
| Unit conversion 1e-11 m/s² -> AU/yr² | 6.66e-8 (notes use 6.6e-8; 0.9% low, consistent with "≈") | Strong |
| Sign/direction: a increases when thrust along +v | a(100yr)-a(0)=+3e-6 AU | Strong |
| Integrator/tolerance convergence (own re-run, t_eval grid, DOP853) rtol 1e-12 -> 0.030172, rtol 1e-13 -> 0.030174 | converged to ~1e-4 relative | Moderate |
| Energy conservation / f=0 control, f-doubling, Radau cross-check | NOT completed (Radau too slow, tool limits) | skipped |

Disagreements found: none. Only one independent check was run (no multi-agent versions), budget-limited.
Guessed assumptions: see ASSUMPTIONS.md (#3, #5); neither changes the 2-sig-fig result.
Minor: if quoting 3 s.f., use 0.030 (0.0302 with f=6.6e-8; 0.0305 with the exact 1e-11 m/s² conversion).
