# GMIT Higher Diploma in Data Anaytics
## Programming and Scripting Project 2021: Analysis of the Iris Flower Data Set
## Author
Kate McGrath
## Student ID
G00398908
## Submission Date
30/04/2021
## Introduction

This repository contains code to characterise and analyse the Iris Flower Data set, and output a summary text file and graphs highlighting key findings.
## Code and Modules/Libraries
The code associated with this project is written exclusively in Python, and was developed using the following software:</br>
  * Anaconda
  * Visual Studio Code
  * Cmder

The following libararies should be installed in order to run the code without issue:

```python
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    import sys
```

Additionally, the following standard python modules are leveraged in the code:

```python
    # to read in/manipulate file
    import csv
    # file creation exception handling
    import os 
```


## Overview of Iris Data Set

The Iris Data Set was first published in 1936, in a paper entitled “The use of multiple measurements in taxonomic problems”, which is recognized as a seminal work within the domain of pattern recognition literature [1]. The paper proposes a linear model to differentiate members of three species of iris plant, based on the shape Its author, Sir Ronald Fisher, was a celebrated statistician and geneticist. Other notable contributions made by Fisher to the field of statistics include the Fisher's Exact Test, which determines whether a non-random association exists between two categorical (grouping) variables and the analysis of variance (ANOVA) test, which is a method of determining whether the means of two or more groups differ significantly [2]. 

<p align="center">
  <img src="https://github.com/katemcg93/PANDS_Project_2021/blob/main/Fisher.PNG?raw=true" alt="Sir Ronald Fisher"/></br>
  <br></br>
  <br>
  </br>
 Figure 1: Sir Ronald Fisher. Source: Wikimedia Commons
</p>

The Iris Data Set consists of 50 samples from three species of Iris flower: Iris Versicolor, Iris Virgninica and Iris Setosa. </br>

For each sample, four data points have been recorded. These are: 
 - Sepal Width, in cm
 - Sepal Length, in cm
 - Petal Width, in cm
 - Petal Width, in cm
 
 <p align="center">
  <img src="https://github.com/katemcg93/PANDS_Project_2021/blob/main/Iris%20Plants.PNG" alt="Iris Flower Species"/></br>
  <br></br>
 Figure 2: Flower Species Described in Iris Data Set. Source: Kaggle.com
</p>

### Objectives of Project

This objective of this project is to characterize the iris data set, leveraging the many Python libraries that have been built for data analysis and visualization.

To organize my findings, I have identified three key research questions:

1. What are the key characteristics of the Iris Data Set?
2. Does any relationship, positive or negative, exist between the four variables?
3. Is there a significant difference in variable values between the three species?

The first question is answered using histograms, descriptive statistics, normality testing and the identification of outliers. The second is addressed using correlation heatmaps and scatter plots,to visually represent the degree to which the variables influence each other. The final question is addressed by comparing the mean value of each variable at the species level. 

## Part 1: Features of the Data Set
 


## References

1. Archive.ics.uci.edu. 2021. UCI Machine Learning Repository: Iris Data Set. [online] Available at: <https://archive.ics.uci.edu/ml/datasets/iris> [Accessed 24 April 2021].
2. Medium. 2021. The Iris Dataset — A Little Bit of History and Biology. [online] Available at: <https://towardsdatascience.com/the-iris-dataset-a-little-bit-of-history-and-biology-fb4812f5a7b5> [Accessed 24 April 2021].





