---
id: LWT-2094
type: technique
name: Identify the creator tool of a PDF document using byte-frequency and entropy machine-learning classification
description: Determine which specific software tool (e.g. Adobe Acrobat PDFMaker, Microsoft Word, LibreOffice Writer, TeX, Apple Pages) was used to create a PDF document -- and, with lower accuracy, which version of that tool -- by training a machine-learning classifier (a convolutional neural network performs best) on each candidate document's byte-frequency distribution combined with its Shannon entropy, without relying on the document's metadata, which can be trivially removed or tampered with.
objective_ids:
  - DFO-1004
  - DFO-1008
weakness_ids:
  - LWW-2099
aliases:
  - Forensic digital document examination (FDDE) tool type identification
source_refs:
  - LWCite-2116
updated_at: 2026-08-16
status: complete
---

# Identify the creator tool of a PDF document using byte-frequency and entropy machine-learning classification

## Summary

Establishing which software tool created a digital document supports questioned-document-style investigative questions about a document's origin and authenticity -- for instance, flagging that a document was produced by a tool known to have security vulnerabilities, or that it was created with an unusual or unexpected tool for its claimed context -- but conventional metadata-based tool attribution is unreliable since metadata can be edited or stripped without altering the document's actual content. Extending byte-level file-type-identification techniques (byte-frequency distribution and entropy, both used previously for distinguishing file *types*) to the finer-grained problem of distinguishing which specific *tool* created a document of an already-known type achieves high classification accuracy without depending on any metadata field.

## Details

For each PDF file, a byte-frequency histogram is computed by counting the occurrence of every possible byte value (0-255) across the file and normalizing by total byte count, producing a 256-dimensional feature vector describing the file's overall byte-value distribution; Shannon entropy is separately computed from the same byte-value probability distribution as a single scalar summarizing the file's overall randomness/predictability. The two features are combined into a composite feature vector and used to train and compare six machine-learning classifiers (decision tree, random forest, gradient boosting machine, k-nearest neighbors, support vector machine, and a convolutional neural network) to predict which of several candidate creator tools produced a given PDF, using a labeled training/test dataset assembled from documents scraped across multiple public repositories (GovDocs, Data.gov, SafeDocs, and arXiv) and labeled by their internal creator/producer metadata tag (used only as the ground-truth label for training, not as a feature the classifier sees), with the tag itself scrubbed from the file before feature extraction to ensure the model learns from byte-level structure rather than trivially reading the same metadata a real-world questioned document may lack. Because some tool categories were naturally underrepresented in the scraped datasets, oversampling of minority classes was applied and shown to measurably improve classification performance, particularly for the CNN and random forest models.

## Examples

- Across eight PDF creator tools (ACOMP.exe, PScript5.dll, Microsoft Word, Acrobat PDFMaker for Word, TeX, Adobe InDesign, LibreOffice Writer, Apple Pages), the CNN classifier achieved the highest overall performance with oversampling applied (96% accuracy, 96% precision, 96% recall, 97% F1-score), followed by Random Forest (92% accuracy) and SVM/GBM (91%/90% accuracy); KNN and Decision Tree performed markedly worse (79% and 83% accuracy respectively), likely because PDFs from different tools can still show similar overall byte distributions, degrading the effectiveness of KNN's distance-based similarity measure specifically.
- Per-tool accuracy varied substantially: ACOMP.exe, Microsoft Word, TeX, and Apple Pages were classified with over 95% accuracy by most models (consistent, tool-specific byte-level structure), while Adobe InDesign and Acrobat PDFMaker showed more mixed results (Decision Tree/KNN around 81%, CNN up to 95%), and PScript5.dll and LibreOffice Writer were the most challenging tools to classify, with KNN and Decision Tree accuracy in the 69-73% range even though CNN again performed significantly better for these tools.
- A follow-up experiment applying the same byte-frequency-plus-entropy approach to distinguish between different *versions* of the same tool (four versions each of Acrobat PDFMaker and Microsoft Word) confirmed feasibility but with substantially lower accuracy than tool-type classification (roughly 60-85% depending on model and specific version pair), attributed in part to a smaller available sample size per version (2,000 files) limiting the models' ability to learn fine-grained version-specific distinctions.

## Related Objectives

- `DFO-1004` Conduct research
- `DFO-1008` Establish identities

## Related Weaknesses

- [[weaknesses/PDF creator-tool classification accuracy is markedly lower for version-level identification than tool-level identification]]

## References

- [LWCite-2116] Zia and Adedayo, 2025, "Tool type identification for forensic digital document examination", FSI: Digital Investigation 54, 301972.
