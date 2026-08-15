---
id: DFW-2021
type: weakness
name: Software signature search engine precision degrades sharply on realistic forensic datasets
description: A doc2vec-based software signature search engine's precision drops substantially when evaluated against a realistic, uncontrolled forensic dataset compared to purpose-built controlled test machines, meaning a meaningful share of a case's positive software-presence detections may be false positives.
categories:
  - ASTM_INAC_EX
mitigation_ids:
  - DFM-2021
source_refs:
  - DFCite-2021
updated_at: 2026-08-14
status: partial
---

# Software signature search engine precision degrades sharply on realistic forensic datasets

## Summary

The source paper's own results show S3E model precision on the 20 purpose-built controlled machines ranging from 0.795 to about 0.82, but precision on the more realistic M57 Patents corpus (real, uncurated employee-machine disk images) dropping to roughly 0.52-0.63 - "none of the models reach high precision" against M57, even though many of the same models retain strong recall (up to 1.0) on both datasets. The paper attributes this gap to the more complex, less controlled nature of the M57 data compared to the deliberately staged controlled-machine scenarios.

## Why It Matters

An investigator using this triage technique to narrow a search space risks a meaningfully high false-positive rate on real-world disk images - the very setting the tool is meant to be used in - since the strong precision measured on controlled test machines does not carry over to realistic data. Treating a positive software-presence detection as confirmed without further verification could misdirect investigative effort toward software that was not actually present on the system.

## Related Mitigations

- [[mitigations/Manually verify positive software-signature detections before relying on them, especially outside controlled test conditions]]

## Used By

- [[techniques/Detect installed software using a paragraph-vector signature search engine]]

## References

- [DFCite-2021] Soltani et al., 2021 — Section V.C.2 and Figure 8 report M57-machine precision in the approximate range 0.52-0.63, well below the 0.795-0.82 range measured on controlled machines (Section V.C.1, Figure 4).
