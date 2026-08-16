---
id: DFT-2088
type: technique
name: Detect periods of phone movement using WhatsApp logfiles and iOS motion-sensor cache traces
description: Reconstruct periods when an iPhone was being carried, walking, or driving -- beyond what the Health app itself records -- by parsing WhatsApp's internal logfiles for network-state and connectivity-change entries correlated with movement, and by parsing the iOS `cache_encryptedC.db` file's motion-classification tables (MotionStateHistory, StepCountHistory, NatalieHistory), which log the device's own on-board motion-state estimates independent of any specific app.
objective_ids:
  - DFO-1001
weakness_ids:
  - DFW-2091
aliases:
  - iPhone movement traces from WhatsApp and cache_encryptedC.db
source_refs:
  - DFCite-2107
updated_at: 2026-08-16
status: complete
---

# Detect periods of phone movement using WhatsApp logfiles and iOS motion-sensor cache traces

## Summary

Beyond the well-studied Health app (see [[techniques/Evaluate iPhone Health app distance data using a likelihood ratio]]), an iPhone retains at least two further sources of movement-related evidence: WhatsApp's own diagnostic logfiles, which record network connectivity transitions that correlate with a phone physically moving between network coverage areas, and the OS-level `cache_encryptedC.db` file, which stores the device's continuous internal motion-state classification (e.g. stationary, walking, running, automotive/driving) independent of any particular app being open.

## Details

WhatsApp's plaintext logfiles record connectivity events (e.g. Wi-Fi-to-cellular handoffs) with timestamps; because such handoffs often correlate with a phone physically leaving or entering a given network's coverage area, a sequence of these events over time can support an inference about when a device (and its likely carrier) was moving between locations, without needing an app-specific location or activity API. The `cache_encryptedC.db` SQLite database, part of iOS's CoreMotion/health-sensing infrastructure, contains several tables logging different aspects of the device's continuous on-board motion classification: `MotionStateHistory` records discrete state transitions (e.g. stationary, walking, running, automotive), `StepCountHistory` records step counts over time windows, and `NatalieHistory` records related motion-classification data. Because this classification runs continuously at the OS level regardless of which app (if any) is in the foreground, it can corroborate or extend movement inferences drawn from app-specific sources like the Health app, and it persists data even when no specific health- or fitness-tracking app was ever opened by the user.

## Examples

- Controlled experiments comparing ground-truth movement periods (walking, driving, and stationary segments performed by test subjects) against the timing derived from WhatsApp logfile connectivity events and `cache_encryptedC.db` motion-state transitions measured the true positive rate, false discovery rate, and average timing accuracy (typically on the order of tens of seconds) with which each source's inferred movement periods matched the ground truth.

## Related Objectives

- `DFO-1001` Reconstruct events

## Related Weaknesses

- [[weaknesses/Phone-based movement-detection accuracy from app and OS traces varies sharply by phone-lock state and foreground-app status]]

## References

- [DFCite-2107] van Zandwijk and Boztas, 2021, "The phone reveals your motion: digital traces of walking, driving and other movements on iPhones", FSI: Digital Investigation 37, 301170.
