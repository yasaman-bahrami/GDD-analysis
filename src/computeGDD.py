import os
import argparse
import numpy as np
import pandas as pd

'''
    In this file, we get data from the csv files we downloaded before and compute GDD and the 65
'''
def computeGDD(Data, baseTemp):  # Checking GDD values and Computing it.
    key = 0
    GDD = []
    Data['GDD'] = ((Data['Max Temp'] + Data['Min Temp']) / 2) - baseTemp
    for item in Data['GDD']:
        if item >= 0:
            key += item
        GDD.append(key)
    Data['GDD'] = GDD
    return Data

def Main():
    parser=argparse.ArgumentParser()
    parser.add_argument("baseTemp", type=int)
    parser.add_argument("-st", dest="stationId", nargs='*')
    parser.add_argument("-ct", dest="cityName", nargs='*')
    args=parser.parse_args()
    for i in range(len(args.stationId)):    # Read data from local csv files and clean it(by dropping rows with nan elements).
        filePath=os.getcwd()+'/CSVData/'+args.cityName[i] + 'GDDData.csv'
        csvData=pd.read_csv(filePath, delimiter=',', skiprows=0)
        Data=pd.DataFrame(csvData, columns=['Date/Time', 'Max Temp', 'Min Temp'])
        Data.replace('', np.nan, inplace=True)
        Data=Data.dropna()
        GDDData = computeGDD(Data, args.baseTemp)  # Calculate GDD


if __name__ == '__main__':
    Main()