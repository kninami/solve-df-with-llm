---
id: DFW-1241
type: weakness
name: Client-attached geotag metadata on public social media maps can be poisoned with false locations undetected by the platform
description: A public social-media map feature displays media at the location its uploading user's client software attached to it, without the platform independently verifying that location against the media's actual content or capture location, so any user can broadcast media geotagged to an incorrect or fabricated location and the map will display it as if it were genuine, undetected by the platform.
categories:
  - ASTM_INAC_EX
mitigation_ids:
  - DFM-1242
source_refs:
  - DFCite-1256
updated_at: 2026-08-13
status: complete
---

# Client-attached geotag metadata on public social media maps can be poisoned with false locations undetected by the platform

## Summary

The authors note "a heavy reliance on trust is implied on the manner in which [the platform] presents [media] on a publicly accessible map," since the displayed location comes from client-attached metadata rather than server-side verification against the media's actual content or provenance. They illustrate the risk with an observed example: a video depicting what appeared to be a nonexistent oasis was geotagged to a location without any nearby body of water, demonstrating that a map's displayed location can diverge from where or what the media actually shows without any platform-level detection or flag.

## Why It Matters

An investigator using a harvested public social-media map as a surveillance or corroboration source is relying on user-supplied, unverified location metadata that any user (deliberately or accidentally) can misrepresent, meaning any single harvested item's displayed location cannot, by itself, be treated as reliable evidence that the depicted event occurred at that location. Because the platform performs no independent verification, a database-poisoning attack — deliberately uploading falsely-geotagged media to mislead anyone monitoring the map — is undetectable from the harvested data alone.

## Related Mitigations

- [[mitigations/Corroborate social-media-scraped surveillance location data with independent forensic verification before treating it as reliable]]

## Used By

- [[techniques/Harvest public social media location data using a reverse-engineered internal API]]

## References

- [DFCite-1256] Matthews et al., 2021, "Ghost protocol -- Snapchat as a method of surveillance", FSI: Digital Investigation 36, 301112.
