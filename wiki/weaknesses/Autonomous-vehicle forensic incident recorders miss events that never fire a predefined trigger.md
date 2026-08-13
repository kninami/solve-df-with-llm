---
id: DFW-1228
type: weakness
name: Autonomous-vehicle forensic incident recorders miss events that never fire a predefined trigger
description: A ring-buffer-based forensic incident recorder only moves data to permanent storage when a predefined trigger (airbag deployment, IDS alert, plausibility-check failure) fires, so an unanticipated failure mode or a novel attack that does not match any predefined trigger is overwritten by the ring buffer and permanently lost.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1228
source_refs:
  - DFCite-1239
updated_at: 2026-08-13
status: complete
---

# Autonomous-vehicle forensic incident recorders miss events that never fire a predefined trigger

## Summary

The proposed Forensic Incident Recorder architecture stores high-resolution sensor, V2X, and diagnostic data in a ring buffer that is continuously overwritten unless a specific trigger (safety-system activation, IDS alert, critical system failure, sensor/communication anomaly, or manual technical-supervisor intervention) moves the relevant window to permanent local storage. Because the standard-data set and its trigger list cannot realistically anticipate every possible incident type given autonomous-vehicle ecosystems' data volume and novelty, an event that does not match a predefined trigger condition leaves no permanent record at all.

## Why It Matters

An investigator reconstructing an incident that stemmed from a genuinely novel failure mode, an attack technique not covered by the vehicle's Intrusion Detection System signatures, or a subtle degradation that does not cross any predefined anomaly threshold will find the relevant high-resolution sensor and V2X data already overwritten by the time an investigation begins, even though the recorder was functioning correctly throughout — the gap is a design limitation of trigger-based retention, not an equipment failure. This risk is structurally similar to, but distinct from, general volatile-evidence loss: here the data was captured into the buffer but discarded because no trigger recognized its relevance, rather than being lost due to a shutdown or acquisition-timing problem.

## Related Mitigations

- [[mitigations/Configure a broad default trigger set and a technical-supervisor manual override for autonomous-vehicle forensic incident recorders]]

## Used By

- [[techniques/Assess and design for digital forensic readiness]]

## References

- [DFCite-1239] Dološ et al., 2026, "Forensic readiness for autonomous mobility: The forensic incident recorder and information system concept", FSI: Digital Investigation 56, 302044.
