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
  - ChatGPT-assisted teaching scenario storyboarding
  - ForTrace
source_refs:
  - DFCite-1059
  - DFCite-1061
  - DFCite-1110
  - DFCite-1247
  - DFCite-1267
  - DFCite-1273
updated_at: 2026-08-14
status: complete
---

# Synthesize digital forensic training and validation datasets

## Summary

Manually building forensic datasets by hand is time-consuming and rarely reflects the full breadth of real-world conditions, and prior synthesizers are often narrowly scoped to one artifact type or one platform. Two complementary automated-synthesis approaches address this for different platform targets: an LLM-agent-driven storyboard toolchain for mobile devices, and a modular declarative-scripting framework for virtualized desktop/network environments — both substantially reducing manual effort while preserving reviewability of the generated content.

## Details

**Mobile devices (AutoPodMobile/APM)**: an LLM agent authors a storyboard in APML (a Markdown-based activity language covering roughly 10 user activity types) from a high-level scenario description; each storyboard activity maps to a Python script that executes the corresponding action on a real or emulated phone (e.g. transmitting messages in real time with human-like typing-speed delays, adding contacts or calendar events); a forensic disk image of the populated device is then created (via ADB-based imaging after rooting for Android, or jailbreaking plus SSH-based access for iOS). LLMs run locally so no data needs to leave the local environment.

**Virtualized desktop/network environments (AKF)**: a modular, hypervisor-agnostic framework (targeting VirtualBox-hosted Windows VMs by default) drives simulated human activity through a declarative scripting language — which can itself be authored with the help of generative AI — and automatically documents every generated artifact's provenance using CASE-ontology metadata for later querying. The AKF paper explicitly scopes itself to non-mobile targets and names mobile dataset synthesis as unaddressed future work, making it complementary to (not overlapping with) the mobile storyboard approach; it also does not address efficient distribution of large generated datasets (a problem other tools address via techniques like partition squeezing or differential imaging).

**Holistic simultaneous multi-layer synthesis (ForTrace)**: rather than targeting persistent storage alone or persistent-plus-network as prior tools did, ForTrace extends the earlier hystck framework into a client-server architecture (a host-side Framework Master driving one or more cloned guest VMs over a private management network) capable of generating correlated persistent-disk, volatile-memory, and network traces from the same simulated scenario simultaneously. A YAML-driven Generator lets a non-programmer configure which User Interaction Model modules (browser, email, file transfer, encrypted-container, PowerShell, multi-user, printer, and a two-component malware-synthesis module covering four infection vectors and multiple persistence mechanisms) run during a scenario, including a random-content flag for background-noise uniqueness; a separate anti-forensics module can suppress or wipe typical Windows artifacts (registry-key-based service disabling, secure deletion of Prefetch/Event Log entries) to simulate an attacker's own evidence-elimination attempts. An XML-based Reporter component logs every executed action and guest-side timestamp as ground truth, and KVM's own snapshotting facility performs the memory acquisition.

**Agent-less holistic synthesis (ForTrace without a client-side agent)**: since a scenario's realism is compromised by any client-side software component running inside the guest to drive or report on the simulation (see [[weaknesses/Virtualized-environment forensic dataset synthesis leaves telltale artifacts absent from real-world data]]), a later reworking of ForTrace removes its client-side Agent entirely and moves all simulation control to the host. Input is delivered to the guest purely through the hypervisor's own control channels — a QEMU Monitor object for injecting mouse/keyboard events as if from real hardware, and an optional `libvirt` pseudo-TTY console channel for shell/command-line interaction — with no code of any kind executing inside, or communicating over the network from, the guest. Because this leaves no return channel for ForTrace to confirm an action succeeded, two host-side feedback mechanisms compensate: Normalized Root-Mean-Square-Error comparison between successive screenshots (used narrowly, e.g. to detect that a VM has finished booting) and, more generally, on-screen text extraction via OCR checked against expected substrings (e.g., to detect and dismiss a cookie-consent popup by matching "Accept"/"Decline" in the extracted text), rather than the curated GUI-element template-matching library used by an earlier, more limited attempt at client-side-software removal. A proof-of-concept multi-participant Linux attack scenario (an SFTP file-sharing server exploited via CVE-2015-3306, attacked from a Kali Linux machine using Metasploit) demonstrated the approach end to end, producing RAM dumps, network dumps, and disk images with no client-side agent present on either VM. A subsequent refinement replaces the earlier curated GUI-element template-matching library with a general computer-vision object-detection model trained to recognize on-screen UI elements (buttons, text fields, dialog affordances) directly from screenshots, letting the host-side controller determine where to click or type without needing per-application templates prepared in advance or brittle fixed screen coordinates that break across resolutions, themes, or minor UI updates — improving both the realism (more human-like, visually-grounded interaction rather than coordinate-scripted input) and the maintainability of agent-less scenario synthesis.

**Manually-authored teaching scenarios (ChatGPT-assisted storyboarding)**: rather than executing a storyboard against a real or emulated device/VM, a general-purpose LLM can be prompted directly to author the narrative content of a digital forensics teaching scenario for manual population — an overall multi-month storyboard of a scenario's events (e.g. an intellectual-property-theft case progressing from an employee's discontent to a decision to exfiltrate data), character profiles and personas for victims/perpetrators including background, motive, and search-term themes, and synthetic content artifacts (chat conversations, emails, assignment documents, anonymised messages) that would populate the resulting disk image. This lighter-weight approach requires manual construction of the actual evidence artifacts from the generated narrative content, rather than automated on-device execution, but was found to produce well-constructed, useful storyboards through iterative prompting (later corrected for less-realistic scenario choices when explicitly asked to improve them).

## Examples

- The mobile storyboard toolchain's initial field trials found human participants could not reliably distinguish AI-generated storyboard content from authentic user activity, though this was not a rigorous, statistically validated assessment.
- AKF's sample ransomware scenario demonstrated its declarative syntax, CASE-based artifact logging, and generative-AI-assisted scenario authoring end to end on a virtualized Windows environment.
- Prompted with "generate an outline timeline of a scenario where someone within a workplace starts a new job and slowly becomes discontent and begins to steal intellectual property", GPT-4 produced a 6-month narrative arc with month-by-month behavioral and internet-history themes, which further prompting expanded into specific candidate search terms and synthetic supporting messages for each month.
- ForTrace's multi-user exfiltration validation scenario had a simulated malicious user disable the Windows Event Log and Prefetch before using a VeraCrypt container to exfiltrate data over SMB, then re-enable the disabled services and securely delete the user account; despite this, security-auditing log entries and a memory-recoverable password (via Volatility) still revealed the malicious activity, and its separate malware-synthesis validation scenario planted a Registry Run-key persistence mechanism whose corresponding `userinit.exe`-launched process was independently recoverable from a memory dump.
- Comparing the agent-less Linux proof-of-concept against a prior client-side-agent-based ForTrace evaluation's catalog of unintended traces, the agent-less approach eliminated the agent's installation logs, password-less sudo configuration, the ForTrace Python library and its `__pycache__` directory, and the agent process plus its autostart entry — but did not eliminate one console-interaction trace: a shell-history entry from the one-time command used to make the console's command prompt static and script-parseable.
- Replacing template-matching-based GUI element detection with a trained computer-vision object-detection model let the same agent-less scenario controller reliably locate and interact with browser and application UI elements across screen-resolution and theme changes that would have broken a fixed-coordinate or template-based approach.

## Related Objectives

- `DFO-1004` Conduct research

## Related Weaknesses

- [[weaknesses/LLM-generated synthetic mobile forensic dataset content can be factually incorrect or incomplete without expert validation]]
- [[weaknesses/Virtualized-environment forensic dataset synthesis leaves telltale artifacts absent from real-world data]]

## References

- [DFCite-1059] Pawlaszczyk et al., 2025, "AI-driven dataset creation in mobile forensics using LLM-based storyboards", FSI: Digital Investigation 55.
- [DFCite-1061] Gonzales et al., 2025, "AKF: A modern synthesis framework for building datasets in digital forensics", FSI: Digital Investigation 55.
- [DFCite-1110] Scanlon et al., 2023, "ChatGPT for digital forensic investigation: The good, the bad, and the unknown", FSI: Digital Investigation 46.
- [DFCite-1247] Göbel et al., 2022, "ForTrace - A holistic forensic data set synthesis framework", FSI: Digital Investigation 40, 301344.
- [DFCite-1267] Wolf, Göbel, and Baier, 2024, "Hypervisor-based data synthesis: On its potential to tackle the curse of client-side agent remnants in forensic image generation", FSI: Digital Investigation 48, 301690.
- [DFCite-1273] Schmidt and Baier, 2026, "Improving trace synthesis by utilizing computer vision for user action emulation", FSI: Digital Investigation 56, 302073. Replaces template-matching-based GUI interaction targeting with a computer-vision object-detection model for more robust and realistic agent-less scenario driving.
