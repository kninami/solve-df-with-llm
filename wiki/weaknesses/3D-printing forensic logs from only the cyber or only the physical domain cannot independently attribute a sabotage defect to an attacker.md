---
id: DFW-1235
type: weakness
name: 3D-printing forensic logs from only the cyber or only the physical domain cannot independently attribute a sabotage defect to an attacker
description: OS, network, and application logs from a 3D printer's cyber domain can reveal that an intrusion occurred but cannot, on their own, prove that a specific detected defect in the printed object was caused by that intrusion, while physical-domain sensor data about the printed object's state can reveal a defect but cannot, on its own, identify who or what caused it.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1236
source_refs:
  - DFCite-1250
updated_at: 2026-08-13
status: complete
---

# 3D-printing forensic logs from only the cyber or only the physical domain cannot independently attribute a sabotage defect to an attacker

## Summary

If an attacked 3D-printed part fails during operation, the investigator must both identify the intruder and prove that the intruder's actions caused the defect that led to the failure. Cyber-domain logs (OS, application, network) can show that an attacker gained access and issued commands, but they cannot conclusively pin responsibility for a resulting physical defect on that access, since a defect could also stem from a hardware fault, material issue, or other non-malicious cause. Conversely, physical-domain sensor data (kinetics, thermodynamics) can reliably characterize a printed object's defect, including ruling out a hardware fault when the same anomaly recurs consistently across every layer, but it says nothing by itself about who manipulated the process or how.

## Why It Matters

An investigation that collects only one of the two domains is structurally incomplete for sabotage attribution: cyber-only logging leaves a "missing link" between confirmed unauthorized access and a specific physical outcome, while physical-only monitoring leaves a confirmed defect with no path back to an attacker or attack mechanism. Without a correlation mechanism tying both domains to the same printed object, an investigator risks either being unable to prove causation in court (cyber logs alone) or being unable to identify a suspect at all (physical logs alone).

## Related Mitigations

- [[mitigations/Correlate cyber-domain and physical-domain 3D-printing logs using a shared per-object identifier to attribute sabotage defects to their cause]]

## Used By

- [[techniques/Assess and design for digital forensic readiness]]

## References

- [DFCite-1250] Rais et al., 2023, "FRoMEPP: Digital forensic readiness framework for material extrusion based 3D printing process", FSI: Digital Investigation 44, 301510.
