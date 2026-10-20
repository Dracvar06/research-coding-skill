# Assumptions (Audit mode; researcher unavailable, so all are `from-code` or `guessed`)

| # | Assumption | Status |
|---|---|---|
| 1 | Units AU, yr, GM = 4π² | from-code |
| 2 | Planar two-body, Sun only, no planets/GR | from-code |
| 3 | Yarkovsky = constant-magnitude 6.6e-8 AU/yr² along +velocity (always prograde thrust) | from-code |
| 4 | 6.6e-8 AU/yr² ≈ 1e-11 m/s² (checked: 1 AU/yr² = 1.5e-4 m/s², so ≈ 9.9e-12) | verified |
| 5 | Start at perihelion, a=1.5, e=0.85 (q = 0.225 AU), 100 yr | from-code |
| 6 | da/dt = slope of linear fit to osculating a(t), sampled every 10 steps | from-code |
| 7 | Quantity to report: the true secular drift of the model in NOTES.md (not of the RK4 discretisation) | guessed (question for researcher: is a purely along-velocity constant acceleration really the intended model? Assumed yes, as NOTES says) |
| 8 | "AU/Myr" = slope(AU/yr) × 1e6 | from-code |
