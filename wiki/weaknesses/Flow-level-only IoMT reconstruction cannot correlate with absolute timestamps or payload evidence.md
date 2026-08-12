---
id: DFW-1017
type: weakness
name: Flow-level-only IoMT reconstruction cannot correlate with absolute timestamps or payload evidence
description: Because flow-level network forensic reconstruction uses cumulative inter-arrival time to build a relative synthetic timeline rather than absolute timestamps, and deliberately excludes packet payload inspection, it cannot be directly correlated with externally time-stamped events, system logs, or application-layer attack characteristics such as malformed payloads or protocol violations.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1017
source_refs:
  - DFCite-1011
updated_at: 2026-08-09
status: complete
---

# Flow-level-only IoMT reconstruction cannot correlate with absolute timestamps or payload evidence

## Summary

The temporal reconstruction is deliberately built on cumulative inter-arrival time because the underlying dataset lacks explicit absolute timestamps suitable for direct chronological reconstruction — a relative rather than absolute timeline. Separately, and by design, the framework restricts itself to flow-level metadata (packet headers, flow statistics) and does not inspect payloads, since encryption or regulatory constraints often make payload inspection infeasible in the target environment (e.g., healthcare IoMT networks).

## Why It Matters

A relative, synthetic timeline cannot be directly cross-referenced against other evidence sources that use real-world clock time — device logs, authentication records, or physical-world witness statements — without an additional step to anchor it to absolute time. Similarly, because payload inspection is out of scope, application-layer attack characteristics (malformed payloads, protocol violations) cannot be directly observed from this analysis alone, meaning findings should be understood as necessarily bounded by what flow metadata alone can reveal, not a complete account of an attack's technical mechanism.

## Related Mitigations

- [[mitigations/Corroborate flow-level reconstructions with absolute-timestamped logs and payload-level evidence]]

## Used By

- [[techniques/Reconstruct network events from flow-level artefacts]]

## References

- [DFCite-1011] Dias and Rao, 2026, "A forensic analysis framework for IoMT network traffic using temporal reconstruction and artefact profiling", FSI: Digital Investigation 57.
