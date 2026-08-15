---
id: DFT-2003
type: technique
name: Trigger SDN forensic evidence collection using unusual-traffic and unexpected-behavior detectors
description: The process of using two complementary automated detectors within a software-defined network (SDN) - a machine-learning anomalous-traffic classifier and a finite-state-machine element-state comparator - to trigger and scope forensic evidence acquisition to only the SDN records relevant to a cybersecurity event.
objective_ids:
  - DFO-1007
weakness_ids:
  - DFW-2003
aliases:
  - SDN DFIR filtering intelligence model
  - Unusual traffic detector and unexpected behavior detector
source_refs:
  - DFCite-2003
updated_at: 2026-08-14
status: partial
---

# Trigger SDN forensic evidence collection using unusual-traffic and unexpected-behavior detectors

## Summary

Rather than collecting and preserving all SDN controller and switch traffic, an investigator deploys two automated detectors that continuously monitor an SDN: one classifies southbound-interface (OpenFlow) traffic as usual or unusual using a trained AI model, and the other compares each SDN element's current state (applications, topology, devices, flows, links, controller access) against its baseline "genesis state" using a finite-state-machine and cross-source majority consensus. Either detector firing triggers the digital forensic and incident response (DFIR) evidence-gathering pipeline, scoping acquisition to only the data plausibly related to the detected event.

## Details

DFCite-2003 implements the unusual traffic detector as an ETL pipeline (extraction of 52 OpenFlow packet features via Pyshark, cleaning, ANOVA/Pearson/Random-Forest-based feature selection down to 8 features, one-hot encoding and centering/scaling normalization) feeding a 5-layer Keras neural network (ReLU hidden layers, Sigmoid output) trained for binary usual/unusual classification, achieving 97.2% average accuracy, 97.34% F1, and AUC 0.81-0.82 across 5-fold cross-validation on a proprietary OpenFlow dataset. The unexpected behavior detector instead models each SDN element's lifecycle as a finite state machine (Genesis -> Idle -> Auxiliary -> Next state), triggering data gathering only once a majority (at least half-plus-one) of independent information sources (activity logs and controller-API-derived state) agree a change occurred, providing corroboration against a single unreliable source. Together the two detectors feed a Filtering, Acquisition, and Treatment Engine that standardizes, deduplicates, and timestamps only the pertinent records before handing them to the forensic processing engine, reducing storage and analysis burden relative to blanket capture-everything approaches.

## Examples

- DFCite-2003's proprietary OpenFlow dataset (522,886 instances, 25/05/2023-29/06/2023) used to train/validate/test the unusual-traffic neural network, evaluated against a Mininet/ONOS DDoS attack scenario and an SDN-application-change scenario.

## Related Objectives

- `DFO-1007` Reduce data under consideration

## Related Weaknesses

- [[weaknesses/An SDN unusual-traffic detector's imperfect recall on usual traffic triggers unnecessary forensic evidence acquisition]]

## References

- [DFCite-2003] Jiménez et al., "A filtering model for evidence gathering in an SDN-oriented digital forensic and incident response context", IEEE Access, 2024 — source of the dual-detector filtering intelligence model and its evaluation metrics.
