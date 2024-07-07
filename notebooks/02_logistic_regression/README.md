 SignLingual: Logistic Regression
---

## Overview

In this section, I will be building four Logistic Regression models:

1. Baseline Logistic Regression model:
    - Uses raw pixel values as features without any additional preprocessing.

2. Logistic Regression model with Feature Extraction (HOG/LBP)
    - Manually extracting features using Histogram of Oriented Gradients (HOG), Local Binary Patterns (LBP) and Colour Histograms before feeding them into the Logistic Regression model.

3. Baseline Logistic Regression model with Augmented Data
    - Same baseline model but now the model is trained on augmented versions of the original dataset,
    - Data augmentation includes variations of the original images such as rotation and horizontal flips to improve models generalisation.

4. Logistic Regression model with Feature Extraction and Augmetented Data
    - Combines feature extraction using HOG/LBP with training on augmented data.

## Data Collection

Using data collected from 01_data_processing, to get further details about the data please refer to README in data folder.

## Model Evaluation

**Without data augmentation:**

|                  | Logistic Regression Model  | Logistic Regression Model with Feature Extraction |
|------------------|----------------------------|---------------------------------------------------|
| Train Score      | 99.99                      | 99.03                                             |
| Validation Score | 99.99                      | 98.86                                             |

**With data augmentation:**

|                  | Logistic Regression Model  | Logistic Regression Model with Feature Extraction |
|------------------|----------------------------|---------------------------------------------------|
| Train Score      | 31.72                      | 48.11                                             |
| Validation Score | 25.82                      | 58.60                                             |


## Conclusion

1. Baseline Logistic Regression Model:

    - Without Augmentation: Both baseline model achieved high training and validation scores, indicating strong performance on the original dataset without overfitting.

    - With Augmentation: Performance significantly dropped for the baseline model, highlighting difficulties in generalisation with augmented data. 

2. Logistic Regression Model with Feature Extraction:

    - Without Augmentation: High performance demonstrating the effectiveness of HOG/LBP methods.
    
    - With Augmentation: Improved performance over the baseline model, indicating better handling of variability introduced by augmentation.
    
Key Findings:

Feature extraction methods like HOG and LBP provide the logistic regression with more meaningful features and so help the model generalise better.
Simpler models such as logistic regression struggle with augmented data however manually extracting features using HOG/LBP can help to an extent.


