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

#### Normality

The program uses the Shapiro Wilk method, which is included in the scipy stats module , to test whether the data is normally distributed[9]. If the result of the Shapiro Wilk test is less than 0.05, we can reject the null hypothesis, i.e. that the data is drawn from a normal distribution. The result of the test will dicate whether parametric or non-parametric statistical tests should be used to  analyze the data. 

````python
def normalitytest(df, t):

    #df is dataframe being passed to function
    # T is title for text file

    #Converting data to numpy array for normality calculation
    swNumpy = df["Sepal Width"].to_numpy()
    pwNumpy = df["Petal Width"].to_numpy()
    slNumpy = df["Sepal Length"].to_numpy()
    plNumpy = df["Petal Length"].to_numpy()

    varList = [swNumpy,pwNumpy, slNumpy, plNumpy]

    #Will need these lists to store test reults later in function
    normalDist = []
    pValues = []

    for var in varList :
        shapiro_test = stats.shapiro(var)
        normalDist.append(shapiro_test)

    #Isolating p value into own list to output to text file
    for result in normalDist:
        pValues.append(result[1])
 ````

#### Skewness and Kurtosis

Skewness measures the symmetry of a data distribution, i.e. whether it is skewed to the left (negative) or right (positive) of the central peak. Kurtosis measures the extent to which the peak of a distribution distributes from the shape of a normal distribution. A positive kurtosis value indicates the data is heavy tailed (more data concentrated in the tails/periphery of the distribution), and conversely a positive value indicates a light tailed distribution (more data concentrated around the peak) [3][4][5]. To calculate these, the program uses built in functions that are included in the scipy stats module.

#### IQR and Outliers

Outliers are obtained by calculating the interquartile range (all data between the first and third quartile), multiplying this value by 1.5 and identifying all data outside of this range. Identifying outliers within the data set is a good practice as these can impact figures for mean and standard deviation, and in some cases may signify anomalies in the data that warrant further investigation. [7][8][9]

````python
    def iqrange (df):
        Q1 = df.quantile(0.25)
        Q3 = df.quantile(0.75)
        IQR = Q3 - Q1

        outliers = (df < (Q1 - 1.5 * IQR)) |(df > (Q3 + 1.5 * IQR))
        totalOutliers = outliers.value_counts()
        return totalOutliers
  ````
  
#### Visual Representation of Data
The programme uses the Seaborn library to create visual representations of the above calculations.

Histograms provide a visual reporesentation of the data distribution, boxplots are used to display outliers within the data set and KDE (Kernel Density Estimate) plots are generated to illustrate the probability density functions for each variable (the probability that a random variable within the data set will equal a given value on the KDE curve). 

## Output/Interpretation of data

### Descriptive Statistics

The output from the descriptive statistics function is given below, for both the dataset and a whole and the individual species.

<details>
           <summary>Overall Data Set</summary>
           <p>

             Sepal Length  Sepal Width  Petal Length  Petal Width
    count        150.00       150.00        150.00       150.00
    mean           5.84         3.06          3.76         1.20
    std            0.83         0.44          1.77         0.76
    min            4.30         2.00          1.00         0.10
    25%            5.10         2.80          1.60         0.30
    50%            5.80         3.00          4.35         1.30
    75%            6.40         3.30          5.10         1.80
    max            7.90         4.40          6.90         2.50

</p>
</details>

<details>
           <summary>Versicolor</summary>
           <p>

       Sepal Length  Sepal Width  Petal Length  Petal Width
       count         50.00        50.00         50.00        50.00
       mean           5.94         2.77          4.26         1.33
       std            0.52         0.31          0.47         0.20
       min            4.90         2.00          3.00         1.00
       25%            5.60         2.52          4.00         1.20
       50%            5.90         2.80          4.35         1.30
       75%            6.30         3.00          4.60         1.50
       max            7.00         3.40          5.10         1.80
</p>
</details>

<details>
           <summary>Virginica</summary>
           <p>

               Sepal Length  Sepal Width  Petal Length  Petal Width
       count         50.00        50.00         50.00        50.00
       mean           6.59         2.97          5.55         2.03
       std            0.64         0.32          0.55         0.27
       min            4.90         2.20          4.50         1.40
       25%            6.22         2.80          5.10         1.80
       50%            6.50         3.00          5.55         2.00
       75%            6.90         3.18          5.88         2.30
       max            7.90         3.80          6.90         2.50
</p>
</details>

<details>
           <summary>Setosa</summary>
           <p>

              Sepal Length  Sepal Width  Petal Length  Petal Width
      count         50.00        50.00         50.00        50.00
      mean           5.01         3.42          1.46         0.24
      std            0.35         0.38          0.17         0.11
      min            4.30         2.30          1.00         0.10
      25%            4.80         3.12          1.40         0.20
      50%            5.00         3.40          1.50         0.20
      75%            5.20         3.68          1.58         0.30
      max            5.80         4.40          1.90         0.60

</p>
</details>

As may be expected, the range is wider in the data set as a whole than that at a species level. In particular, there is a difference of almost 7cm in the maximum and minimum values recorded for petal length, and the standard deviation for this variable is 1.77. When we look at the max and minimum values for this variable within each of the three species, the gap between them is considerably smaller, as is the standard deviation. This is also true of the other three variables, albeit to a lesser degree than petal length. This suggests that within the three species of iris plant, variable values are concentrated within a relatively narrow range.

The output for the three species gives a better understanding of how they differ from each other. For example, we can see that the Virginica plant has the highest average values for Sepal Length, Petal Width and Petal Length. Conversely, the setosa plant has the lowest values for petal length and width, but the highest value for sepal width. Additionally, we can see the three species differ more from each other in their petal measurements than sepal. This may suggest that it would be easier to classify iris plants based on the lengh/width of their petals than their sepals. [12]

### IQR and Outliers

The function for calculating the interquartile range/total outliers in the data set returned the following output:

<details>
           <summary>Outliers</summary>
           <p>

      Sepal Width: Total Outliers: 4
      Petal Width: No Outliers in data
      Sepal Length: No Outliers in data
      Petal Length: No Outliers in data

</p>
</details>

This is also supported by the boxplots generated to visually represent the IQR. 

 <p align="center">
  Figure 3: Outliers: Overall Data Set
  <img src="https://github.com/katemcg93/PANDS_Project_2021/blob/main/Outliers%20Overall%20Dataset.png"/></br>
  <br></br>
</p>

 <p align="center">
  Figure 4: Outliers per Variable/Species
  <img src="https://github.com/katemcg93/PANDS_Project_2021/blob/main/Outliers%20by%20species.png"/></br>
  <br></br>
</p>

Although the total outliers increases slightly when calculated per species, the figure still remains low (between 2 and 6% of recorded samples), and would be unlikely to skew the accuracy of statistical calculations [13]. The box plots also show a significant difference between setosa and the other two species in terms of petal measurements, and also that the range of values for these two variables is much narrower for the setosa plant. We can also see from the box plots that the three species have relatively similar median values for sepal width, which suggests that this would not be a suitable variable to classify plants into species groups [14]

### Skewness and Kurtosis
 
 The function for calculating skewness/kurtosis returned the following output:
 <details>
 <summary>Skewness</summary>
           <p>

            Sepal Length    0.31
            Sepal Width     0.32
            Petal Length   -0.27
            Petal Width    -0.10
            dtype: float64


</p>
</details>

<details>
           <summary>Kurtosis</summary>
           <p>

          Sepal Length   -0.55
          Sepal Width     0.23
          Petal Length   -1.40
          Petal Width    -1.34


</p>
</details>

The skewness values for each of the four variables is between -0.5 and 0.5 which indicates the data is relatively symmetrical. The petal length and width are slightly skewed to the left and the sepal measurements are skewed slightly to the right. The low values for petal length/width in the setosa species is likely causing the negative skew.

The kurtosis for sepal length and width are relatively low, suggesting the data is close to a normal distrubution. Conversely, the petal length/width variables have negative kurtosis values, indicating that they have less outliers than the normal distribution (light-tailed).

### Normality Testing
Normality for the data set as a whole and for each species returned the following output:

<details>
           <summary>Overall</summary>
           <p>

         Sepal Width: normally distributed (p = 0.1)
         Petal Width: not normally distributed (p = 0)
         Sepal Length: not normally distributed (p = 0)
         Petal Length: not normally distributed (p = 0)

</p>
</details>

<details>
           <summary>Versicolor</summary>
           <p>

          Sepal Width: normally distributed (p = 0.34)
          Petal Width: not normally distributed (p = 0)
          Sepal Length: normally distributed (p = 0.46)
          Petal Length: normally distributed (p = 0.16)

</p>
</details>


<details>
           <summary>Virginica</summary>
           <p>

        Sepal Width: normally distributed (p = 0.18)
        Petal Width: normally distributed (p = 0.09)
        Sepal Length: normally distributed (p = 0.26)
        Petal Length: normally distributed (p = 0.11)

</p>
</details>

<details>
           <summary>Setosa</summary>
           <p>

           Sepal Width: normally distributed (p = 0.2)
           Petal Width: not normally distributed (p = 0)
           Sepal Length: normally distributed (p = 0.46)
           Petal Length: normally distributed (p = 0.05)

</p>
</details>

When analyzed as a whole, three of the four variables do not follow a normal distribution. However, when separated by species the data is more likely to be normally distributed. An exception to this is petal length/width for the setosa plant. Petal width is not normally distributed ( = 0), and the p-value for petal length is p = 0.05, meaning we are close to also rejecting the null hypothesis for this variable.
 <p>
  <img src="https://github.com/katemcg93/PANDS_Project_2021/blob/main/histoverall.png"/></br>
  <br></br>
</p>


The sepal width/length distributions are much closer to normality than the petal measurements.

However, once delineated based on species group, the data is closer in appearance to a bell curve for each of the four variables. 

 <p>
  <img src="https://github.com/katemcg93/PANDS_Project_2021/blob/main/Petal%20Length.png"/></br>
  <br></br>
</p>


 <p>
  <img src="https://github.com/katemcg93/PANDS_Project_2021/blob/main/Petal%20Width.png"/></br>
  <br></br>
</p>


 <p>
  <img src="https://github.com/katemcg93/PANDS_Project_2021/blob/main/Sepal%20length.png"/></br>
  <br></br>
</p>


 <p>
  <img src="https://github.com/katemcg93/PANDS_Project_2021/blob/main/Sepal%20Width.png"/></br>
  <br></br>
</p>

Again, the exception to this is petal width/length for the setosa plant. Rather than following a bell curve distribution, the petal length/width values for this species are heavily concentrated within a narrow range of values. The petal width/length variables also seems to have less overlap between species than their sepal counterparts, again suggesting that plants could be more easily classified by their petal measurements. 


## KDE Plots

KDE plots were generated as an accompaniment to the histograms. The two plot types are very similar, but the KDE gives a clearer, less cluttered view of the data distribution curve for each of the three species simultaneously. The plot is interpreted as follows: the x axis represents recorded values for the variables, and plot (area under the curve), which must add up to 1, tells us the probability of seeing a variable at any point along the x axis [17].

 <p>
  <img src="https://github.com/katemcg93/PANDS_Project_2021/blob/main/Petal%20Length%20KDE.png"/></br>
  <br></br>
</p>

 <p>
  <img src="https://github.com/katemcg93/PANDS_Project_2021/blob/main/Petal%20Width%20KDE.png"/></br>
  <br></br>
</p>

For the petal width and length variables, we can see that the peak of the KDE curve is much higher in the setosa species than that of the virginica/versicolor plants, but the range of values is significantly narrower. Based on this curve, we can conclude it is highly probable that iris-setosa plants will have a sepal length of between 0 and 0.5 cm, with around 0.25 cm being the most probable value. In contrast, the virginica and versicolor plant curver have a more gradual peak, cover a wdider area and the probability density does not exceed 0.3 at any given point for either variable. As well as indicating that versicolor and virginica plants in general have longer petals, this plot also illustrates a greater range of values within these species.

 <p>
  <img src="https://github.com/katemcg93/PANDS_Project_2021/blob/main/Sepal%20Length%20KDE.png"/></br>
  <br></br>
</p>

 <p>
  <img src="https://github.com/katemcg93/PANDS_Project_2021/blob/main/Sepal%20Width%20KDE.png"/></br>
  <br></br>
</p>

The KDE plots for sepal length and width again show considerable overlap between the species. In particular, for sepal width the versicolor and virginica species have very similar curves. However, the setosa plant occupies notably higher values on the x axis, suggesting it would be easy to distinguish setosa based on sepal width but it would be difficult to classify virginica/versicolor plants based on this value.   We can again see a steeper, narrower curve for the setosa plant, suggesting less variety in sepal length values for this species, although it is much less pronounced than the petal length/width KDE plots. The lower peak KDE values for these plots suggests that the setosa plant has a greater range of values for sepal length and width. 

1. Archive.ics.uci.edu. 2021. UCI Machine Learning Repository: Iris Data Set. [online] Available at: <https://archive.ics.uci.edu/ml/datasets/iris> [Accessed 24 April 2021].
2. Medium. 2021. The Iris Dataset — A Little Bit of History and Biology. [online] Available at: <https://towardsdatascience.com/the-iris-dataset-a-little-bit-of-history-and-biology-fb4812f5a7b5> [Accessed 24 April 2021].
3. Kolekar, P., 2021. Chapter 8 Descriptive statistics | BioSakshat - Free Study Materials. [online] Biosakshat.github.io. Available at: <https://biosakshat.github.io/descriptive-statistics.html> [Accessed 25 April 2021].
4. McNeese, B. and Barson, T., 2021. Are the Skewness and Kurtosis Useful Statistics?. [online] BPI Consulting. Available at: <https://www.spcforexcel.com/knowledge/basic-statistics/are-skewness-and-kurtosis-useful-statistics#:~:text=If%20the%20kurtosis%20is%20less%20than%20zero%2C%20then%20the%20distribution,the%20impact%20of%20sample%20size.> [Accessed 25 April 2021].
5. Itl.nist.gov. 2021. 1.3.5.11. Measures of Skewness and Kurtosis. [online] Available at: <https://www.itl.nist.gov/div898/handbook/eda/section3/eda35b.htm> [Accessed 25 April 2021].
6. Brownlee, J., 2021. A Gentle Introduction to Normality Tests in Python. [online] Machine Learning Mastery. Available at: <https://machinelearningmastery.com/a-gentle-introduction-to-normality-tests-in-python/> [Accessed 25 April 2021].
7. GeeksforGeeks. 2021. Interquartile Range to Detect Outliers in Data - GeeksforGeeks. [online] Available at: <https://www.geeksforgeeks.org/interquartile-range-to-detect-outliers-in-data/> [Accessed 25 April 2021].
8. Singh, D. and Outliers, C., 2021. Cleaning up Data Outliers with Python | Pluralsight. [online] Pluralsight.com. Available at: <https://www.pluralsight.com/guides/cleaning-up-data-from-outliers> [Accessed 25 April 2021].
9. Medium. 2021. Hands-on : Outlier Detection and Treatment in Python Using 1.5 IQR rule. [online] Available at: <https://medium.com/@prashant.nair2050/hands-on-outlier-detection-and-treatment-in-python-using-1-5-iqr-rule-f9ff1961a414> [Accessed 25 April 2021].
10. Docs.scipy.org. 2021. scipy.stats.shapiro — SciPy v1.6.2 Reference Guide. [online] Available at: <https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.shapiro.html> [Accessed 25 April 2021].
11. Medium. 2021. Histograms and Density Plots in Python. [online] Available at: <https://towardsdatascience.com/histograms-and-density-plots-in-python-f6bda88f5ac0> [Accessed 26 April 2021].
12. Medium. 2021. Exploring Classifiers with Python Scikit-learn — Iris Dataset. [online] Available at: <https://towardsdatascience.com/exploring-classifiers-with-python-scikit-learn-iris-dataset-2bcb490d2e1b> [Accessed 26 April 2021].
13. Data Science Learner. 2021. How to Handle Outliers in Data Analysis ? Multivariate Outlier Detection. [online] Available at: <https://www.datasciencelearner.com/handle-outliers-multivariate-outlier-detection/> [Accessed 26 April 2021].
14. Medium. 2021. Exploratory Data Analysis: Uni-variate analysis of Iris Data set. [online] Available at: <https://medium.com/analytics-vidhya/exploratory-data-analysis-uni-variate-analysis-of-iris-data-set-690c87a5cd40> [Accessed 26 April 2021].
15. Medium. 2021. Skew and Kurtosis: 2 Important Statistics terms you need to know in Data Science. [online] Available at: <https://codeburst.io/2-important-statistics-terms-you-need-to-know-in-data-science-skewness-and-kurtosis-388fef94eeaa> [Accessed 27 April 2021].
16.  Seaborn.pydata.org. 2021. seaborn.kdeplot — seaborn 0.11.1 documentation. [online] Available at: <https://seaborn.pydata.org/generated/seaborn.kdeplot.html> [Accessed 27 April 2021].
17.  Medium. 2021. Histograms and Kernels Density Estimates. [online] Available at: <https://medium.com/@dcomp/histograms-and-kernels-density-estimates-a2c41eb08de3> [Accessed 27 April 2021].



