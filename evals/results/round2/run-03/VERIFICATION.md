# Verification of the Yarkovsky drift result

**Claimed:** da/dt = -0.034 AU/Myr (inward). **Verdict: WRONG.** Correct: **da/dt ≈ +0.0302 AU/Myr (outward)**.

## Evidence
| Check | Result | Strength |
|---|---|---|
| Analytic Gauss equation, da/dt = 2 f a² v/GM, time-averaged over orbit | +0.03018 AU/Myr | known answer (strong) |
| Independent integrator (scipy DOP853, rtol 1e-12), same physics, 100 yr fit | +0.03017 AU/Myr | independent version (strong, agrees with analytic) |
| analysis.py with f=0 (null control; a must be constant) | **-0.0637 AU/Myr** | FAILS: pure integrator error |
| analysis.py f=6.6e-8, step 6 h | -0.0335 | reproduces notes' -0.034 |
| analysis.py f=6.6e-8, step 1 h (30 yr) | +0.0302 | converges to truth |
| analysis.py f=6.6e-8, step 0.25 h (10 yr) | +0.0301 | converged |
| analysis.py f=0, step 1 h | 0.0000 | integrator error gone |

## Cause
The physics in analysis.py is correct (thrust along +v raises a). The bug is numerical: fixed 6-hour RK4 is too coarse at perihelion (q=0.225 AU, e=0.85, speed ~ 12 AU/yr... period at perihelion is short), causing a spurious secular energy loss of about -0.064 AU/Myr in a(t), which is larger than and opposite to the physical +0.030 signal. The sign of the headline result is an integrator artifact.

## Fix / recommendation
Use a step of ≤1 h (or an adaptive/symplectic-aware integrator such as DOP853), and always run the f=0 control (a must stay constant). Report +0.030 AU/Myr.

## Caveats
- Assumption 6 and the constant-magnitude thrust model are taken as given (guessed/from-code). The real Yarkovsky acceleration scales ~1/r², which would change the number; not examined.
- Scripts: verify/check.py (scipy + analytic), verify/rk4_variants.py (step/thrust variants of the original code). analysis.py left unmodified.
