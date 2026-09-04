---
id: LWT-1030
type: technique
name: Acquire vehicle ECU diagnostics using UDS-DoIP and analyze manipulation indicators
description: Acquire diagnostic data from a vehicle's Electronic Control Units (ECUs) over the standardized OBD-II interface using Diagnostic over IP (DoIP) and Unified Diagnostic Services (UDS) protocols, then inspect specific UDS data identifiers (programming date, firmware fingerprint, repair-shop/tester code) to detect indicators of unauthorized firmware or hardware manipulation.
objective_ids:
  - DFO-1006
weakness_ids:
  - LWW-1030
aliases:
  - UDS-DoIP vehicle ECU diagnostic acquisition and manipulation-indicator analysis
source_refs:
  - LWCite-1021
updated_at: 2026-08-09
status: complete
---

# Acquire vehicle ECU diagnostics using UDS-DoIP and analyze manipulation indicators

## Summary

Modern vehicles distribute functionality across many ECUs reachable through a standardized OBD-II diagnostic port. By connecting an OBD-II-to-Ethernet adapter and implementing the DoIP transport and UDS request/response protocols, an examiner can enumerate installed ECUs by their logical target addresses, then query each for specific diagnostic data identifiers that reveal whether its firmware was reprogrammed, and when, without requiring any additional in-vehicle forensic hardware such as an intrusion detection system or event data recorder.

## Details

A scanning application sweeps the full UDS target-address space (0x0000-0xffff) to discover installed ECUs, since internal documentation of the exact address map is often unavailable to the investigator. For each discovered ECU, specific UDS data identifiers are queried and compared to a known default/baseline configuration: `0xf199` (programming date), `0xf184` (application software fingerprint), `0xf198`/`0xf19a` (last repair-shop code or tester/calibration-equipment serial number), and `0xf180`/`0xf181`/`0xf183` (boot/application software identification and fingerprint). Network traffic is captured (e.g., with Wireshark and a protocol-specific dissector) and filtered to positive UDS responses to build an evidence trail; a change in the programming-date or fingerprint identifiers relative to the expected baseline indicates the firmware was reprogrammed after initial flashing.

## Examples

- On a 2018-model electric vehicle, over 100 logical ECU addresses were identified via a full target-address sweep, and diagnostic identifier queries filtered from 3800 to 245 relevant packets found no evidence of firmware reprogramming, allowing the investigator to rule out the manipulation scenario under investigation.

## Related Objectives

- `DFO-1006` Acquire data

## Related Weaknesses

- [[weaknesses/OBD-based diagnostic acquisition cannot reach in-vehicle components not connected to the diagnostic interface]]

## References

- [LWCite-1021] Gomez Buquerin et al., 2021, "A generalized approach to automotive forensics", FSI: Digital Investigation 36.
