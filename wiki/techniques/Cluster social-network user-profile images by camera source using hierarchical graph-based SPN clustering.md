---
id: LWT-2109
type: technique
name: Cluster social-network user-profile images by camera source using hierarchical graph-based SPN clustering
description: Group images collected across many social-network user profiles by which physical smartphone camera captured them, without any prior knowledge of how many distinct cameras are represented, by first detecting and removing "shared images" (images not directly taken by the profile owner's own smartphone, e.g. downloaded, cropped, or web-sourced images, whose sensor pattern noise does not reliably fingerprint any single source device) via density-based outlier detection, then hierarchically clustering the remaining "taken images" using a combined graph-partitioning (Markov clustering) and adaptive-threshold merging approach.
objective_ids:
  - DFO-1008
weakness_ids:
  - LWW-2116
aliases:
  - User profiles' image clustering
source_refs:
  - LWCite-2136
updated_at: 2026-08-16
status: complete
---

# Cluster social-network user-profile images by camera source using hierarchical graph-based SPN clustering

## Summary

Clustering images collected from a set of user profiles (e.g. in a child sexual abuse material or online-harassment investigation spanning many profiles) by camera source can link accounts and evidence images to a common physical device, but real-world profile image collections mix "taken images" (photographed directly by the profile owner's own smartphone, reliably fingerprinted via sensor pattern noise, SPN) with "shared images" (downloaded, cropped, screenshotted, or otherwise sourced images that do not carry a reliable SPN trace back to the profile owner's device and would corrupt a naive clustering process if not separated out first). This technique detects and removes shared images before clustering, and clusters the remaining images into an unknown number of camera-source groups without requiring the investigator to specify that number in advance.

## Details

Each image's residual noise (RN), an approximation of its source camera's SPN, is computed as the difference between the image and a denoised version of itself (via the BM3D denoising filter), then resized to a fixed resolution for computational tractability. The pre-processed residual noises are randomly partitioned into batches (sized to fit available memory), and for each batch: a pairwise Normalized Cross-Correlation similarity matrix is computed between residual noises; on the first pass, DBSCAN (a density-based clustering algorithm not requiring a predetermined cluster count) is applied to this matrix specifically to detect and remove outliers -- images whose residual noise does not correlate strongly with any sufficiently dense group of others, flagged as likely shared images; Markov clustering (a graph-partitioning algorithm using random-walk simulation with expansion and inflation operators) is then applied to the purified correlation matrix to group the remaining residual noises into candidate clusters, with clusters merged when their aggregated similarity exceeds an adaptive threshold that grows more selective as clusters grow larger and score-quality improves (reducing the chance of two different cameras' clusters merging incorrectly). This process repeats hierarchically across successive batches and cluster-merging rounds until no further clusters merge, and a final post-processing step scores each resulting cluster by size and excludes "fine" clusters (too few images sharing consistent SPN characteristics to be reliable) from the final reported result, keeping only sufficiently large "coarse" clusters.

## Examples

- Evaluated on the VISION public benchmark dataset (7,480 native images from 35 smartphones), perturbed with 3,000 additional simulated shared images drawn from sources other than the 35 smartphones, the method's shared-image (outlier) detection combined with clustering achieved Precision 0.996 and Recall 0.754 on the native-resolution dataset (37 of 35 ground-truth clusters recovered, since some smartphones' images split across more than one cluster), correctly flagging 2,836 of the 3,000 injected shared images as outliers.
- Robustness testing across a wide range of injected shared-image proportions (0% to 150% of the original dataset size) showed the method's Precision, Recall, F1-measure, and Adjusted Rand Index remained comparatively stable across all four tested SN-platform-simulated datasets, confirming the clustering quality is not unduly degraded even as the proportion of shared images requiring detection and removal grows substantially.

## Related Objectives

- `DFO-1008` Establish identities

## Related Weaknesses

- [[weaknesses/SPN-based image clustering degrades sharply for heavily compressed images from certain social-network platforms]]

## References

- [LWCite-2136] Rouhi, Bertini, and Montesi, 2021, "User profiles' image clustering for digital investigations", FSI: Digital Investigation 38, 301171.
