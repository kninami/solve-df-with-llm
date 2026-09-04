---
id: LWM-2053
type: mitigation
name: Adopt authenticated OTA firmware updates and continuous kernel patching for drone fleets before an incident occurs
source_refs:
  - LWCite-2054
updated_at: 2026-08-14
status: partial
---

# Adopt authenticated OTA firmware updates and continuous kernel patching for drone fleets before an incident occurs

## Summary

As a forensic-readiness and security-hardening measure, DaaS operators should adopt an authenticated over-the-air (OTA) firmware update mechanism (e.g. a certificate-secured, zero-downtime handover update strategy) in place of unauthenticated public vendor-website downloads, and require the embedded OS/kernel to be kept current with security patches independently of the higher-level firmware release cadence.

## Addresses

- [[weaknesses/Drone firmware bundles severely outdated OS kernels with many unpatched known vulnerabilities despite being labeled the latest release]]

## How To Apply

Where feasible, prioritize drone platforms and vendors that support TLS-certificate-secured OTA firmware distribution over plain public-website downloads, and periodically extract and fingerprint the actual embedded OS/kernel version (via the same static-analysis approach used to detect this weakness) to verify it is not silently lagging behind the firmware's stated release version. Track the fingerprinted kernel version against a vulnerability database on an ongoing basis, and treat a drone platform found running significantly outdated, high-vulnerability-count kernel software as a documented risk factor when investigating an incident involving that device.

## References

- [LWCite-2054] Salamh et al., 2021 — Section 2.3's discussion of firmware update strategies (handover updates, TLS-secured remote updates) describes the authenticated OTA approach this mitigation recommends adopting in place of public vendor-website distribution.
