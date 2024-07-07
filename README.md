## Sign-Lingual
=========================

### Executive Summary

As of today, there are over 300 different sign languages spoken by more than by more than 72 million deaf or hard-of-hearing people worldwide[1]. Despite sign language becoming a powerful tool for people of all hearing abilities to communicate with others, more can be done to promote inclusivity. My idea is to develop a machine learning sign language interpreter for ASL (American Sign Language) to bridge the gap between signers and non-signers. 

### Impact of Solution 
The main purpose of my project would be to break communication barriers between signers and non-signers thus increasing inclusivity and greater social connections. With a machine learning interpreter there would be less reliance on human translators at various events, schools, etc. This could lead to cost savings for deaf and hard-of-hearing people.

### Proposed Solution

In this project, I will use the following five approaches to tackle this problem and will conduct a comparison to see which model performs best:

    - Logistic Regression
    - Logistic Regression with Feature Extraction
    - Convolutional Neural Network (CNN)
    - VGG(16) [Tranfer Learning]
    - ResNet(50) [Tranfer Learning]

To begin my analysis I will use MNIST dataset which is clean dataset where every image is centered and there is little 'noise'. I will then augment this data using Keras to see how each model performs when noise is introduced. 

On building my models, I will attempt to uncover how each model 'learns' which features are key identifiers for specific classes (letters).

To conclude, I will assess the performance of each of these models using data from the real world.

### Dataset Description 
Working with two datasets:
    
    1. MNIST Sign Langauge dataset from openml
        - 1400 images for each letter in alphabet, there is no image data for letters j and z as they are moving sign (not image).

    2. Real World Images
        - Images I have captured using teachable machine

### Organization

#### Repository 

* `app`
    - streamlit python file used as a demo for my project
    - demo uses fine tuned VGG model to make predictions

* `data` 
    - contains link to copy of the dataset (stored in a publicly accessible Google Drive folder)

* `model`
    - pikled files of all models

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
        - Transfer Learning: Basic VGG 
                             Basic ResNet
                             VGG with data augmentation
                             ResNet with data augmentation   
                             Fine tuning of VGG
                             Fine tuning of ResNet
        - Model Evaluation: Include an evaluation of models on the real world dataset (apart from the transfer learning models)

* `docs`
    - contains final presenations of project
    - contains images of cnn and vgg architecture
    - contains project overview 

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

For more information on the data and models, please refer to the README in the data folder and model folder

### Credits & References

[1] https://education.nationalgeographic.org/resource/sign-language/

------------------------------------------------------------------------------