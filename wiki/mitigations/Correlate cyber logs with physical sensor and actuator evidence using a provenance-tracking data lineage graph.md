---
id: LWM-2019
type: mitigation
name: Correlate cyber logs with physical sensor and actuator evidence using a provenance-tracking data lineage graph
source_refs:
  - LWCite-2019
updated_at: 2026-08-14
status: partial
---

# Correlate cyber logs with physical sensor and actuator evidence using a provenance-tracking data lineage graph

## Summary

Do not investigate a CPS incident's cyber evidence (logs, network traces) and physical evidence (sensor measurements, actuator states, environmental conditions) as separate workstreams; feed both into a provenance-tracking framework that converts raw logs into a verifiable data-lineage graph linking cyber events to their physical consequences.

## Addresses

- [[weaknesses/CPS forensic investigations analyze cyber and physical evidence in disjointed silos]]

## How To Apply

Deploy proactive logging that timestamps and correlates cyber-layer events (network traffic, control commands, log entries) with physical-layer telemetry (sensor readings, actuator state changes) from the same time window, and route both into a provenance-tracking pipeline (adaptor -> notification -> retrieval -> repository -> graph browser) so an investigator can trace a single incident's origins and evolution across both domains rather than reconciling separate cyber and physical evidence sets manually after the fact.

## References

- [LWCite-2019] K et al., 2026 — Section VIII.C "Key Insights" states that "meaningful analysis in this context requires correlating cyber artifacts...with physical evidence...timely" and presents provenance frameworks (Figure 15) as the mechanism for converting raw logs into a verifiable, integrated data lineage record.
