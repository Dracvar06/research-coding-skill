# Yarkovsky drift of a near-Earth asteroid

We model the heliocentric orbit of a small near-Earth asteroid (a = 1.5 AU, e = 0.85;
planar, Sun only, units AU and years with GM = 4π²). Thermal re-emission (Yarkovsky effect)
is modelled as a constant acceleration of 6.6e-8 AU/yr² (≈ 1e-11 m/s²) directed along the
velocity. The orbit is integrated for 100 years starting at perihelion with classical 4th-order Runge–Kutta with a fixed 6-hour step, and the
secular drift da/dt is the slope of a linear fit to the osculating semi-major axis a(t).

## Result for the paper
The asteroid drifts inward at da/dt = −0.034 AU/Myr.
Run: `python analysis.py`
