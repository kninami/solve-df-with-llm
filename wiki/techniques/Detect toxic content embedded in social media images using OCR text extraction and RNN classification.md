---
id: DFT-2110
type: technique
name: Detect toxic content embedded in social media images using OCR text extraction and RNN classification
description: Detect "troll" or toxic content that a social media user has embedded as text within an image (e.g. a meme or screenshot) -- content invisible to a purely text-based moderation or investigation pipeline -- by extracting the embedded text with optical character recognition (OCR) and classifying the extracted text as toxic or non-toxic with a bidirectional recurrent neural network.
objective_ids:
  - DFO-1019
  - DFO-1012
weakness_ids:
  - DFW-2117
aliases:
  - OCR-plus-deep-learning social media troll detection
source_refs:
  - DFCite-2137
updated_at: 2026-08-16
status: complete
---

# Detect toxic content embedded in social media images using OCR text extraction and RNN classification

## Summary

Toxic or harassing ("troll") content on social media is not confined to plain text posts; it is frequently embedded as text within an image, which a text-only content-analysis or keyword-search pipeline cannot see at all. Running OCR over collected images first, then classifying the recovered text with a bidirectional recurrent neural network trained on labeled toxic/non-toxic text, extends automated toxic-content detection to this image-embedded-text category, supporting an investigator's review of harassment, cyberbullying, or other toxic-content cases.

## Details

Collected social media images are passed through an OCR engine to extract any embedded text, which is then pre-processed (tokenization, normalization) before being fed into a trained bidirectional RNN (which processes the text sequence in both forward and backward directions, letting the model use context from both preceding and following words when judging toxicity) that outputs a toxic/non-toxic classification. Because OCR accuracy depends heavily on how the source image renders its text (font choice, background contrast, image resolution/compression), the pipeline's overall accuracy is bounded by how reliably the OCR stage extracts a faithful transcription for the model to classify, in addition to the RNN classifier's own accuracy on well-transcribed text.

## Examples

- Evaluated on a labeled dataset of toxic and non-toxic social-media-style images, the combined OCR-plus-RNN pipeline achieved an overall detection accuracy of approximately 92% on images using standard, clearly-legible fonts.
- Accuracy dropped substantially, to roughly 62-88% depending on the specific style, when the source images used stylized, decorative, or otherwise non-standard fonts, since OCR misreads of the underlying text propagate directly into misclassification regardless of the RNN classifier's own accuracy on correctly-transcribed text.

## Related Objectives

- `DFO-1019` Detect anti-forensics and other anomalies
- `DFO-1012` Locate potentially relevant content

## Related Weaknesses

- [[weaknesses/OCR-based toxic-content detection accuracy drops sharply for images using stylized or decorative fonts]]

## References

- [DFCite-2137] "Using deep learning to detect social media 'trolls'", FSI: Digital Investigation 48, 2024.
