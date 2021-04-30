  #Author: Kate McGrath

# This code uses Python data analysis and visualization libraries to carry out exploratory analysis on the Iris Data Set
# The code outputs summaries of the four numerical variables to a text file with formatting
# It generates graphs on the distribution of data and correlation between variables
# It uses the independent sample t-test to determine whether the mean values for each of the variables differs significantly between species 
# The aim of this analysis is to describe the data set characteristics, look for correlation between variables 
# and determine degree to which the three iris species differ from each other in their morphology
# For discussion of the findings please refer to readme in repository

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import kurtosis

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
    kt = irisDataSet.kurtosis(axis = 0)

    print(kt)

#Writing results of output to summary text file
#First creating headings using = symbol to make file easier to read
#using \n to skip lines
   
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

#Converting Skewness and Kurtosis to string and writing them to text file
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
    #This function will provide a visualization of the above outlier calculation
    #As well as generating boxplots for dataset as a whole, also generating them for each species
    #this is to see if total outliers increases at species level, and for which species

    #Changing style of graph
    sns.set(style = "whitegrid")
    plt.figure(figsize = (14,12))

    #Generating subplots so boxplots will output on same figure
    plt.subplot(2,2,1)

    #Setting up box plot, x is the variable for which outliers are presented on x axis
    #Data is the data frame being passed to the plot, in this case the iris data set
    #Using hex colours as palettes don't allow different colours for individual subplots
    sl = sns.boxplot(x = "Sepal Length", data = irisDataSet, color = "#3dd178")
    
    #Formatting font for title, and removing X axis labels as they're redundant with title
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

    #Using tight layout to adjust padding between the plots
    plt.tight_layout (pad = 8.0)
    plt.savefig("Outliers Overall Dataset.png")
    plt.close ()


    #using palette rather than hex colours for species boxplots, will colour each of the three plots a different shade
    sns.set_palette("BuGn")

    #Making figure longer/wider to accomodate subplots 
    plt.figure(figsize = (24,16))

    plt.subplot(2,2,1)
    
    #This code is similar to boxplot generation for overall data set, except hue = "Species " added
    #This will create one boxplot per variable/species group
    
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

#Grouping functions to create file together
def createfile ():
    datasummary()
    descriptivestats()
    outliers ()

createfile ()


def histograms():
    #Resetting seaborn style to give white background for histogram and show ticks next to numbers on axis
    sns.set(style = "white")
    sns.set(style = "ticks")

    #Creating subplot of histograms for overall data set
    #Will be generating singular histograms broken down by species later in function
    plt.subplot(2,2,1)
    sns.histplot(irisDataSet, x = "Sepal Length", multiple = "stack", color = "#FCBCB8" )
    
    plt.subplot(2,2,2)
    sns.histplot(irisDataSet, x = "Sepal Width", multiple = "stack", color = "#A7E8BD")

    plt.subplot(2,2,3)
    sns.histplot(irisDataSet, x = "Petal Length", multiple = "stack", color = "#EFA7A7")

    plt.subplot(2,2,4)
    sns.histplot(irisDataSet, x = "Petal Width", multiple = "stack", color = "#C7EAE4")

    #Suptitle is to give the subplots one overall title in the centre of the figure
    plt.suptitle("\t Data Distribution: All Species", size = 24, fontstyle = "oblique")
    plt.tight_layout()

    plt.savefig("histoverall.png")
    plt.close ()

    #Generating histograms for same data set but separated by species
    #The first plot gives an overall impression of data distribution
    #These graphs will show how data is distributed for each species group
    #Using individual plots rather than subplots as there's too much detail contained in the hists for a supblot
    #Using step element rather than stack because of considerable overlap between species groups, esp for sepal measurements 
  
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

    #Using shapiro wilk test to calculate normality and appending  results to normal dist array
    for var in varList :
        shapiro_test = stats.shapiro(var)
        normalDist.append(shapiro_test)

    #Isolating p value into own list to output to text file
    for result in normalDist:
        pValues.append(result[1])

    #Creating dict and combining p results with the variable names
    # So when outputting to file can include name of variable and results for readability  
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

            #This code is dictating the output to the text file
            #If the shapiro wilk test yields a value of less than <.05 it's not normally distributed and vice versa
            # The loop examines each key/value pair in the pvaluesVars dictionary individually and outputs a line to the text file
            for key,value in pValuesVars.items():
                if value > 0.05:
                    f.write("\n {}: normally distributed (p = {})".format(key,round(value,2)))
                else:
                    f.write("\n {}: not normally distributed (p = {})".format(key,round(value),2))
    
    update_file()

#Calling normality test function and passing overall dataset and species values in turn
#t = title for text file
normalitytest(irisDataSet, t = "Overall")
normalitytest(versicolor, t = "Versicolor")
normalitytest(virginica, t = "Virginica")
normalitytest(setosa, t = "Setosa")

# KDE plots generated to accompany histograms
# These provide an understanding of how likley a random sample within the datset will have a given value
# Function to create KDE plot takes two arguments, a is the data to plot and t is the title
# Setting hue to species so probability distribution will be generated for each species

def kde_plots (a,t):
    kdeplot = sns.kdeplot (data = irisDataSet, x = a, palette="Paired",hue = "Species", fill = True)
    kdeplot.set_title("{}".format(t), fontsize = 20, pad = 20, va = "center", fontstyle = "oblique")
    plt.savefig("{}.png".format(t))
    plt.close()

kde_plots (irisDataSet["Sepal Length"], t = "Sepal Length KDE")
kde_plots (irisDataSet["Sepal Width"],  t = "Sepal Width KDE")
kde_plots (irisDataSet["Petal Length"], t = "Petal Length KDE")
kde_plots (irisDataSet["Petal Width"], t = "Petal Width KDE")


# Below function is generating heat maps to display correlation coefficients, obtained using Pearson's method, between the four variables
# Heatmaps are generated for data set as a whole as well as the three species groups
# The function takes three arguments
    # x is the data to plot (correlation coefficients)
    # T is the plot title
    # S is text to save the plot under

def correlation ():
    def correlationMap (x, t, s):
        plt.figure()
        # Calling axes so that tick labels can be added, to make the maps easier to interpret
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

#Below function is plotting each pair of variables against each other to graphically display the relationship between them
#If correlation is high, would expect that the scatteplot would resemble a line graph
#Separating the data by species to get an idea of both the overall relationship and the correlation between variables within species groups
#The function will output the scatterplots and also save them
#Function takes 4 arguments
    #a is the data to be plotted on x axis
    #b corresponds to y axis
    #x is the name to save the plot as
    #t is the title

def scatterplots (a,b,x, t):
    scatterPlot = sns.scatterplot(data = irisDataSet, x=a, y=b, hue = "Species", style = "Species", s = 100, palette = "coolwarm")
    scatterPlot.set_title("{}".format(t), fontsize = 20, pad = 20, va = "center", fontstyle = "oblique")
    sns.despine ()
    plt.savefig("{}.png".format(x))
    plt.show ()
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

# The pair plot outputs scatter plots for each pair of variables within sub plots
# This plot will be used in the readme rather than the individual scatter plots as it gives an instantaneous view of all variable pair relationships
def pairplot ():
    pairplot = sns.pairplot(irisDataSet, hue = "Species", palette = "coolwarm")
    plt.savefig("pairplot.png")
    plt.close()

pairplot()

# Last part of analysis is determining whether mean values for the numerical variables differ significantly between the species
# Independent samples t test (parametric) and mann whitney (non-parametric) tests are used to compare means
# Independent samples t test has two assumptions: normality and equal variance
# Levene's test is to determine whether or not the test should be run assuming equal variances
# Results from the normality testing earlier in the programme will be used to determine whether mann-whitney or independent samples test should be run


# Levene's test function takes two arguments
# x and y are the data sets to compare
# The test returns True if the p value is > 0.05 which means equal variances can be assumed
# Otherwise, the test returns false, must reject null hypothesis that variances are equal
def levenes_test(x, y):
    result = stats.levene(x,y)
    #print(result)
    if result[1] <0.05:
        return False
    else:
        return True
    
#Called function for each species/variable combination
#Printed returned values and used these to determine whether equal variances could be assumed

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

#This code will be run for pairs of variables where equal variances may be assumed
#Function takes two arguments, x, y and h, where x and y are the two data sets to be compared 
#and h is a heading to make the test output easier to interpret
#If p value is less than 0.05, the test result and "significant difference" is outputted to the console
# Otherwise "not significant" is outputted

def compare_means_ev (x,y,h):
    result = stats.ttest_ind(x, y)
    print("{}".format(h))
    print(result)
    if result [1] < 0.05:
        print("Significant difference")
    
    else:
        print("Not significant ")

#This code will be run for pairs of variables where Levene's test showed unequal variance
def compare_means_no_ev (x,y,h):
    result = stats.ttest_ind(x, y, equal_var=False)
    print("{}".format(h))
    print(result)
    if result [1] < 0.05:
        print("Significant difference")
    
    else:
        print("Not significant ")

#This code uses the mann whitney test and will be run for variables that don't follow a normal distribution, i.e. petal width variables
def compare_means_non_para (x,y, h):
    result = stats.mannwhitneyu(x, y)
    print("{}".format(h))
    print(result)
    if result [1] < 0.05:
        print("Significant difference")
    
    else:
        print("Not significant ")

    

sigSetVirgSW = compare_means_no_ev(setosa["Sepal Width"], virginica["Sepal Width"], h = "Virginica and Setosa - Sepal Width")
sigsetVirgSL = compare_means_no_ev(setosa["Sepal Length"], virginica["Sepal Length"], h = "Virginica and Setosa - Sepal Length")
sigsetVirgPW = compare_means_non_para(setosa["Petal Width"], virginica["Petal Width"], h = "Virginica and Setosa - Petal Width")
sigsetVirgPL = compare_means_no_ev(setosa["Petal Length"], virginica["Petal Length"], h = "Virginica and Setosa - Petal Length")

sigSetVersSW = compare_means_ev(setosa["Sepal Width"], versicolor["Sepal Width"], h = "Versicolor and Setosa - Sepal Width")
sigSetVersSL = compare_means_no_ev(setosa["Sepal Length"], versicolor["Sepal Length"], h = "Versicolor and Setosa - Sepal Length")
sigsetVersPW = compare_means_non_para(setosa["Petal Width"], versicolor["Petal Width"], h = "Versicolor and Setosa - Petal Width")
sigsetVersSPL= compare_means_no_ev(setosa["Petal Length"], versicolor["Petal Length"], h = "Versicolor and Setosa - Petal Length")

sigVerVirgSW = compare_means_ev(versicolor["Sepal Width"], virginica["Sepal Width"], h = "Virginica and Setosa - Sepal Width")
sigVerVirgSL = compare_means_ev(versicolor["Sepal Length"], virginica["Sepal Length"], h = "Virginica and Setosa - Sepal Length")
sigsVerVirgPW = compare_means_non_para(versicolor["Petal Width"], virginica["Petal Width"], h = "Virginica and Setosa - Petal Width")
sigsVerVirgPL = compare_means_no_ev(versicolor["Petal Length"], virginica["Petal Length"],h = "Virginica and Setosa - Petal Length" )



   




