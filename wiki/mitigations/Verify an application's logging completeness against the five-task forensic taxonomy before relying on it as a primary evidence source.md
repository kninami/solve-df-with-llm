---
id: DFM-1293
type: mitigation
name: Verify an application's logging completeness against the five-task forensic taxonomy before relying on it as a primary evidence source
source_refs:
  - DFCite-1323
updated_at: 2026-08-15
status: complete
---

# Verify an application's logging completeness against the five-task forensic taxonomy before relying on it as a primary evidence source

## Summary

Before relying on an application's own logs as a primary source of timeline or correlation evidence, check whether they actually contain timestamps, unique identifiers, and sufficient user-action and exception detail — do not assume adequacy, and supplement with external evidence sources (OS-level logs, network captures, file system metadata) where gaps are found.

## Addresses

- [[weaknesses/Open-source application logs commonly omit timestamps and unique identifiers needed for forensic event correlation]]

## How To Apply

Using [[techniques/Assess an application's log adequacy for forensic use against a five-task taxonomy]], check the specific application's log output (or, where source is available, its logging source code) for each of the five task requirements before an investigation depends on it. Where an application's logs lack timestamps or correlation identifiers, do not attempt to reconstruct a timeline or correlate events from the application's own logs alone — cross-reference with system-level logs, network traffic captures, or file system timestamp metadata that can supply the missing timing or correlation information instead.

## References

- [DFCite-1323] Azahari and Balzarotti, 2024, "On the inadequacy of open-source application logs for digital forensics", FSI: Digital Investigation 49, 301750.
