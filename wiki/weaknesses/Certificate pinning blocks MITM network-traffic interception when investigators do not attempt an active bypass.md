---
id: LWW-1197
type: weakness
name: Certificate pinning blocks MITM network-traffic interception when investigators do not attempt an active bypass
description: An app that implements certificate pinning rejects a man-in-the-middle proxy's substituted certificate even though it is trusted at the OS level, so a plain MITM traffic-capture attempt yields no decrypted content at all against that app unless the investigator separately attempts an active pinning-bypass technique.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-1197
source_refs:
  - LWCite-1208
updated_at: 2026-08-13
status: complete
---

# Certificate pinning blocks MITM network-traffic interception when investigators do not attempt an active bypass

## Summary

Whether a plain MITM proxy captures usable network evidence from a given app depends entirely on that app's TLS implementation, not on investigator skill or on whether the test device is rooted: in the Life360 case study, the Android build enforced certificate pinning and produced only connection failures under MITM interception, while the iOS build (no pinning at the tested version) yielded fully decrypted traffic under an identical proxy setup.

## Why It Matters

An investigator who concludes that an app "does not transmit meaningful data over the network" based on a failed plain-MITM attempt against one platform's build may simply have encountered that platform's certificate pinning, while the same app on a different platform (or a future/past version without pinning) could yield substantial network evidence. Since pinning is applied inconsistently even within the same app across its own platform builds, a failed capture attempt should be treated as inconclusive about the app's actual network behavior, not as evidence the traffic contains nothing forensically relevant.

## Related Mitigations

- [[mitigations/Attempt certificate-pinning bypass when plain MITM interception fails to decrypt app traffic]]

## Used By

- [[techniques/Intercept mobile app network traffic using a MITM proxy]]

## References

- [LWCite-1208] Aagaard et al., 2023, "Family locating sharing app forensics: Life360 as a case study", FSI: Digital Investigation 44, 301478.
