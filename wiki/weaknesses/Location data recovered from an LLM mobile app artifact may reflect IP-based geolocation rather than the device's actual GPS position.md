---
id: LWW-1202
type: weakness
name: Location data recovered from an LLM mobile app artifact may reflect IP-based geolocation rather than the device's actual GPS position
description: An LLM mobile app can return and store location-specific results (e.g. nearby-business answers, location-tagged conversation metadata) even when the device's location service is explicitly disabled, most plausibly via IP-based geolocation of the network connection rather than the device's GPS; an investigator who treats this recovered location data as a precise on-device GPS reading risks over-stating its accuracy.
categories:
  - ASTM_MISINT
mitigation_ids:
  - LWM-1202
source_refs:
  - LWCite-1215
updated_at: 2026-08-13
status: complete
---

# Location data recovered from an LLM mobile app artifact may reflect IP-based geolocation rather than the device's actual GPS position

## Summary

With the device location service disabled throughout testing, ChatGPT (Android and iOS) still answered a "nearest restaurant" prompt with specific nearby business names, addresses, and distances, and Gemini's Google Takeout export contained location coordinates recorded during the same disabled-location testing window; Copilot similarly returned location results accurate to within roughly a 0.5-mile radius. The study's authors note IP-based geolocation of the device's network connection as the most plausible explanation, since prior work has found such IP-geolocation databases are not consistently reliable for determining exact user positions.

## Why It Matters

If an investigator reports location data recovered from an LLM app's conversation history or metadata as though it were a precise, GPS-derived record of the user's physical location, the finding may overstate the artifact's actual precision and reliability, since IP-based geolocation is coarser and can be inaccurate. Because this occurs even when the user has taken the ordinary privacy step of disabling location services, an investigator should not assume the absence of enabled location permissions rules out location-related evidence being present, nor assume that when present it necessarily reflects the device's true GPS position.

## Related Mitigations

- [[mitigations/Verify whether location data recovered from an LLM app artifact is GPS-derived or IP-based geolocation before treating it as precise location evidence]]

## Used By

- [[techniques/Collect conversational AI artifacts across cloud export, desktop cache, browser cache, and mobile app storage]]

## References

- [LWCite-1215] Tyagi et al., 2025, "Forensic analysis and privacy implications of LLM mobile apps: A case study of ChatGPT, Copilot, and Gemini", FSI: Digital Investigation 54, 301974.
