---
id: LWM-2020
type: mitigation
name: Adapt cross-transferable digital forensics, CPS forensics, and reliability-analysis methodology pending CAV-specific standards
source_refs:
  - LWCite-2020
updated_at: 2026-08-14
status: partial
---

# Adapt cross-transferable digital forensics, CPS forensics, and reliability-analysis methodology pending CAV-specific standards

## Summary

Until CAV-specific forensic standards and validated tools exist, ground a CAV investigation in ISO/IEC 27037's general evidence-handling requirements and draw transferable methodology from four adjacent, more mature fields: conventional digital forensics (shared connected-node investigation techniques), cyber-physical-system forensics (directly transferable given CAVs are a CPS subset), software reliability analysis (to preemptively identify manufacturer-specific component weaknesses investigators should focus on), and penetration testing (to assess the CAV's IoT-device attack surface before an incident).

## Addresses

- [[weaknesses/No standardized forensic framework or toolset exists for connected autonomous vehicles]]

## How To Apply

Document explicitly, for each piece of CAV evidence handled, which adjacent-field methodology and standard was applied (e.g. ISO/IEC 27037 for chain-of-custody, CPS-forensics practice for sensor/actuator correlation) in the absence of a CAV-specific equivalent, so the reasoning behind evidentiary handling choices is traceable and defensible in legal proceedings until CAV-specific standards mature. Provide first responders and investigating technicians with dedicated training and equipment for CAV data curation from damaged hardware, and prioritize data types by likely evidentiary value and volatility given time and equipment constraints at the scene.

## References

- [LWCite-2020] Sharma and Gillanders, 2022 — Section VI.B "Existing Solutions to Forensic" identifies digital forensics, CPS forensics, software reliability analysis, and penetration testing as the four existing branches that could play a key role in CAV forensics pending dedicated standards.
