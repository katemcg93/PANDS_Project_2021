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




def normalitytest():
    swNumpy = irisDataSet["Sepal Width"].to_numpy()
    pwNumpy = irisDataSet["Petal Width"].to_numpy()
    slNumpy = irisDataSet["Sepal Length"].to_numpy()
    plNumpy = irisDataSet["Petal Length"].to_numpy()

    varList = [swNumpy,pwNumpy, slNumpy, plNumpy]
    varNames= ["Sepal Width", "Petal Width", "Sepal Length", "Petal Length"]
    normalDist = []
    pValues = []


    for var in varList :
        shapiro_test = stats.shapiro(var)
        normalDist.append(shapiro_test)

    for result in normalDist:
        pValues.append(result[1])
        print(pValues)
    
    pValuesVars = dict(zip(varNames, pValues))
    print(pValuesVars.values())

    for value in pValuesVars.values():
        print(type(value))
        if value < 0.05:
            print("True")
        else:
            print("False")

normalitytest()