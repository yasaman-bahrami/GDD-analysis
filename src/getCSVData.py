import os
import pandas as pd
import numpy as np
import pdb



def getCSVData(filePath):
    try:
        gddData = pd.read_csv(filePath, delimiter = ',' ,skiprows=0)
    except:
        print("Oops! there is problem in reading data", gddData)

    Data = pd.DataFrame(gddData)
    Data.replace('', np.nan, inplace = True)
    Data = Data.dropna()
    rowLen = len(Data.index)
    # if (rowLen > 365):
    #     for i in range(rowLen - 365 - 1):
    #         csvData = csvData.drop(csvData.index[len(csvData) - 1])
    # elif (rowLen < 365):
    #     for i in range(365 - rowLen):
    #         csvData.append(csvData.tail(1), ignore_index=True)
    Index = Data.keys()
    Date, maxTemp, minTemp = np.array(Data['Date/Time']),np.array(Data['Max Temp']), np.array(Data['Min Temp'])

    return Data, Date, maxTemp, minTemp





