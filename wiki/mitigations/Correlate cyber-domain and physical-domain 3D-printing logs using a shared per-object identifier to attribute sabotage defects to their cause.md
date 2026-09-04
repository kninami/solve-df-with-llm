---
id: LWM-1236
type: mitigation
name: Correlate cyber-domain and physical-domain 3D-printing logs using a shared per-object identifier to attribute sabotage defects to their cause
source_refs:
  - LWCite-1250
updated_at: 2026-08-13
status: complete
---

# Correlate cyber-domain and physical-domain 3D-printing logs using a shared per-object identifier to attribute sabotage defects to their cause

## Summary

Deploy both cyber-domain logging (OS, network, and application logs) and physical-domain sensor monitoring (kinetics and thermodynamics of the printer's direct-manipulable sub-processes) for a 3D-printing setup, and tag every printed object with a unique identifier shared across both domains' logs so a post-incident investigation can correlate a confirmed physical defect with the specific cyber-domain activity that produced it.

## Addresses

- [[weaknesses/3D-printing forensic logs from only the cyber or only the physical domain cannot independently attribute a sabotage defect to an attacker]]

## How To Apply

Assign each printed object a unique identifier (e.g. a compact digit scheme encoding the printer, print start date and time, and a per-batch object sequence number) at the start of a print job, and propagate that identifier into both the object's physical-domain sensor logs and the corresponding cyber-domain OS/network/application logs. During a post-incident investigation, use the shared identifier to pull the matching cyber and physical logs for a suspect object side by side: use the physical logs (space-domain geometry, thermodynamic profile, and timing profile) to characterize and rule out non-malicious causes for a detected defect, and use the cyber logs (login attempts, modified configuration files, network traffic) to identify the access path and mechanism, rather than relying on either domain's logs alone.

## References

- [LWCite-1250] Rais et al., 2023, "FRoMEPP: Digital forensic readiness framework for material extrusion based 3D printing process", FSI: Digital Investigation 44, 301510.
