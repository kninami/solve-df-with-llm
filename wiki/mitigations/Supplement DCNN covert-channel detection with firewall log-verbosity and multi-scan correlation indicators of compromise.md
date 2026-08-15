---
id: DFM-1265
type: mitigation
name: Supplement DCNN covert-channel detection with firewall log-verbosity and multi-scan correlation indicators of compromise
source_refs:
  - DFCite-1286
updated_at: 2026-08-14
status: complete
---

# Supplement DCNN covert-channel detection with firewall log-verbosity and multi-scan correlation indicators of compromise

## Summary

Since a machine-learning classifier alone cannot reliably catch a low-bandwidth port-scan covert channel, pair it with independent indicators of compromise — repeated port scans against the same firewall from a single source IP, unusual firewall log-retrieval access patterns, and reduced firewall logging verbosity — and consider deliberately reducing default firewall log granularity as a structural countermeasure that suppresses the covert channel's usable carrier capacity, accepting the resulting loss of per-scan forensic detail as a trade-off.

## Addresses

- [[weaknesses/DCNN-based port-scan covert-channel detection accuracy approaches chance level for low-bandwidth embeddings]]

## How To Apply

Correlate flagged or suspicious port scans against a longer observation window for repeated scans from the same source IP address against the same firewall, since a single asynchronous covert channel typically requires transmitting its hidden message across multiple port scans over time. Monitor for anomalous access to firewall or central syslog log files by workstations, users, or service accounts that do not normally retrieve them, and for ARP-cache-poisoning indicators if a man-in-the-middle retrieval scenario is a plausible threat model. As a structural countermeasure, consider configuring the firewall to log only that a port scan occurred rather than logging each individual scanned port, or applying log normalization (e.g. consistent lower-case encoding) to reduce the entropy and redundancy available for a port-scan-based or general syslog-based covert channel to exploit — while documenting that this reduces log detail that might otherwise be needed for other investigative purposes.

## References

- [DFCite-1286] Lamshöft, Neubert, Hielscher, Vielhauer and Dittmann, 2022, "Knock, knock, log: Threat analysis, detection & mitigation of covert channels in syslog using port scans as cover", DFRWS 2022 EU; FSI: Digital Investigation 40, 301335.
