---
id: DFT-2014
type: technique
name: Verify a recording's time using electric network frequency correlation
description: The process of confirming or refuting a claimed recording time for an audio or video file by extracting its embedded Electric Network Frequency (ENF) signal - the mains power grid's continually fluctuating AC frequency, picked up incidentally by mains-powered recording equipment - and correlating it against a ground-truth ENF signal recorded from the power grid at the claimed time.
objective_ids:
  - DFO-1001
weakness_ids:
  - DFW-2014
aliases:
  - ENF-based time-of-recording verification
  - STFT segmentation scheme for ENF estimation
source_refs:
  - DFCite-2014
updated_at: 2026-08-14
status: partial
---

# Verify a recording's time using electric network frequency correlation

## Summary

Mains-powered audio and video recording equipment incidentally embeds the power grid's Electric Network Frequency (ENF) - a signal that fluctuates continually around 50 or 60 Hz depending on supply/demand imbalance and is consistent across an entire interconnected grid at a given moment - into the recording, via electromagnetic fields (dynamic microphones), acoustic mains hum (electret microphones), or mains-powered lighting (video). An investigator extracts this ENF signal from a query recording using Short-Time Fourier Transform (STFT) segmentation and correlates it against a ground-truth ENF signal independently logged from the grid, to confirm or refute a claimed recording date/time - for example, to test an alibi claim that a recording was made somewhere other than a crime scene at the time of a crime.

## Details

DFCite-2014 improves the conventional STFT-based ENF estimation stage (which divides a decimated, bandpass-filtered signal into fixed-size overlapping segments and estimates one ENF sample per segment midpoint via peak-magnitude FFT detection and quadratic interpolation) by adding an anterior and posterior adaptive segmentation phase. Rather than discarding the ENF information before the midpoint of the first fixed-size segment and after the midpoint of the last, the proposed scheme constructs additional segments of progressively shrinking size (each 2x the hop size smaller than the last) anchored to the recording's actual start and end, recovering ENF samples the conventional method loses entirely. This produces a longer, more distinctive ENF signal (since short-duration ENF patterns recur more often across different times, making them less reliable for verification) without altering the underlying per-segment estimation accuracy, and the extension is complementary to - and can be layered with - other ENF-accuracy-enhancement strategies (e.g. Robust Filtering Algorithm, Enhanced Maximum-Likelihood Estimation) applied within each segment.

## Examples

- DFCite-2014's ENF-WHU dataset evaluation: extending a 32-second-segment ENF signal by 7 samples at each end raised the true time-stamp match rate for 2-minute audio clips from 54.62% (conventional STFT) to 61.54%, and combining the segmentation scheme with an existing E-MLE enhancement raised the 10-minute-clip match rate from 91.46% to 98.78%.

## Related Objectives

- `DFO-1001` Reconstruct events

## Related Weaknesses

- [[weaknesses/ENF-based time-of-recording verification has low match accuracy for short recordings]]

## References

- [DFCite-2014] Yalinkilic and Vatansever, "An enhanced STFT segmentation framework for ENF-based media forensics", IEEE Access, 2024 — source of the adaptive anterior/posterior segmentation scheme and its ENF-WHU evaluation results.
