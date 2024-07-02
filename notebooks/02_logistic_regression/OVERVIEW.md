# SignLingual: Action Plan

### Contents

1. [Overview](#overview)
2. [Methodology](#methodology)
3. [Data Collection](#data-collection)
4. [Data Preprocessing](#data-preprocessing)
5. [Model Development](#model-development)
6. [Model Evaluation](#model-evaluation)
7. [Deployment](#deployment)
8. [Future Work](#future-work)
9. [Conclusion](#conclusion)

---

## Overview

This README outlines the action plan for building a machine learning translator for MNIST ASL dataset.

## Outline

In this project I will focus on building the following models:

 - Logistic Regression Models
 - Convolutional Neural Network (CNN)
 - Transfer learning usifn ResNet50 and VGG16

1. Logisitc Regression

    - Begin by building a baseline Logistic Regression model using pixel intensities from the MNIST data to be my fetaures
    - Utilise feature extrraction techniques such as HOG, LBP and Colour Histograms to create feature vectors for each image
    - Develop a Logistic Regression Model based on these feature vectors
    - Use data augmentation techniques to assess the ability for both Logistic Regression models to generalise to 'real' data

2. Convolutional Neural Network (CNN)

    - Build a CNN using Fucntional API
    - Extract weights and feature map for each convoluted layer to gain some insight as to what the network is learning
    - Use data augmentation techniques to assess the ability for CNN to generalise to 'real' data

3. Transfer Learning 

    - Utilsie VGG16 and ResNet50 by first assessing the accuracy of these pre-trained models on the MNIST dataset as is
    - Assess performance when data is augmented
    - Perform fine-tuning on dataset which I capture using Teachable Machine

## Data Collection
          

    

## Data Preprocessing



## Model Development



## Model Evaluation



## Deployment



## Future Work



## Conclusion


