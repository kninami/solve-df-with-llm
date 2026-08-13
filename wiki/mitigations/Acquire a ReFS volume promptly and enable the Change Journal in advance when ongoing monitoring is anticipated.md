---
id: DFM-1215
type: mitigation
name: Acquire a ReFS volume promptly and enable the Change Journal in advance when ongoing monitoring is anticipated
source_refs:
  - DFCite-1227
updated_at: 2026-08-13
status: complete
---

# Acquire a ReFS volume promptly and enable the Change Journal in advance when ongoing monitoring is anticipated

## Summary

Minimize the delay between an event of investigative interest and acquisition of a ReFS volume to reduce the chance that intervening write activity has overwritten the relevant Logfile transactions, and proactively enable the Change Journal on systems expected to require ongoing monitoring so a second, independently cross-checkable journal artifact is available.

## Addresses

- [[weaknesses/ReFS's circular-buffer journal cannot recover file events older than the buffer's retention window]]

## How To Apply

Prioritize acquisition of ReFS volumes as early as practical once a device or system is identified as relevant, since both the Logfile and the Change Journal continuously overwrite their oldest transactions during normal file-system use. On systems under an organization's own control where future incident investigation is anticipated (e.g. servers, monitored endpoints), enable the Change Journal in advance via `fsutil`, since it is disabled by default and, once enabled, provides an independent record that can cross-validate a Logfile-derived timeline. Where only the Logfile is available, document the reconstruction as bounded by the buffer's observed retention window rather than presenting it as a complete history of all file-system activity on the volume.

## References

- [DFCite-1227] Lee et al., 2021, "Forensic analysis of ReFS journaling", FSI: Digital Investigation 38.
