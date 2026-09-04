---
id: LWM-1120
type: mitigation
name: Practice chip-off removal and restoration on a replica device and use standardized fitted fixtures before working the exhibit
source_refs:
  - LWCite-1112
updated_at: 2026-08-12
status: complete
---

# Practice chip-off removal and restoration on a replica device and use standardized fitted fixtures before working the exhibit

## Summary

Before attempting chip-off removal or restoration on the actual exhibit, rehearse the full procedure on an identical or similar test/replica device, and use base plates, clamps, and vices sized specifically for the target IC's package rather than improvised or generic fixtures, to avoid the mechanical and thermal precision failures that can outright destroy the chip.

## Addresses

- [[weaknesses/Chip-off removal or restoration handling can catastrophically fracture the target IC before it can be read]]

## How To Apply

Identify the exhibit's model/IC package from visible casing markings or online resources (retailer listings, teardown videos) and source a matching or similar test device to physically rehearse deconstruction, removal, and restoration before touching the exhibit. During restoration, use base plates and clamping fixtures measured and sized for the specific IC's dimensions — the source case's data-loss incident was traced to a base plate too narrow for the IC, allowing the vice to nip and split the chip — and continuously monitor temperature with a thermocouple during removal rather than judging solder liquefaction by time or visual estimate alone.

## References

- [LWCite-1112] Hadgkiss et al., 2022, "Cheap as chips: An accessible chip off acquisition method for ball grid array (BGA) integrated circuits in digital investigations", FSI: Digital Investigation 42-43.
