---
id: LWT-2072
type: technique
name: Perform live selective imaging of file system data using a modular AFF4-based acquisition tool
description: Acquire only explicitly selected file system data objects and metadata from a running (live) Windows system into a partial forensic image, rather than a full bitwise copy, using a modular pipeline of artifact acquisition, integrity validation, and AFF4-container storage stages designed to preserve forensic soundness despite executing on the very system being examined.
objective_ids:
  - DFO-1006
  - DFO-1010
weakness_ids:
  - LWW-1132
aliases:
  - Selective Imaging Tool
  - SIT
source_refs:
  - LWCite-2080
updated_at: 2026-08-16
status: complete
---

# Perform live selective imaging of file system data using a modular AFF4-based acquisition tool

## Summary

As storage device capacity keeps growing, taking a full bitwise disk image before analysis wastes increasing amounts of time and space; selective imaging addresses this by copying only explicitly selected data objects, producing a considerably smaller partial image. Performing this selection live — running the imaging software on the system that holds the evidence, rather than after shutting it down — is necessary whenever a system cannot be powered off (e.g. to preserve volatile evidence or maintain availability), but is less well understood and tooled than traditional post-mortem selective imaging.

## Details

The Selective Imaging Tool (SIT) is a four-module pipeline built on the DFIR ORC framework, targeting modern Windows NTFS (and FAT) file systems. Its artifact module (a modified version of DFIR ORC's `GetThis` tool) locates and copies file system entries matching configured name/path/size criteria without altering the source, acquiring a wide range of metadata categories alongside each artifact including MD5, SHA1, and SHA256 hashes computed immediately at acquisition time; results are staged in ZIP archives with metadata temporarily held in a CSV file. Its validation module then acts as a fail-safe, re-checking the artifact module's output for interferences, corruption, or crashes as quickly as possible via error handling, artifact/metadata-consistency checks (e.g. missing metadata for a collected artifact), and a verification step that recomputes and compares all three hash codes for every artifact against those recorded during acquisition — flagging any mismatch as a possible sign of undetected tampering with collected evidence, and providing collision-resistant SHA256 verification per current NIST guidance. Its AFF4 module (an open, ZIP-based, extensible container format used elsewhere in disk imaging) stores both the acquired artifacts and their metadata together, converting validated output into an RDF Turtle central metadata registry so that direct associations between a file object and its metadata (including compression, size, and custom XML-Schema-typed fields) persist within the resulting image and can be interchangeably referenced by URL between investigators. The four modules are designed to run sequentially but can each be repeated, executed independently, or disabled — e.g. disabling the validation module trades soundness assurance for raw performance — and a backup archive of all acquired artifacts serves as an additional redundancy against corruption.

## Examples

- SIT is fully open-source (available on GitLab) and is, per its authors, the only known open-source tool offering selective live imaging of file system data with comparable reliability and integrity safeguards for Windows live systems.
- A general set of five live-selective-imaging soundness priorities — minimize source corruption, ensure evidence authenticity/integrity, provide extensive documentation, ensure digital reliability/security, and ensure physical reliability/security — informed SIT's modular design, including its logging of every action to console output for user review during acquisition.

## Related Objectives

- `DFO-1006` Acquire data
- `DFO-1010` Preserve digital evidence

## Related Weaknesses

- [[weaknesses/Autonomous system processes and forensic tool vulnerabilities inadvertently alter or destroy evidence during acquisition or examination]]

## References

- [LWCite-2080] Faust, Thierry, Müller, and Freiling, 2021, "Selective Imaging of File System Data on Live Systems", FSI: Digital Investigation 36, 301115.
