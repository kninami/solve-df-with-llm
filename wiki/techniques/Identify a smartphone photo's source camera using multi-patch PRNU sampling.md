---
id: LWT-1301
type: technique
name: Identify a smartphone photo's source camera using multi-patch PRNU sampling
description: Attribute a smartphone photo to its source camera despite the photo-response non-uniformity (PRNU) sensor "fingerprint" being unstable in smartphone imagery — due to heavy in-pipeline processing (beautification, filtering), lighting/scene-complexity sensitivity, and the diversity of smartphone imaging pipelines — by extracting multiple PRNU-carrying patches from different regions of a single examined image to simulate a set of homologous same-source images, then combining them via machine learning into an automated, threshold-free source-attribution decision.
objective_ids:
  - DFO-1008
weakness_ids:
  - LWW-1312
aliases:
  - Multivariate PRNU sampling for smartphone source attribution
source_refs:
  - LWCite-1353
updated_at: 2026-08-15
status: complete
---

# Identify a smartphone photo's source camera using multi-patch PRNU sampling

## Summary

PRNU-based source camera identification performs well on traditional cameras but degrades significantly on smartphone images because of the vast diversity of smartphone brands, models, and imaging pipelines — devices apply intensive processing (beautification, filtering) that distorts or conceals the underlying sensor fingerprint, and the PRNU signal itself is sensitive to lighting conditions and scene complexity. Rather than requiring a set of genuinely independent same-source images (as prior multi-image-aggregation approaches do, which is often infeasible when only a single examined image is available), extracting multiple patches from different spatial regions of that single image simulates a set of homologous images, providing the statistical stability of multi-sample aggregation from just one photo.

## Details

PRNU features are extracted using two independent noise-extractor types to verify the approach generalizes across extraction methods: a non-data-driven wavelet-domain decomposition algorithm, and a deep U-shaped residual neural network (DRUNet). Peak-to-correlation-energy (PCE) distribution statistics on positive (same-source) and negative (different-source) sample pairs from the FODB smartphone-image dataset are analyzed to quantitatively characterize the regional instability of PRNU features within smartphone images — including a newly proposed Relative Range to Max (RRM) metric applied to positive sample pairs specifically to quantify how much PRNU reliability varies across different regions of the same image. The resulting per-patch PCE statistics feed a machine-learning classifier that performs automated same-source/different-source discrimination directly, without requiring an investigator to manually set and justify a PCE decision threshold as prior single-sample approaches require.

## Examples

- Analyzing the PCE distribution of negative (different-source) sample pairs across the FODB dataset quantified how denoising method choice (wavelet vs. DRUNet) and input patch size each affect the mean and variance of PCE scores, informing which extractor/size combinations are best suited to the multi-patch approach.
- The multi-patch framework was validated with both the wavelet and DRUNet extractors, demonstrating that the approach's stability improvement is not an artifact of one specific noise-extraction algorithm but generalizes across non-data-driven and deep-learning-based extraction methods alike.

## Related Objectives

- `DFO-1008` Establish identities

## Related Weaknesses

- [[weaknesses/PRNU reliability varies unpredictably across regions of a single smartphone image]]

## References

- [LWCite-1353] Liang, Gao, and Xu, 2025, "Research on smartphone image source identification based on PRNU features collected multivariate sampling strategy", FSI: Digital Investigation 54, 301991.
