---
id: LWM-2065
type: mitigation
name: Search likely evidence locations for a surviving copy of a suspect image's original cover file
source_refs:
  - LWCite-2067
updated_at: 2026-08-15
status: complete
---

# Search likely evidence locations for a surviving copy of a suspect image's original cover file

## Summary

When steganography is suspected in an image, actively search a comprehensive list of likely locations for a surviving, unmodified copy of the same original image, rather than defaulting to unreliable statistical steganalysis of the suspect payload image alone, since human error and technical limitations frequently leave a copy of the original behind even when a suspect intended to wipe it.

## Addresses

- [[weaknesses/Statistical steganalysis without a located original cover image is unreliable and can be defeated by data-wiping the cover file]]

## How To Apply

Search the following locations, among others, for a same-dimension, visually similar candidate original image: the suspect's own hard drive filesystem, removable USB drives, cameras and mobile devices, CDs/DVDs, local and cloud email inboxes/outboxes, recent web search and browser histories (including Google Image searches), network-attached storage devices, employment computers and networks, recycle bins (including already-deleted files removed from recycle bins), online photo galleries, and personal or business associates' files and devices. Once a visually similar candidate is found, use file hash values to identify any additional exact copies already residing on the same file system, and use bit-plane comparison software (see [[techniques/Detect image LSB steganography using bit-plane cover-image comparison]]) to confirm the match and pinpoint exactly which bit planes were modified before treating the result as evidence.

## References

- [LWCite-2067] Pelosi & Easttom, 2021, "Positive Identification of Least Significant Bit (LSB) Image Steganography Using Cover Image Comparisons", JDFSL 15(6). Provides the 14-location checklist for locating a candidate original cover image and recommends "an active search for the original image if suspicion of steganographic usage exists."
