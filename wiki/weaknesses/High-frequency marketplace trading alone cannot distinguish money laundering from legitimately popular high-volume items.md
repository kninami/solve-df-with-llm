---
id: LWW-1283
type: weakness
name: High-frequency marketplace trading alone cannot distinguish money laundering from legitimately popular high-volume items
description: A single frequency-based signal — an item, seller, or buyer appearing unusually often in marketplace trade data — cannot by itself distinguish laundering-related activity from an item that is simply genuinely popular or more commonly obtainable, since both produce the same statistical outlier pattern in trade-frequency data.
categories:
  - ASTM_MISINT
mitigation_ids:
  - LWM-1284
source_refs:
  - LWCite-1311
updated_at: 2026-08-15
status: complete
---

# High-frequency marketplace trading alone cannot distinguish money laundering from legitimately popular high-volume items

## Summary

In a real Steam Marketplace dataset, the single most-traded item accounted for 14.1% of all observed trades, and the top 10 items together accounted for 74.9% — a result the researchers explicitly note does not by itself justify suspicion, since the item's own popularity or ease of acquisition equally explains high trade frequency, and item function/desirability could not be independently confirmed from the trade data alone.

## Why It Matters

An investigator who treats any single frequency outlier (most-traded item, most-active seller or buyer) as evidence of money laundering risks a high false-positive rate against ordinary high-volume legitimate trading activity, wasting investigative resources and potentially casting unwarranted suspicion on legitimate market participants. Because the underlying trade data provides no direct signal of intent, frequency-based indicators are only a prioritization tool, not confirmation.

## Related Mitigations

- [[mitigations/Cross-reference multiple independent frequency indicators and item-specific context before treating a marketplace trade pattern as suspicious]]

## Used By

- [[techniques/Detect potential money laundering using frequency-based marketplace transaction indicators]]

## References

- [LWCite-1311] Cooke and Marshall, 2024, "Money laundering through video games, a criminals' playground", FSI: Digital Investigation 50, 301802.
