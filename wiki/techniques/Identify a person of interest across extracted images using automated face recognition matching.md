---
id: LWT-2058
type: technique
name: Identify a person of interest across extracted images using automated face recognition matching
description: Automatically match a known person of interest's reference photo(s) against a large set of images extracted from seized media, using facial-landmark feature encoding, to flag which images likely contain that person without manual review of every file.
objective_ids:
  - DFO-1008
weakness_ids:
  - LWW-2058
aliases:
  - Automated PoI identification (SynFO)
source_refs:
  - LWCite-2059
updated_at: 2026-08-15
status: complete
---

# Identify a person of interest across extracted images using automated face recognition matching

## Summary

Given a set of reference images of a known person of interest (PoI) and a much larger set of unknown images extracted from evidence, detect faces in every image and compute a fixed-dimension facial-landmark encoding for each, then compare encodings to automatically flag likely matches. This turns a manual, hours-long visual review of thousands of pictures into an automated triage step.

## Details

The technique uses a face-detection model (a faster Histogram-of-Oriented-Gradients model, or a slower but more accurate Convolutional Neural Network model) to locate faces in each image, then computes a 128-dimension facial-landmark feature vector per detected face. Matching supports four modes — one-to-one, one-to-many, many-to-one, and many-to-many — so an investigator can check a single suspect photo against an entire extracted image corpus, or check every unknown face against a gallery of multiple known persons. It is typically chained after an image-extraction step (see [[techniques/Extract embedded picture files from documents and disk images using format-aware carving]]) so the candidate image set already excludes irrelevant non-picture files. Match results are logged to a file for investigator review and documentation rather than acted on automatically, keeping a human in the loop for the final identification decision.

## Examples

- The SynFO command-line tool ran automated PoI identification against images extracted from a 16GB SD card and a 32GB USB drive, correctly verifying the PoI in day, indoor, and single-camera night scenarios, including images with multiple faces in frame and images embedded inside document containers (e.g., a forged ID card image inside a word-processor file).
- Using the `hog` model completed verification in under two minutes per device in testing, while the `cnn` model traded speed for higher accuracy, illustrating the practical speed/accuracy tradeoff investigators can select per case.

## Related Objectives

- `DFO-1008` Establish identities

## Related Weaknesses

- [[weaknesses/Face-recognition PoI verification fails under poor lighting, heavy rain, or facial-hair changes]]

## References

- [LWCite-2059] Gogia & Rughani, 2023, "An ML Based Digital Forensics Software for Triage Analysis Through Face Recognition", JDFSL, Manuscript 1772. Source of the SynFO automated PoI identification methodology, its four matching modes, and its HOG/CNN model tradeoff.
