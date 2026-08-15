---
id: DFM-1259
type: mitigation
name: Apply a secondary graph-based correction step to re-score and filter unsupervised insider-threat anomaly detections before escalating them to investigators
source_refs:
  - DFCite-1276
updated_at: 2026-08-14
status: complete
---

# Apply a secondary graph-based correction step to re-score and filter unsupervised insider-threat anomaly detections before escalating them to investigators

## Summary

After an unsupervised anomaly-detection model flags candidate insider-threat behavior sequences, run a secondary correction step — for example, hypergraph-based partitioning that clusters flagged sequences by feature-relationship density and assigns each a confidence score based on how tightly it clusters with other flagged anomalies — and only escalate sequences whose correction confidence exceeds a validated threshold.

## Addresses

- [[weaknesses/Unsupervised anomaly-based insider threat detection produces a high false-positive rate because not all behavioral anomalies indicate malicious insider action]]

## How To Apply

Treat the raw output of an unsupervised anomaly-detection model as a candidate list rather than a final finding. Build a weighted hypergraph (or comparable graph-based clustering structure) over the flagged anomalous sequences using their feature relationships, partition it to separate a densely-connected "hyper-abnormal" cluster from a sparser "hyper-normal" cluster, and assign each flagged sequence a correction confidence score reflecting which partition it falls into. Set an escalation threshold via cross-validation on labeled or partially-labeled historical data where available, and route only sequences whose correction confidence clears that threshold to human analyst review, documenting the unescalated majority as suppressed low-confidence anomalies rather than discarding them entirely, in case later evidence warrants revisiting them.

## References

- [DFCite-1276] Wei, Chow and Yiu, 2021, "Insider threat prediction based on unsupervised anomaly detection scheme for proactive forensic investigation", FSI: Digital Investigation 38, 301126.
