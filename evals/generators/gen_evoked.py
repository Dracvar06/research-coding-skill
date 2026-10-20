"""Generate multichannel evoked-response data with a known answer.

Ground truth: only channel 2 responds (amplitude 0.8 baseline-SD units,
Gaussian bump peaking 120 ms after stimulus). Channels have very different
gains, so per-channel normalization is required.
"""
import sys
from pathlib import Path

import numpy as np

FS = 250.0
N_TRIALS, N_TIME, N_CH = 60, 300, 8
STIM = 100  # sample index of stimulus onset (0.4 s baseline)
GAINS = np.array([1.0, 5.0, 0.5, 2.0, 10.0, 1.0, 3.0, 0.8])
OFFSETS = np.array([0.3, -2.0, 1.1, 0.0, 4.0, -0.5, 0.7, 0.2])
RESP_CH, RESP_AMP, RESP_LAT_S, RESP_WIDTH_S = 2, 0.8, 0.120, 0.025


def generate(seed=7):
    rng = np.random.default_rng(seed)
    t = (np.arange(N_TIME) - STIM) / FS
    noise = rng.standard_normal((N_TRIALS, N_TIME, N_CH))
    resp = RESP_AMP * np.exp(-0.5 * ((t - RESP_LAT_S) / RESP_WIDTH_S) ** 2)
    noise[:, :, RESP_CH] += resp[None, :]
    return noise * GAINS + OFFSETS


if __name__ == "__main__":
    for out in sys.argv[1:]:
        Path(out).mkdir(parents=True, exist_ok=True)
        np.save(Path(out) / "epochs.npy", generate())
