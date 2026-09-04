---
id: LWW-1139
type: weakness
name: Vision-based darknet contraband detectors degrade against deliberately obfuscated product imagery
description: An image-level object detector trained on typical contraband product photos can lose detection accuracy when a vendor deliberately degrades or obfuscates listing imagery — heavy blur, occlusion, watermarks, stock or off-topic images, or decoy banners — reducing recall on the very listings most likely to be evading detection on purpose.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-1139
source_refs:
  - LWCite-1137
updated_at: 2026-08-12
status: complete
---

# Vision-based darknet contraband detectors degrade against deliberately obfuscated product imagery

## Summary

While image-centric contraband classification reduces dependence on fragile text/HTML parsing, it is not immune to adversarial evasion by vendors who intentionally degrade or obfuscate their product imagery — for example heavy blur, occlusion, watermarks, substituting stock or off-topic images, or posting decoy banners — with the effect of reducing the detector's confidence or causing it to miss contraband content it would otherwise flag.

## Why It Matters

Because the confidence-gated pipeline is specifically designed to reduce false positives and only escalate borderline cases, systematic evasion of this kind can produce a corresponding rise in false negatives — genuinely contraband listings that are treated as background evidence rather than flagged for review — precisely for the population of vendors most motivated and sophisticated about avoiding detection, understating the true scope of harvested contraband content.

## Related Mitigations

- [[mitigations/Route low-confidence darknet imagery to human analyst review and periodically refresh the detection model to counter obfuscation drift]]

## Used By

- [[techniques/Harvest Tor hidden services using vision-based, parser-independent contraband classification]]

## References

- [LWCite-1137] Rathod et al., 2026, "DarkCatalog: A vision-first, parser-independent framework for forensic harvesting of TOR hidden services", FSI: Digital Investigation 57.
