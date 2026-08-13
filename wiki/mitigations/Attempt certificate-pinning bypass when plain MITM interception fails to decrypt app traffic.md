---
id: DFM-1197
type: mitigation
name: Attempt certificate-pinning bypass when plain MITM interception fails to decrypt app traffic
source_refs:
  - DFCite-1208
updated_at: 2026-08-13
status: complete
---

# Attempt certificate-pinning bypass when plain MITM interception fails to decrypt app traffic

## Summary

When a plain man-in-the-middle proxy attempt against a target app produces only connection errors rather than decrypted content, do not conclude the app's network traffic is unrecoverable; instead, confirm whether certificate pinning is the cause and, if so, attempt an active pinning-bypass technique before ruling out network-traffic acquisition.

## Addresses

- [[weaknesses/Certificate pinning blocks MITM network-traffic interception when investigators do not attempt an active bypass]]

## How To Apply

Test the target app's specific platform build under a plain MITM proxy first, since pinning enforcement varies by platform and version. If interception fails, use a runtime instrumentation tool (e.g. Frida via `objection`) to patch the app's certificate-verification logic, as in [[techniques/Bypass certificate pinning to intercept encrypted IoT companion-app network traffic using a Frida-based MITM proxy]], and re-attempt interception. If the bypass itself fails (e.g. due to additional anti-tampering protections), fall back to on-device logical acquisition of the app's local storage as the primary evidence source rather than assuming no network evidence exists.

## References

- [DFCite-1208] Aagaard et al., 2023, "Family locating sharing app forensics: Life360 as a case study", FSI: Digital Investigation 44, 301478.
