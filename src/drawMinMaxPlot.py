import numpy as np
import matplotlib.pyplot as plt
import argparse
import os
from getCSVData import getCSVData
""" producing MIN/MAX plots for the city as input"""

def savePlot(stationId, cityName):
    for i in range(len(stationId)):    #draw min and max plots base on ongoing path
        FL_Path= (os.getcwd()+'/CSVData/'+cityName[i]+'GDDData.csv')
        Data, Date, maxTemp, minTemp = getCSVData(FL_Path)
        Max_Min_Plot = drawMinMaxPlot(minTemp, maxTemp, cityName[i])
        Max_Min_Plot.savefig("./plots/minMaxPlot"+str(cityName[i])+".png")
        Max_Min_Plot.clf()

'''The main function of drawing plot'''
def drawMinMaxPlot(mn, mx, cityName):
    plt.subplot(1,1,1)
    mnLen = len(mn)
    mxLen = len(mx)
    X = np.linspace(1, mnLen, mnLen)
    Y = np.linspace(1, mxLen, mxLen)
    plt.grid(True)
    plt.plot(X, mn, color="blue", label="Min Temperature")
    plt.plot(Y, mx, color="red", label="Max Temperature")
    plt.legend(loc='upper right')
    ax = plt.gca()
    ax.set_axis_bgcolor('yellow')
    ax.set_xlabel('Days', fontsize=11)
    ax.set_ylabel('Temperature', fontsize=11)
    plt.title('Min and Max plot for '+cityName, color="black", fontsize=14)
    return plt

'''----------------------------Main--------------------------------------------'''
def Main():
    parser = argparse.ArgumentParser()     # checking
    parser.add_argument("-st", dest="stationId", nargs = '*')
    parser.add_argument("-ct", dest="cityName", nargs = '*')
    parser.add_argument("-dmm", dest="dmmColor", nargs = '*')
    args = parser.parse_args()
    savePlot(args.stationId, args.cityName)


if __name__ == '__main__':
    Main()
