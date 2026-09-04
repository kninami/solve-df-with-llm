---
id: LWM-1252
type: mitigation
name: Monitor and dynamically resize the ARM stage-2 acquisition page pool, retrying during lower system load
source_refs:
  - LWCite-1266
updated_at: 2026-08-13
status: complete
---

# Monitor and dynamically resize the ARM stage-2 acquisition page pool, retrying during lower system load

## Summary

To reduce the chance of an ARM stage-2 fault-trapping memory acquisition aborting under heavy page-fault load, monitor the auxiliary pages pool's occupancy during acquisition, allow it to grow dynamically rather than using a fixed size, and prefer running the acquisition during a period of lower system activity where feasible.

## Addresses

- [[weaknesses/ARM stage-2 fault-trapping memory acquisition aborts under heavy page-fault load, producing no snapshot]]

## How To Apply

Where the acquisition tool supports it, configure or extend the pages pool to resize dynamically in response to observed fault rate, rather than relying on a fixed 1000-page (or similarly sized) allocation that can be overwhelmed under busy-mode loads (measured at up to roughly 50% in-coherency risk in testing). If a live system's workload can be safely reduced or paused briefly before acquisition (idle-mode testing showed in-coherency risk below 0.4%), do so; if the acquisition aborts due to pool overload, retry once load has decreased, and use the non-linear (low-CPU) acquisition mode over a constrained or metered network connection where a longer acquisition duration is an acceptable trade-off for lower processor and I/O impact.

## References

- [LWCite-1266] Yehuda, Shlingbaum, Gershfeld, Tayouri, and Zaidenberg, 2021, "Hypervisor memory acquisition for ARM", FSI: Digital Investigation 37, 301106.
