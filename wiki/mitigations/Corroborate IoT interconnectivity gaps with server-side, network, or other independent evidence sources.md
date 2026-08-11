---
id: DFM-1080
type: mitigation
name: Corroborate IoT interconnectivity gaps with server-side, network, or other independent evidence sources
source_refs:
  - DFCite-1070
updated_at: 2026-08-10
status: complete
---

# Corroborate IoT interconnectivity gaps with server-side, network, or other independent evidence sources

## Summary

Do not conclude that two IoT services or devices are unrelated solely because the interconnectivity-identification phase found no supporting trace; corroborate with independent evidence sources — server-side/cloud logs, network traffic captures, or the other party's own artifacts — before ruling out a suspected interconnection.

## Addresses

- [[weaknesses/IoT interconnectivity identification finds no relationship when the connected service retains no interconnection traces]]

## How To Apply

When investigative context (e.g. a suspect's known device inventory or prior statements) suggests two services or devices may be interconnected despite the local artifact-based interconnectivity phase finding nothing, pursue independent corroboration such as cloud/server-side logs (via legal process), network traffic captures, or artifacts from the other endpoint's own device, rather than treating the absence of local traces as proof the interconnection did not occur.

## References

- [DFCite-1070] Kim et al., 2022, "An improved IoT forensic model to identify interconnectivity between things", FSI: Digital Investigation 44.
