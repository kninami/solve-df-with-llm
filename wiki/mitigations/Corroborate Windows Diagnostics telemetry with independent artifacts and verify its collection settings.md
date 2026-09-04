---
id: LWM-1160
type: mitigation
name: Corroborate Windows Diagnostics telemetry with independent artifacts and verify its collection settings
source_refs:
  - LWCite-1163
updated_at: 2026-08-12
status: complete
---

# Corroborate Windows Diagnostics telemetry with independent artifacts and verify its collection settings

## Summary

Check the system's diagnostic data collection level (registry `AllowTelemetry`/`MaxTelemetryAllowed` policy value, or Settings > Diagnostics & Feedback history where available) before relying on EventTranscript.db, and cross-reference recovered events against independent artifacts — shellbags and LNK files for USB activity, and the relevant browser's own history/cache for browsing activity when a non-default browser is in use.

## Addresses

- [[weaknesses/Windows Diagnostics omits activity recorded outside optional data collection or the default browser]]

## How To Apply

Record the device's diagnostic data collection level as part of the examination notes so the completeness of any EventTranscript.db-derived timeline can be correctly caveated. If the target device is known or suspected to use a third-party browser, extract that browser's own history, cache, and session artifacts in parallel rather than relying on Windows Diagnostics for browsing activity. Where corporate or managed environments centrally enforce the optional collection setting via policy (e.g. Patch Management System), confirm the enforced setting rather than assuming the Windows default.

## References

- [LWCite-1163] Park and Lee, 2022, "DiagAnalyzer: User behavior analysis and visualization using Windows Diagnostics logs", FSI: Digital Investigation 43, 301450.
