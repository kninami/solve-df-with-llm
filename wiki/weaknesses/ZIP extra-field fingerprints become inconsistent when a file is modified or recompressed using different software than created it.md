---
id: LWW-1199
type: weakness
name: ZIP extra-field fingerprints become inconsistent when a file is modified or recompressed using different software than created it
description: When an existing ZIP archive is later added to, deleted from, or modified using a different application than the one that originally created it, only the headers of the changed entries reflect the modifying application's fingerprint while unchanged entries retain the original application's fingerprint, so a single archive can contain multiple coexisting, contradictory environment fingerprints that a naive single-fingerprint attribution would misread as one consistent creation environment.
categories:
  - ASTM_MISINT
mitigation_ids:
  - LWM-1199
source_refs:
  - LWCite-1210
updated_at: 2026-08-13
status: complete
---

# ZIP extra-field fingerprints become inconsistent when a file is modified or recompressed using different software than created it

## Summary

Experiments adding, deleting, and modifying individual files within an existing ZIP archive using a second application (SW2) showed that only the local file header and, where applicable, the central directory header of the changed entry are updated to reflect SW2's fingerprint; unrelated, unmodified entries in the same archive continue to show the original creating application's (SW1's) fingerprint. Deleting a file removes both its own fingerprint and, in some cases, its corresponding extra field from the remaining entries' headers, further complicating a whole-archive fingerprint read.

## Why It Matters

An investigator who examines only a single representative entry's extra-field fingerprint and generalizes it to the whole archive risks either missing evidence that the archive was modified after its initial creation, or misattributing the entire archive to whichever application happens to match the entry inspected. Since some fingerprint characteristics are target-file-dependent rather than purely environment-dependent (e.g. whether double-zipping recompresses unrelated entries), a full structural analysis of every entry's headers — not a spot check — is needed before concluding an archive was produced entirely by one application and OS.

## Related Mitigations

- [[mitigations/Cross-check ZIP extra-field fingerprints for mixed-software modification before attributing a single creation environment]]

## Used By

- [[techniques/Determine a ZIP file's creation environment using extra-field structural fingerprints]]

## References

- [LWCite-1210] Um et al., 2021, "File fingerprinting of the ZIP format for identifying and tracking provenance", FSI: Digital Investigation 39, 301271.
