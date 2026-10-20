# Evoked response — which sensor responds to the stimulus?

Recording: 8 sensors, 60 trials, 250 Hz. Each epoch is 1.2 s with the stimulus at 0.4 s
(sample 100). `data/epochs.npy` has shape (trials, time, channels).

The sensors have arbitrary gains and DC offsets (different amplifiers), so each channel is
z-scored relative to its own pre-stimulus baseline before averaging across trials.
The response is searched for 50–200 ms after the stimulus. We report the channel with the
largest absolute peak in the trial average, its latency, and the SNR (peak / SD of the
pre-stimulus part of the average).

## Result for the paper
Channel 4 shows the strongest evoked response (1.17 z at 176 ms, SNR 4.2).
Run: `python analysis.py`
