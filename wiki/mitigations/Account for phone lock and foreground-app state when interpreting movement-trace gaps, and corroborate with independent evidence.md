---
id: LWM-2092
type: mitigation
name: Account for phone lock and foreground-app state when interpreting movement-trace gaps, and corroborate with independent evidence
source_refs:
  - LWCite-2107
updated_at: 2026-08-16
status: complete
---

# Account for phone lock and foreground-app state when interpreting movement-trace gaps, and corroborate with independent evidence

## Summary

When interpreting WhatsApp logfile or `cache_encryptedC.db` motion-trace data for a period of interest, explicitly consider whether the phone was likely locked or the relevant app was backgrounded during that period before concluding an absence of trace data reflects an absence of movement, and corroborate movement inferences with an independent evidence source where the stakes warrant it.

## Addresses

- [[weaknesses/Phone-based movement-detection accuracy from app and OS traces varies sharply by phone-lock state and foreground-app status]]

## How To Apply

Before concluding a phone was stationary during a period with no recorded movement trace, check for independent evidence of the phone's lock state during that period (e.g. screen-on/off logs, other app usage timestamps) that might explain a trace gap unrelated to actual movement. Where a movement conclusion is significant to the case, corroborate the WhatsApp/`cache_encryptedC.db`-derived inference with an independent source such as the Health app's own step/distance data (see [[techniques/Evaluate iPhone Health app distance data using a likelihood ratio]]), cell-tower or Wi-Fi connection logs, or witness testimony, rather than relying on a single trace source alone. Stay current with published research on iOS's internal motion-tracking mechanisms, since some of the underlying trace-generation behavior is not yet fully documented and future findings may refine how gaps should be interpreted.

## References

- [LWCite-2107] van Zandwijk and Boztas, 2021, "The phone reveals your motion: digital traces of walking, driving and other movements on iPhones", FSI: Digital Investigation 37, 301170.
