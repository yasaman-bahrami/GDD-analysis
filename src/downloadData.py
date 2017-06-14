import os
import wget
import argparse
import numpy as np
import pandas as pd
from saveCSVData import saveCSVData
import pdb

""" If there is no errors, this function will download and then save a csv file 
    that has the required columns for our further computation and plots.
"""


# Read csv file
def cleanData(cityData):
    cols = cityData.columns.values
    for i in range(0, len(cols)):
        if "Max Temp (" in cols[i]:
            cols[i] = "Max Temp"
        if "Min Temp (" in cols[i]:
            cols[i] = "Min Temp"
    return cols


def downloadData(startYear, endYear, stationId, cityName):
    while (startYear <= endYear):
        originUrl = 'http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID='
        url = originUrl + str(stationId) + '&Year=' + str(
            startYear) + '&Month=12&Day=31&timeframe=2&submit= Download+Data'
        fileName = wget.download(url)  # Download daily historical temperature data for several cities automatically
        cityData = pd.read_csv(fileName, encoding='ISO-8859-1', delimiter=',', skiprows=25)
        cityData.columns = cleanData(cityData)
        csvData = pd.DataFrame(cityData, columns=['Date/Time', 'Max Temp', 'Min Temp'])
        csvData.replace('', np.nan, inplace=True)
        csvData = csvData.dropna()
        filePath = (os.getcwd() + '/CSVData/' + cityName + 'GDDData.csv')
        startYear += 1
        saveCSVData(csvData, filePath)
        os.remove(fileName)


def Main():
    # Getting arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("startYear", type=int)
    parser.add_argument("endYear", type=int)
    parser.add_argument("-st", dest="stationId", nargs='*')
    parser.add_argument("-ct", dest="cityName", nargs='*')
    args = parser.parse_args()
    lenStation = len(args.stationId)
    i = 0
    while (i < lenStation):
        downloadData(args.startYear, args.endYear, args.stationId[i], args.cityName[i])
        i += 1


if __name__ == '__main__':
    Main()
