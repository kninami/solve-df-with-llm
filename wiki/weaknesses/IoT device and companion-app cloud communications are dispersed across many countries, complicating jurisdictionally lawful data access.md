---
id: DFW-1261
type: weakness
name: IoT device and companion-app cloud communications are dispersed across many countries, complicating jurisdictionally lawful data access
description: An IoT device's cloud-stored data is not necessarily located in the country where the device physically operates, and a majority of tested devices sent data to multiple different countries rather than a single destination, so an investigator cannot assume a single jurisdiction's legal process will secure all of a device's cloud-held evidence.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1262
source_refs:
  - DFCite-1282
updated_at: 2026-08-14
status: complete
---

# IoT device and companion-app cloud communications are dispersed across many countries, complicating jurisdictionally lawful data access

## Summary

Analyzing network traffic destination metadata for 32 IoT devices tested from a UK/Australia-based testbed found 77% (24 of 32) sent data to more than one country, and all 32 tested devices ultimately terminated communication somewhere among 26 different destination countries — with the United States receiving traffic from all 32 devices despite the nearest cloud data center to the physical testbed being located elsewhere, showing that a vendor's advertised or geographically nearest data center does not reliably predict where a specific device's data is actually stored.

## Why It Matters

Legal access to cloud-stored evidence typically requires a request compliant with the laws of the jurisdiction where the data is held, and a documented case shows a major vendor (Microsoft) refusing to comply with a US search warrant specifically because the requested data was stored outside the US; an investigator who assumes a single jurisdiction's legal process will suffice, or who does not verify where a specific device's data actually resides before initiating that process, risks delay or an unsuccessful data request, and multi-destination cases can require coordinating legal process across several jurisdictions with differing requirements simultaneously.

## Related Mitigations

- [[mitigations/Extract IoT network traffic destination metadata early to identify every jurisdiction a legal data request will need to cover]]

## Used By

- [[techniques/Triage IoT device network communications for exploitable cleartext data using port scanning and entropy pre-testing]]

## References

- [DFCite-1282] Wu, Breitinger and Niemann, 2021, "IoT network traffic analysis: Opportunities and challenges for forensic investigators?", DFRWS 2021 APAC; FSI: Digital Investigation 38, 301123.
