---
id: DFM-1163
type: mitigation
name: Escalate to logical or physical extraction when live dashboard or plaintext access to automotive app data is blocked
source_refs:
  - DFCite-1166
updated_at: 2026-08-12
status: complete
---

# Escalate to logical or physical extraction when live dashboard or plaintext access to automotive app data is blocked

## Summary

Do not treat a blank or connection-dependent dashboard as evidence that no telemetry exists — always attempt logical extraction of the app's local files, and treat encrypted local files as a signal to escalate to lab-based decryption or reverse engineering rather than as a dead end.

## Addresses

- [[weaknesses/Encrypted or connection-dependent automotive app storage blocks lower-intrusion telemetry extraction]]

## How To Apply

Follow the triage decision sequence: if the dongle is disconnected and the dashboard is inaccessible, bag the phone and escalate to lab-based logical extraction rather than concluding the device is a dead end at the scene. In the lab, if an app's local files are found to be encrypted, document this and consider reverse-engineering the app's encryption scheme (as is possible with sufficient time and expertise) or pursuing the vendor's cloud-side data via a legal warrant, rather than reporting a low artifact count as evidence the app collected little data.

## References

- [DFCite-1166] Sumaila and Bahsi, 2022, "Digital forensic analysis of mobile automotive maintenance applications", FSI: Digital Investigation 43, 301440.
