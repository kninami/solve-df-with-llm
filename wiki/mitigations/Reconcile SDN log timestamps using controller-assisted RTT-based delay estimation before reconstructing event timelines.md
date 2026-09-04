---
id: LWM-1134
type: mitigation
name: Reconcile SDN log timestamps using controller-assisted RTT-based delay estimation before reconstructing event timelines
source_refs:
  - LWCite-1130
updated_at: 2026-08-12
status: complete
---

# Reconcile SDN log timestamps using controller-assisted RTT-based delay estimation before reconstructing event timelines

## Summary

Before merging infrastructure-, control-, and application-layer SDN logs into a single event timeline, have the controller measure and apply a per-switch delay correction so that timestamps recorded at different layers are adjusted onto a common, causally consistent reference before being compared or ordered.

## Addresses

- [[weaknesses/SDN log timestamps diverge across infrastructure, control, and application layers, misordering causally related events]]

## How To Apply

Configure the SDN controller to periodically probe each attached switch (e.g. via OpenFlow echo request/reply) and compute a smoothed round-trip delay estimate (an exponential moving average reduces sensitivity to transient jitter) for each switch. When correlating a controller-side decision timestamp with the corresponding switch-side effect timestamp for the same flow event, apply the estimated one-way delay as a correction before comparing the two, and record the applied correction alongside the reconciled timestamp so the reconciliation step itself is auditable. Combine this with contextual enrichment (attaching flow, topology, and controller-state metadata to each event) and hash-chained log integrity assurance so that reconciled, enriched logs remain both accurate and tamper-evident for later use as evidence.

## References

- [LWCite-1130] Koswane, Tabona and Maupong, 2026, "Controller-assisted timestamp reconciliation for reliable SDN forensics", FSI: Digital Investigation 58.
