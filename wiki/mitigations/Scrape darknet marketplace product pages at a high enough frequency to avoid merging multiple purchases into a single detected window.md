---
id: LWM-1106
type: mitigation
name: Scrape darknet marketplace product pages at a high enough frequency to avoid merging multiple purchases into a single detected window
source_refs:
  - LWCite-1101
updated_at: 2026-08-12
status: complete
---

# Scrape darknet marketplace product pages at a high enough frequency to avoid merging multiple purchases into a single detected window

## Summary

When estimating purchase counts or timing from a product's sales-counter increments, use a scraping interval short enough relative to the product's expected sale rate that each interval is unlikely to contain more than one completed sale, and treat purchase-window estimates as imprecise when the underlying interval was necessarily longer.

## Addresses

- [[weaknesses/Sales-counter-based purchase detection merges multiple distinct purchases when the scraping interval is too long]]

## How To Apply

Where infrastructure allows, scrape high-volume or high-interest product pages at the shortest practical interval (the source paper used roughly 15 minutes) to minimize the chance of multiple purchases occurring within a single sampling window. Where a longer interval was unavoidable (e.g. due to rate-limiting or CAPTCHA-driven scraping constraints), explicitly caveat any purchase-count or purchase-window estimate as a lower bound and an imprecise window rather than an exact count.

## References

- [LWCite-1101] Dolejška et al., 2023, "Busting up Monopoly: Methods for modern darknet marketplace forensics", FSI: Digital Investigation 46.
