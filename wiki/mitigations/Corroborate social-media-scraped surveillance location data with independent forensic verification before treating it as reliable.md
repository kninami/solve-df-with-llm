---
id: LWM-1242
type: mitigation
name: Corroborate social-media-scraped surveillance location data with independent forensic verification before treating it as reliable
source_refs:
  - LWCite-1256
updated_at: 2026-08-13
status: complete
---

# Corroborate social-media-scraped surveillance location data with independent forensic verification before treating it as reliable

## Summary

Treat a harvested public social-media map item's displayed location and timestamp as an investigative lead rather than as verified fact, and corroborate it with independent media-forensic analysis or an unrelated evidence source before relying on it in an investigation or presenting it as evidence.

## Addresses

- [[weaknesses/Client-attached geotag metadata on public social media maps can be poisoned with false locations undetected by the platform]]

## How To Apply

Apply traditional media-forensic authentication tools and techniques to a harvested item's actual visual/audio content — checking for consistency between the depicted scene and the claimed location (landmarks, weather, shadows, signage) and for signs of manipulation — rather than accepting its displayed geotag at face value. Where possible, cross-reference harvested items against independent sources such as traditional CCTV footage, other witnesses' harvested content of the same event, or known ground-truth landmarks near the claimed location, and treat any item that cannot be independently corroborated as unverified.

## References

- [LWCite-1256] Matthews et al., 2021, "Ghost protocol -- Snapchat as a method of surveillance", FSI: Digital Investigation 36, 301112.
