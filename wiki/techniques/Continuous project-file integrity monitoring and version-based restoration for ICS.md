---
id: DFT-1053
type: technique
name: Continuous project-file integrity monitoring and version-based restoration for ICS
description: Continuously monitor a PLC engineering workstation's project files (the ladder-logic program source, e.g., Siemens TIA Portal's .plf/.idx pair) for size or content changes, collect and hash-verify each new version into a version-history database as soon as a change is detected, and restore any prior version on demand — detecting and recovering from unauthorized PLC logic tampering without directly investigating the live PLC, which would risk its continuous availability.
objective_ids:
  - DFO-1019
weakness_ids:
  - DFW-1056
aliases:
  - TIAMon
  - TIAMachine
source_refs:
  - DFCite-1046
updated_at: 2026-08-09
status: complete
---

# Continuous project-file integrity monitoring and version-based restoration for ICS

## Summary

Directly investigating a PLC to detect a cyber-attack (via memory or network forensics on the controller itself) risks compromising the ICS's availability, which must be maintained continuously in critical infrastructure. Because attacks that alter PLC logic (such as Stuxnet) do so by first compromising the engineering workstation (EWS) and modifying its project files before the changed logic is transmitted to the PLC, monitoring and versioning those project files provides a way to detect and respond to such attacks without touching the operational controller.

## Details

A watchdog component periodically checks whether the project file pair's size has changed or whether a new record has appeared in the file's internal index; on any change, it collects the updated file pair, computes MD5 and SHA1 hashes, and inserts a new versioned record (with acquisition time, path, size, and both hash values) into a SQLite database, distinguishing this from routine authorized edits made through the vendor's own engineering software (which are also tracked, not just malicious direct binary modification). A separate restoration component queries the database by project and then by a specific historical event, retrieves the corresponding stored file-pair version, and writes it back to a chosen recovery location, verifying the restored files' hashes against the stored record to confirm successful, unaltered recovery.

## Examples

- Simulating a Stuxnet-style attack against a Siemens TIA Portal Step 7 project (SIMATIC S7-1200 PLC) that modified the ladder logic via a malicious DLL exploiting an insecure-library-loading vulnerability: the monitoring tool detected the resulting project file size/content change (adding 200,425 bytes) both when the change was made through the TIA Portal and when the project file's binary was directly modified with a hex editor, and successfully restored the pre-attack version with matching hash values in both cases.

## Related Objectives

- `DFO-1019` Detect anti-forensics and other anomalies

## Related Weaknesses

- [[weaknesses/ICS project-file monitoring and restoration tooling lacks its own performance and security evaluation]]

## References

- [DFCite-1046] Shin et al., 2022, "A study on command block collection and restoration techniques through detection of project file manipulation on engineering workstation of industrial control system", FSI: Digital Investigation 40.
