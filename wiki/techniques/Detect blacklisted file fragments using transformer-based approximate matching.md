---
id: DFT-1120
type: technique
name: Detect blacklisted file fragments using transformer-based approximate matching
description: Detect whether a fragment of a blacklisted file (e.g. known malware, or a corporate secret document) is embedded within a much larger candidate file by computing a traditional fuzzy hash (ssdeep or TLSH) of the candidate and classifying that hash with a transformer neural network trained to recognize the blacklisted fragment's presence, improving fragment-detection accuracy over comparing fuzzy hashes directly while keeping the compact, scalable hash representation.
objective_ids:
  - DFO-1019
weakness_ids:
  - DFW-1125
aliases:
  - DLAM
  - Deep Learning Approximate Matching
source_refs:
  - DFCite-1119
updated_at: 2026-08-12
status: complete
---

# Detect blacklisted file fragments using transformer-based approximate matching

## Summary

Traditional approximate matching (fuzzy hashing) algorithms such as TLSH and ssdeep are widely used to detect blacklisted content — known malware or leaked corporate documents — even when only a fragment of the original file is present, but their direct hash-similarity comparison fails once the fragment is small relative to the surrounding (much larger) candidate file. Deep Learning Approximate Matching (DLAM) instead trains a transformer network to classify a candidate file's fuzzy hash directly as containing or not containing a specific blacklisted fragment, learning fragment-detection patterns that plain hash-similarity comparison misses.

## Details

DLAM computes a candidate file's fuzzy hash (ssdeep or TLSH) as a compact intermediate representation, tokenizes the resulting byte-string hash, adds absolute positional encoding to preserve byte order, and trains a transformer model with binary cross-entropy loss to predict whether a target fragment's known signature is present. Evaluated on JavaScript malware and PDF/Office corporate-secret documents, DLAM matched or exceeded the accuracy of unbounded-length multi-resolution hashes (mrsh-cf, mrsh-v2) while using only the much shorter, fixed-length ssdeep or TLSH hash as its input — for JavaScript files, DLAM achieved 93% accuracy versus 50% for direct ssdeep/TLSH similarity comparison at the same fragment-to-file size ratio. Because it works from a short, fixed-length hash rather than an unbounded one, DLAM also eliminates the tedious manual extraction of "known-to-be-bad parts" that unbounded multi-resolution hashing otherwise requires before a search can even begin, making large-scale automated classification more practical. The paper is a supervised approach: models are trained per fragment/blacklist category using labeled examples of files with and without that fragment present.

## Examples

- On a JavaScript malware fragment-detection test corpus, applying DLAM to ssdeep hashes achieved 93% classification accuracy, compared to 50% for ssdeep's own similarity-score comparison on the same fragment sizes.
- DLAM applied to TLSH hashes remained able to detect fragments even where TLSH's own similarity comparison had already dropped to near-chance performance as the fragment shrank relative to the surrounding file.

## Related Objectives

- `DFO-1019` Detect anti-forensics and other anomalies

## Related Weaknesses

- [[weaknesses/DLAM requires supervised retraining per blacklisted fragment, unlike signature-database-updatable fuzzy hashing]]

## References

- [DFCite-1119] Uhlig et al., 2023, "Combining AI and AM - Improving approximate matching through transformer networks", FSI: Digital Investigation 45.
