**The result in NOTES.md is wrong.** The correct value is about **da/dt = +0.030 AU/Myr**, an outward drift. NOTES.md says −0.034 AU/Myr, inward.

**What is wrong:** the physics in `analysis.py` is right, but the integration is not accurate enough. With a 6-hour RK4 step, the asteroid's very close perihelion passage (q = 0.225 AU) produces a numerical energy loss. That loss lowers the fitted a(t) by about 0.064 AU/Myr, which is larger than the real +0.030 AU/Myr signal and opposite in sign.

**The evidence:**
- **Null control:** with the thrust set to zero, `analysis.py` should give no drift but gives **−0.0637 AU/Myr**. That error is purely numerical.
- **Convergence:** with the thrust back on, shrinking the step gives +0.0302 AU/Myr at 1 h and +0.0301 AU/Myr at 0.25 h. These were shorter runs, 30 and 10 years. The zero-thrust control also drops to 0.0000 at 1 h.
- **Independent integrator:** scipy's DOP853 at tight tolerance, run over the full 100 years, gives +0.03017 AU/Myr.
- **Analytic check:** orbit-averaging the standard formula for thrust along the velocity, da/dt = 2fa²v/GM, gives +0.03018 AU/Myr. A thrust along the velocity should raise a, which is another reason the inward sign could not be right.

**For the paper:**
- Use a step of 1 hour or smaller, or an adaptive integrator.
- Run the zero-thrust control (a should stay constant) before trusting any drift number.
- Report +0.030 AU/Myr.

**Assumptions I could not check with you:**
- I took the setup as given: the orbit, the constant-magnitude thrust, and the linear-fit definition of the drift.
- A real Yarkovsky acceleration falls off roughly as 1/r², so the constant-thrust model would give a different number than a physical one. I didn't examine that.
- I made no changes to `analysis.py`.

Files are in `/tmp/claude-0/-home-user/f0022ab6-33dd-5702-9526-8ac996d696c5/scratchpad/round2/runs/run-03`:
- `VERIFICATION.md`
- `ASSUMPTIONS.md`
- `verify/check.py`
- `verify/rk4_variants.py`
