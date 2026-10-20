import numpy as np

GM_SUN = 4 * np.pi**2      # AU^3 / yr^2
A0, E0 = 1.5, 0.85         # initial semi-major axis (AU) and eccentricity
T_ALONG = 6.6e-8           # Yarkovsky along-track acceleration (AU / yr^2)
DT = 0.25 / 365.25         # 6 h step (yr)
YEARS = 100.0


def accel(r, v):
    grav = -GM_SUN * r / np.linalg.norm(r) ** 3
    yark = T_ALONG * v / np.linalg.norm(v)
    return grav + yark


def deriv(state):
    r, v = state[:2], state[2:]
    return np.concatenate([v, accel(r, v)])


def rk4_step(state, dt):
    k1 = deriv(state)
    k2 = deriv(state + 0.5 * dt * k1)
    k3 = deriv(state + 0.5 * dt * k2)
    k4 = deriv(state + dt * k3)
    return state + dt / 6.0 * (k1 + 2 * k2 + 2 * k3 + k4)


def semi_major_axis(state):
    r = np.linalg.norm(state[:2])
    v2 = state[2:] @ state[2:]
    return 1.0 / (2.0 / r - v2 / GM_SUN)


# start at perihelion
q = A0 * (1 - E0)
state = np.array([q, 0.0, 0.0, np.sqrt(GM_SUN * (1 + E0) / q)])

n_steps = int(YEARS / DT)
t_out, a_out = [], []
for i in range(n_steps):
    state = rk4_step(state, DT)
    if i % 10 == 0:
        t_out.append((i + 1) * DT)
        a_out.append(semi_major_axis(state))

slope = np.polyfit(t_out, a_out, 1)[0]  # AU / yr
print(f"a(0) = {a_out[0]:.6f} AU, a({YEARS:.0f} yr) = {a_out[-1]:.6f} AU")
print(f"da/dt = {slope * 1e6:.4f} AU/Myr")
