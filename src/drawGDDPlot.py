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
    
