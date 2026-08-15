---
id: DFW-2058
type: weakness
name: Face-recognition PoI verification fails under poor lighting, heavy rain, or facial-hair changes
description: Automated face-matching against a known person of interest can fail to verify a genuine match when the candidate image was captured in poor lighting, heavy rain, or shows the person with a substantially different amount of facial hair than the reference photo, producing a false negative.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-2059
source_refs:
  - DFCite-2059
updated_at: 2026-08-15
status: complete
---

# Face-recognition PoI verification fails under poor lighting, heavy rain, or facial-hair changes

## Summary

Automated person-of-interest face matching was tested across day, indoor, rain, and night scenarios using cameras ranging from a DSLR to smartphones. Detection (locating a face at all) succeeded across all tested conditions, but verification (confirming the detected face matches the known PoI) failed specifically in the combined night-plus-rain scenario, and the authors separately note that real-world images of people with and without facial hair, or captured under severe light conditions, can produce false positives or false negatives more broadly.

## Why It Matters

If an investigator treats an automated "no match" result as conclusive, a genuine appearance of the person of interest captured in adverse conditions (poor lighting, rain, or after a facial-hair change) can be silently excluded from the evidence set, undermining completeness of the identification process. Conversely, an unreviewed false positive under the same conditions risks misattributing an image to the wrong individual.

## Related Mitigations

- [[mitigations/Manually review low-confidence automated face matches and prefer the higher-accuracy detection model when speed is not critical]]

## Used By

- [[techniques/Identify a person of interest across extracted images using automated face recognition matching]]

## References

- [DFCite-2059] Gogia & Rughani, 2023, "An ML Based Digital Forensics Software for Triage Analysis Through Face Recognition", JDFSL, Manuscript 1772. Reports a verification failure in the night-plus-rain test scenario and notes facial-hair and severe-lighting conditions as broader sources of false positives/negatives.
