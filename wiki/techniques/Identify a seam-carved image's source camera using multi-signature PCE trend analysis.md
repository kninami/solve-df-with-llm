---
id: LWT-1103
type: technique
name: Identify a seam-carved image's source camera using multi-signature PCE trend analysis
description: Determine the source camera of a seam-carved image by selecting its highest-energy (least likely to have been carved) block, correlating that block against a sequence of camera PRNU signatures built from increasing numbers of reference images, and classifying the resulting trend in peak-to-correlation-energy (PCE) values rather than relying on a single PCE threshold.
objective_ids:
  - DFO-1008
weakness_ids:
  - LWW-1093
aliases:
  - CAMID
  - CAM1D
source_refs:
  - LWCite-1103
updated_at: 2026-08-12
status: complete
---

# Identify a seam-carved image's source camera using multi-signature PCE trend analysis

## Summary

Seam carving — a content-aware resizing technique that removes low-energy "seam" pixels — destroys the pixel-to-pixel positional correspondence that standard PRNU-based source camera identification depends on, since seams removed from a photo do not follow a fixed, image-independent pattern. CAM1D restores reliable identification by tracking how a candidate block's correlation with a *sequence* of increasingly large camera signatures trends over that sequence, rather than testing a single fixed-size camera signature against the whole image.

## Details

The method first performs block selection: the seam-carved image is divided into blocks and the block with the greatest summed gradient magnitude ("energy") is chosen, since high-energy (highly textured) regions are less likely to have had seams removed and so are more likely to retain pixel-aligned noise residue. A search is then performed within a window across a sequence of camera signatures {K_Ci(m), K_Ci(2m), ..., K_Ci(rm)} built from increasing numbers of reference images from candidate camera C_i, yielding a maximum-PCE value and matched position for each signature size. Five features are extracted from this sequence — the summed PCE values, the overall PCE trend (final minus initial), the stability of the matched position across the sequence, and two features capturing the sharpness of the correlation peak — and combined via entropy-weighted normalization into a single decision score. If the seam-carved photo genuinely originates from camera C_i, PCE values increase and the matched position stays stable as more reference images are used to build the signature; if not, the trend is essentially random. This directly exploits the observation that a single fixed-size PCE test is unreliable on seam-carved images (remaining below the standard PCE=50 threshold even with 120 reference images) while the multi-signature *trend* remains discriminating.

## Examples

- Tested on a 13-device dataset (smartphones and digital cameras, VISION/Dresden source images) with a 128x128 candidate block, CAM1D achieved 87-99% per-camera accuracy (95% average) on images seam-carved with at least one seam per 50x50 block, compared to unreliable results from a single PCE value even with 120 reference images.

## Related Objectives

- `DFO-1008` Establish identities

## Related Weaknesses

- [[weaknesses/Closed-set source-recording-device recognition cannot identify a device absent from its training set]]

## References

- [LWCite-1103] Irshad et al., 2023, "CAMID: An assuasive approach to reveal source camera through inconspicuous evidence", FSI: Digital Investigation 46.
