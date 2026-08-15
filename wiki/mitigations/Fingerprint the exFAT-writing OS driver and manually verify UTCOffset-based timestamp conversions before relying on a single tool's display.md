---
id: DFM-1263
type: mitigation
name: Fingerprint the exFAT-writing OS driver and manually verify UTCOffset-based timestamp conversions before relying on a single tool's display
source_refs:
  - DFCite-1283
updated_at: 2026-08-14
status: complete
---

# Fingerprint the exFAT-writing OS driver and manually verify UTCOffset-based timestamp conversions before relying on a single tool's display

## Summary

Before treating a forensic tool's displayed exFAT timestamp as accurate, identify which operating system's driver actually wrote the relevant directory entry using root-directory artifacts and 10ms-increment field patterns, and manually verify the raw UTCOffset field's value in a hex viewer rather than relying solely on any single tool's automated interpretation.

## Addresses

- [[weaknesses/exFAT timestamp interpretation is unreliable across OS drivers and forensic tools due to inconsistent UTCOffset handling]]

## How To Apply

Inspect the exFAT volume's root directory for OS-fingerprinting artifacts (`.fseventsd`/`.Spotlight-V100` for MacOS usage, `System Volume Information` for Windows usage) and check whether the `UTCOffset` fields are uniformly valid or invalid (`0x00`) across a sample of directory entries, since a uniformly-invalid pattern indicates the Linux FUSE driver. Once the writing driver is identified, apply the correct interpretation rule for that driver rather than a fixed volume-wide assumption: treat FTK Imager's UTC+0 display as accurate only if the raw UTCOffset value is genuinely UTC+0; treat EnCase's and Autopsy's outputs as unverified whenever the underlying UTCOffset fields are invalid or the tool's selected timezone does not match the volume's actual writing conditions; and cross-check X-Ways' output against a raw hex-level read of the UTCOffset field whenever a directory entry shows a mix of valid and invalid offset values. Where the actual local time of the writing computer cannot be determined from the timestamp alone (e.g. Linux native driver volumes, which always store UTC+0 regardless of true local time), disclose this as an unresolved gap rather than presenting an assumed local time as fact.

## References

- [DFCite-1283] Nordvik and Axelsson, 2022 (corrigendum 2023), "It is about time — Do exFAT implementations handle timestamps correctly?", FSI: Digital Investigation 42-43, 301476.
