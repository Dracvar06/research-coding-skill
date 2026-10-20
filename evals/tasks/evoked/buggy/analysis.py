import numpy as np

FS = 250.0          # Hz
STIM = 100          # stimulus onset sample
WINDOW = (0.05, 0.20)  # s, response search window

epochs = np.load("data/epochs.npy")  # (trials, time, channels)
n_trials, n_time, n_ch = epochs.shape
t = (np.arange(n_time) - STIM) / FS

baseline = epochs[:, :STIM, :]
mu = baseline.mean(axis=(1, 2), keepdims=True)
sd = baseline.std(axis=(1, 2), keepdims=True)
z = (epochs - mu) / sd

evoked = z.mean(axis=0)  # (time, channels)

win = (t >= WINDOW[0]) & (t <= WINDOW[1])
ev_win = evoked[win]
peak_idx = np.argmax(np.abs(ev_win), axis=0)
peak_amp = ev_win[peak_idx, np.arange(n_ch)]
peak_lat = t[win][peak_idx]
noise = evoked[t < 0].std(axis=0)
snr = np.abs(peak_amp) / noise

print("ch  amp(z)  lat(ms)  SNR")
for c in range(n_ch):
    print(f"{c:2d}  {peak_amp[c]:6.2f}  {peak_lat[c]*1000:7.0f}  {snr[c]:5.1f}")

best = int(np.argmax(np.abs(peak_amp)))
print(f"\nStrongest response: channel {best}, amplitude {peak_amp[best]:.2f} z, "
      f"latency {peak_lat[best]*1000:.0f} ms, SNR {snr[best]:.1f}")
