**The result in NOTES.md is wrong. The asteroid drifts outward at da/dt ≈ +0.030 AU/Myr, not inward at −0.034.**

**What's wrong.** The sign and size come from numerical error in the integration, not from the physics. The fixed 6-hour RK4 step is too coarse for e = 0.85. Perihelion is at 0.225 AU, where the speed is about 18 AU/yr. RK4 is not energy-conserving, so it leaks orbital energy and a(t) drifts downward on its own.

**Evidence**
- **No thrust:** with the Yarkovsky term set to zero, the 6 h step still gives da/dt = −0.063 AU/Myr. A real two-body orbit would give 0. With a 1 h step the spurious drift falls to about −8e-6.
- **Sign:** a thrust along the velocity adds energy, so a should increase. The code's own result (−0.034) has the wrong sign.
- **Analytic check:** the orbit-averaged Gauss equation for this setup gives +0.0302 AU/Myr. The 20-year runs with thrust give −0.0333 at 6 h and +0.0301 at 1 h.
- **Full run:** the 100-year run with a 1 h step gives +0.0302 AU/Myr (a goes from 1.500000 to 1.500003 AU). That matches the analytic value.

**Assumptions I made**
- I took the model as written in NOTES.md (planar, Sun only, constant 6.6e-8 AU/yr² along the velocity, start at perihelion). I did not change those.
- The acceleration conversion is fine: 1e-11 m/s² is about 6.66e-8 AU/yr².
- My analytic check uses the standard Gauss equation for da/dt with a purely along-track force.

**Fix before submitting.** Reduce the step in `analysis.py` to 1 h or smaller, or use an adaptive or symplectic integrator. Add a zero-thrust control run showing da/dt ≈ 0. Then change NOTES.md to say the asteroid drifts outward at da/dt ≈ +0.030 AU/Myr. I did not edit your files. My check script is in my scratchpad directory, not your project.
