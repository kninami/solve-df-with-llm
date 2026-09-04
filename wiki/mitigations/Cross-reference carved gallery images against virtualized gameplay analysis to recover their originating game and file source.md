---
id: LWM-1110
type: mitigation
name: Cross-reference carved gallery images against virtualized gameplay analysis to recover their originating game and file source
source_refs:
  - LWCite-1105
updated_at: 2026-08-12
status: complete
---

# Cross-reference carved gallery images against virtualized gameplay analysis to recover their originating game and file source

## Summary

After carving media files from a suspect application archive, virtualize the application and progress through it to observe which gallery images are displayed at which unlock point, then match the displayed content against the carved output to reconstruct each image's originating game and in-application location.

## Addresses

- [[weaknesses/File carving of virtualized game-gallery images does not preserve source-path metadata]]

## How To Apply

Run the carving pass first to recover the full set of static media, then separately virtualize the suspect application in an environment matched to the seized system and play through it, documenting which carved images correspond to which unlocked gallery section and game. Retain both the carved file set and the virtualization session log/screenshots so that provenance can be demonstrated even though it is not embedded in the carved files' own metadata.

## References

- [LWCite-1105] Jaeckel and Labudde, 2026, "Case note: Digital forensic challenges through synthetic CSAM in video games", FSI: Digital Investigation 57.
