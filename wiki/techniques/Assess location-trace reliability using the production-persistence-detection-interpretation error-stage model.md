---
id: LWT-2103
type: technique
name: Assess location-trace reliability using the production-persistence-detection-interpretation error-stage model
description: Evaluate how much confidence to place in a device-derived location trace (GPS, Wi-Fi, cell-tower, or app-recorded coordinates) by systematically considering which of five distinct stages -- trace generation/production, persistence, detection/extraction, examination/display, and interpretation/reconstruction -- could have introduced uncertainty or error into the specific trace being relied upon, rather than treating a recovered coordinate as an unqualified fact about where a device was.
objective_ids:
  - DFO-1001
  - DFO-1004
weakness_ids:
  - LWW-2109
aliases:
  - Location-trace error taxonomy
source_refs:
  - LWCite-2128
updated_at: 2026-08-16
status: complete
---

# Assess location-trace reliability using the production-persistence-detection-interpretation error-stage model

## Summary

A recovered location coordinate is the end product of a long chain of hardware, software, storage, and analysis steps, any of which can introduce inaccuracy before the value ever reaches an investigator's screen. Structuring the assessment of a location trace's reliability around five distinct stages -- how the trace was originally produced, how it was subsequently persisted (or altered) in storage, how a forensic tool detected and extracted it, how the tool displayed it for examination, and how an investigator interprets and reconstructs an event from it -- gives a systematic checklist for identifying where a specific trace's uncertainty most plausibly originates, rather than treating "GPS error" as the only source of location-trace unreliability.

## Details

**Production**: the underlying positioning technology (GPS, Wi-Fi-based positioning, or cell-tower triangulation) has an inherent accuracy radius that varies by environment (open sky versus urban canyon versus indoors), and different positioning APIs on the same device can disagree for the same real-world location and moment, since they may draw on different underlying signal sources or calculation models. **Persistence**: an operating system or application may buffer, delay, throttle, or round a location update before writing it to permanent storage, particularly to conserve battery, meaning the stored timestamp and coordinate can reflect the buffering/writing event rather than the moment the position was actually measured. **Detection/extraction**: a forensic tool must correctly parse the specific database or file structure a location trace is stored in, and different structures encode fields (such as a special "unknown" or "invalid" value for latitude/longitude/accuracy) that a naive parser can silently misinterpret as a valid, precise coordinate rather than a placeholder. **Examination/display**: a forensic tool's own user interface can lose information present in the raw extracted data -- rounding a coordinate to fewer decimal places than the source stored, or omitting an available accuracy-radius field from the displayed table or map pin -- narrowing what an investigator sees relative to what is actually recoverable. **Interpretation/reconstruction**: even a technically accurate, precisely-displayed trace can be misinterpreted if an investigator conflates a "sent" location with a "received" one in a messaging context, assumes a single point represents certainty rather than a probable area, or fails to account for known API-specific systematic offsets when comparing traces from different sources for the same event.

## Examples

- An analyzed AirTag location-history buffering case showed a location update generated while a paired iPhone was in airplane mode was queued and only actually transmitted once connectivity resumed, several hours and roughly 1,734 km away from where the position was actually measured -- illustrating a persistence-stage error that, without awareness of this buffering behavior, could be badly misinterpreted at the reconstruction stage as evidence the tracked object physically moved that distance in that time window.
- A messaging application's local database was found to potentially swap which stored field represents a location the user sent versus one they received, a detection/extraction- or interpretation-stage risk that could reverse an investigator's conclusion about which party shared a location with whom.
- A specific iOS cache database field was found to use the value -1 to indicate an intentionally coarse or unknown accuracy/area (rather than a genuinely precise reading), which a forensic tool or investigator unaware of this convention could misread as a literal accuracy value.
- Comparing location data for the same journey through a metro tunnel as separately estimated by two different mapping-service APIs showed a measurable discrepancy between the two APIs' estimated positions for the same real-world moment, illustrating a production-stage inter-source disagreement independent of any storage or display issue.
- Forensic tool visualizations were observed to round latitude/longitude coordinates to fewer decimal places than the source data contained, and some tools omit any indication of a location fix's reported accuracy radius when displaying it on a map, both examination/display-stage information losses that narrow what an investigator can assess about a trace's actual precision.

## Related Objectives

- `DFO-1001` Reconstruct events
- `DFO-1004` Conduct research

## Related Weaknesses

- [[weaknesses/Location-based service APIs buffer, round, or omit precision metadata, causing device location traces to misrepresent actual position or timing]]

## References

- [LWCite-2128] "Uncertainty and error in location traces", FSI: Digital Investigation 48, 2024.
