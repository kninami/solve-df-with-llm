---
id: LWT-1179
type: technique
name: Model digital evidence evaluation using a Bayesian network
description: Combine multiple digital forensic findings into a single, structured, logically-sound probabilistic evaluation by building a case-specific Bayesian network from a set of competing propositions, deriving a likelihood ratio from it to support a transparent, balanced evaluative report.
objective_ids:
  - DFO-1001
weakness_ids:
  - LWW-1187
aliases:
  - Bayesian network evidence evaluation
  - BN modeling for Trojan horse defense cases
source_refs:
  - LWCite-1190
updated_at: 2026-08-13
status: complete
---

# Model digital evidence evaluation using a Bayesian network

## Summary

When several digital findings must be weighed together under disputed propositions about who performed an activity (e.g. a Trojan horse defense claim that malware, not the device owner, downloaded illegal content), reasoning informally in an expert's head produces conclusions that are hard to check, communicate, or defend in court. A Bayesian network makes each observation, proposition, and their probabilistic dependencies an explicit graphical node, from which a likelihood ratio can be mechanically derived using standard BN software.

## Details

The construction proceeds in a fixed sequence of node types: a black proposition node captures the competing case-level hypotheses (e.g. "the suspect knowingly downloaded the files" vs. "an unknown remote party did"); blue activity nodes split each proposition into the concrete activities it entails (e.g. downloading, gaining remote access); green association-proposition nodes capture side-activities the expert also investigated (e.g. "who performed regular user activity around the relevant time?") that are directly linked to but distinct from the main case proposition; yellow transfer/accumulation nodes and red case-finding nodes represent how an activity generates and persists as an observable trace, and the trace actually recovered from the device. Each node has an attached Conditional Probability Table (CPT), and an LR is derived from the fully populated network using BN software (e.g. Hugin). The approach adapts a template originally developed for evaluating physical trace evidence (DNA/fibers) given activity-level propositions, which the source paper found transfers cleanly to digital cases; the resulting network is case-specific but the method (node types, sequence, and colour scheme) generalizes to any dispute over the actor or nature of an activity, not just Trojan horse defense specifically.

## Examples

- A fictive case example modeled whether "Mr. X" or an unknown remote intruder knowingly downloaded illegal files, combining five digital findings (bank payment logs, eMule search history, files present in the home directory, an absent remote-access-tool log despite the tool being installed, and recently-viewed-file entries in a media player) into a single likelihood ratio via the constructed network.
- The network's association-proposition nodes separately modeled "who performed regular user activity around the download time?" and "who performed file-ownership-related activity (e.g. viewing the files) after the download?", allowing side-activity evidence to inform the main proposition without conflating the two.

## Related Objectives

- `DFO-1001` Reconstruct events

## Related Weaknesses

- [[weaknesses/Bayesian network probability assignments rely on subjective judgment outside typical forensic domain expertise]]

## References

- [LWCite-1190] Vink et al., 2025, "Evaluating digital forensic findings in Trojan horse defense cases using Bayesian networks", FSI: Digital Investigation 55, 302023.
