---
id: DFM-2128
type: mitigation
name: Document and minimize evidentiary alteration when injecting active payloads to identify a stalkerware abuser
source_refs:
  - DFCite-2148
updated_at: 2026-08-16
status: complete
---

# Document and minimize evidentiary alteration when injecting active payloads to identify a stalkerware abuser

## Summary

Before injecting an XSS or other active payload into a victim's device to exploit a stalkerware dashboard vulnerability, fully image and document the device's pre-injection state, use an easily distinguishable payload/contact name so it cannot be mistaken for genuine victim data, and remove the injected artifact once it has served its purpose and the required evidence has been captured.

## Addresses

- [[weaknesses/Injecting an XSS payload to identify a stalkerware abuser alters the victim device's content]]

## How To Apply

Capture a full forensic image of the device (or at minimum the relevant data store) before adding any payload-bearing contact or message, log the exact payload content, insertion time, and injection vector in the case notes, and use a payload/contact name pattern that is clearly artificial and would never be confused with real victim contacts. Once the payload has triggered against the stalkerware dashboard and the abuser-identifying data has been captured by the listener, delete the injected contact or message from the victim's device and note the removal in the documentation to restore the device as closely as possible to its original state.

## References

- [DFCite-2148] Mangeard et al., 2024, "WARNE: A stalkerware evidence collection tool", FSI: Digital Investigation 48.
