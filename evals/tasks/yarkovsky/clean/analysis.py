import numpy as np
from scipy.integrate import solve_ivp

GM_SUN = 4 * np.pi**2      # AU^3 / yr^2
A0, E0 = 1.5, 0.85         # initial semi-major axis (AU) and eccentricity
T_ALONG = 6.6e-8           # Yarkovsky along-track acceleration (AU / yr^2)
YEARS = 100.0


def accel(r, v):
    grav = -GM_SUN * r / np.linalg.norm(r) ** 3
    yark = T_ALONG * v / np.linalg.norm(v)
    return grav + yark


def deriv(t, state):
    r, v = state[:2], state[2:]
    return np.concatenate([v, accel(r, v)])


def semi_major_axis(state):
    r = np.linalg.norm(state[:2])
    v2 = state[2:] @ state[2:]
    return 1.0 / (2.0 / r - v2 / GM_SUN)


# start at perihelion
q = A0 * (1 - E0)
state0 = np.array([q, 0.0, 0.0, np.sqrt(GM_SUN * (1 + E0) / q)])

sol = solve_ivp(deriv, [0.0, YEARS], state0, method="DOP853",
                rtol=1e-12, atol=1e-14, dense_output=True)
t_out = np.linspace(0.0, YEARS, 20000)
a_out = np.array([semi_major_axis(sol.sol(t)) for t in t_out])

slope = np.polyfit(t_out, a_out, 1)[0]  # AU / yr
print(f"a(0) = {a_out[0]:.6f} AU, a({YEARS:.0f} yr) = {a_out[-1]:.6f} AU")
print(f"da/dt = {slope * 1e6:.4f} AU/Myr")
