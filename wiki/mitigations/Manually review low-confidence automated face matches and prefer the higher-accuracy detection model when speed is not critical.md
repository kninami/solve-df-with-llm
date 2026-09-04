---
id: LWM-2059
type: mitigation
name: Manually review low-confidence automated face matches and prefer the higher-accuracy detection model when speed is not critical
source_refs:
  - LWCite-2059
updated_at: 2026-08-15
status: complete
---

# Manually review low-confidence automated face matches and prefer the higher-accuracy detection model when speed is not critical

## Summary

Do not treat an automated face-recognition "no match" as conclusive evidence a person of interest is absent from an image set, particularly for images captured under poor lighting, heavy rain, or showing a substantial facial-hair change; manually spot-check a sample of "no match" results in those conditions, and select the slower, more accurate detection model over the faster one whenever verification accuracy matters more than processing time.

## Addresses

- [[weaknesses/Face-recognition PoI verification fails under poor lighting, heavy rain, or facial-hair changes]]

## How To Apply

Where an investigation depends on ruling a person of interest in or out of an image set, run automated matching first for triage speed, but before finalizing a report, manually review the images captured under known problem conditions (low light, rain, snow, or where the reference photo and candidate images differ significantly in facial hair) rather than trusting the automated result alone; where the case allows the extra processing time, re-run matching with the higher-accuracy (e.g., CNN-based) detection model rather than the default faster (e.g., HOG-based) model to reduce the false-negative rate before manual review.

## References

- [LWCite-2059] Gogia & Rughani, 2023, "An ML Based Digital Forensics Software for Triage Analysis Through Face Recognition", JDFSL, Manuscript 1772. States the tool's own hog/cnn accuracy-speed tradeoff and identifies facial hair and severe lighting/rain conditions as known sources of false positives/negatives.
