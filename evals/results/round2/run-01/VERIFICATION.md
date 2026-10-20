# Verification
**Headline claim (NOTES.md): da/dt = -0.034 AU/Myr (inward). INCORRECT.**
Corrected: da/dt = **+0.0302 AU/Myr (outward)**.

| Check | Result | Strength |
|---|---|---|
| Analytic: orbit-averaged Gauss/energy eq. da/dt = (2T/n)·<sqrt(1+2e cos f+e²)>/sqrt(1-e²) (independent, numeric average over mean anomaly) | +0.03018 AU/Myr | known answer (strong) |
| Independent integrator (scipy DOP853, rtol 1e-13), same setup | +0.030174 AU/Myr | independent version |
| analysis.py with step 0.03 h-scale (0.03 d = 0.72 h) | +0.0302 | convergence |
| analysis.py, T=0 (no thrust; a must be constant) at 6 h step | -0.0637 AU/Myr (spurious!) | null control FAILS |
| DOP853, T=0 | -1.5e-7 AU/Myr (≈0) | passes |
| analysis.py as given (6 h) | -0.0335 AU/Myr | |

**Cause:** the fixed 6 h RK4 step is too coarse for e=0.85 (perihelion 0.225 AU, speed ≈18 AU/yr). RK4 has a spurious secular energy loss
of about -0.064 AU/Myr, which is larger than and opposite to the physical +0.030 AU/Myr, so the sign flips. (-0.0637 + 0.0302 ≈ -0.0335.)
The physics (prograde thrust → a increases) agrees with the analytic result; the negative value is a numerical artifact, not an asteroid property.

**Fix:** use a much smaller step (or adaptive/high-order integrator) and add the T=0 control (a must stay constant) to the script.
Note NOTES.md also quotes the same result to 2 digits; the correct value to quote is +0.030 AU/Myr.

Remaining guessed assumptions: see ASSUMPTIONS.md (#5, #6). Files: verify/v2_dop853.py, verify/a_T0.py, verify/a_fine.py.
