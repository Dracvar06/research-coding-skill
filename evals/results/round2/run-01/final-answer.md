**The result in NOTES.md is wrong.** The asteroid drifts outward at about **+0.030 AU/Myr**, not inward at −0.034 AU/Myr. The sign is wrong, and so is the magnitude, though only by about 10%.

**What's wrong:** the fixed 6-hour RK4 step is too coarse for this orbit. The perihelion is only 0.225 AU (e = 0.85), where the speed is about 18 AU/yr. At that step size RK4 loses energy numerically. I ran `analysis.py` with the thrust set to zero, where a must stay constant, and it drifted at −0.064 AU/Myr. That spurious drift is larger than the physical signal and has the opposite sign. Adding the two gives 0.0302 − 0.0637 ≈ −0.0335, which matches the −0.034 in NOTES.md. A thrust along the velocity should raise a, so an inward drift was the first sign something was off.

**Evidence for +0.0302 AU/Myr:**
- **Analytic orbit average:** the energy equation gives da/dt = (2T/n)·⟨√(1+2e cos f+e²)⟩/√(1−e²), which evaluates to +0.03018 AU/Myr.
- **Independent integrator:** SciPy's DOP853 with a tight tolerance gives +0.030174 AU/Myr. With no thrust it gives about 0 (−1.5e-7 AU/Myr), so it passes the control that your code fails.
- **Your own code, refined:** `analysis.py` with the step cut to about 0.7 hours gives +0.0302 AU/Myr.

The unit conversion (6.6e-8 AU/yr² ≈ 1e-11 m/s²) is fine.

**Fix:** use a much smaller step or an adaptive high-order integrator. Also add the zero-thrust check to the script. The value to report is +0.030 AU/Myr.

You weren't available, so the open questions are in ASSUMPTIONS.md with my guesses. Both are about the intended direction of the thrust (item 6 is the sign) and whether a 6-hour step was meant to be acceptable (item 5). The conclusion above doesn't depend on either: the zero-thrust control and the analytic result settle it.

Files are in the working directory:
- ASSUMPTIONS.md
- VERIFICATION.md
- verify/v2_dop853.py
- verify/a_T0.py
- verify/a_fine.py
