# Verification report

**Headline (NOTES.md): da/dt = −0.034 AU/Myr — INCORRECT. Corrected: da/dt ≈ +0.0302 AU/Myr (outward).**

| Check | Result | Strength |
|---|---|---|
| Control, thrust = 0 (a must be constant) using analysis.py as-is | slope −0.0637 AU/Myr, should be 0 → FAIL | known answer |
| Analytic orbit-averaged drift, da/dt = 2a²vf/GM averaged over mean anomaly | +0.03018 AU/Myr | known answer |
| Independent DOP853 (rtol 1e-12), same model | +0.03017 AU/Myr (control f=0: −3e-6 ≈ 0) | independent, agrees with analytic |
| analysis.py with step 1.5 h / 0.6 h | +0.0301 / +0.0302 | convergence |
| analysis.py with 6 h step (as submitted) | −0.0335 | wrong |

## Cause
Fixed 6 h RK4 step is far too coarse at perihelion (q = 0.225 AU, v ≈ 18 AU/yr, e = 0.85).
RK4 is dissipative: it systematically loses orbital energy, so a decreases by ≈ −0.064 AU/Myr (the f=0 control),
which exceeds and flips the sign of the true +0.030 AU/Myr signal. Physically, a prograde along-velocity
force adds energy (dE/dt = f·v > 0), so a cannot drift inward.

## Disagreements
Only one: submitted code vs. analytic/DOP853; resolved as numerical-error bug above.

## Remaining guessed assumptions
See ASSUMPTIONS.md #7 (model intent). Only a single critical module (integrator) was checked;
independent versions were scipy DOP853 and the analytic formula.

## Suggested fix
Use step ≲ 1.5 h (converged to ~0.0302) or an adaptive/symplectic-aware integrator; add the f=0 control as a test.
