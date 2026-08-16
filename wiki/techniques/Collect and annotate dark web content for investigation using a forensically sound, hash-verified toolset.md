---
id: DFT-2068
type: technique
name: Collect and annotate dark web content for investigation using a forensically sound, hash-verified toolset
description: Manually select, categorize, and annotate clear- and dark-web (Tor .onion) content of investigative interest directly in-browser, automatically archive the annotated page and its metadata with hash-verified integrity checks, synchronize annotations across a team of collaborating investigators via a central server, and use the resulting labelled data set to train ML classifiers that automatically categorize previously unseen web pages.
objective_ids:
  - DFO-1012
weakness_ids:
  - DFW-2068
aliases:
  - The Digital Detective's Discourse
  - D3 toolset
source_refs:
  - DFCite-2072
updated_at: 2026-08-15
status: complete
---

# Collect and annotate dark web content for investigation using a forensically sound, hash-verified toolset

## Summary

Investigators frequently need to manually select and tag dark web content relevant to a case, but lacked a bespoke tool for doing so with forensic soundness and team collaboration. This technique implements annotation as a browser add-on (for Tor Browser or regular Firefox) that lets an investigator right-click to categorize a page or save highlighted text, automatically archives the full page content and metadata to a central, hash-verified database, and uses the accumulating labelled data set both to measure inter-annotator agreement and to train classifiers that categorize new, previously unseen web pages.

## Details

The toolset (called "D3") is built from five components: an in-browser annotator add-on that lets a non-technical investigator right-click to save highlighted text, create a custom category, and annotate/categorize the active page (each interaction is hashed with SHA256 — or MD5 specifically for .onion URLs, to enable comparison against a public dark-web blacklist — and timestamped before being queued for sync); a central server component that receives synchronized annotation data via a REST API, verifying a SHA256 hash sum of each transmitted message against what was sent to confirm the data's integrity was preserved in transit; a collector component that, once a new URL is received centrally, independently fetches and archives the raw page content (via Torsocks for `.onion` addresses) to preserve chain of custody separately from the annotator's own view of the page; an analyzer component that builds ML classifiers (SVM, Logistic Regression, Random Forest, Naive Bayes) from the accumulated annotations/categorizations/highlighted-text/page-content bag-of-words, and separately calculates inter-annotator agreement (Cohen's kappa) between two annotators' categorizations of the same content; and a dashboard visualizer presenting the latest annotated URLs, database statistics, and agreement/classifier scores to the investigative team. This complements dark-web analysis techniques focused on an already-collected data set, such as [[techniques/Map a Tor darkmarket ecosystem using bipartite network analysis of onion services and identification forms]], by providing the upstream, forensically-sound collection and labelling step those analyses depend on.

## Examples

- A 95-URL demonstration data set (categorized as dark marketplace, steroids, covid-19, gambling, hacking, credit cards, seized, or legitimate, drawn ~85% from confirmed cybercriminal content and ~15% legitimate, checked against a public dark-web blacklist to confirm no child abuse material was inadvertently included) trained classifiers that reached 85-96% accuracy on previously unseen pages via five-fold cross-validation, with Random Forest achieving a balanced accuracy above 85% (precision 0.86, recall 1.00).
- A fictitious case-study workflow: an investigator searches for drug-marketplace URLs via a clear-web dark-web-link aggregator, annotates and categorizes each Tor page as belonging to a specific drug type using the add-on, and the resulting shared, growing training data set lets the classifier automatically flag new URLs relating to the same drug type without every investigator having to manually visit and review them.

## Related Objectives

- `DFO-1012` Locate potentially relevant content

## Related Weaknesses

- [[weaknesses/Inter-annotator disagreement in manually categorizing dark web content degrades the reliability of ML classifiers trained on it]]

## References

- [DFCite-2072] Bergman & Popov, 2022, "The Digital Detective's Discourse: A Toolset for Forensically Sound Collaborative Dark Web Content Annotation and Collection", JDFSL 17(5). Source of the D3 toolset architecture, its hash-verification/chain-of-custody design, the 95-URL demonstration data set, and the classifier/inter-annotator-agreement evaluation.
