---
id: DFM-2096
type: mitigation
name: Verify MLLM agent action completion against a fresh screenshot before trusting automated experiment results involving dynamic content
source_refs:
  - DFCite-2112
updated_at: 2026-08-16
status: complete
---

# Verify MLLM agent action completion against a fresh screenshot before trusting automated experiment results involving dynamic content

## Summary

When using an MLLM-agent-driven Android automation framework for a forensic experiment involving video playback, advertisement-heavy applications, or other rapidly-changing screen content, manually review the framework's action log and captured screenshots to confirm each intended action actually completed as designed, rather than assuming a completed experiment run means every action succeeded.

## Addresses

- [[weaknesses/MLLM-agent-driven Android automation frequently fails on dynamic real-time content such as video playback and pop-up advertisements]]

## How To Apply

After an automated experiment run involving an application or content type known to include fast-changing UI elements (video players, ad-supported apps), review the framework's per-action screenshots and operation logs to confirm each action's actual target was still present and correctly identified at execution time, rather than trusting the run's overall success/failure summary alone. Where an action repeatedly retried up to the operation-count threshold, treat the resulting artifact comparison for that specific action as unreliable and either re-run it with adjusted timing/threshold parameters or fall back to manual interaction for that specific step. Where feasible, use built-in device media controls (e.g. hardware/software media-key events) instead of relying on tap-based interaction with transient on-screen video controls, since this avoids the timing race between screenshot capture and control visibility entirely.

## References

- [DFCite-2112] Shang, Sakzad, and Hall, 2025, "Thumb: A forensic automation framework leveraging MLLMs and OCR on Android device", FSI: Digital Investigation 54, 301949.
