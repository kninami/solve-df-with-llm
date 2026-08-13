---
id: DFM-1244
type: mitigation
name: Prioritize full forensic-vault routing over battery savings during an active investigation
source_refs:
  - DFCite-1258
updated_at: 2026-08-13
status: complete
---

# Prioritize full forensic-vault routing over battery savings during an active investigation

## Summary

When a battery-performance-adaptive edge-cloud malware detection system (such as GreenForensics) is deployed on a device that is actively under forensic scrutiny or suspected of hosting an ongoing incident, configure its coverage/complexity controls to favor maximal cloud-vault routing coverage over battery or performance savings, rather than leaving the routing decision to the device's default power-management state.

## Addresses

- [[weaknesses/Battery-performance-conscious routing reduces cloud-vault forensic coverage of detected malware samples]]

## How To Apply

Where GreenForensics' discrete or continuous coverage controls are exposed to an administrator or investigator, explicitly override the default Power Mode-linked routing behavior to force full or near-full sample forwarding to the cloud vault for the duration of an active investigation, accepting the associated battery and network cost as justified by the evidentiary value of complete forensic capture. Where such controls are not exposed or cannot be safely overridden remotely, document which detection events may have received reduced-coverage handling so a reviewer can account for potential evidentiary gaps.

## References

- [DFCite-1258] Sewak, Sahay, and Rathore, 2022, "GreenForensics: Deep hybrid edge-cloud detection and forensics system for battery-performance-balance conscious devices", FSI: Digital Investigation 43, 301445.
