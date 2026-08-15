---
id: DFW-1285
type: weakness
name: Reconstructing a network share's file system solely from SMB protocol structure conceals the source and destination hosts that produced it
description: Organizing a reconstructed network-capture file system purely by SMB share and tree hierarchy — the default mounting behavior — presents files and directories without their originating IP addresses, ports, or which specific host generated a given entry, discarding network-layer context that may be essential to attributing file activity to a specific machine.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1286
source_refs:
  - DFCite-1313
updated_at: 2026-08-15
status: complete
---

# Reconstructing a network share's file system solely from SMB protocol structure conceals the source and destination hosts that produced it

## Summary

Because the default mounted hierarchy is organized only by SMB server and share/tree name — mirroring how a traditional file system would present the data — the essential network capture artifacts that identify which specific machine (by IP address or port) sent or received a given file or command are not visible anywhere in the reconstructed hierarchy unless an investigator deliberately requests them.

## Why It Matters

An investigator browsing the default reconstructed file system with ordinary file system tools sees only file names, paths, and content — indistinguishable from a locally-imaged disk — and could easily overlook that the capture may span multiple source or destination hosts (e.g. several clients accessing the same share, or the same client's activity spanning several sessions), misattributing file activity to a single host or losing the ability to correlate specific files with the specific machine that created or accessed them.

## Related Mitigations

- [[mitigations/Use protocol-context sorting to preserve source and destination network metadata when mounting a reconstructed network-capture file system]]

## Used By

- [[techniques/Reconstruct a network share's file system hierarchy and file operations from captured SMB traffic]]

## References

- [DFCite-1313] Hilgert, Mahr, and Lambertz, 2024, "Mount SMB.pcap: Reconstructing file systems and file operations from network traffic", FSI: Digital Investigation 50, 301807.
