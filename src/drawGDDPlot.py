import numpy as np
import matplotlib.pyplot as plt
import argparse
import os
from getCSVData import getCSVData
import pdb

'''producing GDD plots for cities'''
def drawGDDPlot(gdd, cityName, gColor):
    #pdb.set_trace()
    rowLen = len(gdd)
    gdd_space=np.linspace(1, 12,rowLen)
    plt.subplot(1, 1, 1)
    plt.grid(True)
    plt.title('GDD plot')
    plt.plot(gdd_space, gdd, color=gColor, label = cityName)
    plt.legend(loc='upper right')
    ax=plt.gca()
    ax.set_xlabel('Months')
    ax.set_ylabel('GDD based on base_temp=10')
    return plt
    
def Main():
    # Taking the arguments from command line. 
    parser = argparse.ArgumentParser()
    parser.add_argument("-st", dest="stationId", nargs = '*', help="Please provide a list of station Id.")
    parser.add_argument("-ct", dest="cityName", nargs = '*', help="Please provide a list of city names corresponding to stations.")
    parser.add_argument("-gc", dest="gColor", nargs = '*', help="Please provide the colors for each city graph.")
	
    args = parser.parse_args()
	
    cityData = []
    for i in range(len(args.stationId)):
    	# Reading the data from downloaded .csv files. 
        CurrentPath = os.getcwd()
        FilePath= (CurrentPath+'/CSVData/'+args.cityName[i]+'GDDData.csv')
        Data, Date, maxTemp, minTemp = getCSVData(FilePath)
        cityData.append(Data['GDD'])
    
    for i in range(len(cityData)):
        gdd_plt = drawGDDPlot(cityData[i], args.cityName[i], args.gColor[i])
		
    gdd_plt.savefig("./plots/GDDPlotIMG.png")

if __name__ == '__main__':
    Main()
