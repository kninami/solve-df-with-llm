---
id: DFT-2046
type: technique
name: Detect and classify grid frequency events using SPEDA and machine learning
description: The process of screening synchrophasor (PMU) frequency time-series data for power-grid events - frequency excursions, oscillatory events, transient/impulsive events, generator or load loss, and islanding - by denoising and detrending the signal, computing a rolling-statistics-based event detection index across dual (10s/20s) sliding windows, and classifying confirmed events by type and severity using a trained machine-learning classifier.
objective_ids:
  - DFO-1019
weakness_ids:
  - DFW-2046
aliases:
  - SPEDA-ML (Synchrophasor Event Detection Algorithm with Machine Learning)
  - Synchrophasor Event Detection Index (SPEDI)
source_refs:
  - DFCite-2047
updated_at: 2026-08-14
status: partial
---

# Detect and classify grid frequency events using SPEDA and machine learning

## Summary

A power grid operator or forensic investigator examining wide-area frequency monitoring data for signs of equipment malfunction, cyberattack, or destabilizing events needs to both detect that a deviation occurred and understand what kind of event it was and how severe. An investigator denoises and normalizes the raw PMU frequency stream, screens it for statistically significant deviations using a dual-timescale rolling-window approach (a fast 10-second window for transient/short events, a slow 20-second window for sustained events), scores each detected deviation's severity with a composite index, and classifies the confirmed event into a specific category using a trained ML model.

## Details

DFCite-2047's pipeline: raw PMU frequency data is min-max scaled, then denoised using a Stationary Wavelet Transform (chosen over the Discrete Wavelet Transform for its translation-invariance, important for preserving event timing) with thresholded detail coefficients. A sliding-window ARIMA model computes rolling mean, variance, and standard deviation over both a 10-second and a 20-second window; a deviation exceeding a 1-standard-deviation threshold in the fast window flags a candidate "Fast" event, while a deviation surviving into the slow window flags a "Slow" event - the Synchrophasor Event Detection Algorithm (SPEDA). Each detected event's severity is quantified by the Synchrophasor Event Detection Index (SPEDI), a normalized (0-1), weighted combination of standard deviation (weight 0.3), variance (0.3), cumulative distribution function (0.15), stationarity via the Augmented Dickey-Fuller test (0.1), and event duration (0.15) - unlike single-metric indices (Voltage Stability Index, Frequency Deviation Index, Rate-of-Change-of-Frequency, Power System Oscillation Index), SPEDI's multi-metric design lets it classify events by both severity and duration on one normalized scale (e.g. SPEDI > 0.8 suggests a generator/load loss; 0.5-0.7 suggests prolonged oscillatory events). Confirmed events are finally classified by type using an ML classifier trained on features including start/end time, duration, and event frequency; of ten compared classifiers (SVM, k-NN, Decision Tree, Random Forest, XGBoost, ANN, Gradient Boosting, LightGBM, and two Attention Network variants), XGBoost achieved the best overall performance.

## Examples

- DFCite-2047's cross-dataset validation on New England ISO (ISO-NE1 through ISO-NE6) and European Continental (EUC) synchrophasor datasets, including a real system-wide mode oscillation (ISO-NE1, 0.27 Hz, near-resonance conditions for 3 minutes) and a regional generator-issue oscillation (ISO-NE3, 1.13 Hz, up to 115 MW peak-to-peak for 3 minutes).
- XGBoost benchmark: 99.3% accuracy, 99.32% F1-score, lowest RMSE/MSE/MAE among all ten tested classifiers, at a moderate 319.764ms training time.

## Related Objectives

- `DFO-1019` Detect anti-forensics and other anomalies

## Related Weaknesses

- [[weaknesses/Grid frequency event classifier accuracy is inflated by severe class imbalance among rare event types]]

## References

- [DFCite-2047] Gopinathan and Shanmugam, "Synchrophasor forensics: Tracking spatiotemporal anomalies and diagnosing grid frequency events with machine learning for enhanced situational awareness", IEEE Access, 2024 — source of the SPEDA/SPEDI methodology and ML classifier benchmark described above.
