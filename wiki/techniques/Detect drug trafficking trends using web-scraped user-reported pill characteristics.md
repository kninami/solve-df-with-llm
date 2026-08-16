---
id: DFT-2121
type: technique
name: Detect drug trafficking trends using web-scraped user-reported pill characteristics
description: Automatically scrape a clear-web drug-checking/user-report forum to build a structured dataset of illicit drug pill characteristics (logo, colour, shape, suspected contents), listing location, and listing date, then analyze it for temporal usage trends and geographic trafficking flow patterns.
objective_ids:
  - DFO-1004
  - DFO-1012
weakness_ids:
  - DFW-2130
aliases:
  - OSINT ecstasy pill report analysis
source_refs:
  - DFCite-2150
updated_at: 2026-08-16
status: complete
---

# Detect drug trafficking trends using web-scraped user-reported pill characteristics

## Summary

Open, free-form user-report websites where drug users voluntarily post information about a pill's physical characteristics, suspected contents, and their location are a freely accessible open-source intelligence (OSINT) source for drug market analysis. Automated web scraping of such a site converts thousands of loosely structured, free-text listings into a structured dataset that can be analyzed for general summary characteristics (most common logos, colours, shapes) and, using each report's location and listing date, for geographic movement trends such as which region a pill type is first reported in and how long it takes to appear in other regions.

## Details

An AI-assisted visual web-scraping tool detects and extracts the critical fields from each listing (pill name, location, listing date, username, suspected contents, rating, reagent-testing status, shape, logo, colour, safety warning, listing URL, thumbnail URL) into a spreadsheet-compatible dataset. Because the source data is free-form and uses inconsistent terminology (synonyms, abbreviations, spelling errors) for the same underlying value, a manual data-cleaning pass recodes free-text variants of each categorical variable (location, logo, shape, colour) to a single canonical value before analysis. Geographic trafficking-flow analysis groups reports by a persistent logo/colour/shape combination (treated as evidence of a single production batch) and orders each combination's listing dates by region to infer a directional flow, and lag-time analysis (e.g. days between a batch's first report on one coast and its first report on the other) can suggest how long batches take to traffic between distant regions.

## Examples

- Scraping www.pillreports.net (ScrapeStorm) produced 4,358 categorized ecstasy pill reports across Australia and New Zealand spanning 2005-2020, whose regional distribution concurred with the Australian Criminal Intelligence Commission's wastewater-analysis-derived MDMA consumption rankings, and whose east-to-west lag analysis (mean 363 days) suggested an east-coast entry point with roughly one-year onshore distribution to Western Australia.

## Related Objectives

- `DFO-1004` Conduct research
- `DFO-1012` Locate potentially relevant content

## Related Weaknesses

- [[weaknesses/Voluntary self-reported drug data samples only a harm-reduction-conscious subset of the user population]]

## References

- [DFCite-2150] Maybir and Chapman, 2021, "Web scraping of ecstasy user reports as a novel tool for detecting drug market trends", FSI: Digital Investigation 37.
