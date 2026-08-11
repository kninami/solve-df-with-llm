---
id: DFM-1045
type: mitigation
name: Confirm the logging driver before applying a format-specific structured-log carving algorithm
source_refs:
  - DFCite-1035
updated_at: 2026-08-09
status: complete
---

# Confirm the logging driver before applying a format-specific structured-log carving algorithm

## Summary

Before attempting to carve deleted container or application logs, determine which logging driver or log format was actually configured for the target system, and only apply a carving algorithm built for that specific format; do not assume a json-file-format carver (or any other format-specific tool) will work regardless of the actual logging configuration.

## Addresses

- [[weaknesses/Structured-log carving techniques tied to one log format do not generalize to other logging drivers]]

## How To Apply

Where possible, check the container platform's configuration (e.g., Docker daemon or per-container logging driver settings) to identify which of the available logging drivers was in use before selecting a carving tool. If the configuration cannot be determined directly, examine any surviving log fragments for format-identifying structural markers (e.g., JSON key names and braces for json-file, versus syslog's line-oriented format) to infer the format before committing carving effort. If no carving tool exists for the identified format, treat this as a gap requiring separate, format-specific tool development rather than assuming an available json-file carver is broadly applicable.

## References

- [DFCite-1035] Ge et al., 2021, "A novel file carving algorithm for docker container logs recorded by json-file logging driver", FSI: Digital Investigation 39.
