#author Kate McGrath
#This file is an initial attempt at analysing and understanding data, probably won't make it into actual project

#import csv
#with open ("irisDataset.csv") as csv_file:
    #data_reader = csv.reader(csv_file, delimiter = ",")
    #for row in data_reader:
        #print (row)

import pandas as pd 
irisDataSet = pd.read_csv ("IrisDataSet.csv", index_col = "Class")
print("Sanity")
print(irisDataSet)