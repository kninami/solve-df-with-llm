---
id: DFT-1010
type: technique
name: Estimate file execution times from Shimcache
description: Apply an interval-estimation algorithm to the Windows Application Compatibility Cache (Shimcache) artifact to approximate file execution times for Advanced Persistent Threat (APT) detection, since Shimcache does not natively record execution timestamps.
objective_ids:
  - DFO-1017
weakness_ids:
  - DFW-1010
aliases:
  - Shimcache execution time estimation
  - XTEC Shimcache analysis
source_refs:
  - DFCite-1005
updated_at: 2026-08-09
status: complete
---

# Estimate file execution times from Shimcache

## Summary

The Windows Shimcache records that a file existed and was referenced by the OS but, unlike Prefetch, does not natively store when it was executed. The XTEC approach estimates an execution-time interval for each Shimcache entry and feeds sequences of estimated-time events into an anomaly-scoring ML model to flag behaviors consistent with Advanced Persistent Threats.

## Details

XTEC combines a preprocessing module (parsing Prefetch, Shimcache, and Windows Event Log artifacts) with an interval-estimation algorithm that assigns an approximate execution-time window to Shimcache entries, and a Random Forest-based anomaly-scoring model that flags suspicious event sequences (e.g., unusual `net`/`ping`/`runas` activity) with a numeric anomaly score. Because Shimcache lacks ground-truth execution timestamps, the estimation step is a structural workaround rather than a direct reading of stored data, so its accuracy has not been broadly validated outside the case study's environment.

## Examples

- Flagging an interval `2019/05/02 17:25:02-18:01:05` containing `runas` and process ID 4824 with an anomaly score of 0.8, versus a routine `net`/`ping` interval scored 0.2.

## Related Objectives

- `DFO-1017` Extract artifacts stored by the operating system

## Related Weaknesses

- [[weaknesses/Shimcache lacks native file execution timestamps requiring unvalidated estimation]]

## References

- [DFCite-1005] Dunsin et al., 2024, "A comprehensive analysis of the role of artificial intelligence and machine learning in modern digital forensics and incident response", FSI: Digital Investigation 48.
