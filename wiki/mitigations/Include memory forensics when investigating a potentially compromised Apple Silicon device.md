---
id: LWM-1092
type: mitigation
name: Include memory forensics when investigating a potentially compromised Apple Silicon device
source_refs:
  - LWCite-1084
updated_at: 2026-08-10
status: complete
---

# Include memory forensics when investigating a potentially compromised Apple Silicon device

## Summary

When investigating a potentially compromised Apple Silicon Mac, acquire and analyze the device's memory in addition to a disk image, since Rosetta-2-translated Intel malware can use memory-only execution techniques that leave no trace on disk.

## Addresses

- [[weaknesses/Memory-only Intel malware execution techniques remain fully functional under Rosetta 2 on Apple Silicon]]

## How To Apply

Include memory acquisition as a standard step in Apple Silicon incident response, not only disk imaging, and use memory-forensics tooling capable of analyzing Apple Silicon memory images to look for indicators of memory-only-loaded code, unusual process/library loading patterns, or other artifacts consistent with Rosetta-2-translated Intel malware that would not appear in a disk-only examination.

## References

- [LWCite-1084] Mettig et al., 2023, "Assessing the threat of Rosetta 2 on Apple Silicon devices", FSI: Digital Investigation 46.
