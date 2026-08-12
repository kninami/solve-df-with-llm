---
id: DFT-1064
type: technique
name: Synthesize digital forensic training and validation datasets
description: Build synthetic datasets for forensic tool training, testing, and validation by scripting simulated human activity and automatically executing it against a target environment, rather than manually populating devices or systems by hand — either by having an LLM agent author a Markdown-based "storyboard" of user activities executed on a real or emulated mobile device, or by driving a virtualized desktop/network environment through a modular declarative-scripting framework, with generated-artifact provenance documented for later use.
objective_ids:
  - DFO-1004
weakness_ids:
  - DFW-1069
  - DFW-1071
aliases:
  - Automated synthesis of digital forensic training and validation datasets
  - AutoPodMobile
  - APM
  - AKF
  - Automated Kinetic Framework
source_refs:
  - DFCite-1059
  - DFCite-1061
updated_at: 2026-08-10
status: complete
---

# Synthesize digital forensic training and validation datasets

## Summary

Manually building forensic datasets by hand is time-consuming and rarely reflects the full breadth of real-world conditions, and prior synthesizers are often narrowly scoped to one artifact type or one platform. Two complementary automated-synthesis approaches address this for different platform targets: an LLM-agent-driven storyboard toolchain for mobile devices, and a modular declarative-scripting framework for virtualized desktop/network environments — both substantially reducing manual effort while preserving reviewability of the generated content.

## Details

**Mobile devices (AutoPodMobile/APM)**: an LLM agent authors a storyboard in APML (a Markdown-based activity language covering roughly 10 user activity types) from a high-level scenario description; each storyboard activity maps to a Python script that executes the corresponding action on a real or emulated phone (e.g. transmitting messages in real time with human-like typing-speed delays, adding contacts or calendar events); a forensic disk image of the populated device is then created (via ADB-based imaging after rooting for Android, or jailbreaking plus SSH-based access for iOS). LLMs run locally so no data needs to leave the local environment.

**Virtualized desktop/network environments (AKF)**: a modular, hypervisor-agnostic framework (targeting VirtualBox-hosted Windows VMs by default) drives simulated human activity through a declarative scripting language — which can itself be authored with the help of generative AI — and automatically documents every generated artifact's provenance using CASE-ontology metadata for later querying. The AKF paper explicitly scopes itself to non-mobile targets and names mobile dataset synthesis as unaddressed future work, making it complementary to (not overlapping with) the mobile storyboard approach; it also does not address efficient distribution of large generated datasets (a problem other tools address via techniques like partition squeezing or differential imaging).

## Examples

- The mobile storyboard toolchain's initial field trials found human participants could not reliably distinguish AI-generated storyboard content from authentic user activity, though this was not a rigorous, statistically validated assessment.
- AKF's sample ransomware scenario demonstrated its declarative syntax, CASE-based artifact logging, and generative-AI-assisted scenario authoring end to end on a virtualized Windows environment.

## Related Objectives

- `DFO-1004` Conduct research

## Related Weaknesses

- [[weaknesses/LLM-generated synthetic mobile forensic dataset content can be factually incorrect or incomplete without expert validation]]
- [[weaknesses/Virtualized-environment forensic dataset synthesis leaves telltale artifacts absent from real-world data]]

## References

- [DFCite-1059] Pawlaszczyk et al., 2025, "AI-driven dataset creation in mobile forensics using LLM-based storyboards", FSI: Digital Investigation 55.
- [DFCite-1061] Gonzales et al., 2025, "AKF: A modern synthesis framework for building datasets in digital forensics", FSI: Digital Investigation 55.
