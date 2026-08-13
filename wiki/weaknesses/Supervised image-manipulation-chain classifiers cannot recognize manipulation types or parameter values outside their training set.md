---
id: DFW-1209
type: weakness
name: Supervised image-manipulation-chain classifiers cannot recognize manipulation types or parameter values outside their training set
description: A supervised manipulation-operator-chain classifier is trained on a fixed, closed set of manipulation types (e.g. median filtering, Gaussian blur, resampling) and specific parameter values (e.g. particular kernel sizes or quality factors) for each, and has no mechanism for correctly classifying, or flagging as unrecognized, an image edited with a manipulation type or parameter value it was not trained on.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1209
source_refs:
  - DFCite-1222
updated_at: 2026-08-13
status: complete
---

# Supervised image-manipulation-chain classifiers cannot recognize manipulation types or parameter values outside their training set

## Summary

The evaluated network was trained on a fixed roster of five manipulation types (JPEG re-compression, median filtering, Gaussian blur, resampling, and additive white Gaussian noise) at a small, fixed set of parameter values (e.g. 3x3 and 5x5 kernels, quality factors 50-90, resampling factors 1.2/1.5), and its operator-chain classification is a closed multi-class problem over those specific manipulations and their two-step combinations. No mechanism is described for detecting a manipulation type absent from this set, or a parameter value outside the trained range, nor for flagging an image edited by an unfamiliar tool as "unrecognized" rather than forcing it into the nearest trained class.

## Why It Matters

An investigator relying on this class of classifier to reconstruct an image's editing history must confirm that the actual editing tools and parameter ranges plausible for the case (which may not be known in advance) fall within the model's trained categories; otherwise the model will still output a confident-looking chain classification rather than indicating the manipulation is unrecognized, which risks a wrong processing-history conclusion being presented as though it were validated. This is compounded for real-world images, which may have passed through editing software using default or non-standard parameter values never represented in the fixed training set.

## Related Mitigations

- [[mitigations/Validate a manipulation-chain classifier's type and parameter coverage against the case's suspected editing tools]]

## Used By

- [[techniques/Reconstruct an image's manipulation-operator chain using a dual-stream residual network]]

## References

- [DFCite-1222] Kadha et al., 2023, "Forensic analysis of manipulation chains: A deep residual network for detecting JPEG-manipulation-JPEG", FSI: Digital Investigation 47.
