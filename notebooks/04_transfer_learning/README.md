 SignLingual: Transfer Learning
---

## Overview

This folder contains the implementation of two transfer learning models: VGG-16 and ResNet50
The purpose is to leverage these pre-trained models to adapt them to classify sign language gestures effectively.

To evaluate the two models, I will assess performance on:

    1. Original MNIST dataset
    2. Augmented MNIST dataset
    3. Fine-Tuning the models on real world data

## Data Collection

    - MNIST sign language dataset (look at README in data folder)
    - Use images I collected using Teachable Machine (look at README in data folder) to perform fine-tuning

## Model Evaluation

**Results:**

|                  | VGG Model     | VGG with Augmented Data | VGG Fine-Tuned |
|------------------|---------------|-------------------------|----------------|
| Train Score      | 99.98         | 93.70                   | 99.68          |
| Validation Score | 99.83         | 98.98                   | 99.49          |

|                  | ResNet     | ResNet with augmentation | ResNet fine tuned |
|------------------|------------|--------------------------|-------------------|
| Train Score      | 99.99      | 89.27                    | 70.60             |
| Validation Score | 99.88      | 98.28                    | 68.53             |

## Conclusion

Based on the results, the VGG models generally outperform the ResNet models across both original and augmented datasets. VGG has shown its capability in capturing detailed features well enough to generalise to augmented data and to perform well in top-up training. Despite ResNet being a deeper network and therfore learning more features, it requires a large dataset to train effectively. 

Therefore, I will be using VGG as my model to make predictions in my live demo.
