---
id: LWT-2034
type: technique
name: Detect ongoing cyber-attacks using MITRE ATT&CK and Cyber Kill Chain ontological reasoning
description: The process of detecting an in-progress cyber-attack, rather than only individual malicious techniques, by recognizing MITRE ATT&CK techniques from digital artifacts collected during system monitoring, associating them to tactics and Cyber Kill Chain (CKC) phases, and using rule-based ontological reasoning to confirm that a valid, chronologically-ordered combination of related CKC phases has occurred.
objective_ids:
  - DFO-1019
weakness_ids:
  - LWW-2034
aliases:
  - Fronesis
  - Combinations Of Sequences of CKC Phases (COSP)
source_refs:
  - LWCite-2034
updated_at: 2026-08-14
status: partial
---

# Detect ongoing cyber-attacks using MITRE ATT&CK and Cyber Kill Chain ontological reasoning

## Summary

Signature- and anomaly-based detection approaches typically flag individual malicious events without confirming they form a coherent, in-progress attack, and dwell times for undetected attacks can span weeks. An investigator or defensive system instead continuously examines digital artifacts (both volatile, like running processes, and non-volatile, like emails and log files) collected with digital-forensics-preserving integrity, uses rule-based reasoning to recognize which MITRE ATT&CK technique each artifact's pattern indicates, maps each recognized technique to its tactic and then to a Cyber Kill Chain phase (Delivery, Exploitation, Installation, Command-and-Control), and confirms an ongoing attack only when a proper combination of related, time-ordered phases (a COSP) is found - directly reconstructing the attack's progression rather than just flagging isolated indicators.

## Details

LWCite-2034's Fronesis ontology (built on OWL/SWRL, using UCO for digital-artifact classes) formalizes five core concepts - COSP, Phase, Tactic, Technique, Artifact - and their relationships (hasTrace, hasTechnique, mapsTo, hasPhase). Detection proceeds in two steps: Step 1 recognizes techniques from artifact patterns (e.g. an EmailMessage artifact with an AttachedFile via hasAttachedFile indicates the Spearphishing Attachment technique), associates the recognized technique's tactic, and maps that tactic to its CKC phase, producing a "CORI" (chain of one Phase, Tactic, Technique instance, and its traces); Step 2 searches CORIs for a valid COSP by checking three conditions - the phase combination and order matches one of four defined COSPs (DE, DEI, DEC, DEIC), each pair of adjacent phase instances is "related" (their traces share common or temporally-close attribute values, e.g. the same file path), and each pair of adjacent phases is "subsequent" (later phase's traces are chronologically newer). Reconnaissance/Weaponization and Actions-on-Objective CKC phases are deliberately excluded, since the former occur in attacker-controlled infrastructure invisible to the monitored system and the latter would mean detection only after the attacker already achieved their objective, defeating the "early" detection goal.

## Examples

- LWCite-2034's email phishing worked example: an EmailMessage with an AttachedFile (Spearphishing Attachment technique -> Initial Access tactic -> Delivery phase), a Process that opens a File (Malicious File technique -> Execution tactic -> Exploitation phase), and a WindowsTask (Scheduled Task technique -> Persistence tactic -> Installation phase) are correlated via shared file paths and subsequent timestamps into a detected COSP(DEI), demonstrated with 16 SWRL rules detecting the attack in 71-815 seconds against 10,000-200,000 artifact individuals on a mid-level workstation.

## Related Objectives

- `DFO-1019` Detect anti-forensics and other anomalies

## Related Weaknesses

- [[weaknesses/Ontology-based cyber-attack detection cannot recognize attacks outside the modeled Cyber Kill Chain sequence or MITRE ATT&CK catalog]]

## References

- [LWCite-2034] Dimitriadis et al., "Fronesis: Digital forensics-based early detection of ongoing cyber-attacks", IEEE Access, 2023 — source of the Fronesis ontology, COSP detection methodology, and email phishing worked example described above.
