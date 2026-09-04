---
id: LWT-2112
type: technique
name: Triage large-scale criminal evidence image collections using a microservice-based multi-classifier pipeline
description: Scale automated image triage for a large criminal-evidence image collection (potentially millions of images across many concurrent cases) by decomposing the analysis into a set of independently deployable microservices -- each running a specialized classifier for a specific evidence category (firearms, ammunition, identity documents, nudity, age, OCR text, face recognition) -- orchestrated through a distributed message-queue and stream-processing architecture rather than a single monolithic classification pipeline.
objective_ids:
  - DFO-1007
  - DFO-1003
weakness_ids:
  - LWW-2119
aliases:
  - INSIDE
source_refs:
  - LWCite-2139
updated_at: 2026-08-16
status: complete
---

# Triage large-scale criminal evidence image collections using a microservice-based multi-classifier pipeline

## Summary

A single case's seized devices can yield hundreds of thousands of images, and a law enforcement agency processes many cases concurrently, making a monolithic, single-machine image-classification pipeline impractical to scale. Structuring image analysis as a set of independent microservices, each specialized for one evidence category and independently scalable, and coordinating them through a distributed message queue (Kafka) and stream-processing framework (Spark), lets an agency add computational capacity for whichever specific classifier categories are the current bottleneck, and add or update individual classifiers without redeploying the entire pipeline.

## Details

Incoming case images are published to a message queue, from which each specialized microservice (a firearm classifier, an ammunition classifier, an identity-document classifier, a nudity classifier, an age-estimation classifier, an OCR text-extraction service, and a face-recognition service) independently consumes and processes images relevant to its own category, publishing results back to a central store for an investigator's review. Because each microservice is independently deployable and scalable, an agency experiencing a backlog specifically in, for example, firearm-image review can allocate additional compute resources to just that microservice without needing to scale the entire pipeline, and a new or improved classifier for one evidence category can be deployed as a drop-in replacement for its microservice without disrupting the others. This architecture explicitly separates the object-detection question ("is a firearm present in this image") from the object-localization question ("where in the image is the firearm"), noting that useful investigative triage requires the location information as well as a bare presence/absence flag to be practically actionable for an investigator reviewing flagged images.

## Examples

- The firearm, ammunition, and identity-document classifiers were evaluated on held-out test data, with the firearm classifier's precision and recall each in the 0.6-0.8 range depending on the specific object subcategory, illustrating that even a purpose-built classifier for a well-defined evidence category leaves a meaningful proportion of relevant images undetected.
- The architecture's independent scalability was demonstrated by provisioning additional processing capacity specifically for the microservices experiencing the highest incoming image volume during a simulated high-throughput scenario, without needing to over-provision capacity for lower-volume classifier categories.

## Related Objectives

- `DFO-1007` Reduce data under consideration
- `DFO-1003` Review content for relevance

## Related Weaknesses

- [[weaknesses/Low-recall evidence-category image classifiers used for triage miss a substantial proportion of relevant images]]

## References

- [LWCite-2139] "Using micro-services and artificial intelligence to analyze images in criminal evidences", FSI: Digital Investigation 48, 2024.
