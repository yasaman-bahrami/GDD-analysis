import numpy as np
import os
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
from getCSVData import getCSVData

list_t=[ 10, 12, 14, 16, 18] # Tbase values

    
def Main():
    key = 0
    for i in range(len(list_t)): # computing GDD for different values of Tbase
        GDD = []
        Path = os.getcwd()
        File = '{}/CSVData/St_JohnsGDDData.csv'.format(Path)
        Data, Date, mx, mn = getCSVData(File)
        Data['GDD' + str(i)] = (Data['Max Temp'] + Data['Min Temp']) / 2 - list_t[i]
        for j in Data['GDD' + str(i)]: # checking the values of GDD
            if j >= 0:
                key += j
            GDD.append(key)
        Data['GDD' + str(i)] = GDD

    
if __name__ == '__main__':
    Main()