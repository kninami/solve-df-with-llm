---
id: DFT-1111
type: technique
name: Identify an internet subscriber from carrier-grade NAT logs using IP, port, and timestamp correlation
description: Attribute an internet-connected activity observed by its destination public IP address, source port, and timestamp to a specific subscriber by reverse-tracking through an ISP's Carrier-Grade NAT (CGN) logs, which map that public IP/port/time combination back to the subscriber's private IP address and session, since many subscribers share a single public IPv4 address under CGN.
objective_ids:
  - DFO-1008
weakness_ids:
  - DFW-1116
aliases:
  - CGN log reverse-tracking
  - NAT444 subscriber identification
source_refs:
  - DFCite-1109
updated_at: 2026-08-12
status: complete
---

# Identify an internet subscriber from carrier-grade NAT logs using IP, port, and timestamp correlation

## Summary

Under Carrier-Grade NAT (CGN/NAT444), an ISP shares a single public IPv4 address among many subscribers by additionally multiplexing on source port ranges, so a public IP address alone (as typically logged by a content or destination server) no longer uniquely identifies a subscriber. Law enforcement instead requests the ISP's CGN logs, which record, per session, the mapping between a subscriber's internal IP/port and the external (public) IP/port assigned to that session at a given time, allowing the destination server's IP+port+timestamp record to be reverse-mapped to a specific subscriber.

## Details

Two CGN logging approaches exist: a standard (non-deterministic) CGN logs the internal-to-external IP/port mapping for every session as it occurs, requiring storage of a large session log; a deterministic CGN instead uses an algorithmic mapping function between internal and external IP/port ranges, letting the mapping be reconstructed from a smaller configuration log rather than a full session log, at the cost of requiring the correct algorithm parameters to be preserved and applied consistently. Because the requesting server or investigator typically only has the destination-side IP, port, and timestamp, correct subscriber attribution depends entirely on the ISP's CGN logs (or deterministic mapping configuration) being complete and internally consistent for the relevant time window. This technique has been used at scale in real criminal investigations, including Turkish prosecutions of alleged users of the ByLock mobile chat application based on CGN log records obtained from ISPs.

## Examples

- Turkish law enforcement requested CGN query results from an ISP (Vodafone Turkey) for a specific mobile phone number's public IP address and port usage over a date range, in order to attribute internet sessions associated with alleged ByLock application use to a specific criminal defendant.

## Related Objectives

- `DFO-1008` Establish identities

## Related Weaknesses

- [[weaknesses/CGN and NAT reverse-tracking misattributes subscribers when overlapping port-assignment errors are undetected in deterministic NAT logs]]


## References

- [DFCite-1109] Gözükara, 2021, "Challenges and possible severe legal consequences of application users identification from CNG-Logs", FSI: Digital Investigation 39.
