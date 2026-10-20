The result in NOTES.md is wrong. The correct value is **da/dt = +0.030 AU/Myr**, an outward drift. NOTES.md has −0.034 AU/Myr, inward. This replaces the "about +0.07" figure in my earlier message, which came from an averaging shortcut that doesn't apply here.

**What's wrong**
- **Sign:** The Yarkovsky acceleration points along the velocity, so it adds energy and the semi-major axis should grow.
- **Cause of the −0.034:** It is numerical drift from the 6-hour RK4 step, which is too coarse for a perihelion of 0.225 AU. With the Yarkovsky term set to zero, `analysis.py` still gives −0.064 AU/Myr.

**How I checked the corrected value**
- **Convergence:** With the step divided by 8 and by 32, the fitted slope is +0.0302 AU/Myr both times, so it has converged.
- **Analytic check:** I averaged the exact expression for da/dt over the orbit, weighting by time. I used da/dt = 2T√(1+2e·cos f+e²)/(n√(1−e²)), where f is the true anomaly. This gives +0.0302 AU/Myr, matching the converged integration.

**Fix**
- Reduce the step in `analysis.py` to about 6 h / 8 or finer.
- Change the NOTES.md result to "drifts outward at da/dt ≈ +0.030 AU/Myr".
- I haven't edited either file.

**Assumptions**
- I took the setup in NOTES.md as intended: planar, Sun only, constant 6.6e-8 AU/yr² along the velocity, and a linear fit to osculating a(t) over 100 years.
- I treated 1e-11 m/s² ≈ 6.6e-8 AU/yr² as correct. I checked the conversion and it holds.

I left `check.py` (my test script) in the directory; delete it if you don't want it.
