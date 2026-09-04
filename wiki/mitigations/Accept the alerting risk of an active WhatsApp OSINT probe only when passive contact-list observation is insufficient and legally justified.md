---
id: LWM-1255
type: mitigation
name: Accept the alerting risk of an active WhatsApp OSINT probe only when passive contact-list observation is insufficient and legally justified
source_refs:
  - LWCite-1270
updated_at: 2026-08-14
status: complete
---

# Accept the alerting risk of an active WhatsApp OSINT probe only when passive contact-list observation is insufficient and legally justified

## Summary

When passive contact-list-based observation yields no profile information because of a target's privacy settings, only escalate to an active probe (such as sending a message, or another action likely to notify the target) if legally justified and necessary, since doing so trades the technique's normal near-zero detection risk for a real chance of alerting the target.

## Addresses

- [[weaknesses/WhatsApp privacy settings can hide profile photo, About text, and last-seen from non-contacts, limiting OSINT visibility]]

## How To Apply

Attempt passive contact-list observation first and document the result, including the absence of visible profile data, as inconclusive rather than as confirmation the target has no such data. Where more complete profile OSINT is genuinely required, weigh the investigative value against the risk that any active interaction (e.g. a message, a call, or a group addition) may notify the target that their number is under scrutiny, and pursue legal alternatives (e.g. a data-preservation or disclosure request to WhatsApp/Meta) instead where the risk of alerting the target is unacceptable.

## References

- [LWCite-1270] van der Meer and Le-Khac, 2026, "Identifying interception possibilities for WhatsApp communication", FSI: Digital Investigation 56, 302070.
