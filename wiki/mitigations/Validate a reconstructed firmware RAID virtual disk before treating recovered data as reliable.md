---
id: LWM-1167
type: mitigation
name: Validate a reconstructed firmware RAID virtual disk before treating recovered data as reliable
source_refs:
  - LWCite-1168
updated_at: 2026-08-12
status: complete
---

# Validate a reconstructed firmware RAID virtual disk before treating recovered data as reliable

## Summary

After reconstructing a deleted firmware RAID virtual disk from inferred parameters, verify both that the resulting volume mounts cleanly and that its file system structures and sampled file contents are internally consistent, iterating on stripe size and disk order candidates until validation succeeds, rather than accepting the first reconstruction that produces a mountable volume.

## Addresses

- [[weaknesses/Guessed stripe size or disk order silently produces a misaligned firmware RAID reconstruction]]

## How To Apply

Where possible, prefer parameters recovered directly from metadata (as is generally available for AMD, and for Intel's still-active virtual disks) over guessed values. When inference is unavoidable (deleted Intel volumes), iterate through the RAID level's common stripe-size values and candidate disk orderings, and after each attempt load a handful of known or expected sample files from the reconstructed volume into a standard forensic tool (e.g. FTK Imager) to confirm their content is intact and uncorrupted, rather than relying on "the volume mounted" alone as proof of correct reconstruction. Where file system artifacts (such as an NTFS `$Upcase` file) are available, use them to cross-check the inferred stripe size before finalizing the reconstruction.

## References

- [LWCite-1168] Yun et al., 2025, "Digital forensic approaches to Intel and AMD firmware RAID systems", FSI: Digital Investigation 54, 301971.
