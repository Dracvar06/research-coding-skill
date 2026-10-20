"""Generate two-detector energy spectra with a weak Gaussian line.

Ground truth: linear background + Gaussian line at 511.0 keV, width 6 keV,
amplitude TRUE_AMP counts/bin per detector. Both detectors see the same
underlying spectrum with independent Poisson noise.
"""
import sys
from pathlib import Path

import numpy as np

EDGES = np.linspace(440.0, 580.0, 71)  # 70 bins of 2 keV
TRUE_AMP, TRUE_MU, TRUE_SIGMA = 18.0, 511.0, 6.0
BKG_A, BKG_B = 400.0, -0.4  # counts/bin = BKG_A + BKG_B * (E - 440)


def expected(e):
    return BKG_A + BKG_B * (e - 440.0) + TRUE_AMP * np.exp(-0.5 * ((e - TRUE_MU) / TRUE_SIGMA) ** 2)


def generate(seed=11):
    rng = np.random.default_rng(seed)
    centers = 0.5 * (EDGES[:-1] + EDGES[1:])
    lam = expected(centers)
    return centers, rng.poisson(lam), rng.poisson(lam)


if __name__ == "__main__":
    centers, d1, d2 = generate()
    for out in sys.argv[1:]:
        Path(out).mkdir(parents=True, exist_ok=True)
        np.savetxt(Path(out) / "spectrum.csv",
                   np.column_stack([centers, d1, d2]),
                   delimiter=",", header="energy_keV,counts_det1,counts_det2",
                   comments="", fmt=["%.1f", "%d", "%d"])
