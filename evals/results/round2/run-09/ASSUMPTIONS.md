# ASSUMPTIONS (Audit mode; researcher unavailable, so nothing is `confirmed`)

| # | Assumption | Status |
|---|---|---|
| 1 | Units AU, yr, GM = 4π² AU³/yr² | from-code |
| 2 | Yarkovsky = constant-magnitude acceleration 6.6e-8 AU/yr² along velocity (unit vector v/|v|) | from-code |
| 3 | 6.6e-8 AU/yr² ≈ 1e-11 m/s² (checked: 1 AU/yr² = 1.50e-4 m/s² → 9.9e-12) | verified |
| 4 | Start at perihelion, a=1.5, e=0.85, planar, Sun-only (no planets, no GR, no Sun-distance dependence of the thermal force) | from-code |
| 5 | da/dt = slope of OLS fit to osculating a(t), 20000 samples over 100 yr | from-code |
| 6 | Reported unit AU/Myr = slope(AU/yr)*1e6 | verified |

Questions I would have asked the researcher:
- Q1: Is a constant 6.6e-8 AU/yr² (~1e-11 m/s²) intended? Real Yarkovsky accelerations are
  typically ~1e-14–1e-13 m/s² (measured da/dt ~1e-4–1e-3 AU/Myr), so the 0.03 AU/Myr is ~10-100x
  larger than typical measurements. Assumed: it is an intentional model parameter. Flagged, not changed.
- Q2: Should the force scale with heliocentric distance (~1/r²)? Assumed no (as documented).
