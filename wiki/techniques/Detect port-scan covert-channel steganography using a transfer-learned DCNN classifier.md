---
id: LWT-1248
type: technique
name: Detect port-scan covert-channel steganography using a transfer-learned DCNN classifier
description: Identify a TCP port scan carrying a hidden message encoded in its destination-port ordering (a covert command-and-control channel later retrievable from firewall or syslog records) by rendering each scan's port sequence as a grayscale image and classifying it with a deep convolutional neural network fine-tuned via transfer learning, rather than relying on hand-crafted statistical features.
objective_ids:
  - DFO-1019
weakness_ids:
  - LWW-1264
aliases:
  - DCNN port-scan steganography detector
source_refs:
  - LWCite-1286
updated_at: 2026-08-14
status: complete
---

# Detect port-scan covert-channel steganography using a transfer-learned DCNN classifier

## Summary

An adversary can hide a Command-and-Control message inside the pseudo-random ordering of destination ports in an otherwise-ordinary TCP port scan, which a compromised firewall then logs via syslog for later covert retrieval; because hand-crafted statistical features (timestamps, time-deltas, port sequences) failed to reliably discriminate this pattern from benign port-scan randomness, a deep convolutional neural network trained via transfer learning on an image representation of the scanned-port sequence can instead learn its own discriminating features directly.

## Details

Each captured port scan's sequence of destination ports is rendered as a 32x32 grayscale "image" (each cell representing one of the 1,000 most common TCP ports, marked according to scan occurrence), upscaled to 299x299 and saved as a JPEG to match the input requirements of an ImageNet-pretrained InceptionV3 architecture, whose convolutional feature-extraction layers are frozen and whose final classification layer is replaced with a single sigmoid output distinguishing steganographic from non-steganographic scans. This reframes covert-channel detection as an image-classification problem, letting the network learn whatever discriminating structure exists in the port-selection pattern without the analyst needing to hand-engineer statistical features in advance.

## Examples

- Trained on scans embedding hidden messages at three different bandwidths (256, 512, and 768 covert bits per 1,000-port scan) plus non-steganographic control scans, the detector reached 92.26% accuracy on its own training data but only 60.5% accuracy overall on independent test data, correctly classifying 63% of steganographic and 53% of non-steganographic test samples.
- Detection accuracy on test data rose with embedding bandwidth — 54% at 256 covert bits, 68% at 512 bits, 67% at 768 bits — confirming that a covert channel using more of a port scan's available entropy for embedding is measurably easier to detect than a low-bandwidth one.

## Related Objectives

- `DFO-1019` Detect anti-forensics and other anomalies

## Related Weaknesses

- [[weaknesses/DCNN-based port-scan covert-channel detection accuracy approaches chance level for low-bandwidth embeddings]]

## References

- [LWCite-1286] Lamshöft, Neubert, Hielscher, Vielhauer and Dittmann, 2022, "Knock, knock, log: Threat analysis, detection & mitigation of covert channels in syslog using port scans as cover", DFRWS 2022 EU; FSI: Digital Investigation 40, 301335.
