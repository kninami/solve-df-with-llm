---
id: DFM-1071
type: mitigation
name: Disclose and account for virtualization and synthesizer artifacts when using synthetic forensic datasets
source_refs:
  - DFCite-1061
  - DFCite-1247
  - DFCite-1267
updated_at: 2026-08-13
status: complete
---

# Disclose and account for virtualization and synthesizer artifacts when using synthetic forensic datasets

## Summary

When using a virtualization-based synthetic dataset for research, training, or tool validation, explicitly document that the dataset was synthesized and account for the presence of virtualization- and automation-agent-specific artifacts, rather than treating the dataset as equivalent to genuine real-world evidence.

## Addresses

- [[weaknesses/Virtualized-environment forensic dataset synthesis leaves telltale artifacts absent from real-world data]]

## How To Apply

For use cases where discoverable synthesizer artifacts would be a confound (e.g. evaluating anti-forensic or anomaly-detection tooling, or claims about real-world user-behavior realism), either strip or account for known virtualization/agent traces before use, or restrict the dataset's use to purposes (e.g. testing whether a tool correctly parses a given artifact type) where their presence does not compromise the result. Where the synthesis framework provides an explicit cleanup routine (e.g. ForTrace's `initClean()`/`cleanUp()` guest functions, which remove Event Log and Prefetch entries created during template preparation and delete the framework's own installation directory and default user account after a scenario completes), run it as a standard step before distributing a generated image, and document the manual command list needed to remove any remaining traces the automated cleanup does not yet cover.

Where feasible, prefer preventing a trace from being created at all over cleaning it up afterward: a follow-up evaluation found that most of the traces previously catalogued for an agent-based synthesis framework were specifically attributable to the client-side agent component, and that controlling the guest purely through host-side hypervisor means (input injection via the QEMU Monitor, feedback via screenshot comparison or OCR on the guest's graphical output, and console-based shell interaction rather than an in-guest agent process) eliminates the agent's installation logs, password-less sudo configuration, its own library files, and its process/autostart entry outright, since prevention removes an entire class of subsequent-deletion failure modes. This does not eliminate every trace on its own — a shell-history entry from console-prompt setup persisted even without an agent present — so an agent-less architecture should still be paired with the disclosure and cleanup practices above for any traces prevention alone does not cover.

## References

- [DFCite-1061] Gonzales et al., 2025, "AKF: A modern synthesis framework for building datasets in digital forensics", FSI: Digital Investigation 55.
- [DFCite-1247] Göbel et al., 2022, "ForTrace - A holistic forensic data set synthesis framework", FSI: Digital Investigation 40, 301344.
- [DFCite-1267] Wolf, Göbel, and Baier, 2024, "Hypervisor-based data synthesis: On its potential to tackle the curse of client-side agent remnants in forensic image generation", FSI: Digital Investigation 48, 301690.
