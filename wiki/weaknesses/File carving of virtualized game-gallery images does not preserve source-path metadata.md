---
id: DFW-1110
type: weakness
name: File carving of virtualized game-gallery images does not preserve source-path metadata
description: When gated media-gallery images are recovered via file carving rather than direct extraction from a known application path, the carved output has no associated metadata linking each image back to the specific game, archive, or in-application location it originated from, so provenance must be reconstructed separately.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1110
source_refs:
  - DFCite-1105
updated_at: 2026-08-12
status: complete
---

# File carving of virtualized game-gallery images does not preserve source-path metadata

## Summary

The paper states this directly: "the images from the video game galleries were also found and processed in X-Ways using file carving. However, no metadata such as source paths could be reconstructed for them. Consequently, the origin of the images could only be determined after the game files were analysed in detail" (i.e. via virtualized gameplay).

## Why It Matters

An investigator who carves out media files from a suspect archive or executable without also analyzing the originating application's runtime behavior risks having a set of recovered images with no way to determine which specific game, gallery, or unlock condition each image belongs to — information that can matter for establishing which content was actually reachable, and therefore potentially viewed, by the accused.

## Related Mitigations

- [[mitigations/Cross-reference carved gallery images against virtualized gameplay analysis to recover their originating game and file source]]

## Used By

- [[techniques/Virtualize a suspect executable in a matched OS environment to unlock gated content for review]]

## References

- [DFCite-1105] Jaeckel and Labudde, 2026, "Case note: Digital forensic challenges through synthetic CSAM in video games", FSI: Digital Investigation 57.
