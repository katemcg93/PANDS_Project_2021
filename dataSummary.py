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
virginica = irisDataSet[irisDataSet["Species"]=="Iris-virginica"]

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
        f.write("Below are summaries of the four numerical variables broken down by species:")

        speciesNames = ["Versicolor", "Virginica", "Setosa"]

        f.write("\n")
        f.write("\n")
        f.write("\n {}:".format(speciesNames[0]))
        f.write(str(descriptiveStatsVersicolor))

        f.write("\n")
        f.write("\n")
        f.write("\n {}:".format(speciesNames[1]))
        f.write(str(descriptiveStatsVirginica))

        f.write("\n")
        f.write("\n")
        f.write("\n {}:".format(speciesNames[2]))
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

    print(overallMean, overallStd, speciesMean, speciesStd)

meanandstd()

def correlation ():
    def correlationMap (x):
        plt.figure()
        corMap = sns.heatmap(x, annot = True, cmap = "mako")
        plt.tight_layout()
        ax = plt.axes()
        ax.set_yticklabels(labels = corMap.get_yticklabels(), fontsize = "10", va = "center")
  

    overallCorrMap = correlationMap(irisDataSet.corr(method = "pearson"))
    ax = plt.axes()
    title = ax.set_title("Correlation Between Numerical Variables - All Species")
    plt.savefig("{} corr.png".format("overall"))
    plt.close()
  
    versicolorCorrMap = correlationMap(versicolor.corr(method = "pearson"))
    ax = plt.axes()
    title= ax.set_title("Correlation Between Numerical Variables - Versicolor")
    plt.savefig("{} corr.png".format("versicolor"))
    plt.close()

    virginicaCorrMap = correlationMap(virginica.corr(method = "pearson"))
    ax = plt.axes()
    title = ax.set_title("Correlation Between Numerical Variables - Virginica")
    plt.savefig("{} corr.png".format("virginica"))
    plt.close()

    setosaCorrMap = correlationMap(setosa.corr(method = "pearson"))
    ax = plt.axes()
    title = ax.set_title("Correlation Between Numerical Variables - Setosa")
    plt.savefig("{} corr.png".format("setosa"))
    plt.close()

correlation()

def scatterplots (a,b,x):
    scatterPlot = sns.scatterplot(data = irisDataSet, x=a, y=b, hue = "Species", style = "Species", s = 100, palette = "coolwarm")
    plt.savefig("{}.png".format(x))
    plt.show ()
    plt.close ()
    return scatterPlot

species_sw_pl = scatterplots(sepalWidth,petalLength, x = "sepalwdith_petallength")
species_pl_sw = scatterplots(petalLength,sepalWidth, x = "petallength_sepalwdith")
species_sw_pl = scatterplots(sepalWidth,sepalLength, x = "sepalwdith_sepallength")
species_pl_sw = scatterplots(sepalLength,sepalWidth, x = "sepallength_sepalwdith")
species_sw_pl = scatterplots(sepalWidth,petalLength, x = "sepalwdith_petallength")
species_sw_pl = scatterplots(sepalLength,petalLength, x = "sepallength_petallength")
species_pl_sw = scatterplots(petalLength,sepalLength, x = "petallength_sepalength")
species_sw_pl = scatterplots(petalWidth,petalLength, x = "petalwidth_petallength")
species_pl_sw = scatterplots(petalLength,petalWidth, x = "petallength_petalwidth")



def pairplot ():
    pairplot = sns.pairplot(irisDataSet, hue = "Species", palette = "coolwarm")
    plt.savefig("pairplot.png")
    plt.close()

pairplot()




def histvariables():

    def overallHist(a):
        plt.figure()
        sns.histplot(irisDataSet, x = a, multiple = "stack")
    

    slenHist = overallHist("Sepal Length")
    plt.savefig("Sepal_Length_Overall.png")
    plt.close()
    
    swidHist = overallHist("Sepal Width")
    plt.savefig("Sepal_Width_Overall.png")
    plt.close()

    plenHist = overallHist("Petal Length")
    plt.savefig ("Petal_Length_Overall.png")
    plt.close()

    pwidHist = overallHist("Petal Width")
    plt.savefig ("Petal_Width_Overall.png")
    plt.close()


    def histSpecies(a):
        plt.figure()
        sns.histplot(irisDataSet, x = a, hue = "Species", multiple = "stack")

       
    slenHistSpec = histSpecies("Sepal Length")
    plt.savefig("Sepal_Length_Species.png")
    plt.close()

    swidHistSpec = histSpecies("Sepal Width")
    plt.savefig("Sepal_Width_Species.png")
    plt.close()

    plenHistSpec = histSpecies("Petal Length")
    plt.savefig("Petal_Length_Species.png")
    plt.close()

    pwidHistSpec = histSpecies("Petal Width")
    plt.savefig("Petal_Width_Species.png")
    plt.close()

    
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


    def update_file ():

        with open ("IrisDataSummary.txt", "a") as f:
            f.write("\n")
            f.write("\n")
            f.write("Normality Testing using the Shapiro-Wilk method returned the following results: \n")
            for key,value in pValuesVars.items():
                if value > 0.05:
                    f.write("\n {}: normally distributed (p = {})".format(key,round(value,2)))
                else:
                    f.write("\n {}: not normally distributed (p = {})".format(key,round(value),2))
    
    update_file()

normalitytest()


def outliers():

    df= irisDataSet
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
    
    
    def boxplots ():
        
        sns.set(style = "whitegrid")
        plt.figure(figsize = (14,12))

        plt.subplot(2,2,1)

        sl = sns.boxplot(x = "Sepal Length", data = irisDataSet, color = "#3dd178")
        sl.set_title("Sepal Length", fontsize = 20, pad = 20, va = "center", fontstyle = "oblique")
        sl.set_xlabel(None)

        plt.subplot(2,2,2)
        
        sw = sns.boxplot(x = "Sepal Width", data = irisDataSet, color = "#31ded5")
        sw.set_title("Sepal Width", fontsize = 20, pad = 20, va = "center", fontstyle = "oblique")
        sw.set_xlabel(None)

        plt.subplot(2,2,3)

        pw = sns.boxplot(x = "Petal Width", data = irisDataSet, color = "#31ded5")
        pw.set_title("Petal Width", fontsize = 20, pad = 20, va = "center", fontstyle = "oblique")
        pw.set_xlabel(None)

        plt.subplot(2,2,4)

        pl = sns.boxplot(x = "Petal Length", data = irisDataSet, color = "#3dd178")
        pl.set_title("Petal Length", fontsize = 20, pad = 20, va = "center", fontstyle = "oblique")
        pl.set_xlabel(None)
        plt.tight_layout (pad = 8.0)
        plt.savefig("Outliers Overall Dataset.png")
        plt.close ()

        sns.set_palette("BuGn")

        plt.figure(figsize = (24,16))

        plt.subplot(2,2,1)

        ssl = sns.boxplot(x = "Species", y = "Sepal Length", data = irisDataSet, hue = "Species")
        ssl.set_title("Sepal Length", fontsize = 20, pad = 20, va = "center", fontstyle = "oblique")
        ssl.set_xlabel(None)

        plt.subplot(2,2,2)
        
        ssw = sns.boxplot(x = "Species", y = "Sepal Width", data = irisDataSet, hue = "Species")
        ssw.set_title("Sepal Width", fontsize = 20, pad = 20, va = "center", fontstyle = "oblique")
        ssw.set_xlabel(None)

        plt.subplot(2,2,3)

        spw = sns.boxplot(x = "Species", y  = "Petal Width", data = irisDataSet, hue = "Species", color = "#31ded5")
        spw.set_title("Petal Width", fontsize = 20, pad = 20, va = "center", fontstyle = "oblique")
        spw.set_xlabel(None)

        plt.subplot(2,2,4)

        spl = sns.boxplot(x = "Species", y = "Petal Length", data = irisDataSet, hue = "Species", color = "#3dd178")
        spl.set_title("Petal Length", fontsize = 20, pad = 20, va = "center", fontstyle = "oblique")
        spl.set_xlabel(None)

        plt.tight_layout (pad = 8.0)
        plt.savefig("Outliers by species.png")
        plt.close ()          

    boxplots()


outliers()

def kde_plots (a):
    sns.kdeplot (data = irisDataSet, x = a, palette="Paired",hue = "Species", fill = True)
    plt.show()
    plt.close()

kde_plots (irisDataSet["Sepal Length"])
kde_plots (irisDataSet["Sepal Width"])
kde_plots (irisDataSet["Petal Length"])
kde_plots (irisDataSet["Petal Width"])



def levenes_test(x, y):
    result = stats.levene(x,y)
    print(result)
    if result[1] <0.05:
        return False
    else:
        return True
    
setVirgSW = levenes_test(setosa["Sepal Width"], virginica["Sepal Width"])
setVirgSL = levenes_test(setosa["Sepal Length"], virginica["Sepal Length"])
setVirgPW = levenes_test(setosa["Petal Width"], virginica["Petal Width"])
setVirgPL = levenes_test(setosa["Petal Length"], virginica["Petal Length"])
print(setVirgPL,setVirgSL,setVirgSW,setVirgPW)

setVersSW = levenes_test(setosa["Sepal Width"], versicolor["Sepal Width"])
setVersSL = levenes_test(setosa["Sepal Length"], versicolor["Sepal Length"])
setVersPW = levenes_test(setosa["Petal Width"], versicolor["Petal Width"])
setVersPL = levenes_test(setosa["Petal Length"], versicolor["Petal Length"])
print(setVersSW,setVersSL,setVersSW,setVersPW)

verVirgSW = levenes_test(virginica["Sepal Width"], versicolor["Sepal Width"])
verVirgSL = levenes_test(virginica["Sepal Length"], versicolor["Sepal Length"])
verVirgPW = levenes_test(virginica["Petal Width"], versicolor["Petal Width"])
verVirgPL = levenes_test(virginica["Petal Length"], versicolor["Petal Length"])
print(verVirgSW,verVirgSL,verVirgPL,verVirgPW)

def compare_means_ev (x,y):
    result = stats.ttest_ind(x, y)
    print(result)
    if result [1] < 0.05:
        print("Significant difference")
    
    else:
        print("Not significant ")

def compare_means_no_ev (x,y):
    result = stats.ttest_ind(x, y, equal_var=False)
    print(result)
    if result [1] < 0.05:
        print("Significant difference")
    
    else:
        print("Not significant ")

    

sigSetVirgSW = compare_means_no_ev(setosa["Sepal Width"], virginica["Sepal Width"])
sigsetVirgSL = compare_means_no_ev(setosa["Sepal Length"], virginica["Sepal Length"])
sigsetVirgPW = compare_means_ev(setosa["Petal Width"], virginica["Petal Width"])
sigsetVirgPL = compare_means_no_ev(setosa["Petal Length"], virginica["Petal Length"])

sigSetVersSW = compare_means_ev(setosa["Sepal Width"], versicolor["Sepal Width"])
sigSetVersSL = compare_means_no_ev(setosa["Sepal Length"], versicolor["Sepal Length"])
sigsetVersPW = compare_means_ev(setosa["Petal Width"], versicolor["Petal Width"])
sigsetVersSPL= compare_means_no_ev(setosa["Petal Length"], versicolor["Petal Length"])

sigVerVirgSW = compare_means_ev(versicolor["Sepal Width"], virginica["Sepal Width"])
sigVerVirgSL = compare_means_ev(versicolor["Sepal Length"], virginica["Sepal Length"])
sigsVerVirgPW = compare_means_ev(versicolor["Petal Width"], virginica["Petal Width"])
sigsVerVirgPL = compare_means_no_ev(versicolor["Petal Length"], virginica["Petal Length"])




   




