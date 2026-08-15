---
id: DFM-2058
type: mitigation
name: Use hash-digest matching against known-original images to detect image metadata tampering
source_refs:
  - DFCite-2058
updated_at: 2026-08-15
status: complete
---

# Use hash-digest matching against known-original images to detect image metadata tampering

## Summary

Where hashes of an image's original, untampered state are known, compute the hash digest of the image under analysis and match it against the known-original hash to detect whether the image's metadata has been manipulated, since metadata manipulation (e.g., with tools such as Exiftool) is otherwise a low-effort anti-forensic technique that most image forensics tools cannot independently detect.

## Addresses

- [[weaknesses/No single forensic tool satisfies all core and optional requirements when tested against a CFTT-aligned specification]]

## How To Apply

When a case involves images with a plausible known-original source (e.g., a suspect's device backup, a distributor's original upload, or a prior forensic acquisition), compute and retain hash digests at the earliest point of acquisition; when authenticity is later in question, recompute the hash of the image under analysis and compare it against the retained hash, and treat a mismatch combined with inconsistent or stripped EXIF metadata as an indicator of deliberate metadata manipulation rather than benign re-encoding.

## References

- [DFCite-2058] Khalid & Qadir, 2022, "An Evaluation Framework For Digital Image Forensics Tools", JDFSL 17(4). States that hash digests and hash-matching are "the single counter" to image metadata manipulation as an anti-forensic technique, provided hashes of the original image are known.
