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

The Iris Data Set was first published in 1936, in a paper entitled “The use of multiple measurements in taxonomic problems”, which is recognized as a seminal work within the domain of pattern recognition literature [1]. The paper proposes a linear model to differentiate members of three species of iris plant, based on the shape. <br>
</br>
Its author, Sir Ronald Fisher, was a celebrated statistician and geneticist. Other notable contributions made by Fisher to the field of statistics include the Fisher's Exact Test, which determines whether a non-random association exists between two categorical (grouping) variables and the analysis of variance (ANOVA) test, which is a method of determining whether the means of two or more groups differ significantly [2]. 
<br>
</br>
<p align="center">
  <img src="https://github.com/katemcg93/PANDS_Project_2021/blob/main/Fisher.PNG?raw=true" alt="Sir Ronald Fisher"/></br>
 <br> 
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
 *Figure 2: Flower Species Described in Iris Data Set. Source: Kaggle.com
</p>

### Objectives of Project

This objective of this project is to characterize the iris data set, leveraging the many Python libraries that have been built for data analysis and visualization.

To organize my findings, I have identified three key research questions:

1. What are the key characteristics of the Iris Data Set?
2. Does any relationship, positive or negative, exist between the four variables?
3. Is there a significant difference in variable values between the three species?

The first question is answered using histograms, descriptive statistics, normality testing and the identification of outliers. The second is addressed using correlation heatmaps and scatter plots,to visually represent the degree to which the variables influence each other. The final question is addressed by comparing the mean value of each variable at the species level. 

## Part 1: Features of the Data Set

The first part of the analysis.py file reads the csv (comma delimited) file containing the data set, and assigns names to each column. This is needed so we can distinguish between the four numerical variables, and group the data by species during analysis. The csv data is converted into a Pandas data frame, to facilitate analysis. 

```python
irisDataSet = pd.read_csv ("IrisDataSet.csv", sep = ",", 
names = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Species"])
```
In the readme file accompanying the data set [1], errors on rows 35 and 38 are highlighted and the correct values are provided. Therefore, before carrying out any analysis on the data set a function is called to correct these errors and return an updated version of the data frame.

```python
def updaterows():
#In the names file accompanying the dataset, 
#some errors in the 35th and 38th rows were highlighted 
#Overwriting incorrect values for samples 35 and 38 

    irisDataSet.at[34, "Petal Width"] = 0.2
    irisDataSet.at[37, "Sepal Width"] = 3.6
    irisDataSet.at[37, "Petal Length"] = 1.4
    return irisDataSet

irisDataSet = updaterows()
```
The next part of the analysis focuses on extracting some initial high-level insights on the data and outputting these to a text file. The total rows and columns are obtained and isolated into their own variables so they can be used in the file. 

```python
def datasummary():
    #This is a function that will output a brief description of the dataset to a text file

    #Getting the rows and columns so can talk about number of samples/variables in dataset

    rowsAndColumns = irisDataSet.shape
    totalRows = rowsAndColumns[0]
    totalColumns = rowsAndColumns[1]
```
Once the variables required for the initial data description have all been declared, these are written to a text file. First the program will check if the file already exists, and if so it will be removed to prevent duplication of text. 

The next part of the program calculates descriptive statistics for the data set as a whole and for each of the three species, which were isolated into their own dataframes for this purpose. These are also written to the text file.

```python 
def descriptivestats ():

    descriptiveStats = irisDataSet.describe()
    descriptiveStatsVersicolor = versicolor.describe()
    descriptiveStatsVirginica = virginica.describe()
    descriptiveStatSetosa = setosa.describe()
````

To get a better understanding of the distribution and consistency of the data, the program calculates skewness, kurtosis, total outliers and normality for each variable. These are also outputted to the text file.

Skewness measures the symmetry of a data distribution, i.e. whether it is skewed to the left (negative) or right (positive) of the central peak. Kurtosis measures the extent to which the peak of a distribution distributes from the shape of a normal distribution. A positive kurtosis value indicates the data is heavy tailed (more data concentrated in the tails/periphery of the distribution), and conversely a positive value indicates a light tailed distribution (more data concentrated around the peak) [3][4][5]

Outliers are obtained by calculating the interquartile range (all data between the first and third quartile), multiplying this value by 1.5 and identifying all data outside of this range. Identifying outliers within the data set is a good practice as these can impact figures for mean and standard deviation, and in some cases may signify anomalies in the data that warrant further investigation. [6][7][8]

````python
    def iqrange (df):
        Q1 = df.quantile(0.25)
        Q3 = df.quantile(0.75)
        IQR = Q3 - Q1

        outliers = (df < (Q1 - 1.5 * IQR)) |(df > (Q3 + 1.5 * IQR))
        totalOutliers = outliers.value_counts()
        return totalOutliers
  ````
 

## References

1. Archive.ics.uci.edu. 2021. UCI Machine Learning Repository: Iris Data Set. [online] Available at: <https://archive.ics.uci.edu/ml/datasets/iris> [Accessed 24 April 2021].
2. Medium. 2021. The Iris Dataset — A Little Bit of History and Biology. [online] Available at: <https://towardsdatascience.com/the-iris-dataset-a-little-bit-of-history-and-biology-fb4812f5a7b5> [Accessed 24 April 2021].
3. Kolekar, P., 2021. Chapter 8 Descriptive statistics | BioSakshat - Free Study Materials. [online] Biosakshat.github.io. Available at: <https://biosakshat.github.io/descriptive-statistics.html> [Accessed 25 April 2021].
4. McNeese, B. and Barson, T., 2021. Are the Skewness and Kurtosis Useful Statistics?. [online] BPI Consulting. Available at: <https://www.spcforexcel.com/knowledge/basic-statistics/are-skewness-and-kurtosis-useful-statistics#:~:text=If%20the%20kurtosis%20is%20less%20than%20zero%2C%20then%20the%20distribution,the%20impact%20of%20sample%20size.> [Accessed 25 April 2021].
5. Itl.nist.gov. 2021. 1.3.5.11. Measures of Skewness and Kurtosis. [online] Available at: <https://www.itl.nist.gov/div898/handbook/eda/section3/eda35b.htm> [Accessed 25 April 2021].
6. GeeksforGeeks. 2021. Interquartile Range to Detect Outliers in Data - GeeksforGeeks. [online] Available at: <https://www.geeksforgeeks.org/interquartile-range-to-detect-outliers-in-data/> [Accessed 25 April 2021].
7. Singh, D. and Outliers, C., 2021. Cleaning up Data Outliers with Python | Pluralsight. [online] Pluralsight.com. Available at: <https://www.pluralsight.com/guides/cleaning-up-data-from-outliers> [Accessed 25 April 2021].
8. Medium. 2021. Hands-on : Outlier Detection and Treatment in Python Using 1.5 IQR rule. [online] Available at: <https://medium.com/@prashant.nair2050/hands-on-outlier-detection-and-treatment-in-python-using-1-5-iqr-rule-f9ff1961a414> [Accessed 25 April 2021].


