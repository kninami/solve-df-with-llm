---
id: DFT-2115
type: technique
name: Identify the messaging app that transmitted a video using container structure and metadata machine learning
description: Determine which of several instant messaging applications (IMAs) transmitted or re-encoded a given video file -- a distinct question from which camera originally captured it -- by extracting features from the video's ISOBMFF container box structure/sequence, video/audio metadata fields, and H.264/H.265 encoding parameters, then classifying the resulting feature vector with a trained ensemble machine-learning model.
objective_ids:
  - DFO-1008
  - DFO-1002
weakness_ids:
  - DFW-2121
aliases:
  - IMA video source application identification
source_refs:
  - DFCite-2144
updated_at: 2026-08-16
status: complete
---

# Identify the messaging app that transmitted a video using container structure and metadata machine learning

## Summary

When a video file is shared via an instant messaging application, the app typically re-encodes it according to its own transmission-quality settings, altering the container structure, metadata, and encoding parameters in ways that are characteristic of that specific application -- distinct from, and complementary to, source-camera identification, since a video's originating camera and its subsequent transmission history are separate investigative questions. Extracting and combining three feature categories (container file format box sequence, video/audio metadata fields, and H.264/H.265 encoding parameters) and training a machine-learning classifier on them can identify which of several candidate messaging apps most recently transmitted a given video file.

## Details

Container File Format (CFF) features capture the type and order of top-level "boxes" within a video's ISOBMFF (MP4/MOV-based) container structure (e.g. `ftyp`, `moov`, `mdat`, and their sub-boxes), since different apps' encoding pipelines produce characteristically different box sequences and internal organization even when the final container format is nominally the same. Video Metadata (VM) features are drawn from both general container-level fields (format profile, brands, writing-application encoder string, movie name, copyright, overall bitrate) and per-stream fields for the audio (title, ID, bitrate, alternate group) and video (title, ID, bitrate, width, height) tracks specifically. Encoding Parameter (EP) features are extracted from the H.264/H.265 bitstream's own control structures (Sequence Parameter Set, Picture Parameter Set, Video Usability Information), including format profile/settings, color range, color primaries, transfer characteristics, and matrix coefficients -- values that reflect specific encoder configuration choices an app's transmission pipeline applies. All numeric features are used directly; textual features (e.g. format profile, codec ID) are tokenized, integer-indexed, and word-embedded, with Principal Component Analysis applied afterward to reduce dimensionality before classifier training. Eleven candidate machine-learning models are compared (including Random Forest, Extra Trees, Gradient Boosting, and several others), with the three best-performing combined into a voting ensemble, and K-fold cross-validation combined with SMOTE oversampling is used to address the inherent class imbalance across apps with different numbers of available transmission/editing option combinations.

## Examples

- Across a self-generated dataset of 1,974 sample videos spanning 16 widely-used IMAs (Band, Discord, Facebook Messenger, KakaoTalk, Line, QQ, Session, Signal, Slack, Snapchat, Teams, Telegram, Viber, WeChat, WhatsApp, Wire) sent via both Android and iOS devices under every available transmission/editing option per app, the Extra Trees model achieved the highest classification accuracy of the eleven models compared, at 99.92% using the full feature set.
- Feature-importance analysis on the winning Extra Trees model found the CFF box sequence feature contributed the single highest importance (9.2%), followed by the H.264/H.265 format-settings encoding parameter (8.5%) and the video-track title metadata field (6.2%), and reducing the feature set to only the top 14-15 most important features (from an initial 22 manually curated features) yielded the highest overall accuracy of 99.96%, exceeding the full-feature-set result.
- t-SNE and UMAP dimensionality-reduction visualizations of the selected feature set showed the 16 IMAs (further split by OS, into 30 total distinct classes) forming visually distinct, well-separated clusters, corroborating the quantitative classification results and confirming the selected features' discriminative power for this task.

## Related Objectives

- `DFO-1008` Establish identities
- `DFO-1002` Extract data from specific formats

## Related Weaknesses

- [[weaknesses/Messaging-app video-source classifiers confuse apps sharing similar vendor re-encoding pipelines]]

## References

- [DFCite-2144] Yang, Kim, and Park, 2024, "Video source identification using machine learning: A case study of 16 instant messaging applications", FSI: Digital Investigation 50, 301812.
