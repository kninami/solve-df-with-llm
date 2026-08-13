---
id: DFW-1116
type: weakness
name: CGN and NAT reverse-tracking misattributes subscribers when overlapping port-assignment errors are undetected in deterministic NAT logs
description: A deterministic CGN's algorithmic internal-to-external IP/port mapping can silently assign overlapping port ranges to multiple concurrent subscribers ("port-jumping"), and separately, session logs can contain internally inconsistent, overlapping, or technically impossible entries (missing public IP/port fields, colliding session times, or upload/download volumes inconsistent with the session type), any of which can cause a reverse-tracked subscriber attribution to be wrong without the error being visible in the log output itself.
categories:
  - ASTM_INAC_AS
mitigation_ids:
  - DFM-1116
source_refs:
  - DFCite-1109
updated_at: 2026-08-12
status: complete
---

# CGN and NAT reverse-tracking misattributes subscribers when overlapping port-assignment errors are undetected in deterministic NAT logs

## Summary

The paper documents this as a previously undiscussed, real-world failure mode found in actual CGN logs used as evidence in Turkish criminal trials: analyzing a specific deterministic-NAT ISP's (Vodafone Turkey's) CGN configuration, the author calculates that with 1,655,000 reserved public IPv4 addresses shared among 20 million customers (12 subscribers per address on average) and a 42,021-port range assigned to the logged session, "port-jumping errors may exist... The port-jumping error has never been discovered or mentioned in the literature before." Separately, thorough analysis of the underlying GPRS/WAP session logs (Historical Traffic Search records) found large numbers of session records overlapping in time for the same subscriber (46,782 sessions overlapping with at least six others in one dataset), 47.28% of GPRS records missing the cellular network information field required to validate the session, and individual sessions with technically impossible data-volume/duration combinations.

## Why It Matters

An investigator or court relying on a CGN log's subscriber attribution as evidence risks accepting a misidentification: because a deterministic CGN's port range can be shared by multiple concurrent subscribers without the log format itself flagging the ambiguity, and because underlying session logs can contain colliding, missing-field, or physically implausible entries, the ISP-provided reverse-tracking result can point to the wrong subscriber while appearing, on its face, to be a valid, complete log entry — with documented cases of resulting extended pretrial detention, imprisonment, and other severe legal consequences for wrongly identified individuals.

## Related Mitigations

- [[mitigations/Cross-validate CGN log subscriber attributions against overlapping-session and data-volume consistency checks before use as sole evidence]]

## Used By

- [[techniques/Identify an internet subscriber from carrier-grade NAT logs using IP, port, and timestamp correlation]]

## References

- [DFCite-1109] Gözükara, 2021, "Challenges and possible severe legal consequences of application users identification from CNG-Logs", FSI: Digital Investigation 39.
