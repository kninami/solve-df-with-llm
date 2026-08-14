---
id: DFT-2002
type: technique
name: Select a forensic toolkit using a domain-specific feature-scoring model
description: The process of comparing candidate forensic toolkits within a specific domain (e.g. operating system, file system, live memory, web, email, network, or multimedia forensics) by scoring each on a checklist of domain-relevant features and ranking them by summed score.
objective_ids:
  - DFO-1015
weakness_ids:
  - DFW-2002
aliases:
  - Feature Scoring Model (FSM) toolkit ranking
source_refs:
  - DFCite-2002
updated_at: 2026-08-14
status: partial
---

# Select a forensic toolkit using a domain-specific feature-scoring model

## Summary

Before committing to a forensic toolkit for a specific domain of an investigation, an investigator enumerates the features relevant to that domain (e.g. malware analysis, live memory analysis, and JumpList analysis for live memory forensics; header, mailbox, and system-artifact analysis for email forensics), checks which candidate toolkits support each feature, and computes a normalized score to rank the toolkits from best to worst fit for that domain.

## Details

DFCite-2002 operationalizes this as a Feature Scoring Model (FSM): each domain-relevant feature supported by a toolkit earns 2 points, an unsupported feature earns 0, and the toolkit's total is normalized to a 0-100 percent score. The paper applies this across seven forensic domains (operating system, file system/disk, live memory, web, email, network, multimedia) against widely used toolkits (Autopsy, Redline, Belkasoft Evidence Center, OSForensics, ProDiscover Basic, X-Ways, EnCase, FTK, Magnet Axiom, Volatility, Rekall, F-Response, Network Miner, LogRhythm, PLIXER, NIKSUN, Nmap, XPLiCO, InstaForensics, Amped, Cognitech, FMDES, AMR, avdetective), finding, for example, that FTK scores highest for OS, file system, web, and email forensics; Belkasoft Evidence Center for live memory forensics; Network Miner for network forensics; and InstaForensics/Cognitech for multimedia forensics. This complements narrower single-purpose tool-fitness frameworks (e.g. the five-questions tool-fitness framework) by giving a repeatable, quantitative first-pass shortlist across an entire domain rather than validating a single already-chosen tool.

## Examples

- DFCite-2002's Table 16-22 FSM scores: FTK 100% for OS forensics and 83-100% for email; Belkasoft Evidence Center 85% for live memory; Network Miner and LogRhythm 77% for network forensics; InstaForensics and Cognitech 85% for multimedia forensics.

## Related Objectives

- `DFO-1015` Prepare for a digital investigation

## Related Weaknesses

- [[weaknesses/A feature-scoring toolkit ranking that weights all features equally can misrank the best tool for a case's actual priorities]]

## References

- [DFCite-2002] Javed et al., "A comprehensive survey on computer forensics", IEEE Access, 2022 — source of the FSM formula (Equation 1) and its per-domain toolkit feature comparisons.
