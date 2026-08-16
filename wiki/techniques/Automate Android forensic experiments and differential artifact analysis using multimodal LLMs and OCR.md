---
id: DFT-2091
type: technique
name: Automate Android forensic experiments and differential artifact analysis using multimodal LLMs and OCR
description: Drive a rooted physical Android device through a forensic experiment using plain natural-language action descriptions (rather than scripted commands or widget IDs), interpreted and executed by a multimodal large language model (MLLM) agent that perceives the screen via OCR and icon localization, then automatically extract and differentially compare the device's internal storage before and after each action to attribute specific artifact changes (thumbnails, cache files, database records) to the specific user action that caused them.
objective_ids:
  - DFO-1004
  - DFO-1011
weakness_ids:
  - DFW-2095
aliases:
  - Thumb
source_refs:
  - DFCite-2112
updated_at: 2026-08-16
status: complete
---

# Automate Android forensic experiments and differential artifact analysis using multimodal LLMs and OCR

## Summary

Prior automated Android forensic experiment frameworks (e.g. AnforA) require an examiner to write detailed scripted command sequences referencing specific UI widget IDs, a significant barrier to entry, and physical-device testing is often skipped in favor of virtual machines, which can behave differently from real hardware (e.g. installation failures, anti-forensic detection of virtualized environments). Thumb addresses both limitations: an examiner describes each experiment action in plain natural language (e.g. "open the video displayed on the screen exactly once by clicking directly on the video frame"), and two cooperating MLLM agents interpret the current screen state (via OCR text extraction and icon-localization models) and decide/execute the corresponding ADB-driven action directly on a rooted physical device, after which the framework automatically extracts and differentially compares the device's `/data/data` application storage before and after the action.

## Details

The framework has three components run in sequence. **Authentication** confirms ADB connectivity and root access to the target device (`adb shell su -c whoami` returning `root`), then accepts the examiner's plain-language list of experiment actions and target application package name. **Automation test** iterates through each action: a planning agent tracks overall task progress, a decision agent interprets the current screen (via the visual perception module's OCR and icon-localization output) and selects the next operation from a constrained action space (tap, swipe, type text, open app, pause video, home, stop), executed via ADB; a memory unit retains short-term context across the steps of a single action so the agent can track multi-step progress within a complex instruction. An operation-count threshold (empirically set to 7 attempts) caps how long the agent will retry a given action before declaring it failed, both preventing infinite loops on unexpected pop-ups/redirects and flagging actions that likely diverged from the intended sequence. **Analysis** then extracts the target application's directory before and after each action (via `tar`/`adb pull`, with a hash computed and re-verified for integrity), and a recursive directory-comparison function classifies every file as modified, added, or removed; type-specific sub-analyzers further interpret the changes for XML files (tag/attribute/value diffs), SQLite databases (table/row/column diffs), and images (signature-based carving for common formats, SIFT-based keypoint matching to compare thumbnails/screenshots against the corresponding full-size image or a captured screenshot, and metadata extraction), with detected keywords also cross-referenced against captured screenshots to verify on-screen relevance.

## Examples

- Comparing user actions across capturing a photo with the device camera, saving an image from WhatsApp, and subsequently opening it in the gallery, the framework's differential and thumbnail-comparison analysis distinguished the resulting cache artifacts precisely: a camera-captured photo generated a 177x177 thumbnail in `files/gallery_disk_cache/small_size/` immediately, a WhatsApp-saved image generated no equivalent cache entry until the gallery was subsequently opened, and opening any image in the gallery (regardless of its origin) generated a 237x237 `small_size` thumbnail plus, upon clicking the image, two further 177x235 thumbnails and one full-size 720x956 thumbnail -- and deleting the image from the gallery did not remove any of the already-cached thumbnails.
- Comparing a Chrome login performed on an Android emulator versus a physical device, the emulator was found to store a `password_value` field within a discoverable login-related database file that the physical device did not retain in the same location, illustrating a concrete virtualization-versus-real-device artifact discrepancy the framework's differential analysis directly surfaced.
- Across a set of applications flagged by the Internet Watch Foundation as highly susceptible to misuse for distributing inappropriate content (browsers, video-streaming platforms, chat apps, peer-to-peer file-sharing software), the framework achieved automation performance measured via four metrics (success rate, error-step count, operation execution time, extraction time), demonstrating adaptability across a broad range of application types without per-application scripting.

## Related Objectives

- `DFO-1004` Conduct research
- `DFO-1011` Extract artifacts stored by applications

## Related Weaknesses

- [[weaknesses/MLLM-agent-driven Android automation frequently fails on dynamic real-time content such as video playback and pop-up advertisements]]

## References

- [DFCite-2112] Shang, Sakzad, and Hall, 2025, "Thumb: A forensic automation framework leveraging MLLMs and OCR on Android device", FSI: Digital Investigation 54, 301949.
