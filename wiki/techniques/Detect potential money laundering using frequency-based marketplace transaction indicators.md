---
id: DFT-1273
type: technique
name: Detect potential money laundering using frequency-based marketplace transaction indicators
description: Flag potentially suspicious money-laundering transactions on an unregulated peer-to-peer marketplace (such as a video-game item secondary marketplace) by measuring, over a fixed period, the most frequently traded items, the most frequent sellers, the most frequent buyers, and duplicated trades (identical buyer, seller, item, and value repeated), and cross-referencing accounts that appear as outliers on more than one of these measures.
objective_ids:
  - DFO-1005
weakness_ids:
  - DFW-1283
aliases:
  - Steam Marketplace money-laundering detection
source_refs:
  - DFCite-1311
updated_at: 2026-08-15
status: complete
---

# Detect potential money laundering using frequency-based marketplace transaction indicators

## Summary

Traditional automated money-laundering detection in banking identifies suspicious activity by irregularities in transaction frequency, volume, or complexity. The same frequency-based principle transfers to unregulated peer-to-peer secondary marketplaces — such as video-game item trading platforms — where the "layering" stage of money laundering (moving funds through many transactions to obscure their origin) can be approximated by scraping publicly accessible trade data and identifying accounts or items that are statistical outliers on simple frequency measures.

## Details

Using publicly accessible trade-history data (seller ID, buyer ID, trade value, timestamp, and item ID), four frequency parameters are computed over the observation period: the most frequently traded items, the most frequent sellers, the most frequent buyers, and duplicated trades (the identical item, at the identical value, between the identical buyer and seller, repeated). Each parameter's top-10 outliers are examined for three signals: whether they are clear visual outliers relative to the rest of the distribution, whether the observed frequency is feasible for a human to perform without automation, and — most importantly — whether the same account (buyer or seller ID) appears as an outlier across more than one of the four parameters, since cross-parameter recurrence is a stronger indicator than any single measure alone (a single high-frequency item alone may simply reflect genuine popularity rather than laundering).

## Examples

- Applied to five days of Steam Marketplace trade data for Counter-Strike: Global Offensive (1,108,199 total trades), the top 10 most-traded items accounted for 74.9% of all trades, with the single most-traded item alone accounting for 14.1% — findings the authors note are not independently sufficient to indicate laundering (since a genuinely popular item can also be traded at high frequency) but which identify accounts and items warranting further investigation, particularly where the same account recurs across the frequent-buyer, frequent-seller, and duplicated-trade measures.

## Related Objectives

- `DFO-1005` Prioritize digital evidence sources

## Related Weaknesses

- [[weaknesses/High-frequency marketplace trading alone cannot distinguish money laundering from legitimately popular high-volume items]]

## References

- [DFCite-1311] Cooke and Marshall, 2024, "Money laundering through video games, a criminals' playground", FSI: Digital Investigation 50, 301802.
