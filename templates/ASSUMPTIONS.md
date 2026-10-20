# Assumptions — <project name>

Status: `confirmed` (researcher agreed) · `guessed` (Claude's choice, needs review) · `from-code` (read off existing code, Audit mode)

Reviewed by researcher on: <date or "not yet">

## Data
| # | Assumption | Status | Notes |
|---|---|---|---|
| D1 | Input file format, columns and their meaning | | |
| D2 | Units of each column | | |
| D3 | Missing values / NaN handling | | |
| D4 | Data cuts / cleaning rules | | |

## Conventions
| # | Assumption | Status | Notes |
|---|---|---|---|
| C1 | Array axis order (e.g. `[time, channel]`) | | |
| C2 | Coordinate system / sign conventions | | |
| C3 | Normalization (per sample? per bin width? to unit area?) | | |
| C4 | Binning: edges, inclusive/exclusive, under/overflow | | |
| C5 | Log base, angle units (rad/deg), time zero | | |

## Model and statistics
| # | Assumption | Status | Notes |
|---|---|---|---|
| M1 | Physical/statistical model being fitted or simulated | | |
| M2 | Noise model (Gaussian? Poisson? correlated?) | | |
| M3 | Estimators (`ddof`, MLE vs. least squares, one/two-sided tests) | | |
| M4 | Priors / parameter bounds | | |
| M5 | Numerical method and tolerances (integrator, step size, convergence criteria) | | |

## Reproducibility
| # | Assumption | Status | Notes |
|---|---|---|---|
| R1 | Random seeds | | |
| R2 | Library versions that matter | | |

## Headline results
- <the number/plot/claim that goes into the paper, and which modules feed it>
