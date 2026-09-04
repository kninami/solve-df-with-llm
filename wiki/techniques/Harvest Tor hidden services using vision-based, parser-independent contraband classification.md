---
id: LWT-1136
type: technique
name: Harvest Tor hidden services using vision-based, parser-independent contraband classification
description: Crawl and periodically re-crawl a corpus of Tor hidden-service (.onion) URLs, capturing rendered-page screenshots alongside raw HTML/media/OSINT metadata, and classify captured screenshots for contraband categories (e.g. drugs, weapons) using an image-level object detector, so that harvesting and evidence flagging survive HTML/template changes that would break a DOM- or keyword-based crawler.
objective_ids:
  - DFO-1012
weakness_ids:
  - LWW-1139
aliases:
  - DarkCatalog
  - Vision-first, parser-independent forensic harvesting of Tor hidden services
source_refs:
  - LWCite-1137
updated_at: 2026-08-12
status: complete
---

# Harvest Tor hidden services using vision-based, parser-independent contraband classification

## Summary

Prior darknet harvesting systems (e.g. ATOL, D-miner, Smart Crawler) rely on keyword matching, static JSON transformation, or DOM/HTML parsing, all of which degrade or break when a site is obfuscated, redesigned, or migrated. This technique instead treats each captured page primarily as an image: a YOLO-family object detector is run over rendered-page screenshots to flag drug and weapon imagery directly, independent of the underlying HTML structure, while text, metadata, and OSINT identifiers (wallet addresses, PGP keys) are retained as corroborating, non-primary evidence.

## Details

The pipeline verifies each candidate .onion URL's reachability, then for each active service performs parallelized, deduplicated crawling that captures HTML pages, rendered screenshots, and downloaded media, storing all captured artifacts with cryptographic hashes and capture metadata (capture ID, extraction modality, model/version, confidence, localization) for court-admissible provenance and reproducibility. Object detection (YOLOv4, selected after a statistically validated paired comparison against YOLOv5s and Faster R-CNN) classifies screenshots into Drugs/Weapons/background categories using confidence-gated decision policies: high-confidence detections are surfaced automatically, low-confidence or ambiguous detections are routed to human analyst review rather than being auto-labeled, and purely benign or off-topic imagery contributes only background evidence. Evaluated across 5000 candidate .onion URLs (43% found inactive, underscoring the value of upfront URL verification before allocating crawl effort), the detector achieved mean mAP@0.5 of 93.4% and F1-score of 91.5% for the two contraband classes, at an average processing time of roughly 68 seconds per 1000 URLs — a 3.1x speedup over the ATOL baseline. Case studies applied the framework to reconstruct the timeline and evidence footprint of two real-world darknet disruptions (the AlphaBay marketplace takedown and a LockBit ransomware leak-site disruption), evaluating coverage/stability, temporal drift, and cross-page correlation as retrospective forensic-utility measures. This is distinct in both purpose and mechanism from [[techniques/Archive darknet marketplace content using periodic web scraping]], which periodically scrapes DOM-structured marketplace listing/vendor/forum content for longitudinal retention rather than performing image-based contraband classification across the broader Tor hidden-service ecosystem.

## Examples

- Confusion-matrix evaluation on a held-out 500-image-per-class test set showed only 43 drug images misclassified as weapons and 42 weapon images misclassified as drugs, reflecting that darknet vendors tend to maintain visually distinctive branding of illicit products that supports reliable image-based classification even under some obfuscation.

## Related Objectives

- `DFO-1012` Locate potentially relevant content

## Related Weaknesses

- [[weaknesses/Vision-based darknet contraband detectors degrade against deliberately obfuscated product imagery]]

## References

- [LWCite-1137] Rathod et al., 2026, "DarkCatalog: A vision-first, parser-independent framework for forensic harvesting of TOR hidden services", FSI: Digital Investigation 57.
