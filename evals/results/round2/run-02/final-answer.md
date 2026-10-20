**The result in NOTES.md is wrong.** The asteroid drifts outward, not inward, and the drift is about +0.030 AU/Myr, not −0.034 AU/Myr.

**What is wrong**
- **Integration error:** `analysis.py` integrates with fixed-step RK4 at 6 hours. With e = 0.85 the perihelion is only 0.225 AU, so this step is too coarse. The numerical error alone makes a(t) drift by about −0.064 AU/Myr. I confirmed this by running the script with the Yarkovsky term set to zero. The true drift in that case is zero, but the script still gives −0.0637 AU/Myr.
- **Sign:** The reported −0.034 AU/Myr is the real signal plus that spurious −0.064 AU/Myr. An acceleration directed along the velocity adds energy, so the semi-major axis must grow. The "inward" conclusion comes entirely from the numerical error.
- **Units are fine:** 1e-11 m/s² does convert to 6.6e-8 AU/yr², so no change is needed there.

**Corrected result**
- A tight-tolerance integration (DOP853, rtol 1e-13) gives da/dt = **+0.0302 AU/Myr**. With the thrust set to zero it gives about −1.7e-7 AU/Myr, which is zero within precision.
- An independent orbit-averaged analytic formula gives +0.03018 AU/Myr, which agrees.
- Over 100 years, a grows by about 3.0e-6 AU.

**Suggested fix:** replace the integrator with an adaptive high-order one such as `scipy.integrate.solve_ivp` with DOP853 and tight tolerances. Alternatively, keep RK4 with a much smaller step, or one that adapts near perihelion. Then change the NOTES.md line to "The asteroid drifts outward at da/dt ≈ +0.030 AU/Myr."

**Assumptions**
- I took the setup in NOTES.md as intended: planar, Sun only, perihelion start, thrust along the velocity.
- I treated the linear fit to a(t) as the definition of the drift.
- I did not edit your files.

My checks are in `/tmp/claude-0/-tmp-claude-0--home-user-f0022ab6-33dd-5702-9526-8ac996d696c5-scratchpad-round2-runs-run-02/f0022ab6-33dd-5702-9526-8ac996d696c5/scratchpad/chk.py`.
