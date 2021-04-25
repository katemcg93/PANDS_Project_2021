  #Author: Kate McGrath

# This code will carry out some initial analysis on the iris dataset 
#and output summaries on each variable to a text file

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

# to read in/manipulate file
import csv
# file creation exception handling
import os 


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

# Outputting descriptive statistics : mean, percentiles, max, min
# For whole dataset and each species to analyse differences between them
    descriptiveStats = irisDataSet.describe()

    descriptiveStatsVersicolor = versicolor.describe()

    descriptiveStatsVirginica = virginica.describe()

    descriptiveStatSetosa = setosa.describe()

#Calculating skewness and kurtosis to get better understanding of data distribution
#Is the data symmetrical and is it light/heavy tailed

    skew = irisDataSet.skew()
    kt = irisDataSet.kurt ()

#Writing results of output to summary text file
#First creating headings using = symbol to make file easier to read
   
    with open ("IrisDataSummary.txt", "a") as f:
        f.write("\n")
        f.write("\n")
        f.write("\tDescriptive Statistics")
        f.write("\n")
        f.write ("=" * 40)

        f.write("\n")
        f.write("\tOverall Data Set")
        f.write("\n")
        f.write("=" * 40)
        f.write("\n")
        f.write(str(descriptiveStats))

        f.write("\n")
        f.write("\n")
    
    #Putting species names into array so can use them as headings for descriptive stats

        speciesNames = ["Versicolor", "Virginica", "Setosa"]

        f.write("\n")
        f.write("\n")
        f.write("=" * 40)
        f.write("\n")
        f.write("\t {}:".format(speciesNames[0]))
        f.write("\n")
        f.write("=" * 40)
        f.write("\n")
        f.write(str(descriptiveStatsVersicolor))
        f.write("\n")

        f.write("\n")
        f.write("\n")
        f.write("=" * 40)
        f.write("\n")
        f.write("\t {}:".format(speciesNames[1]))
        f.write("\n")
        f.write("=" * 40)
        f.write("\n")
        f.write(str(descriptiveStatsVirginica))
        f.write("\n")

        f.write("\n")
        f.write("\n")
        f.write("=" * 40)
        f.write("\n")
        f.write("\t {}:".format(speciesNames[2]))
        f.write("\n")
        f.write("=" * 40)
        f.write("\n")
        f.write(str(descriptiveStatSetosa))
        f.write("\n")

        f.write("\n")
        f.write("\n")
        f.write("=" * 40)
        f.write("\n")
        f.write("\t Skewness")
        f.write("\n")
        f.write("=" * 40)
        f.write("\n")
        f.write(str(skew))
        f.write("\n")

        f.write("\n")
        f.write("\n")
        f.write("=" * 40)
        f.write("\n")
        f.write("\t Kurtosis")
        f.write("\n")
        f.write("=" * 40)
        f.write("\n")
        f.write(str(kt))

def outliers():

    #This function is to understand how many outliers are contained in the dataset
    #Outliers: where sample values are abnormally higher/lower than the range within which most of the population falls (the interquartile range)
    #Generally done in the early stages of data analysis as outliers can impact the accuracy of statistical tests
    #Outliers can be calculated by getting the interquartile range and adding 1.5 x IQR to Q3 and subtracting this figure from Q1
    #Any numbers outside these ranges are outliers (upper or lower bound)
    #This function calculates the IQR, detects outliers and identifies which variable they're from
    #It updates the text file with total outliers per variable

    def iqrange (df):
        Q1 = df.quantile(0.25)
        Q3 = df.quantile(0.75)
        IQR = Q3 - Q1

        outliers = (df < (Q1 - 1.5 * IQR)) |(df > (Q3 + 1.5 * IQR))
        totalOutliers = outliers.value_counts()
        return totalOutliers
    
    #The above test returns a count of outliers (True) and normal values (False). 
    #Below code converts the output to a dict, so can test later whether outliers, i.e. samples with a value of True are present 

    slOutliers = iqrange(sepalLength).to_dict()
    swOutliers = iqrange(sepalWidth).to_dict()
    plOutliers = iqrange(petalLength).to_dict()
    pwOutliers = iqrange(petalWidth).to_dict()

  #Function to detect whether outliers exist in the dataset for each variable, and if so, return the total outlier count with variable name
  # This will then be written to the text file
   
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
        f.write("=" * 40)
        f.write("\n")
        f.write("\t Outliers:")
        f.write("\n")
        f.write("=" * 40)
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

def createfile ():
    datasummary()
    descriptivestats()
    outliers ()

createfile ()


def histograms():
    sns.set(style = "white")
    sns.set(style = "ticks")

    plt.subplot(2,2,1)
    sns.histplot(irisDataSet, x = "Sepal Length", multiple = "stack", color = "#FCBCB8" )
    
    plt.subplot(2,2,2)
    sns.histplot(irisDataSet, x = "Sepal Width", multiple = "stack", color = "#A7E8BD")

    plt.subplot(2,2,3)
    sns.histplot(irisDataSet, x = "Petal Length", multiple = "stack", color = "#EFA7A7")

    plt.subplot(2,2,4)
    sns.histplot(irisDataSet, x = "Petal Width", multiple = "stack", color = "#C7EAE4")

    plt.suptitle("\t Data Distribution: All Species", size = 24, fontstyle = "oblique")
    plt.tight_layout()

    plt.savefig("histoverall.png")
    plt.close ()

    slh = sns.histplot(irisDataSet, x = "Sepal Length", element = "step", palette = "BuPu", hue = "Species")
    slh.set_title("Sepal Length Distribution by Species", fontsize = 20, pad = 20, va = "center", fontstyle = "oblique")
    plt.savefig("Sepal length.png")
    plt.close ()
    
    swh = sns.histplot(irisDataSet, x = "Sepal Width", element = "step", palette = "BuPu", hue = "Species")
    swh.set_title("Sepal Width Distribution by Species", fontsize = 20, pad = 20, va = "center", fontstyle = "oblique")
    plt.savefig("Sepal Width.png")
    plt.close ()


    plh = sns.histplot(irisDataSet, x = "Petal Length", element = "step", palette = "BuPu", hue = "Species")
    plh.set_title("Petal Length Distribution by Species", fontsize = 20, pad = 20, va = "center", fontstyle = "oblique")
    plt.savefig("Petal Length.png")
    plt.close()

    pwh = sns.histplot(irisDataSet, x = "Petal Width", element = "step", palette = "BuPu", hue = "Species")
    pwh.set_title("Petal Width Distribution by Species", fontsize = 20, pad = 20, va = "center", fontstyle = "oblique")
    plt.savefig("Petal Width.png")
    plt.close ()

histograms()

def normalitytest(df, t):

    #Converting data to numpy array for normality calculation
    swNumpy = df["Sepal Width"].to_numpy()
    pwNumpy = df["Petal Width"].to_numpy()
    slNumpy = df["Sepal Length"].to_numpy()
    plNumpy = df["Petal Length"].to_numpy()

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
            f.write("=" * 60)
            f.write("\n")
            f.write("\t Data Distribution : {}".format(t))
            f.write("\n")
            f.write("=" * 60)
            for key,value in pValuesVars.items():
                if value > 0.05:
                    f.write("\n {}: normally distributed (p = {})".format(key,round(value,2)))
                else:
                    f.write("\n {}: not normally distributed (p = {})".format(key,round(value),2))
    
    update_file()

normalitytest(irisDataSet, t = "Overall")
normalitytest(versicolor, t = "Versicolor")
normalitytest(virginica, t = "Virginica")
normalitytest(setosa, t = "Setosa")

def kde_plots (a,t):
    kdeplot = sns.kdeplot (data = irisDataSet, x = a, palette="Paired",hue = "Species", fill = True)
    kdeplot.set_title("{}".format(t), fontsize = 20, pad = 20, va = "center", fontstyle = "oblique")
    plt.savefig("{}.png".format(t))
    plt.close()

kde_plots (irisDataSet["Sepal Length"], t = "Sepal Length KDE")
kde_plots (irisDataSet["Sepal Width"],  t = "Sepal Width KDE")
kde_plots (irisDataSet["Petal Length"], t = "Petal Length KDE")
kde_plots (irisDataSet["Petal Width"], t = "Petal Width KDE")


def correlation ():
    def correlationMap (x, t, s):
        plt.figure()
        ax = plt.axes()
        corMap = sns.heatmap(x, annot = True, cmap = "mako")
        ax.set_title ("{}".format(t))
        ax.set_yticklabels(labels = corMap.get_yticklabels(), fontsize = "10", va = "center")
        plt.tight_layout()
        plt.savefig("{}".format(s))
        plt.close()
  

    overallCorrMap = correlationMap(irisDataSet.corr(method = "pearson"), t = "Correlation Map - All Species", s = "overall")
    versicolorCorrMap = correlationMap(versicolor.corr(method = "pearson"), t = "Correlation Map - Versicolor", s = "versicolor")
    virginicaCorrMap = correlationMap(virginica.corr(method = "pearson"), t = "Correlation Map - Virginica", s = "virginica" )
    setosaCorrMap = correlationMap(setosa.corr(method = "pearson"), t = "Correlation Map - Setosa", s = "setosa" )


correlation()

def scatterplots (a,b,x, t):
    scatterPlot = sns.scatterplot(data = irisDataSet, x=a, y=b, hue = "Species", style = "Species", s = 100, palette = "coolwarm")
    scatterPlot.set_title("{}".format(t), fontsize = 20, pad = 20, va = "center", fontstyle = "oblique")
    sns.despine ()
    plt.savefig("{}.png".format(x))
    #plt.show ()
    plt.close ()
    return scatterPlot

species_sw_pl = scatterplots(sepalWidth,petalLength, x = "sepalwdith_petallength", t = "Correlation: Sepal Width vs Petal Length")
species_pl_sw = scatterplots(petalLength,sepalWidth, x = "petallength_sepalwdith", t = "Correlation: Petal Length vs Sepal Width")
species_sw_pl = scatterplots(sepalWidth,sepalLength, x = "sepalwdith_sepallength", t = "Correlation: Sepal Width vs Sepal Length")
species_pl_sw = scatterplots(sepalLength,sepalWidth, x = "sepallength_sepalwdith", t = "Correlation: Sepal Length vs Sepal Width")
species_sw_pl = scatterplots(sepalWidth,petalLength, x = "sepalwdith_petallength", t = "Correlation: Sepal Width vs Petal Length")
species_pl_sw = scatterplots(petalLength,sepalLength, x = "petallength_sepalength",t = "Correlation: Petal Width vs Sepal Length")
species_sw_pl = scatterplots(petalWidth,petalLength, x = "petalwidth_petallength", t = "Correlation: Petal Width vs Petal Length" )
species_pl_sw = scatterplots(petalLength,petalWidth, x = "petallength_petalwidth", t = "Correlation: Petal Length vs Petal Width" )

def pairplot ():
    pairplot = sns.pairplot(irisDataSet, hue = "Species", palette = "coolwarm")
    plt.savefig("pairplot.png")
    plt.close()

pairplot()

def levenes_test(x, y):
    result = stats.levene(x,y)
    #print(result)
    if result[1] <0.05:
        return False
    else:
        return True
    
setVirgSW = levenes_test(setosa["Sepal Width"], virginica["Sepal Width"])
setVirgSL = levenes_test(setosa["Sepal Length"], virginica["Sepal Length"])
setVirgPW = levenes_test(setosa["Petal Width"], virginica["Petal Width"])
setVirgPL = levenes_test(setosa["Petal Length"], virginica["Petal Length"])
#print(setVirgPL,setVirgSL,setVirgSW,setVirgPW)

setVersSW = levenes_test(setosa["Sepal Width"], versicolor["Sepal Width"])
setVersSL = levenes_test(setosa["Sepal Length"], versicolor["Sepal Length"])
setVersPW = levenes_test(setosa["Petal Width"], versicolor["Petal Width"])
setVersPL = levenes_test(setosa["Petal Length"], versicolor["Petal Length"])
#print(setVersSW,setVersSL,setVersSW,setVersPW)

verVirgSW = levenes_test(virginica["Sepal Width"], versicolor["Sepal Width"])
verVirgSL = levenes_test(virginica["Sepal Length"], versicolor["Sepal Length"])
verVirgPW = levenes_test(virginica["Petal Width"], versicolor["Petal Width"])
verVirgPL = levenes_test(virginica["Petal Length"], versicolor["Petal Length"])
#print(verVirgSW,verVirgSL,verVirgPL,verVirgPW)

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



   




