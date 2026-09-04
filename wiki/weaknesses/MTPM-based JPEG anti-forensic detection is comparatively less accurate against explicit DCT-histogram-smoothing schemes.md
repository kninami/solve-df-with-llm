---
id: LWW-2024
type: weakness
name: MTPM-based JPEG anti-forensic detection is comparatively less accurate against explicit DCT-histogram-smoothing schemes
description: The MTPM-based second-order detector's minimum decision error is consistently higher (meaning detection is less reliable) against anti-forensic schemes that use explicit DCT histogram smoothing (FD_Gur, FD_v, FD_Fan) than against other tested anti-forensic techniques, so an investigator's confidence in detecting anti-forensically hidden JPEG compression should vary by which specific anti-forensic scheme was used.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-2024
source_refs:
  - LWCite-2024
updated_at: 2026-08-14
status: partial
---

# MTPM-based JPEG anti-forensic detection is comparatively less accurate against explicit DCT-histogram-smoothing schemes

## Summary

The source paper's own minimum-decision-error results (Figures 5, 7, 8, 9) show that across every dataset and detector tested, including the proposed MTPM-based approach, "the minimum decision error is high for the anti-forensic techniques FD_Gur, FD_v, FD_Fan when compared to other techniques," attributing this to their use of "explicit histogram smoothing." The paper separately reports that FD_Fan "successfully fools the NA-DJPG detector...with minimum decision error value near to 0.5" (i.e. near chance level) for a comparison double-JPEG detector, underscoring that explicit-histogram-smoothing anti-forensic schemes are a genuinely harder detection case across the field, not just for one baseline method.

## Why It Matters

An investigator relying on MTPM-based (or similar second-order-statistic) JPEG anti-forensic detection should not treat a negative result (no detected compression/tampering) as equally confident regardless of which anti-forensic tool may have processed the image; detection reliability is measurably weaker specifically against tools using explicit DCT histogram smoothing, meaning genuinely anti-forensically processed evidence is more likely to go undetected when that particular smoothing approach was used.

## Related Mitigations

- [[mitigations/Apply a complementary JPEG anti-forensic detector when explicit DCT histogram smoothing is suspected]]

## Used By

- [[techniques/Detect JPEG compression despite anti-forensic processing using Markov transition probability matrices]]

## References

- [LWCite-2024] Kumar et al., 2021 — Section III.A and Figures 5, 7-9 report consistently higher minimum decision error against FD_Gur, FD_v, and FD_Fan across every tested detector, including the proposed MTPM approach.
