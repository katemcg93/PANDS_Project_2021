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

    plt.suptitle("Data Distribution: All Species", size = 24, fontstyle = "oblique")
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