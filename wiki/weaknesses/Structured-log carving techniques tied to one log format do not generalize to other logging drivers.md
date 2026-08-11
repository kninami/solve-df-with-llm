---
id: DFW-1045
type: weakness
name: Structured-log carving techniques tied to one log format do not generalize to other logging drivers
description: A carving algorithm built around one structured log format's specific field markers and grammar (e.g., Docker's json-file logging driver format) cannot be applied to logs produced by a different logging driver or a different container/log platform without separate, format-specific redevelopment, since the identification and reassembly stages both depend directly on that format's particular structural conventions.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1045
source_refs:
  - DFCite-1035
updated_at: 2026-08-09
status: complete
---

# Structured-log carving techniques tied to one log format do not generalize to other logging drivers

## Summary

The authors state this directly as a limitation and direction for future work: "Our carver only works on json-file logs and further research on carving container logs in other formats or in a cloud environment could be taken." Docker alone supports 11 built-in logging drivers with distinct log formats, meaning containers configured to use any driver other than json-file (e.g., syslog, journald, or a cloud-native logging backend) would not be recoverable by this specific carving algorithm at all.

## Why It Matters

An investigator who encounters a compromised container host cannot assume a json-file-log carving tool will recover logs regardless of the container's actual logging configuration; if the target used a different logging driver, this technique provides no recovery capability whatsoever, not merely reduced accuracy. Confirming which logging driver was actually configured for the containers of interest is therefore a necessary prerequisite before selecting or attempting to apply this class of format-specific carving tool.

## Related Mitigations

- [[mitigations/Confirm the logging driver before applying a format-specific structured-log carving algorithm]]

## Used By

- [[techniques/Content-similarity-based reassembly of fragmented structured-text log files]]

## References

- [DFCite-1035] Ge et al., 2021, "A novel file carving algorithm for docker container logs recorded by json-file logging driver", FSI: Digital Investigation 39.
