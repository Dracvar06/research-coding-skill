# Assumptions (Audit mode; researcher unavailable, so nothing is "confirmed")
| # | Assumption | Status |
|---|---|---|
| 1 | Units AU, yr, GM=4π²; 6.6e-8 AU/yr² ≈ 9.9e-12 m/s² (checked, consistent with "≈1e-11 m/s²") | from-code, checked |
| 2 | Yarkovsky = constant magnitude along +velocity (prograde), as NOTES says | from-code |
| 3 | da/dt = least-squares slope of osculating a(t) sampled every 10 steps (60 h) over 100 yr | from-code |
| 4 | Planar, Sun-only, no GR/planets | from-code |
| 5 | Q (was to ask): is a 6 h RK4 step acceptable for e=0.85, q=0.225 AU? GUESS: not assumed; tested by convergence | guessed -> tested |
| 6 | Q: intended sign: prograde thrust should increase a. GUESS: NOTES text "inward" is the claim being audited | guessed |
