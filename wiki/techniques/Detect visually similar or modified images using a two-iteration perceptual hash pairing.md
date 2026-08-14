---
id: DFT-2016
type: technique
name: Detect visually similar or modified images using a two-iteration perceptual hash pairing
description: The process of locating visually similar or deliberately modified images (e.g. cropped, mirrored, watermarked, rotated, or color-altered copies of known illicit content) within a large seized image collection by comparing perceptual hashes against a reference set, then applying a second, complementary perceptual hash algorithm to filter the first pass's false-positive matches before analyst review.
objective_ids:
  - DFO-1012
weakness_ids:
  - DFW-2016
aliases:
  - ChaSAM Forensics
  - chHash and domiHash perceptual hash algorithms
source_refs:
  - DFCite-2016
updated_at: 2026-08-14
status: partial
---

# Detect visually similar or modified images using a two-iteration perceptual hash pairing

## Summary

Because conventional cryptographic hashing (MD5/SHA) only matches byte-identical files and fails the moment an image is cropped, mirrored, watermarked, resized, or otherwise altered - a routine anti-forensic evasion for illicit imagery such as CSAM - an investigator instead compares images using perceptual hashes that summarize an image's visual structure rather than its exact bytes, tolerating minor alterations while still flagging visually similar content. Because a single perceptual hash algorithm run alone still produces a substantial share of false-positive matches, ChaSAM Forensics runs a first, broader hash algorithm to surface all plausible candidates, then re-filters those candidates with a second, complementary hash algorithm before presenting the final result set for analyst review.

## Details

DFCite-2016 evaluates six perceptual hash algorithms (aHash, dHash, dHash-v, pHash, and two new algorithms: domiHash and chHash) using resize -> grayscale/thresholding -> difference/DCT calculation -> binarization -> 64-bit hash-generation pipelines, compared via Hamming distance against a configurable threshold. chHash departs from convention by black/white-thresholding the image (empirically tuned threshold of 114, not the standard 128) before applying DCT, rather than using grayscale, and was found to have the lowest single-iteration false-positive rate of all six algorithms (43.75% cleaning efficiency). domiHash, a dHash derivative comparing diagonal (rather than row- or column-wise) pixel differences, was specifically designed to detect rotated images, a known weakness of conventional dHash/aHash, but its efficiency drops sharply for other transformations like mirroring. The ChaSAM Forensics tool architecture loads candidate images from a "target" folder, extracts each one's perceptual hash across parallel worker routines, and compares them against a "source" folder of known/reference images, writing matches to an "extracted" results folder; running the comparison with 32-64 parallel routines was found to give the best throughput-to-overhead ratio across six tested hardware configurations (up to roughly 70-95% faster than single-routine execution).

## Examples

- DFCite-2016's dHash+chHash two-iteration pairing on a 12,920-file test corpus (9 transformation types plus 17 rotation angles applied to an original 380-image set): raised true-positive filtering from 29.52% (dHash alone) to 96.43%, eliminating 73 of 74 false-positive files while removing only 4 of 31 true positives.
- Validated against 25 AI-generated child images (Bing image generator) and a real, legally restricted CSAM sample set (40 modified copies), where dHash+chHash and dHash-v+chHash both reached 100% accuracy in the second iteration.

## Related Objectives

- `DFO-1012` Locate potentially relevant content

## Related Weaknesses

- [[weaknesses/Single-iteration perceptual hash image matching produces a high false-positive rate]]

## References

- [DFCite-2016] dos Santos et al., "ChaSAM: An architecture based on perceptual hashing for image detection in computer forensics", IEEE Access, 2024 — source of the chHash/domiHash algorithms, the two-iteration pairing scheme, and the evaluation results described above.
