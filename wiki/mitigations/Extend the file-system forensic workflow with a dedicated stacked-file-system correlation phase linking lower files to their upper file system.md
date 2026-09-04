---
id: LWM-1222
type: mitigation
name: Extend the file-system forensic workflow with a dedicated stacked-file-system correlation phase linking lower files to their upper file system
source_refs:
  - LWCite-1234
updated_at: 2026-08-13
status: complete
---

# Extend the file-system forensic workflow with a dedicated stacked-file-system correlation phase linking lower files to their upper file system

## Summary

After completing standard lower-file-system analysis, check for implementation-specific indicators of a stacked file system (distinctive hierarchies, header signatures, or extended attributes) and, if found, add a dedicated correlation step that recovers the upper file system's names, hierarchy, and content before concluding the examination.

## Addresses

- [[weaknesses/Standard file system forensic tools cannot associate a stacked file system's lower files with their corresponding upper files]]

## How To Apply

During lower-file-system analysis, watch for known stacked-file-system indicators: unusual `00`-`FF`-style hex-named directory hierarchies, hidden management directories, files whose names are UUIDs/GFIDs rather than meaningful identifiers, or distinctive fixed-header byte signatures at the start of otherwise-ordinary files. On finding such indicators, identify the specific stacked file system in use and consult its implementation details (open-source code, vendor documentation, or prior research) to determine whether upper/lower correlation requires only the lower file system's own metadata (local/unmanaged distributed systems) or extraction of a separate management-server metadata store (managed distributed systems). Extract and parse whichever metadata source is required, correlate each upper file to its lower file(s) via the resulting mapping, and only then treat the lower-file-system-only findings as complete, since the upper file system frequently contains the names and organizational context an investigator actually needs.

## References

- [LWCite-1234] Hilgert, Lambertz and Baier, 2024, "Forensic implications of stacked file systems", DFRWS EU 2024; FSI: Digital Investigation 48, 301678.
