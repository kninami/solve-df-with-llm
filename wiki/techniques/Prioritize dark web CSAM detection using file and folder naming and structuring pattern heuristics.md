---
id: LWT-2111
type: technique
name: Prioritize dark web CSAM detection using file and folder naming and structuring pattern heuristics
description: Improve the efficiency of automated child sexual abuse material (CSAM) detection on dark web sites by first analyzing file and folder naming conventions and directory structuring patterns known to be associated with CSAM distribution (e.g. specific keyword patterns, age-indicating abbreviations, or characteristic folder-organization schemes), and prioritizing image-content-analysis scanning toward files and folders matching these patterns rather than scanning an entire site's contents with equal priority.
objective_ids:
  - DFO-1007
  - DFO-1012
weakness_ids:
  - LWW-2118
aliases:
  - File/folder naming heuristics for CSAM detection prioritization
source_refs:
  - LWCite-2138
updated_at: 2026-08-16
status: complete
---

# Prioritize dark web CSAM detection using file and folder naming and structuring pattern heuristics

## Summary

Automated image-content-based CSAM detection (e.g. perceptual hashing against known-CSAM databases, or trained classifiers) is computationally expensive to run against a dark web site's entire file inventory, and dark web CSAM distributors frequently use identifiable naming and folder-structuring conventions when organizing their content. Analyzing file and folder names and directory structure first, and using matches against known naming/structuring patterns to prioritize which files receive computationally expensive image-content analysis, improves detection efficiency without requiring every file to be scanned at equal priority.

## Details

The technique catalogs naming and structuring conventions empirically observed across known CSAM-distributing dark web sites -- including specific keyword and abbreviation patterns associated with victim age indicators, series/collection naming conventions distributors use to organize related content, and characteristic folder hierarchy patterns (e.g. content grouped by purported age category or source). File and folder names encountered during a crawl or examination are checked against these known patterns, and matches are used to assign a priority score that determines the order in which files are queued for the more computationally expensive image-content-analysis stage, letting a fixed computational budget be allocated toward the files most likely to actually contain CSAM first, rather than processing files in an arbitrary or purely sequential order.

## Examples

- Applying the naming/structuring heuristics to a test corpus of dark web site directory listings improved the efficiency of subsequent image-content-based CSAM detection by prioritizing scanning toward files with pattern-matching names and folder placements, reducing the computational resources needed to identify a given proportion of true CSAM content relative to unprioritized scanning.

## Related Objectives

- `DFO-1007` Reduce data under consideration
- `DFO-1012` Locate potentially relevant content

## Related Weaknesses

- [[weaknesses/File and folder naming heuristics for CSAM detection cannot recognize deliberately disguised or novel naming conventions]]

## References

- [LWCite-2138] "Using file and folder naming and structuring to improve automated detection of child sexual abuse images on the Dark Web", FSI: Digital Investigation 48, 2024.
