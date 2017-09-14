# deepLeaf
## Introduction
 - There are almost 0.5 million species of plant in the world
 - Identify the classes of species is very meaningful: Species population tracking and preservation, Plant-based medical research, Crop and food supply management.
 - One of Kaggle competition
 
## Problem Formulation
 - Input: A binary image of leaf
 - Output: The species of this leaf (out of 99 species)

## Dataset
### Training
 - 990 leaves (99 species, 10 samples/species)
 - For each leaf, pre-extracted features provided: Shape (64-attribute vector); Margin (64-attribute vector); Interior texture (64-attribute vector)
 - We split this set into training (0.8) and validation (0.2)

### Testing
 - 594 leaves (99 species, 6 samples/species)
 
## Classification
### Basic Idea
 - Train Deep Neural Network as a classifier
### Three Stages
 - 1. Use [images] only as training features
 - 2. Use [pre-extracted features] only
 - 3. Use [images, pre-extracted features]
#### Stage 1 [images]
 - Image Exploration:
 1. Rotation may confuse the classifier
 2. Scaling matters
 3. For some cases, image features are not strong from observation

 - Data Augmentation
 1. Resize it directly
 2. Pad first, then resize
 
### Implementation
#### Program
 - Keras
#### Loss Function
 - Categorical Cross Entropy
#### Training, validation accuracy
 - Percentage of correct prediction
 
### Stage 1 [images]
#### Our First Network Structure

 
## Autoencoder Feature Extraction
## Visualization
## Discussion

<p align="center">
<img src="http://i.imgur.com/cQ7tXaB.png">
Fig. test
</p>
