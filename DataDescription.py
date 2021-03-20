#author Kate McGrath
#This file is an initial attempt at analysing and understanding data,  won't make it into actual project
#Committing it to show my early work on the project

import pandas as pd 

#Getting a feel for what dataset looks like, want to view all data while still getting to grips with it
#Returning data correct to two decimal places
pd.set_option("display.precision", 2)

irisDataSet = pd.read_csv ("IrisDataSet.csv")
print(irisDataSet.head())
print(irisDataSet.tail())

#Viewing descriptive statistics, although this doesn't tell us much without class data
print(irisDataSet.describe())

print(irisDataSet.shape)
print(irisDataSet.columns)

print(irisDataSet["Class"].value_counts())

print(irisDataSet.corr(method = "pearson"))