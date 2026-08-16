---
id: DFW-2127
type: weakness
name: Injecting an XSS payload to identify a stalkerware abuser alters the victim device's content
description: Recovering an abuser's identity by exploiting a stalkerware dashboard's cross-site-scripting vulnerability requires writing an investigator-controlled payload into the victim's own contact list, text messages, or file names, which changes the original content of the seized device before analysis is complete.
categories:
  - ASTM_INAC_ALT
mitigation_ids:
  - DFM-2128
source_refs:
  - DFCite-2148
updated_at: 2026-08-16
status: complete
---

# Injecting an XSS payload to identify a stalkerware abuser alters the victim device's content

## Summary

To trigger a stored cross-site-scripting vulnerability in a stalkerware app's web dashboard, the investigator must plant a crafted payload somewhere the stalkerware will collect and upload it, for example by adding a new contact whose name is the payload, or by sending a text message that contains it. The payload has to be executed by the abuser browsing the dashboard, so it typically stays on the device until triggered rather than being immediately reverted, which means the victim device's contact list or message store no longer matches its pre-collection state.

## Why It Matters

Any active alteration of a device under investigation raises evidentiary integrity questions, particularly where the altered artifact (a contact entry, an SMS) is itself a data type that might otherwise be considered as part of the case. If the alteration is not clearly documented, a later reviewer could mistake the investigator-injected contact or message for genuine victim data, or a challenge to the evidence's authenticity could arise from the fact that device content changed during the collection process rather than only during acquisition.

## Related Mitigations

- [[mitigations/Document and minimize evidentiary alteration when injecting active payloads to identify a stalkerware abuser]]

## Used By

- [[techniques/Identify a stalkerware abuser by exploiting insecure local storage and web-dashboard vulnerabilities]]

## References

- [DFCite-2148] Mangeard et al., 2024, "WARNE: A stalkerware evidence collection tool", FSI: Digital Investigation 48.
