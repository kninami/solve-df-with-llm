---
id: LWW-2051
type: weakness
name: Open-source DPI classification limitations cause missed and misclassified IM calls in VoIP network forensics
description: Using an open-source deep packet inspection tool to classify encrypted IM/VoIP traffic causes some calls to go undetected (dropped packets not correctly classified) and limits how many distinct IM applications' traffic signatures are recognized, since traffic classification accuracy depends entirely on the DPI tool's own signature implementation and how current it is with application/protocol updates.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-2051
source_refs:
  - LWCite-2052
updated_at: 2026-08-14
status: partial
---

# Open-source DPI classification limitations cause missed and misclassified IM calls in VoIP network forensics

## Summary

The source paper's own results directly attribute a shortfall to its DPI tool: "The failed 2 calls may be dropped packets not reaching the DPI or dropped in the DPI interface itself, as a non-commercial tool was used... it is believed that the results could be further improved by incorporating commercial DPI." It separately notes that "there were only five IM applications in the dataset owing to the misclassification from nDPI. It is an open-source DPI and depends on its classification of IP related to the service," even though the test network actually ran six IM applications (WhatsApp, Signal, Facebook Messenger, Snapchat, Telegram, FaceTime). The paper's own "Limitations" section adds that DPI performance for identifying traffic types "was limited by its implementation and how dynamic and adaptable it was for new updates and protocols."

## Why It Matters

An investigator relying on this technique with an open-source DPI tool should expect some genuine IM calls to be missed or an IM application's traffic to go unrecognized entirely, purely as an artifact of the DPI signature library's coverage and currency rather than any flaw in the underlying STUN-correlation methodology. Since IM applications update frequently and can change their signaling behavior, a DPI signature set that is not actively maintained will progressively miss more calls and applications over time.

## Related Mitigations

- [[mitigations/Use a commercial DPI tool and maintain current signatures when performing VoIP network forensics]]

## Used By

- [[techniques/Identify VoIP call participants from encrypted IM traffic using STUN correlation]]

## References

- [LWCite-2052] Sarhan et al., 2024 — Section IV.C's discussion of the two failed call identifications and the five-vs-six application discrepancy directly attributes both to nDPI classification limitations, and the paper's own "Limitations" and "Future Work" sections reinforce this.
