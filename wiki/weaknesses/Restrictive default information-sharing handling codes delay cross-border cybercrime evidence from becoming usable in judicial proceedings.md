---
id: LWW-1137
type: weakness
name: Restrictive default information-sharing handling codes delay cross-border cybercrime evidence from becoming usable in judicial proceedings
description: When partners default to the most restrictive handling code (e.g. H1, "not to be disclosed in judicial proceedings without the provider's permission") for shared data, investigators cannot use that data in the criminal case file without a formal request to the provider, which can take months or years and stalls an active cybercrime investigation.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-1137
source_refs:
  - LWCite-1135
updated_at: 2026-08-12
status: complete
---

# Restrictive default information-sharing handling codes delay cross-border cybercrime evidence from becoming usable in judicial proceedings

## Summary

Cross-border and cross-sector cybercrime investigations depend on data shared by other countries' law enforcement agencies, CSIRTs, and private incident responders, each applying their own information-classification scheme (TLP or EU H0-H3). Some contributing partners routinely mark shared data with a restrictive default code (e.g. H1) as a caution, even when a less restrictive code would be legally sufficient, and once shared, the receiving investigative team cannot unilaterally reclassify that data to permit its use in a formal case file or judicial proceeding.

## Why It Matters

Evidence that is investigatively critical but formally classified as intelligence-only sits unusable in the case for as long as it takes to obtain the provider's formal downgrade or disclosure permission — in the studied case, up to nearly two years for some material — even though the investigative team already possessed and understood the data's content. This effectively re-introduces an incompleteness gap after the data has technically been collected: the evidence exists in the investigative team's possession but cannot be relied on or disclosed, delaying prosecutorial progress and creating risk that time-sensitive leads go stale before they can be formally acted on.

## Related Mitigations

- [[mitigations/Pre-agree a directional TLP-to-H0-H3 translation framework with cross-sector and cross-border partners before a joint cybercrime investigation begins]]

## Used By

- [[techniques/Apply a directional, condition-based translation framework between TLP and law-enforcement handling codes in cross-sector cybercrime investigations]]

## References

- [LWCite-1135] Heitmann and Johnsen, 2026, "Cybercrime investigations in practice: Insights from the LockerGoga ransomware attack on Norsk Hydro", FSI: Digital Investigation 57.
