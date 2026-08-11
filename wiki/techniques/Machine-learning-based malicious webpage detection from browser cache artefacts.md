---
id: DFT-1065
type: technique
name: Machine-learning-based malicious webpage detection from browser cache artefacts
description: Automatically flag malicious web pages (exploit kits, cryptomining scripts, and other browser-borne threats) encountered by a browser under investigation by applying a machine-learning classifier — such as a random forest trained on a labeled corpus of benign and malicious page features — to pages reconstructed from browser cache/history artefacts, then present detections through a malicious-probability score and a timeline visualization to focus the investigator's manual review.
objective_ids:
  - DFO-1019
weakness_ids:
  - DFW-1070
aliases:
  - AIBFT
  - Artificial Intelligence Browser Forensic Toolkit
source_refs:
  - DFCite-1060
updated_at: 2026-08-10
status: complete
---

# Machine-learning-based malicious webpage detection from browser cache artefacts

## Summary

Manually reviewing the thousands of web pages a browser under investigation may have visited is impractical, and signature-based antivirus detection focused on known patterns misses novel malicious pages. Training a machine-learning model (random forest, in the evaluated implementation) on a large labeled corpus of benign and malicious page features and applying it to pages recovered from the browser's own cache/history data lets an investigator triage at scale, prioritizing pages by a malicious-probability score and a visual timeline rather than reviewing every page individually.

## Details

The toolkit (AIBFT) combines a malicious detection model and a separate malicious-probability measurement model to reduce false positives and false negatives, trained on 52,500 collected benign and malicious web pages and achieving 99.8% accuracy with the random forest algorithm among the AI algorithms tested. Detected pages are presented through a timeline analyzer and visualization function that the authors report drastically reduces manual analysis time compared to existing browser-investigation tools, several of which lack any AI-based detection, prediction, or visualization capability.

## Examples

- Comparative testing against four commercial antivirus products found that AIBFT detected a cryptomining web page that none of the four antivirus products flagged, illustrating its value for novel threats not yet covered by signature-based detection.

## Related Objectives

- `DFO-1019` Detect anti-forensics and other anomalies

## Related Weaknesses

- [[weaknesses/Private browsing mode leaves no browser cache for machine-learning-based malicious webpage detection to analyze]]

## References

- [DFCite-1060] Kim et al., 2021, "AIBFT: Artificial Intelligence Browser Forensic Toolkit", FSI: Digital Investigation 36.
