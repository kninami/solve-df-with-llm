---
id: LWT-2114
type: technique
name: Estimate underage subject age from facial images using FaceNet-embedding regression
description: Predict a specific numeric age (rather than a broad age band or binary child/adult label) for an underage subject depicted in a facial image, by extracting a 512-dimensional FaceNet facial embedding and feeding it into a compact regression neural network trained specifically on underage-skewed datasets, addressing the scarcity of accurately age-labeled underage facial imagery through targeted dataset combination and augmentation.
objective_ids:
  - DFO-1008
weakness_ids:
  - LWW-1127
aliases:
  - Vec2UAge
source_refs:
  - LWCite-2141
updated_at: 2026-08-16
status: complete
---

# Estimate underage subject age from facial images using FaceNet-embedding regression

## Summary

Fine-grained age estimation for underage subjects (a task with direct relevance to indecent-image-of-children investigations) is limited both by the scarcity of large, accurately age-labeled datasets skewing toward younger age brackets, and by most published age-estimation research being built and validated primarily on adult-skewed datasets (e.g. celebrity image datasets, whose subjects are disproportionately represented in a narrow adult age range). Rather than classifying images into broad age bands, this technique treats age as a continuous regression target predicted from a 512-dimensional FaceNet facial embedding (rather than raw pixel input) via a compact four-layer neural network, trained on two combined underage-skewed datasets with targeted data augmentation to help address the underlying data scarcity.

## Details

FaceNet embeddings are high-dimensional vector representations (512 dimensions in this work) produced by a deep convolutional network trained via a triplet-loss function that places facial images of the same identity close together in the embedding space and different identities further apart; using this pre-computed embedding as the regression model's input, rather than raw pixels, gives the downstream model a much lower-dimensional, already-informative starting representation to learn an age mapping from. The regression network itself is a simple four-layer fully-connected network (512, 256, 128, and a single output neuron) using ReLU activations, trained with mean squared error loss to predict a single continuous age value. To address underage-data scarcity, two datasets are combined -- VisAGe (over 21k images, mainly underage subjects, labeled by age and gender) and Selfie-FV (over 21k facial-vector-only images of female subjects aged 8-38) -- and image augmentation (horizontal flip, rotation, random zoom, random distortion, random color/contrast/brightness, random erasure) is applied to the training set specifically to increase effective dataset size for underrepresented age bins, with an augmentation-fidelity check (cosine similarity between original and augmented embeddings) used to confirm an augmentation technique does not distort the facial identity itself before including it in the training pipeline.

## Examples

- Comparing four gradient-based optimizers (ADAM, ADAGRAD, SGD, and Stochastic Weight Averaging) across two experiment sets (a fixed initial learning rate, and a cyclic-learning-rate-informed initial rate), the best-performing model (SGD optimizer, cyclic-rate-informed initial learning rate of 0.0302) achieved a test Mean Absolute Error of 2.36 years, and the best fixed-learning-rate model (ADAM) achieved a test MAE of 2.46 years -- both markedly outperforming a prior contour-based Dlib approach's 2.73-year MAE, and outperforming state-of-the-art cloud-based age-estimation services (Amazon Rekognition, Microsoft Azure Face API) on the same underage bracket.
- Random erasure was found to be the augmentation technique with the highest cosine similarity (0.9837) to the original image's facial embedding, indicating it altered the model's learned facial representation the least of the tested techniques, while random contrast (0.3341) altered it the most; this analysis informed which augmentation techniques were judged safe to apply without risking training the model on a facial representation meaningfully different from the original.
- Per-age-bin error analysis (Mean Absolute Difference) found the winning model performed best (lowest error) for 2, 12, and 14-year-old subjects specifically, with performance following a similar trend across the top three best-performing experiment configurations, informing where the model's predictions can be trusted with greatest confidence within the underage range.

## Related Objectives

- `DFO-1008` Establish identities

## Related Weaknesses

- [[weaknesses/Regression and multi-class age-estimation models under-detect child images despite reasonable aggregate accuracy]]

## References

- [LWCite-2141] Anda, Dixon, and Bou-Harb, 2021, "Vec2UAge: Enhancing underage age estimation performance through facial embeddings", FSI: Digital Investigation 36, 301119.
