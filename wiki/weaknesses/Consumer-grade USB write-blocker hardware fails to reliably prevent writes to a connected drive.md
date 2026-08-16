---
id: DFW-2071
type: weakness
name: Consumer-grade USB write-blocker hardware fails to reliably prevent writes to a connected drive
description: A budget consumer-grade USB write-block adapter can fail NIST CFTT hardware-write-block validation, allowing sectors on a connected drive to be modified during acquisition despite the device being marketed and configured as a "write protect" tool.
categories:
  - ASTM_INAC_ALT
mitigation_ids:
  - DFM-2071
source_refs:
  - DFCite-2075
updated_at: 2026-08-15
status: complete
---

# Consumer-grade USB write-blocker hardware fails to reliably prevent writes to a connected drive

## Summary

A CoolGear "Write Protect" consumer-grade USB SATA/IDE adapter (approximately $50), tested with its write-protect switch engaged, failed NIST's CFTT Federated Testing hardware-write-block suite and CRU's Writeblocker Validation Utility in every tested configuration: a SATA SSD connected under Linux, the same SATA SSD connected under Windows, and a SATA HDD connected under Windows all showed "Sectors on the drive were modified during the test," with the CFTT summary explicitly reporting a FAIL result. This occurred despite the device's own physical switches and its manufacturer-stated inability to disable write blocking without power-cycling the device — its actual write-blocking behavior did not match its designed/advertised behavior.

## Why It Matters

A write blocker that silently fails to block writes is the single most consequential possible failure in an acquisition workflow: any modification made to a suspect drive during imaging directly alters original evidence, potentially changing file-system metadata, timestamps, or data content in ways that could be challenged as spoliation or that undermine the integrity of hash values computed afterward. Because the device's physical indicators and switches gave no outward sign of the failure, an investigator relying on it without independent validation would have no way of knowing writes had occurred.

## Related Mitigations

- [[mitigations/Independently validate any write blocker against NIST CFTT test suites before relying on it for evidence acquisition]]

## Used By

- [[techniques/Validate a forensic tool's conformance using a CFTT-aligned specification]]

## References

- [DFCite-2075] Herrera, 2021, "Viability of Consumer Grade Hardware for Learning Computer Forensics Principles", JDFSL 16(3). Reports FAIL results ("Sectors on the drive were modified during the test") for the CoolGear write-block adapter across SATA SSD (Linux and Windows) and SATA HDD (Windows) test configurations under both the CFTT Federated Testing suite and CRU's Writeblocker Validation Utility.
