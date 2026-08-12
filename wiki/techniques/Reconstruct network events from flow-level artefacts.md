---
id: DFT-1017
type: technique
name: Reconstruct network events from flow-level artefacts
description: Reconstruct attack timelines and prioritize suspicious traffic from network flow-level metadata alone (temporal, volume, statistical, and protocol-level features), without packet payload access, using cumulative inter-arrival time for relative timeline reconstruction and a lightweight classifier for triage.
objective_ids:
  - DFO-1001
  - DFO-1005
weakness_ids:
  - DFW-1017
aliases:
  - Flow-level network artefact forensic reconstruction
  - IoMT network traffic temporal reconstruction
  - flow-level forensic artefact profiling
source_refs:
  - DFCite-1011
updated_at: 2026-08-09
status: complete
---

# Reconstruct network events from flow-level artefacts

## Summary

When payload inspection is infeasible (encryption, privacy regulation, proprietary protocols — common in environments such as healthcare IoMT networks), an investigator can still reconstruct meaningful forensic evidence purely from flow-level metadata: inter-arrival time (temporal), total flow size (volume), min/max/mean/variance (statistical), and protocol presence (TCP/UDP/ICMP/ARP). These features support relative timeline reconstruction, attack-type attribution, and machine-learning-assisted triage that prioritizes suspicious flows for analyst review, without a real-time detection or courtroom-proof objective.

## Details

Temporal reconstruction builds a synthetic timeline per traffic class by cumulatively summing inter-arrival times (since absolute timestamps are often unavailable), producing a flow-accumulation curve whose shape (steep vs. gradual) reveals automated flooding versus organic benign communication. Protocol-level attribution links specific protocols to attack behaviors (e.g., dominant TCP for flooding/MQTT abuse, elevated ICMP for reconnaissance, ARP presence for spoofing) without requiring payload parsing. A supporting (not primary) machine-learning classifier — e.g., a Random Forest trained on the same interpretable features — is used purely for triage prioritization, deliberately kept auxiliary to preserve analyst judgement, interpretability, and traceability of conclusions to observable artefacts rather than opaque model output.

## Examples

- CICIoMT2024 dataset: flow accumulation curves distinguished benign IoMT telemetry (gradual, near-linear growth) from DoS/flooding and protocol-abuse attacks (steep, near-vertical accumulation within short intervals), and a Random Forest triage model achieved 0.93 macro-average precision across benign/DoS/MQTT/reconnaissance/spoofing traffic classes.

## Related Objectives

- `DFO-1001` Reconstruct events
- `DFO-1005` Prioritize digital evidence sources

## Related Weaknesses

- [[weaknesses/Flow-level-only IoMT reconstruction cannot correlate with absolute timestamps or payload evidence]]

## References

- [DFCite-1011] Dias and Rao, 2026, "A forensic analysis framework for IoMT network traffic using temporal reconstruction and artefact profiling", FSI: Digital Investigation 57.
