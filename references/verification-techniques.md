# Verification techniques catalog

Known-answer and invariant checks for code whose real-data output is unknown.
Pick at least one per module. Expected values must come from first principles,
not from running the code under test.

## Universal

| Technique | What it checks | Example |
|---|---|---|
| Tiny hand-computed case | Arithmetic, indexing, conventions | 3 data points, compute the mean/fit/statistic by hand in a comment, assert equality |
| Units / dimensional analysis | Missing constants, wrong conversions | Scale all inputs from m to km; output in physical units must be unchanged after conversion back |
| Normalization | Probabilities, PDFs, weights | Histogram/PDF integrates to 1; weights sum to N |
| Symmetry / permutation | Accidental order dependence | Shuffle rows of independent samples → same result |
| Metamorphic relation | Linearity, shifts, scaling | Multiply input by 2 → linear output doubles; shift time by Δ → peak moves by Δ |
| Round trip | Transform/inverse pairs | `ifft(fft(x)) ≈ x`, `decode(encode(x)) == x`, unit conversion and back |
| Edge cases | NaN, empty, constant input | Zero-variance input, empty bins, single sample, all-NaN column — decide expected behavior in ASSUMPTIONS.md |
| Independent version | Implementation bugs (weak if versions share model/approach) | Closed-form vs. iterative solution of the same estimator |

## Numerical simulation (ODE/PDE, Monte Carlo, N-body, lattice…)

- **Analytic limits**: turn off interactions/damping/forcing where a closed form
  exists (free particle, harmonic oscillator, diffusion of a Gaussian, zero
  coupling). The simulation must reproduce it.
- **Convergence order**: run at step sizes h, h/2, h/4. For a method of order p,
  error ratios should approach 2^p. Wrong ratio = bug (or the method isn't what
  you think). Use Richardson extrapolation when no exact solution exists.
- **Method of manufactured solutions (MMS)**: choose a smooth solution u*(x,t),
  plug it into the equations to compute the source term it implies, add that
  source, and check the solver returns u* with the expected convergence order.
- **Conservation**: energy, momentum, mass, charge, probability — check drift
  over time is within the integrator's expected error (and doesn't grow when
  it shouldn't, e.g. symplectic integrators).
- **Symmetry**: rotate/translate/reflect the initial condition → output transforms
  the same way.
- **Monte Carlo**: compare against an exactly solvable small system (e.g. 2×2
  Ising by enumeration); check that statistical error decreases as 1/√N.
- **Cheap fallback** for slow runs: tiny grid / few particles / short times for
  convergence and limits; full-size run only once.

## Statistical analysis (fits, inference, hypothesis tests, pipelines)

- **Injection–recovery**: generate synthetic data from the *assumed* model with
  known parameters (realistic noise, cuts, binning), run the full analysis, and
  check the parameters come back.
- **Pull / coverage test** (checks error bars, not just values): repeat
  injection–recovery over many realizations (≈200–1000). Pulls
  `(fit − true) / σ_fit` should have mean ≈ 0 (no bias) and std ≈ 1 (honest
  errors); 68% / 95% intervals should cover the true value ~68% / ~95% of the time.
- **Null test**: inject no signal → detection significance distributed as
  expected under H0 (e.g. p-values uniform).
- **Known reference values**: compare to a textbook/published dataset with known
  result (e.g. classic regression datasets) if the method is standard.
- **Estimator conventions**: biased vs. unbiased variance (`ddof`), log vs. ln,
  one- vs. two-sided tests — encode in ASSUMPTIONS.md and test with a hand case.
- **Model mismatch probe**: inject data from a slightly different model (e.g.
  heavier-tailed noise) and see how much the result moves — documents robustness,
  not correctness.
- **Cheap fallback** for slow fits: fewer realizations (≈50) — enough to catch a
  factor-√2 error-bar bug; state the reduced precision in the report.

## ML / signal processing

- **Shuffled-label negative control**: train on permuted labels → performance
  must drop to chance. If not, there is leakage or a bug in evaluation.
- **Leakage checks**: no overlap of IDs/subjects/time windows between train and
  test; preprocessing (scalers, PCA, feature selection) fitted on train only;
  time-series splits respect time order.
- **Known-signal pass-through**: feed a pure sinusoid / impulse / step through the
  filter chain; compare amplitude/phase/delay with the filter's theoretical
  response.
- **Planted-feature test**: create synthetic data where only feature k is
  informative → model/feature importance should identify k.
- **Overfit-a-tiny-batch**: model must reach ~zero training loss on a handful of
  samples (sanity check of the training loop).
- **Determinism**: same seed → same result; different seeds → spread consistent
  with reported uncertainty.
- **Baseline comparison**: trivial baseline (majority class, linear model,
  persistence forecast) — a fancy model far above it on noisy data deserves
  suspicion.
- **Cheap fallback**: smaller model/subset for negative controls; full run once.

## Choosing techniques for a module

1. Can you generate data where the right output is known? → injection–recovery,
   analytic limit, MMS, known-signal.
2. Is there a property that must hold whatever the data? → invariants,
   metamorphic relations, negative controls.
3. Neither? → the module is **critical by rule**: give it independent versions
   and flag it in the report as "verified by agreement only".
