---
id: LWM-1202
type: mitigation
name: Verify whether location data recovered from an LLM app artifact is GPS-derived or IP-based geolocation before treating it as precise location evidence
source_refs:
  - LWCite-1215
updated_at: 2026-08-13
status: complete
---

# Verify whether location data recovered from an LLM app artifact is GPS-derived or IP-based geolocation before treating it as precise location evidence

## Summary

Before citing location information recovered from an LLM mobile app's conversation content or metadata as evidence of a user's physical location, determine whether it was derived from the device's GPS or from coarser IP-based geolocation, and report its likely precision accordingly rather than presenting it as a precise position.

## Addresses

- [[weaknesses/Location data recovered from an LLM mobile app artifact may reflect IP-based geolocation rather than the device's actual GPS position]]

## How To Apply

Check whether device location services were enabled at the time the artifact was generated and, where possible, correlate the recovered location with the device's actual network (Wi-Fi/cellular) connection records at that timestamp; a location result recovered despite location services being disabled should be treated as indicative of IP-based geolocation and reported with appropriately reduced confidence about precision (on the order of city/neighborhood-level rather than exact coordinates), rather than as an equivalent to a device-native GPS reading.

## References

- [LWCite-1215] Tyagi et al., 2025, "Forensic analysis and privacy implications of LLM mobile apps: A case study of ChatGPT, Copilot, and Gemini", FSI: Digital Investigation 54, 301974.
