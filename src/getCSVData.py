import os
import pandas as pd
import numpy as np
import pdb

""" This function gets a path and reads the result from CSV in CSV format
"""

def cleanCSV(gddData):
    Data = pd.DataFrame(gddData)
    Data.replace('', np.nan, inplace=True)
    Data = Data.dropna()
    Date, maxTemp, minTemp = np.array(Data['Date/Time']), np.array(Data['Max Temp']), np.array(Data['Min Temp'])
    return Data, Date, maxTemp, minTemp

def getCSVData(filePath):
    gddData = pd.read_csv(filePath, delimiter = ',' ,skiprows=0)
    Data, Date, maxTemp, minTemp = cleanCSV(gddData)
    return Data, Date, maxTemp, minTemp