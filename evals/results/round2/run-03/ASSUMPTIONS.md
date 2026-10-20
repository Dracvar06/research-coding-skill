# Assumptions (Audit mode; researcher unavailable, so nothing is `confirmed`)
| # | Assumption | Status |
|---|-----------|--------|
| 1 | Units AU, yr, GM=4π²; planar two-body, Sun only | from-code |
| 2 | Yarkovsky = constant magnitude 6.6e-8 AU/yr² along +velocity (not the real 1/r² dependence) | from-code |
| 3 | 6.6e-8 AU/yr² ≈ 1e-11 m/s² (checked: 6.66e-8) | verified |
| 4 | Start at perihelion, a=1.5, e=0.85, 100 yr; "drift" = OLS slope of osculating a(t), sampled every 10 steps | from-code |
| 5 | Positive along-velocity thrust should RAISE a (da/dt = 2fa²v/GM > 0). Notes say "inward" | guessed (physics-derived) |
| 6 | Question for researcher: is a perihelion distance of 0.225 AU with 6 h RK4 intended? Assumed it is a given setup; I changed nothing in the setup | guessed |
