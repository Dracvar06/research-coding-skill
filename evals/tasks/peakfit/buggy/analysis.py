import numpy as np
from scipy.optimize import curve_fit

data = np.loadtxt("data/spectrum.csv", delimiter=",", skiprows=1)
energy, n1, n2 = data[:, 0], data[:, 1], data[:, 2]

# combine the two detectors
counts = 0.5 * (n1 + n2)
sigma = np.sqrt(counts) / 2


def model(e, a, b, amp, mu, width):
    return a + b * (e - 440.0) + amp * np.exp(-0.5 * ((e - mu) / width) ** 2)


p0 = [counts[0], 0.0, 10.0, 511.0, 5.0]
popt, pcov = curve_fit(model, energy, counts, p0=p0, sigma=sigma, absolute_sigma=True)
perr = np.sqrt(np.diag(pcov))

names = ["bkg_a", "bkg_b", "amp", "mu", "width"]
for n, v, e in zip(names, popt, perr):
    print(f"{n:6s} = {v:9.3f} +/- {e:.3f}")

amp, amp_err = popt[2], perr[2]
print(f"\nLine amplitude: {amp:.1f} +/- {amp_err:.1f} counts/bin")
print(f"Significance:   {amp / amp_err:.1f} sigma")
