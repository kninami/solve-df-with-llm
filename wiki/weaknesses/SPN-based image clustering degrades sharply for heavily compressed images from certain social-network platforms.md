---
id: DFW-2116
type: weakness
name: SPN-based image clustering degrades sharply for heavily compressed images from certain social-network platforms
description: Sensor-pattern-noise-based image clustering accuracy varies substantially depending on which social-network platform's compression pipeline processed the images being clustered, with heavily-compressed low-resolution variants (e.g. a platform's "low resolution" tier) showing markedly lower precision, recall, and outlier-detection accuracy than the same images' higher-resolution or native variants, because aggressive compression degrades the sensor pattern noise signal the clustering depends on.
categories:
  - ASTM_INCOMP
  - ASTM_MISINT
mitigation_ids:
  - DFM-2117
source_refs:
  - DFCite-2136
updated_at: 2026-08-16
status: complete
---

# SPN-based image clustering degrades sharply for heavily compressed images from certain social-network platforms

## Summary

Testing the clustering method across four platform-simulated datasets (native resolution, WhatsApp, Facebook High Resolution, and Facebook Low Resolution) found precision, recall, and related quality measures dropped substantially for the most heavily-compressed dataset: the Facebook Low Resolution dataset measured Precision 0.796, Recall 0.301, and F1-measure 0.433 (versus Precision 0.996, Recall 0.754, F1-measure 0.858 for the native-resolution dataset under the same evaluation), and correctly detected only 12 of 35 ground-truth device clusters (versus 37 of 35 for native resolution, since native-resolution clustering sometimes splits a single device's images across more than one cluster but still identifies all 35 devices in some grouping).

## Why It Matters

An investigator applying this clustering technique to images collected from a platform whose compression pipeline degrades SPN quality more aggressively (as Facebook's low-resolution tier does relative to WhatsApp or Facebook's higher-resolution tier) should expect substantially lower recall specifically -- meaning a meaningful proportion of genuinely same-source images may fail to be grouped together at all, understating the true extent of common camera-source evidence across the examined profiles. Treating clustering results from a heavily-compressed image source with the same confidence as results from higher-quality sources risks both missing genuine device-source links and misjudging how thorough the clustering coverage actually was for that platform.

## Related Mitigations

- [[mitigations/Validate SPN-based image clustering accuracy per source platform and compression level before relying on recall for heavily compressed images]]

## Used By

- [[techniques/Cluster social-network user-profile images by camera source using hierarchical graph-based SPN clustering]]

## References

- [DFCite-2136] Rouhi, Bertini, and Montesi, 2021, "User profiles' image clustering for digital investigations", FSI: Digital Investigation 38, 301171.
