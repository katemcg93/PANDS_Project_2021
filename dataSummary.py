#Author: Kate McGrath

# This code will carry out some initial analysis on the iris dataset 
#and output summaries on each variable to a text file

import pandas as pd
import numpy as np
import seaborn as sns
import csv
import os
import matplotlib.pyplot as plt
from scipy import stats

#Set everything to display 2 decimal places 
pd.set_option("display.precision", 2)

#Reading in the Iris Data Set file and adding column names
irisDataSet = pd.read_csv ("IrisDataSet.csv", sep = ",", names = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Species"])

varNames = ["Sepal Width", "Petal Width", "Sepal Length", "Petal Length"]

#Isolating the three species into own dataframes
versicolor = irisDataSet[irisDataSet["Species"]=="Iris-versicolor"]
setosa = irisDataSet[irisDataSet["Species"]=="Iris-setosa"]
virginica = irisDataSet[irisDataSet["Species"]=="Iris-setosa"]

#Isolating Variables into dataframes
sepalLength = irisDataSet["Sepal Length"]
sepalWidth = irisDataSet["Sepal Width"]
petalLength = irisDataSet["Petal Length"]
petalWidth = irisDataSet["Petal Width"]

irisDSSpecies = irisDataSet.groupby(["Species"])
spSepalLength = irisDSSpecies["Sepal Length"]
spSepalWidth = irisDSSpecies["Sepal Width"]
spPetalLength = irisDSSpecies["Petal Length"]
spPetalWidth = irisDSSpecies["Petal Width"]

def updaterows():
#In the names file accompanying the dataset, some errors in the 35th and 38th rows were highlighted 
#Overwriting incorrect values for samples 35 and 38 

    irisDataSet.at[34, "Petal Width"] = 0.2
    irisDataSet.at[37, "Sepal Width"] = 3.6
    irisDataSet.at[37, "Petal Length"] = 1.4
    return irisDataSet

irisDataSet = updaterows()

def datasummary():
    #This is a function that will output a brief description of the dataset to a text file

    #Getting the rows and columns so can talk about number of samples/variables in dataset

    rowsAndColumns = irisDataSet.shape
    totalRows = rowsAndColumns[0]
    totalColumns = rowsAndColumns[1]
 
    #Get list of variable names, without square brackets/commas, so they can be referenced in text file
    columnHeaders = irisDataSet.columns.values
    separator = ", "
    cleanHeaders = separator.join(columnHeaders[0:4])

    #Get list of plant species names and total species sampled, so can reference them in text file
    irisPlantSpecies = irisDataSet["Species"].unique()
    speciesList = list(irisPlantSpecies)
    separator = ", "
    cleanSpeciesList = separator.join(speciesList[0:2])
    irisPlantSpeciesCount  = len(irisPlantSpecies)

    #Getting count of samples within one of the species groups for output file
    #So number of samples per species can be referenced in output file
    #Because the sample count per species is the same in all groups can just take one of them

    samplePerSpecies = (irisDataSet["Species"] == "Iris-versicolor").sum()

    #If file already exists this will remove it, so not writing over existing file
    if os.path.exists("IrisDataSummary.txt"):  
        os.remove("IrisDataSummary.txt")

    else: 
        print("New Summary Text File Created")  

    with open ("IrisDataSummary.txt", "w") as f:
        f.write("This dataset contains a total of {} samples, with {} attributes used to describe them.".format(totalRows, totalColumns))
        f.write("\nThe attributes are as follows: {} and {}.".format(cleanHeaders, columnHeaders[-1]))
        
        f.write("\nThese samples are subdivided into one of {} species of iris plant. \nThese are: {} and {}.".format(irisPlantSpeciesCount, cleanSpeciesList, speciesList[-1]))
        f.write("\nEach species group contains a total of {} samples.".format(samplePerSpecies))
        
        f.write("\n")

def descriptivestats ():
    descriptiveStats = irisDataSet.describe()

    descriptiveStatsVersicolor = versicolor.describe()
    descriptiveStatsVirginica = virginica.describe()
    descriptiveStatSetosa = setosa.describe()

    with open ("IrisDataSummary.txt", "a") as f:
        f.write("\n")
        f.write("\n")
        f.write("Below is a summary of the characteristics of the Iris Data Set:")

        f.write("\n")
        f.write("\n")
        f.write(str(descriptiveStats))

        f.write("\n")
        f.write("\n")
        f.write("Below are summaries of the three numerical variables broken down by species:")

        speciesNames = ["Versicolor", "Virginica", "Setosa"]

        f.write("\n")
        f.write("\n")
        f.write("\n {} :".format(speciesNames[0]))
        f.write(str(descriptiveStatsVersicolor))

        f.write("\n")
        f.write("\n")
        f.write("\n {} :".format(speciesNames[1]))
        f.write(str(descriptiveStatsVirginica))

        f.write("\n")
        f.write("\n")
        f.write("\n {} :".format(speciesNames[2]))
        f.write(str(descriptiveStatSetosa))


def createfile ():
    datasummary()
    descriptivestats()

createfile ()

def meanandstd ():

    overallMean = irisDataSet.mean()
    speciesMean = irisDataSet.groupby("Species").mean()

    overallStd = irisDataSet.std()
    speciesStd = irisDataSet.groupby("Species").std()


meanandstd()

def correlation ():

    def correlationMap (x):
        sns.heatmap(x, annot = True, cmap = "mako")
        plt.show()
    
    overallCorrMap = correlationMap(irisDataSet.corr(method = "pearson"))
    versicolorCorrMap = correlationMap(versicolor.corr(method = "pearson"))
    virginicaCorrMap = correlationMap(virginica.corr(method = "pearson"))
    setosaCorrMap = correlationMap(setosa.corr(method = "pearson"))

correlation()

def histvariables():

    def overallHist(a):
        sns.histplot(irisDataSet, x = a, multiple = "stack")
        plt. show()

    slenHist = overallHist("Sepal Length")
    swidHist = overallHist("Sepal Width")
    plenHist = overallHist("Petal Length")
    pwidHist = overallHist("Petal Width")

    def histSpecies(a,):
        sns.histplot(irisDataSet, x = a, hue = "Species", multiple = "stack")

        plt.show()

    slenHistSpec = histSpecies("Sepal Length")
    swidHistSpec = histSpecies("Sepal Width")
    plenHistSpec = histSpecies("Petal Length")
    pwidHistSpec = histSpecies("Petal Width")

    print(type(slenHistSpec))

    return

histvariables()

def normalitytest():

    swNumpy = irisDataSet["Sepal Width"].to_numpy()
    pwNumpy = irisDataSet["Petal Width"].to_numpy()
    slNumpy = irisDataSet["Sepal Length"].to_numpy()
    plNumpy = irisDataSet["Petal Length"].to_numpy()


    varList = [swNumpy,pwNumpy, slNumpy, plNumpy]
    normalDist = []
    pValues = []

    for var in varList :
        shapiro_test = stats.shapiro(var)
        normalDist.append(shapiro_test)

    for result in normalDist:
        pValues.append(result[1])
        
    pValuesVars = dict(zip(varNames, pValues))

    with open ("IrisDataSummary.txt", "a") as f:
        f.write("\n")
        f.write("\n")
        f.write("Normality Testing using the Shapiro-Wilk method returned the following results: \n")
        for key,value in pValuesVars.items():
            if value > 0.05:
                f.write("\n {}: normally distributed (p = {})".format(key,round(value,2)))
            else:
                f.write("\n {}: not normally distributed (p = {})".format(key,round(value),2))

normalitytest()


def outliers():

    def iqrange (df):
        Q1 = df.quantile(0.25)
        Q3 = df.quantile(0.75)
        IQR = Q3 - Q1

        outliers = (df < (Q1 - 1.5 * IQR)) |(df > (Q3 + 1.5 * IQR))
        totalOutliers = outliers.value_counts()
        return totalOutliers
      
    slOutliers = iqrange(sepalLength).to_dict()
    swOutliers = iqrange(sepalWidth).to_dict()
    plOutliers = iqrange(petalLength).to_dict()
    pwOutliers = iqrange(petalWidth).to_dict()

    def testOutliers(key,dict):
        if key in dict:
            return ("Total Outliers: {}".format (dict[key]))
        else:
            return ("No Outliers in data")

    slOutlierText = testOutliers(True, slOutliers)
    swOutlierText = testOutliers(True, swOutliers)
    plOutlierText = testOutliers(True, plOutliers)
    pwOutlierText = testOutliers(True, pwOutliers)

   
    with open ("IrisDataSummary.txt", "a") as f:
        f.write("\n")
        f.write("\n")
        f.write("Outlier testing for each variable returned the following results:")
        f.write("\n")
        f.write("\n {}: {}".format(varNames[0], swOutlierText))
        f.write("\n {}: {}".format(varNames[1], pwOutlierText))
        f.write("\n {}: {}".format(varNames[2], slOutlierText))
        f.write("\n {}: {}".format(varNames[3], pwOutlierText))

outliers()






