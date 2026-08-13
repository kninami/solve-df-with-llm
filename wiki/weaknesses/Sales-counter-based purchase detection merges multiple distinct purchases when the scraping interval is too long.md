---
id: DFW-1106
type: weakness
name: Sales-counter-based purchase detection merges multiple distinct purchases when the scraping interval is too long
description: Detecting a darknet marketplace purchase by observing an increment in a product's public sales counter between two scrapes cannot distinguish a single purchase from several purchases that occurred within the same scraping interval, so a longer interval systematically under-counts and imprecisely windows purchase events.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1106
source_refs:
  - DFCite-1101
updated_at: 2026-08-12
status: complete
---

# Sales-counter-based purchase detection merges multiple distinct purchases when the scraping interval is too long

## Summary

The paper states this limitation directly for its procurement-tracking method: relying on the actual scraping period length, "too long a period results in an imprecise purchase window definition and possibly window merging — a situation when multiple purchases occur/are detected in a single given period." The sales-counter value only reveals that the counter changed, not how many individual increments occurred or when within the interval each one happened.

## Why It Matters

An investigator using sales-counter deltas to estimate the number and timing of a vendor's completed transactions (for example, to support an earnings or activity estimate) risks systematically under-counting purchases and reporting an imprecise time window whenever the actual purchase rate exceeds the scraping frequency, without any indication in the data itself that a merge has occurred.

## Related Mitigations

- [[mitigations/Scrape darknet marketplace product pages at a high enough frequency to avoid merging multiple purchases into a single detected window]]

## Used By

- [[techniques/Archive darknet marketplace content using periodic web scraping]]

## References

- [DFCite-1101] Dolejška et al., 2023, "Busting up Monopoly: Methods for modern darknet marketplace forensics", FSI: Digital Investigation 46.
