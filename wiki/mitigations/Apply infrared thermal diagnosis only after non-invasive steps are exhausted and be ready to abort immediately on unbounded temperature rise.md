---
id: LWM-2039
type: mitigation
name: Apply infrared thermal diagnosis only after non-invasive steps are exhausted and be ready to abort immediately on unbounded temperature rise
source_refs:
  - LWCite-2039
updated_at: 2026-08-14
status: partial
---

# Apply infrared thermal diagnosis only after non-invasive steps are exhausted and be ready to abort immediately on unbounded temperature rise

## Summary

Follow the decision diagram's ordering strictly: exhaust non-invasive optical, X-ray, and acoustic-microscopy diagnosis, and obtain judicial authorization for invasive analysis, before applying infrared thermal imaging; during the test itself, monitor temperature continuously and be prepared to power down and stop the process the moment temperature rises without stabilizing, rather than waiting to see if it eventually plateaus.

## Addresses

- [[weaknesses/Infrared diagnostic imaging of a damaged SD card risks creating or worsening the fault it is meant to locate]]

## How To Apply

Run the infrared acquisition against a control (known-good) sample of the same or a similar card first, to establish an expected thermal baseline, then compare the evidentiary card's behavior against it in real time. Take frequent thermal snapshots at short time intervals from power-up, and define an explicit temperature or time-based abort threshold in advance so the decision to stop is not made reactively once damage risk is already elevated. Document the invasive nature of the technique and the authorization obtained before use, consistent with the protocol's own guidance that invasive techniques require prior judicial approval.

## References

- [LWCite-2039] Thomas-Brans et al., 2022 — the paper's own case study (Section IV.D.2) models this exact monitoring and stop-on-rise practice, halting analysis once the memory die's temperature climbed without stabilizing, to avoid further damage to the sample.
