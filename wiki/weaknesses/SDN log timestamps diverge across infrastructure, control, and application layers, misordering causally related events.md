---
id: DFW-1134
type: weakness
name: SDN log timestamps diverge across infrastructure, control, and application layers, misordering causally related events
description: Switches, the controller, and applications in a software-defined network each timestamp events using their own local clock and logging pipeline, so an unreconciled cross-layer timeline can present a controller decision and its switch-side effect out of their true causal order.
categories:
  - ASTM_INAC_AS
  - ASTM_MISINT
mitigation_ids:
  - DFM-1134
source_refs:
  - DFCite-1130
updated_at: 2026-08-12
status: complete
---

# SDN log timestamps diverge across infrastructure, control, and application layers, misordering causally related events

## Summary

Because the SDN control plane (the controller) is physically and logically separated from the data plane (the switches), and both are separate again from any application-layer logging, the same real-world event (e.g. a flow rule being installed and then acted on) is recorded with independent local timestamps at each layer. Network transmission delay, clock drift, and differing logging pipeline latency between the layers mean these timestamps do not line up, so a naive merge of the logs can present events in an order that does not match what actually happened.

## Why It Matters

An investigator reconstructing an SDN-based incident (e.g. an attacker exploiting a controller vulnerability to reprogram switch flow tables) who trusts each layer's local timestamp without reconciliation risks concluding that a switch-side effect preceded its controller-side cause, or vice versa, undermining both the accuracy of the reconstructed timeline and its defensibility if challenged in court. The paper reports this cross-layer timestamp inconsistency as a core forensic readiness gap in SDN environments, distinct from ordinary single-host clock skew, because it is inherent to SDN's control/data-plane separation.

## Related Mitigations

- [[mitigations/Reconcile SDN log timestamps using controller-assisted RTT-based delay estimation before reconstructing event timelines]]

## Used By

- [[techniques/Reconcile cross-layer SDN forensic timestamps using controller-assisted delay estimation]]

## References

- [DFCite-1130] Koswane, Tabona and Maupong, 2026, "Controller-assisted timestamp reconciliation for reliable SDN forensics", FSI: Digital Investigation 58.
