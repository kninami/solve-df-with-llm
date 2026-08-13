---
id: DFT-1190
type: technique
name: Intercept mobile app network traffic using a MITM proxy
description: Route a mobile app's network traffic through an investigator-controlled man-in-the-middle (MITM) proxy configured with a trusted CA certificate, decrypting and inspecting the app's HTTPS requests and responses when the app does not implement certificate pinning.
objective_ids:
  - DFO-1006
weakness_ids:
  - DFW-1197
aliases:
  - MITM traffic capture of a mobile app
  - Fiddler/Charles proxy-based mobile app traffic interception
source_refs:
  - DFCite-1208
updated_at: 2026-08-13
status: complete
---

# Intercept mobile app network traffic using a MITM proxy

## Summary

A test device's Wi-Fi is routed through a proxy tool (e.g. Fiddler, mitmproxy, Charles) whose root CA certificate is installed as trusted on the device, so the proxy can transparently decrypt, log, and re-encrypt the target app's HTTPS traffic; where the app does not independently verify the server certificate against a pinned value, this captures the full plaintext request/response content exchanged between the app and its backend without needing to reverse-engineer the app itself.

## Details

This is the baseline network-traffic-capture technique, distinct from active certificate-pinning-bypass approaches: it relies only on the OS trusting the proxy's CA certificate at the system level, and succeeds only against apps that accept any certificate trusted by the OS rather than checking for one specific, hardcoded certificate. It is commonly the first technique attempted before resorting to a more invasive bypass (see [[techniques/Bypass certificate pinning to intercept encrypted IoT companion-app network traffic using a Frida-based MITM proxy]]) when that fails. Because the technique's success depends entirely on the target app's TLS configuration, the same app can behave differently across platforms or versions, so an investigator should test both the Android and iOS builds of a target app separately rather than assuming a result on one platform generalizes to the other.

## Examples

- Life360 (Aagaard et al., 2023): traffic between the Life360 app and its backend was captured via a Fiddler MITM proxy. On iOS, the app did not implement certificate pinning, so the proxy fully decrypted the app's traffic, revealing location, circle-membership, and messaging data in transit. On Android, the app enforced certificate pinning at the tested version, so the same proxy setup produced only connection failures and no decrypted content, regardless of whether the test device was rooted.

## Related Objectives

- `DFO-1006` Acquire data

## Related Weaknesses

- [[weaknesses/Certificate pinning blocks MITM network-traffic interception when investigators do not attempt an active bypass]]

## References

- [DFCite-1208] Aagaard et al., 2023, "Family locating sharing app forensics: Life360 as a case study", FSI: Digital Investigation 44, 301478.
