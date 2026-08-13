---
id: DFM-1228
type: mitigation
name: Configure a broad default trigger set and a technical-supervisor manual override for autonomous-vehicle forensic incident recorders
source_refs:
  - DFCite-1239
updated_at: 2026-08-13
status: complete
---

# Configure a broad default trigger set and a technical-supervisor manual override for autonomous-vehicle forensic incident recorders

## Summary

Reduce the gap between a forensic incident recorder's predefined trigger set and real-world unanticipated events by combining a deliberately broad, threat-analysis-derived default trigger list with a manual retention-activation capability that a qualified technical supervisor (or another involved vehicle) can invoke whenever an irregularity merits closer scrutiny even though it has not yet crossed a preset threshold.

## Addresses

- [[weaknesses/Autonomous-vehicle forensic incident recorders miss events that never fire a predefined trigger]]

## How To Apply

Derive the recorder's trigger set from a comprehensive Threat Analysis and Risk Assessment (TARA) rather than an ad hoc list, and supplement it with an AI-based best-guess relevance estimator that can flag and retain data for scenarios outside the predefined trigger catalogue, treating its output as an assistive signal rather than a fully accurate classifier. Empower an authorized technical supervisor to manually trigger permanent retention whenever an irregularity is suspected (for example, following an external report or a police warning) even absent a matching automated trigger, and allow an incident-involved vehicle to broadcast a trigger to other nearby vehicles so their recorders act as corroborating technical witnesses for an incident they were not the direct subject of.

## References

- [DFCite-1239] Dološ et al., 2026, "Forensic readiness for autonomous mobility: The forensic incident recorder and information system concept", FSI: Digital Investigation 56, 302044.
