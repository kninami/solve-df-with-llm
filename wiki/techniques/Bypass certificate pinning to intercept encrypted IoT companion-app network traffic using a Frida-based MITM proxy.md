---
id: LWT-1166
type: technique
name: Bypass certificate pinning to intercept encrypted IoT companion-app network traffic using a Frida-based MITM proxy
description: Route a rooted Android device's traffic through an HTTPS-intercepting MITM proxy with a trusted system-level CA certificate, then use a Frida-based instrumentation tool to patch the target companion app's certificate-pinning check at runtime, allowing an examiner to capture and decrypt the app's TLS-protected communication with an IoT device or its vendor cloud.
objective_ids:
  - DFO-1016
weakness_ids:
  - LWW-1172
aliases:
  - Certificate un-pinning for IoT companion app traffic capture
source_refs:
  - LWCite-1177
updated_at: 2026-08-12
status: complete
---

# Bypass certificate pinning to intercept encrypted IoT companion-app network traffic using a Frida-based MITM proxy

## Summary

Certificate pinning prevents a standard man-in-the-middle proxy from decrypting an app's TLS traffic even when its CA certificate is trusted at the OS level, because the app independently verifies the server certificate against a hardcoded expected value; repackaging the app with an injected Frida instrumentation gadget lets an examiner defeat this check at runtime and recover the plaintext of an otherwise TLS-protected companion-app-to-device or companion-app-to-cloud conversation.

## Details

A Raspberry Pi configured as a Wi-Fi access point routes device traffic through `mitmproxy`, which performs the MITM interception; the proxy's CA certificate must first be installed as a trusted system certificate on the Android test device (requiring root, e.g. via a Magisk module to make the read-only system certificate store writable). Because this alone is insufficient against apps that pin their expected certificate, the tool `objection` is used to patch and repackage the target APK, injecting a Frida gadget that dynamically alters the app's certificate-verification control flow at runtime so pinning checks pass regardless of the certificate actually presented. This combination successfully decrypted traffic for three of six tested companion apps; the remaining three failed the unpinning step and instead threw network-connection errors, indicating additional anti-tampering protections beyond simple certificate pinning.

## Examples

- Decrypted traffic for the eWeLink, meross, and Shelly Smart Control companion apps revealed device status, configuration, and switching-command payloads exchanged both locally and with the vendor cloud.
- Local (non-cloud) communication was found to be unencrypted for most tested relays, and only partially encrypted (command payload only) for three others, meaning MITM decryption was primarily needed for the cloud-connected portion of the traffic.

## Related Objectives

- `DFO-1016` Overcome protection mechanisms

## Related Weaknesses

- [[weaknesses/Replay-attack vulnerability in local smart-relay communication undermines reliable attribution of a captured switching action]]

## References

- [LWCite-1177] Eichhorn and Pugliese, 2024, "Do You \"Relay\" Want to Give Me Away? - Forensic Cues of Smart Relays and Their IoT Companion Apps", FSI: Digital Investigation 50, 301810.
