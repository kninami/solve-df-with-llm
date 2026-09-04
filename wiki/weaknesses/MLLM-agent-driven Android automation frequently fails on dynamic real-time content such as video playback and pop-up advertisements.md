---
id: LWW-2095
type: weakness
name: MLLM-agent-driven Android automation frequently fails on dynamic real-time content such as video playback and pop-up advertisements
description: An MLLM agent that perceives an Android device's screen from discrete screenshots, rather than continuous real-time video, cannot reliably observe or react to content that changes quickly or unpredictably -- such as a video's transient on-screen playback controls, or a pop-up advertisement appearing mid-action -- causing the agent to act on stale screen information and enter repeated failed-action loops until the operation-count threshold is reached.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-2096
source_refs:
  - LWCite-2112
updated_at: 2026-08-16
status: complete
---

# MLLM-agent-driven Android automation frequently fails on dynamic real-time content such as video playback and pop-up advertisements

## Summary

Because most current MLLM systems cannot process real-time video input and respond effectively, an agent attempting to interact with fast-changing on-screen content -- for example, tapping a video frame to reveal media controls that are only visible for a few seconds before disappearing again -- can repeatedly capture a screenshot, decide on an action based on what it saw, and find the target element already gone by the time the action executes, producing a loop of ineffective repeated taps. The framework's own evaluation identified pop-up advertisements appearing between screen-capture intervals as its most significant source of high failure rates and error steps, since the agent's decisions are based on the most recent screenshot, which may no longer reflect the actual current screen state once an unexpected pop-up has appeared.

## Why It Matters

An investigator relying on this class of automation framework to conduct a forensic experiment involving video-playback interaction, advertisement-heavy applications, or any other rapidly-changing UI risks incomplete or stalled experiment execution, and the resulting artifact-differential analysis will only reflect whatever actions the agent actually managed to complete, not necessarily the full intended experiment sequence. Because the operation-count threshold exists specifically to bound how long the agent will retry before giving up, a failed-action loop consumes processing time and attempts without producing the intended data, and a naive interpretation of "no artifacts changed" for a failed action could be mistaken for a genuine forensic finding rather than an automation failure.

## Related Mitigations

- [[mitigations/Verify MLLM agent action completion against a fresh screenshot before trusting automated experiment results involving dynamic content]]

## Used By

- [[techniques/Automate Android forensic experiments and differential artifact analysis using multimodal LLMs and OCR]]

## References

- [LWCite-2112] Shang, Sakzad, and Hall, 2025, "Thumb: A forensic automation framework leveraging MLLMs and OCR on Android device", FSI: Digital Investigation 54, 301949.
