---
id: DFM-2117
type: mitigation
name: Validate SPN-based image clustering accuracy per source platform and compression level before relying on recall for heavily compressed images
source_refs:
  - DFCite-2136
updated_at: 2026-08-16
status: complete
---

# Validate SPN-based image clustering accuracy per source platform and compression level before relying on recall for heavily compressed images

## Summary

Before treating SPN-based image clustering results as a comprehensive account of which profile images share a common camera source, determine which social-network platform and compression tier processed the images and account for that platform's known clustering accuracy, treating recall as significantly less reliable for heavily-compressed image sources.

## Addresses

- [[weaknesses/SPN-based image clustering degrades sharply for heavily compressed images from certain social-network platforms]]

## How To Apply

Identify, where possible, which platform and compression tier (e.g. native/original, standard-resolution re-upload, or a platform's own low-resolution tier) produced the profile images being clustered with [[techniques/Cluster social-network user-profile images by camera source using hierarchical graph-based SPN clustering]], and expect substantially reduced recall for heavily-compressed sources specifically. Do not treat an image's absence from any cluster, or a smaller-than-expected cluster, as confirmation it lacks a common source with other clustered images when the source platform is known to compress heavily; instead, treat such cases as inconclusive and pursue independent corroboration where source-device linkage is important to the investigation. Where the case allows, prefer collecting the highest-resolution/least-compressed version of a profile image available (e.g. via a legal request to the platform, if pursuing the strongest recall) rather than relying solely on whatever compressed version is directly visible on the profile.

## References

- [DFCite-2136] Rouhi, Bertini, and Montesi, 2021, "User profiles' image clustering for digital investigations", FSI: Digital Investigation 38, 301171.
