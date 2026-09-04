---
id: LWM-1066
type: mitigation
name: Seize and directly examine the source smartwatch to strengthen audio file authentication
source_refs:
  - LWCite-1056
updated_at: 2026-08-10
status: complete
---

# Seize and directly examine the source smartwatch to strengthen audio file authentication

## Summary

Where possible, seize and directly examine the smartwatch that originated a questioned audio file, rather than relying on the audio file alone, so that the device's own file-system timestamps can be cross-checked against the audio file's internal timestamps and file-naming convention.

## Addresses

- [[weaknesses/Audio-file-only smartwatch recording authentication is weaker than authentication backed by the source device]]

## How To Apply

If the originating smartwatch is available, use the Smart Development Bridge (SDB) tool to access its file system directly and extract file creation/modification timestamps for comparison against the audio file's embedded name and container-atom timestamps, applying the method's two authentication criteria (file-system modification time equals change time; file-name time is no later than the internal creation time). Where the device is unavailable, treat spectral- and metadata-only authentication as provisional and note the reduced evidentiary strength in the report.

## References

- [LWCite-1056] Park et al., 2024, "Advanced forensic method to authenticate audio files from Tizen-based Samsung Galaxy Watches", FSI: Digital Investigation 48.
