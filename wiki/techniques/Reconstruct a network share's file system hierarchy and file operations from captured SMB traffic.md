---
id: DFT-1275
type: technique
name: Reconstruct a network share's file system hierarchy and file operations from captured SMB traffic
description: Rebuild an SMB network share's original directory hierarchy, file content, multiple file versions, and metadata purely from a captured SMB network traffic file, and separately fingerprint the sequence of SMB commands a specific Windows API file operation produces so that recorded traffic can be interpreted as the underlying user activity that generated it, going beyond standard tools like Wireshark that only extract individual transferred files.
objective_ids:
  - DFO-1001
  - DFO-1002
weakness_ids:
  - DFW-1285
aliases:
  - Mount SMB.pcap
  - SMB Command Fingerprinting (SCF)
source_refs:
  - DFCite-1313
updated_at: 2026-08-15
status: complete
---

# Reconstruct a network share's file system hierarchy and file operations from captured SMB traffic

## Summary

When physical access to a device is unavailable or on-disk files have already been modified or deleted, an SMB network capture can substitute for direct file system access: parsing the SMB2/SMB3 protocol's CREATE, CLOSE, READ, WRITE, QUERY_INFO/SET_INFO, and QUERY_DIRECTORY commands recovers not just individual transferred files (as Wireshark does) but the share's full directory hierarchy, per-file metadata, multiple historical versions of the same file, and — by fingerprinting which sequence of SMB commands each Windows file-system API call produces — the specific user- or process-level file operations that generated the traffic.

## Details

**File system reconstruction**: CREATE requests carry a file or directory's full path relative to the share root (established via the preceding TREE_CONNECT), letting the hierarchy including parent directories be rebuilt; file content is recovered from READ/WRITE command payloads, and metadata (timestamps, attributes) from CREATE responses and SET_INFO commands. Because a capture can span the same file being created, modified, and deleted multiple times, each observed version is preserved as a distinct file rather than being overwritten, and an optional `--snapshot` feature layers the mounted hierarchy by point-in-time snapshot (a new snapshot directory is created whenever a rename or deletion is observed) so an investigator can navigate the share as it appeared at any captured moment. A mounting implementation lets investigators browse the reconstructed hierarchy with ordinary file system tools (`ls`, etc.), and also supports HTTP and FTP capture in addition to SMB. **SMB Command Fingerprinting (file operations)**: individual Windows API calls (`CreateFile`, `FindFirstFile`, and others) were systematically exercised against a live SMB share while simultaneously capturing network traffic and, via `frida-trace`, the API calls actually made, establishing which specific sequence and field values of SMB commands each API call and parameter combination produces (e.g. `CreateFile`'s `OPEN_ALWAYS`/`CREATE_NEW`/`CREATE_ALWAYS` dispositions each add an extra CREATE request targeting the parent directory; requesting write access under `OPEN_EXISTING` adds a QUERY_INFO for the file's normalized name). These fingerprints let an investigator work backward from an observed SMB command sequence to the specific higher-level file operation (and by extension, user interaction) that produced it, demonstrated end to end by reconstructing `cmd.exe` file-manipulation activity purely from its SMB traffic fingerprint.

## Examples

- Mounting a captured `test_share` SMB session with the `--show-metadata` flag displayed the share's reconstructed file names, hierarchy, and timestamps, including three distinct captured versions of the same file (`file2.txt`) as separate entries navigable with standard file system tools.
- Using the `--sortby` feature to organize the mounted hierarchy by source/destination IP and, for HTTP, by domain, surfaced network-context information (which host originated which file) that is otherwise concealed when the hierarchy is built purely from protocol structure.
- Applying SMB Command Fingerprinting rules derived from Windows API analysis, the researchers reconstructed specific `cmd.exe` file operations purely from the SMB command sequence observed in captured network traffic, without any access to the client or server file system itself.

## Related Objectives

- `DFO-1001` Reconstruct events
- `DFO-1002` Extract data from specific formats

## Related Weaknesses

- [[weaknesses/Reconstructing a network share's file system solely from SMB protocol structure conceals the source and destination hosts that produced it]]

## References

- [DFCite-1313] Hilgert, Mahr, and Lambertz, 2024, "Mount SMB.pcap: Reconstructing file systems and file operations from network traffic", FSI: Digital Investigation 50, 301807.
