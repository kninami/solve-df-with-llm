---
id: LWT-2021
type: technique
name: Detect installed software using a paragraph-vector signature search engine
description: The process of triaging a target disk image to determine which software packages ran on it by comparing the disk's file-path metadata against a database of pre-built software signatures using a doc2vec paragraph-vector similarity search, narrowing the investigation scope before a full manual examination.
objective_ids:
  - DFO-1012
weakness_ids:
  - LWW-2021
aliases:
  - Software Signature Search Engine (S3E)
  - Forensic differential analysis for software signatures
source_refs:
  - LWCite-2021
updated_at: 2026-08-14
status: partial
---

# Detect installed software using a paragraph-vector signature search engine

## Summary

Rather than manually searching a disk image's hundreds of thousands of files and folders for traces of every application of interest - a slow, examiner-experience-dependent process - an investigator pre-builds a "software signature" (the set of file paths consistently created when a given application is installed and run under several usage scenarios) for each software package of interest, then queries a target disk's own file-path list against a database of these signatures using a similarity-search engine to quickly conclude which software packages were present.

## Details

LWCite-2021's signature-construction subsystem builds each software's signature via forensic differential analysis: disk copies are taken before and after running a target application under multiple usage scenarios (e.g. opening/editing/saving different file types), fiwalk extracts each copy's file-system metadata as DFXML, and `make_differential_dfxml` isolates the file paths created during that run; combining the difference-sets across all scenarios for a piece of software yields its signature. The signature-detection subsystem (the Software Signature Search Engine, S3E) then trains a doc2vec model (PV-DM or PV-DBOW) over the full signature corpus so each software signature and the target disk's own extracted file-path query become vectors in a shared space; cosine similarity between the query and each signature is compared against a per-software threshold (itself calibrated by querying a freshly installed "base-controlled" system, which has no software installed, against each signature) to decide presence or absence. Because signature word order and syntax differ from natural language (each "sentence" is a full file path, each "word" a path component, separated by `/` rather than spaces), the paragraph-vector approach still outperformed both an averaged word2vec model and a TF-IDF-based model on recall in the paper's experiments.

## Examples

- LWCite-2021's 120 tested S3E model configurations (varying doc2vec type, vector size, window size, and threshold) against 20 controlled machines (Windows 7/XP) and the M57 Patents corpus: the top-recall models used PV-DM with a small/medium threshold, achieving perfect (1.0) recall on controlled machines and up to 1.0 recall on M57 machines, with query time under 7 seconds per S3E model.

## Related Objectives

- `DFO-1012` Locate potentially relevant content

## Related Weaknesses

- [[weaknesses/Software signature search engine precision degrades sharply on realistic forensic datasets]]

## References

- [LWCite-2021] Soltani et al., "Developing software signature search engines using paragraph vector model: A triage approach for digital forensics", IEEE Access, 2021 — source of the forensic differential analysis signature construction and S3E doc2vec search engine described above.
