## Sign-Lingual
=========================

### Executive Summary

As of today, there are over 300 different sign languages spoken by more than by more than 72 million deaf or hard-of-hearing people worldwide[1]. Despite sign language becoming a powerful tool for people of all hearing abilities to communicate with others, more can be done to promote inclusivity. My idea is to develop a machine learning sign language interpreter for ASL (American Sign Language) to bridge the gap between signers and non-signers. 

### Impact of Solution 
The main purpose of my project would be to break communication barriers between signers and non-signers thus increasing inclusivity and greater social connections. With a machine learning interpreter there would be less reliance on human translators at various events, schools, etc. This could lead to cost savings for deaf and hard-of-hearing people.

### Proposed Solution

In this project, I will use the following three models to tackle this problem and will conduct a comparison to see which model performs best:

    - Logistic Regression
    - Logistic Regression with Feature Extraction
    - Convolutional Neural Network (CNN)

To begin my analysis I will use MNIST dataset which is clean dataset where every image is centered and there is little 'noise'. I will then augment this data using Keras to see how each model performs when noise is introduced. 

On building my models, I will attempt to uncover how each model 'learns' which features are key identifiers for specific classes (letters).
To conclude, I will assess the performance of each of these models and assess which letters the models misclassify the most and why. I will also identify which model handles data augmentation the best and see if these results differ from non-augmented data.

### Dataset Description 
1400 images for each letter in alphabet, there is no image data for letters j and z as they are moving sign (not image).

### Organization

#### Repository 

* `data` 
    - contains link to copy of the dataset (stored in a publicly accessible Google Drive folder)
    - saved copy of aggregated / processed data as long as those are not too large (> 10 MB)

* `model`
    - joblib dump of final model / model object

* `notebooks`
    - contains all final notebooks involved in the project
    - notebooks are broken up into sub folders:
        - data processing: Loading and processing of MNIST data
                           Data augmentation of MNIST data
        - logistic regression: Basic logistic regression model
                               Logistic regression model with feature extraction
                               Basic logistic regression model with data augmentation
                               Logistic regression model with feature extraction with data augmentation
        - CNN: Basic CNN model
               Basic CNN model with data augmentaion
        - Model Evaluation: Include an analysis of the models built (to be built at later date)
        - my files: to store pikl/kera/jpg objects

* `docs`
    - contains final report which summarises the project

* `references`
    - contains papers / tutorials used in the project

* `src`
    - Contains the project source code (refactored from the notebooks)

* `.gitignore`
    - Part of Git, includes files and folders to be ignored by Git version control

* `conda.yml`
    - Conda environment specification

* `Makefile`
    - Automation script for the project

* `README.md`
    - Project landing page (this page)

* `LICENSE`
    - Project license

#### Dataset

... Google Drive links to datasets and pickeled models

### Credits & References

[1] https://education.nationalgeographic.org/resource/sign-language/

------------------------------------------------------------------------------