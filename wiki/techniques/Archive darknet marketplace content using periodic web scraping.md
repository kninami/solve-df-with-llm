---
id: LWT-1100
type: technique
name: Archive darknet marketplace content using periodic web scraping
description: Automatically and periodically scrape a darknet marketplace's product listings, vendor/operator profiles, forum posts, and activity feeds at fine-grained intervals (e.g. every ~15 minutes) to build a longitudinal archive that survives the marketplace's eventual shutdown and supports later investigative analysis.
objective_ids:
  - DFO-1006
weakness_ids:
  - LWW-1106
aliases:
  - Darknet marketplace product data retention
  - Darknet marketplace operator data retention
  - Darknet marketplace user activity metadata collection
  - Periodic web scraping of darknet marketplaces
source_refs:
  - LWCite-1101
updated_at: 2026-08-12
status: complete
---

# Archive darknet marketplace content using periodic web scraping

## Summary

Darknet marketplaces (DNMs) disappear without warning — through law enforcement seizure, exit scam, hack, or voluntary closure — taking all publicly accessible product listings, vendor profiles, and forum content with them. Automated, high-frequency web scraping captures this content while it is still available, producing a data set that supports post-mortem investigation long after the marketplace itself is gone.

## Details

The method targets several distinct but complementary data categories, each collected via the same periodic-scraping infrastructure: (1) **product data** — listing titles, photos, descriptions, prices, buyer reviews, and vendor profile metadata, which is both the highest-volume and easiest-to-gather evidence and can serve as direct or corroborative evidence in a search (e.g. matching a product photo's background furniture to a suspect's home); (2) **operator data** — server metadata, maintenance/outage windows, and hand-authored forum content (announcements, canaries, PGP-signed messages) from admins and moderators, useful for building an operator activity timeline for cross-correlation with OSINT or surveillance logs; and (3) **user activity metadata** — inferred from content changes between successive scrapes (new listings, incrementing sale/review counters, updated last-seen timestamps), which can establish a vendor's or buyer's active time windows, approximate time zone, and correlation with other observed activity, without needing the scraped content itself to be meaningful. The reliability of all three depends on scraping frequently enough relative to the events being measured — a single data point in a month-long window is far less informative than many samples over a short one. The method was demonstrated at scale on Monopoly Market, monitored via periodic scraping for nearly a year before its December 2021 shutdown (later revealed as part of the international "SpecTor" seizure operation), and a subsequent applicability survey found comparable product-listing, activity-feed, and review data present on most other currently active DNMs and fraud shops.

## Examples

- A product listing photo published on a marketplace matched a carpet pattern and scratch-marked table found during a subsequent home search, corroborating a suspect's involvement despite no drugs being found on scene.
- Nearly year-long periodic archiving of Monopoly Market (roughly every 15 minutes) produced active-vendor-count, product-count, and category-trend time series that remained available for analysis after the market's December 2021 shutdown.

## Related Objectives

- `DFO-1006` Acquire data

## Related Weaknesses

- [[weaknesses/Sales-counter-based purchase detection merges multiple distinct purchases when the scraping interval is too long]]

## References

- [LWCite-1101] Dolejška et al., 2023, "Busting up Monopoly: Methods for modern darknet marketplace forensics", FSI: Digital Investigation 46.
