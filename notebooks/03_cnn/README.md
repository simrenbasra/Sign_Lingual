 SignLingual: CNN 
---

## Overview

In this section, I will be building a CNN model with two 2 convolutional layers.

1. Baseline CNN model:
    - Building CNN architecture
    - Training the CNN on the original MNIST dataset
    - Extracting feature maps and kernels out of CNN for model interpretability

2. CNN model with Augmented Data:
    - Using the base CNN model to train on augmented data
    - Assess performance of CNN model with augmentation

## Data Collection

Using data collected from 01_data_processing, to get further details about the data please refer to README in data folder.

## Model Evaluation

**Results:**

|                  | CNN        | CNN with augmentation |
|------------------|------------|-----------------------|
| Train Score      | 99.30      | 79.89                 |
| Validation Score | 99.26      | 92.78                 |

## Conclusion

    1. Base CNN Model: 
       - Achieved high scores with 99.30% on training data and 99.26% on validation data.  
       - Indicates robust learning and good generalisation from the original MNIST sign language dataset as hardly any difference between training and   validation scores

    2. CNN Model with Augmentation: 
       - Showed reduced performance compared to the base CNN model, with training accuracy dropping to 79.89% and validation accuracy at 92.78%.
       -  Augmentation introduced variability, potentially leading to confusion.


Key Insights:
    CNN works by learning features from a given dataset and using the features to classify images. While this has proved to be the most effective method so far in terms of performance with augmented and non-augmented data, it would be interesting to asssess the performance of pre-defined models. 
    Pre-defined models are trained on a very large and diverse image dataset and are superior to CNNs as they are not limited to the data we provide and so are more likely to be more robust when classifying real world images.