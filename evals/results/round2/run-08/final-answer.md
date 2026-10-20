**The result in NOTES.md is correct.** da/dt = +0.030 AU/Myr holds up. I made no changes to the files.

- **Rerun:** `python analysis.py` gives a(0) = 1.500000 AU and a(100 yr) = 1.500003 AU. The fitted slope is da/dt = 0.0302 AU/Myr, which rounds to the +0.030 in the notes.
- **Independent check:** For a constant along-velocity acceleration T, the instantaneous rate is da/dt = 2a²vT/GM. I averaged this over one orbit, using a Kepler-equation solution with a = 1.5 and e = 0.85. That gave 0.03018 AU/Myr, which matches the integrated value. The sign is also right, since thrust along the velocity raises a.
- **Units:** 6.6e-8 AU/yr² is about 9.9e-12 m/s², so the "≈ 1e-11 m/s²" in the notes is fine.
- **Code:**
  - The initial conditions are correct: perihelion at q = a(1−e), with perihelion speed √(GM(1+e)/q).
  - The semi-major axis comes from the vis-viva relation.
  - The slope comes from a linear fit to a(t) sampled at 20,000 points over 100 years, which covers about 54 orbits. The within-orbit oscillation in osculating a averages out, so the fit is not biased.

**Assumptions I made:**
- I read "AU/Myr" as AU per million years, which is what the code's ×1e6 conversion does.
- I did not question the 1e-11 m/s² acceleration. It is large for a real Yarkovsky effect on a km-scale body, but the notes present it as a model input, so I left it alone.

**Minor wording point:** you may want to quote 0.030 as "≈ 0.030" or give 0.0302, since the integrated value is 0.0302.
