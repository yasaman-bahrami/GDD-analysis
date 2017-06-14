import os
import argparse
import numpy as np
import pandas as pd
import pdb
from saveCSVData import saveCSVData
'''
    In this file, we get data from the csv files we downloaded before and compute GDD and the 65
'''
def computeGDD(Data, baseTemp):  # Checking GDD values and Computing it.
    key = 0
    GDD = []
    dataMax = []
    dataMin = []
    for item in Data['Max Temp']:
        if item >30:
            item = 30
        dataMax.append(item)
    for item in Data['Min Temp']:
        if item < baseTemp:
            item = 10
        dataMin.append(item)
    Data['Max Temp'] = dataMax
    Data['Min Temp'] = dataMin
    Data['GDD'] = ((Data['Max Temp'] + Data['Min Temp']) / 2) - baseTemp
    for item in Data['GDD']:
        if item >= 0:
            key += item
        GDD.append(key)
    Data['GDD'] = GDD
    return Data

def readCleanCSV(cityName):
    filePath = os.getcwd() + '/CSVData/' + cityName + 'GDDData.csv'
    csvData = pd.read_csv(filePath, delimiter=',', skiprows=0)
    df = pd.DataFrame(csvData, columns=['Date/Time', 'Max Temp', 'Min Temp'])
    df.replace('', np.nan, inplace=True)
    df = df.dropna()
    return df,filePath

def Main():
    parser=argparse.ArgumentParser()
    parser.add_argument("baseTemp", type=int)
    parser.add_argument("-ct", dest="cityName", nargs='*')
    parser.add_argument("-st", dest="stationId", nargs='*')
    args=parser.parse_args()
    for i in range(len(args.stationId)):    # Read data from local csv files and clean it(by dropping rows with nan elements).
        df,filePath = readCleanCSV(args.cityName[i])
        GDDData = computeGDD(df, args.baseTemp)  # Calculate GDD
        saveCSVData(GDDData, filePath) # Save GDD data


if __name__ == '__main__':
    Main()
