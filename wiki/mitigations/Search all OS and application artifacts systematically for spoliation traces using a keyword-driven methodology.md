---
id: LWM-1176
type: mitigation
name: Search all OS and application artifacts systematically for spoliation traces using a keyword-driven methodology
source_refs:
  - LWCite-1176
updated_at: 2026-08-12
status: complete
---

# Search all OS and application artifacts systematically for spoliation traces using a keyword-driven methodology

## Summary

Before concluding that no evidence exists of a deleted file's prior existence, run a systematic keyword search (filename, content, renamed variants) across every OS and application artifact location known to record file-related metadata, rather than checking only the small set of previously-published, well-known trace sources.

## Addresses

- [[weaknesses/Failure to systematically enumerate spoliation-trace sources causes deleted-file evidence to be overlooked]]

## How To Apply

Build a target-specific dataset (create, access, modify, copy, up/download, and other actions on representative files) to first identify which system and application artifacts record file metadata for the OS/application versions under investigation, then classify each discovered source as previously "studied," "known but unanalyzed," or genuinely "unknown," reviewing current literature to avoid duplicating already-published analysis. Use unique filenames and content during any generated test dataset to avoid false-positive keyword matches, and re-run the artifact-source enumeration whenever the OS or key applications are updated, since artifact locations and formats can change between versions.

## References

- [LWCite-1176] Joun et al., 2023, "Discovering spoliation of evidence through identifying traces on deleted files in macOS", FSI: Digital Investigation 44, 301502.
