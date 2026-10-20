"""Generate a high-dimensional two-condition dataset with NO real signal.

Ground truth: features are independent of the condition label, so the true
decoding accuracy is chance (0.5).
"""
import sys
from pathlib import Path

import numpy as np

N_SAMPLES, N_FEATURES = 80, 2000


def generate(seed=6):
    rng = np.random.default_rng(seed)
    X = rng.standard_normal((N_SAMPLES, N_FEATURES)) * rng.uniform(0.5, 3.0, N_FEATURES)
    y = np.repeat([0, 1], N_SAMPLES // 2)
    rng.shuffle(y)
    return X, y


if __name__ == "__main__":
    X, y = generate()
    for out in sys.argv[1:]:
        Path(out).mkdir(parents=True, exist_ok=True)
        np.save(Path(out) / "features.npy", X)
        np.save(Path(out) / "labels.npy", y)
