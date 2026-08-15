---
id: DFM-1258
type: mitigation
name: Obtain a full physical image of an infotainment system's storage chip before installing any jailbreak or extraction software, when hardware access allows
source_refs:
  - DFCite-1275
updated_at: 2026-08-14
status: complete
---

# Obtain a full physical image of an infotainment system's storage chip before installing any jailbreak or extraction software, when hardware access allows

## Summary

Where the necessary hardware access, tooling, and time are available, obtain a bit-for-bit physical dump of an infotainment system's storage chip (e.g. via chip-off or in-system programming) before installing any software jailbreak, so that a pristine pre-modification copy exists even if the jailbreak's own installation later overwrites recoverable deleted data.

## Addresses

- [[weaknesses/Installing a software jailbreak to gain forensic access to an infotainment system risks overwriting recoverable deleted data before acquisition]]

## How To Apply

Before applying any jailbreak, daemon-installer, or SSH-mod package to an infotainment system, first attempt a full physical extraction of its storage chip (chip-off, in-system programming, or JTAG, as hardware access permits) to preserve an unmodified baseline image, then run standard SQLite parsing and unallocated-space carving against that image independently of the jailbreak-based extraction. Where physical extraction is genuinely infeasible (e.g. the tooling for a specific chip package does not yet exist, as documented for some SYNC 3 hardware revisions), document that the jailbreak-based logical extraction is a lower-fidelity fallback, note the specific jailbreak/daemon files installed and their approximate write footprint, and disclose the resulting integrity limitation in the investigative report rather than presenting the extraction as equivalent to a bit-for-bit physical image.

## References

- [DFCite-1275] Antonson, Quick and Choo, 2025, "Infotainment system Forensics: Ford SYNC 3 gen 2 infotainment system as a use case", FSI: Digital Investigation 53, 301917.
