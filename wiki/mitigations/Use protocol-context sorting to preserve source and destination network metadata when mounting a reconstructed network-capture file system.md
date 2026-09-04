---
id: LWM-1286
type: mitigation
name: Use protocol-context sorting to preserve source and destination network metadata when mounting a reconstructed network-capture file system
source_refs:
  - LWCite-1313
updated_at: 2026-08-15
status: complete
---

# Use protocol-context sorting to preserve source and destination network metadata when mounting a reconstructed network-capture file system

## Summary

When mounting a reconstructed network-capture file system for investigative review, use a sorting/hierarchy feature that includes source and destination IP addresses, ports, and protocol-specific identifiers (e.g. HTTP domain) as directory levels, rather than the default protocol-only hierarchy, so network-layer attribution remains visible alongside the reconstructed file content.

## Addresses

- [[weaknesses/Reconstructing a network share's file system solely from SMB protocol structure conceals the source and destination hosts that produced it]]

## How To Apply

When using [[techniques/Reconstruct a network share's file system hierarchy and file operations from captured SMB traffic]], mount the capture with a `--sortby` (or equivalent) option configured to include source/destination IP and port at minimum, and any available protocol-specific identifiers (domain, URI, share name) as needed for the case. Where multiple hosts or sessions are present in the same capture, confirm the resulting hierarchy separates their file activity before drawing conclusions about which host performed a given file operation, and record which hierarchy configuration was used to reproduce the analysis if challenged.

## References

- [LWCite-1313] Hilgert, Mahr, and Lambertz, 2024, "Mount SMB.pcap: Reconstructing file systems and file operations from network traffic", FSI: Digital Investigation 50, 301807.
