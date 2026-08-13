---
id: DFM-1199
type: mitigation
name: Cross-check ZIP extra-field fingerprints for mixed-software modification before attributing a single creation environment
source_refs:
  - DFCite-1210
updated_at: 2026-08-13
status: complete
---

# Cross-check ZIP extra-field fingerprints for mixed-software modification before attributing a single creation environment

## Summary

Before attributing a ZIP archive to a single creating application or OS, inspect the extra-field structure of every local and central-directory header individually rather than sampling one entry, since post-creation modification by a second application only changes the headers of the entries it touched.

## Addresses

- [[weaknesses/ZIP extra-field fingerprints become inconsistent when a file is modified or recompressed using different software than created it]]

## How To Apply

Run the automated extra-field classifier against every entry's local and central-directory header in the archive, not just a representative sample, and flag any archive where different entries' fingerprints disagree. Where fingerprints disagree, treat this as evidence of a modification history rather than an ambiguous read: the entries carrying a distinct fingerprint were likely added, deleted, or modified after the archive's initial creation, and the inconsistency itself is corroborating evidence of alteration timing and tooling that can be reported alongside the file's contents.

## References

- [DFCite-1210] Um et al., 2021, "File fingerprinting of the ZIP format for identifying and tracking provenance", FSI: Digital Investigation 39, 301271.
