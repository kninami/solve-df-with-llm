---
id: DFW-1165
type: weakness
name: Metaverse platforms do not log avatar motion or voice conversation content
description: Current metaverse platforms record only coarse activity such as which world an avatar joined and text messages sent through a linked messenger, but do not log an avatar's detailed in-world behavior — its motion or the content of its voice conversations — so an investigator cannot reconstruct exactly how a user acted or what they said while present in a shared metaverse space from currently available artifacts alone.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1165
source_refs:
  - DFCite-1167
updated_at: 2026-08-12
status: complete
---

# Metaverse platforms do not log avatar motion or voice conversation content

## Summary

Applying the five-area ecosystem forensic process to a simulated grooming scenario recovered which restricted world a suspect and victim both joined and confirmed text-based messenger contact, but was unable to recover any record of the avatar's in-world motion (e.g. following another avatar, physical gestures) or the content of any voice conversation that took place while both avatars were present in the world, because current metaverse platforms simply do not generate or retain that level of behavioral log by default.

## Why It Matters

For incidents whose most serious conduct occurs through in-world avatar behavior or spoken voice interaction rather than text messages — which describes many of the metaverse-specific harms (grooming, harassment, assault) that motivate metaverse forensic investigations in the first place — an investigator relying solely on currently available platform artifacts will be unable to establish exactly what occurred during the interaction, even when coarse evidence (shared world membership, timing, text contact) corroborates that some interaction took place.

## Related Mitigations

- [[mitigations/Petition the metaverse service provider for enhanced logs and corroborate with circumstantial artifacts]]

## Used By

- [[techniques/Apply a five-area ecosystem-based digital forensic process to metaverse platforms]]

## References

- [DFCite-1167] Kim et al., 2023, "Digital forensic approaches for metaverse ecosystems", FSI: Digital Investigation 46, 301608.
