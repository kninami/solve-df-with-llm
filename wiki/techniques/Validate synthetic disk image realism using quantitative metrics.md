---
id: LWT-1040
type: technique
name: Validate synthetic disk image realism using quantitative metrics
description: Quantitatively assess how realistic a synthetic (scenario-based) forensic disk image is relative to real-world disk images by computing a large battery of automatable metrics (configuration, longevity, activity, volume) across both, using a cryptographically-inspired "realism game" framework in which a verifier tries to distinguish synthetic from real-world images using only queryable feature measurements.
objective_ids:
  - DFO-1004
weakness_ids:
  - LWW-1041
aliases:
  - Metrics-based synthetic disk image realism validation
source_refs:
  - LWCite-1031
updated_at: 2026-08-09
status: complete
---

# Validate synthetic disk image realism using quantitative metrics

## Summary

Scenario-based synthetic disk images are widely used for digital forensics research, tool testing, and training, but their usefulness depends on being sufficiently realistic — and until now realism has mostly been assessed informally. Borrowing terminology from cryptographic authentication protocols, a "realism game" formally defines realism: a verifier that can query arbitrarily many allowed features of a disk image, across many rounds against both real-world and synthetic images, should be no better than random guessing at telling them apart if the synthetic images are realistic with respect to that feature set.

## Details

A plugin-based measurement framework computes a wide set of metrics (98 in the reference implementation) across four categories — Configuration (e.g., installed applications, browser presence, screen ratio), Longevity (e.g., OS lifetime, install/shutdown time), Activity (e.g., link files, browser history visits/searches, login counts, USB connections), and Volume (e.g., file counts, non-NSRL files, file types) — computed identically across a set of real-world disk images and a set of synthetic ones, then compared distributionally (e.g., via box plots, means, medians) to identify where synthetic datasets diverge from real-world patterns. Because the framework is plugin-based, new metrics can be added incrementally, and the same underlying approach can support other applications beyond realism assessment, such as evaluating forensic tool behavior at scale or supporting quick disk-image triage.

## Examples

- Comparing three datasets (11 real-world, 14 public synthetic, 14 internal synthetic disk images): the Real-world dataset showed a markedly higher median login count (619) than the Public (17) or Internal (10,145, driven by one outlier) datasets, and a substantially higher median browser-history visit count (428) than either synthetic dataset (236 Public, low Internal), directly identifying dimensions where the synthetic datasets under-represented real-world activity levels.

## Related Objectives

- `DFO-1004` Conduct research

## Related Weaknesses

- [[weaknesses/Quantitative disk-image realism metrics cannot detect narrative incoherence in synthetic scenario data]]

## References

- [LWCite-1031] Voigt et al., 2025, "A metrics-based look at disk images: Insights and applications", FSI: Digital Investigation 52.
