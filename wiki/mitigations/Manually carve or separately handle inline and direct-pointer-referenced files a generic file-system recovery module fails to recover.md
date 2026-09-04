---
id: LWM-2102
type: mitigation
name: Manually carve or separately handle inline and direct-pointer-referenced files a generic file-system recovery module fails to recover
source_refs:
  - LWCite-2118
updated_at: 2026-08-16
status: complete
---

# Manually carve or separately handle inline and direct-pointer-referenced files a generic file-system recovery module fails to recover

## Summary

Where a new file-system module's automated deleted-file recovery is known to under-recover files stored via inline or direct-pointer addressing, supplement it with manual carving or file-system-specific low-level analysis targeted specifically at these alternative-addressing structures, rather than relying on the module's standard recovery pass alone.

## Addresses

- [[weaknesses/New TSK file-system modules recover inline and direct-pointer-referenced files at a much lower rate than standard indirect-block files]]

## How To Apply

Where the target file system supports inline data storage or direct-pointer addressing (as F2FS does), do not treat a module's standard deleted-file recovery pass as covering these cases with the same reliability as standard indirect-block files. Where feasible, apply targeted manual carving informed by the specific structure's known on-disk layout, or wait for and apply an updated module version specifically addressing this addressing type once available. Document in casework reporting that a lower recovery-confidence category (inline/direct-pointer files) may not be fully represented in an automated recovery pass's results.

## References

- [LWCite-2118] "Towards a practical usage for the Sleuth Kit supporting file system add-ons", FSI: Digital Investigation 48, 2024.
