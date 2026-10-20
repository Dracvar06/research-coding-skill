# Assumptions (Audit mode; researcher unavailable, so none are `confirmed`)

| # | Assumption | Status |
|---|---|---|
| 1 | Units AU, yr, GM = 4π² (Sun only, planar, no planets/GR) | from-code |
| 2 | Yarkovsky = constant-magnitude acceleration along v (f = 6.6e-8 AU/yr²) | from-code |
| 3 | 1e-11 m/s² ≈ 6.66e-8 AU/yr²; code/notes use 6.6e-8 (≈1% lower, i.e. 0.991e-11 m/s²) | guessed: rounding intended |
| 4 | Start at perihelion, a=1.5, e=0.85; "drift" = OLS slope of osculating a(t) over 100 yr | from-code |
| 5 | Question for researcher: is a 100-yr linear fit of osculating a acceptable vs. a longer baseline / orbit-averaged a? | guessed: yes (osculating oscillations are tiny relative to the trend) |
| 6 | Result quoted to 2 significant figures, no uncertainty | from-code |
