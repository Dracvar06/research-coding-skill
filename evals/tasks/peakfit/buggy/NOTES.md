# Search for a 511 keV line

Two identical detectors look at the same source for the same time. `data/spectrum.csv`
has the counts per 2 keV bin for each detector (energy column = bin centre).

We average the two spectra bin by bin and fit a Gaussian line on a linear background,
using Poisson uncertainties on the counts. The significance of the line is the fitted
amplitude divided by its uncertainty.

## Result for the paper
We observe a line with amplitude 25.8 ± 6.6 counts/bin, a 3.9σ excess.
Run: `python analysis.py`
