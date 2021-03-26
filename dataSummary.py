#Author: Kate McGrath

# This code will carry out some initial analysis on the iris dataset 
#and output summaries on each variable to a text file

import pandas as pd
import numpy as np
import seaborn as sns
import csv
import os
import matplotlib.pyplot as plt

#Set everything to display 2 decimal places 
pd.set_option("display.precision", 2)

#Reading in the Iris Data Set file and adding column names
irisDataSet = pd.read_csv ("IrisDataSet.csv", sep = ",", names = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Species"])

#In the names file accompanying the dataset, some errors in the 35th and 38th rows were highlighted 
#Overwriting incorrect values for samples 35 and 38 

#Isolating the three species into own dataframes
versicolor = irisDataSet[irisDataSet["Species"]=="Iris-versicolor"]
setosa = irisDataSet[irisDataSet["Species"]=="Iris-setosa"]
virginica = irisDataSet[irisDataSet["Species"]=="Iris-setosa"]

def updateRows(irisDataSet):
    irisDataSet.at[34, "Petal Width"] = 0.2
    irisDataSet.at[37, "Sepal Width"] = 3.6
    irisDataSet.at[37, "Petal Length"] = 1.4
    return irisDataSet

updateRows(irisDataSet)

def dataSummary():
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
        f.write("\n")


def initialAnalysis ():
    #This function will carry out some high level analysis on the data
    overallMean = irisDataSet.mean()
    speciesMean = irisDataSet.groupby("Species").mean()

    overallStd = irisDataSet.std()
    speciesStd = irisDataSet.groupby("Species").std()

    
    overallCorr = irisDataSet.corr(method = "pearson")
    versicolorCorr = versicolor.corr(method = "pearson")
    virginicaCorr = virginica.corr(method = "pearson")
    setosaCorr = setosa.corr(method = "pearson")

    correlationMap = sns.heatmap(overallCorr, annot =True ,cmap = "mako")
    plt.show()

    correlationMapVersicolor = sns.heatmap(versicolorCorr, annot =True ,cmap = "mako")
    plt.show()

    correlationMapVirginica = sns.heatmap(virginicaCorr, annot =True ,cmap = "mako")
    plt.show()

    correlationMapSetosa = sns.heatmap(setosaCorr, annot =True ,cmap = "mako")
    plt.show()

    sns.histplot(irisDataSet, x = "Sepal Length", hue = "Species", multiple = "stack")
    plt.show()

    sns.histplot(irisDataSet, x = "Sepal Width", hue = "Species", multiple = "stack")
    plt.show()

    sns.histplot(irisDataSet, x = "Petal Length", hue = "Species", multiple = "stack")
    plt.show()

    sns.histplot(irisDataSet, x = "Petal Width", hue = "Species", multiple = "stack")
    plt.show()





    
      




dataSummary()
initialAnalysis()


