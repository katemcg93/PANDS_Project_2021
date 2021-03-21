#Author: Kate McGrath

# This file will carry out some initial analysis on the iris dataset 
#and output summaries on each variable to a text file

import pandas as pd
import csv
import os

#Set everything to display 2 decimal places as default is 6, not required for this dataset
pd.set_option("display.precision", 2)

#Reading in the Iris Data Set file and adding column names
irisDataSet = pd.read_csv ("IrisDataSet.csv", sep = ",", names = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Species"])

#In the names file accompanying the dataset, some errors in the 35th and 38th rows were highlighted 
#and correct values were provided
#This code is to overwrite the incorrect values with the correct ones for index 34 and 37 of the dataset
def updateRows(irisDataSet):
    irisDataSet.at[34, "Petal Width"] = 0.2
    irisDataSet.at[37, "Sepal Width"] = 3.6
    irisDataSet.at[37, "Petal Length"] = 1.4
    return irisDataSet

updateRows(irisDataSet)


def summaryFile():
    #Will use
    rowsAndColumns = irisDataSet.shape

    totalRows = rowsAndColumns[0]
    totalColumns = rowsAndColumns[1]

    columnHeaders = irisDataSet.columns.values
    separator = ", "
    cleanHeaders = separator.join(columnHeaders[0:4])


    irisPlantSpecies = irisDataSet["Species"].unique()

    speciesList = list(irisPlantSpecies)
    separator = ", "
    cleanSpeciesList = separator.join(speciesList[0:2])

    irisPlantSpeciesCount  = len(irisPlantSpecies)

    #Getting count of samples within one of the species groups for output file
    #Because the sample count per species is the same in all groups can just take one of them
    #Otherwise would have to repeat below code for each species and store in a list
    samplePerSpecies = (irisDataSet["Species"] == "Iris-versicolor").sum()


    if os.path.exists("IrisDataSummary.txt"):  
        os.remove("IrisDataSummary.txt")

    else: 
        print("This file doesn't exist")

    with open ("IrisDataSummary.txt", "w") as f:
        f.write("This dataset contains a total of {} samples, with {} attributes used to describe them.".format(totalRows, totalColumns))
        f.write("\nThe attributes are as follows: {} and {}.".format(cleanHeaders, columnHeaders[-1]))
        f.write("\nThese samples are subdivided into one of {} species of iris plant. \nThese are: {} and {}.".format(irisPlantSpeciesCount, cleanSpeciesList, speciesList[-1]))
        f.write("\nEach species group contains a total of {} samples.".format(samplePerSpecies))

summaryFile()