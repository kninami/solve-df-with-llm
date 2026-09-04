---
id: LWM-2043
type: mitigation
name: Switch to streaming encryption or enforce a size ceiling before storing large potential digital evidence
source_refs:
  - LWCite-2044
updated_at: 2026-08-14
status: partial
---

# Switch to streaming encryption or enforce a size ceiling before storing large potential digital evidence

## Summary

Before deploying a Fernet-based (or similarly whole-file-in-memory) secure evidence storage pipeline in an environment that may need to store large potential digital evidence, either replace the encryption approach with a streaming-capable scheme that encrypts data in chunks, or enforce an explicit maximum file-size ceiling matched to the deployment's available memory and route oversized evidence through a separate acquisition/preservation workflow.

## Addresses

- [[weaknesses/Fernet-based whole-file-in-memory encryption limits the practical size of securely stored evidence]]

## How To Apply

Where the organization's expected potential digital evidence includes large artifacts (memory dumps, disk images, video), replace or supplement the whole-file encryption library with a streaming/chunked encryption implementation that does not require the full file in memory at once. Where replacing the encryption library is not feasible in the near term, size the deployment's available RAM to comfortably exceed the largest PDE expected, and configure the ingestion API to reject or redirect files exceeding a documented size ceiling rather than allowing an oversized ingestion attempt to risk memory exhaustion.

## References

- [LWCite-2044] Singh et al., 2022 — the paper's own future-work discussion (Section VIII) lists switching to file-streaming as the identified fix for this limitation.
